# B06_status_audit_connections (802s)

Updated the MC5 status prose in [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1406), [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:440), and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:718) so they now match the live BV/bar surface: coderived `D^{\mathrm{co}}` resolved for all classes, ordinary chain level proved for `G/L`, conditional for `C` on harmonic decoupling, and false for `M`.

`FIXED`
- [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1406): removed the overstatement that scalar Heisenberg/class `C` results “resolve” the full chain-level conjecture; they now read as scalar consequences predicted by `conj:v1-master-bv-brst`.
- [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:440): corrected the conjecture-status gloss from “G/L/C proved” to `G/L` proved, `C` conditional, `M` false; also narrowed the later “MC5 is proved” sentence to the genus-0/genus-1/analytic sewing lanes only.
- [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:718): normalized the repeated MC5 summaries and tables at the affected status blocks so they no longer claim unconditional class `C` chain-level resolution.

Verification: I re-read the edited passages and ran targeted `rg` checks for the stale phrases (`classes~G, L, C`, `holds for classes~G, L, C`, `Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level`, `MC5 at genus~$0$ and genus~$1$ is proved`); all returned no matches. I did not run a TeX build. A generic `---|```` grep only hit pre-existing comment/table separators outside the edited status text.

One cross-volume label split remains outside this patch: `thm:general-hs-sewing` still differs between Vol I and Vol II, and I left the Vol II duplicate untouched because it was outside the assigned file set.


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
session id: 019d8772-b0ba-79f1-8d64-f2b272280317
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


Fix ClaimStatus mismatches in ALL chapters/connections/*.tex files.
Especially bv_brst.tex (MC5 status), concordance.tex (all statuses).
mcp startup: no servers

thinking
**Considering status mismatches**

I’m thinking it might be a good idea to spawn an explorer agent to tackle those status mismatches. The plan is to use the explorer to map mismatches in chapters and connections. My goal is to fix all claim status mismatches in those files. I should also inspect for any discrepancies between the environment and status registry. Keeping edits minimal is essential since I may be dealing with many files. It seems like I might need user updates every 30 seconds, so commentary updates are on my list.
codex
Using `claim-surface-sync` for this pass because the task is status/environment drift across theorem surfaces. I’m starting by reading the skill instructions and the live status sources (`CLAUDE.md`, `chapters/connections/concordance.tex`, `metadata/theorem_registry.md`, the red-team summary, and the affected `chapters/connections/*.tex` files) to isolate exactly which claim statuses disagree.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

exec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Identifying status mismatches**

I need to identify the status mismatches in all chapters and connection files. This could involve checking the label_status_conflicts.csv or using scripts to find discrepancies. I want to generate a list focusing on ClaimStatus mismatches across files. It seems essential to inspect the current git status as well. Maybe I should explore the chapters and connections further to confirm specific files and labels, especially as advised by the developer to trust initial findings.
thinking
**Inspecting claim status mismatches**

I want to use the explorer agent for a specific task: checking for claim status mismatches in the chapters and connection files, particularly in bv_brst.tex regarding MC5 and the concordance summary statuses. I think I should reference the theorem registry and possibly the label_status_conflicts.csv for this check. It feels essential to have a focused approach so I can effectively identify any discrepancies in those files.
codex
I have the canonical status sources open. Next I’m mapping the actual drift inside `chapters/connections/*.tex`, with emphasis on `bv_brst.tex` and any labels whose local status disagrees with `concordance.tex` or the generated conflict reports.
collab spawn_agent(call_w2WNhPulKXJMrRJIthXvKLiG, prompt="Inspect status/environment drift limited to /Users/raeez/chiral-bar-cobar/chapters/connections/*.tex. Focus on: (1) all …")
mcp startup: no servers
spawn_agent(call_w2WNhPulKXJMrRJIthXvKLiG, prompt="Inspect status/environment drift limited to /Users/raeez/chiral-bar-cobar/chapters/connections/*.tex. Focus on: (1) all …") pending init:
  agent: 019d8773-3334-74d2-8498-5c20d9febadf
exec
/bin/zsh -lc ls in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
**Updating exploration plan**

I should run the explorer tool, but while that's going on, I think it’s a good idea to inspect files manually using 'rg.' I’m realizing it’d be helpful to have a plan in place. So, I’ll take time to update my plan with the necessary steps involved in this process. This way, I can make sure everything goes smoothly and I cover all my bases! Let's get organized!
exec
/bin/zsh -lc 'cat .agents/skills/claim-surface-sync/SKILL.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
Plan update
Tracing claim-status drift across connection chapters, then applying only the minimal status corrections and re-verifying local coherence.
  → Inventory status mismatches in chapters/connections, including bv_brst.tex and concordance.tex
  • Patch the affected connection files with minimal truthful status edits
  • Re-read modified surfaces and grep modified files for status/forbidden-pattern regressions


thinking
**Inspecting claim status inconsistencies**

I'm focusing on identifying mismatches between claim statuses in chapters/connections/*.tex files and their references in the concordance, including MC5 and bv_brst statuses. I'll start by gathering relevant files and parsing macros or labels that track claim statuses, then cross-check these against the concordance to find discrepancies for minimal fixes.
exec
/bin/zsh -lc "sed -n '1,200p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
/bin/zsh -lc 'ls chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
arithmetic_shadows.tex
bv_brst.tex
casimir_divisor_core_transport.tex
concordance.tex
dg_shifted_factorization_bridge.tex
editorial_constitution.tex
entanglement_modular_koszul.tex
feynman_connection.tex
feynman_diagrams.tex
frontier_modular_holography_platonic.tex
genus1_seven_faces.tex
genus_complete.tex
holographic_codes_koszul.tex
holographic_datum_master.tex
holomorphic_topological.tex
kontsevich_integral.tex
master_concordance.tex
outlook.tex
physical_origins.tex
poincare_computations.tex
thinking
**Inspecting file list**

I'm thinking about inspecting the file list, particularly looking at "label_status_conflicts.csv." It seems like a good idea to run parallel commands to get a comprehensive view. I should definitely explore using rg — that seems fitting for this task. I’ll stay organized and make sure I’m handling this efficiently while checking each file. Let’s see what insights we can gather from those commands!
exec
/bin/zsh -lc "if [ -f label_status_conflicts.csv ]; then rg -n \"chapters/connections|bv_brst|concordance|MC5|mc5\" label_status_conflicts.csv; else echo 'label_status_conflicts.csv missing'; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"\\\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open)\" chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open)|Status" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"MC5|mc5|ClaimStatus|\\\\begin\\{(theorem|proposition|lemma|conjecture|corollary|remark|definition)\\}|\\\\label\\{\" chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
label_status_conflicts.csv missing
 exited 2 in 51ms:
rg: regex parse error:
    (?:\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open))
       ^^
error: unrecognized escape sequence
 exited 2 in 50ms:
rg: regex parse error:
    (?:MC5|mc5|ClaimStatus|\begin\{(theorem|proposition|lemma|conjecture|corollary|remark|definition)\}|\label\{)
                                                                                                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
30:& \textbf{Theorem} & \textbf{Statement} & \textbf{Status} \\
38: & \ClaimStatusProvedHere \\
46: & \ClaimStatusProvedHere \\
58: & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
68: & \ClaimStatusProvedHere \\
80: & \ClaimStatusProvedHere
536:\begin{proposition}[GLZ as special case; \ClaimStatusProvedHere]\label{prop:glz-special-case}
550:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
775:\ClaimStatusProvedHere
801:\ClaimStatusProvedHere
824:\ClaimStatusProvedHere
844:\ClaimStatusProvedHere
868:\ClaimStatusProvedHere
905:\ClaimStatusProvedHere
1432:arXiv:2503.17563 (2025). Status: preprint.
1485:Status: preprint.
1525:Status: preprints.
1552:Status: preprint.
1577:Status: \textbf{published} (peer-reviewed).
1612:from factorisation} (preprint, 2025). Status: preprints.
exec
/bin/zsh -lc 'rg -n "ClaimStatus" chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 1163

chapters/connections/typeA_baxter_rees_theta.tex:145:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:204:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:243:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:297:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:338:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:431:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:460:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:510:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:545:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:595:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:680:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:742:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:788:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:848:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:882:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:923:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:959:\ClaimStatusProvedHere
chapters/connections/typeA_baxter_rees_theta.tex:1001:\ClaimStatusProvedHere

thinking
**Analyzing ClaimStatus mismatches and MC5 references**

I'm parsing the directory to find labels whose ClaimStatus conflicts with other repo occurrences or concordance summaries, focusing especially on key theorems and MC5 statuses in `bv_brst.tex` and `concordance.tex`. I want to zero in on specific cases where declared statuses differ between label definitions and cross-references.
exec
/bin/zsh -lc 'rg -n "MC5" -n chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2169:\begin{remark}[Research remark: class~$\mathsf{M}$ spectral and completed MC5]
2176:strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
2207:research target is a spectral form of MC5 whose higher differentials
2250:upgrade of MC5 for class~$\mathsf{M}$.
2511:the higher-genus MC5 comparison between the handle-gluing BRST
2543:$bc$ ghosts gives the MC5 genus-$0$ case proved in
exec
/bin/zsh -lc "sed -n '2120,2290p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
comparison cone to be coacyclic.

\emph{The spacetime viewpoint.}
In the Costello--Li framework of twisted supergravity, the bulk
theory on $\mathrm{AdS}_{d+1}$ is computed by Witten diagrams
using the bulk propagator, while the boundary theory is computed
by the bar complex using the boundary OPE. The mismatch between
bulk and boundary propagators at one loop ($g = 1$) is the
holographic anomaly: the Weyl anomaly coefficient
$a - c$ in $4d$ becomes, on the algebraic side, a harmonic
correction to the BV/bar comparison. The coderived formalism
packages this anomaly as curvature data rather than forcing a
strict differential. Theorem~\ref{thm:bv-bar-coderived} shows that
the comparison map becomes an isomorphism after localizing at
coacyclic objects.

\emph{The categorical viewpoint.}
The coderived category $D^{\mathrm{co}}(\cA)$ is the natural
home for curved dg~algebras: it is the homotopy category of
dg~comodules over the bar coalgebra $B(\cA)$ in which

exec
/bin/zsh -lc 'rg -n "ClaimStatus" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
75:\begin{remark}[BV/bar dictionary; \ClaimStatusHeuristic]
184:\begin{theorem}[BV complex $=$ geometric bar complex; \ClaimStatusProvedElsewhere{} \cite{CG17}]
270:\begin{remark}[Heuristic QME/MC comparison; \ClaimStatusHeuristic]
295:\ClaimStatusHeuristic]\label{rem:genus0-amplitude-bar}
356:\begin{theorem}[BRST cohomology = physical states; \ClaimStatusProvedElsewhere{} \cite{CG17}]
385:\ClaimStatusProvedHere]
430:\ClaimStatusConjectured]
465:\begin{lemma}[BRST nilpotence; \ClaimStatusProvedElsewhere{} \cite{FGZ86}]
490:\ClaimStatusProvedHere]
641:\ClaimStatusProvedHere]
683:\begin{proposition}[Koszul duality preserves BRST anomaly cancellation; \ClaimStatusProvedHere]
766:\ClaimStatusProvedHere]
825:\ClaimStatusProvedElsewhere]
918:\ClaimStatusProvedHere]
1031:\ClaimStatusProvedHere]
1127:\ClaimStatusConditional]
1170:\ClaimStatusConditional]
1194:\ClaimStatusProvedHere]
1306:\begin{theorem}[Conditional configuration-space BV package; \ClaimStatusConditional]
1333:\begin{remark}[Quantum master equation; \ClaimStatusHeuristic]
thinking
**Fixing regex and searching**

I need to fix regex escaping, which might involve using single quotes and double backslashes. In shells, single quotes make the regex see backslashes as escapes, while a literal backslash would require four backslashes. It's easier to use the `-F` flag for search. I’ll use `rg -n -F '\ClaimStatus'` for that. I also need to identify all chapters and connections in `.tex` files and possibly write a script to scan label statuses. My main goal is fixing claim status mismatches in these files, identifying conflicts via the metadata generated under `metadata/`, maybe in a CSV format.
exec
/bin/zsh -lc "sed -n '2230,2545p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
where the hats denote inverse limits over finite weight truncations
and finite shadow windows, equivalently a pro-object built from those
finite quotients. The conjectural statement is not that the raw
direct-sum complexes are quasi-isomorphic, but that each finite
quotient of $\widehat f_g$ is a strict quasi-isomorphism and that the
inverse-limit comparison is continuous and filtration-compatible. This
is stronger than Theorem~\ref{thm:bv-bar-coderived}, because it
remembers every finite stage, and weaker than a raw chain-level
quasi-isomorphism, because it allows the infinite class~$\mathsf{M}$
defect to die only after completion.

Between ordinary chain level and bare coderived equivalence lies an
intermediate strengthening. One may ask that $\widehat f_g$ be a weak
equivalence of filtered curved models in the sense of
Definition~\ref{def:curved-weak-equiv}, equivalently an isomorphism
already in the provisional coderived category of
Definition~\ref{def:provisional-coderived}. This retains the full
filtered-completed class~$\mathsf{M}$ tower while remaining compatible
with the proved coderived theorem. On the current record, this
filtered-completed spectral statement is the sharpest plausible
codex
The initial pass confirms `concordance.tex` carries several hard-coded status summaries, so I’m not assuming the table is authoritative. I’m switching to label-by-label extraction from the connection chapters to find the exact drift before editing.
exec
/bin/zsh -lc "rg -n -F 'mc5' chapters/connections/bv_brst.tex chapters/connections/*.tex metadata/theorem_registry.md CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "find . -maxdepth 3 \\( -name '*status*conflict*' -o -name '*claim*ledger*' -o -name '*suspicious_proved_claim_dependencies.csv' -o -name '*theorem*registry*' \\) | sort" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root=pathlib.Path('chapters/connections')
for p in sorted(root.glob('*.tex')):
    text=p.read_text()
    if 'ClaimStatus' in text or '\\\\begin{' in text:
        print(f'FILE {p}')
        for i,line in enumerate(text.splitlines(),1):
            if 'ClaimStatus' in line:
                print(f'{i}:{line}')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/editorial_constitution.tex:460:\label{rem:mc5-vs-bv-brst}
chapters/connections/editorial_constitution.tex:567:\label{conj:standard-tower-mc5-reduction}
chapters/connections/editorial_constitution.tex:658:\label{cor:standard-tower-mc5-closure}
chapters/connections/editorial_constitution.tex:696:of Proposition~\ref{conj:standard-tower-mc5-reduction}. That
chapters/connections/editorial_constitution.tex:914:(Volume~II, Theorem~mc5-genus-one-bridge): the Feynman-defined
chapters/connections/outlook.tex:679:\phantomsection\label{conj:standard-tower-mc5-reduction-outlook}
chapters/connections/outlook.tex:681:\phantomsection\label{cor:standard-tower-mc5-closure-outlook}
chapters/connections/feynman_diagrams.tex:280:\begin{remark}[MC5 local packet]\label{rem:mc5-local-packet}
chapters/connections/feynman_diagrams.tex:523:\label{def:genus0-mc5-coefficient-packet}
chapters/connections/feynman_diagrams.tex:560:Definition~\ref{def:genus0-mc5-coefficient-packet}.
 succeeded in 51ms:
./archive/metadata/theorem_registry.md
./healing_20260413_130533/H32_theorem_registry_rebuild.md
./healing_20260413_132214/H32_theorem_registry_rebuild.md
./metadata/theorem_registry.md
 succeeded in 50ms:
FILE chapters/connections/arithmetic_shadows.tex
198:\ClaimStatusProvedHere
312:\ClaimStatusProvedHere
337:\ClaimStatusProvedHere
350:\ClaimStatusProvedHere
388:\ClaimStatusProvedHere
445:\ClaimStatusProvedHere
476:\ClaimStatusProvedHere
501:\ClaimStatusProvedHere
524:\ClaimStatusProvedHere
692:\ClaimStatusProvedHere
780:\ClaimStatusProvedHere
995:\ClaimStatusProvedHere
1023:\ClaimStatusProvedHere
1073:\ClaimStatusProvedHere
1156:\ClaimStatusProvedHere
1174:\ClaimStatusProvedHere
1196:\ClaimStatusProvedHere
1248:\ClaimStatusProvedHere
1267:\ClaimStatusProvedHere
exec
/bin/zsh -lc 'rg -n "bar-cobar-isomorphism-main" -n' in /Users/raeez/chiral-bar-cobar succeeded in 62ms:
Total output lines: 1484

rectification_20260412_233715/R13_introduction.md:567: Theorem~\ref{thm:bar-cobar-isomorphism-main}).
rectification_20260412_233715/R13_introduction.md:592: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): the
healing_20260413_132214/H18_remove_class_M_MC5.md:380:$B(\cA)$ by bar-cobar inversion, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
metadata/dependency_graph.dot:2439:  thm_bar_cobar_isomorphism_main [label="thm:bar-cobar-isomorphism-main\ntheorem [Pr]\nGeometric bar--cobar duality", style=filled, fillcolor="#c8e6c9"];
metadata/dependency_graph.dot:2907:  thm_bar_cobar_isomorphism_main_equations [label="thm:bar-cobar-isomorphism-main-equations\ntheorem [Pr]\nBar-cobar isomorphism, retained for equa...", style=filled, fillcolor="#c8e6c9"];
relaunch_20260413_111534/R19_coderived_models.md:358:metadata/claims.jsonl:255:{"label": "prop:descent-fan", "env_type": "proposition", "status": "ProvedHere", "file": "chapters/connections/concordance.tex", "line": 9794, "title": "Descent fan structure", "refs_in_block": ["thm:bar-cobar-isomorphism-main", "thm:higher-genus-inversion", "thm:riccati-algebraicity", "constr:shadow-epstein-eisenstein", "eq:constrained-epstein-fe", "thm:sewing-hecke-reciprocity"]}
relaunch_20260413_111534/R19_coderived_models.md:361:metadata/claims.jsonl:2683:{"label": "thm:fourier-four-properties", "env_type": "theorem", "status": "ProvedElsewhere", "file": "chapters/theory/fourier_seed.tex", "line": 918, "title": "The four properties of the Fourier transform", "refs_in_block": ["thm:bar-cobar-isomorphism-main", "thm:higher-genus-inversion", "thm:quantum-complementarity-main", "thm:modular-characteristic"]}
metadata/theorem_registry.md:424:| `thm:bar-cobar-isomorphism-main` | `theorem` | 3941 | Geometric bar--cobar duality |
metadata/theorem_registry.md:828:| `thm:bar-cobar-isomorphism-main-equations` | `theorem` | 2586 | Bar-cobar isomorphism, retained for equation labels |
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:340:/bin/zsh -lc 'rg -n "filtered-comparison|Verdier|SC-formality|class G|lattice|Koszul equiv|Theorem A|bar-cobar-isomorphism-main|thm:verdier-bar-cobar|thm:shadow-formality-identification" chapters/theory/chiral_koszul_pairs.tex chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:362:chapters/theory/bar_construction.tex:99:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:367:chapters/theory/chiral_koszul_pairs.tex:46:(Theorem~\ref{thm:bar-cobar-isomorphism-main}) is the unique
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:377:chapters/theory/chiral_koszul_pairs.tex:568: (Theorem~\ref{thm:bar-cobar-isomorphism-main}): for a chiral
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:423:wave2_audit_20260413_001942/S06_intro_to_body.md:458:./chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:424:wave2_audit_20260413_001942/S06_intro_to_body.md:462:./rectification_20260412_233715/R02_higher_genus_complementarity.md:506:chapters/theory/chiral_koszul_pairs.tex:3611:\label{thm:bar-cobar-isomorphism-main}
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:425:wave2_audit_20260413_001942/S06_intro_to_body.md:464:./rectification_20260412_233715/R18_cobar_construction.md:448:chapters/theory/chiral_koszul_pairs.tex:3639:\label{thm:bar-cobar-isomorphism-main}
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:507:Theorem~A (Theorem~\ref{thm:bar-cobar-isomorphism-main}):
relaunch_20260413_111534/R01_chiral_koszul_pairs.md:1198:Theorem~\ref{thm:bar-cobar-isomorphism-main} from a fiberwise
exec
/bin/zsh -lc 'rg -n "ClaimStatus" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
38: & \ClaimStatusProvedHere \\
46: & \ClaimStatusProvedHere \\
58: & C0/C1: \ClaimStatusProvedHere; C2: \ClaimStatusConditional \\
68: & \ClaimStatusProvedHere \\
80: & \ClaimStatusProvedHere
536:\begin{proposition}[GLZ as special case; \ClaimStatusProvedHere]\label{prop:glz-special-case}
550:\begin{theorem}[FG duality from \texorpdfstring{$\chirAss$}{Ass-ch} self-duality; \ClaimStatusProvedHere]\label{thm:fg-from-assch}
775:\ClaimStatusProvedHere
801:\ClaimStatusProvedHere
824:\ClaimStatusProvedHere
844:\ClaimStatusProvedHere
868:\ClaimStatusProvedHere
905:\ClaimStatusProvedHere
2368:\ClaimStatusProvedHere
2571: \ClaimStatusProvedHere]
2817:\ClaimStatusProvedHere
2869:\ClaimStatusProvedHere
4158:\begin{theorem}[Pixton ideal from shadow obstruction tower; \ClaimStatusProvedHere]
4465:(\ClaimStatusConjectured) identifies the modular characteristic
4639:\begin{proposition}[Bar-cobar bridge; \ClaimStatusProvedElsewhere]


exec
/bin/zsh -lc "rg -n \"label\\{thm:heisenberg-sewing\\}\" -n \"chapters/connections\"" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Identifying file mismatches**

I need to inspect relevant files and lines where there are mismatches. I'll probably explore all labels in chapters or connections that have status drift across the repository. A script to parse labels and statuses could be useful here. Since the label_status_conflicts.csv file is missing, I might have to generate it from local scripts or parse the data myself. I'll need to be careful because environment titles might have specific formatting, and I want to ensure I capture all statuses accurately.
thinking
**Comparing statuses and surfaces**

I also need to compare the concordance text statuses with the actual surfaces. Since the user specifically asked about all concordance statuses, it's possible that some are outdated in the summary table or remarks. I could use the explorer to help find these discrepancies. Before I start editing, it would be wise to inspect the git status to ensure that I have a clear understanding of the current state.
exec
/bin/zsh -lc 'git status --short' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 M CLAUDE.md
 M chapters/connections/casimir_divisor_core_transport.tex
 M chapters/connections/dg_shifted_factorization_bridge.tex
 M chapters/connections/holomorphic_topological.tex
 M chapters/connections/kontsevich_integral.tex
 M chapters/connections/typeA_baxter_rees_theta.tex
 M chapters/connections/ym_boundary_theory.tex
 M chapters/connections/ym_higher_body_couplings.tex
 M chapters/connections/ym_instanton_screening.tex
 M chapters/examples/genus_expansions.tex
 M chapters/examples/landscape_census.tex
 M chapters/theory/bar_cobar_adjunction_inversion.tex
 M chapters/theory/en_koszul_duality.tex
 M chapters/theory/higher_genus_foundations.tex
 M chapters/theory/higher_genus_modular_koszul.tex
 M chapters/theory/introduction.tex
 M chapters/theory/ordered_associative_chiral_kd.tex
 M compute/lib/elliptic_drinfeld_coproduct_engine.py
 M main.tex
 M standalone/survey_modular_koszul_duality_v2.pdf
exec
/bin/zsh -lc "rg -n \"label\\{thm:heisenberg-sewing\\}\"" in /Users/raeez/chiral-bar-cobar succeeded in 67ms:
standalone/N5_mc5_sewing.tex:465:\begin{theorem}[Heisenberg sewing]\label{thm:heisenberg-sewing}
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
relaunch_20260413_111534/S14_standalone_to_main.md:1666:   188	\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
healing_20260413_132214/H11_SC_formal_alt.md:6264:\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:17430:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:28594:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:39759:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:50924:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:62087:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:73250:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:84388:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:95571:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:106744:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:117938:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:129145:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:140338:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:151514:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:162691:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:173873:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}
healing_20260413_132214/H11_SC_formal_alt.md:184975:-\newlabel{thm:heisenberg-sewing}{{F.16.5}{1876}{Heisenberg sewing theorem; \ClaimStatusProvedHere }{theorem.F.16.5}{}}

exec
/bin/zsh -lc "sed -n '4680,4760p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
defect on the torus); extension to $g \geq 2$ is proved algebraically
(Theorem~\ref{thm:inductive-genus-determination}:
inductive genus determination via the bar-intrinsic construction),
with the analytic comparison
(Theorem~\ref{thm:analytic-algebraic-comparison})
established for all graph amplitudes on~$\Sigma_g$
by two-dimensional convergence
(Proposition~\ref{prop:2d-convergence}:
no UV renormalization in dimension~$2$).
The remaining analytic input is HS-sewing
(Definition~\ref{def:hs-sewing}) for the mode-sum
extension from $\cA_{\mathrm{alg}}$ to $\cA^{\mathrm{sew}}$.
\end{proposition}

\begin{proposition}[Relative holographic deformation bridge;
\ClaimStatusProvedHere]%
\label{prop:vol2-relative-holographic-bridge}%
\index{relative holographic deformation complex!cross-volume bridge}%
The forgetful morphism
$p\colon \mathfrak{g}^{\mathrm{SC}}_T \to \gAmod[\cA]$

thinking
**Addressing file mismatches**

I need to avoid unrelated tasks and focus on editing the assigned files, particularly bv_brst.tex and the concordance. The user specifically requested fixing mismatches in all chapters and connections in *.tex files, which feels broad. Since there are modified connection files from the user, I need to read carefully to avoid overwriting any changes. I should probably compare with HEAD to see modifications, but it might not be necessary. I'll work on a script to help identify status conflicts across the repo.
thinking
**Creating a script for status checks**

I think local prose summary references show some status disagreements, so I should write a script for this. It needs to be robust enough to search for \begin{theorem} and then find \ClaimStatusX within the same or next few lines up to the label. There are many claims in these files, so I'll focus on parsing environment starts with statuses and finding labels within the next 10 lines. I need to handle cases like in twisted_holography_quantum_gravity, where I see `\begin{theorem}[...]ClaimStatusProvedHere` without a semicolon on the same line. This script will help extract labels and statuses, reporting any labels with more than one status in chapters or connections.
codex
I have enough context to narrow the work. I’m now extracting labeled claims and statuses across the repo so I can fix only the actual drift surfaces, rather than hand-editing every status-bearing paragraph in `chapters/connections`.
exec
/bin/zsh -lc 'rg -n "prop:vol2" -n chapters/connections' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/concordance.tex:4640:\label{prop:vol2-bar-cobar-bridge}%
chapters/connections/concordance.tex:4665:\label{prop:vol2-dk-ybe-bridge}%
chapters/connections/concordance.tex:4673:\label{prop:vol2-w-algebra-bridge}%
chapters/connections/concordance.tex:4696:\label{prop:vol2-relative-holographic-bridge}%
chapters/connections/concordance.tex:4717:\label{prop:vol2-ribbon-thooft-bridge}%
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re
root=pathlib.Path('.')
status_re=re.compile(r'\\\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open)')
begin_re=re.compile(r'\\\\begin\\{(["'^}]+)'"\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
files=sorted(root.rglob('*.tex'))
occ=[]
for p in files:
    try:
        lines=p.read_text().splitlines()
    except Exception:
        continue
    i=0
    while i < len(lines):
        line=lines[i]
        if '\\\\begin{' in line and 'ClaimStatus' in line:
            m=begin_re.search(line)
            s=status_re.search(line)
            label=label_re.search(line)
            env=m.group(1) if m else None
            status=s.group(1) if s else None
            j=i
            # search a short window for label/status continuation
            while (label is None or status is None) and j+1 < len(lines) and j < i+8:
                j += 1
                nxt=lines[j]
                if status is None:
                    s=status_re.search(nxt)
                    if s: status=s.group(1)
                if label is None:
                    label=label_re.search(nxt)
            if label and status:
                occ.append((label.group(1), status, str(p), i+1, env))
                i=j
        i += 1
# report conflicts involving chapters/connections
from collections import defaultdict
by=defaultdict(list)
for item in occ:
    by[item[0]].append(item)
for label, items in sorted(by.items()):
    statuses={x[1] for x in items}
    if len(statuses)>1 and any('/connections/' in x[2] for x in items):
        print(label)
        for st, path, line, env in sorted((x[1], x[2], x[3], x[4]) for x in items):
            print(f'  {st:15} {path}:{line} [{env}]')
PY" in /Users/raeez/chiral-bar-cobar
thinking
**Investigating status inconsistencies within directory**

I'm exploring how claim statuses in the `chapters/connections` directory might conflict with other parts of the repo—especially looking at potential mismatches between statuses defined there, those in `metadata/claims.jsonl`, and the `metadata/theorem_registry`. There's a lot to check, so I'm focusing on understanding the data structures and files that record these statuses to spot any inconsistencies.
exec
/bin/zsh -lc 'rg -n "thqg_open_closed_realization" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
3000:#### `chapters/connections/thqg_open_closed_realization.tex` (10)
exec
/bin/zsh -lc "sed -n '2980,3045p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
| `cor:thqg-VII-gaussian-degeneration` | `corollary` | 1318 | Degeneration for Gaussian algebras |
| `prop:thqg-VII-mixed-nondegeneration` | `proposition` | 1352 | Non-degeneration for mixed-type algebras |
| `thm:thqg-VII-ss-shadow-obstruction` | `theorem` | 1387 | Spectral sequence differentials as shadow obstructions |
| `thm:thqg-VII-mc-vs-bootstrap` | `theorem` | 1476 | MC recursion vs.\ conformal bootstrap |
| `thm:thqg-VII-crossing-from-mc` | `theorem` | 1543 | Crossing symmetry from the MC equation |
| `cor:thqg-VII-genus-g-bootstrap` | `corollary` | 1607 | Genus-$g$ bootstrap from MC |
| `prop:thqg-VII-bootstrap-gap` | `proposition` | 1688 | The bootstrap gap |
| `comp:thqg-VII-heis-g0` | `computation` | 1786 | Genus-$0$ Heisenberg |
| `comp:thqg-VII-heis-g1` | `computation` | 1817 | Genus-$1$ Heisenberg |
| `comp:thqg-VII-heis-g2` | `computation` | 1865 | Genus-$2$ Heisenberg |
| `comp:thqg-VII-heis-g3` | `computation` | 1962 | Genus-$3$ Heisenberg |
| `comp:thqg-VII-heis-g4` | `computation` | 2035 | Genus-$4$ Heisenberg |
| `thm:thqg-VII-recursion-closed` | `theorem` | 2159 | Recursion reproduces the closed form |
| `cor:thqg-VII-rank-d` | `corollary` | 2235 | Rank-$d$ Heisenberg |
| `thm:thqg-VII-one-loop-gravity` | `theorem` | 2493 | Genus-\texorpdfstring{$1$}{1} scalar term from \texorpdfstring{$\Theta^{(1)}$}{Theta(1)} |
| `thm:thqg-VII-g-loop-amplitude` | `theorem` | 2535 | Integrated genus-\texorpdfstring{$g$}{g} MC functional |
| `thm:thqg-VII-non-renormalization` | `theorem` | 2587 | Scalar genus expansion for Gaussian algebras |
| `prop:thqg-VII-complexity-bounds` | `proposition` | 2666 | Complexity bounds on genus-\texorpdfstring{$g$}{g} integrand classes |
| `thm:thqg-VII-depth-classification` | `theorem` | 2769 | Shadow depth classifies gravitational theories |

 succeeded in 5.02s:
conj:bar-graph-complex
  Conjectured     chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a001fc1b/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a074cd40/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a506436b/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a7f8357c/.claude/worktrees/agent-a6d629eb/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a085ecd2/.claude/worktrees/agent-a9d63dc4/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a0c7a747/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a15e6d47/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a1766399/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a237e09b/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a277b925/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a2a46b8f/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a35dd0a7/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a3fbfc9b/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a40a6cef/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a4185af5/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a4d26dab/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a558f389/chapters/connections/feynman_diagrams.tex:227 [conjecture]
  Heuristic       .claude/worktrees/agent-a618b30c/chapters/connections/feynman_diagrams.tex:227 [conjecture]
exec
/bin/zsh -lc 'rg -n "thqg-oc-mc-equation" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
6910: Theorem~\ref{thm:thqg-oc-mc-equation}). \textbf{Proved}:
6997: (Theorem~\ref{thm:thqg-oc-mc-equation}), with the clutching
7039: (Theorem~\ref{thm:thqg-oc-mc-equation}).
10142:Theorem~\ref{thm:thqg-oc-mc-equation})
10278: (Theorem~\ref{thm:thqg-oc-mc-equation}). The BV/BRST
10495: all genera (Theorem~\ref{thm:thqg-oc-mc-equation}). The
exec
/bin/zsh -lc "sed -n '6890,7050p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 universal bulk with open color~$\cA$.
\item The \emph{local-global bridge}
 (Theorem~\ref{thm:thqg-local-global-bridge}): restriction of the
 bordered FM convolution to the formal disk identifies with
 $\mathcal{C}^\bullet_{\mathrm{ch}}(\cA, \cA)$.
 \textbf{Proved}: Morita invariance of the derived center.
\item The \emph{annulus trace theorem}
 (Theorem~\ref{thm:thqg-annulus-trace}):
 $\int_{S^1_p} \mathcal{M} \simeq HH_*(\mathcal{M})$.
 \textbf{Proved}: by Ayala--Francis $\otimes$-excision on the
 standard Weiss cover of $S^1_p$, reducing to the two-sided bar
 complex $A_b \otimes^{\mathbf{L}}_{A_b^e} A_b = HH_*(A_b)$.
 The annulus degeneration proposition
 (Proposition~\ref{prop:thqg-annulus-degeneration-kappa})
 connects this to the genus-$1$ curvature:
 $\Delta_{\mathrm{ns}}(\operatorname{Tr}_\cA) = \kappa(\cA)
 \cdot \lambda_1$.
\item The \emph{open/closed MC element}
 $\Theta^{\mathrm{oc}}_\cA = \Theta_\cA + \sum_j \mu^{\mathcal{M}_j}$
 (Construction~\ref{constr:thqg-oc-mc-element},


exec
/bin/zsh -lc "sed -n '1200,1270p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 is about which tautological class on $\overline{\cM}_g$ appears
 in the scalar trace of~$\Theta_\cA$, not about open-closed
 consistency.
\item \emph{The independent open-sector derivation.}
 Computing $F_g$ from iterated clutching on
 $\mathcal{C}_{\mathrm{op}}$ alone (without invoking the
 bar-intrinsic construction) and verifying agreement with the
 closed-sector tower is a separate programme. The MC-forced
 consistency guarantees that such a computation, if carried out,
 \emph{must} agree; it does not construct the computation.
\end{enumerate}
\end{remark}

% -------------------------------------------------------------------
\subsection{CT-2: the modular cooperad conjecture for the open sector}
\label{subsec:thqg-ct2-cooperad-conjecture}
\index{CT-2 conjecture|textbf}
\index{modular cooperad!open sector|textbf}
% -------------------------------------------------------------------

thinking
**Evaluating directory exclusions**

I’m noticing noise from .claude directories in the script. I need to focus on the root repo and exclude hidden directories, especially .claude and .git. It seems I should run the process only on live files within the current working tree and consider sibling repos if there are status conflicts. The user wants to see all chapters and connections tied to the current repo, so I'll make sure to parse only what's necessary.
thinking
**Inspecting label conflicts**

I need to determine if the same label exists elsewhere before editing the current repo. I’m considering using grep across volumes manually and possibly running rg on sibling repos — though they’ll be read-only. The instructions suggest that I should check all three volumes for shared statuses. I’ll avoid editing outside the current repo but can still inspect for conflicts. I want to ensure I have a solid inventory of label conflicts, so I’ll focus on the relevant .tex files. Let's execute the script!

thinking
**Analyzing ClaimStatus mismatches across files**

I'm exploring whether theorem claim statuses in the chapters/connections folder conflict with other occurrences in the repo or with summaries in concordance.tex. I'll check for labels repeated with differing statuses, focusing on the possibility of drift or duplicates by searching claim statuses and label appearances in multiple files. This might help isolate a few key mismatches to highlight.
exec
/bin/zsh -lc 'rg -n "thqg-oc-mc-equation" -n' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
metadata/dependency_graph.dot:862:  thm_thqg_oc_mc_equation [label="thm:thqg-oc-mc-equation\ntheorem [Pr]\nOpen/closed MC equation", style=filled, fillcolor="#c8e6c9"];
metadata/theorem_registry.md:3010:| `thm:thqg-oc-mc-equation` | `theorem` | 979 | Open/closed MC equation |
chapters/examples/heisenberg_eisenstein.tex:2445:(Theorem~\ref{thm:thqg-oc-mc-equation}) encodes all cooperad
chapters/examples/heisenberg_eisenstein.tex:2503: (Theorem~\ref{thm:thqg-oc-mc-equation}):
chapters/connections/thqg_open_closed_realization.tex:929:(Theorem~\ref{thm:thqg-oc-mc-equation}(d)), the clutching
chapters/connections/thqg_open_closed_realization.tex:979:\label{thm:thqg-oc-mc-equation}
chapters/connections/thqg_open_closed_realization.tex:983:\begin{equation}\label{eq:thqg-oc-mc-equation}
chapters/connections/thqg_open_closed_realization.tex:1013:The equation~\eqref{eq:thqg-oc-mc-equation} is the
chapters/connections/thqg_open_closed_realization.tex:1108:\textup{(}Theorem~\textup{\ref{thm:thqg-oc-mc-equation})}
chapters/connections/thqg_open_closed_realization.tex:1159:Theorem~\ref{thm:thqg-oc-mc-equation}. Each genus-$g$
chapters/connections/thqg_open_closed_realization.tex:1163:Theorem~\ref{thm:thqg-oc-mc-equation}(a)--(d).
chapters/connections/thqg_open_closed_realization.tex:1320: recorded in Theorem~\ref{thm:thqg-oc-mc-equation}(a). This fixes
chapters/connections/concordance.tex:6910: Theorem~\ref{thm:thqg-oc-mc-equation}). \textbf{Proved}:
chapters/connections/concordance.tex:6997: (Theorem~\ref{thm:thqg-oc-mc-equation}), with the clutching
chapters/connections/concordance.tex:7039: (Theorem~\ref{thm:thqg-oc-mc-equation}).
chapters/connections/concordance.tex:10142:Theorem~\ref{thm:thqg-oc-mc-equation})
chapters/connections/concordance.tex:10278: (Theorem~\ref{thm:thqg-oc-mc-equation}). The BV/BRST
chapters/connections/concordance.tex:10495: all genera (Theorem~\ref{thm:thqg-oc-mc-equation}). The
chapters/connections/thqg_entanglement_programme.tex:64: & \ref{thm:thqg-oc-mc-equation} \\
metadata/label_index.json:21122:  "eq:thqg-oc-mc-equation": {
exec
/bin/zsh -lc "python3 - <<'PY'
import pathlib,re,os
roots=[pathlib.Path('/Users/raeez/chiral-bar-cobar'),pathlib.Path('/Users/raeez/chiral-bar-cobar-vol2'),pathlib.Path('/Users/raeez/calabi-yau-quantum-groups')]
status_re=re.compile(r'\\\\ClaimStatus(ProvedHere|ProvedElsewhere|Conjectured|Conditional|Heuristic|Open)')
begin_re=re.compile(r'\\\\begin\\{(["'^}]+)'"\\}')
label_re=re.compile(r'\\\\label\\{(["'^}]+)'"\\}')
ignore_parts={'.git','.claude','archive','healing_20260413_130533','healing_20260413_132214','resume_20260413_165929','fix_wave_B_20260413_171623'}
occ=[]
for root in roots:
    if not root.exists():
        continue
    for p in root.rglob('*.tex'):
        if any(part in ignore_parts for part in p.parts):
            continue
        try:
            lines=p.read_text().splitlines()
        except Exception:
            continue
        i=0
        while i < len(lines):
            line=lines[i]
            if '\\\\begin{' in line and 'ClaimStatus' in line:
                env=begin_re.search(line)
                status=status_re.search(line)
                label=label_re.search(line)
                j=i
                while (status is None or label is None) and j+1 < len(lines) and j < i+8:
                    j += 1
                    nxt=lines[j]
                    if status is None:
                        status=status_re.search(nxt)
                    if label is None:
                        label=label_re.search(nxt)
                if status and label:
                    occ.append((label.group(1), status.group(1), str(p), i+1, env.group(1) if env else '?'))
                    i=j
            i += 1
from collections import defaultdict
by=defaultdict(list)
for item in occ:
    by[item[0]].append(item)
for label in sorted(by):
    items=by[label]
    statuses={x[1] for x in items}
    if len(statuses)>1 and any('/chapters/connections/' in x[2] and x[2].startswith('/Users/raeez/chiral-bar-cobar/') for x in items):
        print(label)
        for st,path,line,env in sorted((x[1], os.path.relpath(x[2], '/Users/raeez'), x[3], x[4]) for x in items):
            print(f'  {st:15} {path}:{line} [{env}]')
PY" in /Users/raeez/chiral-bar-cobar succeeded in 558ms:
thm:general-hs-sewing
  ProvedElsewhere chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex:154 [theorem]
  ProvedHere      chiral-bar-cobar/chapters/connections/genus_complete.tex:1385 [theorem]
thm:twisted-ym-boundary-brst
  ProvedElsewhere chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:53 [theorem]
  ProvedHere      chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:186 [theorem]
  ProvedHere      chiral-bar-cobar/chapters/connections/ym_boundary_theory.tex:204 [theorem]
thm:twisted-ym-tangent-center
  ProvedElsewhere chiral-bar-cobar-vol2/chapters/connections/ym_synthesis_core.tex:90 [theorem]
  ProvedHere      chiral-bar-cobar-vol2/chapters/connections/ym_boundary_theory.tex:212 [theorem]
  ProvedHere      chiral-bar-cobar/chapters/connections/ym_boundary_theory.tex:230 [theorem]
exec
/bin/zsh -lc 'rg -n -C2 "MC5" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2167-\end{remark}
2168-
2169:\begin{remark}[Research remark: class~$\mathsf{M}$ spectral and completed MC5]
2170-\label{rem:bv-bar-class-m-frontier}
2171-\index{BV algebra!class M frontier|textbf}%
--
2174-Proposition~\ref{prop:chain-level-three-obstructions} isolate not
2175-only the surviving coderived statement but also the exact reason the
2176:strict chain-level form of MC5 fails for class~$\mathsf{M}$. For
2177-Virasoro and principal $\cW_N$, the higher harmonic discrepancies
2178-satisfy
--
2205-supplies the corresponding coderived spectral sequence, with strict
2206-$E_1$ page because the curvature lies in positive filtration. The
2207:research target is a spectral form of MC5 whose higher differentials
2208-record the harmonic classes $c_r(\cA)$ and whose abutment is a
2209-coacyclic cone. This replaces a false strict chain identity by a
--
2248-with the proved coderived theorem. On the current record, this
2249-filtered-completed spectral statement is the sharpest plausible
exec
/bin/zsh -lc "sed -n '1400,1455p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
[\mathfrak{C}(\cA) \star_{P_\cA} \mathfrak{C}(\cA)]
\;\in\;
H^2\!\bigl(\mathcal{C}^{\bullet}_{\mathrm{ch}}(\cA, \cA),\, \delta\bigr)
\;=\; \mathcal{Z}^2,
\end{equation}
where $\mathfrak{C}(\cA)$ is the cubic shadow
(eq.~\eqref{eq:nms-cubic-shadow}),
$H_\cA$ is the Hessian (the quadratic shadow, i.e.\ the modular
characteristic $\kappa(\cA)$ on the one-dimensional primary slice),
$P_\cA = H_\cA^{-1}$ is the propagator, and
$(\mathfrak{C} \star_{P_\cA} \mathfrak{C})(x_1, x_2, x_3, x_4)
:= \sum_\alpha \mathfrak{C}(x_1, x_2, e_\alpha)\, P_\cA^{\alpha\beta}\,
\mathfrak{C}(e_\beta, x_3, x_4)$
is the sewing product contracting one pair of indices with the
propagator. The first term is the local quartic contact;
the second is the tree correction from two cubic emissions joined
by one propagator.
\end{construction}

\begin{theorem}[Vanishing and nonvanishing of
exec
/bin/zsh -lc 'rg -n "thqg-local-global-bridge" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
6892: (Theorem~\ref{thm:thqg-local-global-bridge}): restriction of the
6973: (Theorem~\ref{thm:thqg-local-global-bridge}(iii)).
6988: (Theorem~\ref{thm:thqg-local-global-bridge}).
8896:(Theorem~\ref{thm:thqg-local-global-bridge}(i))
8995:of Theorem~\ref{thm:thqg-local-global-bridge}.
11053: (Theorem~\ref{thm:thqg-local-global-bridge}) identifies the
exec
/bin/zsh -lc "sed -n '8872,8910p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
higher-degree shadows of $\cA$ and $\cA^!$ via the
Verdier involution, but the constraint is \emph{not}
$\Theta_\cA + \Theta_{\cA^!} = 0$: at the scalar level,
$\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$
, and the full-tower relation is
$\mathbb{D}(\Theta_\cA) = \Theta_{\cA^!}$
(Verdier intertwining, not negation).
The complementarity sum
$S_{\mathrm{EE}}^{\mathrm{scalar}}(\mathrm{Vir}_c)
+ S_{\mathrm{EE}}^{\mathrm{scalar}}(\mathrm{Vir}_{26-c})
= \tfrac{26}{3}\log(L/\epsilon)$
follows from the proved $\kappa + \kappa' = 13$
identity, not from a conjectural
$\Theta + \Theta' = 0$.

\smallskip\noindent
\textbf{(21)~Canonical cyclotomic boundary chart from root stacks}%
\label{item:concordance-cyclotomic-chart}%
\index{cyclotomic chart!canonical|textbf}%
\index{root stack!boundary chart|textbf}%
exec
/bin/zsh -lc "sed -n '1080,1215p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,730p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1260,1385p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\item \emph{Universal MC duality.}
The universal Maurer--Cartan classes satisfy
$\Theta_{\widehat{\fg}_k} + \Theta_{\widehat{\fg}_{-k-2h^\vee}}
= 0$ (Theorem~\ref{thm:explicit-theta}), since
$\kappa(\widehat{\fg}_k) + \kappa(\widehat{\fg}_{-k-2h^\vee}) = 0$
by Theorem~\ref{thm:genus-universality}(ii).
The chain-level mechanism underlying~(c) is:
the Verdier involution exchanges
$\Theta_{\widehat{\fg}_k}$ and $-\Theta_{\widehat{\fg}_{k'}}$,
producing the Lagrangian splitting of
Theorem~\ref{thm:quantum-complementarity-main}.
\end{enumerate}
\end{corollary}

\begin{proof}
Part~(a) is the cohomology-level consequence of
Theorem~\ref{thm:bar-semi-infinite-km}. Part~(b): the
curvature $m_0 = \kappa \cdot \mathbf{1}$ in the bar complex
corresponds, under the quasi-isomorphism~$\Psi$, to the
 succeeded in 50ms:
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

The physical content (Gaiotto's framework, boundary chiral
algebras, HT boundary conditions, W-algebras from Higgs branches)
is in Volume~II\@. The BV algebra structure on the bar complex
from configuration-space geometry is in
\S\ref{sec:complete-bv-structure}.

% Labels preserved for cross-reference compatibility.
\label{rem:ht-from-n4-sym}%
\label{rem:boundary-chiral-algebra-bv}%
\label{rem:bar-cobar-ht-boundary}%
% conj:holographic-bar-cobar defined in genus_complete.tex
\label{rem:w-algebra-bar-cobar}%


\section{The BV algebra structure}
\label{sec:complete-bv-structure}

\subsection{BV algebra definition}

 succeeded in 51ms:
Conjecture~\ref{conj:dk-compacts-completion}) is downstream of MC3.
MC4 on the $\mathcal{W}_\infty$ tower is
\textbf{unconditionally closed} at all stages via
$\mathcal{W}_N$ rigidity
(Theorem~\ref{thm:winfty-all-stages-rigidity-closure})
within the strong completion-tower framework
(Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
Yangian tower is closed on the evaluation-generated core ($249$~tests);
the DK-$5$ categorical packet in type~$A$ is now accessible
(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
genus~$0$ and genus~$1$ is proved
(Theorems~\ref{thm:genus1-universal-curvature}
and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
(Theorem~\ref{thm:inductive-genus-determination}),
two-dimensional convergence
(Proposition~\ref{prop:2d-convergence}),
and the HS-sewing criterion
(Theorem~\ref{thm:general-hs-sewing}).
\emph{Critical point}: MC3 package~(i) (categorical CG) is now
resolved for all types
exec
/bin/zsh -lc 'rg -n "conj:ct2" -n chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "CT-2" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'rg -n "ClaimStatusConjectured" chapters/connections/thqg_open_closed_realization.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1233:\ClaimStatusConjectured

exec
/bin/zsh -lc "sed -n '1210,1245p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
\end{remark}

% -------------------------------------------------------------------
\subsection{CT-2: the modular cooperad conjecture for the open sector}
\label{subsec:thqg-ct2-cooperad-conjecture}
\index{CT-2 conjecture|textbf}
\index{modular cooperad!open sector|textbf}
% -------------------------------------------------------------------

The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
carries cocomposition maps read off from clutching on bordered
Fulton--MacPherson compactifications, and at genus~$1$ the
annulus trace recovers the open-closed identification proved in
Theorem~\ref{thm:thqg-mc-forced-consistency}. The structural question
left open by that theorem is whether these partial data assemble into
a \emph{modular cooperad} in the sense of Getzler--Kapranov
\cite{GetzlerKapranov98}, and whether the assembled structure is
determined by the open-closed MC element $\Theta^{\mathrm{oc}}_\cA$.
We record the expected answer as a conjecture and give a five-phase
thinking
**Investigating MC5 status**

I need to infer something from the red-team’s "MC5 status." It seems like the bv_brst.tex file indicates that the MC5 status is definitive when it perhaps should be conditional. That's because it depends on `cor:standard-tower-mc5-closure` or a similar factor. I should really inspect the bv_brst file to find where "MC5" is mentioned. Let’s search for that to clarify this dependency!
exec
/bin/zsh -lc "rg -n -C 4 -i 'MC5|mc5|standard-tower-mc5|bar-semi-infinite|algebraic-string-dictionary|master-theta|BV/BRST|physics completion|conditional' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
35-$\mathsf{L}$, and~$\mathsf{C}$ admit stronger chain-level statements
36-than class~$\mathsf{M}$. The higher-genus comparison is resolved in
37-$D^{\mathrm{co}}$ because the harmonic discrepancy factors through
38-the curvature and the resulting cone is $m_0$-torsion, hence
39:coacyclic. The stronger chain-level statement is unconditional for
40:classes~$\mathsf{G}$ and~$\mathsf{L}$, conditional for
41-class~$\mathsf{C}$ on harmonic decoupling, and open for
42-class~$\mathsf{M}$. The Heisenberg case is resolved at the
43-scalar level at all genera:
44-$F_g^{\mathrm{BV}}(\cH_\kappa) = F_g^{\mathrm{bar}}(\cH_\kappa)
--
262-inserts a diagonal residue, contracting the logarithmic form $\eta_{ij}$ via a
263-delta-function along $D_{ij}$. This is the loop-insertion operator in the bar
264-complex, distinct from the cobar functor $\Omega$ (which recovers $\cA$ from
265-$B(\cA)$ by bar-cobar inversion, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
266:The precise algebraic version of this operator is conditional
267-\textup{(}Theorem~\ref{thm:config-space-bv}\textup{)}.
268-\end{definition}
269-
270-\begin{remark}[Heuristic QME/MC comparison; \ClaimStatusHeuristic]

exec
/bin/zsh -lc 'rg -n "thqg_entanglement" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

thinking
**Identifying theorem status**

I need to check the MC5 status in the bv_brst.tex document. I’m thinking of searching for a specific theorem that might be labeled as the algebraic-string-dictionary. It might be helpful to examine around line 380, as well as looking at lines 39-42 for relevant status info. I guess I should start by viewing the top of the file to get a better context. Let's see what I can find!
exec
/bin/zsh -lc "sed -n '1,120p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '360,520p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1380,1705p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '600,840p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{BV-BRST formalism and Gaiotto's perspective}
\label{ch:bv-brst}
\index{Batalin--Vilkovisky|see{BV algebra}}

The physicist's BRST cohomology and the algebraist's bar resolution
are not analogous: they are the same computation. The BV formalism
is a machine for computing derived functors; the bar complex is a
machine for computing derived functors; at genus~$0$, they are the
same machine applied to the same input. Costello's formulation of
perturbative QFT as the theory of derived moduli problems makes the
identification inevitable: the BRST operator computes the derived
space of gauge-equivalence classes, which is what the bar differential
computes on the algebraic side. What requires proof is not the
coincidence but the precise scope of the agreement.

The BV Laplacian and the sewing operator agree at genus~$0$. The
quantum master equation $\hbar \Delta S + \tfrac12\{S,S\} = 0$ of
the BV formalism coincides on $\mathbb{P}^1$ with the bar
differential $d_{\mathrm{bar}}$ of the chiral algebra: the
BRST operator $Q_{\mathrm{BRST}}$ is the bar differential, the
 succeeded in 51ms:
\end{theorem}

\begin{example}[Free \texorpdfstring{$bc$}{bc} ghost system]
The $bc$ system has fields $b(z)$ of weight $\lambda$ and $c(z)$ of weight $1-\lambda$, OPE $b(z)c(w) \sim (z-w)^{-1}$, central charge $c_{bc} = 1 - 3(2\lambda - 1)^2$, and BRST operator $Q = \oint c(z) \bigl(T_{\text{matter}}(z) + \tfrac{1}{2}T_{\text{ghost}}(z)\bigr) dz$.

For the bosonic string, $\lambda = 2$ (so $b$ has weight~$2$ and $c$ has weight~$-1$), giving $c_{\text{ghost}} = 1 - 3(3)^2 = -26$ and ghost stress tensor $T_{\text{ghost}} = -2b\,\partial c - (\partial b)\,c$.

On the relative complex $\ker(b_0) \cap \ker(L_0^{\mathrm{tot}})$,
the BRST nilpotence condition is:
\[
Q_{\mathrm{BRST}}^2 = 0
\iff c_{\mathrm{matter}} + c_{\mathrm{ghost}} = 0,
\quad\text{i.e., } c_{\mathrm{matter}} = 26
\]
(on the full complex, $Q_{\mathrm{BRST}}^2 = \tfrac{c-26}{12}\,c_0$;
see Lemma~\ref{lem:brst-nilpotence}).

In the bar complex, the residue component $d_{\mathrm{res}}$
of the bar differential heuristically corresponds to $Q_{\mathrm{BRST}}$
under the identification of Theorem~\ref{thm:bv-bar-geometric}.
 succeeded in 51ms:
a lifting problem: the obstruction to extending lies in
$H^{n+1}(\mathrm{gr}^N\,\barB^{\mathrm{ch}}_0)$, which is the
$(n+1)$-st cohomology of the classical bar complex at weight~$N$.
Since the classical bar complex of a Lie algebra is acyclic in
sufficiently high degree (by the Koszul resolution), the obstructions
vanish degree by degree, and the induction proceeds.

The map $\Phi$ so constructed is a filtered chain map inducing an
isomorphism on $E_1$ pages. By the Eilenberg--Moore comparison
theorem, $\Phi$ is a quasi-isomorphism.
\end{proof}

\begin{remark}[BV/BRST reading of the master square]
\label{rem:bv-convergence}
\index{BV complex!convergence with bar complex}
Theorem~\ref{thm:brst-bar-genus0} realizes the parallel-track identifications of Remarks~\ref{rem:bv-parallel-track} and~\ref{rem:anomaly-parallel-track}: in~\eqref{eq:master-square}, $\barB_X(\cA)$ is the BV complex, $\barB_X(\cA^!)$ the ghost complex, $\mathbb{D}_{\mathrm{Ran}}$ the field--antifield exchange, and $\dfib^{\,2} = \kappa \cdot \omega_1$ the conformal anomaly. The square commutes precisely when $\kappa = 0$.
\end{remark}

\begin{remark}[Explicit form of \texorpdfstring{$\Phi$}{math}]\label{rem:brst-bar-explicit}
For the bosonic string $\cA = \mathcal{H}^{26}$, the chain map
 succeeded in 51ms:
Functoriality of the underlying bar construction is standard. The
extra BV functoriality and lax monoidal statements are exactly the
assumed functorial and tensor-compatibility properties of the
conditional BV package, while the Verdier-duality comparison is part
of the additional hypothesis in the theorem statement.
\end{proof}

\begin{remark}[Shifted symplectic structure from BV]\label{rem:bv-shifted-symplectic}
\index{shifted symplectic!from BV}
Conditional on Theorems~\ref{thm:config-space-bv}
and~\ref{thm:bv-functor}, the BV bracket on
$\barB^{\mathrm{ch}}(\cA)$ would provide a bar-side
$(-1)$-shifted Poisson model for the deformation theory. The
unconditional shifted-symplectic statements used later in the
manuscript instead come from the Verdier pairing on
$C_g = R\Gamma(\overline{\mathcal{M}}_g,\mathcal{Z}(\cA))$
\textup{(}Proposition~\ref{prop:ptvv-lagrangian}\textup{)} and from
the ambient cyclic deformation formal moduli problem
\textup{(}Theorem~\ref{thm:ambient-complementarity-fmp}\textup{)}.
\end{remark}
exec
/bin/zsh -lc "sed -n '8150,8195p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
coefficients of this deformation in the parameter
$k + h^\vee$.
\end{remark}

% ============================================================
\subsection{Three Langlands gaps}
\label{subsec:concordance-langlands-gaps}
\index{Langlands programme!structural gaps}

The spectral continuation programme
(\S\ref{subsec:concordance-spectral-continuation} below)
explores arithmetic consequences of the shadow obstruction tower.
Before entering that programme, we state three structural
gaps between the proved core of this monograph and any
Langlands-type statement. These are not technical
difficulties awaiting a clever argument; they are
category-level separations between the objects this
monograph constructs and the objects the Langlands
programme requires.

exec
/bin/zsh -lc "rg -n -C 3 'thm:algebraic-string-dictionary|algebraic string dictionary|master-bv-brst|v1-master-bv-brst|BV/BRST comparison|WZW/genus' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1404-\index{BV algebra!bar complex identification!Heisenberg}
1405-
1406-The free-field case resolves
1407:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
1408-for the Heisenberg family. The proof uses four independent
1409-arguments that all produce the same identity.
1410-
--
1626-\label{rem:heisenberg-bv-bar-scope}
1627-\index{BV algebra!bar complex identification!scope}
1628-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
1629:Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
1630-\textup{(}partition function\slash free energy\textup{)} for the
1631-Heisenberg family at all genera.
1632-The Heisenberg succeeds because it is class~G:
--
1660-\index{BV algebra!chain-level obstructions|textbf}
1661-\index{chain-level BV/bar identification}
1662-The chain-level identification
1663:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
exec
/bin/zsh -lc 'rg -n "ClaimStatusProvedHere.*thqg" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Evaluating time periods**

I need to look into the period from 1760 to 1910, possibly focusing on some theorems from that time. It seems like there might be interesting developments during this era that would be worth exploring and labeling. It's intriguing to think about what theories emerged then! I want to make sure to gather enough information before diving deeply into the details.
exec
/bin/zsh -lc "sed -n '1760,1925p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
central insertion with that degree is
$m_0^{\lfloor r/2 \rfloor - 1}$. Therefore
\[
\delta_r^{\mathrm{harm}}
\;=\;
c_r(\cA)\cdot m_0^{\lfloor r/2 \rfloor - 1}
\qquad\text{for every } r \geq 4.
\]
For class~G, there are no interaction vertices, so every
$c_r(\cA)$ vanishes. For class~L
\textup{(}affine Kac--Moody at non-critical level
$k \neq -h^\vee$\textup{)}, the interaction vertex is the
structure-constant tensor $f^{abc}$. The cubic harmonic
correction has the form
$\sum_c f^{abc}\cdot I_{\mathrm{harm}}(z_1,z_2)\cdot f^{cde}$,
where $I_{\mathrm{harm}}$ is the integral of the harmonic
propagator against the cubic vertex measure. Antisymmetry of
$f^{abc}$ and the Jacobi identity
$f^{abc}f^{cde} + \text{cyclic} = 0$ force this coefficient to
vanish, and shadow depth $r_{\max} = 3$ excludes quartic and
exec
/bin/zsh -lc 'rg -n "BV complex" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
10230: for every chirally Koszul algebra~$\cA$, the BV complex and the

exec
/bin/zsh -lc "sed -n '10210,10250p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \delta F_2^{\mathrm{grav}}(\cW_N, c)
 = \frac{(N{-}2)(N{+}3)}{96}
 + \frac{(N{-}2)(3N^3 + 14N^2 + 22N + 33)}{24c},
 \]
 vanishing if and only if $N = 2$ (Virasoro: uniform-weight).
 Exact for $\cW_3$; a lower bound for $N \geq 4$
 (higher-spin exchange adds positive corrections).
 The cross-channel tower through genus~$4$ is recorded in
 Computations~\ref{comp:w3-genus3-cross}
 and~\ref{comp:w3-genus4-cross}; at genus~$3$,
 the cross-channel correction already exceeds the scalar
 part by a factor of~$1.35$ at large~$c$.

\item \textbf{BV/BRST $=$ bar at higher genus}
 (Conjecture~\ref{conj:v1-master-bv-brst}).

 \smallskip\noindent
 \emph{Resolution in $D^{\mathrm{co}}$.}
 \textbf{Resolved} in the coderived category
 (Theorem~\ref{thm:bv-bar-coderived}):
thinking
**Inspecting theorem labels**

I think I might need to check the remark status, as it refers to a chain-level class G/L equivalence. This might depend on some propositions or theorems. The user is particularly concerned about the MC5 status, so I should look closely at the beginning of the file. I'll examine theorem labels around 825, 918, and 1031 to identify any suspicious statuses. I’ll also check around the specific label for `thm:algebraic-string-dictionary`.
exec
/bin/zsh -lc "rg -n '\\\\label\\{["'^}]+'"\\}' chapters/connections/bv_brst.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2:\label{ch:bv-brst}
59:\label{rem:brst-anomaly-gkw}
76:\label{rem:bv-bar-bridge}
105:\label{rem:modular-qme-bv}
113:\begin{equation}\label{eq:modular-qme-bv}
157:\label{rem:sft-bar-identification}
171:\label{def:bv-data-chiral}
185:\label{thm:bv-bar-geometric}
250:\label{def:bv-laplacian}
271:\label{rem:qme-bar-cobar}
291:\label{subsec:bv-bar-identification}
295:\ClaimStatusHeuristic]\label{rem:genus0-amplitude-bar}
322:\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
328:\begin{remark}[Anomaly = curvature]\label{rem:anomaly-curvature-bv}
338:\label{def:brst-operator}
357:\label{thm:brst-physical-states}
386:\label{thm:log-form-ghost-law}
431:\label{conj:bar-topological-brst}
443:\label{sec:brst-bar-chain-map}
454:\begin{equation}\label{eq:brst-differential}
exec
/bin/zsh -lc 'rg -n "v1-master-bv-brst" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1407:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
1629:Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
1663:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
1797:(Conjecture~\ref{conj:v1-master-bv-brst})
1850:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
exec
/bin/zsh -lc 'rg -n "conj:v1" chapters/connections/bv_brst.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1407:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
1629:Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
1663:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)}
1797:(Conjecture~\ref{conj:v1-master-bv-brst})
1850:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
exec
/bin/zsh -lc "if [ -f suspicious_proved_claim_dependencies.csv ]; then rg -n 'bv_brst|concordance|MC5|mc5' suspicious_proved_claim_dependencies.csv; else echo 'missing suspicious_proved_claim_dependencies.csv'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
missing suspicious_proved_claim_dependencies.csv
exec
/bin/zsh -lc "rg -n \"label\\{conj:v1-master-bv-brst\" -n" in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
chapters/connections/outlook.tex:674:\phantomsection\label{conj:v1-master-bv-brst-outlook}
relaunch_20260413_111534/F10_prerequisites_MC1_5.md:1667:chapters/connections/editorial_constitution.tex:434:\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1624:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1651:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1709:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1797:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1870:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:1958:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2031:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2119:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2231:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2319:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2397:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2485:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2580:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2668:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2797:+\label{conj:v1-master-bv-brst}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2885:+\phantomsection\label{conj:v1-master-bv-brst-outlook}
fix_wave_A_20260413_112727/A15_fix_duplicate_labels_v1.md:2989:+\label{conj:v1-master-bv-brst}
exec
/bin/zsh -lc "sed -n '400,450p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
exec
/bin/zsh -lc 'rg -n "v1-master-bv-brst" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
725: class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
1989: conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
3383: (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
4756:genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
7744:\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
7905: (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
10224: (Conjecture~\ref{conj:v1-master-bv-brst}).
11155: \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
11282: conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
collab wait(call_7Oskvh2FJKoD4Ep2KmiyKv6x)
  receivers: 019d8773-3334-74d2-8498-5c20d9febadf
exec
/bin/zsh -lc "sed -n '7720,7760p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\operatorname{grt}_1(\text{weight }4) = 0$,
so the filtration-$4$ coefficient is a coboundary with
no free parameter. The spectral Drinfeld class vanishes at
filtration~$4$. Beyond filtration~$4$,
$\operatorname{grt}_1$ is nonzero at all odd weights
$\geq 3$; at even weights,
$\dim\operatorname{grt}_1 = 0$ for
weights $4$ and~$6$, then
$\dim\operatorname{grt}_1(\text{weight }8) = 1$
\textup{(}from $[\sigma_3, \sigma_5]$\textup{)},
$\dim\operatorname{grt}_1(\text{weight }10) = 1$
\textup{(}from $[\sigma_3, \sigma_7]$\textup{)}, and
$\dim\operatorname{grt}_1(\text{weight }12) = 2$
\textup{(}one Ihara-reduced bracket $+$ the cusp
form~$\Delta_{12}$\textup{)}.
The spectral Drinfeld class must be analysed
case by case at weights $\geq 8$.
\end{remark}

\begin{remark}[Frontier status of the ten load-bearing conjectures, as of 2026]
exec
/bin/zsh -lc "rg -n 'conj:v1-vassiliev-bar' -n metadata/claims.jsonl" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
291:{"label": "conj:v1-vassiliev-bar", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 1781, "title": "Vassiliev invariants from bar complex", "refs_in_block": ["thm:prism-higher-genus"], "cites_in_block": ["BarNatan95"]}

thinking
**Summarizing status consistency checks**

I’m compiling a detailed summary confirming no conflicting ClaimStatus drift after cross-checking `metadata/claims` and key files like `editorial_constitution.tex` and `concordance.tex`. I’ll highlight MC5 status details from `bv_brst.tex` with relevant line references and note concordance statuses match stated surfaces, providing a concise bullet list covering each requested focus area with file, line, label, status, and any recommendations.
codex
- **ClaimStatus drift:** Checked every label in `chapters/connections` that participates in the “ten load-bearing conjectures” list (e.g., `conj:v1-master-bv-brst` at `chapters/connections/editorial_constitution.tex:434` is still marked `\ClaimStatusConjectured`, and `metadata/claims.jsonl:291` records the same status), and no other cross-file label occurs with a different ClaimStatus elsewhere in the repo. Verdict: no reportable drift; no fix needed.

- **MC5 packages:** `chapters/connections/bv_brst.tex:2169-2250` re‑states that the coderived BV/bar identification (`thm:bv-bar-coderived`) survives for all classes while the strict MC5 comparison fails for class M (higher-order harmonic obstructions) and is now phrased as a spectral/completed upgrade; the subsequent conjecture in the same file (`chapters/connections/bv_brst.tex:2508-2513`) leaves the higher‑genus handle-gluing comparison (the backbone of MC5 beyond genus 0) open. Recommendation: leave the coderived statement as proved, and keep the spectral/completed MC5 conjecture explicitly labelled `ClaimStatusConjectured` until a filtered comparison is constructed.

- **Concordance statuses:** The concordance text (`chapters/connections/concordance.tex:7744-7758` and surrounding discussion of the frontier ten) explicitly records the BV/BRST/bar conjecture as “open but resolved in \(D^{\mathrm{co}}\)” and links to the same label and context as the source files, so nothing there contradicts the individual surfaces’ status tags. No additional mismatches spotted; no further action required.
wait(call_7Oskvh2FJKoD4Ep2KmiyKv6x) 1 agents complete:
  019d8773-3334-74d2-8498-5c20d9febadf completed: "- **ClaimStatus drift:** Checked every label in `chapters/connections` that participates in the “ten load-bearing conjec…"
codex
The cross-file label scan came back clean except for one genuine live drift surface outside the two target files. I’m now checking the status prose inside `concordance.tex` itself, because that file contains manual status summaries that do not show up as label conflicts.
exec
/bin/zsh -lc "sed -n '7728,7770p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7768,7810p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1380,1425p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '130,180p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (Remark~\ref{rem:beyond-hook-rectangular}).
\item \textup{Conjecture~\ref{conj:d-module-purity-koszulness} ($\cD$-module purity $\Rightarrow$ Koszulness).}
 Forward direction proved. Converse reduces to PBW~$=$~Saito weight filtration;
 proved for KM (Proposition~\ref{prop:d-module-purity-km-equivalence}), open for rank~$\geq 2$
 $\cW$-algebras. The principal $\cW_N$ case at generic central charge
 is Conjecture~\ref{conj:d-module-purity-wn-principal}, conditional on
 compatibility of principal DS reduction with the Kashiwara filtration.
\end{enumerate}
\end{remark}

\begin{remark}[Chromatic-shadow correspondence]
\label{rem:chromatic-shadow-correspondence}
\ClaimStatusConjectured
\index{chromatic filtration!shadow correspondence}
The genus spectral sequence (Construction~\ref{const:vol1-genus-spectral-sequence}) with $E_1$ page isolating tree ($p=0$), one-loop ($p=1$), genus-$2$ shell ($p=2$) data admits a conjectural identification with the chromatic filtration in stable homotopy theory. At each chromatic height~$n$, the $E(n)$-localization of the spectral Steinberg object (Vol~II, the spectral-braiding chapter) should recover the genus-$n$ shell of the shadow obstruction tower:
\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{lll}
\textbf{Chromatic height} & \textbf{Shadow shell} & \textbf{Classical avatar} \\
\hline
 succeeded in 52ms:
$\dim\operatorname{grt}_1(\text{weight }8) = 1$
\textup{(}from $[\sigma_3, \sigma_5]$\textup{)},
$\dim\operatorname{grt}_1(\text{weight }10) = 1$
\textup{(}from $[\sigma_3, \sigma_7]$\textup{)}, and
$\dim\operatorname{grt}_1(\text{weight }12) = 2$
\textup{(}one Ihara-reduced bracket $+$ the cusp
form~$\Delta_{12}$\textup{)}.
The spectral Drinfeld class must be analysed
case by case at weights $\geq 8$.
\end{remark}

\begin{remark}[Frontier status of the ten load-bearing conjectures, as of 2026]
\label{rem:concordance-frontier-status-2026}
\index{open conjectures!frontier status 2026}
The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
\begin{enumerate}
\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
 \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
\item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
 Restricted DK-4 on the evaluation-generated core is the next step.
 succeeded in 52ms:
pairs of pants; each sewing circle contributes one pair-of-pants
composition. Composition of two Hilbert--Schmidt operators is
trace class.
\end{proof}

\begin{theorem}[General HS-sewing criterion; \ClaimStatusProvedHere]%
\label{thm:general-hs-sewing}%
\index{HS-sewing!general criterion|textbf}%
Let\/ $\cA$ be a positive-energy chiral algebra with
\textup{(i)}~subexponential sector growth $\log\dim H_n = o(n)$
and \textup{(ii)}~polynomial OPE growth
$|C^{c,k}_{a,i;\,b,j}| \leq K(a+b+c+1)^N$.
Then $\cA$ satisfies HS-sewing for every $0 < q < 1$.
\end{theorem}

\begin{proof}
\[
\|m_{a,b}^c\|_{\mathrm{HS}}^2
\;\leq\;
\dim H_a \cdot \dim H_b \cdot \dim H_c
 succeeded in 52ms:
\begin{proposition}[Pair-of-pants as HS operator; \ClaimStatusProvedElsewhere]
% label removed: prop:thqg-I-pants-hs
\index{pair of pants!HS operator}
Under HS-sewing~\eqref{V1-eq:thqg-I-hs-sewing-condition}, the $q$-weighted multiplication operator $m_q \colon \mathcal{H}_q(\cA) \,\widehat{\otimes}\, \mathcal{H}_q(\cA) \to \mathcal{H}_q(\cA)$ is Hilbert--Schmidt, with
\begin{equation}% label removed: eq:thqg-I-mq-hs-bound
\|m_q\|_{\HS}^2 \;=\; \sum_{a,b,c \geq 0} q^{a+b+c}\,\|m^c_{a,b}\|_{\HS}^2 \;<\; \infty.
\end{equation}
Consequently, every closed amplitude on a genus-$g$ surface obtained by sewing is trace class.
\end{proposition}

\begin{proof}
Direct from the definition: $\|m_q\|_{\HS}^2$ is precisely the left-hand side of~\eqref{V1-eq:thqg-I-hs-sewing-condition}. A genus-$g$ surface with $n$ punctures is obtained by sewing $2g - 2 + n$ pairs of pants along $3g - 3 + n$ circles. Each sewing circle contributes one pair-of-pants composition. By the Hilbert--Schmidt composition inequality~\eqref{V1-eq:thqg-I-hs-composition}, each composition of two HS operators gives a trace-class operator. Since $g \geq 1$ requires at least two compositions, and trace-class operators form an ideal, the result follows.
\end{proof}

\begin{remark}[Sewing topology]
% label removed: rem:thqg-I-sewing-topology
\index{sewing!topology}
The pair-of-pants decomposition of a genus-$g$ surface $\Sigma_{g,n}$ into $2g - 2 + n$ trinions and $3g - 3 + n$ sewing circles is determined by a pants graph $\Gamma_P$. Different choices of $\Gamma_P$ give different factorizations of the sewing operator, but the trace (the partition function) is independent of $\Gamma_P$ by the factorization property. The sewing topology on the space of pants decompositions is captured by the flip graph, whose vertices are pants decompositions and whose edges are elementary moves (Dehn twists and handle slides). The partition function is invariant under flips by the pentagon and hexagon identities of the chiral algebra.
\end{remark}



thinking
**Evaluating repository status**

I'm considering whether the current repository, ProvedHere, should stay that way while duplicates are labeled ProvedElsewhere. The same label across volumes creates conflicts, as AGENTS require stable epistemic status. There's a concern about editing volume two due to safety, but the current task emphasizes the current repo. The user wants all chapters included, so I'll need to investigate mismatches within the current repo. I should extract references from the concordance table for comparison purposes.
thinking
**Analyzing frontier list details**

I’m looking at item 1 from the frontier list that states, "Resolved in D^co... Chain-level proved for classes G, L, C." This leads me to question whether class C is indeed chain-level proved. The bv_brst remarks indicate that class C maintains the chain-level BV/bar identification at genus 1. Plus, there's the all-genera harmonic-decoupling hypothesis utilized in the theorem. I need to clarify these connections to ensure everything aligns correctly.
exec
/bin/zsh -lc "rg -n 'Chain-level proved|chain-level|conditional for class~\\\\mathsf\\{C\\}|resolved in D\\"'^'"\\{\\\\mathrm\\{co\\}\\}|higher-genus comparison|class~\\\\mathsf\\{C\\}|harmonic decoupling|open for class~\\\\mathsf\\{M\\}|resolved at the scalar level' chapters/connections/bv_brst.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:35:$\mathsf{L}$, and~$\mathsf{C}$ admit stronger chain-level statements
chapters/connections/bv_brst.tex:36:than class~$\mathsf{M}$. The higher-genus comparison is resolved in
chapters/connections/bv_brst.tex:39:coacyclic. The stronger chain-level statement is unconditional for
chapters/connections/bv_brst.tex:41:class~$\mathsf{C}$ on harmonic decoupling, and open for
chapters/connections/bv_brst.tex:53:chain-level identification breaks: the cross-channel term in the
chapters/connections/bv_brst.tex:55:harmonic decoupling is assumed, and class~$\mathsf{M}$ is precisely
chapters/connections/bv_brst.tex:92:The chain-level identifications (antifields versus
chapters/connections/bv_brst.tex:101:chain-level equalities.
chapters/connections/bv_brst.tex:1087:The chain-level mechanism underlying~(c) is:
chapters/connections/bv_brst.tex:1643:\item the chain-level quasi-isomorphism between the BV complex and
chapters/connections/bv_brst.tex:1647:\item the full quantum master equation as a chain-level identity
chapters/connections/bv_brst.tex:1653:characteristic of the bar complex); the chain-level identification
chapters/connections/bv_brst.tex:1657:\begin{proposition}[Three chain-level obstructions and harmonic factorization;
chapters/connections/bv_brst.tex:1659:\label{prop:chain-level-three-obstructions}
chapters/connections/bv_brst.tex:1660:\index{BV algebra!chain-level obstructions|textbf}
chapters/connections/bv_brst.tex:1661:\index{chain-level BV/bar identification}
chapters/connections/bv_brst.tex:1662:The chain-level identification
chapters/connections/bv_brst.tex:1680: the OPE, producing chain-level discrepancies.
chapters/connections/bv_brst.tex:1707: conditional on harmonic decoupling.
chapters/connections/bv_brst.tex:1716: the naive ordinary chain-level comparison fails, but the
codex
I found at least one concrete manual-status mismatch in `concordance.tex`: it currently says the higher-genus BV/bar chain-level statement is proved for class `C`, while `bv_brst.tex` only proves that lane under harmonic decoupling. I’m checking the other status summary blocks in `concordance.tex` for the same overstatement pattern before editing.
exec
/bin/zsh -lc "sed -n '3378,3388p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '700,735p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1968,1994p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7058,7076p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7896,7910p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11158,11172p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 (2)~\textbf{Genus-$0$ algebraic BRST/bar proved}
 (Theorem~\ref{thm:algebraic-string-dictionary});
 (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived});
 (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
 (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
 (5)~tree-level amplitude pairing \textbf{conditional} on
 Corollary~\ref{cor:string-amplitude-genus0} \\
\bottomrule
\end{tabular}
\end{center}
 succeeded in 50ms:
 (Theorem~\ref{thm:shadow-higgs-field}) has convergence
 radius $|c|/3$ in the degree variable;
 the MC4 completion radius is controlled by the same parameter
 $\lambda_{\mathrm{eff}} = -6/c$
 (Chapter~\ref{chap:arithmetic-shadows},
 Remark~\ref{rem:effective-coupling}).
\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
 Inductive genus
 determination, 2D convergence (no UV renormalization needed),
 analytic-algebraic comparison, and the general HS-sewing criterion
 (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
 plus subexponential sector growth implies convergence at all genera).
 Heisenberg sewing proved (Theorem~\ref{thm:heisenberg-sewing}:
 one-particle Bergman reduction, Fredholm determinant). At genus~$0$
 the algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}.
 BV=bar in the coderived category is proved for all four shadow
 classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 succeeded in 50ms:
\item \emph{Koszul duality.}
 The CG framework includes Koszul duality for factorization algebras
 (CG, Vol.~2, Chapter~5), specialized to holomorphic factorization
 algebras on curves. Their Koszul duality, restricted to this setting,
 recovers our chiral Koszul duality. Our contribution is the explicit
 identification of the Koszul dual for all standard families
 (Kac--Moody, Virasoro, $\mathcal{W}_N$, etc.) via the bar-cobar
 adjunction on Fulton--MacPherson spaces.
\item \emph{Quantum corrections.}
 The CG perturbative quantization framework produces $A_\infty$
 structures from Feynman diagram expansions (CG, Vol.~2, Chapter~3).
 Our curved $A_\infty$ structure on the bar complex is the
 chiral-algebraic counterpart: the curvature $m_0 = \kappa \cdot
 \mathbf{1}$ arises from the highest-order OPE pole (quartic for
 Virasoro, double for Heisenberg), not from a Feynman diagram sum.
 The genus universality theorem shows that these two perspectives
 produce the same genus-$g$ obstruction class.
\item \emph{BV-BRST.}
 The CG BV formalism motivates the BRST/bar comparison package in
 Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
 succeeded in 50ms:
 (b)~the independent open-sector derivation of genus-$g$
 amplitudes from iterated clutching on
 $\mathcal{C}_{\mathrm{op}}$ without using the bar-intrinsic
 construction.
\item \emph{Honest scope.}
 The dg-shifted Yangian is proved for the affine lineage
 (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}).
 The general perturbative 3d~HT Yangian structure is conjectural.
 The BV/BRST~$=$~bar identification at higher genus is resolved
 in the coderived category $D^{\mathrm{co}}$ for all shadow classes
 (Theorem~\ref{thm:bv-bar-coderived});
 the chain-level identification fails for class~M.
 The Heisenberg scalar level is proved at the chain level
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
\end{enumerate}

% ======================================================================
\section{Conjecture promotions and the true frontier}
\label{sec:concordance-conjecture-promotions}
 succeeded in 52ms:
 (Open Problem~\ref{op:multi-generator-universality}, resolved
 negatively).
\item \emph{BV/BRST $=$ bar at higher genus.}
 For the Heisenberg, the scalar-level identification
 $F_g^{\mathrm{BV}} = F_g^{\mathrm{bar}} = \kappa\cdot\lambda_g^{\mathrm{FP}}$
 is proved at all genera
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 The general chain-level identification at genus $g \geq 1$
 is conjectural
 (Conjecture~\ref{conj:v1-master-bv-brst}). Tests~1--4 control
 the bar side; the BV/BRST comparison is an independent
 assertion about the physics.
\item \emph{Non-perturbative completion.}
 The four tests are perturbative in genus. The
 algebraic shadow obstruction tower $\sum_g F_g \hbar^{2g}$ converges
 succeeded in 52ms:
 The BV path integral on $\Sigma_g$ produces
 $\Theta^{\mathrm{BV}}_T
 \in \MC(\mathfrak{g}^{\mathrm{BV}}_T)$.
 At genus~$0$, the PVA descent theorems identify the two
 convolution algebras and their MC elements.
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
 \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
 sending $\Theta^{\mathrm{oc}}_\cA$ to
 $\Theta^{\mathrm{BV}}_T$ remains open for class~M.

exec
/bin/zsh -lc "sed -n '1919,1995p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{thm:bv-bar-coderived}%
\index{BV algebra!bar complex identification!coderived category|textbf}%
\index{coderived category!BV/bar identification|textbf}%
Let~$\cA$ be a chirally Koszul algebra. The genus-$0$ BV/bar
comparison is the chain-level quasi-isomorphism of
Theorem~\ref{thm:bv-bar-geometric}. For each genus
$g \geq 1$, let
\[
 f_g \colon
 C^{\bullet}_{\mathrm{BV}}(\cA, \Sigma_g)
 \longrightarrow
 B^{(g)}(\cA)
\]
be the comparison morphism of filtered curved
factorization models
obtained by replacing the BV propagator with its Hodge
decomposition relative to the bar propagator. Then:
\begin{enumerate}[label=\textup{(\roman*)}]
\item for every genus $g \geq 0$,
\[
exec
/bin/zsh -lc "rg -n -C 2 'conj:v1-master-bv-brst|thm:bv-bar-coderived|harmonic decoupling|class~M|class~\\\\mathsf\\{M\\}|class~\\\\mathsf\\{C\\}|coderived category \\"'$D'"\\"'^'"\\{\\\\mathrm\\{co\\}\\}' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
269-class~L (single Massey product, $r_{\max} = 3$),
270-class~C (quartic then rigid by stratum separation, $r_{\max} = 4$),
271:class~M (intrinsically non-formal, $r_{\max} = \infty$).
272-
273-\section{Principal contributions}\label{sec:principal-contributions}
--
373- and the moonshine module~$V^\natural$
374- \textup{(}Chapter~\ref{chap:moonshine}:
375: $\kappa = 12$, class~M, Niemeier discrimination
376- at $c = 24$\textup{)}.
377- Genus-$g$ free energies through $g = 10$ with
--
718- The CG BV formalism motivates the BRST/bar comparison package in
719- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
720: in the coderived category $D^{\mathrm{co}}$ for all shadow classes
721: (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
722- Heisenberg scalar identification is proved at all genera
723- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
724- G, L, C are proved. The chain-level identification fails for
725: class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
exec
/bin/zsh -lc "sed -n '11272,11285p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10223,10270p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11154,11174p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}; the
 genuswise chain-level BV/BRST/bar identification remains
 conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
 class~M chain-level false).
MC3 splits into three layers
(Corollary~\ref{cor:mc3-all-types} and
 succeeded in 50ms:
\item \textbf{BV/BRST $=$ bar at higher genus}
 (Conjecture~\ref{conj:v1-master-bv-brst}).

 \smallskip\noindent
 \emph{Resolution in $D^{\mathrm{co}}$.}
 \textbf{Resolved} in the coderived category
 (Theorem~\ref{thm:bv-bar-coderived}):
 for every chirally Koszul algebra~$\cA$, the BV complex and the
 bar complex are quasi-isomorphic in $D^{\mathrm{co}}(\cA)$ at
 all genera. The key mechanism for class~M: the degree-$r$
 chain-level obstruction satisfies
 $\delta_r \propto m_0^{\lfloor r/2 \rfloor - 1}$, and in
 $D^{\mathrm{co}}$ the curvature acts as
 $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$, so every
 $\delta_r$ is coderived-exact.

 \smallskip\noindent
 \emph{Chain-level status.}
 For the Heisenberg algebra $\cH_\kappa$, the scalar-level
 identification
exec
/bin/zsh -lc "sed -n '9828,9836p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item \emph{BV/BRST $=$ bar at higher genus}
 \textup{(}Conjecture~\ref{conj:v1-master-bv-brst},
 \textbf{resolved in $D^{\mathrm{co}}$} by
 Theorem~\ref{thm:bv-bar-coderived}\textup{)}.
 The BV path integral on $\Sigma_g$ produces
 $\Theta^{\mathrm{BV}}_T
 \in \MC(\mathfrak{g}^{\mathrm{BV}}_T)$.
 At genus~$0$, the PVA descent theorems identify the two
 convolution algebras and their MC elements.
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
 \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
 sending $\Theta^{\mathrm{oc}}_\cA$ to
 $\Theta^{\mathrm{BV}}_T$ remains open for class~M.

\item \emph{Pixton ideal generation}
 succeeded in 51ms:
& Holographic dictionary:
 bulk reconstruction from the derived center \\
& BV/BRST $=$ bar at higher genus:
 resolved in $D^{\mathrm{co}}$ for all shadow classes
 \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
 chain-level false for class~M;
 Heisenberg scalar level proved at chain level
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
& Shadow--chromatic correspondence
exec
/bin/zsh -lc "rg -n 'algebraic-string-dictionary|master-theta|general-hs-sewing' chapters/connections/bv_brst.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/connections/concordance.tex:1978: (Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
chapters/connections/concordance.tex:1983: (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
chapters/connections/concordance.tex:3377: (Theorem~\ref{thm:general-hs-sewing});
chapters/connections/concordance.tex:3379: (Theorem~\ref{thm:algebraic-string-dictionary});
chapters/connections/concordance.tex:4483:(Theorem~\ref{thm:general-hs-sewing}).
chapters/connections/concordance.tex:5515:(Theorem~\ref{thm:master-theta}).
chapters/connections/concordance.tex:7091:criterion (Theorem~\ref{thm:general-hs-sewing}) together
chapters/connections/concordance.tex:7857:(Theorem~\ref{thm:general-hs-sewing}) proves convergence for
chapters/connections/concordance.tex:9768: \textup{(}Theorem~\ref{thm:general-hs-sewing}\textup{)} \\
chapters/connections/concordance.tex:11273: at all genera (Theorem~\ref{thm:general-hs-sewing}); the
chapters/connections/concordance.tex:11275: (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
exec
/bin/zsh -lc "rg -n '\\\\label\\{thm:algebraic-string-dictionary\\}|\\\\begin\\{theorem\\}\\[.*algebraic.*string.*dictionary|\\\\begin\\{theorem\\}\\[.*BRST.*bar.*' chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/bv_brst.tex:489:\begin{theorem}[Genus-\texorpdfstring{$0$}{0} BRST-bar quasi-isomorphism;

thinking
**Exploring alias labels**

I'm thinking about searching for an alias label from another file globally. It seems like a good idea to broaden the search so I can find the information more efficiently. I want to ensure that I don’t miss anything important by limiting the scope. I wonder what specific results I might uncover through this broader search. Let's see how this goes!
exec
/bin/zsh -lc "rg -n 'thm:algebraic-string-dictionary' ." in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
Total output lines: 210

./metadata/dependency_graph.dot:1218:  thm_algebraic_string_dictionary [label="thm:algebraic-string-dictionary\ntheorem [Pr]\nAlgebraic bar/BRST genus dictionary", style=filled, fillcolor="#c8e6c9"];
./metadata/theorem_registry.md:1515:| `thm:algebraic-string-dictionary` | `theorem` | 4771 | Algebraic bar/BRST genus dictionary |
./metadata/label_index.json:47026:  "thm:algebraic-string-dictionary": {
./metadata/claims.jsonl:286:{"label": "conj:v1-master-bv-brst", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 434, "title": "BV/BRST/bar identification", "refs_in_block": ["thm:bv-bar-coderived", "thm:master-pbw", "thm:master-theta", "conj:master-dk-kl", "conj:v1-master-infinite-generator", "thm:algebraic-string-dictionary", "cor:string-amplitude-genus0"]}
./metadata/claims.jsonl:287:{"label": "conj:standard-tower-mc5-reduction", "env_type": "conjecture", "status": "Conjectured", "file": "chapters/connections/editorial_constitution.tex", "line": 567, "title": "Standard-tower MC5 reduction after MC3 and realized\nMC4", "refs_in_block": ["conj:master-dk-kl", "prop:winfty-mc4-frontier-package", "def:winfty-stage4-ward-normalized", "prop:yangian-typea-realization-criterion", "thm:yangian-typea-realization-plus-compacts", "thm:yangian-typea-realization-plus-fundamental-packet", "thm:algebraic-string-dictionary", "thm:master-theta"]}
./metadata/claims.jsonl:288:{"label": "cor:standard-tower-mc5-closure", "env_type": "corollary", "status": "Conditional", "file": "chapters/connections/editorial_constitution.tex", "line": 658, "title": "Standard-tower MC5 closure on the canonical Yangian\nlocus", "refs_in_block": ["conj:master-dk-kl", "def:winfty-stage4-ward-normalized", "thm:yangian-formal-moduli-plus-core-realization", "thm:yangian-canonical-realization-plus-vector-line", "thm:algebraic-string-dictionary", "thm:master-theta"]}
./metadata/claims.jsonl:1180:{"label": "thm:algebraic-string-dictionary", "env_type": "theorem", "status": "ProvedHere", "file": "chapters/examples/free_fields.tex", "line": 4771, "title": "Algebraic bar/BRST genus dictionary", "refs_in_block": ["thm:bar-semi-infinite-km", "thm:brst-bar-genus0", "cor:anomaly-duality-km", "rem:w3-kappa-sums", "thm:genus-universality", "thm:genus-induction-strict"]}
./rectification_20260412_233715/R13_introduction.md:262:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
./rectification_20260412_233715/R13_introduction.md:335:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
./wave2_audit_20260413_001942/C18_bv_brst.md:970:   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:3:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
./wave2_audit_20260413_001942/C18_bv_brst.md:973:   ./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1669:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:3:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:135:CLAUDE.md:492:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:154:metadata/theorem_registry.md:1482:| `thm:algebraic-string-dictionary` | `theorem` | 4746 | Algebraic bar/BRST genus dictionary |
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:243:  1482	| `thm:algebraic-string-dictionary` | `theorem` | 4746 | Algebraic bar/BRST genus dictionary |
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:335:  1952	 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
./wave2_audit_20260413_001942/S11_bv_brst_to_body.md:1669:- [HIGH] chapters/theory/higher_genus_modular_koszul.tex:24845 — PROBLEM: the main-theorem seam collapses MC5 into an undifferentiated “outside” conjectural region. Lines 24845-24846 say the four tests “exhaust the proved output,” and lines 24882-24885 list higher-genus `BV/BRST = bar` as simply outside, but `bv_brst.tex:30-40` and `1881-1969` explicitly split that surface into: proved genus-0 algebraic BRST/bar, proved Heisenberg scalar all-genus equality, and only a conditional coderived higher-genus lift, with class `\mathsf{M}` the obstruction locus. FIX: change line 24845 to `Four independent bar-side tests exhaust the proved output internal to the modular Koszul machine.` Replace lines 24878-24885 with: `Three regions lie outside these four bar-side tests: multi-weight universality at $g \geq 2$ (Open Problem~\ref{op:multi-generator-universality}, resolved negatively); the \emph{chain-level} higher-genus identity $\mathrm{BV}/\mathrm{BRST}=\mathrm{bar}$ (Conjecture~\ref{conj:master-bv-brst}); Chapter~\ref{ch:bv-brst} proves the genus-$0$ algebraic BRST/bar comparison (Theorem~\ref{thm:algebraic-string-dictionary}), proves the Heisenberg scalar equality at all genera (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and records the coderived lift only conditionally (Theorem~\ref{thm:bv-bar-coderived}); class~$\mathsf{M}$ is the chain-level obstruction locus; and non-perturbative completion.`
./wave2_audit_20260413_001942/U09_missing_examples.md:5:- [CRITICAL] chapters/frame/guide_to_main_results.tex:99 — PROBLEM: the flagship guide repeats the same false MC5 status, says `$D^{\mathrm{co}}$-level BV=bar proved`, and mentions “Heisenberg sewing via Fredholm determinant” without citing `thm:heisenberg-sewing` at all. FIX: change clause (3) to “$D^{\mathrm{co}}$-level BV=bar conditional,” add the proved Heisenberg scalar theorem `thm:heisenberg-bv-bar-all-genera`, and expand the location cell to include `\ref{thm:heisenberg-sewing}` alongside `\ref{thm:general-hs-sewing}` and `\ref{thm:algebraic-string-dictionary}`.


thinking
**Evaluating theorem status**

I'm seeing that the audit files highlight a critical issue with thm:bv-bar-coderived possibly being conditional. However, in the actual bv_brst.tex document, it shows ClaimStatusProvedHere, not conditional. The audit suggests a stale condition from a previous source, but the user mentioned that the audit findings are pertinent. It seems the current state supports the theorem being proved. I should verify the theorem’s statement and check `editorial_constitution.tex`, especially concerning the class conditions mentioned. Maybe there's also something to clarify about the MC5 note.
thinking
**Searching editorial constitution**

I’m thinking I need to check the current `editorial_constitution` for any similar overstatements, though I wonder if that’s necessary since the task mentions all chapters and connections. It might be helpful to look for MC5 status phrases there too. It'll help ensure everything aligns correctly with the user's request. Let's dig into that document and see if there's anything noteworthy that might pertain to the task at hand.
exec
/bin/zsh -lc "rg -n -C 2 'MC5|bv-bar-coderived|resolved in \\"'$D'"\\"'^'"\\{\\\\mathrm\\{co\\}\\}|class~C|harmonic decoupling|chain-level false|chain-level conjectural|class~M' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
147-MC4 & Infinite-generator convergence
148- & \textbf{Proved} (strong completion towers) \\
149:MC5 & BV/BRST $=$ bar
150- & \textbf{Partially proved} (HS-sewing; genus-$0$ algebraic) \\
151-\bottomrule
--
177-The remaining example-specific tasks are coefficient stabilization and
178-H-level target identification.
179:MC5 is not fully proved. What is proved at all genera is the analytic
180-HS-sewing package
181-\textup{(}Theorem~\ref{thm:general-hs-sewing}: polynomial OPE growth
--
439-
440-\emph{Resolved in $D^{\mathrm{co}}$}
441:\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
442-the BV and bar complexes are quasi-isomorphic in the coderived category
443:for all chirally Koszul algebras, including class~M.
444-The chain-level identification holds for classes~G, L, C but
445:\emph{fails} for class~M
446-\textup{(}quartic harmonic obstruction\textup{)}.

thinking
**Auditing editorial connections**

I’m noticing that there's a mismatch in the editorial at line 444, where it mentions that chain-level holds for classes G, L, and C. I think it might need to change to just G and L, while putting class C under harmonic decoupling. Since the task involves all chapters and connections, I should audit other connection files for any similar stale phrases. I’ll search the current connection files for "classes G, L, C" and "class M false" using rg.
exec
/bin/zsh -lc "rg -n 'classes~G, L, C|classes G, L, C|class~C under harmonic decoupling|class~M chain-level false|chain-level holds for classes~G, L, C|chain-level identification fails for class~M|resolved in \\"'$D'"\\"'^'"\\{\\\\mathrm\\{co\\}\\}' chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/editorial_constitution.tex:444:The chain-level identification holds for classes~G, L, C but
chapters/connections/concordance.tex:3383: (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
chapters/connections/concordance.tex:7069: the chain-level identification fails for class~M.
chapters/connections/concordance.tex:7745: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9831: resolved in $D^{\mathrm{co}}$ for all shadow classes
chapters/connections/concordance.tex:11156: \textbf{resolved in $D^{\mathrm{co}}$} by
chapters/connections/concordance.tex:11283: class~M chain-level false).

thinking
**Searching for resolutions**

I need to search for "resolved in D^co," which might not be a mismatch after all. I'm looking specifically around line 11156, where perhaps only class M remains open. I should also check for phrases like "obstruction iii resolved for classes G, L, and C." It might be helpful to explore broader patterns as well! This way, I can gather more context and information.
exec
/bin/zsh -lc "rg -n 'class~C|class~\\\\mathsf\\{C\\}|harmonic decoupling|chain-level proved for classes|holds for classes~G, L, C|remains open for class~M|fails for class~M|class~M chain-level false' chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/editorial_constitution.tex:444:The chain-level identification holds for classes~G, L, C but
chapters/connections/concordance.tex:222:class~C escapes via stratum separation),
chapters/connections/concordance.tex:270:class~C (quartic then rigid by stratum separation, $r_{\max} = 4$),
chapters/connections/concordance.tex:2135: on the one-dimensional metric, $\beta\gamma$ (class~C) has $S_5 = 1/2 \neq 0$,
chapters/connections/concordance.tex:3134:(i)~the symplectic fermion IS Koszul (class~C, PBW universality;
chapters/connections/concordance.tex:3383: (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
chapters/connections/concordance.tex:7069: the chain-level identification fails for class~M.
chapters/connections/concordance.tex:11171: $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
chapters/connections/concordance.tex:11283: class~M chain-level false).

thinking
**Exploring status mismatches**

I’m considering that there could be more manual status mismatches that aren’t confined to just class C. It seems like I might need to search through audit files that reference concordance. There might be generated reports that pinpoint exact lines where issues occur. I’ll have to dig into the audit notes to find out more about the concordance status mismatches. This should help clarify any discrepancies!
exec
/bin/zsh -lc "rg -n 'concordance\\.tex:.*MC5|concordance\\.tex:.*class~M|concordance\\.tex:.*class~C|Chain-level proved for classes G, L, C|holds for classes~G, L, C|mc5 status|BV/BRST' wave2_audit_20260413_001942 platonic_rectification_20260413_114523 relaunch_20260413_111534 2>/dev/null" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 313

relaunch_20260413_111534/R13_introduction.md:245:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved. The analytic HS-sewing package is proved at all genera (Theorem~\ref{thm:general-hs-sewing}); the genus-$0$ algebraic BRST/bar comparison is proved (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar in the coderived category is proved for all four shadow classes including class~M (Theorem~\ref{thm:bv-bar-coderived}). The genuswise chain-level BV/BRST/bar identification remains conjectural (class~M chain-level false), and the tree-level amplitude pairing is conditional on Corollary~\ref{cor:string-amplitude-genus0}. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
relaunch_20260413_111534/R13_introduction.md:255:MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}
relaunch_20260413_111534/R19_coderived_models.md:99:508:| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
relaunch_20260413_111534/R19_coderived_models.md:769:chapters/connections/concordance.tex:1943:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
relaunch_20260413_111534/R19_coderived_models.md:771:chapters/connections/concordance.tex:1956: classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:576:\item \emph{BV/BRST $=$ bar at higher genus}
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md:611:\item \textbf{BV/BRST $=$ bar at higher genus}
platonic_rectification_20260413_114523/P10_MC5_coderived_upgrade.md: WARNING: stopped searching binary file after match (found "\0" byte around offset 775350)
wave2_audit_20260413_001942/C13_virasoro.md:483:   114	     "BV/BRST→Main theorems. Check: (a) MC5 status consistent between files, (b) chain-level vs coderived distinction maintained, (c) class-M caveats propagated"),
relaunch_20260413_111534/S14_standalone_to_main.md:2246:chapters/connections/concordance.tex:7634: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
relaunch_20260413_111534/S14_standalone_to_main.md:2369:standalone/introduction_full_survey.tex:4851:MC5 & Genus tower (analytic sewing) & \textbf{analytic part proved} & HS-sewing (Thm~\ref{thm:general-hs-sewing}); genuswise BV/BRST/bar identification conjectural; genus-$0$ algebraic BRST/bar proved (Thm~\ref{thm:algebraic-string-dictionary}), tree-level amplitude pairing conditional on Cor.~\ref{cor:string-amplitude-genus0}
relaunch_20260413_111534/S14_standalone_to_main.md:2556:standalone/survey_modular_koszul_duality.tex:7780:Master conjectures MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera and the genuswise BV/BRST/bar identification conjectural. MC3 holds for all simple types on the evaluation-generated core via multiplicity-free $\ell$-weights (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual problem DK-4/5 (extension beyond evaluation modules) is downstream.
relaunch_20260413_111534/S14_standalone_to_main.md:2566:standalone/introduction_full_survey.tex:4841:The five Master Conjectures MC1--MC5 organize the structural results. MC1 through MC4 are proved; MC5 is partially proved, with the analytic HS-sewing package established at all genera while the genuswise BV/BRST/bar identification remains conjectural. MC3 holds for all simple types on the evaluation-generated core (Theorem~\ref{thm:categorical-cg-all-types}, Corollary~\ref{cor:mc3-all-types}). The residual DK-4/5 problem (extension beyond evaluation modules) is downstream of MC3. Proof status and refinements are in Chapter~\ref{chap:concordance}.
relaunch_20260413_111534/XV08_thm_status_xvol.md:246:/Users/raeez/chiral-bar-cobar/README.md:26:All five master conjectures MC1-MC5 are proved: MC1 (PBW), MC2 (MC element), MC3 (thick generation, all simple types; type A unconditional, other types conditional on Lemma L for the rank-independence step), MC4 (completion towers), MC5 (analytic HS-sewing at all genera). The full genuswise BV/BRST/bar identification at genus g >= 1 remains conjectural; genus 0 algebraic BRST/bar comparison is proved.
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:206:chapters/connections/concordance.tex:6938: The BV/BRST~$=$~bar identification at higher genus is resolved
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:207:chapters/connections/concordance.tex:7610:\item \textup{Conjecture~\ref{conj:master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:208:chapters/connections/concordance.tex:7763:\item \emph{BV/BRST $=$ bar at higher genus.}
wave2_audit_20260413_001942/C07_higher_genus_foundations.md:209:chapters/connections/concordance.tex:9688:& BV/BRST $=$ bar at higher genus:
exec
/bin/zsh -lc "sed -n '500,545p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\text{evaluation-generated core}
&\Longrightarrow \text{MC3 enlargement}\\
&\Longrightarrow \text{MC4 H-level comparison}\\
&\Longrightarrow \text{MC5 physics completion}.
\end{aligned}
\]
\emph{Current status of this chain.}
MC4 now splits into MC4$^+$ (positive towers, solved by
stabilization, Theorem~\ref{thm:stabilized-completion-positive})
and MC4$^0$ (resonant towers, reduced to a finite resonance problem
by Theorem~\ref{thm:resonance-filtered-bar-cobar}); see
Remark~\ref{rem:mc4-reduction-chain}.
MC3 is \textbf{proved for all simple types} on the evaluation-generated
core: the all-types categorical
prefundamental Clebsch--Gordan closure and evaluation-generated-core
DK comparison are proved
\textup{(}Theorem~\ref{thm:categorical-cg-all-types},
Corollary~\ref{cor:dk23-all-types}\textup{)}, and type~$A$ adds the
shifted-prefundamental and pro-Weyl packets. The residual DK-4/5
problem (compact/completed extension beyond evaluation modules,

thinking
**Fixing MC5 status issues**

I realize that my current understanding seems too rigid. It likely refers to the analytic lane rather than the full MC5. The task emphasizes needing to address especially the bv_brst MC5 status and check the concordance of all statuses. There's also a connection to the editorial_constitution that needs addressing. I'll need to fix all mismatches in MC5 status across connections and search other files with phrases like "MC5 is proved" using rg across connections.
exec
/bin/zsh -lc "rg -n 'MC5 .*proved|MC5.*resolved|MC5.*conjectural|MC5.*conditional|BV/BRST.*resolved|BV=bar.*proved|chain-level.*class~M|class~M.*fails|class~C.*harmonic decoupling|analytic and coderived proved' chapters/connections/*.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:2543:$bc$ ghosts gives the MC5 genus-$0$ case proved in
chapters/connections/editorial_constitution.tex:179:MC5 is not fully proved. What is proved at all genera is the analytic
chapters/connections/editorial_constitution.tex:461:The analytic convergence component of MC5 is fully resolved:
chapters/connections/editorial_constitution.tex:819:MC5 & \textbf{Analytic part proved}
chapters/connections/thqg_entanglement_programme.tex:457:the analytic HS-sewing construction (MC5 analytic lane, proved) at genus $ng$,
chapters/connections/outlook.tex:188:proved and MC5 partially proved (analytic HS-sewing at all genera;
chapters/connections/outlook.tex:259:MC1 through MC4 are proved. MC5 is partially proved: the analytic
chapters/connections/outlook.tex:263:chain-level BV/BRST/bar identification remains conjectural (class~M
chapters/connections/concordance.tex:1974:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
chapters/connections/concordance.tex:1986: BV=bar in the coderived category is proved for all four shadow
chapters/connections/concordance.tex:3380: (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
chapters/connections/concordance.tex:7066: The BV/BRST~$=$~bar identification at higher genus is resolved
chapters/connections/concordance.tex:7069: the chain-level identification fails for class~M.
chapters/connections/concordance.tex:7745: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
chapters/connections/concordance.tex:9833: chain-level false for class~M;
chapters/connections/concordance.tex:10261: For class~M, the chain-level identification \emph{fails}:
chapters/connections/concordance.tex:10298: is whether a chain-level quasi-isomorphism exists for class~M,
chapters/connections/concordance.tex:11270: MC1 through MC4 are proved. MC5 is resolved

thinking
**Inspecting outlook and entanglement programs**

I think I need to inspect the outlook and the entanglement_programme based on what the user mentioned about all chapters and connections. It seems like there could be some mismatches there. I should verify if the statuses are accurate, so I’ll take a look at the outlook lines and the entanglement_programme to ensure everything aligns properly. Let's see what I can find!
codex
I found the broader pattern: the live drift isn’t label tags so much as stale MC5 status prose repeated across connection chapters. I’m checking the other connection chapters that summarize MC5 (`editorial_constitution`, `outlook`, `concordance`, and any programmatic bridge text) so the fix stays consistent.
exec
/bin/zsh -lc "sed -n '170,270p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '440,470p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11264,11286p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '432,448p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\label{rem:no-bifunctor}
\index{bifunctoriality!failure of two-sided}
\index{one-slot obstruction}
Robert-Nicoud--Wierstra~\cite[Section~6]{RNW19} prove that although
the convolution functor $\operatorname{hom}_\alpha(-,-)$ extends to
$\infty_\alpha$-morphisms in either slot separately, there is
\emph{no} honest bifunctor accepting $\infty$-morphisms in both slots
simultaneously. The MC3 categorical lift must proceed one slot at a
time.
\end{remark}

% ======================================================================

\section{Three concentric rings}
\label{sec:three-rings}
\index{three concentric rings|textbf}

\noindent\textbf{Ring~1} (proved core): Theorems~A--H, MC1--MC4
proved and MC5 partially proved (analytic HS-sewing at all genera;
genus-$0$ algebraic BRST/bar; $D^{\mathrm{co}}$-level BV=bar for all
 succeeded in 52ms:
\begin{equation}\label{eq:thqg-renyi}
S_n^{(g)}(\cA)
\;:=\;
\frac{1}{1-n}
\log\frac{Z_n^{(g)}(\cA)}{Z^{(g)}(\cA)^n}.
\end{equation}
The von~Neumann entropy is recovered in the $n \to 1$ limit:
$S^{(g)}(\cA) = \lim_{n \to 1} S_n^{(g)}(\cA)$.
\end{conjecture}

\begin{remark}[Evidence]
Standard replica argument \cite{Calabrese-Cardy04, Lewkowycz-Maldacena13}
adapted to the algebraic framework. The
heuristic status reflects two issues: (1)~the analytic continuation
$n \to 1$ requires the Carlson theorem, which demands growth bounds
on $Z_n^{(g)}$ in $n$ that have not been established algebraically;
(2)~the evaluation on the replica manifold of genus $ng$ requires
the analytic HS-sewing construction (MC5 analytic lane, proved) at genus $ng$,
which is computationally nontrivial for large~$n$.
\end{remark}
 succeeded in 50ms:
 \emph{Violated anti-pattern}:
 (same name, different object: the chart is not
 the category).

\item \textbf{``All master conjectures resolved.''}
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}; the
 genuswise chain-level BV/BRST/bar identification remains
 conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
 class~M chain-level false).
 succeeded in 52ms:

\begin{conjecture}[BV/BRST/bar identification]
\label{conj:v1-master-bv-brst}
\ClaimStatusConjectured{}
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.

\emph{Resolved in $D^{\mathrm{co}}$}
\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
the BV and bar complexes are quasi-isomorphic in the coderived category
for all chirally Koszul algebras, including class~M.
The chain-level identification holds for classes~G, L, C but
\emph{fails} for class~M
\textup{(}quartic harmonic obstruction\textup{)}.

\emph{This is the mathematical-physics bridge. It is



thinking
**Clarifying class distinctions**

I think the Outlook text looks mostly fine but might need to mention class C conditional/open. It discusses "chain-level BV/BRST/bar conjectural" without clearly stating class distinctions. If it mentions coderived proved, that's okay, but it might be unnecessary to bring up class C. However, saying "class M false" might imply class C isn't conjectural, which could be misleading. I'll need to search for explicit mentions of "G, L, C" to ensure accuracy in context. The user is interested in fixing mismatches, focusing on clear false statements.
thinking
**Identifying mismatches in classifications**

I think we shouldn't rewrite everything, just enough to address the key issues. The phrase "remains open for class M" might imply that class C isn’t open, which is a mismatch. In line 11171, it states that chain-level identification remains open for class M, but that’s misleading since class C is also included. Line 7069 muddles things further by suggesting failures in class M without clarifying C. I’ve noted that lines 724 and 7745 incorrectly state classes G, L, and C are proved, which is definitely false.
thinking
**Searching for unconditional class C phrases**

I should search for exact phrases regarding unconditional class C. Using regex for terms like `G, L, C` might help narrow it down. Phrases like "Obstruction (iii) is resolved for classes" or "remains open for class M" are important to check too. I think it’s a good idea to fix explicit statements about unconditional class C and perhaps include a caveat about class C in general summaries to prevent any misreading. I need to identify all summary blocks that may need adjustments.
exec
/bin/zsh -lc "rg -n 'Conjecture~\\\\ref\\{conj:v1-master-bv-brst\\}.*scalar|resolves Conjecture~\\\\ref\\{conj:v1-master-bv-brst\\}|establishes Conjecture~\\\\ref\\{conj:v1-master-bv-brst\\}' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1407:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
1629:Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
1850:Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
exec
/bin/zsh -lc "rg -n 'MC5 .*proved|MC5 .*resolved|Conjecture~\\\\ref\\{conj:v1-master-bv-brst\\}|chain-level identification holds for classes|class~M|harmonic decoupling' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
50:(Conjecture~\ref{conj:v1-master-bv-brst}).
179:MC5 is not fully proved. What is proved at all genera is the analytic
443:for all chirally Koszul algebras, including class~M.
444:The chain-level identification holds for classes~G, L, C but
445:\emph{fails} for class~M
461:The analytic convergence component of MC5 is fully resolved:
468:Conjecture~\ref{conj:v1-master-bv-brst} is the \emph{identification}
544:Conjecture~\ref{conj:v1-master-bv-brst} is the
560:Conjecture~\ref{conj:v1-master-bv-brst} $\to$ Future~9.
819:MC5 & \textbf{Analytic part proved}
1310:\textup{(}Conjecture~\ref{conj:v1-master-bv-brst}\textup{)},
1350: Conjecture~\ref{conj:v1-master-bv-brst}.
1599: (Conjecture~\ref{conj:v1-master-bv-brst}),
1718:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
1856:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
1996:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)
2056:(Contributing to Conjecture~\ref{conj:v1-master-bv-brst}.)

thinking
**Considering code patching**

I think I need to patch just line 444 and 529 for the updates. I could search for the phrase "MC5 at," which might help me locate it quickly. It looks like line 529 is already relevant to what I’m trying to find. I should focus on searching for the exact phrases "MC5 at" or "genus" to ensure I get the correct context for my changes. This approach seems like the right way to proceed!
exec
/bin/zsh -lc "rg -n 'MC5 at|genus~\\"'$0'"\\"'$ and genus~'"\\"'$1'"\\"'$|genus '"\\"'$g >= 2'"\\"'$ is proved'"' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
529:(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
530:genus~$0$ and genus~$1$ is proved

thinking
**Reviewing analytic components**

I’m considering whether I should take a closer look around line 459 to verify if any adjustments are needed. Line 461 indicates that the analytic convergence component is fully resolved, which seems promising. I might want to also mention concepts like genus0 algebraic and Heisenberg scalar as part of this discussion. So, my next step is to inspect lines 459 to 470 to see what's there.
exec
/bin/zsh -lc "sed -n '459,475p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{remark}[MC5 analytic resolution vs.\ BV/BRST identification]
\label{rem:mc5-vs-bv-brst}
The analytic convergence component of MC5 is fully resolved:
Theorem~\ref{thm:general-hs-sewing} (HS-sewing at all genera)
and Theorem~\ref{thm:heisenberg-sewing} (Heisenberg sewing via
Fredholm determinant) prove that sewing amplitudes converge for
the entire standard landscape (universal algebras; for simple
quotients at admissible levels, see
Remark~\ref{rem:thqg-I-admissible}). What remains conjectural in
Conjecture~\ref{conj:v1-master-bv-brst} is the \emph{identification}
of the BV/BRST complex of the physical field theory with the
bar complex of the chiral algebra, a mathematical-physics bridge
that is logically downstream of the purely algebraic theorems and
requires input from perturbative QFT (Costello--Gwilliam
framework) beyond genus~$0$.
\end{remark}


thinking
**Searching for audit notes**

I’m thinking about searching for explicit phrases like "classes G, L, C are proved" and "remains open for class M." Checking the concordance might help me find those. I could also look into audit notes related to C17_concordance to ensure I'm covering all bases. I should focus on searching specific lines in the audit for relevant information. Let's proceed to open the necessary documents!
exec
/bin/zsh -lc "sed -n '1568,1595p' wave2_audit_20260413_001942/C17_concordance.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  6928	 (\textbf{op:multi-generator-universality}, resolved negatively;
  6929	 Theorem~\ref{thm:multi-weight-genus-expansion});
  6930	 (b)~the independent open-sector derivation of genus-$g$
  6931	 amplitudes from iterated clutching on
  6932	 $\mathcal{C}_{\mathrm{op}}$ without using the bar-intrinsic
  6933	 construction.
  6934	\item \emph{Honest scope.}
  6935	 The dg-shifted Yangian is proved for the affine lineage
  6936	 (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}).
  6937	 The general perturbative 3d~HT Yangian structure is conjectural.
  6938	 The BV/BRST~$=$~bar identification at higher genus is resolved
  6939	 in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  6940	 (Theorem~\ref{thm:bv-bar-coderived});
 succeeded in 53ms:
  9328	The Drinfeld--Sokolov reduction functor, applied to the
  9329	affine $\widehat{\fsl}_2$ dg-shifted Yangian data
  9330	$(m_2, r(z), \Delta)$ via homological perturbation,
  9331	should produce a well-defined Virasoro dg-shifted Yangian
  9332	at the chain level
  9333	(Vol~II, Theorem~\textup{thm:ds-hpl-transfer}).


thinking
**Harmonizing status updates**

I'm considering how to handle line 11270 regarding "MC5," which is resolved analytically but not at the chain level. It's broad enough, but perhaps we should mention G/L proved and C conditional. Given the user's request for consistency in statuses, it might be a good idea to consolidate the repeated MC5 summary lines into a single formula. That seems like a worthwhile update that could maintain clarity without overcomplicating things.
thinking
**Considering technical details**

I'm thinking about how to add nuance to my work, particularly around section 3380/1974, which discusses the Dco-level BV for all shadow classes, including class M. It might be good to mention the Heisenberg scalar theorem separately for clarity. It's worth noting that line 3378 already includes genus0 and tree-level conditional info without Heisenberg scalar. I need to check for references regarding "formality obstruction resolved at all genera" from the relaunch S16 as well. I'll search for "Formality obstruction."
exec
/bin/zsh -lc "rg -n 'Formality obstruction|resolved at all genera|MC5' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1974:\item \emph{MC5} (\textbf{analytic and coderived proved; chain-level conjectural}):
2012:Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
2943: & analytic bar coalgebra (MC5) \\[2pt]
3375:MC5 & Genus tower & Five components:
4526: & MC5 sewing programme,
4756:genus (MC5, Conjecture~\ref{conj:v1-master-bv-brst}).
6815: sewing (MC5). The integer-$n$ construction is well-defined from the
9731:& MC1, MC2, MC4, and the analytic/coderived lanes of MC5
11270: MC1 through MC4 are proved. MC5 is resolved




thinking
**Evaluating theorem registry**

I need to inspect the full 3375 rows; I've already checked some. It's essential to align with the theorem registry, which tracks only ProvedHere. There might be a cross-volume conflict with `thm:general-hs-sewing` between the current repository and vol2. The user asked for all chapters/connections in the current repo, and I found it. However, if I don't edit, I might miss a crucial finding related to claim status mismatches. I'll need to decide whether to update the current repo's genus_complete or not. In the current repo, `thm:general-hs-sewing` has a full proof, and in vol2, it's a duplicate labeled ProvedElsewhere. There is no mismatch within the current repo, but the same label across the volumes shows different statuses. Since AGENTS suggests updating duplicates in the same session or leaving a note about untouched areas, I need to be cautious with any edits.
thinking
**Analyzing theorem status**

I’m considering leaving a note in the final output, but the completeness contract requires me to address every finding. The explorer identified a genuine live drift surface outside two target files. Since the issue is in the current repo, I could potentially change the duplicate status to ProvedElsewhere. However, that would mean losing the original proof surface, which isn’t ideal. 

Maybe renaming the duplicate label in vol2 or noting it as pending is better. Since I can’t edit vol2 due to assignments, I need to think this through carefully. The same label should ideally not drift across primary sources and duplicates, but perhaps it’s not a “mismatch” that needs fixing. Although AGENTS flagged it, the user asked me to focus solely on the current repo. I might simply mention that it’s blocked or pending due to cross-volume issues without taking any further action in the current repo.
thinking
**Considering unresolved collisions**

I could note this as an unresolved external collision. The completeness contract states I need to mark findings as FIXED or BLOCKED. I should mention that the cross-volume `thm:general-hs-sewing` is blocked by action safety and user scope, but I'm unsure if it qualifies if not mentioned in audit findings. 

I might need to use a pre-edit verification protocol; however, I'm questioning if status/environment mismatches fall under any templates. Maybe I don’t need to create labels, but AGENTS says it's mandatory before editing any hot zone, so I should consider that carefully.
thinking
**Evaluating file patches**

I’m considering searching patterns again to ensure they are removed from modified files. I might need to patch cross-volume for `thm:general-hs-sewing`, but I wonder if I should ignore it based on the scope. The user might request “ALL chapters/connections,” but `genus_complete.tex` isn’t showing up in search results due to a mismatch. I could change its status to `ProvedElsewhere`, but that feels less truthful since it has full proof. Instead, I might leave it as is and note it as blocked. I need to carefully craft my patch.
codex
I’ve isolated the concrete fixes. The edits are limited to three files: `bv_brst.tex` to stop overstating scalar consequences as resolutions of the full chain-level conjecture, `editorial_constitution.tex` to correct the MC5 chain-status summary, and `concordance.tex` to align every repeated MC5 status block with the live `bv_brst` theorem surface.
file update
M /Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex
@@ -717,10 +717,11 @@
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
@@ -1988,4 +1989,5 @@
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
@@ -3381,4 +3383,5 @@
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
@@ -7068,3 +7071,4 @@
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
@@ -7744,3 +7748,3 @@
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
@@ -9832,3 +9836,4 @@
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
@@ -10257,5 +10262,5 @@
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
@@ -11170,3 +11175,5 @@
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
@@ -11281,3 +11288,4 @@
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
M /Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex
@@ -1405,4 +1405,4 @@
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
@@ -1627,6 +1627,7 @@
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
@@ -1848,5 +1849,6 @@
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
M /Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex
@@ -443,3 +443,4 @@
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
@@ -528,6 +529,9 @@
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
@@ -536,3 +540,5 @@
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
apply_patch(auto_approved=true) exited 0 in 35ms:
Success. Updated the following files:
M chapters/connections/bv_brst.tex
M chapters/connections/editorial_constitution.tex
M chapters/connections/concordance.tex
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

codex
The edits are in place. I’m re-reading each modified block now to catch any local coherence issues and then I’ll run the requested grep pass on the modified files.
exec
/bin/zsh -lc "sed -n '1400,1418p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '436,446p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1624,1634p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1844,1855p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

\section{Resolution for the Heisenberg algebra at all genera}
\label{sec:bv-bar-heisenberg-all-genera}
\index{Heisenberg!BV/bar identification|textbf}
\index{BV algebra!bar complex identification!Heisenberg}

The free-field case proves the scalar free-energy identity
predicted by Conjecture~\ref{conj:v1-master-bv-brst}
for the Heisenberg family. The proof uses four independent
arguments that all produce the same identity.

\begin{theorem}[BV $=$ bar for the Heisenberg at all genera;
\ClaimStatusProvedHere]
\label{thm:heisenberg-bv-bar-all-genera}
\index{Heisenberg!BV partition function}
\index{Faber--Pandharipande number!BV/bar identification}
For the Heisenberg vertex algebra $\cH_\kappa$ at level
$\kappa \neq 0$ and for every genus $g \geq 1$:
\begin{equation}\label{eq:bv-bar-heisenberg}
exec
/bin/zsh -lc "sed -n '1984,1991p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7066,7071p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '523,541p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{remark}[Why the Heisenberg is special]
\label{rem:heisenberg-bv-bar-scope}
\index{BV algebra!bar complex identification!scope}
Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
consequence predicted by
Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
family at all genera.
The Heisenberg succeeds because it is class~G:
a single Gaussian channel, no interaction vertices, and
 succeeded in 51ms:
For a holomorphic field theory on a Riemann surface, the BV/BRST
complex coincides with the bar complex of the associated chiral algebra,
at all genera.

\emph{Resolved in $D^{\mathrm{co}}$}
\textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
the BV and bar complexes are quasi-isomorphic in the coderived category
for all chirally Koszul algebras, including class~M.
The chain-level identification holds for classes~G and~L, is
conditional for class~C on harmonic decoupling, and
\emph{fails} for class~M
 succeeded in 51ms:
 harmonic correction does not factor through a free subsystem.
\end{enumerate}
The three mechanisms combine to show that the quartic
harmonic-propagator correction vanishes for the $\beta\gamma$
system at genus~$1$, despite the nonzero quartic shadow
$Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
resolved obstructions~(1) and~(2), this establishes the
scalar genus-$1$ consequence predicted by
Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
local model for the
all-genera harmonic-decoupling hypothesis used in
Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
exec
/bin/zsh -lc "sed -n '3378,3384p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '718,726p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11166,11172p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10255,10263p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11276,11284p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7744,7747p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9830,9835p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 The dg-shifted Yangian is proved for the affine lineage
 (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}).
 The general perturbative 3d~HT Yangian structure is conjectural.
 The BV/BRST~$=$~bar identification at higher genus is resolved
 in the coderived category $D^{\mathrm{co}}$ for all shadow classes
 (Theorem~\ref{thm:bv-bar-coderived});
 succeeded in 52ms:
 (Theorem~\ref{thm:algebraic-string-dictionary}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}.
 BV=bar in the coderived category is proved for all four shadow
 classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
 The genuswise chain-level BV/BRST/bar identification remains
 conjectural in general: classes~G and~L are proved, class~C is
 conditional on harmonic decoupling, and class~M is chain-level
 succeeded in 51ms:
\textbf{unconditionally closed} at all stages via
$\mathcal{W}_N$ rigidity
(Theorem~\ref{thm:winfty-all-stages-rigidity-closure})
within the strong completion-tower framework
(Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
Yangian tower is closed on the evaluation-generated core ($249$~tests);
the DK-$5$ categorical packet in type~$A$ is now accessible
(downstream of the MC3 package proved on the evaluation-generated core).
On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
the genus-$1$ bar-side curvature package is proved
\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
and~\ref{thm:genus1-d-squared}\textup{)}; and for
genus $g \ge 2$, inductive genus determination
(Theorem~\ref{thm:inductive-genus-determination}),
two-dimensional convergence
(Proposition~\ref{prop:2d-convergence}),
and the HS-sewing criterion
(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
 succeeded in 51ms:
 (1)~\textbf{Analytic HS-sewing proved} at all genera: polynomial OPE growth $+$ subexponential sector growth implies convergence
 (Theorem~\ref{thm:general-hs-sewing});
 (2)~\textbf{Genus-$0$ algebraic BRST/bar proved}
 (Theorem~\ref{thm:algebraic-string-dictionary});
 (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived});
 (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
 succeeded in 51ms:
The CG BV formalism motivates the BRST/bar comparison package in
Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
in the coderived category $D^{\mathrm{co}}$ for all shadow classes
(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
Heisenberg scalar identification is proved at all genera
(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
G and~L are proved, class~C is conditional on harmonic decoupling,
and the chain-level identification fails for class~M
(Conjecture~\ref{conj:v1-master-bv-brst}).
 succeeded in 51ms:
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 succeeded in 51ms:
 At genus~$0$, the PVA descent theorems identify the two
 convolution algebras and their MC elements.
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 succeeded in 51ms:
 (d)~direct bar-complex graph sum
 (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 Three obstructions to extending the identification
 beyond the scalar level are identified at the chain level
 (Proposition~\ref{prop:chain-level-three-obstructions}):
 (i)~the homotopy-transfer correction from the SDR data,
 (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
 (iii)~the curved $\Ainf$-structure vs flat BV operator.
 Obstruction~(iii) is resolved for classes~G and~L
 succeeded in 52ms:
\label{rem:concordance-frontier-status-2026}
\index{open conjectures!frontier status 2026}
The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
\begin{enumerate}
 succeeded in 51ms:
& Entanglement entropy $S_{\mathrm{EE}} = (c/3)\log(L/\epsilon)$
 from $\kappa$-level complementarity \\
& Holographic dictionary:
 bulk reconstruction from the derived center \\
& BV/BRST $=$ bar at higher genus:
 resolved in $D^{\mathrm{co}}$ for all shadow classes
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Inspecting truncated outputs**

I’ve noticed some outputs got truncated due to ranges being too short. I need to take a closer look at the missing ends, specifically for the editorial line after the HS-sewing criterion, the concordance frontier item lines 7744-7747, and the table row line 9830-9835. Also, there are line numbers 11166-11172 that need attention. I’ll need to adjust the ranges to ensure I capture everything properly. Let's go for longer ranges!
exec
/bin/zsh -lc "sed -n '537,545p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7744,7748p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:inductive-genus-determination}),
two-dimensional convergence
(Proposition~\ref{prop:2d-convergence}),
and the HS-sewing criterion
(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
sewing/convergence lane. The higher-genus BV/BRST/bar
identification itself remains the downstream physics completion.
\emph{Critical point}: MC3 package~(i) (categorical CG) is now
resolved for all types
 succeeded in 52ms:
\label{rem:concordance-frontier-status-2026}
\index{open conjectures!frontier status 2026}
The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
\begin{enumerate}
\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
exec
/bin/zsh -lc "sed -n '11166,11174p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9830,9837p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10260,10266p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11276,11285p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 (i)~the homotopy-transfer correction from the SDR data,
 (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
 (iii)~the curved $\Ainf$-structure vs flat BV operator.
 Obstruction~(iii) is resolved for classes~G and~L
 at the chain level, and for class~C conditional on harmonic
 decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
 For class~M, the chain-level identification \emph{fails}:
 succeeded in 52ms:
& Entanglement entropy $S_{\mathrm{EE}} = (c/3)\log(L/\epsilon)$
 from $\kappa$-level complementarity \\
& Holographic dictionary:
 bulk reconstruction from the derived center \\
& BV/BRST $=$ bar at higher genus:
 resolved in $D^{\mathrm{co}}$ for all shadow classes
 \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
 chain-level proved for classes~G/L, conditional for class~C on
 succeeded in 52ms:
 At genus~$0$, the PVA descent theorems identify the two
 convolution algebras and their MC elements.
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
 \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
 succeeded in 50ms:
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Considering output adjustments**

Okay, it seems I'm trying to figure out how to adjust the display for better visibility. Maybe I should use slightly wider margins or even open with line numbers? Inspecting the frontier item and the line after a certain chain-level phrase is important too. I could try using grep with the -n option. For clarity, widening the output might help too. Let's figure out the best approach for this!
exec
/bin/zsh -lc "sed -n '9830,9838p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11168,11176p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '11276,11286p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7744,7750p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
& Entanglement entropy $S_{\mathrm{EE}} = (c/3)\log(L/\epsilon)$
 from $\kappa$-level complementarity \\
& Holographic dictionary:
 bulk reconstruction from the derived center \\
& BV/BRST $=$ bar at higher genus:
 resolved in $D^{\mathrm{co}}$ for all shadow classes
 \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
 chain-level proved for classes~G/L, conditional for class~C on
 harmonic decoupling, false for class~M;
 succeeded in 51ms:
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
 \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
 sending $\Theta^{\mathrm{oc}}_\cA$ to
 $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
 succeeded in 51ms:
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 succeeded in 51ms:
\label{rem:concordance-frontier-status-2026}
\index{open conjectures!frontier status 2026}
The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
\begin{enumerate}
\item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
 \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
\item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '11168,11178p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 In $D^{\mathrm{co}}$, the identification extends to all genera
 and all shadow classes: the degree-$r$ chain-level obstruction
 $\delta_r \propto m_0^{\lfloor r/2\rfloor - 1}$ is
 coderived-exact since $m_0 \cdot x = d^2(x) \in
 \operatorname{Im}(d)$. The chain-level identification
 $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
 \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
 sending $\Theta^{\mathrm{oc}}_\cA$ to
 $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
 conditional for class~C on harmonic decoupling, and false for
 class~M at the ordinary chain level.
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '11276,11288p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \emph{Misleading.}
 MC1 through MC4 are proved. MC5 is resolved
 analytically and in the coderived category, but not at
 chain level: the analytic HS-sewing package is proved
 at all genera (Theorem~\ref{thm:general-hs-sewing}); the
 genus-$0$ algebraic BRST/bar comparison is proved
 (Theorem~\ref{thm:algebraic-string-dictionary}); BV=bar
 in the coderived category is proved for all four shadow
 classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived}); the tree-level
 amplitude pairing is conditional on
 Corollary~\ref{cor:string-amplitude-genus0}; the
 genuswise chain-level BV/BRST/bar identification remains
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '11288,11292p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 genuswise chain-level BV/BRST/bar identification remains
 conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
 classes~G/L proved, class~C conditional on harmonic decoupling,
 class~M chain-level false).
MC3 splits into three layers
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Evaluating text for clarity**

I think everything looks okay overall, but I might need to inspect the continuation for item 3384. It's fine, but I want to be cautious. I should also take a look at the extended line for item 7066 to ensure that the grammar is correct. I'll use a broader perspective when checking these to catch any potential issues. It’s always best to double-check, just to be safe!
exec
/bin/zsh -lc "sed -n '7066,7073p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 The dg-shifted Yangian is proved for the affine lineage
 (Vol~II, Theorem~\textup{thm:Koszul\_dual\_Yangian}).
 The general perturbative 3d~HT Yangian structure is conjectural.
 The BV/BRST~$=$~bar identification at higher genus is resolved
 in the coderived category $D^{\mathrm{co}}$ for all shadow classes
 (Theorem~\ref{thm:bv-bar-coderived});
 at chain level, classes~G and~L are proved, class~C is conditional
 on harmonic decoupling, and class~M fails.
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '9830,9836p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
& Entanglement entropy $S_{\mathrm{EE}} = (c/3)\log(L/\epsilon)$
 from $\kappa$-level complementarity \\
& Holographic dictionary:
 bulk reconstruction from the derived center \\
& BV/BRST $=$ bar at higher genus:
 resolved in $D^{\mathrm{co}}$ for all shadow classes
 \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '9836,9840p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
 chain-level proved for classes~G/L, conditional for class~C on
 harmonic decoupling, false for class~M;
 Heisenberg scalar level proved at chain level
 \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '3378,3385p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 (1)~\textbf{Analytic HS-sewing proved} at all genera: polynomial OPE growth $+$ subexponential sector growth implies convergence
 (Theorem~\ref{thm:general-hs-sewing});
 (2)~\textbf{Genus-$0$ algebraic BRST/bar proved}
 (Theorem~\ref{thm:algebraic-string-dictionary});
 (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
 (Theorem~\ref{thm:bv-bar-coderived});
 (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
 (classes~G/L proved, class~C conditional on harmonic decoupling,
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

exec
/bin/zsh -lc "sed -n '3385,3387p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 (classes~G/L proved, class~C conditional on harmonic decoupling,
 class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
 (5)~tree-level amplitude pairing \textbf{conditional} on
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining



thinking
**Running grep for patterns**

I need to run grep for forbidden patterns in the modified files, and maybe also check for references and labels. It seems useful to look for stale phrases like `classes G, L, C`, and I might want to grep those out. I should specifically target modified files for suspicious patterns, like `classesG, L, C` or `remains open for classM`. The user specifically asked for grep to check forbidden patterns, so I’ll focus on that.
thinking
**Grep status patterns in files**

I need to grep for status patterns specifically in the modified files. I'll look for terms like `classesG, L, C`, `classM remains false`, and some conjecture references. It seems there might be phrases like `MC5 at genus$0$ and genus$1$`. I also want to check for banned prose such as em-dashes, since the entire file might have multiple occurrences. The user asked for grep after every .tex write, so I’ll focus on the specific stale phrases we touched in our revision.
codex
The local reread is consistent. I’m doing the final grep pass now against the modified files for the stale status phrases that motivated the fix, plus a quick bad-prose check on the edited surfaces.
exec
/bin/zsh -lc "rg -n -F 'Conjecture~\\ref{conj:v1-master-bv-brst} at the scalar level' chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'classes~G, L, C' chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'holds for classes~G, L, C' chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'MC5 at genus~"'$0$ and genus~$1$ is proved'"' chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -- '---|"'```'"' chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/editorial_constitution.tex:829:Ind. & --- & ${\sim}8$ independent problems
chapters/connections/concordance.tex:2415:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:2520:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:2566:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:2639:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:3048:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:3083:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:3102:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:3177:%% ------------------------------------------------------------------
chapters/connections/concordance.tex:9669:% ----------------------------------------------------------------------
chapters/connections/concordance.tex:9901:% ----------------------------------------------------------------------
chapters/connections/concordance.tex:9906:% ----------------------------------------------------------------------
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining



thinking
**Exploring verification processes**

I'm thinking about how to avoid failing verification. Maybe I could just search the differences? It seems `rg` showed no stale status phrases, but I notice that `---` matches things outside the edits. The user did ask for verification, so I should mention that. Perhaps running commands like `git diff --stat` or `git diff --unified=0` could help review modified files. It might be worth using `exec` as well.
thinking
**Checking git changes**

I need to check the git diff for the lines that were touched. I'll use the command `git diff -- chapters/...` to confirm the changes. Perhaps I should add some commentary for clarity. I’m thinking running it for the files might be helpful, but I want to make sure to do it without any specific context first. It seems like a straightforward approach!
exec
/bin/zsh -lc 'git diff --unified=0 -- chapters/connections/bv_brst.tex chapters/connections/editorial_constitution.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa27491..dae2eab 100644
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1406,2 +1406,2 @@ the ambient cyclic deformation formal moduli problem
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
@@ -1628,4 +1628,5 @@ $\lambda_3^{\mathrm{FP}} = 31/967680$.
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
@@ -1849,3 +1850,4 @@ $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Updating process status**

Alright, I need to run the update plan steps to check their statuses. I’ve completed Step 1, which was the inventory, and Step 2 is done with the patch. Now, I think Step 3, which involves verification after using grep, might be completed too. I just want to ensure everything's properly updated before moving forward. Okay, let's get this done!
Plan update
Applied the status-surface corrections and verified the edited passages plus a targeted grep pass against the stale MC5 phrases.
  ✓ Inventory status mismatches in chapters/connections, including bv_brst.tex and concordance.tex
  ✓ Patch the affected connection files with minimal truthful status edits
  ✓ Re-read modified surfaces and grep modified files for status/forbidden-pattern regressions
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Considering the explorer agent**

I'm thinking it's probably a good idea to consider closing the explorer agent. There are aspects that suggest this might be wise. I want to weigh the options carefully before deciding to ensure I'm making the right choice. I hope I’m not jumping the gun here! But it feels like the right move at this moment. Let me just gather more thoughts before I make a final decision.
collab close_agent(call_jXaUrcHAoHdIzF1wmoEjvXkP)
  receiver: 019d8773-3334-74d2-8498-5c20d9febadf
close_agent(call_jXaUrcHAoHdIzF1wmoEjvXkP) completed: "- **ClaimStatus drift:** Checked every label in `chapters/connections` that participates in the “ten load-bearing conjec…":
  receiver: 019d8773-3334-74d2-8498-5c20d9febadf
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining


thinking
**Considering format for findings**

I’m thinking about how to organize the task. A paragraph plus bullet points might work well since it mentions every finding. I could create short sections like **Status** and verification. It seems useful to include line numbers after edits. I could derive those from a diff or use the `nl -ba`, but I want to ensure the final output has exact line numbers if I use links. I wonder if I can use approximate numbers from sed outputs as an alternative?
exec
/bin/zsh -lc "rg -n 'conditional on harmonic decoupling|conjectural in general|chain-level proved for classes~G/L|At the ordinary chain level|at chain level, classes~G and~L are proved|is proved for classes~G and~L' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'conditional for class~C on harmonic decoupling|analytic sewing/convergence lane|genus-\\"'$0'"\\"'$ algebraic BRST/bar comparison is proved'"' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'scalar free-energy identity|scalar genus-\\"'$1'"\\"'$ consequence|consequence predicted by'"' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
445:conditional for class~C on harmonic decoupling, and
531:On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
 succeeded in 52ms:
1406:The free-field case proves the scalar free-energy identity
1630:consequence predicted by
1851:scalar genus-$1$ consequence predicted by
 succeeded in 52ms:
724:G and~L are proved, class~C is conditional on harmonic decoupling,
1990: conjectural in general: classes~G and~L are proved, class~C is
1991: conditional on harmonic decoupling, and class~M is chain-level
3384: (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
3385: (classes~G/L proved, class~C conditional on harmonic decoupling,
7072: at chain level, classes~G and~L are proved, class~C is conditional
7749: \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
9691: chain-level lift is conjectural in general.
9837: chain-level proved for classes~G/L, conditional for class~C on
11176: $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
11289: conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
11290: classes~G/L proved, class~C conditional on harmonic decoupling,
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining




thinking
**Reflecting on repo connections**

I'm pondering the user's request about connection files, focusing only on the current repo, and realizing that mentioning details that are outside this scope could complicate things. The completeness contract requires addressing all findings, and while "ClaimStatus mismatches in ALL chapters/connections" applies, the cross-volume conflict actually isn't included. I think a concise note stating there was no edit for that cross-volume instance would be transparent. But I’ll need to frame it carefully to avoid follow-up questions.
thinking
**Clarifying patch details**

I'm considering whether to mention that no TeX build was run. Since I didn’t run one, I think it’s important to note that. The grep results show no matches for the targeted stale phrases, but I found pre-existing comment and table separators in the file without this patch. I wonder if mentioning this is too detailed. I need to present a concise conclusion while ensuring clarity regarding the verification loop the user asked about.
thinking
**Planning the structure**

I want to make sure that my final output is under 50 to 70 lines, aiming for around 12 to 15 lines. It’s important to keep that in mind while crafting my response! I think if I can stay focused and organized, I should be able to create something concise yet informative. Let’s work on that structure together, so it’s clear and within those guidelines. Getting this right is key!
codex
Updated the MC5 status prose in [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1406), [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:440), and [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:718) so they now match the live BV/bar surface: coderived `D^{\mathrm{co}}` resolved for all classes, ordinary chain level proved for `G/L`, conditional for `C` on harmonic decoupling, and false for `M`.

`FIXED`
- [bv_brst.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/bv_brst.tex:1406): removed the overstatement that scalar Heisenberg/class `C` results “resolve” the full chain-level conjecture; they now read as scalar consequences predicted by `conj:v1-master-bv-brst`.
- [editorial_constitution.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/editorial_constitution.tex:440): corrected the conjecture-status gloss from “G/L/C proved” to `G/L` proved, `C` conditional, `M` false; also narrowed the later “MC5 is proved” sentence to the genus-0/genus-1/analytic sewing lanes only.
- [concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:718): normalized the repeated MC5 summaries and tables at the affected status blocks so they no longer claim unconditional class `C` chain-level resolution.

Verification: I re-read the edited passages and ran targeted `rg` checks for the stale phrases (`classes~G, L, C`, `holds for classes~G, L, C`, `Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level`, `MC5 at genus~$0$ and genus~$1$ is proved`); all returned no matches. I did not run a TeX build. A generic `---|```` grep only hit pre-existing comment/table separators outside the edited status text.

One cross-volume label split remains outside this patch: `thm:general-hs-sewing` still differs between Vol I and Vol II, and I left the Vol II duplicate untouched because it was outside the assigned file set.
file update:
diff --git a/chapters/connections/bv_brst.tex b/chapters/connections/bv_brst.tex
index fa2749149ab05703e3a00e13e3f1eb6b7807d89c..dae2eab3d53ce646d5d16c3b960ccc7eb9b0d0e4
--- a/chapters/connections/bv_brst.tex
+++ b/chapters/connections/bv_brst.tex
@@ -1403,8 +1403,8 @@
 \index{Heisenberg!BV/bar identification|textbf}
 \index{BV algebra!bar complex identification!Heisenberg}
 
-The free-field case resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level
+The free-field case proves the scalar free-energy identity
+predicted by Conjecture~\ref{conj:v1-master-bv-brst}
 for the Heisenberg family. The proof uses four independent
 arguments that all produce the same identity.
 
@@ -1625,10 +1625,11 @@
 \begin{remark}[Why the Heisenberg is special]
 \label{rem:heisenberg-bv-bar-scope}
 \index{BV algebra!bar complex identification!scope}
-Theorem~\ref{thm:heisenberg-bv-bar-all-genera} resolves
-Conjecture~\ref{conj:v1-master-bv-brst} at the \emph{scalar level}
-\textup{(}partition function\slash free energy\textup{)} for the
-Heisenberg family at all genera.
+Theorem~\ref{thm:heisenberg-bv-bar-all-genera} proves the
+\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
+consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for the Heisenberg
+family at all genera.
 The Heisenberg succeeds because it is class~G:
 a single Gaussian channel, no interaction vertices, and
 all moduli dependence controlled by the Quillen anomaly.
@@ -1846,9 +1847,10 @@
 harmonic-propagator correction vanishes for the $\beta\gamma$
 system at genus~$1$, despite the nonzero quartic shadow
 $Q^{\mathrm{contact}}_{\beta\gamma}$. Together with the
-resolved obstructions~(1) and~(2), this establishes
-Conjecture~\ref{conj:v1-master-bv-brst} at the scalar level for
-class~C at genus~$1$. This is the local model for the
+resolved obstructions~(1) and~(2), this establishes the
+scalar genus-$1$ consequence predicted by
+Conjecture~\ref{conj:v1-master-bv-brst} for class~C. This is the
+local model for the
 all-genera harmonic-decoupling hypothesis used in
 Theorem~\ref{thm:bv-bar-coderived}: once every harmonic insertion
 factors through the same composite free-field sector, the quartic
diff --git a/chapters/connections/concordance.tex b/chapters/connections/concordance.tex
index 291debed9c83e0c0edbbf39f11d74b74b0ff8b69..b5630154d0b1947aa5a56fb440ac6a1eccc7c681
--- a/chapters/connections/concordance.tex
+++ b/chapters/connections/concordance.tex
@@ -715,14 +715,15 @@
  The genus universality theorem shows that these two perspectives
  produce the same genus-$g$ obstruction class.
 \item \emph{BV-BRST.}
- The CG BV formalism motivates the BRST/bar comparison package in
- Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
- in the coderived category $D^{\mathrm{co}}$ for all shadow classes
- (Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
- Heisenberg scalar identification is proved at all genera
- (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
- G, L, C are proved. The chain-level identification fails for
- class~M (Conjecture~\ref{conj:v1-master-bv-brst}).
+The CG BV formalism motivates the BRST/bar comparison package in
+Chapter~\ref{ch:bv-brst}. The BV/bar identification is resolved
+in the coderived category $D^{\mathrm{co}}$ for all shadow classes
+(Theorem~\ref{thm:bv-bar-coderived}); at the chain level, the
+Heisenberg scalar identification is proved at all genera
+(Theorem~\ref{thm:heisenberg-bv-bar-all-genera}), and classes
+G and~L are proved, class~C is conditional on harmonic decoupling,
+and the chain-level identification fails for class~M
+(Conjecture~\ref{conj:v1-master-bv-brst}).
 \item \emph{Monoidal bar-cobar.}
  Booth--Lazarev~\cite{BL24} construct monoidal model structures on
  categories of coalgebras, providing the homotopical infrastructure
@@ -1986,8 +1987,9 @@
  BV=bar in the coderived category is proved for all four shadow
  classes including class~M (Theorem~\ref{thm:bv-bar-coderived}).
  The genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst}; class~M
- chain-level false).
+ conjectural in general: classes~G and~L are proved, class~C is
+ conditional on harmonic decoupling, and class~M is chain-level
+ false (Conjecture~\ref{conj:v1-master-bv-brst}).
  Pillar~C (Mok's log-smooth degeneration) provides additional
  inductive structure via rigid special-fibre decomposition.
  \emph{Arithmetic connection}: the sewing--Selberg formula
@@ -3379,8 +3381,9 @@
  (Theorem~\ref{thm:algebraic-string-dictionary});
  (3)~\textbf{$D^{\mathrm{co}}$-level BV=bar proved} for all four shadow classes including class~M
  (Theorem~\ref{thm:bv-bar-coderived});
- (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural}
- (class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
+ (4)~genuswise chain-level BV/BRST/bar identification \textbf{conjectural in general}
+ (classes~G/L proved, class~C conditional on harmonic decoupling,
+ class~M chain-level false; Conjecture~\ref{conj:v1-master-bv-brst});
  (5)~tree-level amplitude pairing \textbf{conditional} on
  Corollary~\ref{cor:string-amplitude-genus0} \\
 \bottomrule
@@ -7066,7 +7069,8 @@
  The BV/BRST~$=$~bar identification at higher genus is resolved
  in the coderived category $D^{\mathrm{co}}$ for all shadow classes
  (Theorem~\ref{thm:bv-bar-coderived});
- the chain-level identification fails for class~M.
+ at chain level, classes~G and~L are proved, class~C is conditional
+ on harmonic decoupling, and class~M fails.
  The Heisenberg scalar level is proved at the chain level
  (Theorem~\ref{thm:heisenberg-bv-bar-all-genera}).
 \end{enumerate}
@@ -7742,7 +7746,7 @@
 The ten most load-bearing genuinely open conjectures, ranked by downstream impact:
 \begin{enumerate}
 \item \textup{Conjecture~\ref{conj:v1-master-bv-brst} (BV/BRST~$=$~bar at higher genus).}
- \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. The chain-level identification remains false for class~M (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$). Chain-level proved for classes G, L, C.
+ \textbf{Resolved in $D^{\mathrm{co}}$} (Theorem~\ref{thm:bv-bar-coderived}): the BV and bar complexes are quasi-isomorphic in the coderived category for all four shadow classes, including class~M. At the ordinary chain level, classes~G and~L are proved, class~C is conditional on harmonic decoupling, and class~M remains false (quartic harmonic obstruction $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a coboundary in ordinary chain complexes, but $m_0 \cdot x = d^2(x) \in \operatorname{Im}(d)$ in $D^{\mathrm{co}}$).
 \item \textup{Conjecture~\ref{conj:master-dk-kl} (DK--KL identification).}
  Restricted DK-4 on the evaluation-generated core is the next step.
 \item \textup{Conjecture~\ref{conj:v1-master-infinite-generator} (infinite-generator completion).}
@@ -9830,7 +9834,8 @@
 & BV/BRST $=$ bar at higher genus:
  resolved in $D^{\mathrm{co}}$ for all shadow classes
  \textup{(}Theorem~\ref{thm:bv-bar-coderived}\textup{)};
- chain-level false for class~M;
+ chain-level proved for classes~G/L, conditional for class~C on
+ harmonic decoupling, false for class~M;
  Heisenberg scalar level proved at chain level
  \textup{(}Theorem~\ref{thm:heisenberg-bv-bar-all-genera}\textup{)} \\
 & Shadow--chromatic correspondence
@@ -10255,9 +10260,9 @@
  (i)~the homotopy-transfer correction from the SDR data,
  (ii)~the non-abelian sewing kernel at genus~$\geq 2$,
  (iii)~the curved $\Ainf$-structure vs flat BV operator.
- Obstruction~(iii) is resolved for classes~G, L, and~C
- at the chain level
- (Remark~\ref{rem:bv-bar-class-c-proof}).
+ Obstruction~(iii) is resolved for classes~G and~L
+ at the chain level, and for class~C conditional on harmonic
+ decoupling (Theorem~\ref{thm:bv-bar-coderived}(iii)).
  For class~M, the chain-level identification \emph{fails}:
  the quartic harmonic discrepancy
  $\delta_4 \propto Q^{\mathrm{contact}} \cdot m_0$ is not a
@@ -11168,7 +11173,9 @@
  $\mathfrak{g}^{\mathrm{oc}}_\cA|_{g \geq 1}
  \simeq \mathfrak{g}^{\mathrm{BV}}_T|_{g \geq 1}$
  sending $\Theta^{\mathrm{oc}}_\cA$ to
- $\Theta^{\mathrm{BV}}_T$ remains open for class~M.
+ $\Theta^{\mathrm{BV}}_T$ is proved for classes~G and~L,
+ conditional for class~C on harmonic decoupling, and false for
+ class~M at the ordinary chain level.
 
 \item \emph{Pixton ideal generation}
  \textup{(}Theorem~\ref{thm:pixton-from-shadows}\textup{)}.
@@ -11279,7 +11286,8 @@
  amplitude pairing is conditional on
  Corollary~\ref{cor:string-amplitude-genus0}; the
  genuswise chain-level BV/BRST/bar identification remains
- conjectural (Conjecture~\ref{conj:v1-master-bv-brst};
+ conjectural in general (Conjecture~\ref{conj:v1-master-bv-brst};
+ classes~G/L proved, class~C conditional on harmonic decoupling,
  class~M chain-level false).
 MC3 splits into three layers
 (Corollary~\ref{cor:mc3-all-types} and
diff --git a/chapters/connections/editorial_constitution.tex b/chapters/connections/editorial_constitution.tex
index af7fc10b3acb4c369dc372e1a10a718c25102890..76accbbf936de0504f581b19b2a20bbce8b19289
--- a/chapters/connections/editorial_constitution.tex
+++ b/chapters/connections/editorial_constitution.tex
@@ -441,7 +441,8 @@
 \textup{(}Theorem~\textup{\ref{thm:bv-bar-coderived}}\textup{)}:
 the BV and bar complexes are quasi-isomorphic in the coderived category
 for all chirally Koszul algebras, including class~M.
-The chain-level identification holds for classes~G, L, C but
+The chain-level identification holds for classes~G and~L, is
+conditional for class~C on harmonic decoupling, and
 \emph{fails} for class~M
 \textup{(}quartic harmonic obstruction\textup{)}.
 
@@ -526,15 +527,20 @@
 (Theorem~\ref{thm:completed-bar-cobar-strong}). MC4 on the
 Yangian tower is closed on the evaluation-generated core ($249$~tests);
 the DK-$5$ categorical packet in type~$A$ is now accessible
-(downstream of the MC3 package proved on the evaluation-generated core). MC5 at
-genus~$0$ and genus~$1$ is proved
-(Theorems~\ref{thm:genus1-universal-curvature}
-and~\ref{thm:genus1-d-squared}); genus $g \ge 2$ is proved via inductive genus determination
+(downstream of the MC3 package proved on the evaluation-generated core).
+On the MC5 side, the genus-$0$ algebraic BRST/bar comparison is proved
+\textup{(}Theorem~\ref{thm:algebraic-string-dictionary}\textup{)};
+the genus-$1$ bar-side curvature package is proved
+\textup{(}Theorems~\ref{thm:genus1-universal-curvature}
+and~\ref{thm:genus1-d-squared}\textup{)}; and for
+genus $g \ge 2$, inductive genus determination
 (Theorem~\ref{thm:inductive-genus-determination}),
 two-dimensional convergence
 (Proposition~\ref{prop:2d-convergence}),
 and the HS-sewing criterion
-(Theorem~\ref{thm:general-hs-sewing}).
+(Theorem~\ref{thm:general-hs-sewing}) prove the analytic
+sewing/convergence lane. The higher-genus BV/BRST/bar
+identification itself remains the downstream physics completion.
 \emph{Critical point}: MC3 package~(i) (categorical CG) is now
 resolved for all types
 (Theorem~\ref{thm:categorical-cg-all-types}); the remaining

tokens used
473,967
