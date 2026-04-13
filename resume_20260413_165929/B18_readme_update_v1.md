# B18_readme_update_v1 (376s)

Updated [README.md](/Users/raeez/chiral-bar-cobar/README.md).

- `FIXED` 1. Page count: `2,617`, taken from `main.pdf` (`pdfinfo`; modified April 13, 2026).
- `FIXED` 2. Test count: `125,444 collected (124,511 active; 933 deselected)`, from the requested `python3 -m pytest compute/tests/ --co -q`.
- `FIXED` 3. Theorem status summary: the README table now follows `chapters/connections/concordance.tex`, with `A/B/D/H` marked proved here, `C0/C1` proved here, and `C2` conditional; I also added a scope sentence so the summary does not outrun the chapter hypotheses.
- `FIXED` 4. Overclaims: removed the old `MC1`-`MC5 are proved` surface, corrected the object-summary block to the canonical five objects, replaced stale status metrics with grounded ones, corrected the Koszulness-programme tally to `9 unconditional + 1 proved consequence + 1 conditional + 1 one-directional`, and updated the test/build comments plus tree counts to match the live repo.

Verification: stale-pattern grep on `README.md` returned no matches; banned-prose grep returned no matches; `README.md` has no `\ref{}` or `\label{}` surface to validate. I did not run a fresh TeX build or execute the tests themselves; I only inspected the last built PDF and collected pytest items.


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
session id: 019d87dd-ad51-7562-bea9-9048807b1ed1
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


TARGET: README.md (Vol I)
Read the current README. Update:
1. Page count (check from last build)
2. Test count (run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ --co -q 2>&1 | tail -1)
3. Theorem status summary (from concordance)
4. Ensure no claims exceed what's proved
Do NOT inflate scope.
mcp startup: no servers


thinking
**Considering the use of explorers**

I see that I can use parallel execution for file reads, as the developer prefers multi_tool_use.parallel. I might need to use explorer agents, especially for codebase questions. However, this is a simple task of editing the README. The instructions emphasize trusting explorers without verification. Since the user is asking to modify the README, it might make sense to use an explorer agent to inspect it directly, although I’m weighing if that's necessary or too much.
thinking
**Balancing explorers and personal reading**

I can still utilize the explorer to gather context from the necessary files, but I should also read them myself. I think I should rely on the explorer to identify relevant sections in the README and summarize the theorem status. However, the instructions say I must personally read certain source files before making any significant edits. So, maybe I can combine using the explorer for summaries while I read the required files myself to ensure accuracy.
codex
Using `claim-surface-sync` and `build-surface` for this pass because the README touches theorem-status claims and build/test-derived counts. I’m reading the required repo surfaces first, then I’ll pull the current build/test numbers and make a tightly scoped README edit.
exec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
 succeeded in 51ms:
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
codex
I’ve loaded the relevant skill instructions. Next I’m reading the required source surfaces and locating the live README claims that need to be narrowed or updated against the concordance and current build artifacts.
exec
/bin/zsh -lc "sed -n '1,260p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git status --short README.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,260p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,260p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' README.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 50ms:
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
 M README.md
 succeeded in 50ms:
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
# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

| Theorem | Statement | Status |
|:-------:|-----------|--------|
| **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |

thinking
**Inspecting README changes**

I need to check the modifications made to the README file carefully to avoid overwriting the user's changes. I think running a `git diff` on the README.md will let me see the differences between the current modified state and HEAD. It’s essential to inspect the diff to ensure I'm aware of what's been changed and to protect those user modifications that I don’t want to disrupt.
codex
`README.md` is already dirty in the worktree, so I’m checking the current delta before editing. I need to preserve any unrelated user changes while tightening only the status/count claims that this task targets.
exec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/README.md b/README.md
index f7544ca..986ea94 100644
--- a/README.md
+++ b/README.md
@@ -15,15 +15,15 @@ The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassoci
 
 ## Five Main Theorems
 
-| Theorem | Statement |
-|:-------:|-----------|
-| **(A)** | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
-| **(B)** | Bar-cobar inversion: quasi-isomorphism on the Koszul locus |
-| **(C)** | Complementarity: deformations of A and obstructions of A^! are Lagrangian complements |
-| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g at all genera (uniform-weight lane) |
-| **(H)** | Hochschild duality: ChirHoch*(A) polynomial, Koszul-functorial |
+| Theorem | Statement | Status |
+|:-------:|-----------|--------|
+| **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
+| **(B)** | Strict bar-cobar inversion on the Koszul locus; coderived/coacyclic refinement off the locus | Proved here |
+| **(C)** | Complementarity package: C0/C1 are proved; the shifted-symplectic/BV upgrade C2 is conditional | C0/C1 proved here; C2 conditional |



thinking
**Updating page and theorem counts**

I need to update the page count from the last build and check the test count using a command. The README file has possibly been altered before, so I must verify if the page count is actually 2745 from the PDF. The theorem summary might need more nuance, especially regarding claims made about the “Six-Object Web.” I need to ensure I’m not overstating anything and carefully examine the README for any other unproven claims. This is critical since the user requests accurate details on the theorem status.
thinking
**Reviewing claims and gathering data**

I might need to narrow down claims related to Shadow Depth Classification. There's a statement about L/C terminating at 3/4, but I'm unsure if that's true. The README mentions that L terminates at 3 and C at 4, so I need to verify whether these claims are actually proven. The user specifically asks me to check the README and ensure no claims exceed what's supported, so I should be cautious. I'll also gather the latest page count and test count from the last build by checking the PDF and any existing build artifacts.
thinking
**Checking theorem status and README**

I should summarize the theorem statuses from the concordance, focusing on the details as presented in the table. The README mentions "Five Main Theorems" with their statuses, which appears mostly aligned. I might need to add references indicating which theorems are proved or conditional. For example, D should clarify it's only on the proved uniform-weight lane, while genus 1 should cover all families. I'll also check if theorem A includes D_Ran interplay and the algebra-level Verdier, ensuring it aligns with D_Ran.
codex
I’ve confirmed the README already has a pending theorem-status rewrite, but the numeric claims still need to be grounded. Next I’m pulling the actual test collection count and the current built PDF page count, then I’ll tighten any remaining README wording that still overclaims beyond concordance.
exec
/bin/zsh -lc 'rg -n "Pages|Compute tests|Five Main Theorems|Status|BV/BRST|MC1|MC2|MC3|MC4|MC5|proved here|conditional|conjectural" README.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files -g 'main.pdf' -g '*.pdf' ." in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
16:## Five Main Theorems
18:| Theorem | Statement | Status |
22:| **(C)** | Complementarity package: C0/C1 are proved; the shifted-symplectic/BV upgrade C2 is conditional | C0/C1 proved here; C2 conditional |
26:The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
45:## Status
49:| Pages | 2,745 |
52:| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
59:| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
83:- **Part IV** (Physics Bridges): Feynman, BV/BRST, E_n, Langlands (YM/HT content migrated to Vol II)
85:- **Part VI** (The Frontier): conditional extensions, conjectural outlook
 succeeded in 51ms:
./introduction_full_survey.pdf
./survey_modular_koszul_duality.pdf
./test_concordance.pdf
./w3_holographic_datum.pdf
./bp_self_duality.pdf
./N2_mc3_all_types.pdf
./survey_modular_koszul_duality_v2.pdf
./Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
./genus1_seven_faces.pdf
./programme_summary_sections9_14.pdf
./test_bar.pdf
./garland_lepowsky.pdf
./riccati.pdf
./N4_mc4_completion.pdf
./programme_summary_section1.pdf
./main.pdf
./programme_summary_sections2_4.pdf
./computations.pdf
./classification_trichotomy.pdf
./modular_koszul_duality_annals.pdf
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/ --co -q 2>&1 | tail -1' in /Users/raeez/chiral-bar-cobar
thinking
**Waiting for test results**

I see that Pytest is still running the session, so I’ll wait for that to finish. It seems like I need to check the page count, possibly using `pdfinfo main.pdf`. The user mentioned comparing the last build date of `main.pdf` and `modular_koszul_duality.pdf`, which might indicate that `main.pdf` is the latest. I should check for any symlinks with `ls -lt` to clarify things. Let's run those checks and see what I find!
exec
/bin/zsh -lc 'ls -lt main.pdf modular_koszul_duality.pdf 2>/dev/null' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pdfinfo main.pdf | rg '"'^Pages|''^ModDate|''^File size'"'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
-rw-r--r--@ 1 raeez  staff  13126202 Apr 13 19:23 main.pdf
-rw-r--r--@ 1 raeez  staff  12964420 Apr  8 15:20 modular_koszul_duality.pdf
 succeeded in 52ms:
ModDate:         Mon Apr 13 19:22:45 2026 SAST
Pages:           2617
File size:       13126202 bytes
exec
/bin/zsh -lc "sed -n '1,140p' README.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

| Theorem | Statement | Status |
|:-------:|-----------|--------|
| **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
 succeeded in 20.81s:
124511/125444 tests collected (933 deselected) in 12.53s









thinking
**Updating test counts**

I've noticed that the test counts in the README don't quite match the latest output. I want to clarify that the command shows `124,511 selected` out of `125,444 collected`, with `933 deselected`. So, I'm thinking "collected" means total tests. To be accurate, I should write that `125,444 collected (124,511 active; 933 deselected)`, but I need to be cautious with language. Also, I need to confirm the page count is exactly `2617`, reflecting the last build, which was updated on April 13, 2026.
thinking
**Reviewing README details**

I think the README should specify that there are `2,617 pages`. I want to ensure I'm using the correct document like `modular_koszul_duality.pdf`, but main.pdf is likely the most current. I could mention that it's from the April 13, 2026 build, although that might not be necessary. I need to verify the theorem status summary from concordance — it probably matches. The line about "g >= 1 remains conjectural" might be an overclaim; I should look for other such claims in the README to refine my statements.
thinking
**Refining AGENTS description**

In AGENTS, it seems like D only applies to the proved uniform-weight lane, while the multi-weight cross-channel exists as a separate entity. I’m thinking that the phrase "controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera" might be overly broad. This could be problematic since multi-weight scenarios for g >= 2 require the inclusion of cross-channel terms. I’ll need to clarify this to avoid any potential confusion.
thinking
**Evaluating theorem claims**

I think the claim "across all genera" might not be necessarily false, but I need to ensure that no claims exceed what's proven. I should check the source for the count of tagged claims. The README says there are 6200+, but the theorem registry indicates 3112 in Volume I, which seems inconsistent. The AGENTS top says the total is 3500+ across three volumes, so I need to clarify these figures and update the theorem status summary accordingly.
thinking
**Clarifying claims and counts**

I’m considering the possibility of informal claims being included, but it seems the registry tracks only proved claims. The total of 3112 statuses suggests that the 6200 claims figure is false. Regarding the cross-volume labels of 13,100+, they might include duplicates. The user wants the theorem status summary updated to ensure no claims exceed what's proved. I definitely need to verify all counts, starting with updating the "Tagged claims" to 3112 from the theorem registry and reassessing other metrics for accuracy.
thinking
**Assessing claims for accuracy**

I’m looking at the page count, test count, and theorem status summary. The key is to ensure no claims exceed what's proven without inflating the scope. This means I should focus on fixing only targeted items and obvious overclaims instead of overhauling the entire README. However, I suspect there are several unverified numeric claims in the status table. It might be necessary to audit some lines to ensure everything aligns correctly with what’s proved.
thinking
**Considering README updates**

I’m realizing that the figure "32 building PDFs" might exceed what we've verified, and I haven't built yet. The user pointed out that the page count is only from the last build, not other metrics. I should consider removing or softening unverified metrics instead of verifying everything. If the README has unchecked counts, it's a concern. The goal is to ensure no claims exceed what's proven, so I might need to prune unverified counts, but I'm wondering about the user's request to update the current README.
thinking
**Updating README details**

The user specifically asked for an update on page count, test count, and theorem status summary, ensuring no claims exceed what’s proven. It seems like fixing the theorem status summary and adjusting counts is essential, while the rest can stay unless something is blatantly false. The README has already been changed to include theorem statuses but not counts, so I might just need to adjust those and any tagged claims. I want to ensure the language about consistency is clear, so I'll review it closely.
thinking
**Verifying theorem summary**

I need to check if the theorem summary fully aligns with the concordance, and it seems like it does. I might update the H statement to include `\ChirHoch^1(V_k(g))\cong g` and mention collapsing by local FM formality, but I think the current summary is already good and not overclaiming. I could also mention that C0 ordinary-derived functions are only valid on a flat perfect locus with genus 0. I should figure out if the README has any unnecessary patterns and run a grep after editing to ensure it's clean.
codex
The current README has another likely overclaim outside the requested counts: the shadow-depth table may be stating finite termination too strongly. I’m checking concordance and nearby source before deciding whether to narrow that table or leave it.
exec
/bin/zsh -lc 'rg -n "theorem packages|ClaimStatusProvedHere|ClaimStatusConditional|ClaimStatusConjectured|Theorem~H|Theorem~D|Complementarity" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"shadow depth|Shadow depth|class~G|class~L|class~C|class~M|r_max|betagamma|quartic shadow|then terminates|infinite tower\" chapters/connections/concordance.tex README.md chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
24:The algebraic engine rests on five theorem packages.
38: & \ClaimStatusProvedHere \\
46: & \ClaimStatusProvedHere \\
47:\textbf{C} & Complementarity
58: & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
70: & \ClaimStatusProvedHere \\
82: & \ClaimStatusProvedHere
138: modular Koszul algebras (Theorem~H).
204:\item \textbf{Complementarity}
416: Theorem~H does not apply there, and the oper/Feigin--Frenkel package
481:Theorem~C identifies its genus-$g$ curvature; Theorem~D computes
538:\begin{proposition}[GLZ as special case; \ClaimStatusProvedHere]\label{prop:glz-special-case}
552:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
844:\ClaimStatusProvedHere
868:\ClaimStatusProvedHere
882:\textup{(}Theorem~D\textup{)}, the cubic shadow
905:\ClaimStatusProvedHere
2369:\ClaimStatusProvedHere
2572: \ClaimStatusProvedHere]
3303:bar-cobar inversion via Theorem~H, polynomial growth, and
 succeeded in 51ms:
Total output lines: 1391

README.md:38:| Class | Shadow depth | Archetype | Defining property |
README.md:41:| **L** | 3 | Affine Kac-Moody | Lie/tree: cubic shadow, then terminates |
README.md:42:| **C** | 4 | beta-gamma | Contact/quartic: quartic shadow, then terminates |
README.md:43:| **M** | infinity | Virasoro, W_N | Mixed: infinite tower, all higher shadows nonzero |
chapters/connections/concordance.tex:193: and the quartic shadow~$S_4$.
chapters/connections/concordance.tex:220:On each primary line it controls shadow depth
chapters/connections/concordance.tex:224:class~C escapes via stratum separation),
chapters/connections/concordance.tex:237:of the chiral theory (class~G, $r_{\max} = 2$) via
chapters/connections/concordance.tex:263:\textbf{Shadow depth classifies complexity within the Koszul world.}\enspace
chapters/connections/concordance.tex:267:shadow depth $r_{\max}$ and the four-class partition
chapters/connections/concordance.tex:270:class~G (formal, $r_{\max} = 2$),
chapters/connections/concordance.tex:271:class~L (single Massey product, $r_{\max} = 3$),
chapters/connections/concordance.tex:272:class~C (quartic then rigid by stratum separation, $r_{\max} = 4$),
chapters/connections/concordance.tex:273:class~M (intrinsically non-formal, $r_{\max} = \infty$).
chapters/connections/concordance.tex:377: $\kappa = 12$, class~M, Niemeier discrimination
chapters/connections/concordance.tex:726:G and~L are proved, class~C is conditional on harmonic decoupling,
chapters/connections/concordance.tex:727:and the chain-level identification fails for class~M
chapters/connections/concordance.tex:826:\index{shadow depth!envelope-shadow complexity}
exec
/bin/zsh -lc 'rg -n "Tagged claims|Cross-volume labels|Compute modules|Automated hook checks|Koszul equivalences|Standalone papers|Example families|Shadow census families" README.md metadata .' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
README.md:50:| Tagged claims | ~6,200+ |
README.md:51:| Cross-volume labels | ~13,100+ |
README.md:54:| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
README.md:55:| Shadow census families | 25 (14 original + 11 added) |
README.md:56:| Compute modules | 1,350+ lib + 1,410+ test |
README.md:58:| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
README.md:59:| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
README.md:60:| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
README.md:61:| Standalone papers | 32 building PDFs (all pass; 0 failures) |
./healing_20260413_132214/H19_remove_genus0_koszul_vii.md:270:I need to find information on the Koszul equivalences theorem, specifically around (vii) and its current discussions. I'm wondering if I should use the explorer tool to help with this search. It might be useful to spawn the explorer and see what I can uncover. Let's give that a try and see what resources are available on this topic!
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:2237: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:2410: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:2636: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:2893: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3121: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3331:    43	| Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3338:    50	| Standalone papers | 3 (preface_full_survey, bar_chain_models_chiral_quantum_groups, ordered_associative_chiral_kd) |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3461: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3696: | Tagged claims | ~2,650+ |
./fix_wave_D_20260413_182434/D11_arity_ban_v2.md:3952: | Tagged claims | ~2,650+ |

thinking
**Updating audit records**

I’ve got some findings from the audit: the `README.md` row is flagged, and it shifted from 10 unconditional to 9 unconditional plus 1 proved consequence. That's definitely over what’s been proved, so I need to fix it! I should align the `Koszul equivalences` row with current sources. I need to check the current sources for the exact wording, possibly by searching through concordance or `chiral_koszul_pairs` for a summary. Time to get searching!
codex
I found one concrete overclaim in the README metrics block: the Koszul-equivalences tally is stale against the current source history. I’m grounding that line now so the README doesn’t advertise a stronger equivalence package than the manuscript actually proves.
exec
/bin/zsh -lc "sed -n '3520,3588p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "nine unconditional Koszul equivalences|Koszul equivalences|proved consequence|D-module purity|Lagrangian" chapters/theory/chiral_koszul_pairs.tex chapters/connections/concordance.tex appendices/dual_methodology.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "3,112|3112|Total tagged claims|Status Totals|Snapshot" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
\toprule
$\cA_1$ & $\cA_2$ & $r_{\max}(\cA_1 \oplus \cA_2)$ & Class \\
\midrule
$G$ & $G$ & $\max(2,2) = 2$ & $G$ \\
$G$ & $L$ & $\max(2,3) = 3$ & $L$ \\
$L$ & $L$ & $\max(3,3) = 3$ & $L$ \\
$G$ & $M$ & $\max(2,\infty) = \infty$ & $M$ \\
$C$ & $M$ & $\max(4,\infty) = \infty$ & $M$ \\
\bottomrule
\end{tabular}
\end{center}
The entry $L \oplus L = L$ (not~$C$) is the decisive case: two
affine Kac--Moody factors at levels $k_1$, $k_2$ produce no
cross-sector shadow terms at depth~$4$, because the quartic
obstruction $S_4$ is intrinsic to each factor's OPE and the
mixed channels contribute only regular terms.

This join-semilattice structure is specific to direct sums.
Constructions that create new OPE singularities between
sectors can raise the shadow class strictly: a quantum
 succeeded in 51ms:
appendices/dual_methodology.tex:201:Koszul locus, and characterizes it (see the Koszul equivalences meta-theorem,
chapters/connections/concordance.tex:52: duality/Lagrangian only for $g \geq 1$ and genus~$0$
chapters/connections/concordance.tex:210: and the two summands are complementary Lagrangians for the
chapters/connections/concordance.tex:260:and Lagrangian complementarity have no classical analogue.
chapters/connections/concordance.tex:345: duality and the Lagrangian package for $g \geq 1$, while genus~$0$
chapters/connections/concordance.tex:2024:factorization-homology criterion; 1 proved consequence,
chapters/connections/concordance.tex:2071: Theorem~C from additive splitting to a two-layer Lagrangian
chapters/connections/concordance.tex:2072: geometry: the Verdier-side Lagrangian package is proved, while the
chapters/connections/concordance.tex:2075: with two Lagrangian maps, a complementarity potential~$S_\cA$
chapters/connections/concordance.tex:2079: Lagrangian is linear
chapters/connections/concordance.tex:2506: Lagrangian complementarity: $\mathcal{M}_\cA, \mathcal{M}_{\cA^!} \hookrightarrow \mathcal{M}_{\mathrm{comp}}$ are $(-1)$-shifted Lagrangian
chapters/connections/concordance.tex:3261:the Lagrangian criterion~(\ref{item:kp-lagrangian}) now
chapters/connections/concordance.tex:3305:The Lagrangian criterion~(\ref{item:kp-lagrangian}) is conditional
chapters/connections/concordance.tex:3982:Verdier-side package gives the Lagrangian geometry on
chapters/connections/concordance.tex:4811: & Lagrangian complementarity; C2 shifted-symplectic upgrade & C2: \textbf{Conditional} & \ref{thm:quantum-complementarity-main}, \\
chapters/connections/concordance.tex:5054:\subsection{The Lagrangian form of complementarity}
chapters/connections/concordance.tex:5061:The natural strengthening is a Lagrangian-polarization theorem,
chapters/connections/concordance.tex:5064:\begin{theorem}[Lagrangian complementarity package;
chapters/connections/concordance.tex:5066:\index{Lagrangian!complementarity|textbf}
chapters/connections/concordance.tex:5075: Lagrangians in the sense of
 succeeded in 51ms:
12:## Snapshot
17:| Total tagged claims | 3112 |
21:## Status Totals
exec
/bin/zsh -lc "sed -n '2014,2030p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9748,9756p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\textup{(}analytic HS-sewing at all genera, genus-$0$ algebraic
BRST/bar, $D^{\mathrm{co}}$-level BV=bar for all shadow classes;
chain-level BV/BRST/bar conjectural\textup{)},
MC3 \textup{(}evaluation core all types unconditional; categorical
CG all types unconditional; type-$A$ post-core reduction proved on the
Baxter-locus seed, with residual compact-completion DK-4/5 downstream
of the Baxter constraint and Conjecture~\ref{conj:dk-compacts-completion}\textup{)},
DK-0/1 (proved), DK-2/3 (evaluation-generated core proved),
and the Koszulness characterization programme
(9 unconditional equivalences, with \textup{(}vii\textup{)} the genus-$0$
factorization-homology criterion; 1 proved consequence,
1 conditional, 1 one-directional;
Theorem~\ref{thm:koszul-equivalences-meta}). This is the spine. Nothing in the extension
appendices touches it except to cross-reference from it.

\subsection*{Ring~2: The nonlinear characteristic layer}
Before the extension appendices, the modular characteristic was
 succeeded in 51ms:
 (extension beyond evaluation modules) downstream \\
& Koszulness programme: $9$ unconditional
 equivalences \textup{(}with factorization homology at
 genus~$0$\textup{)} $+$ $1$ proved consequence
 \textup{(}chiral Hochschild on the Koszul locus\textup{)}
 $+$ $1$ conditional (Lagrangian)
 $+$ $1$ one-directional (D-module purity)
 \textup{(}Theorem~\ref{thm:koszul-equivalences-meta}\textup{)} \\
& Shadow obstruction tower algebraicity:





thinking
**Verifying counts and metrics**

I realize that leaving outdated values may lead to false claims. A quick solution could be to remove unverified rows or refine them based on accurate counts. I think of verifying counts using simple shell commands, like counting Python and LaTeX files in specific directories. I could also utilize regex for cross-volume labels. While checking automated hook scripts might be less essential, ensuring standalone papers are validated is important for clarity.
thinking
**Narrowing metrics for accuracy**

I’m considering whether to limit the metrics block to just validated items. This approach might reduce the number of rows, but could also go beyond what's necessary. I think it’s essential to keep counts like page numbers and tagged claims, as well as compute tests, while eliminating unnecessary rows. Although the user didn’t request trimming, I feel that if some claims can’t be quickly verified, it makes sense to remove those unsupported rows for accuracy.
thinking
**Evaluating edits for accuracy**

I’m considering making edits to remove the most problematic rows that include known stale or overclaiming numbers. Specifically, I need to look at things like tagged claims, compute tests, and Koszul equivalences. There’s also a questionable row about standalone papers that may or may not be accurate from the last build. The user didn’t specifically ask for updates, but since reliability is key, I should probably correct any overclaims that stand out.
thinking
**Reviewing claims and status metrics**

I need to address overclaims found in the Koszul equivalences, where there are 10 unconditional, 1 conditional, and 1 partial claim. That definitely needs fixing. The tagged claims show a false count of around 6,200+, which seems stale based on current metadata. The standalone papers state that all pass with 0 failures, but this might not relate to mathematical proof. To meet the user's request, I could clarify the status section and remove any unverified rows. This way, it stays scoped and truthful.
thinking
**Deciding on minimal edits**

I think for a minimal edit, I should replace the entire status table with only the rows we can verify, including the Theorem status row, while leaving unsupported metrics out. The user didn't specifically ask for this shrink, but it might be the easiest way to ensure accuracy. Since the file already has a lengthy status table, perhaps I should only adjust rows with grounded sources and address any obvious overclaims. I might need to check for prior audit notes related to README counts and any flagged claims.
exec
/bin/zsh -lc "rg -n \"README\\.md:\" wave2_audit_20260413_001942/S20_readme_to_manuscript.md fix_wave_B_20260413_171623/B18_readme_update_v1.md fix_wave_B_20260413_171623/B20_readme_update_v3.md fix_wave_A_20260413_112727/A05_concordance.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
fix_wave_B_20260413_171623/B18_readme_update_v1.md:3:Updated [README.md](/Users/raeez/chiral-bar-cobar/README.md:16) and [README.md](/Users/raeez/chiral-bar-cobar/README.md:45).
fix_wave_B_20260413_171623/B18_readme_update_v1.md:371:1. The README’s “All five master conjectures MC1–MC5 are proved…” claim (`README.md:16-27`) overshoots the concordance: MC3 is only proved on the evaluation-generated core with the DK-4/5 extension beyond that still flagged as downstream/conjectural, and MC5’s analytic/coderived lanes are proved while the genuswise chain-level BV/BRST/bar identification remains conjectural (with some shadow classes only conditional) (`chapters/connections/concordance.tex:1875-1993`).  
fix_wave_B_20260413_171623/B18_readme_update_v1.md:374:  019d8799-38eb-7fb1-bb1b-b4ca3e4d26c1 completed: "1. The README’s “All five master conjectures MC1–MC5 are proved…” claim (`README.md:16-27`) overshoots the concordance: …"
fix_wave_B_20260413_171623/B18_readme_update_v1.md:776:close_agent(call_B4hY6MAD3OLPdKqLh9SZK127) completed: "1. The README’s “All five master conjectures MC1–MC5 are proved…” claim (`README.md:16-27`) overshoots the concordance: …":
fix_wave_B_20260413_171623/B18_readme_update_v1.md:839:Updated [README.md](/Users/raeez/chiral-bar-cobar/README.md:16) and [README.md](/Users/raeez/chiral-bar-cobar/README.md:45).
fix_wave_B_20260413_171623/B20_readme_update_v3.md:3:Edited [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md:6) only.
fix_wave_B_20260413_171623/B20_readme_update_v3.md:184:README.md:6:The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
fix_wave_B_20260413_171623/B20_readme_update_v3.md:185:README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
fix_wave_B_20260413_171623/B20_readme_update_v3.md:186:README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:187:README.md:57:| CY_2 functor (d=2) | **Proved** |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:188:README.md:58:| Lattice VOA bridge | **Proved** |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:189:README.md:59:| CoHA = E_1 sector | **Proved** |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:190:README.md:60:| Drinfeld center = E_2 | **Proved** |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:191:README.md:61:| CY_3 functor (d=3) | **Conjectural** (central open problem) |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:192:README.md:62:| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:193:README.md:63:| Langlands = Koszul | **Conjectural** |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:194:README.md:68:| Pages | ~335+ |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:195:README.md:74:| Compute tests | ~17,700+ |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:271:README.md:64:| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
fix_wave_B_20260413_171623/B20_readme_update_v3.md:272:README.md:74:| Compute tests | ~17,700+ |


thinking
**Updating summary details**

I think I should add a sentence after the heading about the summaries following the concordance. The user mentions needing a theorem status summary based on that. I’d like to say, “These summaries follow the concordance; precise theorem statements carry the standing finiteness/Koszul/uniform-weight hypotheses." That might help narrow down claims. I’m also considering if I need to update the tagged claims based on the new metadata. Maybe I should verify counts across volumes just to be sure!
thinking
**Evaluating metrics fixes**

I’m thinking that I might be able to fix all these metrics in a cost-effective way. I should probably prioritize fixing the ones that are clearly stale first. It’s a good idea to get counts for compute files, TeX files, and standalone counts because those numbers might give me useful insights. I could also consider using a parallel approach to speed up the process. That could make things more efficient!
codex
I’m checking a few adjacent README metrics now because several of them are cheap to verify, and I’d rather correct or remove a stale public count than leave it asserting the wrong surface.
exec
/bin/zsh -lc "find compute/tests -name '*.py' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find compute/lib -name '*.py' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find chapters -name '*.tex' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find appendices -name '*.tex' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find standalone -maxdepth 1 -name '*.tex' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -o '\\\\label\\{' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups -g '*.tex' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1423
 succeeded in 50ms:
1352
 succeeded in 51ms:
15
 succeeded in 51ms:
89
 succeeded in 52ms:
51
 succeeded in 51ms:
24720






thinking
**Clarifying chapter counts**

I need to note that there should be 89 chapters and 15 appendices, not 113, as I mistakenly thought. The README mentions 113 .tex chapters, 15 appendices, and 36 standalone documents, but actually, there are 51 standalone .tex files. I wonder if I should update this information, even though the user didn’t specifically ask for it. I should make sure that my counts reflect accurately in the status and structure blocks as well.
thinking
**Updating status table**

I’m considering how to fix the status table since the old row is incorrect. The user didn’t specifically ask, but I think it’s important to correct it. I want to adjust the "Source files" row to accurately reflect "89 chapter .tex + 15 appendices + 51 standalone .tex," even though some standalone files might not be papers. Maybe it’s best to prune the status table to keep only grounded rows with the updated metrics since stale numbers could cause confusion.
thinking
**Revising theorem counts**

I’m considering whether to remove the `Koszul equivalences` row since it’s a distinct count not requested, and it seems to be overclaiming. Instead, I could change it to exactly `9 unconditional + 1 proved consequence + 1 conditional + 1 one-directional`, which feels minimal. I think it's better to update rather than delete since it’s informative. I should also revise `Tagged claims`, `Source files`, and `Compute modules` rows. Adjusting those seems feasible, but I need to be careful not to inflate the scope.
thinking
**Considering README edits**

I realize this is a repository question, but it seems like it’s not strictly enforced. I might need to prepare a pre-edit verification block. The AGENTS system says that a pre-edit protocol is mandatory for editing hot zones, though the README isn’t a hot zone and doesn't involve theorem labels or formulas. Still, I may want to inspect current README lines for theorem summary and status sections to apply a patch. Adding a sentence after the theorem heading about scope and hypotheses could be useful, but I want to keep it minimal.
thinking
**Updating structure blocks**

I’m thinking about updating the bottom structure block to include `lib` and `tests`. I'll adjust the source files row to reflect exactly 89 chapters plus 15 appendices and 51 standalone `.tex` files. But, hmm, I wonder if the current label "Source files" is still fitting or if it needs a refresh. Maybe it’s okay as is, but I’ll keep it in mind for a potential update.
thinking
**Inspecting test counts**

I need to clarify the test count because the user only asked for the number of tests through a command. The current comment about the test suite being fast is definitely misleading based on the audit. I can verify that `make test` might actually use around 124,511 active tests. Hmm, I'll need to check the Makefile to understand the relevant commands better. I'll read through the lines quickly to get a clearer picture.
exec
/bin/zsh -lc "sed -n '300,360p' Makefile" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find compute/tests -name 'test_*.py' | wc -l | tr -d ' '" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
	@python3 -c "import json; d=json.load(open('metadata/census.json')); t=d['totals']; print(f'  PH={t[\"ProvedHere\"]} PE={t[\"ProvedElsewhere\"]} CJ={t[\"Conjectured\"]} H={t[\"Heuristic\"]} O={t[\"Open\"]} total={t[\"total_claims\"]}')"

## audit: Run Beilinson proof-chain integrity audit on theorem dependency DAG.
audit: metadata
	@python3 -c "from compute.lib.beilinson_auditor import BeilinsonAuditor; a = BeilinsonAuditor('.'); r = a.run_audit(); print(a.format_report(r))"

## verify: Run anti-pattern verification on all .tex files.
verify:
	@./scripts/verify_edit.sh --all

## test: Run fast test suite (excludes @pytest.mark.slow).  Use for rapid iteration.
test:
	@if [ -d compute/tests ] && ls compute/tests/test_*.py 1>/dev/null 2>&1; then \
		echo "  ── Running compute test suite (fast: excludes slow) ──"; \
		mkdir -p $(LOG_DIR); \
		if [ -f compute/.venv/bin/python ]; then \
			PYTHON_BIN=compute/.venv/bin/python; \
		elif [ -f .venv/bin/python ]; then \
			PYTHON_BIN=.venv/bin/python; \
		else \
 succeeded in 51ms:
1421



thinking
**Reviewing Python file counts**

I'm looking at the count of Python files, which includes `test_*.py`, `__init__.py`, and potentially `conftest.py`. I think the row should say `Compute Python files` instead of modules. For the bottom structure block, I see that I could mention `tests/ 1,421 test files (125K collected tests)`, but I'm wondering if the user prefers a test count instead of a file count since the current numbers are a bit stale. I may also want to clarify the inclusion of `__init__.py` in my counts.
thinking
**Clarifying test counts and commands**

I’m looking at the test counts, noting that we might have 124,511 out of 125,444 tests collected, with 933 deselected. The comment could clarify that these are all non-slow tests currently selected. For `make test-full`, the comment could reflect that all tests are currently collected. I’m considering whether the command for `-m "not slow"` is necessary, given that defaults may already deselect slow tests through `conftest.py`. Even though the user requested running the command without the marker, I see the output already shows 933 deselections.
thinking
**Considering audit findings**

I’m thinking that the bullet list of three items isn't really a theorem claim, but more of a structural explanation. There’s a chance it could exceed what's proved if objects are mixed or conflated. But, it seems like this might not have been checked in the user's requested audit. My goal, as always, is a truth-first approach. I’ll search to see if there was any audit finding on the "Six-Object Web." If not, I’ll check the README for relevant audits.
exec
/bin/zsh -lc "rg -n \"Six-Object|Five-Object|D_Ran\\(B\\(A\\)\\)|A\\"'^i|Koszul dual" wave2_audit_20260413_001942 fix_wave_B_20260413_171623 README.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 2356

README.md:28:## The Six-Object Web
README.md:32:- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
README.md:33:- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:101:E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:399:scripts/mega_rescue_100.py:203:    ("M66_BD_full", "FULL Beilinson-Drinfeld cross-check. Read BD [BD04] Chapters 3-4. Verify: (a) our chiral Koszul duality extends BD's chiral homology, (b) our E_inf treatment is compatible, (c) Arnold form = BD's factorization structure. Write Remark[BD full comparison] in concordance."),
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:560:{'label': 'thm:main-koszul-hoch', 'env_type': 'theorem', 'status': 'ProvedHere', 'file': 'chapters/theory/chiral_hochschild_koszul.tex', 'line': 693, 'title': 'Koszul duality for Hochschild cohomology\n\\textup{(}Theorem~H\\textup{)}', 'labels_in_block': ['thm:main-koszul-hoch', 'eq:hochschild-H-derived'], 'refs_in_block': ['conv:regime-tags', 'def:chiral-koszul-morphism', 'def:bigraded-hochschild', 'lem:hochschild-shift-computation']}
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:722:\begin{theorem}[Koszul duality for Hochschild cohomology
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:725:\index{Hochschild cohomology!Koszul duality|textbf}
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:829:$\ChirHoch^2(\mathrm{Vir}_c) = \mathbb{C}$: by the Koszul duality
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:1122:I'm checking the concordance entry, and it looks okay. I think I might need to inspect the E1 claim, but it seems Theorem 4 could be relevant since it mentions that E1-chiral Koszul duality extends to Yangians and toroidal areas, going beyond E_inf. However, I should verify if the theorem statement is broad enough. It cites something on line 5290 related to chiral_koszul_pairs, so I could read that snippet for clarity.
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:1144:\section{\texorpdfstring{The $\Eone$-chiral Koszul duality theorem}{The E1-chiral Koszul duality theorem}}
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:1396:Under Koszul duality $\cA \leftrightarrow \cA^!$,
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:2485:\item \emph{$C_2$-cofiniteness}: orthogonal to Koszulness; Koszul duality maps $C_2$-cofinite to non-$C_2$-cofinite.
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:4900:appendices/koszul_reference.tex:263:The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:5133:produced by ordered associative chiral Koszul duality of $\widehat{\mathfrak{g}}_k$
fix_wave_B_20260413_171623/B16_concordance_full_sync.md:5363: On the affine lineage, the open-colour Koszul dual
fix_wave_B_20260413_171623/B20_readme_update_v3.md:354: \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. The automorphic correction of the BKM superalgebra $\mathfrak{g}_X$ is identified with the shadow obstruction tower $\Theta_{A_X}$; the denominator identity equals the bar-complex Euler product.
fix_wave_B_20260413_171623/B14_stale_cross_vol_refs_v2.md:121:chapters/examples/examples-complete.tex:19:Shadow depth classifies the \emph{complexity} of the Lagrangian self-intersection within the standard families. All four classes are chirally Koszul (Vol~I, PBW universality); classes~$\mathsf{G}$, $\mathsf{L}$, $\mathsf{C}$ have formal Swiss-cheese structure, while class~$\mathsf{M}$ (Virasoro, $\mathcal{W}_N$) has infinite shadow depth and non-formal Swiss-cheese structure, with well-defined Koszul duals carrying higher $A_\infty$ operations (Vol~I, Theorem~\ref*{V1-thm:koszul-equivalences-meta}).









thinking
**Considering output adjustments**

I’m thinking about checking the output or audit logs. The user mentioned not to inflate the numbers. Instead, maybe I could soften the row to say “Standalone papers | 51 .tex sources; 32 listed in build target” or possibly remove the row altogether to maintain accuracy. I know there are 51 `.tex` files in the standalone directory and potentially 32 PDFs for the build target, which I could verify by looking at the Makefile, but that might not be necessary.
thinking
**Updating row counts**

I’ve counted all the labels across the volumes, and it’s coming to 24,720. That means the current row is definitely stale, so I should update it to avoid leaving false information. Other rows like `Example families` and `Shadow census families` might still be okay, but I’m unsure. Meanwhile, `Anti-patterns` seems current. It feels like if I fix only some rows and leave others, it might work, but the `Cross-volume labels` definitely need an update since we have the exact count now.
thinking
**Updating current rows**

I think I need to update the rows that I can verify as current. Here’s what I have: Pages are at 2617, tagged claims are 3112, and cross-volume labels are at 24,720. For compute tests, I've collected 125,444 total, with 124,511 active and 933 deselected. I’ve got 89 chapter .tex files, 15 appendices, and 51 standalone .tex files. The compute Python files number 1,352 for libs and 1,421 for test files. I’ll consider leaving rows like example families and shadow census families as they seem okay.
thinking
**Simplifying report structure**

I'm thinking about the patterns and counts. Maybe it's okay to keep some entries like "Standalone papers | 8 publishable..." and "Standalone papers | 32 building PDFs," but I'm concerned about duplicates and unverified keys. I could change the second entry to "Standalone directory | 51 .tex sources" or remove both. It seems simpler to replace the whole status table with fewer verified rows to avoid unsupported elements. Since the user wants a summary, this should be a clearer and cleaner edit.
thinking
**Updating status metrics**

I'm working on the status metrics layout. I have the following entries: total pages, tagged claims, and claim-status totals with classifications like ProvedHere, ProvedElsewhere, and so on. I also include compute tests, the source tree with chapters and appendices, and compute Python files. This format grounds the information and eliminates questionable claims. It doesn’t mention cross-volume labels, which aligns with the request to avoid inflating scope. I'll adjust the structure and make sure all comments fit the overall goal.
thinking
**Refining structure and terminology**

I need to make sure I'm not using semicolons in the markdown, which should be fine. It looks like I need to update the structure blocks; for example, the line about `tests/ 1,379 test files` should be more precise, changing it to `tests/ 1,421 test files (125,444 collected tests)`. The `lib/ 1,313 verification engines` is also outdated, so I could update it to `lib/ 1,352 Python files`, which feels safer. Lastly, I should clarify the entry for `standalone/ 36 standalone papers` to ensure accuracy.
thinking
**Considering structural adjustments**

I'm thinking about how to make the structure more truthful by possibly adjusting the chapters and titles. Maybe we should update the title from "The Six-Object Web" to "The Five Objects" to reflect accurate content since we're already making significant edits to the README. While it's not absolutely necessary, I'm leaning towards correcting this mathematical inaccuracy. It seems like a simple fix to ensure clarity and correctness without completely rewriting sections.
thinking
**Editing theoretical concepts**

I'm structuring the section as "The Five Objects" with five key elements: the chiral algebra, bar coalgebra, dual coalgebra, dual algebra, and chiral derived center, with clear mappings. I want to clarify that the inversion is not Koszul duality, and how one recovers the dual algebra from the dual coalgebra. I also consider terminology concerns, like whether to use the Greek notation for duals, but I'll stick with the ASCII version since it's consistent. Overall, I want to maintain clarity while being careful about how strong the statements can be.
thinking
**Checking for forbidden patterns**

I need to run a grep command for forbidden patterns in the modified README.md file after making edits. I could look for stale patterns like `6,200`, `13,100`, `10 unconditional`, `8K`, `125K`, and any general banned formulas that may not be relevant. The user specifically asked for checking the modified files, so I’ll focus on targeting stale patterns for the README, while noting that the AGENTS guidelines are mostly related to .tex files.
codex
I’ve got the grounded replacements. I’m patching only `README.md`, keeping the current theorem-table rewrite, and tightening the adjacent status/count surfaces so the public summary stays within what the concordance and live artifacts actually support.
file update
M /Users/raeez/chiral-bar-cobar/README.md
@@ -17,2 +17,4 @@
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
@@ -27,9 +29,10 @@
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
@@ -48,15 +51,9 @@
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
@@ -69,4 +66,4 @@
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
@@ -97,5 +94,5 @@
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```
apply_patch(auto_approved=true) exited 0 in 19ms:
Success. Updated the following files:
M README.md
file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```

file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```


thinking
**Reviewing patterns for clarity**

I need to re-read the relevant sections and possibly search for any stale or forbidden patterns. I should also check if the line widths are acceptable. It could be helpful to have commentary around PE, but it isn't strictly necessary. So, let me read through the README snippet to refresh my memory and make sure I'm catching all the important details. I'll take my time to ensure I understand everything clearly!
codex
The patch is in. I’m re-reading the edited sections now and then I’ll run the requested grep pass on `README.md` for the stale/forbidden patterns that were in scope for this fix.
exec
/bin/zsh -lc "sed -n '1,140p' README.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "~6,200|~13,100|10 unconditional|~8K|125,388|124,455|1,313|1,379|The Six-Object Web|MC1|MC2|MC3|MC4|MC5 are proved" README.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note|---|—" README.md' in /Users/raeez/chiral-bar-cobar exited 1 in 50ms:

 succeeded in 51ms:
# Modular Koszul Duality

**Volume I** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product via collision residues on FM_n(C), the deconcatenation coproduct encodes the cofree tensor coalgebra structure. This is the primitive object of the programme. The symmetric bar B^Sigma is its Sigma_n-coinvariant shadow. Integration over Fulton-MacPherson compactifications computes the bar complex; Verdier duality interchanges bar and cobar; and the failure of nilpotence at genus g >= 1 is controlled by a single scalar invariant kappa(A) that organizes the quantum corrections across all genera. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* (this volume) | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese SC^{ch,top}, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |

## Five Main Theorems

These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.

| Theorem | Statement | Status |
 succeeded in 51ms:
11:|:------:|-------|------|
21:|:-------:|-----------|--------|
42:|:-----:|:-----------:|-----------|-------------------|
51:|--------|------:|
file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```


thinking
**Interpreting grep patterns**

I’m dealing with some grep patterns, as there are specific lines found due to the `---` in markdown table separators. The user wants to identify forbidden patterns in modified files. For the README, the em dash potentially creates false positives because of tables. I might need to mention that no prose has banned tokens; using improved grep to exclude tables could be a smart move. I’ll consider running a narrower grep for Unicode em dash and banned prose tokens, excluding table separators.
codex
The stale-pattern grep came back clean. The prose-hygiene grep only hit Markdown table separators because of the raw `---` pattern, so I’m rerunning that check without counting table syntax as a violation.
exec
/bin/zsh -lc 'rg -n "—|notably|crucially|remarkably|furthermore|we now|it is worth noting|worth mentioning|it should be noted|it is important to note" README.md' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```



thinking
**Summarizing git changes**

I need to check the `git diff` to summarize changes, potentially using `git diff -- README.md`. I should verify the coherence of the status table and note that the line `Claim-status totals` in the markdown table might affect formatting due to semicolons. I also want to ensure there's no `\ref` or `\label` in the README, which seems to be fine. Finally, I might need to clarify the precise scope in the updated Theorem B to avoid vagueness.
thinking
**Checking status table wording**

I need to check if the status table row `Koszulness programme` should clarify its wording to "1 one-directional" instead of "one one-directional" for better interpretation. That sounds good! I also want to use `git diff` to examine changes and consider any potential risks associated with them. It seems only logical to get the diff now to ensure everything is on the right track. Let's proceed with that!
exec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/README.md b/README.md
index f7544ca..65f39c5 100644
--- a/README.md
+++ b/README.md
@@ -15,23 +15,26 @@ The ordered bar complex B^{ord}(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassoci
 
 ## Five Main Theorems
 
-| Theorem | Statement |
-|:-------:|-----------|
-| **(A)** | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
-| **(B)** | Bar-cobar inversion: quasi-isomorphism on the Koszul locus |
-| **(C)** | Complementarity: deformations of A and obstructions of A^! are Lagrangian complements |
-| **(D)** | Modular characteristic: obs_g = kappa(A) * lambda_g at all genera (uniform-weight lane) |
-| **(H)** | Hochschild duality: ChirHoch*(A) polynomial, Koszul-functorial |
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
 
-All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
+| Theorem | Statement | Status |
+|:-------:|-----------|--------|
file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```


thinking
**Verifying README references**

The diff looks good, but I'm thinking I might not need to include line references. I should consider mentioning that there's no \ref or \label in the README. To verify this, I could quickly check with a command like `grep` or `rg '\\\\(ref|label)' README.md`. It seems simple enough to do! I'll make sure everything is clear and accurate for the user.
exec
/bin/zsh -lc "rg -n '\\\\(ref|label)\\{' README.md" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```


thinking
**Considering file changes**

I should think about whether there are user modifications that aren't ours. Since the file has undergone edits, I’ve made sure to preserve the current differences and add more changes. That's good. I wonder if I should run a `git status --short README.md`, but it may not be strictly necessary. Still, it could be helpful to see an overview of the current status of the file.
codex
The edited README re-reads coherently, and there are no `\ref{}` or `\label{}` surfaces in the file. I’m done with the verification pass and compiling the fix summary against the four requested items.


thinking
**Creating a concise summary**

I need to make the final answer clear and concise, explicitly mentioning the fixed items, possibly in a bullet list. Including a clickable file link is a good idea. I'll verify that we didn’t run actual tests, just the collection command, so I should mention that. I can structure the summary with short bullets on the fixed items and state the status per finding as FIXED or BLOCKED. Here’s a quick outline of what I’ll include.
thinking
**Summarizing corrections and verifications**

I've made several updates: removed the "MC1–MC5 are proved" claim, corrected the five-object surface, replaced outdated metrics with accurate ones, and revised the Koszulness summary. Verification checks show no matches for stale patterns or banned tokens, and there are no `\ref{}` or `\label{}` present. I should note that I didn't run a full build/test, just inspected `main.pdf` and collected pytest items. Lastly, I need to ensure the final answer is concise, maybe using a bullet list and including the file link.
codex
Updated [README.md](/Users/raeez/chiral-bar-cobar/README.md).

- `FIXED` 1. Page count: `2,617`, taken from `main.pdf` (`pdfinfo`; modified April 13, 2026).
- `FIXED` 2. Test count: `125,444 collected (124,511 active; 933 deselected)`, from the requested `python3 -m pytest compute/tests/ --co -q`.
- `FIXED` 3. Theorem status summary: the README table now follows `chapters/connections/concordance.tex`, with `A/B/D/H` marked proved here, `C0/C1` proved here, and `C2` conditional; I also added a scope sentence so the summary does not outrun the chapter hypotheses.
- `FIXED` 4. Overclaims: removed the old `MC1`-`MC5 are proved` surface, corrected the object-summary block to the canonical five objects, replaced stale status metrics with grounded ones, corrected the Koszulness-programme tally to `9 unconditional + 1 proved consequence + 1 conditional + 1 one-directional`, and updated the test/build comments plus tree counts to match the live repo.

Verification: stale-pattern grep on `README.md` returned no matches; banned-prose grep returned no matches; `README.md` has no `\ref{}` or `\label{}` surface to validate. I did not run a fresh TeX build or execute the tests themselves; I only inspected the last built PDF and collected pytest items.
file update:
diff --git a/README.md b/README.md
index 986ea943c05775ef79e800c1f326d1d9525e3ffe..65f39c514950984360555e6d9aeba32e5baf984f
--- a/README.md
+++ b/README.md
@@ -15,6 +15,8 @@
 
 ## Five Main Theorems
 
+These summaries follow the concordance. The precise chapter statements retain the standing finiteness, Koszul-locus, and uniform-weight hypotheses where applicable.
+
 | Theorem | Statement | Status |
 |:-------:|-----------|--------|
 | **(A)** | Bar-cobar adjunction on Ran(X); the algebra-level Verdier half appears after D_Ran | Proved here |
@@ -25,13 +27,14 @@
 
 The README follows the concordance: A, B, D, and H are proved here; C is split as above. The genuswise chain-level BV/BRST/bar identification for g >= 1 remains conjectural.
 
-## The Six-Object Web
+## The Five Objects
 
-Six objects built from the bar complex B(A), connected by three functors:
+The programme keeps the five canonical objects distinct:
 
-- **A**: the chiral algebra. **B(A)**: its bar coalgebra. **A^!**: Koszul dual algebra.
-- Omega(B(A)) = A (bar-cobar inversion). D_Ran(B(A)) = B(A!) (Verdier intertwining).
-- Z^der_ch(A) = chiral derived center (universal bulk, distinct from bar).
+- **A**: the chiral algebra. **B(A)**: the bar coalgebra. **A^i = H^*(B(A))**: the dual coalgebra. **A^! = ((A^i)^v)**: the dual algebra. **Z^der_ch(A)**: the chiral derived center.
+- Omega(B(A)) = A is bar-cobar inversion, not Koszul duality.
+- A^! is recovered from A^i by linear or Verdier duality.
+- Z^der_ch(A) is Hochschild-cochain bulk, distinct from bar-cobar inversion.
 
 ## Shadow Depth Classification
 
@@ -46,19 +49,13 @@
 
 | Metric | Value |
 |--------|------:|
-| Pages | 2,745 |
-| Tagged claims | ~6,200+ |
-| Cross-volume labels | ~13,100+ |
-| Compute tests | 125,388 collected (124,455 active; 933 deselected) |
-| Source files | 113 .tex chapters + 15 appendices + 36 standalones |
-| Example families | 21 (19 + Y-algebras + logarithmic W(p)) |
-| Shadow census families | 25 (14 original + 11 added) |
-| Compute modules | 1,350+ lib + 1,410+ test |
-| Anti-patterns | AP1-AP185 + AAP1-18 + RS-1..20 + FM1-FM34 |
-| Automated hook checks | 22 (beilinson-gate.sh on every .tex edit) |
-| Koszul equivalences | 10 unconditional + 1 conditional (Lagrangian) + 1 partial (D-module purity) |
-| Standalone papers | 8 publishable (incl. chiral Yangians 115pp, chiral Chern-Weil 24pp, survey tracks A/B) |
-| Standalone papers | 32 building PDFs (all pass; 0 failures) |
+| Pages | 2,617 |
+| Tagged claims (Vol I registry) | 3,112 |
+| Claim-status totals (Vol I registry) | 2,367 ProvedHere; 414 ProvedElsewhere; 289 Conjectured; 12 Conditional; 27 Heuristic; 3 Open |
+| Compute tests | 125,444 collected (124,511 active; 933 deselected) |
+| Source tree | 89 chapter `.tex`; 15 appendices; 51 standalone `.tex` |
+| Compute Python files | 1,352 under `compute/lib`; 1,421 `test_*.py` files under `compute/tests` |
+| Koszulness programme | 9 unconditional equivalences; 1 proved consequence; 1 conditional; 1 one-directional |
 
 ## Build
 
@@ -67,8 +64,8 @@
 pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
 
 # Run tests
-make test          # fast suite (~8K)
-make test-full     # full suite (~125K collected tests)
+make test          # non-slow suite (124,511 currently selected)
+make test-full     # full suite (125,444 currently collected)
 ```
 
 Requires TeX Live 2024+ with pdflatex (memoir, EB Garamond, newtxmath).
@@ -95,7 +92,7 @@
     connections/            Parts IV-VI (~30 files)
   appendices/               signs, FM proofs, tables
   compute/
-    lib/                    1,313 verification engines
-    tests/                  1,379 test files (~125K collected tests)
-  standalone/               36 standalone papers (32 in build target, all pass)
+    lib/                    1,352 Python files
+    tests/                  1,421 test files (125,444 collected tests)
+  standalone/               51 .tex sources
 ```

tokens used
122,787
