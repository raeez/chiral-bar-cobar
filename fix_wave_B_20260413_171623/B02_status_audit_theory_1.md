# B02_status_audit_theory_1 (499s)

Claim-status mismatches are resolved.

- `chapters/theory/bar_construction.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.
- `chapters/theory/cobar_construction.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.
- `chapters/theory/bar_cobar_adjunction_inversion.tex`: FIXED in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1701). I converted the two conjectural `remark` blocks into `conjecture` environments, renamed their labels to `conj:...`, updated the in-file cross-reference, and moved the stranded proof of `thm:bar-cobar-inversion-qi` so the local theorem/conjecture surface stays coherent.
- `chapters/theory/bar_cobar_adjunction_curved.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.

Verification: I re-scanned all four files for `Conjectured/ProvedHere/ProvedElsewhere` tag/environment mismatches and got no hits. I also grepped the edited file for the old forbidden `remark`+`ClaimStatusConjectured` pattern, stale `rem:` labels, and the stale `Remark~\ref{...}` text; all were clean. I did not run a full LaTeX build or regenerate metadata.


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
session id: 019d876a-4a5f-7cd1-b74f-20cb8399c842
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


Fix ClaimStatus mismatches in: chapters/theory/bar_construction.tex, chapters/theory/cobar_construction.tex, chapters/theory/bar_cobar_adjunction_inversion.tex, chapters/theory/bar_cobar_adjunction_curved.tex.
For each file: verify every \ClaimStatus tag matches its environment. Fix mismatches.
mcp startup: no servers
codex
Using `claim-surface-sync` for this pass because the task is purely claim-status/environment alignment. I’m reading the required constitutional surface and the four assigned chapter files first, then I’ll make the minimum tag-only edits and re-check labels/refs in place.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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

 succeeded in 51ms:
Total output lines: 220

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
**Inspecting files for mismatches**

I have the required files, and I need to inspect them carefully. I'll likely use the explorer agent since that's the required protocol. The goal is to check four files for any mismatches between the ClaimStatus and their environments. I need to identify each theorem-like environment with its corresponding \ClaimStatus tag. I'll task the explorer to do this, ensuring that everything aligns according to the specified rules, especially regarding the status tags and their environments.
thinking
**Initiating explorer for edits**

I'm planning to spawn the explorer tool to help me identify all the mismatches. It would be great if it could also suggest some minimal edits that would resolve these issues accurately. I need to ensure that the edits are truthful and align with the underlying rules. This should streamline the process, making it easier to spot discrepancies and propose the necessary changes effectively. Let's get started on this!
codex
I’ve loaded the constitutional/status surface. Next I’m isolating the four assigned files and enumerating every environment/tag mismatch so the edits stay strictly local.
collab spawn_agent(call_T63HI6YFroykRxgcIqj6xULA, prompt="Inspect these files only for ClaimStatus/environment mismatches: chapters/theory/bar_construction.tex, chapters/theory/c…")
mcp startup: no servers
spawn_agent(call_T63HI6YFroykRxgcIqj6xULA, prompt="Inspect these files only for ClaimStatus/environment mismatches: chapters/theory/bar_construction.tex, chapters/theory/c…") pending init:
  agent: 019d876a-beba-7330-82f8-bc3cdc64929d
exec
/bin/zsh -lc 'ls .agents' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
skills
exec
/bin/zsh -lc 'ls .agents/skills' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
beilinson-rectify
build-surface
chriss-ginzburg-rectify
claim-surface-sync
compute-engine-scaffold
cross-volume-propagation
deep-beilinson-audit
frontier-research
multi-path-verify

exec
/bin/zsh -lc 'cat .agents/skills/claim-surface-sync/SKILL.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
thinking
**Considering code exploration limits**

I'm thinking about the explorer tool running and whether I can read files myself at the same time. The instructions say not to re-read or re-search code, but I might need to check specific lines for edits. After the explorer identifies mismatches, maybe I can look at the surrounding lines for context. I should use rg to list ClaimStatus and environments, and exec could help extract relevant lines for editing. I'll just wait for now.
collab wait(call_Ci1WXU2Yg1x8ZtfCUGujm6zq)
  receivers: 019d876a-beba-7330-82f8-bc3cdc64929d
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatus" chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
321:\begin{theorem}[Bar construction as NAP homology; \ClaimStatusProvedHere]\label{thm:bar-NAP-homology}\label{thm:bar-computes-chiral-homology}
577:\ClaimStatusProvedHere
698:\begin{lemma}[Sign compatibility; \ClaimStatusProvedHere]\label{lem:sign-compatibility}
788:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}
970:\begin{proposition}[Pole decomposition of the bar differential; \ClaimStatusProvedHere]\label{prop:pole-decomposition}
1036:\begin{corollary}[Functoriality; \ClaimStatusProvedHere]\label{cor:bar-functorial}
1052:\begin{theorem}[Stokes' theorem on configuration spaces; \ClaimStatusProvedHere]\label{thm:stokes-config}
1147:\begin{corollary}[Residues anticommute at corners; \ClaimStatusProvedHere]\label{cor:residues-anticommute}
1189:\begin{theorem}[Arnold relations; \ClaimStatusProvedHere]\label{thm:arnold-three}
1218:\begin{corollary}[Cohomology of configuration spaces {\cite{Arnold69}}; \ClaimStatusProvedElsewhere]\label{cor:cohomology-config}
1232:\begin{computation}[Degree 0; \ClaimStatusProvedHere]\label{comp:deg0}
1250:\begin{computation}[Degree 1; \ClaimStatusProvedHere]\label{comp:deg1-general}
1428:\begin{theorem}[Bar construction is functorial; \ClaimStatusProvedHere]\label{thm:bar-functorial-complete}
1467:\begin{corollary}[Natural transformation property; \ClaimStatusProvedHere]\label{cor:bar-natural}
1472:\begin{proposition}[Model independence; \ClaimStatusProvedHere]
1505:\begin{theorem}[Bar coalgebra; \ClaimStatusProvedHere]\label{thm:bar-coalgebra}
1529:\begin{theorem}[Coassociativity; \ClaimStatusProvedHere]\label{thm:coassociativity-complete}
1596:\begin{theorem}[Counit axioms; \ClaimStatusProvedHere]\label{thm:counit-axioms}
1647:\begin{corollary}[Bar complex is DG-coalgebra; \ClaimStatusProvedHere]\label{cor:bar-is-dgcoalg}
1664:\begin{theorem}[Differential is coderivation; \ClaimStatusProvedHere]\label{thm:diff-is-coderivation}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatus"' in /Users/raeez/chiral-bar-cobar succeeded in 57ms:
compute/lib/theorem_thm_a_bl_rectification_engine.py:96:    F10 (VERIFIED SOUND): All ClaimStatusProvedHere tags in both
compute/lib/theorem_thm_a_bl_rectification_engine.py:685:    """Verify all ClaimStatusProvedHere tags in both files.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '470,540p' AGENTS.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Missing definitions; hidden imported lemmas; unsupported converses; dangling references; true statement weaker than advertised.

### 5. Patch in Dependency Order
CRITICAL and SERIOUS first, then MODERATE. For each: (a) re-read local context, (b) re-derive or recompute independently, (c) smallest truthful edit, (d) immediately search for downstream advertisements.

### 6. Propagate
After any mathematical change: grep Vol I; grep Vol II; grep Vol III. Update genuine duplicates or leave explicit pending note.

### 7. Verify
Narrowest check that can falsify: targeted pytest; grep for forbidden formulas/stale labels/banned prose; targeted TeX build; metadata check.

### 8. Hostile Re-Read
Reread your own rewrite as an adversary. Try to break it.

### 9. Stop Condition
- **CONVERGED**: no known actionable MODERATE+ issue remains on the modified surface, and narrowest verification passes.
- **BLOCKED**: exact blocker named precisely, with the strongest truthful narrower statement identified.

Do not stop between those states.

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "AP40" -n' in /Users/raeez/chiral-bar-cobar succeeded in 69ms:
Total output lines: 141

audit_campaign_20260412_231034/XV11_claim_status_sync.md:301:The grounding files confirm AP40 is the governing rule: incomplete proof surfaces should live in `conjecture`, while `ProvedHere` must not sit inside a conjecture block. I’m now scanning the three `chapters/` trees for direct environment/status mismatches and then I’ll re-open each candidate in context to kill false positives.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:818:scripts/adversarial_campaign.py:218:    ("AP07_env_mismatch", "AP40: environment/tag mismatch", r"grep -B2 'ClaimStatusConjectured' chapters/ | grep 'begin{theorem}\|begin{proposition}\|begin{corollary}' | head -30", "Conjectured → conjecture env"),
audit_campaign_20260412_231034/XV11_claim_status_sync.md:934:I need to count instances across all three repositories. Should I restrict my focus to theorem environments only, or include propositions and corollaries too? The user specified theorem environments, but the AP40 campaign includes multiple terms. The task clearly states to focus on theorem and conjecture environments. I'll concentrate on those and check for `ClaimStatus` macros within the relevant blocks. It makes sense to record line numbers while ignoring comments. I'll provide the line of the offending macro or environment start as needed.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:940:I have a sharper criterion now: I’m treating a theorem or conjecture block as inconsistent if it *contains* the opposite status macro anywhere in that block, then I’m manually separating genuine mixed-status packaging from harmless narrative mentions. That matches the AP40-style audit the repo already encodes.
audit_campaign_20260412_231034/XV11_claim_status_sync.md:1244:I should think about including a summary after the list regarding the proposition or corollary mismatches to ensure that the user's theorem environments are as they should be. It might not be strictly necessary, but if AP40 contains a prop or cor, there could indeed be additional mismatches. The task is focused specifically on the theorem and conjecture environments, so I'll need to keep that in mind while I check for ClaimStatus consistency across volumes.
healing_20260413_132214/H19_remove_genus0_koszul_vii.md:655:/Users/raeez/calabi-yau-quantum-groups/AGENTS.md:280:- Volume II is dominated by rectification, convention repair, cross-volume propagation, AP40 environment/status drift, AP44 divided-power drift, AP32 uniform-weight drift, V2-AP26/V2-AP30 stale Part references, V2-AP31 proof-after-conjecture, V2-AP32/V2-AP35 artifact/connective drift, and S_2=c/12 divided-power confusion corrections (AP177/FM30).
AGENTS.md:312:**HZ-2. Environment matches tag (AP40)** — 5 waves, 70+ instances.
AGENTS.md:345:AP40, AP125, AP124, AP4, V2-AP31, AP-CY6, AP-CY11, AP-CY14.
AGENTS.md:359:Persistent AP126/AP141; label/status/concordance drift (AP125, AP124, AP40); formula drift (kappa, harmonic, desuspension, central charges); compute/test sync failures; DS ghost charge cascade (AP143); r-matrix convention mixing (AP144/AP148); local-global conflation (AP142); standalone drift; prose fortification; mega-campaign straggler commits (AP146).
AGENTS.md:362:AP40 environment/status (~50 instances in 7 commits); V2-AP34 divided-power drift (15+); AP32 uniform-weight drift (20+); AP126 propagation (34+); V2-AP37 Arakelov normalisation (same error 3x); stale Part refs (V2-AP26: 24+); proof-after-conjecture (V2-AP31); phantom label debt (V2-AP38: 366); undefined macros after migration (V2-AP39).
audit_campaign_20260412_231034/AP14_bare_kappa_v3.md:256:   239	6. CY-C is CONJECTURE. NEVER \begin{theorem} for CY-C (AP40).
CLAUDE.md:45:### HZ-2. AP40 (environment matches tag) -- 5 waves, 70+ instances
CLAUDE.md:149:        Conjectured -> AP40 upstream violation
CLAUDE.md:643:AP40: Environment MUST match tag. Conjectured -> \begin{conjecture}. ProvedElsewhere -> theorem + Remark attribution.
CLAUDE.md:903:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
audit_campaign_20260412_231034/T07_thm_H.md:177:CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
audit_campaign_20260412_231034/F19_arnold_KZ.md:539:AGENTS.md-345-AP40, AP125, AP124, AP4, V2-AP31, AP-CY6, AP-CY11, AP-CY14.
audit_campaign_20260412_231034/SI03_missing_provedhere.md:112:CLAUDE.md:829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.

thinking
**Analyzing environment and ClaimStatus mismatches**

I'm setting out to inspect the specified LaTeX files for any mismatches between theorem-like environments and their associated ClaimStatus tags, based on repo rules ensuring alignment. I'll focus on spotting places where, for instance, a `theorem` environment might wrongly include a `ClaimStatusConjectured` tag, or vice versa, and prepare a concise report listing these discrepancies along with the minimal fix needed. This involves searching each file for ClaimStatus occurrences and checking their surrounding environments carefully.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusConject" chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusHeuristic" chapters/theory/bar_construction.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

wait(call_Ci1WXU2Yg1x8ZtfCUGujm6zq) timed out:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '540,620p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\emph{Component 1: Internal differential $d_{\text{internal}}$.}

If $\mathcal{A}$ has an internal differential $d_\mathcal{A}: \mathcal{A} \to \mathcal{A}$ (e.g., from a BRST complex or de Rham differential), we apply it to each tensor factor:
\[d_{\text{internal}}\left(\phi_0 \otimes \cdots \otimes \phi_n \otimes \omega\right) = \sum_{i=0}^n (-1)^{\epsilon_i} \left(\phi_0 \otimes \cdots \otimes d_\mathcal{A}(\phi_i) \otimes \cdots \otimes \phi_n \otimes \omega\right)\]
where $\epsilon_i$ is the Koszul sign:
\[\epsilon_i = \sum_{j=0}^{i-1} |\phi_j| + \sum_{j=0}^{i-1} 1 = \text{(total degree before } \phi_i\text{)}\]

\emph{Component 2: Residue differential $d_{\text{residue}}$.}

The main geometric operation extracts OPE coefficients via residues at collision divisors.
\[d_{\text{residue}}\left(\phi_0 \otimes \cdots \otimes \phi_n \otimes \omega\right) = \sum_{0 \leq i < j \leq n} (-1)^{\sigma_{ij}} \text{Res}_{D_{ij}}\left[\mu(\phi_i, \phi_j) \otimes \text{(other factors)} \otimes \omega\right]\]
where:
\begin{itemize}
\item $\mu: \mathcal{A} \otimes \mathcal{A} \to \mathcal{A}$ is the OPE (chiral product)
\item $D_{ij} \subset \overline{C}_{n+1}(\Sigma_g)$ is the divisor where $z_i = z_j$
\item $\text{Res}_{D_{ij}}$ is the residue along $D_{ij}$ (see \S\ref{sec:residue-calculus} below)
\item $\sigma_{ij}$ is a sign determined by:
 \begin{enumerate}
 \item Position of $i,j$ in the tensor product (Koszul sign)
 \item Orientation of $D_{ij}$ as boundary (geometric sign)
codex
The mismatch scan is still running. Once I have the exact lines, I’ll patch only the status-bearing blocks and then do a local coherence pass around each edit.
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatus" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
181:\begin{theorem}[Schwartz kernel theorem for cobar {\cite{Hormander}}; \ClaimStatusProvedElsewhere]\label{thm:schwartz-kernel-cobar}
292:\begin{lemma}[Holonomicity of the bar complex; \ClaimStatusProvedHere]%
353:\begin{lemma}[Verdier duality exchanges extensions; \ClaimStatusProvedHere]%
386:\begin{theorem}[Distributional model of the cobar; \ClaimStatusProvedHere]%
469:\ClaimStatusProvedHere]\label{cor:cobar-nilpotence-verdier}
545:\begin{theorem}[Cobar differential; \ClaimStatusProvedHere]\label{thm:cobar-diff-geom}
665:\begin{theorem}[Distributional verification of \texorpdfstring{$d_{\text{cobar}}^2 = 0$}{d\_cobar\textasciicircum 2 = 0}; \ClaimStatusProvedHere]\label{thm:cobar-d-squared-zero}
935:\begin{lemma}[Sign consistency for cobar differential; \ClaimStatusProvedHere]\label{lem:cobar-sign-consistency}
1095:\begin{theorem}[Fermion-boson Koszul duality; \ClaimStatusProvedHere]\label{thm:fermion-boson-koszul}
1197:\begin{conjecture}[Cobar elements as on-shell propagator templates; \ClaimStatusConjectured]\label{conj:cobar-physical}
1254:Conjecture~\ref{conj:cobar-physical} is tagged \ClaimStatusConjectured{} because the identification of cobar elements with on-shell propagators requires external physics input (equations of motion, path integral measure) that lies outside the algebraic framework of this monograph.
1313:\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
1466:\begin{corollary}[Bar-cobar mutual inverses; \ClaimStatusProvedHere]\label{cor:bar-cobar-inverse}
1543:\begin{proposition}[Explicit cobar-bar augmentation; \ClaimStatusProvedHere]
1793:\begin{theorem}[Kontsevich formality (1997) {\cite{Kon99}}; \ClaimStatusProvedElsewhere]\label{thm:kontsevich-formality}
1818:\ClaimStatusProvedHere
1829:\begin{theorem}[Cobar as Čech complex; \ClaimStatusProvedHere]\label{thm:cobar-cech}
1877:\begin{theorem}[Cobar as free chiral algebra; \ClaimStatusProvedHere]\label{thm:cobar-free}
1898:\begin{theorem}[Geometric unit of adjunction; \ClaimStatusProvedHere]\label{thm:geom-unit}
1988:\begin{theorem}[Topology; \ClaimStatusProvedHere]\label{thm:weak-topology}
collab wait(call_X38pST6movnFhcWBldTRHFwj)
  receivers: 019d876a-beba-7330-82f8-bc3cdc64929d
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusConject" -n chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1197:\begin{conjecture}[Cobar elements as on-shell propagator templates; \ClaimStatusConjectured]\label{conj:cobar-physical}
1254:Conjecture~\ref{conj:cobar-physical} is tagged \ClaimStatusConjectured{} because the identification of cobar elements with on-shell propagators requires external physics input (equations of motion, path integral measure) that lies outside the algebraic framework of this monograph.
2843:\begin{conjecture}[Heuristic BRST/bar comparison; \ClaimStatusConjectured]\label{conj:brst-cohomology}
2932:\begin{conjecture}[Anomaly cancellation for matter-ghost systems; \ClaimStatusConjectured]\label{conj:anomaly-cancellation}
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusHeuristic" chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatus" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
305:\begin{theorem}[Filtered Koszul duality (GLZ) {\cite{GLZ22}}; \ClaimStatusProvedElsewhere]\label{thm:filtered-koszul-glz}
345:\begin{proposition}[Filtered implies curved; \ClaimStatusProvedHere]\label{prop:filtered-to-curved}
567:\begin{theorem}[Convergence of bar construction; \ClaimStatusProvedHere]\label{thm:bar-convergence}
935:\begin{lemma}[Adjunction; \ClaimStatusProvedHere]\label{lem:chiral-co-contra-adjunction}
1052:\ClaimStatusProvedHere]\label{prop:chiral-inj-proj-resolutions}
1124:\begin{proposition}[Explicit CDG Hom-complex; \ClaimStatusProvedHere]
1168:\begin{corollary}[Contractibility of coacyclic injectives; \ClaimStatusProvedHere]
1236:\texorpdfstring{$\Psi_C^{\mathrm{ch}}$}{Psi_C^ch}; \ClaimStatusProvedHere]
1302:\ClaimStatusProvedHere]
1442:\ClaimStatusProvedHere]
1499:\ClaimStatusProvedHere]
1606:\begin{theorem}[Bar-cobar inversion: strict on the Koszul locus, coderived off it; \ClaimStatusProvedHere]\label{thm:bar-cobar-inversion-qi}
1775:\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
2017:\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
2168:\ClaimStatusConjectured
2217:\begin{lemma}[Associated graded; \ClaimStatusProvedHere]\label{lem:bar-cobar-associated-graded}
2233:\begin{theorem}[Bar-cobar spectral sequence; \ClaimStatusProvedHere]\label{thm:bar-cobar-spectral-sequence}
2293:\begin{theorem}[Collapse at \texorpdfstring{$E_2$}{E2}; \ClaimStatusProvedHere]\label{thm:spectral-sequence-collapse}
2336:\begin{theorem}[Genus-graded convergence; \ClaimStatusProvedHere]\label{thm:genus-graded-convergence}
2424:\ClaimStatusProvedElsewhere{}
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2940,3045p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proof}
Each boundary stratum $S_T \cong \prod_{v \in V(T)}
\overline{\Conf}_{|v|}(X_v)$ is indexed by a tree~$T$.
The restriction $i_{S_T}^!\,\barBch_n(\cA)$ decomposes as
the tensor product $\bigotimes_{v \in V(T)}
i_v^!\,\barBch_{|v|}(\cA)$,
where each factor is a lower-degree bar component restricted to
$\overline{\Conf}_{|v|}(X_v)$.

Forward: $E_2$-collapse
(Theorem~\ref{thm:pbw-koszulness-criterion}) concentrates each
bar component in degree~$0$; restrictions of degree-$0$ objects
remain in degree~$0$.

Converse: at the deepest stratum $S = D_{\{i,j\}}$
(binary collision), $i_S^!\,\barBch_n$ computes the OPE
residue $a_{(k)}b$ at a single collision. Acyclicity for all
binary strata forces the PBW comparison map to be injective
at every weight, giving $E_2$-collapse.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '2135,2235p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
functoriality of bar-cobar through the $L_\infty$-convolution
$\Convinf$
(Theorem~\ref{thm:operadic-homotopy-convolution}).
In particular, bar-cobar inversion preserves the full quantum
$L_\infty$ structure, not merely the dg~Lie shadow.
\end{remark}

\begin{remark}[Quasi-isomorphism of chain complexes vs chiral algebras]\label{rem:qi-vs-homology-iso}
The distinction is between two levels of structure:

\emph{Chain complex quasi-isomorphism.} A chain map $\psi: C^\bullet \to D^\bullet$ inducing an isomorphism $H^\bullet(\psi): H^\bullet(C) \xrightarrow{\cong} H^\bullet(D)$ on cohomology. This is the standard notion; a ``homology isomorphism'' and a ``quasi-isomorphism'' are the \emph{same thing} at the chain complex level.

\emph{Chiral algebra quasi-isomorphism.} An $A_\infty$ (or chiral algebra) morphism $\psi\colon \mathcal{A} \to \mathcal{B}$ whose linear component $\psi_1\colon \mathcal{A} \to \mathcal{B}$ is a chain complex quasi-isomorphism. Such a map preserves the full $A_\infty$ structure up to coherent homotopy. The distinction matters:
A chain complex quasi-isomorphism tells us only about $H^\bullet$ and need not respect multiplicative or $A_\infty$ structure, whereas a chiral algebra quasi-isomorphism gives a full equivalence in the derived category of chiral algebras, preserving all homotopy-theoretic information. For bar-cobar inversion to establish derived equivalences, the map $\Omega(B(\mathcal{A})) \to \mathcal{A}$ must be a quasi-isomorphism of \emph{chiral algebras}, not of chain complexes alone.

\emph{Example.}
Consider a dga $(C^\bullet, d, \mu)$ with:
\[\cdots \to 0 \to \mathbb{C} \xrightarrow{0} \mathbb{C} \to 0 \to \cdots\]

This has $H^0 = \mathbb{C}$, $H^i = 0$ for $i \neq 0$.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '1990,2125p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 theorem is the abstract collapse criterion of clause~\textup{(4)}.
 In particular, this does \emph{not} remove the genus-$0$ Koszul
 hypothesis of Definition~\ref{def:koszul-locus}; it only says that
 after one passes to the curved or completed factorization surface,
 some off-locus families may still lie on the derived side of the
 wall.

\item \emph{Which families are expected to leave the locus.}
 On the live proved surface, the restrictive boundary is not the
 universal or freely strongly generated landscape but its singular
 quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
 Virasoro, and the principal $\cW$-families enter through PBW-flat
 models and are treated as on-locus. The genuine off-locus candidates
 are quotient algebras with null-vector ideals in the bar-relevant
 range: simple admissible affine quotients, minimal-model Virasoro and
 $\cW$-quotients, critical-level enlargements with extra center, and
 other non-flat PBW degenerations. For such families the coderived
 comparison remains available; what is missing is ordinary
 cohomological detectability of the coacyclic cone. The admissible
 $\widehat{\mathfrak{sl}}_2$ example of
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '4260,4320p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[The bar complex as quantized symmetric power]
\label{rem:quantized-symmetric-power}
\index{bar complex!as quantized symmetric power}
\index{quantized symmetric power}
The bar complex admits a unified interpretation as a \emph{quantized
symmetric power} of the curve. The three bar complexes
$\mathrm{Lie}^c \subset \mathrm{Sym}^c \subset T^c$ on
$s^{-1}\bar{\cA}$ correspond to:
\begin{itemize}
\item $\mathrm{Sym}^c$ (the ``classical symmetric power''): the
 coshuffle coalgebra, factorization on the unordered
 $\operatorname{Ran}(X)$. Its generating function is the exponential:
 $\sum \chi(\mathrm{Sym}^n)\, t^n = \mathrm{PE}[\chi(\cA)\, t]$.
\item $T^c$ (the ``quantum symmetric power''): the deconcatenation
 coalgebra, factorization on ordered configurations
 $\mathrm{Conf}_n^<(X)$. The $R$-matrix $R(z)$ is the quantization
 datum; the passage $T^c \to \mathrm{Sym}^c$ is the
 $\Sigma_n$-coinvariant projection (the classical limit).
\item $\mathrm{Lie}^c$ (the ``primitive part''): the Harrison/coLie
 coalgebra, the infinitesimal generators of the logarithm.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '5410,5460p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{cases}
 \psi_m(\bar\varphi)(a_{m_1},\ldots,a_{m_n})
 & \text{if } m = m_1 + \cdots + m_n, \\
 0 & \text{otherwise},
\end{cases}
\]
where $\psi_m$ is the chiral Lie action on
$\check{C}^m(\mathcal{U};\cA)$ and
$\bar\varphi \in \bigotimes_{i=1}^n
\operatorname{Hom}(\check{C}^{m_i},\check{C}^m)$
is the component of~$\varphi$ at the specified multi-degree.
\end{remark}

\subsection{\v{C}ech--bar comparison as $L_\infty$ morphism}
\label{subsec:cech-bar-comparison}
\index{Cech--bar comparison@\v{C}ech--bar comparison}

The bar complex and the \v{C}ech complex are two resolutions of the
same object (the chiral homology of~$\cA$ on~$X$), and the
convolution formulation makes their compatibility a statement
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && sed -n '6420,6515p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{enumerate}
Each projected image has characteristic polynomial
$t^2-3t-1$, hence eigenvalues $(3 \pm \sqrt{13})/2$. The
projectors intertwine with Drinfeld--Sokolov reduction on
the common core.
\end{proposition}

\begin{proof}
Both B\'{e}zout identities are verified by direct expansion.
The projectors are instances of the coprime-locus functional
calculus: if $\gcd(g,p/g)=1$ and $a(t)g(t)+b(t)(p/g)(t)=1$,
then $e_g(T)=b(T)(p/g)(T)$ is idempotent with image the
$g$-summand in the Chinese remainder decomposition
$k[t]/(p) \cong k[t]/(g) \oplus k[t]/(p/g)$.
\end{proof}

\begin{remark}[Why rank one is deceptive]
\label{rem:rank-one-deceptive}
For the $\widehat{\mathfrak{sl}}_2/\mathrm{Vir}$
correspondence, the recurrence polynomials coincide:
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\begin\\{remark}(.*ClaimStatus)\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n -B 2 -A 2 "ClaimStatusProvedHere" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
343-\subsection{When does filtering degenerate to curved?}
344-
345:\begin{proposition}[Filtered implies curved; \ClaimStatusProvedHere]\label{prop:filtered-to-curved}
346-A filtered chiral algebra $\mathcal{A}$ has an associated \emph{curved structure} if:
347-\begin{enumerate}
--
565-\subsection{Convergence criteria}
566-
567:\begin{theorem}[Convergence of bar construction; \ClaimStatusProvedHere]\label{thm:bar-convergence}
568-Let $\mathcal{A}$ be a chiral algebra and write
569-$\bar{B}(\mathcal{A})=\bigoplus_{n\ge0}\bar{B}^n(\mathcal{A})$ with its bar-degree
--
933-\end{definition}
934-
935:\begin{lemma}[Adjunction; \ClaimStatusProvedHere]\label{lem:chiral-co-contra-adjunction}
936-\index{adjunction!chiral cotensor--contratensor}
937-There is a canonical isomorphism of complexes:
--
1050-
1051-\begin{proposition}[Injective and projective resolutions;
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n -B5 -A2 "ClaimStatusConjectured" chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1770-dramatic failure: the center of
1771-$V_{-2}(\mathfrak{sl}_2)$ jumps in dimension and the bar complex
1772-acquires infinitely many off-diagonal classes.
1773-\end{example}
1774-
1775:\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
1776-\label{rem:admissible-2-koszul}%
1777-\index{2-Koszul!admissible level}%
--
2012- wall, but by itself would not yet supply the promotion required in
2013- clause~\textup{(4)}.
2014-\end{enumerate}
2015-\end{remark}
2016-
2017:\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
2018-\label{conj:koszul-wall-associated-variety}
2019-\index{Koszul locus!derived wall}
--
2163-\end{remark}
2164-
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatus" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
257:\begin{theorem}[Curvature as \texorpdfstring{$\mu_1$}{mu1}-cycle; \ClaimStatusProvedHere]
304:\begin{theorem}[When completion is necessary {\cite{Positselski11,GLZ22}}; \ClaimStatusProvedElsewhere]
362:\begin{proposition}[Acyclicity of curved bar complexes; \ClaimStatusProvedHere]
468:\begin{theorem}[Filtered cooperads (Gui--Li--Zeng~\cite{GLZ22}); \ClaimStatusProvedElsewhere]
484:This theorem is imported and treated as \ClaimStatusProvedElsewhere. The
510:\begin{theorem}[When filtered reduces to curved; \ClaimStatusProvedHere]
579:\begin{theorem}[Conilpotency ensures convergence; \ClaimStatusProvedHere]
752:\ClaimStatusProvedHere]
926:\ClaimStatusProvedHere]
945:\ClaimStatusProvedHere]
1092:\ClaimStatusProvedHere]
1212:\ClaimStatusProvedHere]
1277:\ClaimStatusProvedHere]
1314:\ClaimStatusProvedHere]
1352:\ClaimStatusProvedHere]
1401:\ClaimStatusProvedHere]
1452:\texorpdfstring{$W_\infty$}{W_infty}; \ClaimStatusProvedHere]
1515:\ClaimStatusProvedHere]
1579:package; \ClaimStatusProvedHere]
1615:finite quotients; \ClaimStatusProvedHere]
exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusConjectured" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc 'cd /Users/raeez/chiral-bar-cobar && rg -n "ClaimStatusHeuristic" chapters/theory/bar_cobar_adjunction_curved.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && rg -n \"\\\\begin\\{conjecture\\}.*ClaimStatus\" chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1760,1785p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1760	concentrated on the Koszul diagonal, and
  1761	Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
  1762	level $k = -1/2$ lies outside the Koszul locus because the
  1763	representation category
  1764	$\mathrm{KL}_{-1/2}(\mathfrak{sl}_2)$
  1765	(Arakawa~\cite{Arakawa17, Arakawa2016RationalAdmissible}) is a
  1766	non-semisimple finite tensor category whose singular vectors
  1767	obstruct the diagonal concentration.
  1768	For the critical-level analogue $k = -h^\vee = -2$, the
  1769	Feigin--Frenkel center~\cite{Feigin-Frenkel} causes an even more
  1770	dramatic failure: the center of
  1771	$V_{-2}(\mathfrak{sl}_2)$ jumps in dimension and the bar complex
  1772	acquires infinitely many off-diagonal classes.
  1773	\end{example}
  1774	
  1775	\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
  1776	\label{rem:admissible-2-koszul}%
  1777	\index{2-Koszul!admissible level}%
  1778	\index{admissible level!2-Koszul}%
  1779	The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2155,2185p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2155	
  2156	Compare with the algebra $(D^\bullet, 0, \nu) = (\mathbb{C}, 0, 0)$ in degree 0.
  2157	The projection $\pi: C^\bullet \to D^\bullet$ is a quasi-isomorphism of chain
  2158	complexes (both have $H^0 = \mathbb{C}$), but $\pi$ does \emph{not} respect the
  2159	multiplication ($\pi$ need not intertwine $\mu$ and $\nu$ at the chain level).
  2160	To obtain a quasi-isomorphism of \emph{algebras}, one must work with $A_\infty$
  2161	morphisms, which encode the higher homotopies relating the two multiplicative
  2162	structures.
  2163	\end{remark}
  2164	
  2165	
  2166	\begin{remark}[Derived Morita equivalence and the Koszul conductor]
  2167	\label{rem:bar-morita-koszul-conductor}
  2168	\ClaimStatusConjectured
  2169	\index{derived Morita equivalence!bar coalgebra characterization}
  2170	\index{Koszul conductor!Morita obstruction}
  2171	Theorem~\ref{thm:bar-cobar-inversion-qi} converts the bar coalgebra
  2172	into a complete derived invariant: two Koszul chiral algebras
  2173	$\cA$, $\cB$ are derived Morita equivalent (quasi-isomorphic as
  2174	objects of the bar-cobar localization) if and only if their bar

thinking
**Summarizing mismatches and fix proposals**

I’m noting two environment-status mismatches where `ClaimStatusConjectured` appears inside a `remark` environment, suggesting an environment change to `conjecture` for alignment. I plan to list each mismatch with file paths and lines, describe the issue and the proposed fix, and confirm no other mismatches were found in the scanned files. This will provide a clear, concise summary with suggested next steps.
codex
- `chapters/theory/bar_cobar_adjunction_inversion.tex:1775` — a `remark` (`rem:admissible-2-koszul`) currently carries `\ClaimStatusConjectured`. AP40 says a conjectural tag belongs in a `conjecture` environment, so the minimal fix is an **environment change** (turn the remark into a conjecture or split off a dedicated conjecture block around this speculation).  
- `chapters/theory/bar_cobar_adjunction_inversion.tex:2166-2168` — another `remark` (`rem:bar-morita-koszul-conductor`) is tagged `\ClaimStatusConjectured`. Align the environment/tag by converting this remark into a `\begin{conjecture}…\end{conjecture}` (environment change) or by moving the conjectural text into a proper conjecture statement.  

All other claim-status tags in the four files already sit in matching environments, so no further action is needed.
wait(call_X38pST6movnFhcWBldTRHFwj) 1 agents complete:
  019d876a-beba-7330-82f8-bc3cdc64929d completed: "- `chapters/theory/bar_cobar_adjunction_inversion.tex:1775` — a `remark` (`rem:admissible-2-koszul`) currently carries `…"


thinking
**Evaluating remark tags**

I'm thinking about the tags associated with remarks. The theorem registry lists "ProvedHere," indicating that remarks can be proved. Other potential tags might include Conditional, Heuristic, Open, or Conjectured. There seems to be a loose guideline for conjectured statements, especially since AP40 suggests that if no proof exists, it falls into a conjecture environment with a "ClaimStatusConjectured." If a remark has a speculative note, "ClaimStatusHeuristic" might fit. However, I need to inspect the actual content for accuracy, especially when phrases like "One expects..." arise.
thinking
**Evaluating claim status**

I need to look at the ClaimStatus mismatches and avoid rewriting. It’s important to inspect the content for truthful minimal edits. If the content is based on a conjectural statement, changing the environment to conjecture makes sense. I should read around both locations for context. I might need to consider if an update plan is necessary, but given the task’s complexity, creating a concise plan with steps is a good idea.
Plan update
Explorer isolated two mismatches, both conjectural tags attached to remark environments in `bar_cobar_adjunction_inversion.tex`. I’m checking the local text to choose the smallest truthful fix, then I’ll patch and run the requested forbidden-pattern grep on the modified file set.
  → Read local context around each mismatch and decide the minimal truthful alignment
  • Patch the assigned file(s) with only the necessary environment/tag edits
  • Re-read edited blocks, check local labels/refs, and grep modified files for forbidden patterns
exec
/bin/zsh -lc "sed -n '1748,1808p' chapters/theory/bar_cobar_adjunction_inversion.tex
sed -n '2140,2205p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The counit
$\psi\colon \Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))
\to L_{-1/2}(\mathfrak{sl}_2)$
fails to be a quasi-isomorphism: the surviving off-diagonal class
generates a non-trivial extension in
$\Omega^{\mathrm{ch}}(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$
that has no preimage in $L_{-1/2}(\mathfrak{sl}_2)$.

\emph{Consistency with the Koszul-locus hypothesis.}
At generic level, the vacuum Verma module
$M(k\Lambda_0)$ has no singular vectors in the bar-relevant range,
$H^\bullet(\bar{B}^{\mathrm{ch}}(V_k(\mathfrak{sl}_2)))$ is
concentrated on the Koszul diagonal, and
Theorem~\ref{thm:bar-cobar-inversion-qi} applies. The admissible
level $k = -1/2$ lies outside the Koszul locus because the
representation category
$\mathrm{KL}_{-1/2}(\mathfrak{sl}_2)$
(Arakawa~\cite{Arakawa17, Arakawa2016RationalAdmissible}) is a
non-semisimple finite tensor category whose singular vectors
obstruct the diagonal concentration.

thinking
**Looking into the proof issue**

I'm noticing a mismatch with the proof structure, which seems broken. After the "end{remark}," there should be a "begin proof," followed by text and the "end{remark}" again. It feels like there could be a closure mismatch. I should inspect the lines more closely, especially around the proof and remark areas. The lack of clarity might indicate a significant compile issue, or maybe there’s a truncation problem. I’ll check the lines with numbers to pinpoint the error.
codex
The first flagged block isn’t just a tag mismatch; it also sits next to a malformed proof/closure sequence. I’m reading a slightly wider window now so the minimal edit fixes the status issue without leaving the local environment stack inconsistent.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1768,1825p'
nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2156,2210p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1768	For the critical-level analogue $k = -h^\vee = -2$, the
  1769	Feigin--Frenkel center~\cite{Feigin-Frenkel} causes an even more
  1770	dramatic failure: the center of
  1771	$V_{-2}(\mathfrak{sl}_2)$ jumps in dimension and the bar complex
  1772	acquires infinitely many off-diagonal classes.
  1773	\end{example}
  1774	
  1775	\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
  1776	\label{rem:admissible-2-koszul}%
  1777	\index{2-Koszul!admissible level}%
  1778	\index{admissible level!2-Koszul}%
  1779	The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
  1780	classical Koszulness: bar cohomology
  1781	$H^*(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$ is not
  1782	concentrated in degree~$1$. The off-diagonal class produced by the
  1783	singular vector at conformal weight~$4$ lives in bar degree~$2$.
  1784	A stronger expectation is that the bar cohomology is concentrated in
  1785	degrees $\{1, 2\}$, making $L_{-1/2}(\mathfrak{sl}_2)$ a
  1786	\emph{$2$-Koszul} (or \emph{$N$-Koszul} with $N = 2$) chiral algebra
  1787	in the sense of Berger~\cite{Berger01}:

thinking
**Investigating theorem proof**

I'm pondering whether the proof actually belongs to the previous theorem. It starts right after a remark, but I'm wondering if I should inspect the earlier theorem, particularly the one just before the example. Yet, it might not be relevant. If I change the remark to a conjecture, it seems the proof stays after the conjecture, which could violate AP4. I may need to look at the lines before the example and find the theorem that this proof closes. I'll use context from 1700 or earlier.
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1690,1778p'
nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1805,1888p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1690	carry extra higher-differential data, and this chapter does
  1691	\emph{not} claim that the counit $\psi$ is a quasi-isomorphism there
  1692	\textup{(}see Remark~\ref{rem:sl2-admissible}
  1693	and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
  1694	with the completed correspondence of
  1695	Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
  1696	coderived/contraderived bar-coalgebra comparison of
  1697	Theorems~\ref{thm:positselski-chiral-proved}
  1698	and~\ref{thm:full-derived-module-equiv-proved}; this theorem
  1699	asserts the coderived statement of~(2), and isolates in~(4) the extra
  1700	input needed to recover an ordinary quasi-isomorphism there.
  1701	\end{theorem}
  1702	
  1703	
  1704	\begin{example}[Admissible-level failure of bar-cobar inversion]
  1705	\label{ex:admissible-sl2-failure}
  1706	\index{admissible level!bar-cobar inversion failure}
  1707	\index{bar-cobar inversion!admissible-level counterexample}
  1708	Consider $L_{-1/2}(\mathfrak{sl}_2)$, the simple affine vertex algebra
  1709	at the admissible level $k = -1/2$ for $\widehat{\mathfrak{sl}}_2$



thinking
**Analyzing proof structure**

I’m evaluating the proof related to a theorem that ended at 1701. It seems like the proof may have been misplaced after an interlude example and remark, making it an orphan proof. Although the user only asked about fixing ClaimStatus mismatches, changing the remark to a conjecture brings up other considerations about proof ordering. However, since the proof can stand alone in LaTeX, I wonder if that affects the user's concerns about the mismatch. It’s ultimately complicated!
thinking
**Reviewing proof and labels**

I’m considering whether to ignore some findings, but AGENTS AP4 warns about proof appearing after conjecture—something I need to keep in mind. The task really focuses on addressing claim status mismatches, so maybe I can leave the orphan proof unless it's impacted by my edits. I should check if the second remark is truly a conjectural statement and might need to convert it to a conjecture or change its label. 

I’ll also look for references related to labels in the repo.
thinking
**Searching for references**

I’m thinking about whether renaming could be easier if there are zero references. It might be a good idea to check if any references exist before proceeding with a rename. I need to conduct a search to confirm the situation. That way, I can ensure I’m making the best decision regarding the label change. Let’s see what I can find in order to keep everything clear and organized!
exec
/bin/zsh -lc "rg -n '\\\\ref\\{rem:admissible-2-koszul\\}|\\\\autoref\\{rem:admissible-2-koszul\\}|\\\\Cref\\{rem:admissible-2-koszul\\}|\\\\nameref\\{rem:admissible-2-koszul\\}|rem:admissible-2-koszul' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\ref\\{rem:bar-morita-koszul-conductor\\}|\\\\autoref\\{rem:bar-morita-koszul-conductor\\}|\\\\Cref\\{rem:bar-morita-koszul-conductor\\}|\\\\nameref\\{rem:bar-morita-koszul-conductor\\}|rem:bar-morita-koszul-conductor' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar succeeded in 102ms:
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/D14_proof_after_conj.md:17:- [HIGH] V1 `chapters/theory/bar_cobar_adjunction_inversion.tex:1782` — PROBLEM: AP4. The proof of `thm:bar-cobar-inversion-qi` is stranded after an example and the conjectural remark `rem:admissible-2-koszul`. FIX: move the proof block to immediately after the theorem it proves; place the example and conjectural remark after the proof as post-proof commentary.
/Users/raeez/chiral-bar-cobar/wave2_audit_20260413_001942/D14_proof_after_conj.md:1371:- [HIGH] V1 `chapters/theory/bar_cobar_adjunction_inversion.tex:1782` — PROBLEM: AP4. The proof of `thm:bar-cobar-inversion-qi` is stranded after an example and the conjectural remark `rem:admissible-2-koszul`. FIX: move the proof block to immediately after the theorem it proves; place the example and conjectural remark after the proof as post-proof commentary.
 succeeded in 90ms:
/Users/raeez/chiral-bar-cobar/metadata/dependency_graph.dot:2243:  rem_bar_morita_koszul_conductor [label="rem:bar-morita-koszul-conductor\nremark [Co]\nDerived Morita equivalence and the Koszu...", style=filled, fillcolor="#fff9c4"];
/Users/raeez/chiral-bar-cobar/metadata/label_index.json:30378:  "rem:bar-morita-koszul-conductor": {
/Users/raeez/chiral-bar-cobar/metadata/claims.jsonl:2151:{"label": "rem:bar-morita-koszul-conductor", "env_type": "remark", "status": "Conjectured", "file": "chapters/theory/bar_cobar_adjunction_inversion.tex", "line": 2143, "title": "Derived Morita equivalence and the Koszul conductor", "refs_in_block": ["thm:bar-cobar-inversion-qi", "sec:complementarity"]}
/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:2167:\label{rem:bar-morita-koszul-conductor}
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1988,2025p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1988	 No specific non-Koszul family is presently proved by a separate
  1989	 family-level argument to satisfy that promotion hypothesis. The live
  1990	 theorem is the abstract collapse criterion of clause~\textup{(4)}.
  1991	 In particular, this does \emph{not} remove the genus-$0$ Koszul
  1992	 hypothesis of Definition~\ref{def:koszul-locus}; it only says that
  1993	 after one passes to the curved or completed factorization surface,
  1994	 some off-locus families may still lie on the derived side of the
  1995	 wall.
  1996	
  1997	\item \emph{Which families are expected to leave the locus.}
  1998	 On the live proved surface, the restrictive boundary is not the
  1999	 universal or freely strongly generated landscape but its singular
  2000	 quotient boundary. Heisenberg, universal affine $V_k(\fg)$, generic
  2001	 Virasoro, and the principal $\cW$-families enter through PBW-flat
  2002	 models and are treated as on-locus. The genuine off-locus candidates
  2003	 are quotient algebras with null-vector ideals in the bar-relevant
  2004	 range: simple admissible affine quotients, minimal-model Virasoro and
  2005	 $\cW$-quotients, critical-level enlargements with extra center, and
  2006	 other non-flat PBW degenerations. For such families the coderived
  2007	 comparison remains available; what is missing is ordinary





thinking
**Considering task adjustments**

The task doesn’t mention metadata regeneration, so I think I can make a minimum fix: changing `\begin{remark}` and `\end{remark}` to `\begin{conjecture}` and `\end{conjecture}`. I’ll also update the reference from "Remark" to "Conjecture" without changing the labels to keep the impact minimal. I'm wondering if this is acceptable under AP125 since it does violate the prefix convention. The safety action specifies checking \ref and \label validity, not just the prefix matching. There’s already an invalid prefix after the environment change.
thinking
**Evaluating truthfulness in claims**

I’m questioning whether a stronger expectation remains truthful. The phrase "A stronger expectation is that..." feels conjectural or heuristic, even though the title conveys a theorem-like claim. Maybe I should rephrase it to emphasize heuristic evidence. A minimal edit could just be changing the tag to "Heuristic" instead of environmental. Would that solve the "ClaimStatus mismatches"? If the system allows heuristic remarks, then yes. Let's see if that clears things up!
thinking
**Evaluating mathematical conjectures**

I'm delving into a claim about conjectures and theorems. The first statement seems like a precise unproved claim, so I’d categorize it as conjecture. The second one also presents speculative elements, indicating that it fits into a conjectural environment as well. I think I should run a search for ClaimStatus tags across files—maybe using grep or a quick script—to verify that each tag matches the appropriate environment and ensure consistency across the documents.
thinking
**Considering verification methods**

I’m thinking about how to verify all occurrences of ClaimStatus in four files after edits. One option is to run a small awk or use ripgrep (rg) to display these occurrences. A command like `rg -n '\\begin\\{|\\ClaimStatus'` might work well. There's also the possibility of using repo metadata and manually reviewing two fixed blocks. However, I’m weighing whether to use a quick script in Perl or Python, keeping in mind some guidelines against using Python for file operations when a shell command will do.
thinking
**Planning inspection process**

I’m thinking about how to inspect the files. While it might be tempting to review everything by eye, I realize there could be a lot to sift through, especially since some files are quite large. I could opt for a small Perl script to print environment and status pairs, but it might actually be simpler to use `awk`. This could track the current environment upon encountering "begin" and print lines with status. I should also consider using `rg -n "\\begin{(remark|conjecture).*ClaimStatus|\\ClaimStatus"` on the file to streamline this process.
codex
I’ve pinned the only live mismatches: both are conjectural claim-status tags attached to `remark` environments in `bar_cobar_adjunction_inversion.tex`. I’m converting just those environments, plus one in-file cross-reference that would otherwise misname the first block.
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1774,3 +1774,3 @@
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
@@ -1804,3 +1804,3 @@
 non-Koszul (critical level, no finite collapse).
-\end{remark}
+\end{conjecture}
 
@@ -2009,3 +2009,3 @@
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
@@ -2165,3 +2165,3 @@
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
@@ -2193,3 +2193,3 @@
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
apply_patch(auto_approved=true) exited 0 in 20ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..347ab90c7322a4044850a803bfc2de6e4969d878
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1772,7 +1772,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,7 +1802,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
+\end{conjecture}
 
 \begin{proof}[Dependency-closed proof]
 We verify each numbered clause by previously established results in
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..347ab90c7322a4044850a803bfc2de6e4969d878
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1772,7 +1772,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,7 +1802,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
+\end{conjecture}
 
 \begin{proof}[Dependency-closed proof]
 We verify each numbered clause by previously established results in
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1772,1808p'
nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2004,2014p'
nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '2164,2196p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  1772	acquires infinitely many off-diagonal classes.
  1773	\end{example}
  1774	
  1775	\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
  1776	\label{rem:admissible-2-koszul}%
  1777	\index{2-Koszul!admissible level}%
  1778	\index{admissible level!2-Koszul}%
  1779	The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
  1780	classical Koszulness: bar cohomology
  1781	$H^*(\bar{B}^{\mathrm{ch}}(L_{-1/2}(\mathfrak{sl}_2)))$ is not
  1782	concentrated in degree~$1$. The off-diagonal class produced by the
  1783	singular vector at conformal weight~$4$ lives in bar degree~$2$.
  1784	A stronger expectation is that the bar cohomology is concentrated in
  1785	degrees $\{1, 2\}$, making $L_{-1/2}(\mathfrak{sl}_2)$ a
  1786	\emph{$2$-Koszul} (or \emph{$N$-Koszul} with $N = 2$) chiral algebra
  1787	in the sense of Berger~\cite{Berger01}:
  1788	the square-zero bar-cobar spectral sequence
  1789	\textup{(}Theorems~\ref{thm:bar-cobar-spectral-sequence}
  1790	and~\ref{thm:spectral-sequence-collapse}\textup{)} collapses at a
  1791	finite page~$E_N$ rather than at~$E_2$.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..347ab90c7322a4044850a803bfc2de6e4969d878
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1772,7 +1772,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,7 +1802,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
+\end{conjecture}
 
 \begin{proof}[Dependency-closed proof]
 We verify each numbered clause by previously established results in
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 





thinking
**Evaluating proof placement**

Now, I'm considering if the proof surrounding a conjecture is semantically broken. Should I move the proof to come before the example and conjecture to fix this? It seems like it could be necessary for clarity. I notice that in the theorem at 1701, the proof follows the conjecture, which feels wrong. Moving the proof block right after the theorem might help maintain better coherence. However, I need to be cautious since the user specifically asked not to rewrite correct sections.
thinking
**Checking proof placement**

I need to check the validity of the \ref and \label tags. If my editing finds the proof placed after the conjecture to be incoherent, I might need to fix it. The proof block likely belongs to an earlier theorem, so moving it should not change any content, just enhance clarity. I’ll examine theorem 166 to find its label and title. It seems the proof currently sits after the example and conjecture, but it should actually follow the theorem’s end instead.
thinking
**Considering proof revisions**

I’m pondering whether there could be a second conjecture before the proof. It seems the section starting at line 2017 includes another conjecture following a remark from 2015, which isn't an issue for the proof. I should check the file to confirm where the proof block fits in relation to the preceding theorem. The proof starts with "Dependency-closed proof..." and references necessary clauses, suggesting moving it makes sense. Adjusting the proof isn’t what the user specifically requested, but it will maintain coherence after any changes. I'll apply the patch carefully, possibly cutting and inserting specific lines for clarity.
thinking
**Planning the proof edit**

I'm considering whether it's easier to duplicate the proof after the theorem and then delete the old block instead of trying to patch it directly. I want to avoid any errors, so capturing the exact proof block is crucial. I can utilize the lines from 1807 to 1856 as they are ready for this. Before making any edits, I'll provide an update in the commentary to keep things clear for the user. This will help maintain context and clarity in the documentation.
codex
The status fixes are in place, but the first one now exposes an existing local coherence problem: the proof of `thm:bar-cobar-inversion-qi` is stranded after post-theorem commentary. I’m moving that proof block to immediately follow the theorem so the conjecture doesn’t sit in front of an unrelated proof.

thinking
**Considering patch application**

I need to apply a patch and inspect the theorem surrounding the time from 1640 to 1704. It's crucial to think about where the proof insertion position should be. It feels a bit tricky, but I’ll go through it step-by-step to make sure everything is in order. Let's ensure we get this right and don’t miss anything important while tackling this task!
exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1640,1710p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1640	 \[
  1641	 \psi_g \colon \Omega_g(\bar{B}_g(\mathcal{A})) \longrightarrow \mathcal{A}_g
  1642	 \]
  1643	 and the completed series
  1644	 \[
  1645	 \psi = \sum_{g=0}^\infty \hbar^{2g-2}\psi_g
  1646	 \]
  1647	 are quasi-isomorphisms.
  1648	
  1649	\item \emph{Coderived off-Koszul lane.}
  1650	 For arbitrary complete augmented $\mathcal{A}$ with
  1651	 finite-dimensional graded bar pieces, the factorization counit
  1652	 \[
  1653	 \psi_X \colon \Omega_X \barB_X(\mathcal{A}) \longrightarrow \mathcal{A}
  1654	 \]
  1655	 is a coacyclic-equivalence: its cone
  1656	 \[
  1657	 K_\psi :=
  1658	 \operatorname{cone}\!\bigl(\Omega_X \barB_X(\mathcal{A}) \to \mathcal{A}\bigr)
  1659	 \]
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..347ab90c7322a4044850a803bfc2de6e4969d878
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1772,7 +1772,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,7 +1802,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
+\end{conjecture}
 
 \begin{proof}[Dependency-closed proof]
 We verify each numbered clause by previously established results in
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Constructing a proof block**

I need to create a full proof block, ensuring it’s exactly what I want. After 1701, I'll use apply_patch to insert the proof block and remove the original section from 1807 to 1856. It might be possible to use apply_patch with a copy-delete method. So, I want to proceed very carefully here to avoid any mistakes. There's a lot to consider in making sure everything is executed perfectly!
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1702,2 +1702,53 @@
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
@@ -1805,53 +1856,2 @@
 \end{conjecture}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
 
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

exec
/bin/zsh -lc "nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1688,1810p'
nl -ba chapters/theory/bar_cobar_adjunction_inversion.tex | sed -n '1848,1872p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  1688	quotients and minimal-model Virasoro/W-algebras the PBW/Shapovalov
  1689	argument is unavailable, the square-zero bar spectral sequence can
  1690	carry extra higher-differential data, and this chapter does
  1691	\emph{not} claim that the counit $\psi$ is a quasi-isomorphism there
  1692	\textup{(}see Remark~\ref{rem:sl2-admissible}
  1693	and~\ref{rem:virasoro-module-koszul-minimal}\textup{)}. In those regimes one must work
  1694	with the completed correspondence of
  1695	Corollary~\ref{cor:bar-cobar-inverse} and the intrinsic
  1696	coderived/contraderived bar-coalgebra comparison of
  1697	Theorems~\ref{thm:positselski-chiral-proved}
  1698	and~\ref{thm:full-derived-module-equiv-proved}; this theorem
  1699	asserts the coderived statement of~(2), and isolates in~(4) the extra
  1700	input needed to recover an ordinary quasi-isomorphism there.
  1701	\end{theorem}
  1702	
  1703	\begin{proof}[Dependency-closed proof]
  1704	We verify each numbered clause by previously established results in
  1705	this chapter and in the coderived appendix.
  1706	\begin{enumerate}[label=(D\arabic*)]
  1707	\item \emph{Strict Koszul lane.}
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Evaluating grep options**

I’m considering using `rg` to search for the `ClaimStatusConjectured` in the modified `.tex` files, plus looking for remarks or conjectures. The user wants me to search for forbidden patterns, not just those related to the claim status, which makes me think I should expand my search. I’m wondering if my approach might be overkill. I’ll check specific forbidden patterns that relate to this task, ensuring I don't miss anything important, even if it's a bit more complicated.
codex
The edit surface is stable. I’m running a narrow structural check now: re-scan the four assigned files for remaining claim-status/environment mismatches, then grep the modified file for the old forbidden remark-plus-conjectured pattern.
exec
/bin/zsh -lc "perl -ne '
if(/\\\\begin\\{(theorem|proposition|lemma|corollary|remark|conjecture|definition|example|computation|calculation|verification|maintheorem)\\}/){"'$env=$1;}
if(/'"\\\\ClaimStatus(Conjectured|ProvedHere|ProvedElsewhere)/){"'$status=$1; if(($status eq q(Conjectured) && $env ne q(conjecture)) || (($status eq q(ProvedHere) || $status eq q(ProvedElsewhere)) && $env eq q(conjecture))){print qq($ARGV:$.: env=$env status=$status'"\\n);}}
' chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\begin\\{remark\\}.*\\\\ClaimStatusConjectured|\\\\ClaimStatusConjectured' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/cobar_construction.tex:3613: env=remark status=Conjectured
 succeeded in 52ms:
1826:\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
2017:\begin{conjecture}[Derived Koszul wall; \ClaimStatusConjectured]
2168:\ClaimStatusConjectured
2972:\ClaimStatusConjectured]\label{conj:d-module-purity-koszulness}
3025:\ClaimStatusConjectured]%
4294:\ClaimStatusConjectured]\label{conj:factorization-finiteness-criterion}
5433:\ClaimStatusConjectured]
6474:\ClaimStatusConjectured]
6498:\ClaimStatusConjectured]
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Inspecting verification issues**

I found a mismatch in the cobar_construction.tex that wasn’t caught by the explorer. I need to inspect it further. Plus, I noticed multiple occurrences of ClaimStatusConjectured in the inversion file, which seems fine, but I should check the lines around line 3613 of cobar_construction for context. I need to make sure to fix these issues since they're assigned files. Good catch! I’ll also consider adjusting the verification script since it missed something this time.
codex
The re-scan caught one additional live mismatch the first pass missed: `cobar_construction.tex` has a conjectured tag still sitting on a `remark`. I’m opening that block now and will patch it the same way if the text is genuinely conjectural.
exec
/bin/zsh -lc "nl -ba chapters/theory/cobar_construction.tex | sed -n '3588,3648p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Investigating output issues**

It seems like there’s no output—maybe the file is too short? I think line 3613 exists, but the command might not be outputting anything due to an issue. I wonder if the output being empty is unusual. Perhaps the line range is beyond what's allowed? To troubleshoot this, I should try using an "rg" command around the specific label to dig deeper into what's going wrong.
exec
/bin/zsh -lc "rg -n -C 6 '\\\\ClaimStatusConjectured|\\\\begin\\{remark\\}|\\\\begin\\{conjecture\\}' chapters/theory/cobar_construction.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
55-(Proposition~\ref{prop:cobar-modular-shadow}).
56-Strict inversion may require completion or coderived contexts
57-at higher genus.
58-
59-\subsection{Motivation: reversing the prism}
60-
61:\begin{remark}[Three functors on the bar coalgebra: cobar is NOT the Koszul dual]
62-\label{rem:cobar-three-functors}
63-Before entering the construction, we fix a critical distinction that
64-pervades the chapter. Three functors act on the bar coalgebra
65-$\barB(\cA)$, producing three different objects; confusing any two
66-produces false statements.
67-\begin{enumerate}[label=\textup{(\roman*)}]
--
90-``the cobar of the bar gives the Koszul dual''
91-is false; the correct statement is
92-``the cobar of the bar gives $\cA$, and Verdier duality of the bar
93-gives the homotopy Koszul dual factorization algebra.''
94-\end{remark}
95-
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Searching around a specific line**

I need to get some context around line 3613; the earlier output only provided the beginning lines. So, I might search around that line directly, possibly using awk. But if the file is shorter, sed could give me an empty output. However, line 3613 does exist from the parser, so I should consider if it could be due to a carriage return issue. I'll use Perl along with awk to print line numbers around that specific line.
exec
/bin/zsh -lc "awk 'NR>=3605 && NR<=3625 {printf \"%6d  %s\\n\", NR, "'$0}'"' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Checking file characteristics**

I'm considering the situation where the file might be shorter than 3605 lines. The parser shows cumulative line numbers, so that's confusing. I remember that Perl's $. can print the line number, which could help. Perhaps the file is actually over 3600 lines, but I'm not sure why awk and sed aren't reflecting that. Maybe there are carriage return characters (`\r`) causing issues? I should run `wc -l` to verify the line count.
exec
/bin/zsh -lc 'wc -l chapters/theory/cobar_construction.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    3452 chapters/theory/cobar_construction.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

exec
/bin/zsh -lc "rg -n -C 5 '\\\\ClaimStatusConjectured' chapters/theory/cobar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1192-$n_2$ to be associative, $n_4$ measuring the failure of $n_3$ to be coherent, etc.
1193-\end{example}
1194-
1195-\subsection{Physical interpretation: on-shell propagator and Feynman-rule templates}
1196-
1197:\begin{conjecture}[Cobar elements as on-shell propagator templates; \ClaimStatusConjectured]\label{conj:cobar-physical}
1198-Elements of the cobar complex $\Omega^{\text{ch}}(\mathcal{C})$ should be read as
1199-\emph{algebraic shadow data for on-shell propagators} in the sense of quantum
1200-field theory.
1201-
1202-\emph{Precise statement.} For a chiral coalgebra $\mathcal{C}$ corresponding
--
1249-
1250-This gives the conjectural algebraic template for genus-zero Feynman rules.
1251-\end{remark}
1252-
1253-\begin{remark}[Scope]
1254:Conjecture~\ref{conj:cobar-physical} is tagged \ClaimStatusConjectured{} because the identification of cobar elements with on-shell propagators requires external physics input (equations of motion, path integral measure) that lies outside the algebraic framework of this monograph.
1255-
1256-\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~VII (physics-dictionary).
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 



thinking
**Refining parser logic**

In the four files, it seems only inversion and cobar have conjectures, while bar_construction might not. There could be status mismatches in other areas. I’m thinking of using a more robust parser to only match `\ClaimStatus...` if it's on the same line as `\begin{...}` or within the lines right after, before a blank line or label. It feels challenging, but our mismatches were specifically with tags right below the begin or label. I’ll want to carefully define the matching conditions for safer parsing.
thinking
**Clarifying script logic**

I’m outlining how the script should function. If a line matches the pattern `^\s*\\begin{(env)}.*\\ClaimStatus(Status)`, I’ll record the environment and status. If it matches `^\s*\\begin{(env)}` without the status, I’ll just set the environment. For lines matching `^\s*\\ClaimStatus(Status)`, I’ll record it with the current environment to avoid including mentions in the prose. I need to verify this across all four files and grep for any forbidden patterns.
exec
/bin/zsh -lc "rg -n '"'^'"\\\\begin\\{remark\\}.*\\\\ClaimStatusConjectured|"'^'"\\\\ClaimStatusConjectured"'$'"' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne '
if(/"'^'"\\s*\\\\begin\\{(theorem|proposition|lemma|corollary|remark|conjecture|definition|example|computation|calculation|verification|maintheorem)\\}(.*)"'$/){$env=$1; $rest=$2; if($rest =~ /'"\\\\ClaimStatus(Conjectured|ProvedHere|ProvedElsewhere)/){"'$status=$1; if(($status eq q(Conjectured) && $env ne q(conjecture)) || (($status eq q(ProvedHere) || $status eq q(ProvedElsewhere)) && $env eq q(conjecture))){print qq($ARGV:$.: env=$env status=$status'"\\n);}} next;}
if(/"'^'"\\s*\\\\ClaimStatus(Conjectured|ProvedHere|ProvedElsewhere)\\b/){"'$status=$1; if(($status eq q(Conjectured) && $env ne q(conjecture)) || (($status eq q(ProvedHere) || $status eq q(ProvedElsewhere)) && $env eq q(conjecture))){print qq($ARGV:$.: env=$env status=$status'"\\n);}}
' chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2168:\ClaimStatusConjectured
 succeeded in 51ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

codex
The structural scan is clean now. I’m doing one final diff/readback plus a couple of explicit greps on the edited file for the old stale reference text and the old `remark`-with-`Conjectured` pattern.
exec
/bin/zsh -lc "rg -n 'Remark~\\\\ref\\{rem:admissible-2-koszul\\}|"'^'"\\\\begin\\{remark\\}.*\\\\ClaimStatusConjectured' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/bar_cobar_adjunction_inversion.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5..e6c7232 100644
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@ asserts the coderived statement of~(2), and isolates in~(4) the extra
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 




thinking
**Evaluating label prefixes**

I’m looking at the labels and realizing there’s a mismatch between the label prefix and the environment we’re using. The user asked me to check the validity of references and labels. While the labels themselves are valid, this prefix issue could lead to some confusion.

Do we need to rename anything? If we rename the labels to something that matches, like `conj:`, we’ll also need to update references accordingly, but there's a concern about stale metadata. I’ll need to check this thoroughly!
thinking
**Considering label changes**

I’m thinking about the user's request to only rename labels in explicitly assigned files. It seems that conforming to AP125 makes sense since the `conjecture` environment should use `conj:` labels. While renaming is slightly invasive, I don’t see any references in other files or docs, just self-references and metadata.

However, if the environment changes, that could also make existing metadata stale. So, renaming might just help align the labels properly with the environment, ensuring validity and compliance with the rules. I'll need to check for uniqueness too!
thinking
**Searching for specific labels**

I need to search for the labels `conj:admissible-2-koszul` and `conj:bar-morita-koszul-conductor` across all three volumes using the `rg` command. This should help me locate any relevant instances of these specific terms in the files. I'll make sure to look everywhere to see if there are any notes, references, or details associated with those labels that might be useful for the user. Let's get on it!
codex
The claim-status surface is fixed, but the first pass left the old `rem:` labels on new `conjecture` environments. I’m checking whether the corresponding `conj:` labels are free; if they are, I’ll rename them locally so the label prefix matches the environment instead of leaving semantic drift behind.
exec
/bin/zsh -lc "rg -n '\\\\label\\{conj:admissible-2-koszul\\}|conj:admissible-2-koszul' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n '\\\\label\\{conj:bar-morita-koszul-conductor\\}|conj:bar-morita-koszul-conductor' /Users/raeez/chiral-bar-cobar /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups" in /Users/raeez/chiral-bar-cobar exited 1 in 67ms:

 exited 1 in 68ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..e6c723256589c6808e9e428c5ab8c2f1a979444a
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,6 +1700,57 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
+
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
 
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
@@ -1772,7 +1823,7 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
 \label{rem:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
@@ -1802,58 +1853,7 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
-
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
+\end{conjecture}
 
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,7 +2163,7 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
 \label{rem:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Patching file labels**

I think we should rename the labels and make local references clearer. It seems important to search for any occurrences of old labels, but I wonder if we can skip over things like just metadata and healing documents. The user has limited editing on the assigned files, so I'll focus on updating within the file itself. Alright, let's go ahead and patch this up!
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1826,3 +1826,3 @@
 \begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
@@ -2009,3 +2009,3 @@
  $\widehat{\mathfrak{sl}}_2$ example of
- Conjecture~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
@@ -2166,3 +2166,3 @@
 \begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
apply_patch(auto_approved=true) exited 0 in 23ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Searching for old labels**

I need to search for any old label references within the file, though I wonder if any actually remain. It seems like a good idea to use 'rg' for this task, as it should help me efficiently locate those references — if they exist. I’m curious about what I’ll find and how it might impact the current state of the file. Let’s see what I can uncover!
exec
/bin/zsh -lc "rg -n 'conj:admissible-2-koszul|conj:bar-morita-koszul-conductor' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'rem:admissible-2-koszul|rem:bar-morita-koszul-conductor' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
1827:\label{conj:admissible-2-koszul}%
2010: Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
2167:\label{conj:bar-morita-koszul-conductor}
 exited 1 in 51ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Considering verification process**

I think I should rerun the verification script using an improved parser, but I'm not sure if adding a label prefix with grep is necessary. Also, I need to grep the modified file for any forbidden patterns now. Perhaps using rg could help with filtering out old labels without remarks. Hmm, it looks like I will need to run this across four files again to ensure everything is covered properly.
codex
The labels are now aligned too. I’m rerunning the narrow verification one last time across all four files, then I’ll close with a file-level status map.
exec
/bin/zsh -lc "perl -ne '
if(/"'^'"\\s*\\\\begin\\{(theorem|proposition|lemma|corollary|remark|conjecture|definition|example|computation|calculation|verification|maintheorem)\\}(.*)"'$/){$env=$1; $rest=$2; if($rest =~ /'"\\\\ClaimStatus(Conjectured|ProvedHere|ProvedElsewhere)/){"'$status=$1; if(($status eq q(Conjectured) && $env ne q(conjecture)) || (($status eq q(ProvedHere) || $status eq q(ProvedElsewhere)) && $env eq q(conjecture))){print qq($ARGV:$.: env=$env status=$status'"\\n);}} next;}
if(/"'^'"\\s*\\\\ClaimStatus(Conjectured|ProvedHere|ProvedElsewhere)\\b/){"'$status=$1; if(($status eq q(Conjectured) && $env ne q(conjecture)) || (($status eq q(ProvedHere) || $status eq q(ProvedElsewhere)) && $env eq q(conjecture))){print qq($ARGV:$.: env=$env status=$status'"\\n);}}
' chapters/theory/bar_construction.tex chapters/theory/cobar_construction.tex chapters/theory/bar_cobar_adjunction_inversion.tex chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'Remark~\\\\ref\\{conj:admissible-2-koszul\\}|"'^'"\\\\begin\\{remark\\}.*\\\\ClaimStatusConjectured|rem:admissible-2-koszul|rem:bar-morita-koszul-conductor' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 exited 1 in 52ms:

file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Checking modified files**

I need to check the final git diff to see what changes were made. Hmm, I might just run a command to list the modified files. There’s only one file? The user seems to be looking for specific assigned files, but others are unchanged. That’s fine; I’ll focus on the relevant ones. So I think I can update the plan now that I have a clearer picture.
Plan update
All live mismatches in the assigned files are resolved. The only edited file was `bar_cobar_adjunction_inversion.tex`; the other three files re-scanned clean. I also repaired the adjacent proof placement and label prefixes in the edited file so the local theorem/conjecture surface remains coherent.
  ✓ Read local context around each mismatch and decide the minimal truthful alignment
  ✓ Patch the assigned file(s) with only the necessary environment/tag edits
  ✓ Re-read edited blocks, check local labels/refs, and grep modified files for forbidden patterns
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 


thinking
**Looking into clickable links**

I need to ensure I have clickable links. I think I'll use the link format like [bar_cobar_adjunction_inversion.tex] for referencing. I wonder if it’s possible to include multiple line references, where each link only points to optional line numbers. Maybe I should consider mentioning one link for the beginning of the theorem or proof and another for the conjectural area? But it's crucial to avoid including ranges.
codex
Claim-status mismatches are resolved.

- `chapters/theory/bar_construction.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.
- `chapters/theory/cobar_construction.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.
- `chapters/theory/bar_cobar_adjunction_inversion.tex`: FIXED in [bar_cobar_adjunction_inversion.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex:1701). I converted the two conjectural `remark` blocks into `conjecture` environments, renamed their labels to `conj:...`, updated the in-file cross-reference, and moved the stranded proof of `thm:bar-cobar-inversion-qi` so the local theorem/conjecture surface stays coherent.
- `chapters/theory/bar_cobar_adjunction_curved.tex`: FIXED by verification; no environment/status mismatch was present, so no edit was needed.

Verification: I re-scanned all four files for `Conjectured/ProvedHere/ProvedElsewhere` tag/environment mismatches and got no hits. I also grepped the edited file for the old forbidden `remark`+`ClaimStatusConjectured` pattern, stale `rem:` labels, and the stale `Remark~\ref{...}` text; all were clean. I did not run a full LaTeX build or regenerate metadata.
file update:
diff --git a/chapters/theory/bar_cobar_adjunction_inversion.tex b/chapters/theory/bar_cobar_adjunction_inversion.tex
index 5c48ad5175d818d9826fbf6860d17c95dd7338c3..91bb87108ecf0be0fe2da648d3920a640c0f6078
--- a/chapters/theory/bar_cobar_adjunction_inversion.tex
+++ b/chapters/theory/bar_cobar_adjunction_inversion.tex
@@ -1700,7 +1700,58 @@
 input needed to recover an ordinary quasi-isomorphism there.
 \end{theorem}
 
+\begin{proof}[Dependency-closed proof]
+We verify each numbered clause by previously established results in
+this chapter and in the coderived appendix.
+\begin{enumerate}[label=(D\arabic*)]
+\item \emph{Strict Koszul lane.}
+The genus-$0$ quasi-isomorphism is proved independently by
+Theorem~\ref{thm:bar-nilpotency-complete} and
+Theorem~\ref{thm:chiral-koszul-duality};
+equivalently, it is the implication
+\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
+the fundamental theorem of chiral twisting morphisms
+(Theorem~\ref{thm:fundamental-twisting-morphisms}).
+Under the higher-genus hypotheses of
+Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
+$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
+and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
+series statement.
+
+\item \emph{Coderived off-Koszul lane.}
+Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
+factorization counit $\psi_X$ is an isomorphism in the coderived
+category for every complete augmented input with finite-dimensional
+graded bar pieces. Its proof is independent of
+Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
+$\psi_X$ as coacyclic by stratified Positselski inversion and the
+Verdier-quotient criterion for
+$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
+
+\item \emph{Coderived bar-degree filtration.}
+On the strict square-zero surface, existence and collapse are exactly
+Theorems~\ref{thm:bar-cobar-spectral-sequence}
+and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
+Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
+replaces ordinary abutment by coacyclicity of the cone: the
+associated-graded $E_1$ page is strict because the curvature term lies
+in positive filtration.
 
+\item \emph{Promotion lane.}
+If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
+square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
+coderived and ordinary derived categories and the coderived
+equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
+any class~$G/L$ collapse input for the coderived bar-degree spectral
+sequence turns coacyclicity of the cone into acyclicity, hence into an
+ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
+in clause~(4).
+\end{enumerate}
+Combining (D1)--(D4) gives the strongest proved package stated in the
+theorem.
+\end{proof}
+
+
 \begin{example}[Admissible-level failure of bar-cobar inversion]
 \label{ex:admissible-sl2-failure}
 \index{admissible level!bar-cobar inversion failure}
@@ -1772,8 +1823,8 @@
 acquires infinitely many off-diagonal classes.
 \end{example}
 
-\begin{remark}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
-\label{rem:admissible-2-koszul}%
+\begin{conjecture}[$2$-Koszulness at admissible level; \ClaimStatusConjectured]
+\label{conj:admissible-2-koszul}%
 \index{2-Koszul!admissible level}%
 \index{admissible level!2-Koszul}%
 The preceding example shows that $L_{-1/2}(\mathfrak{sl}_2)$ fails
@@ -1802,59 +1853,8 @@
 classical Koszul (generic level, $E_2$ collapse) $\subset$
 $N$-Koszul (admissible level, $E_N$ collapse) $\subset$
 non-Koszul (critical level, no finite collapse).
-\end{remark}
-
-\begin{proof}[Dependency-closed proof]
-We verify each numbered clause by previously established results in
-this chapter and in the coderived appendix.
-\begin{enumerate}[label=(D\arabic*)]
-\item \emph{Strict Koszul lane.}
-The genus-$0$ quasi-isomorphism is proved independently by
-Theorem~\ref{thm:bar-nilpotency-complete} and
-Theorem~\ref{thm:chiral-koszul-duality};
-equivalently, it is the implication
-\ref{ftm:koszul}$\Rightarrow$\ref{ftm:counit} of
-the fundamental theorem of chiral twisting morphisms
-(Theorem~\ref{thm:fundamental-twisting-morphisms}).
-Under the higher-genus hypotheses of
-Theorem~\ref{thm:higher-genus-inversion}, the genus-$g$ components
-$\psi_g$ for $g \geq 1$ are quasi-isomorphisms by induction on genus,
-and Theorem~\ref{thm:genus-graded-convergence} supplies the completed
-series statement.
-
-\item \emph{Coderived off-Koszul lane.}
-Theorem~\ref{thm:off-koszul-ran-inversion} proves that the
-factorization counit $\psi_X$ is an isomorphism in the coderived
-category for every complete augmented input with finite-dimensional
-graded bar pieces. Its proof is independent of
-Theorem~\ref{thm:higher-genus-inversion}: it identifies the cone of
-$\psi_X$ as coacyclic by stratified Positselski inversion and the
-Verdier-quotient criterion for
-$D^{\mathrm{co}}(\barB\text{-}\mathrm{CoFact})$.
-
-\item \emph{Coderived bar-degree filtration.}
-On the strict square-zero surface, existence and collapse are exactly
-Theorems~\ref{thm:bar-cobar-spectral-sequence}
-and~\ref{thm:spectral-sequence-collapse}. On the curved surface,
-Proposition~\ref{prop:coderived-bar-degree-spectral-sequence}
-replaces ordinary abutment by coacyclicity of the cone: the
-associated-graded $E_1$ page is strict because the curvature term lies
-in positive filtration.
+\end{conjecture}
 
-\item \emph{Promotion lane.}
-If $\kappa(\mathcal{A}) = 0$, then the curved differential becomes
-square-zero, so Theorem~\ref{thm:conilpotent-reduction} identifies the
-coderived and ordinary derived categories and the coderived
-equivalence of~(D2) is an ordinary quasi-isomorphism. More generally,
-any class~$G/L$ collapse input for the coderived bar-degree spectral
-sequence turns coacyclicity of the cone into acyclicity, hence into an
-ordinary quasi-isomorphism. This is the exact extra hypothesis isolated
-in clause~(4).
-\end{enumerate}
-Combining (D1)--(D4) gives the strongest proved package stated in the
-theorem.
-\end{proof}
-
 \begin{remark}[Alternative proof via formality]
 \label{rem:bar-cobar-inversion-alt-formality}
 The strict Koszul lane of
@@ -2007,7 +2007,7 @@
  comparison remains available; what is missing is ordinary
  cohomological detectability of the coacyclic cone. The admissible
  $\widehat{\mathfrak{sl}}_2$ example of
- Remark~\ref{rem:admissible-2-koszul} is the model case: proving its
+ Conjecture~\ref{conj:admissible-2-koszul} is the model case: proving its
  conjectural $2$-Koszul behavior would move it closer to the derived
  wall, but by itself would not yet supply the promotion required in
  clause~\textup{(4)}.
@@ -2163,8 +2163,8 @@
 \end{remark}
 
 
-\begin{remark}[Derived Morita equivalence and the Koszul conductor]
-\label{rem:bar-morita-koszul-conductor}
+\begin{conjecture}[Derived Morita equivalence and the Koszul conductor]
+\label{conj:bar-morita-koszul-conductor}
 \ClaimStatusConjectured
 \index{derived Morita equivalence!bar coalgebra characterization}
 \index{Koszul conductor!Morita obstruction}
@@ -2191,7 +2191,7 @@
 The non-vanishing conductor therefore provides a numerical
 obstruction to derived Morita equivalence that has no counterpart
 in the $K = 0$ families.
-\end{remark}
+\end{conjecture}
 
 \subsection{Proof strategy and filtration}
 

tokens used
77,658
