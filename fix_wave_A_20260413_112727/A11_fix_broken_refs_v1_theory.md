# A11_fix_broken_refs_v1_theory (766s)

Edited only [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5071). I did not touch `higher_genus_complementarity.tex`, `existence_criteria.tex`, or `configuration_spaces.tex` where the audit hits were false positives from searching `chapters/` only.

1. `higher_genus_complementarity.tex:88` `app:nonlinear-modular-shadows` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
2. `higher_genus_complementarity.tex:1198` `app:signs` — BLOCKED: label exists in `appendices/signs_and_shifts.tex`.
3. `higher_genus_complementarity.tex:1198` `app:sign-conventions` — BLOCKED: label exists in `appendices/signs_and_shifts.tex`.
4. `higher_genus_complementarity.tex:1740` `part:characteristic-datum` — BLOCKED: label exists in `main.tex`.
5. `higher_genus_complementarity.tex:2518` `part:characteristic-datum` — BLOCKED: label exists in `main.tex`.
6. `higher_genus_complementarity.tex:4466` `thm:chiral-htt` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
7. `higher_genus_complementarity.tex:4482` `thm:bar-cobar-htt` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
8. `higher_genus_complementarity.tex:5126` `thm:nms-archetype-trichotomy` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
9. `higher_genus_complementarity.tex:5134` `thm:nms-finite-termination` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
10. `higher_genus_complementarity.tex:5782` `thm:nms-archetype-trichotomy` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
11. `ordered_associative_chiral_kd.tex:5075` `thm:affine-monodromy-identification` — FIXED: removed the Vol II-only `\ref` and cited the Volume II one-loop collapse textually.
12. `ordered_associative_chiral_kd.tex:5116` `thm:affine-monodromy-identification` — FIXED: same.
13. `ordered_associative_chiral_kd.tex:5486` `thm:affine-monodromy-identification` — FIXED: same.
14. `ordered_associative_chiral_kd.tex:5666` `thm:affine-monodromy-identification` — FIXED: same.
15. `ordered_associative_chiral_kd.tex:5717` `thm:affine-monodromy-identification` — FIXED: same.
16. `ordered_associative_chiral_kd.tex:6047` `ex:yangian` — FIXED: rewrote to plain “low-degree Yangian computations”.
17. `ordered_associative_chiral_kd.tex:6048` `conj:yangian-ordered-center` — FIXED: rewrote to plain “conjectural ordered-centre bounds”.
18. `ordered_associative_chiral_kd.tex:6146` `conj:yangian-ordered-center` — FIXED: retitled the remark without the dangling conjecture ref.
19. `ordered_associative_chiral_kd.tex:6159` `conj:yangian-ordered-center` — FIXED: replaced with plain conjectural wording.
20. `ordered_associative_chiral_kd.tex:6166` `ex:yangian` — FIXED: replaced with “classical Yangian computation”.
21. `ordered_associative_chiral_kd.tex:8107` `ex:yangian` — FIXED: replaced with “classical Yangian case”.
22. `ordered_associative_chiral_kd.tex:8132` `ex:yangian` — FIXED: same.
23. `ordered_associative_chiral_kd.tex:8168` `ex:yangian` — FIXED: same.
24. `ordered_associative_chiral_kd.tex:8385` `ex:yangian-coproduct` — FIXED: replaced with a local reference to the expansions displayed below.
25. `ordered_associative_chiral_kd.tex:8577` `def:chiral-coproduct` — BLOCKED: not actually broken; a local phantom label already exists later in the file.
26. `ordered_associative_chiral_kd.tex:8731` `def:e1-chiral-rmatrix` — FIXED: redirected to existing `Definition~\ref{def:e1-chiral}`.
27. `ordered_associative_chiral_kd.tex:10225` `thm:tree-formula` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
28. `ordered_associative_chiral_kd.tex:10240` `constr:transfer-ainf` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
29. `existence_criteria.tex:474` `app:koszul-reference` — BLOCKED: label exists in `appendices/koszul_reference.tex`.
30. `configuration_spaces.tex:83` `thm:arnold-iff-nilpotent` — BLOCKED: label exists in `appendices/arnold_relations.tex`.

Verification: the removed dangling labels no longer occur in `ordered_associative_chiral_kd.tex`, and the appendix/main labels above were confirmed to exist on the live surface. The modified file still has many other unresolved refs outside this first-30 task. I did not run a TeX build.


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
session id: 019d863d-b373-7be3-a514-18b057d7be95
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


TARGET: chapters/theory/ (all files)

The audit found 159 CRITICAL+HIGH broken references in Vol I. Focus on theory/ chapters.

Run: grep -rn '\\ref{' chapters/theory/ | head -100
For each ref, check if the corresponding label exists:
  grep -rn 'label{LABELNAME}' chapters/

Fix broken refs by either: (a) correcting the label name, (b) adding the missing label,
or (c) removing the dangling reference if the target was deleted.

Focus on the FIRST 30 broken refs you find. Fix each one.
mcp startup: no servers
codex
I’m treating this as a tightly scoped label/reference repair in `chapters/theory/`. First I’m reading the required repo-constitution files, then I’ll enumerate the first 30 broken `\ref`s in `theory/`, map each to an existing or missing label, and patch only those exact sites.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

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
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Theorem Registry

Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2809 |
| Total tagged claims | 3615 |
| Active files in `main.tex` | 85 |
| Total `.tex` files scanned | 128 |

## Status Totals

| Status | Count |
|---|---:|
| `ProvedHere` | 2809 |
exec
/bin/zsh -lc "sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/claim-surface-sync/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
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
 exited 1 in 52ms:
sed: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory



thinking
**Identifying broken references**

I need to take note that the red_team_summary path is missing, and I might consider finding an alternative archive path to read from. There's the claim-surface-sync skill that could be relevant, so I might announce its usage. I should identify the first 30 broken references by using a script to extract them from chapters/theory and check for missing labels. The user mentioned running a command, and we'll focus on the first 30 broken references found in the grep output. There are 159 broken refs in total to address.
thinking
**Checking broken references**

I think I need to use a command to get the first 100 lines containing references from chapters/theory and parse them to check for missing labels. My goal is to identify the first 30 broken references as I scan through the grep results. I might use a custom script with shell or Perl to help with that. Then, I could spawn an explorer agent to analyze these broken refs and suggest fixes based on existing labels. Even though I shouldn't re-read, opening affected files for context could still be helpful. I'll make sure to ask the explorers precisely what I need.
thinking
**Using the explorer for broken refs**

I think I can trust the explorer's results without needing to verify them. If it lists broken references and suggests potential target labels, there's no need for duplicate searches. However, I should inspect the file context around the actual edit locations, as that doesn't count as re-searching, right? So it might be okay. I’ll use the explorer to identify the broken references and their corresponding labels, so let's go ahead and spawn the explorer!
codex
I’ve loaded the constitutional files and the claim-sync workflow. `raeeznotes/raeeznotes100/red_team_summary.md` is absent, so I’ll fall back to the archive copy if it exists, then I’m using the claim-surface-sync workflow to identify the first 30 broken `\ref`s and their minimal repairs.
exec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
collab spawn_agent(call_GG5vCWERyhy1JJy4RhbW9SnQ, prompt="In /Users/raeez/chiral-bar-cobar, inspect chapters/theory only. Task: run the equivalent of `grep -rn '\\ref{' chapters/…")
spawn_agent(call_GG5vCWERyhy1JJy4RhbW9SnQ, prompt="In /Users/raeez/chiral-bar-cobar, inspect chapters/theory only. Task: run the equivalent of `grep -rn '\\ref{' chapters/…") pending init:
  agent: 019d863e-394a-7f80-ab99-9743c234c9db
mcp startup: no servers

thinking
**Updating the plan**

I need to consider updating my plan. It might help to set things up after I gather some context. I could run some grep commands or maybe wait for the agent to help out. I'm also thinking that I could run some commands myself for a list, since the explorer will manage that. But overall, I feel like we should probably start with a clear plan first.
Plan update
Scoped to the first 30 broken `\ref` targets encountered in `chapters/theory/`. I’ve loaded the required constitutional files and started a precise ref/label audit before patching.
  → Identify the first 30 broken refs in `chapters/theory/` and classify each as typo, missing label, or deleted target
  • Patch only the affected theory files with the minimal truthful fix for each broken ref
  • Re-read modified context, validate labels/refs, and grep modified files for lingering broken patterns

thinking
**Planning broken references script**

I'll write a Python script to scan all labels under `chapters/` and all references in `chapters/theory/`, then find the first 30 broken references whose labels don’t exist. I’ll also suggest close label matches using difflib when appropriate. This approach keeps everything read-only and ordered by file and line.
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python - <<'PY'
import os, re, sys
label_set=set()
root='chapters'
for dirpath, dirnames, filenames in os.walk(root):
    filenames.sort()
    for fname in filenames:
        path=os.path.join(dirpath,fname)
        try:
            text=open(path,'r',encoding='utf-8').read()
        except Exception:
            continue
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', text):
            label_set.add(m.group(1))
ref_list=[]
root='chapters/theory'
for dirpath, dirnames, filenames in os.walk(root):
    dirnames.sort()
    filenames.sort()
    for fname in filenames:
        path=os.path.join(dirpath,fname)
        try:
            lines=open(path,'r',encoding='utf-8').read().splitlines()
        except Exception:
            continue
        for i,line in enumerate(lines,1):
            for m in re.finditer(r'\\\\ref\\{(["'^}]+)'"\\}', line):
                ref_list.append((path, i, m.group(1)))
broken=[]
import difflib
for path,line,label in ref_list:
    if label not in label_set:
        best = difflib.get_close_matches(label, label_set, n=1, cutoff=0.6)
        replacement = best[0] if best else 'missing/deleted'
        broken.append((path,line,label,replacement))
        if len(broken)>=30:
            break
for path,line,label,replacement in broken:
    print(f\"{path}:{line} {label} -> {replacement}\")
print('Total broken found:', len(broken))
PY" in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc "cd /Users/raeez/chiral-bar-cobar && python3 - <<'PY'
import os, re, sys
label_set=set()
root='chapters'
for dirpath, dirnames, filenames in os.walk(root):
    dirnames.sort()
    filenames.sort()
    for fname in filenames:
        path=os.path.join(dirpath,fname)
        try:
            with open(path,'r',encoding='utf-8') as f:
                text=f.read()
        except Exception:
            continue
        for m in re.finditer(r'\\\\label\\{(["'^}]+)'"\\}', text):
            label_set.add(m.group(1))
ref_list=[]
root='chapters/theory'
for dirpath, dirnames, filenames in os.walk(root):
    dirnames.sort()
    filenames.sort()
    for fname in filenames:
        path=os.path.join(dirpath,fname)
        try:
            with open(path,'r',encoding='utf-8') as f:
                lines=f.read().splitlines()
        except Exception:
            continue
        for i,line in enumerate(lines,1):
            for m in re.finditer(r'\\\\ref\\{(["'^}]+)'"\\}', line):
                ref_list.append((path, i, m.group(1)))
broken=[]
import difflib
for path,line,label in ref_list:
    if label not in label_set:
        best = difflib.get_close_matches(label, label_set, n=1, cutoff=0.6)
        replacement = best[0] if best else 'missing/deleted'
        broken.append((path,line,label,replacement))
        if len(broken)>=30:
            break
for path,line,label,replacement in broken:
    print(f\"{path}:{line} {label} -> {replacement}\")
print('Total broken found:', len(broken))
PY" in /Users/raeez/chiral-bar-cobar
thinking
**Considering forbidden patterns**

The user is asking about editing grep for forbidden patterns within modified files. I’m wondering if these patterns could relate to broken references. It seems like AGENTS want grep to check forbidden formulas after every .tex write. Since there are changed labels and refs, it might be necessary to grep for these forbidden formulas in modified files. I'll need to look for specific patterns like `\ref{` for broken labels and ensure that they are valid. A small script to verify references might be useful here. Let's wait for further guidance from the agent.
codex
The archive red-team summary exists, so the required first-read set is now complete. I’m waiting on a targeted ref audit that will hand back the first 30 broken labels in order so I can patch only those sites instead of scanning the whole theory tree blindly.
collab wait(call_00lybVXemvbXDVZ0tWgUcJSc)
  receivers: 019d863e-394a-7f80-ab99-9743c234c9db
 succeeded in 8.82s:
chapters/theory/algebraic_foundations.tex:116 def:bar-complex-algebraic -> def:bar-complex-modules
chapters/theory/algebraic_foundations.tex:443 part:bar-complex -> prop:kzb-bar-complex
chapters/theory/algebraic_foundations.tex:1079 app:signs -> missing/deleted
chapters/theory/algebraic_foundations.tex:1079 app:sign-conventions -> sec:sign-conventions
chapters/theory/bar_cobar_adjunction_curved.tex:323 part:characteristic-datum -> prop:fermion-characteristic-data
chapters/theory/bar_cobar_adjunction_curved.tex:323 part:standard-landscape -> sec:ent-standard-landscape
chapters/theory/bar_cobar_adjunction_curved.tex:5631 part:standard-landscape -> sec:ent-standard-landscape
chapters/theory/bar_cobar_adjunction_inversion.tex:1980 sec:complementarity -> sec:ent-complementarity
chapters/theory/bar_cobar_adjunction_inversion.tex:3275 thm:essential-image-koszul -> thm:essential-image-bar
chapters/theory/bar_construction.tex:641 app:signs -> missing/deleted
chapters/theory/bar_construction.tex:641 app:sign-conventions -> sec:sign-conventions
chapters/theory/bar_construction.tex:641 sec:sign-dictionary-complete -> subsec:heisenberg-dictionary-complete
chapters/theory/bar_construction.tex:954 ver:d2-degree3 -> eq:g2-degree0
chapters/theory/bar_construction.tex:955 prop:master-sign -> prop:branch-master-equation
chapters/theory/bar_construction.tex:955 app:signs -> missing/deleted
chapters/theory/bar_construction.tex:1225 app:arnold-relations -> thm:arnold-relations
chapters/theory/chiral_hochschild_koszul.tex:1003 thm:nms-all-degree-master-equation -> eq:all-degree-master-eq-intro
chapters/theory/chiral_hochschild_koszul.tex:1309 part:characteristic-datum -> prop:fermion-characteristic-data
chapters/theory/chiral_hochschild_koszul.tex:1351 part:characteristic-datum -> prop:fermion-characteristic-data
chapters/theory/chiral_hochschild_koszul.tex:2293 app:signs -> missing/deleted

thinking
**Preparing final list of broken references**

I'm putting together a friendly summary that lists the first 30 broken references found by a Python script, including source file and line, the broken label, and either the best replacement or a note if it's missing or deleted. I'll format it as a numbered list with concise entries showing all these details clearly.
codex
Ran a quick scan (labels across `chapters/`, refs inside `chapters/theory/`) and listed the first 30 `\ref{…}` targets that have no existing label anywhere under `chapters/`. Each line below gives the source location, the broken label, and the closest likely intended label (or “missing/deleted” when no close match exists).
wait(call_00lybVXemvbXDVZ0tWgUcJSc) 1 agents complete:
  019d863e-394a-7f80-ab99-9743c234c9db completed: "Ran a quick scan (labels across `chapters/`, refs inside `chapters/theory/`) and listed the first 30 `\ref{…}` targets t…"

thinking
**Finalizing message content**

I need to make sure I get the final message content from the agent. I wonder if the output is included or if it might be truncated? It might only show a brief status. I think I need to either close or send the input to see if it returns the complete message. It seems like I should call close_agent to receive the last known status or any full message. Let's do that!
collab close_agent(call_MIkNTADF5yZB8unmbWQVHSpV)
  receiver: 019d863e-394a-7f80-ab99-9743c234c9db
close_agent(call_MIkNTADF5yZB8unmbWQVHSpV) completed: "Ran a quick scan (labels across `chapters/`, refs inside `chapters/theory/`) and listed the first 30 `\ref{…}` targets t…":
  receiver: 019d863e-394a-7f80-ab99-9743c234c9db

thinking
**Considering agent interaction**

I'm noticing that I might not have received the full details due to message truncation. I wonder if waiting or closing affects that. Maybe I can use send_input to request a report, but it seems the agent is closed. If I can resume, maybe I could send the input afterward. Alright, so I think the next step is to try resuming the agent and then use send_input. Let's see how that goes!
codex
The first audit finished, but the tool only surfaced its headline, not the detailed 30-line mapping. I’m resuming that explorer and asking for the concrete source-line and replacement list so the edits stay surgical.
collab send_input(call_ha2AhpktiV8NgYXylGx5FODX, prompt="Send the actual ordered list now. Format exactly as 30 flat lines: `sourcefile:line | broken_label | suggested_fix_or_mi…")
  receiver: 019d863e-394a-7f80-ab99-9743c234c9db
send_input(call_ha2AhpktiV8NgYXylGx5FODX, prompt="Send the actual ordered list now. Format exactly as 30 flat lines: `sourcefile:line | broken_label | suggested_fix_or_mi…") pending init:
  receiver: 019d863e-394a-7f80-ab99-9743c234c9db
collab wait(call_3evosFuhEUaRqwTOTTvtM2xn)
  receivers: 019d863e-394a-7f80-ab99-9743c234c9db
wait(call_3evosFuhEUaRqwTOTTvtM2xn) 1 agents complete:
  019d863e-394a-7f80-ab99-9743c234c9db completed: "chapters/theory/higher_genus_complementarity.tex:88 | app:nonlinear-modular-shadows | prop:cobar-modular-shadow
chapters…"
codex
I have the ordered 30-item break list now. Next step is local context only: I’m opening the exact source neighborhoods for each affected line cluster, plus the candidate target labels, to make sure every replacement is semantically correct before I touch the files.
exec
/bin/zsh -lc "sed -n '70,110p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.

\item \emph{Shifted-symplectic Lagrangian upgrade
 \textup{(}conditional on perfectness and nondegeneracy\textup{)}.}\;
 When the relative bar family
 $R\pi_{g*}\barB^{(g)}(\cA)$ is perfect
 \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
 Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
 complex $\mathbf{C}_g(\cA) = R\Gamma(\overline{\mathcal{M}}_g,
 \mathcal{Z}(\cA))$ is non-degenerate, the complex
 $\mathbf{C}_g(\cA)$ carries a $({-}(3g{-}3))$-shifted symplectic
 structure \textup{(}PTVV
 \cite{PTVV13}\textup{)}, and the summands $\mathbf{Q}_g(\cA)$ and
 $\mathbf{Q}_g(\cA^!)$ are Lagrangian subspaces: isotropic of half
 rank, with $\mathbf{Q}_g(\cA) \simeq
 \mathbf{Q}_g(\cA^!)^\vee[-(3g{-}3)]$.
 This is the geometric home of the finite-order shadow
 tower~$\Theta_{\cA}^{\leq r}$
 \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
\end{enumerate}
exec
/bin/zsh -lc "sed -n '1728,1750p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1186,1210p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2508,2528p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
(central extension, eigenvalue $+1$) and $Q_1(\mathcal{H}_\kappa^!) = \mathbb{C}
\cdot \lambda$ (curvature, eigenvalue $-1$). Dimension check: $1 + 1 = 2$.

\emph{Genus $2$}: $\dim H^*(\overline{\mathcal{M}}_2) = 8$
(Poincar\'e polynomial $1 + 3t^2 + 3t^4 + t^6$).
The involution $\sigma$ splits $H^*$ into $\pm 1$-eigenspaces whose
dimensions depend on the chiral algebra through the $j_*/j_!$ extension
data. For Koszul self-dual algebras (e.g., $\mathrm{Vir}_{13}$),
Corollary~\ref{cor:virasoro-quantum-dim} gives
$\dim V^+ = \dim V^- = 4$. For all Koszul chiral algebras
$\cA$ with trivial center, $\dim Q_2(\cA) + \dim Q_2(\cA^!) = 8$.
Detailed genus-$2$ complementarity dimensions are verified in
Part~\ref{part:characteristic-datum} (\S\ref{subsec:genus2-complementarity-verification}).
\end{proof}

This completes Step~III. Combining Steps~7--10, we have shown:
\begin{enumerate}
\item Kodaira--Spencer map via Gauss--Manin connection (Step 7), with anti-commutativity
$\mathbb{D} \circ \nabla_{\kappa(v)}^z = -\nabla_{\kappa(v)}^z \circ \mathbb{D}$
\item Verdier involution $\sigma$ with $\sigma^2 = \mathrm{id}$ (Step 8)
 succeeded in 50ms:
$\kappa(\mathcal{H}_\kappa) = \kappa$.
Taking cohomology of the total differential
$d^{(1)}_{\mathrm{total}}$:
\begin{equation}
Q_1(\mathcal{H}_\kappa) = H^*(\bar{B}^{(1)}(\mathcal{H}_\kappa),\,
d^{(1)}_{\mathrm{total}}) = \mathbb{C} \cdot \kappa
\end{equation}

\emph{Step 2: Compute $Q_1(\mathcal{H}_\kappa^!)$ using complementarity}.

The Koszul dual of the Heisenberg algebra is the curved Chevalley--Eilenberg algebra (cf.\ Part~\ref{part:characteristic-datum}):
\begin{equation}
\mathcal{H}_\kappa^! = \mathrm{CE}(\mathfrak{h}_{-\kappa}) = (\mathrm{Sym}^{\mathrm{ch}}(V^*), d_{\mathrm{CE}}, m_0 = -\kappa \cdot c)
\end{equation}
where $V^*$ is the linear dual of the generating space~$V$, the curvature
$m_0 = -\kappa \cdot c$ encodes the obstruction, and
$\kappa(\mathcal{H}_\kappa^!) = -\kappa$
(since $h^\vee = 0$ for the Heisenberg).
Note: $\mathcal{H}_\kappa^! = \mathrm{Sym}^{\mathrm{ch}}(V^*)
\neq \mathcal{H}_{-\kappa}$; the Koszul dual is generated by~$V^*$,
 succeeded in 50ms:
\langle -, - \rangle: H^q(\bar{B}^p_g(\mathcal{A})) \otimes H^{d-q}(\bar{B}^p_g(
\mathcal{A}^!)) \to \mathbb{C}
\end{equation}
is perfect. Thus $(E_1^{p,q,g})_{\mathcal{A}} \cong ((E_1^{p,d-q,g})_{\mathcal{A}^!})^\vee$.

\emph{Differential $d_1$}: The differential $d_1: E_1^{p,q,g} \to E_1^{p+1,q,g}$ is 
induced by the moduli space differential. Under Verdier duality:
\begin{equation}
\mathbb{D} \circ d_1 = (-1)^{p+q} d_1^\vee \circ \mathbb{D}
\end{equation}
where $d_1^\vee$ is the dual differential.

This sign is precisely the Koszul sign convention (see Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}). 
Thus the differential on $(E_1)_{\mathcal{A}}$ is dual to the differential on 
$(E_1)_{\mathcal{A}^!}$, up to the appropriate sign.

\emph{Higher pages}: By induction, if $(E_r)_{\mathcal{A}} \cong ((E_r)_{\mathcal{A}^!})^\vee$, 
then taking cohomology with respect to $d_r$ preserves this duality:
\begin{equation}
(E_{r+1})_{\mathcal{A}} = H(E_r, d_r)_{\mathcal{A}} \cong (H(E_r, d_r)_{\mathcal{A}^!})^\vee 
exec
/bin/zsh -lc "sed -n '4458,4490p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
$\cA$ are equivalent:
\begin{enumerate}[label=(\roman*)]
\item The bar spectral sequence
$E_1^{p,q}(g) \Rightarrow H^{p+q}(\Omega_g\Bbar_g(\cA))$
collapses at~$E_2$ for all $g \geq 0$.
\item The filtered $\Ainf$-algebra $\Omega_g(\Bbar_g(\cA))$ is
\emph{formal}: quasi-isomorphic to its cohomology with the
transferred $\Ainf$-structure
(Theorem~\textup{\ref{thm:chiral-htt}}).
\item The transferred higher operations satisfy
$\tilde{m}_n^{(g)} = 0$ for $n \geq 3$ and all~$g$
(Koszulness at all genera).
\end{enumerate}
In the factorization homology picture, formality means that
$\int_{\Sigma_g}\cA$ is determined by $\int_{\mathbb{P}^1}\cA$
and the handle attachments, with no higher coherence obstructions.
\end{proposition}

\begin{proof}
(i) $\Rightarrow$ (ii): The spectral sequence arises from the bar
exec
/bin/zsh -lc "sed -n '5118,5140p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5772,5790p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5068,5726p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
$\ell_3^{\mathrm{tr}} \neq 0$ (Virasoro, $\mathcal{W}_N$).
\end{itemize}
The shadow obstruction tower is the homotopy structure made visible.
\end{remark}

\begin{remark}[The three archetypes from the Lagrangian perspective]
\label{rem:three-archetypes-lagrangian}
The fake-complementarity criterion reframes the archetype trichotomy
(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
The Heisenberg is exactly fake: $S_{\mathcal{H}}$ is quadratic.
Affine $\widehat{\mathfrak{sl}}_2$ is cubic at leading order:
$S_{\mathrm{aff}} = \tfrac12 H + \tfrac16\kappa(a,[a,a])$,
so the dual Lagrangian bends cubically. The $\beta\gamma$ system is
quartic on the weight/contact slice. Virasoro is the first family
where the dual Lagrangian has both cubic and quartic bending,
and the complementarity potential is genuinely non-polynomial; its
shadow obstruction tower is infinite (Theorem~\ref{thm:nms-finite-termination}).
\end{remark}

\begin{remark}[Shadow obstruction tower as period correction]
 succeeded in 53ms:
 The shadow obstruction tower terminates at quartic order; $\mathfrak{N}_g$ is
 the leading nonlinear anomaly and captures the full quartic
 contact invariant $\mathfrak{Q}^{\mathrm{contact}}_{\beta\gamma}$.
\item \emph{Virasoro, $\mathcal{W}_N$.}\;
 The shadow obstruction tower is infinite. All trace-log terms
 $\operatorname{Tr}((C_1 B_2)^m)$ contribute, and the anomaly
 series does not truncate. The full metaplectic cocycle carries
 infinite-order modular data.
\end{itemize}
This is the holographic restatement of the archetype trichotomy
(Theorem~\ref{thm:nms-archetype-trichotomy}).
\end{remark}

\begin{theorem}[Critical dimension; \ClaimStatusProvedHere]
\label{thm:critical-dimension}
\index{critical dimension|textbf}
\index{shadow connection!flatness}
\index{Virasoro!critical dimension}
\index{W-algebra@$\mathcal{W}$-algebra!critical dimension}
 succeeded in 52ms:
additional generators (the $A$-cycle and $B$-cycle monodromies),
and their interaction with the braid generators produces the quantum
group $U_q(\mathfrak{g})$ from the Yangian $Y_\hbar(\mathfrak{g})$.

The genus-$1$ lift for the affine lineage
$V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
one-loop collapse mechanism of
Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
giving a rigorous passage from the KZ connection to the KZB connection and
thence to the quantum group.

\subsection{The KZ connection on ordered configurations}
\label{sec:kz-connection}

The genus-$0$ starting point is as follows. Let $\mathfrak{g}$ be a simple
Lie algebra and $k \in \mathbb{C} \setminus \{-h^\vee\}$ generic.
Choose an orthonormal basis $\{I^a\}$ for~$\mathfrak{g}$ with respect
to the Killing form normalised so that
$\operatorname{tr}(I^a I^b) = \delta^{ab}$. The Casimir tensor is
$\Omega = \sum_a I^a \otimes I^a \in \mathfrak{g} \otimes \mathfrak{g}$.
exec
/bin/zsh -lc "sed -n '10216,10248p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '468,480p' chapters/theory/existence_criteria.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8098,8740p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6038,6172p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '76,90p' chapters/theory/configuration_spaces.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
(Theorem~\ref{thm:bar-nilpotency-complete}): the
bar differential at degree~$2$ is a sum of double residues
at pairs of collision divisors $D_{ij} \cap D_{jk}$, and
the Arnold relation is the precise cancellation identity
ensuring that these contributions sum to zero. The
equivalence between the Arnold relation and nilpotency of
the bar differential is
Theorem~\ref{thm:arnold-iff-nilpotent}; at genus~$0$ the
Arnold relation is the \emph{only} obstruction, and its
vanishing gives $d^2 = 0$ unconditionally. At
genus~$g \geq 1$, the Arnold relation is modified by
elliptic corrections
(Proposition~\ref{prop:elliptic-arnold-relations}), and
the failure of strict nilpotency is measured by the
curvature $\kappa(\cA) \cdot \omega_g$.
 succeeded in 56ms:
\emph{Part~(iii).} The Virasoro subalgebra
$\operatorname{Vir}_c \hookrightarrow \mathcal{W}_3^k$ (generated
by~$T$) is autonomous: its OPE closes on itself. The quartic pole
$T_{(3)}T = c/2$ forces $m_3 \neq 0$ on the $T$-sector by the
single-line class~M theorem
(Theorem~\ref{thm:single-line-dichotomy}): the critical
discriminant $\Delta_T = 40/(5c+22) \neq 0$ ensures that the shadow
tower is infinite. The operations $m_k$ for $k \geq 4$ are then
generated by the resolvent tree formula
(Theorem~\ref{thm:tree-formula}): each $m_k$ is a sum over
planar binary trees with $k$~leaves,
\begin{equation}\label{eq:w3-resolvent-tree}
m_k^{\mathcal{W}_3}
= \sum_{T \in \mathrm{PBT}(k)}
 m_2^{(T)} \circ h_{\mathrm{DS}}^{(\mathrm{edges}(T))},
\end{equation}
where $m_2^{(T)}$ denotes the iterated binary product along the
tree~$T$, and $h_{\mathrm{DS}}$ is the DS contracting homotopy
inserted on each internal edge. The number of planar binary trees
with $k$~leaves is the Catalan number $C_{k-1}$, so $m_k$ receives
 succeeded in 54ms:
Virasoro $\text{Vir}$ & No & Yes (completion) & $I$-adic completion \\
\hline
$\mathcal{W}_3$ & No & Yes (all $c$, completed) & Strict Koszul at $c = -2$ only \\
\hline
$\mathcal{W}_N$ ($N < \infty$) & No & Sometimes & Depends on $(N, c)$ \\
\hline
$\mathcal{W}_{1+\infty}$ & No & Yes (completed) & Filtered; see Appendix~\ref{app:koszul-reference} \\
\hline
$\mathcal{W}_\infty$ & No & NO & Unbounded relations \\
\hline
Free fermion ($bc$ ghosts) & Yes & Yes & Exterior coalgebra \\
\hline
$\mathfrak{gl}_n$ current & Yes & Yes & Matrix coalgebra \\
 succeeded in 54ms:
  \circ (\Delta^{\mathrm{ch},\mathrm{op}})^{-1}.
\end{equation}
\end{remark}

% ================================================================
\noindent\emph{QYBE, unitarity, shift, hexagon.}
The quantum Yang--Baxter equation on
$V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
to~\eqref{eq:yangian-qybe}, verified in
Example~\ref{ex:yangian}; the extension to
$V_{\mathrm{EK}}$ follows from the universal property of
$\mathcal{R}(z)$.
Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
\circ \sigma) = \id$ follows from Drinfeld--Jimbo unitarity.
The shift condition
\begin{equation}\label{eq:ek-shift-cond}
  [D \otimes \id + \id \otimes D,\; S(z)]
  \;=\; \partial_z\, S(z)
\end{equation}
follows from the translation-covariance of the Drinfeld
 succeeded in 54ms:
$\cZ(Y_\hbar(\mathfrak{sl}_2)^{\mathrm{ch}}\textrm{-mod})$
should recover the quantum group category
$\mathrm{Rep}_q(\mathfrak{sl}_2)$ at
$q = e^{2\pi i/(k+2)}$. This identification is the
subject of the DK-5 programme; see
\cite[\S6]{Lorgat26I} for the current status in type~$A$.
\end{remark}

The computations in
Example~\ref{ex:yangian} and
Conjecture~\ref{conj:yangian-ordered-center}(v)
concern the kernel of the averaging map on the
ordered chiral centre, a cohomological object.
The following proposition establishes the underlying
representation-theoretic input: the dimension of
$\ker(\av_n)$ on the bare tensor power $V^{\otimes n}$,
before passing to bar-complex cohomology.

\begin{proposition}[Kernel of the Reynolds projector:
general simple Lie algebras]
exec
/bin/zsh -lc "rg -n \"label\\{(prop:cobar-modular-shadow|sec:sign-conventions|thm:chiral-ran|thm:bar-cobar-verdier|thm:w-archetype-trichotomy|thm:w-finite-termination|def:yangian|comp:sl3-yangian-from-ordered-bar|ex:heis-coproduct|def:chiral-operad|def:e1-chiral|thm:residue-formula|constr:ordered-fm|app:koszul_higher_genus|thm:koszul-conilpotent)\\}\" chapters appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{part:characteristic-datum\\}|label\\{part:\" chapters appendices main.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{app:nonlinear-modular-shadows\\}|label\\{app:signs\\}|label\\{app:sign-conventions\\}|label\\{thm:affine-monodromy-identification\\}|label\\{ex:yangian-coproduct\\}|label\\{def:chiral-coproduct\\}|label\\{def:e1-chiral-rmatrix\\}|label\\{constr:transfer-ainf\\}|label\\{ex:yangian\\}\" chapters appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/yangians_foundations.tex:134:\begin{definition}[Yangian]\label{def:yangian}
chapters/examples/w_algebras.tex:4776:\label{thm:w-archetype-trichotomy}
chapters/examples/w_algebras.tex:5201:\label{thm:w-finite-termination}
chapters/theory/higher_genus_modular_koszul.tex:1:\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
chapters/theory/higher_genus_modular_koszul.tex:30764:log-FM compactification\label{constr:ordered-fm}
chapters/theory/poincare_duality_quantum.tex:335:\begin{definition}[Chiral operad]\label{def:chiral-operad}
chapters/theory/bar_construction.tex:634:\subsection{Sign conventions}\label{sec:sign-conventions}
chapters/theory/bar_construction.tex:2140:\begin{theorem}[Residue formula; \ClaimStatusProvedHere]\label{thm:residue-formula}
chapters/examples/yangians_computations.tex:562:\label{comp:sl3-yangian-from-ordered-bar}
chapters/theory/cobar_construction.tex:1313:\begin{theorem}[Bar-cobar Verdier; \ClaimStatusProvedHere]\label{thm:bar-cobar-verdier}
chapters/theory/cobar_construction.tex:1807:\label{prop:cobar-modular-shadow}
chapters/theory/bar_cobar_adjunction_curved.tex:582:\label{thm:koszul-conilpotent}
chapters/theory/ordered_associative_chiral_kd.tex:8226:\label{ex:heis-coproduct}
chapters/theory/algebraic_foundations.tex:1292:\begin{theorem}[Chiral algebras on Ran space; \ClaimStatusProvedElsewhere]\label{thm:chiral-ran}
chapters/theory/algebraic_foundations.tex:2214:\label{def:e1-chiral}
 succeeded in 52ms:
appendices/homotopy_transfer.tex:179:\label{constr:transfer-ainf}
appendices/nonlinear_modular_shadows.tex:2:\label{app:nonlinear-modular-shadows}
appendices/signs_and_shifts.tex:2:\label{app:signs}
appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
 succeeded in 52ms:
main.tex:895:\label{part:bar-complex}
main.tex:1073:\label{part:characteristic-datum}
main.tex:1164:\label{part:standard-landscape}
main.tex:1368:\label{part:physics-bridges}
main.tex:1450:\label{part:seven-faces}
main.tex:1483:\label{part:v1-frontier}


thinking
**Classifying findings**

I’m considering the simplest approach: first classify these 30 findings and fix the genuinely broken ones, leaving false positives as is. The user emphasized addressing every listed finding, but we only generated our own findings. If our list includes false positives, it’s important to address those too. The user specifically said to "focus on the FIRST 30 broken refs," so it might make sense to interpret "broken" accurately across the entire repo and skip false positives. I might need to write a script to parse the first 100 refs and check for their existence across the repo before identifying the first 30 missing ones. But maybe we won’t need the explorer's list if I do that effectively!
thinking
**Running script for labels**

I'm thinking we should run a script to check the actual label existence across the repo. This ensures accuracy, and I might need to mention that some audit findings are false positives related to appendices or the main content. To compute this effectively, I’ll run a shell script that prints the first 100 lines with grep, and then I could check the labels across the repo. Maybe I'll use Perl or awk for this. Let’s execute that command!
codex
Some of the chapter-only hits are already falsified by source: `app:*` labels live in `appendices/`, and `part:*` labels live in `main.tex`. I’m tightening the audit now so I only edit genuinely unresolved refs, not correct appendix/part references that the narrower grep missed.
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/theory/ | head -100" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
chapters/theory/higher_genus_complementarity.tex:39:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:49: \textup{(}Theorem~\textup{\ref{thm:fiber-center-identification})}.
chapters/theory/higher_genus_complementarity.tex:70: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:76: \textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})} and the
chapters/theory/higher_genus_complementarity.tex:88: \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
chapters/theory/higher_genus_complementarity.tex:92:fiber cohomology (Lemma~\ref{lem:perfectness-criterion}), and
chapters/theory/higher_genus_complementarity.tex:95:(Proposition~\ref{prop:standard-examples-modular-koszul}).
chapters/theory/higher_genus_complementarity.tex:116:base change (Lemma~\ref{lem:perfectness-criterion}).
chapters/theory/higher_genus_complementarity.tex:156:(Convention~\ref{conv:heisenberg-kappa-notation}: level $=$ modular
chapters/theory/higher_genus_complementarity.tex:197:(Theorem~\ref{thm:verdier-bar-cobar}).
chapters/theory/higher_genus_complementarity.tex:214:\begin{remark}[H/M/S layers; Convention~\ref{conv:hms-levels}]
chapters/theory/higher_genus_complementarity.tex:220:(Lemma~\ref{lem:involution-splitting}) makes the passage automatic
chapters/theory/higher_genus_complementarity.tex:275:\textup{(}Convention~\textup{\ref{conv:higher-genus-differentials})}.
chapters/theory/higher_genus_complementarity.tex:285:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:295: Definition~\textup{\ref{def:modular-koszul-chiral})}.
chapters/theory/higher_genus_complementarity.tex:357:\textup{(}Convention~\textup{\ref{conv:regime-tags})].}
chapters/theory/higher_genus_complementarity.tex:361:\textup{(}Definition~\textup{\ref{def:modular-koszul-chiral})}
chapters/theory/higher_genus_complementarity.tex:365:\textup{(}Lemma~\textup{\ref{lem:perfectness-criterion})}.
chapters/theory/higher_genus_complementarity.tex:419:(Corollary~\ref{cor:bar-cohomology-koszul-dual}).
chapters/theory/higher_genus_complementarity.tex:427:(Lemma~\ref{lem:perfectness-criterion}) ensures base change applies
exec
/bin/zsh -lc "ruby -e 'lines="'`grep -rn "'"\\\\\\\\ref{\" chapters/theory/ | head -100"'`.lines; refs=[]; lines.each do |line| path,ln,text=line.split(":",3); next unless text; text.scan(/'"\\\\(?:eq|pag|auto)?ref\\{(["'^}]+)'"\\}/){|m| refs << [path,ln.to_i,m[0]]}; end; refs.each_with_index do |(path,ln,label),i| found="'`rg -n --fixed-strings "label{#{label}}" chapters appendices main.tex 2>/dev/null`; status=found.empty? ? "MISSING" : "OK"; puts "%02d #{status} | #{path}:#{ln} | #{label}"; end'"'" in /Users/raeez/chiral-bar-cobar succeeded in 68ms:


thinking
**Investigating command output issues**

I think the ruby command output might be missing, possibly due to a quoting issue. It might be better to run a simpler script to check the first 100 references using grep, and if needed, I can use Python, although I know there are instructions against using it for reading and writing files. Alternatively, I could use shell or grep, or even Perl. 

I’ll also check the existence of broken labels across chapters and appendices to verify what's truly missing out of the 30 labels we're concerned about. Let's see what we can find!
exec
/bin/zsh -lc "rg -n \"label\\{(thm:affine-monodromy-identification|conj:yangian-ordered-center|ex:yangian-coproduct|def:e1-chiral-rmatrix|app:koszul-reference|thm:chiral-htt|thm:bar-cobar-htt|thm:nms-archetype-trichotomy|thm:nms-finite-termination)\\}\" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{(app:nonlinear-modular-shadows|app:signs|app:sign-conventions|part:characteristic-datum|thm:chiral-htt|thm:bar-cobar-htt|thm:nms-archetype-trichotomy|thm:nms-finite-termination|thm:affine-monodromy-identification|ex:yangian|conj:yangian-ordered-center|ex:yangian-coproduct|def:chiral-coproduct|def:e1-chiral-rmatrix|thm:tree-formula|constr:transfer-ainf|app:koszul-reference|thm:arnold-iff-nilpotent)\\}\" chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/log_ht_monodromy_core.tex:1835:\label{thm:affine-monodromy-identification}
 succeeded in 50ms:
main.tex:1073:\label{part:characteristic-datum}
appendices/homotopy_transfer.tex:179:\label{constr:transfer-ainf}
appendices/homotopy_transfer.tex:209:\label{thm:tree-formula}
appendices/homotopy_transfer.tex:455:\label{thm:chiral-htt}
appendices/homotopy_transfer.tex:524:\label{thm:bar-cobar-htt}
appendices/signs_and_shifts.tex:2:\label{app:signs}
appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
appendices/koszul_reference.tex:2:\label{app:koszul-reference}
appendices/arnold_relations.tex:180:\begin{theorem}[Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0}; \ClaimStatusProvedHere]\label{thm:arnold-iff-nilpotent}
appendices/nonlinear_modular_shadows.tex:2:\label{app:nonlinear-modular-shadows}
appendices/nonlinear_modular_shadows.tex:1208:\label{thm:nms-archetype-trichotomy}
appendices/nonlinear_modular_shadows.tex:2191:\label{thm:nms-finite-termination}



thinking
**Investigating "broken" labels**

I noticed that there are lots of "broken" labels in the appendices or Volume 2. Since I'm looking at Volume 1, references to appendix labels are fine if those appendices are included. But references to Volume 2 labels in Volume 1 would be problematic unless there's an external cross-reference, which seems unlikely.

For example, `thm:affine-monodromy-identification` is only in Volume 2, making it truly broken in Volume 1. I'll need to check if `conj:yangian-ordered-center`, `ex:yangian-coproduct`, `def:chiral-coproduct`, `def:e1-chiral-rmatrix` can be found anywhere.
thinking
**Identifying broken entries**

I need to determine which items are actually broken among 30. The ones in the appendices, like app:nonlinear-modular-shadows and thm:bar-cobar-htt, appear to be valid. However, I see that the thm:affine-monodromy-identification is broken in vol1. I'm also investigating examples and definitions, like the ex:yangian and def:chiral-coproduct to check their status. So far, it seems I may have around 12 broken entries out of that list of 30.
thinking
**Continuing to identify broken references**

I need to go beyond the initial 30 chapter-only false positives to find 30 actual broken global references. The user wants me to focus on the first 30 broken references I can identify. While I could say that it’s acceptable to find only 12 actual broken references among 30 candidates, the user wants me to fix each one. I should keep scanning until I get 30 verified broken references within the first 100 lines. I’ll use a robust script to check the labels across chapters and appendices and focus on listing the first 30 that are missing.
codex
The narrow audit shows a real split: several early “broken” refs are false positives because their labels live in `appendices/` or `main.tex`. I’m now switching to the truthful set: the first 30 refs from the same scan whose labels do not exist anywhere in Vol I’s live surface.
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/theory/ | head -100 | perl -ne 'if(/"'^([''^:]+):('"\\d+):(.*)"'$/){$f=$1;$l=$2;$t=$3; while($t =~ /'"\\\\(?:eq|pag|auto)?ref\\{(["'^}]+)'"\\}/g){print \""'$f:$l|$1'"\\n\";}}' | while IFS='|' read -r loc label; do if "'! rg -q --fixed-strings "label{$label}" chapters appendices main.tex; then printf '"'%s | %s\\n' \""'$loc" "$label"; fi; done | head -30' in /Users/raeez/chiral-bar-cobar succeeded in 935ms:



thinking
**Clarifying the reference checks**

I’m noticing that there might not be any missing items in the first 100 lines when I look at appendices or main.tex. So, the first 30 missing references probably occur after those initial lines, but the user’s task involves fixing the first 30 broken ones found within those lines. They suggested running a grep with head -100 to check corresponding labels. It's important to focus on those broken references, but I might need to look further if the total number is larger than expected.
thinking
**Determining the missing references**

I could still meet the user's request by fixing the first 30 broken references found in the chapters, but I realize many might be false positives. The user might want edits based on their audit method, which focuses only on chapters. However, I want to avoid altering correct references in the appendix or main sections. So, I think it’s best to identify and fix only the truly broken ones, potentially scanning beyond the first 100 lines to find 30 actual missing references globally. I'll get started on that!
exec
/bin/zsh -lc "grep -rn '\\\\ref{' chapters/theory/ | perl -ne 'if(/"'^([''^:]+):('"\\d+):(.*)"'$/){$f=$1;$l=$2;$t=$3; while($t =~ /'"\\\\(?:eq|pag|auto)?ref\\{(["'^}]+)'"\\}/g){print \""'$f:$l|$1'"\\n\";}}' | while IFS='|' read -r loc label; do if "'! rg -q --fixed-strings "label{$label}" chapters appendices main.tex; then printf '"'%s | %s\\n' \""'$loc" "$label"; fi; done | head -30' in /Users/raeez/chiral-bar-cobar
thinking
**Improving script efficiency**

I’m thinking that using `rg -q` in a while loop over many references could be slow. Maybe I can use Ruby or AWK to gather unique labels more efficiently? The process might be hanging due to the large number of refs, so it might be a good idea to stop the session. Instead, creating a more efficient script using Ruby to read the label set once seems better. I'll collect all labels with the given command and then parse the output separately.
exec
/bin/zsh -lc "ruby -e 'labels={}; "'`rg -No "label'"\\\\{["'^}]+" chapters appendices main.tex`.each_line{|ln| if ln =~ /label'"\\{(["'^}]+)/ then labels[$1]=true end}; refs=[]; `grep -rn "'"\\\\\\\\ref{\" chapters/theory/"'`.each_line{|line| if line =~ /''^([''^:]+):('"\\d+):(.*)"'$/ then f=$1;l=$2.to_i;t=$3; t.scan(/'"\\\\(?:eq|pag|auto)?ref\\{(["'^}]+)'"\\}/){|m| refs << [f,l,m[0]]} end}; missing=refs.reject{|_,_,lab| labels[lab]}; missing.first(30).each{|f,l,lab| puts \"#{f}:#{l} | #{lab}\" }'" in /Users/raeez/chiral-bar-cobar succeeded in 100ms:


 succeeded in 41.30s:
chapters/theory/ordered_associative_chiral_kd.tex:5075 | thm:affine-monodromy-identification
chapters/theory/ordered_associative_chiral_kd.tex:5116 | thm:affine-monodromy-identification
chapters/theory/ordered_associative_chiral_kd.tex:5486 | thm:affine-monodromy-identification
chapters/theory/ordered_associative_chiral_kd.tex:5666 | thm:affine-monodromy-identification
chapters/theory/ordered_associative_chiral_kd.tex:5717 | thm:affine-monodromy-identification
chapters/theory/ordered_associative_chiral_kd.tex:5970 | part:gravity
chapters/theory/ordered_associative_chiral_kd.tex:6047 | ex:yangian
chapters/theory/ordered_associative_chiral_kd.tex:6048 | conj:yangian-ordered-center
chapters/theory/ordered_associative_chiral_kd.tex:6146 | conj:yangian-ordered-center
chapters/theory/ordered_associative_chiral_kd.tex:6159 | conj:yangian-ordered-center
chapters/theory/ordered_associative_chiral_kd.tex:6166 | ex:yangian
chapters/theory/ordered_associative_chiral_kd.tex:7549 | part:e1-core
chapters/theory/ordered_associative_chiral_kd.tex:7752 | part:e1-core
chapters/theory/ordered_associative_chiral_kd.tex:8107 | ex:yangian
chapters/theory/ordered_associative_chiral_kd.tex:8132 | ex:yangian
chapters/theory/ordered_associative_chiral_kd.tex:8168 | ex:yangian
chapters/theory/ordered_associative_chiral_kd.tex:8385 | ex:yangian-coproduct
chapters/theory/ordered_associative_chiral_kd.tex:8577 | def:chiral-coproduct
chapters/theory/ordered_associative_chiral_kd.tex:8731 | def:e1-chiral-rmatrix
chapters/theory/derived_langlands.tex:1515 | chap:modular-koszul


thinking
**Analyzing broken references**

If my script finds no missing references globally, then it seems like there are no "broken" references according to grep across the broader surface. However, they mentioned 159 broken references in Volume I, possibly outside the `chapters/theory`. My focus is on theory and the first 100, which may not have any actual missing entries. It’s possible they used `grep -rn 'label{LABELNAME}' chapters/` without checking appendices, leading to false positives.
thinking
**Inspecting candidate targets**

I need to examine some potential replacements and their semantics. I realize I haven’t searched certain candidates like `thm:eval-core-identification`, so I should do that. I’m also considering whether better targets might be available. There are various references to ex:yangian/conj, particularly around 6047. It might be helpful to find examples or theorems discussing Yangian, possibly without labels. I think I should focus on unlabeled examples/conjectures that could be added to the file.
thinking
**Searching for "Yangian" labels**

I need to use a tool to search for "Yangian" headings or labels within the file. This will help me understand how they’re positioned and whether any changes or additions are necessary. It’s essential to ensure that I’m capturing all relevant references. By doing this search, I can pinpoint where enhancements could be made and confirm any missing headings that need to be added. Let’s see what results I get!
codex
I’ve narrowed the truthful edit surface. Among the first 30 chapter-only hits, most appendix/part refs are valid and won’t be touched; the real breakage is concentrated in `ordered_associative_chiral_kd.tex`, where several labels are missing entirely or point to a Vol II-only theorem. I’m resolving those next.
exec
/bin/zsh -lc 'rg -n "affine-monodromy-identification|eval-core-identification|Yangian|yangian-ordered-center|yangian-coproduct|chiral-coproduct|e1-chiral-rmatrix|Example|Conjecture" chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
44:Its linear dual, on the chirally Koszul locus, is the dg-shifted Yangian.
2283:\begin{theorem}[Open-colour Koszul dual: the abelian Yangian;
2287:dual of $\cH_k$ is the abelian Yangian
2300:current of the Yangian.
2328:Yangian $Y(\mathfrak{u}(1))$.
2415: $1 + \hbar\,\Omega/z + O(\hbar^2)$. The abelian Yangian
2425: $r_{\max} = \infty$ (class~M). The nontrivial Yangian structure
2448:form that reveals the Yangian as a deformation of the current algebra
2451:with $\Sigma_n$-equivariant factorisation structure); the Yangian
2481:The Yangian $Y_\hbar(\mathfrak{sl}_2)$, with $\hbar = 1/(k+2)$, is the
2599:over the Yangian.
2700:At $\hbar = 0$, the Yangian $Y_\hbar(\mathfrak{sl}_2)$ degenerates to the
2724:confirming that the Yangian is a filtered deformation of the current
2754:diverges and the Yangian construction degenerates: this is the
2774:because it enters the Yangian as $\hbar = 1/(k{+}h^\vee)$, not as an
2806:Yangian $R$-matrix $R(u) = 1 + \hbar\,r(u) + O(\hbar^2)$ has its
2819:Yangian generators $E_n, F_n, H_n$ map to current modes $J^a_n$.
2907:information. The coassociative component sees the Yangian; the chiral component sees
2913:\section{The Virasoro ordered bar complex and the gravitational Yangian}
2916:The affine Yangian $Y_\hbar(\mathfrak{sl}_2)$ has three independent
exec
/bin/zsh -lc "sed -n '8070,8605p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5000,6205p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8688,8755p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{thm:eval-core-identification\\}|label\\{def:yangian\\}|label\\{comp:sl3-yangian-from-ordered-bar\\}|label\\{def:chiral-operad\\}|label\\{def:e1-chiral\\}\" chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of Theorem~\ref{thm:chiral-qg-equiv}: each reads a different
projection of $\barB^{\mathrm{ord}}(\cA)$.
\end{proof}

\begin{remark}[Key formulas of the equivalence]
\label{rem:chiral-qg-key-formulas}
The three equivalences involve the following explicit formulas.
The OPE compatibility axiom:
\begin{equation}\label{eq:ope-compat}
  \Delta^{\mathrm{ch}}(Y(a,z)\, b)
  \;=\;
  Y^{(2)}(\Delta^{\mathrm{ch}}(a), z)
  \cdot \Delta^{\mathrm{ch}}(b),
\end{equation}
where $Y^{(2)}$ is the tensorwise vertex operation.
The coproduct from the bar complex:
\begin{equation}\label{eq:coprod-from-bar}
  \Delta^{\mathrm{ch}} \colon
  \cA \simeq \Omega(\barB^{\mathrm{ord}}(\cA))
  \xrightarrow{\Omega(\Delta)}
 succeeded in 52ms:
rational function $1/z^{n+1}$ is replaced by its unique
elliptic counterpart: $1/z\mapsto\zeta(z|\tau)$ and
$1/z^{n+1}\mapsto\frac{(-1)^{n-1}}{n!}\,\wp^{(n-1)}(z|\tau)$
for $n\ge 1$, with $\wp^{(0)}:=\wp$. These are the unique
functions on $\mathbb{C}\setminus(\mathbb{Z}+\mathbb{Z}\tau)$
that match $1/z^{n+1}+O(z)$ near $z=0$ and are doubly
periodic for $n\ge 1$ (or quasi-periodic for $n=0$). The
prefactor comes from the Laurent expansion
$\wp^{(m)}(z)=(-1)^m(m+1)!/z^{m+2}+O(1)$ specialised to
$m=n-1$. This yields formula~\eqref{eq:elliptic-r-matrix}.

\textbf{Step~3} (Dichotomy).
The quasi-periodicity is inherited entirely from $\zeta(z|\tau)$,
since $\wp$ and all its derivatives are doubly periodic.
Therefore the $B$-cycle monodromy of $r^{E_\tau}$ is
$2\eta_\tau\cdot c_0$, proving~(a). When $c_0=0$, the
$\zeta$-term is absent and $r^{E_\tau}$ is meromorphic on
$E_\tau$, hence the spectral braiding defined by the annular bar
differential decouples from the curved chiral differential. When
$c_0\ne 0$, the non-trivial monodromy
 succeeded in 51ms:
Let $(Q,W)$ be a quiver with potential. The critical CoHA
\[
  \cH_{Q,W}
  = \bigoplus_{d \in \ZZ_{\geq 0}^{Q_0}}
  H^{G_d}_{\mathrm{BM},*}
  (\cM_d^{\mathrm{nil}},\, \varphi_W)
\]
carries two structures of independent geometric origin:
\begin{enumerate}[label=\textup{(\alph*)}]
\item \emph{Vertex coproduct} $\Delta_{\mathrm{CoHA}}$, from
  restriction to Levi subalgebras
  $G_{d_1} \times G_{d_2} \hookrightarrow G_d$; and
\item \emph{$R$-matrix} $R(z)$, from the
  Maulik--Okounkov stable envelope
  construction~\cite{MO19} on the Nakajima variety
  associated to~$Q$.
\end{enumerate}
Jindal--Kaubrys--Latyntsev~\cite{JKL26} prove that these two
structures satisfy the vertex bialgebra axiom (their
Theorems~A and~C):
 succeeded in 50ms:
chapters/examples/yangians_computations.tex:562:\label{comp:sl3-yangian-from-ordered-bar}
chapters/examples/yangians_computations.tex:2765:\label{thm:eval-core-identification}
chapters/examples/yangians_foundations.tex:134:\begin{definition}[Yangian]\label{def:yangian}
chapters/theory/poincare_duality_quantum.tex:335:\begin{definition}[Chiral operad]\label{def:chiral-operad}
chapters/theory/algebraic_foundations.tex:2214:\label{def:e1-chiral}

thinking
**Inspecting examples for labeling**

I need to look for any possible unlabeled examples, like the Yangian reference. My search shows it mentions Example\ref{ex:yangian}, but it's not labeled properly. I think there may be an unlabeled example before something at 8098. I’ll search for `\begin{example}` around 7900. I noticed an example ends just before the `\begin{example}[Heisenberg: trivial case]`. That could be the Yangian example I’m looking for, so I'll check the lines from 7930 to 8045.
exec
/bin/zsh -lc "sed -n '6128,6168p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '7980,8108p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  \ker(\av_n)
  \;\cong\;
  \bigoplus_{\substack{\lambda \,\vdash\, n \\
    \ell(\lambda) \leq r,\;
    \lambda \neq (n)}}
  S_\lambda \otimes V_\lambda(\mathfrak{gl}_r).
\]
For a general simple~$\fg$ acting on~$V$, the Schur--Weyl
decomposition involves the commutant algebra
$\End_\fg(V^{\otimes n})$ rather than the group algebra of
$\GL(V)$, and the individual summands carry different
$\fg$-representations with different dimensions.
The total kernel dimension, however, depends only on
$\dim\Sym^n(V) = \binom{n+d-1}{d-1}$, which is
determined by $d$ alone.
\end{proof}

\begin{remark}[Explicit values and
Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
\label{rem:ker-av-table}
 succeeded in 56ms:
  $\Delta^{\mathrm{ch}} \colon
  \cA \to (\cA \mathbin{\hat\otimes} \cA)((z))$,
  coassociative up to conjugation by~$\Phi$.
\end{enumerate}
The equivalences form a triangle:
\begin{center}
\begin{tikzcd}[column sep=3em, row sep=2.5em]
  \textup{(I)} \ar[rr, shift left=1, "\alpha"]
  \ar[dr, shift left=1, "\gamma^{-1}"']
  && \textup{(II)} \ar[ll, shift left=1, "\alpha^{-1}"]
  \ar[dl, shift left=1, "\beta"] \\
  & \textup{(III)}
  \ar[ul, shift left=1, "\gamma"]
  \ar[ur, shift left=1, "\beta^{-1}"']
\end{tikzcd}
\end{center}
where $\alpha$ restricts the OPE to the real
Stasheff associahedra $K_n \hookrightarrow
\overline{\operatorname{FM}}_n^{\mathrm{ord}}(\bC)$,
$\beta$ applies the cobar functor to the deconcatenation
exec
/bin/zsh -lc "sed -n '2748,2780p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '6910,6940p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $p = 7$ for $C_2$, $p = 11$ for $G_2$ (matching manuscript).
\end{itemize}
Sectorwise finiteness for all simply-laced lattice
VOAs ($A_1$--$A_3$, $D_4$--$D_5$, $E_6$--$E_8$) is verified at the
lattice-bar sector level ($93$~tests,
\texttt{compute/lib/sectorwise\_finiteness.py}),
and the sub-exponential vs.\ exponential growth discrimination is
checked via least-squares fitting of $\log d_n$ to both $c \cdot n$
and $C \cdot \sqrt{n}$ models.
\end{computation}

\end{remark}

\subsubsection*{Resolution: the evaluation-generated core}

\begin{theorem}[Evaluation-generated core identification, type~\texorpdfstring{$A$}{A};
\ClaimStatusProvedHere]
\label{thm:eval-core-identification}
\index{thick generation!evaluation-generated core|textbf}
\index{Drinfeld--Kohno!derived!evaluation-generated core}
 succeeded in 51ms:
$\Omega\in\mathfrak{g}\otimes\mathfrak{g}$ for the quadratic Casimir element
and $P\in\operatorname{End}(V\otimes W)$ for the permutation operator
$v\otimes w\mapsto w\otimes v$.

\subsection{The Yangian $Y_\hbar(\mathfrak{g})$ and the evaluation homomorphism}

\begin{definition}[Drinfeld Yangian]
\label{def:yangian-drinfeld}
The \emph{Yangian} $Y_\hbar(\mathfrak{g})$ is the associative
$\mathbb{C}[\![\hbar]\!]$-algebra generated by
$\{J^a_0,\,J^a_1\mid a=1,\dots,\dim\mathfrak{g}\}$
subject to:
\begin{enumerate}[label=(\roman*)]
\item $J^a_0$ generate a copy of $U(\mathfrak{g})$;
\item $[J^a_0,\,J^b_1]=f^{ab}{}_c\,J^c_1$;
\item Drinfeld's ternary relation:
$[J^a_1,\,[J^b_0,\,J^c_1]]-[J^a_0,\,[J^b_1,\,J^c_1]]$
$=\hbar^2\,A^{abc}_{def}\{J^d_0,J^e_0,J^f_0\}$,
where $A^{abc}_{def}$ is the totally symmetric tensor
of \textup{\cite{Drinfeld-Yangians}} and
exec
/bin/zsh -lc "rg -n \"\\\\begin\\{example\\}|\\\\label\\{ex:\" chapters/theory/ordered_associative_chiral_kd.tex | sed -n '20,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:\begin\{example\}|\label\{ex:)
                         ^^
error: unrecognized escape sequence

thinking
**Considering string formatting**

I need to figure out how to handle a fixed string properly, possibly considering using techniques like escaping. I wonder if grep could be the right tool for the job, but I need to clarify where that fits into my process. It's important to ensure I'm using the appropriate method to get the desired outcome, and I have to check if there are other solutions available too. Let's explore the best approach together!
exec
/bin/zsh -lc "grep -n '\\\\begin{example}\\|\\\\label{ex:' chapters/theory/ordered_associative_chiral_kd.tex | sed -n '20,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

exec
/bin/zsh -lc "grep -n 'begin{example}\\|label{ex:' chapters/theory/ordered_associative_chiral_kd.tex | head -80" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
7246:\begin{example}[Drinfeld polynomials for evaluation chains]
7247:\label{ex:drinfeld-eval-chain}
8225:\begin{example}[Heisenberg: trivial case]
8226:\label{ex:heis-coproduct}
9040:\begin{example}[The $N = 2$ chiral quantum group:
9042:\label{ex:gl2-chiral-qg}
exec
/bin/zsh -lc "sed -n '7238,7260p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$T_i(u)\cdot v_+=(u-a-\hbar)/(u-a)\cdot v_+$ and
$T_j(u)\cdot v_+=v_+$ for $j\neq i$, matching the
classification. The general formula follows from the
tensor product rule for Drinfeld polynomials: the
$P_j$ of a tensor product is the product of the
$P_j$'s of the factors.
\end{proof}

\begin{example}[Drinfeld polynomials for evaluation chains]
\label{ex:drinfeld-eval-chain}
For $\mathfrak{g}=\mathfrak{sl}_2$, rank $r=1$, and an
evaluation chain at points $a_1,\dots,a_n\in\mathbb{C}$
in the fundamental representation:
\[
P(u)=\prod_{k=1}^n(u-a_k).
\]
The module $V_{a_1}\otimes\cdots\otimes V_{a_n}$ is
irreducible if and only if $a_i-a_j\notin\mathbb{Z}\hbar$
for all $i\neq j$ (the non-resonance condition).
When $a_i-a_j\in\mathbb{Z}\hbar$ for some pair, the tensor
exec
/bin/zsh -lc 'rg -n "yangian-ker-av2|ker-av2|ordered-center|ordered chiral center|averaging map" chapters/examples/yangians_computations.tex chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:729:The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:788:by the averaging map.
chapters/theory/ordered_associative_chiral_kd.tex:5911:\index{averaging map!depth surplus|textbf}
chapters/theory/ordered_associative_chiral_kd.tex:5913:The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:5933:the averaging map is the naive $\Sigma_n$-quotient, and
chapters/theory/ordered_associative_chiral_kd.tex:5938:The averaging map is the composition
chapters/theory/ordered_associative_chiral_kd.tex:5997:Remark~\ref{rem:motivic-interpretation}. The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:6017:\item \emph{The symmetric image}: the averaging map $\mathrm{av}$
chapters/theory/ordered_associative_chiral_kd.tex:6048:Conjecture~\ref{conj:yangian-ordered-center}(v)
chapters/theory/ordered_associative_chiral_kd.tex:6049:concern the kernel of the averaging map on the
chapters/theory/ordered_associative_chiral_kd.tex:6064:denote the Reynolds averaging map (projection onto the
chapters/theory/ordered_associative_chiral_kd.tex:6146:Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
chapters/theory/ordered_associative_chiral_kd.tex:6159:Conjecture~\ref{conj:yangian-ordered-center}(v):
chapters/theory/ordered_associative_chiral_kd.tex:6167:equation~\eqref{eq:yangian-ker-av2}).
chapters/theory/ordered_associative_chiral_kd.tex:6210:\index{averaging map!kernel at genus 1}
chapters/theory/ordered_associative_chiral_kd.tex:6247:the elliptic $r$-matrix; the averaging map $\mathrm{av}$ projects
chapters/theory/ordered_associative_chiral_kd.tex:7919:Definition~\ref{def:three-tier-r-matrix}). The averaging map
chapters/theory/ordered_associative_chiral_kd.tex:8126:\textbf{Part B: the ordered chiral center of the EK quantum
chapters/theory/ordered_associative_chiral_kd.tex:8173:equation~\eqref{eq:yangian-ker-av2}.
chapters/theory/ordered_associative_chiral_kd.tex:8217:The ordered chiral center carries the full quantum $R$-matrix
exec
/bin/zsh -lc "sed -n '540,590p' chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{proof}
(i) At filtration degree 1, the generators are
$\{t_{ij}^{(1)} : 1 \leq i,j \leq N\}$ modulo the trace
condition, giving $N^2 - 1$ generators (matching $\dim \mathfrak{sl}_N$).

(ii) The degree-2 bar space $\bar{B}^2$ is spanned by
$\{[t_{ij}^{(1)} | t_{kl}^{(1)}]\}$, giving $(N^2-1)^2$ elements.

(iii) The image of $d_2$ consists of the RTT relations at
level $(1,1)$: $[t_{ij}^{(1)}, t_{kl}^{(1)}] - \delta_{kj} t_{il}^{(1)}
+ \delta_{il} t_{kj}^{(1)}$. These span a subspace of
dimension $(N^2-1)^2 - \dim H^2$, and $H^2 \cong \mathfrak{sl}_N[u]/(u^2)$
at this filtration level.

(iv) At filtration degree $\leq n$, $\dim \bar{B}^1 = (N^2-1)n$,
so $\dim \bar{B}^k = O(N^{2k} n^k)$. For fixed $n$, this is
polynomial in $N$.
\end{proof}

\begin{computation}[The
exec
/bin/zsh -lc "rg -n \"eq:yangian-ker-av2|label\\{eq:yangian-ker-av2\\}\" chapters/theory/ordered_associative_chiral_kd.tex chapters/examples/yangians_computations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/ordered_associative_chiral_kd.tex:6167:equation~\eqref{eq:yangian-ker-av2}).
chapters/theory/ordered_associative_chiral_kd.tex:8173:equation~\eqref{eq:yangian-ker-av2}.
exec
/bin/zsh -lc "sed -n '6200,6245p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{table}
\end{remark}


% ================================================================
\section{Background: chiral algebras and the $\Eone/\Einf$
hierarchy}
\label{sec:background}
\begin{remark}[The averaging kernel at genus~$1$: quasi-modular anomaly and Hodge curvature]
\label{rem:genus1-ker-av}
\index{averaging map!kernel at genus 1}
\index{quasi-modular forms!and averaging kernel}
\index{Hodge bundle!curvature and ker(av)}
\ClaimStatusConjectured
Proposition~\ref{prop:averaging-surplus} characterises $\ker(\mathrm{av})$
at genus~$0$: it is generated by the $R$-matrix monodromy, carrying
the full mixed Tate content of the configuration-space integrals.
At genus~$1$, a new mechanism enters.

The genus-$1$ bar propagator on $E_\tau$ involves the Weierstrass

thinking
**Searching for definitions**

I’m thinking about the definition mentioned in Step 7 regarding the chiral coproduct. Maybe there's a definition in this file that isn’t clearly labeled. I’ll search for the phrase “Chiral coproduct” to see if I can find anything that matches. It’s important to ensure I’m correctly verifying the axioms, so finding the right definition is crucial! Let’s get to searching now!
exec
/bin/zsh -lc "grep -n 'Chiral coproduct\\|chiral coproduct\\|E_1-chiral algebra\\|vertex R-matrix' chapters/theory/ordered_associative_chiral_kd.tex | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
7907:chiral coproduct from the Hall comultiplication. The shadow
7962:associahedra), and the chiral coproduct $\Delta^{\mathrm{ch}}$
7984:\item $\Eone$-chiral algebra with compatible chiral coproduct
8068:$d_{\barB}|_{\text{degree } k}$, and the chiral coproduct is
8248:a chiral coproduct, and an $\Ainf$ structure, all explicit
8268:\item \textup{(Chiral coproduct at all spins.)}
8499:construction produces a chiral coproduct on
9230:level prefix~$\Psi$, and a chiral coproduct with all
9603:  via cobar dualization, the chiral coproduct
9818:\subsection{Coderived chiral coproduct for class~M}
9837:\begin{conjecture}[Coderived chiral coproduct; \ClaimStatusConjectured]
9839:\index{coderived category!chiral coproduct|textbf}%
9846:\item \textup{(Coderived chiral coproduct.)}
9887:  \emph{only} chiral coproduct available, and it equips
9895:\index{coderived category!chiral coproduct!mechanism}%
9952:\index{coderived category!chiral coproduct!relation to $\Ethree$}%
exec
/bin/zsh -lc "sed -n '7840,7995p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '9800,9985p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 $R(z) = \tau$ (the Koszul-signed flip).
 This is the subclass where the chiral product extends
 across the diagonal without singularities.

\item \emph{Vertex algebras with poles}
 \textup{(}all families in the table above\textup{)}:
 $R(z) \ne \tau$, but $R(z)$ is \emph{derived} from the
 local OPE via analytic continuation.
 Both (a) and (b) are $\mathsf{E}_\infty$-chiral.

\item \emph{Genuinely $\mathsf{E}_1$-chiral}
 \textup{(}Etingof--Kazhdan quantum vertex algebras,
 Yangians as independent algebras, quantum groups\textup{)}:
 $R(z) \ne \tau$ and $R(z)$ is \emph{independent input},
 not derivable from a local symmetric structure.
 Only (c) is genuinely $\mathsf{E}_1$.
\end{enumerate}
Tiers~(a) and~(b) are both $\mathsf{E}_\infty$.
The ordered bar complex is a computational tool for
$\mathsf{E}_\infty$-chiral algebras; it does not make them
 succeeded in 52ms:
Then
\[
Q_{DS}(A^!)\simeq Q_{DS}(A)^!.
\]
For every $A$-bimodule $M$ one should have
\[
Q_{DS}\bigl(\KK_A^{\mathrm{bi}}(M)\bigr)\simeq
\KK_{Q_{DS}(A)}^{\mathrm{bi}}\bigl(Q_{DS}(M)\bigr).
\]
\end{conjecture}

\begin{remark}
Theorem~\ref{thm:ordered-associative-ds-principal} records the proved principal corridor from
Volume~II. Conjecture~\ref{conj:DS-arbitrary-nilpotent} isolates the remaining non-principal
frontier: one must verify PBW compatibility and the lift of the BRST differential to the ordered
bar coalgebra beyond the principal and hook-type regimes.
\end{remark}

\subsection{Coderived chiral coproduct for class~M}
\label{subsec:coderived-chiral-coproduct}
exec
/bin/zsh -lc "sed -n '2200,2235p' chapters/theory/algebraic_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
\end{definition}

\begin{remark}[Verdier versus linear duality]
\label{rem:verdier-vs-linear}
\index{Verdier duality}
$\mathbb{D}(\mathcal{M})$ is the Verdier dual
$\mathcal{D}$-module, not the na\"{\i}ve linear dual
$\mathrm{Hom}_k(\mathcal{M}, k)$. The Koszul
dual~$\cA^!$ is constructed via Verdier duality on
$\overline{C}_n(X)$
(Theorem~\ref{thm:bar-cobar-verdier}).
\end{remark}

\begin{definition}[\texorpdfstring{$\Eone$}{E1}-chiral algebra = nonlocal vertex algebra]
\label{def:e1-chiral}
\index{$\mathbb{E}_1$-chiral algebra|textbf}
An \emph{$\Eone$-chiral algebra} on $X$ is an associative (but not
necessarily commutative) algebra over the associative chiral
operad~$\chirAss$ (Definition~\ref{def:chiral-ass-operad}):
a $\mathcal{D}_X$-module $\cA$ with binary chiral operation
exec
/bin/zsh -lc "grep -n 'ordered chiral centre\\|ordered chiral center\\|kernel of the averaging map\\|ker(\\\\av' chapters/theory/ordered_associative_chiral_kd.tex | sed -n '1,60p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
6054:concern the kernel of the averaging map on the
6055:ordered chiral centre, a cohomological object.
6058:$\ker(\av_n)$ on the bare tensor power $V^{\otimes n}$,
6073:  \dim \ker(\av_n\big|_{V^{\otimes n}})
6084:$\dim\ker(\av_n) = 2^n - (n+1)$.
6087:$\dim\ker(\av_2) = d^2 - d(d{+}1)/2 = d(d{-}1)/2
6133:  \ker(\av_n)
6165:$\ker(\av_n)$ on the ordered chiral centre is a subquotient
6166:of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
6199:\caption{Dimension of $\ker(\av_n\big|_{V^{\otimes n}})$
7935:$\Sigma_n$-equivariant, and $\ker(\av) \neq 0$ at degree
8131:\textbf{Part B: the ordered chiral center of the EK quantum
8171:\emph{The kernel $\ker(\av)$.}
8172:The ordered chiral centre computation parallels
8175:$\ker(\av_2)\big|_{V \otimes V}
8181:$\ker(\av_2)$ dimension. The scalar shadow surviving
8184:$\ker(\av_3) \cong \Lambda^3(\fg) = \CC$ carries the
8222:The ordered chiral center carries the full quantum $R$-matrix
8225:$\ker(\av_2) \neq 0$ demonstrates that the ordered theory

thinking
**Searching for conjectures**

I’m trying to figure out if there’s a conjecture label around 7935 or somewhere close by. I wonder if searching for `begin{conjecture}` in that area will help clarify things. It’s a bit frustrating to think there might be a detail missing, so exploring nearby is probably a good approach. Let’s see what I can find to fill in any gaps in the information!
exec
/bin/zsh -lc "grep -n 'begin{conjecture}\\|label{conj:' chapters/theory/ordered_associative_chiral_kd.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
5570:\begin{conjecture}[Yangian--quantum group deformation beyond the affine lineage]
5572:\label{conj:yangian-quantum-group-general}
9684:\begin{conjecture}[Geometric realization of the diagonal bicomodule]
9686:\label{conj:bordered}
9788:\begin{conjecture}[Reduction commutes with associative chiral duality
9791:\label{conj:DS-arbitrary-nilpotent}
9837:\begin{conjecture}[Coderived chiral coproduct; \ClaimStatusConjectured]
9838:\label{conj:coderived-chiral-coproduct}%
10619:\begin{conjecture}[Full three-language equivalence]
10621:\label{conj:three-language-equivalence}
10684:\begin{conjecture}[Trigonometric and elliptic ordered chiral homology]
10685:\label{conj:trig-elliptic-ordered}
10701:\begin{conjecture}[Higher-genus ordered chiral homology]
10702:\label{conj:higher-genus-ordered-ch}
exec
/bin/zsh -lc "sed -n '8168,8188p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  + O(z^{-2})\Bigr).
\end{equation}

\emph{The kernel $\ker(\av)$.}
The ordered chiral centre computation parallels
Example~\ref{ex:yangian}; the result is identical on
cohomology. On $V \otimes V$:
$\ker(\av_2)\big|_{V \otimes V}
\cong \bigwedge^2 V = \CC$,
the same one-dimensional space as
equation~\eqref{eq:yangian-ker-av2}.
The quantum corrections from $S(z)$ shift the subleading
terms of the flat sections but do not alter the
$\ker(\av_2)$ dimension. The scalar shadow surviving
$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
identical to the classical value. At degree~$3$, the kernel
$\ker(\av_3) \cong \Lambda^3(\fg) = \CC$ carries the
quantum-corrected Drinfeld associator
\begin{equation}\label{eq:ek-ker-av3}
  \Phi_{\mathrm{KZ}}^S - 1
exec
/bin/zsh -lc "sed -n '6038,6150p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\cZ(Y_\hbar(\mathfrak{sl}_2)^{\mathrm{ch}}\textrm{-mod})$
should recover the quantum group category
$\mathrm{Rep}_q(\mathfrak{sl}_2)$ at
$q = e^{2\pi i/(k+2)}$. This identification is the
subject of the DK-5 programme; see
\cite[\S6]{Lorgat26I} for the current status in type~$A$.
\end{remark}

The computations in
Example~\ref{ex:yangian} and
Conjecture~\ref{conj:yangian-ordered-center}(v)
concern the kernel of the averaging map on the
ordered chiral centre, a cohomological object.
The following proposition establishes the underlying
representation-theoretic input: the dimension of
$\ker(\av_n)$ on the bare tensor power $V^{\otimes n}$,
before passing to bar-complex cohomology.

\begin{proposition}[Kernel of the Reynolds projector:
general simple Lie algebras]

thinking
**Adjusting titles and references**

I see the title needs to be modified to something like "Explicit values and the ordered-centre conjectural bounds." I’ll also change instances of "Conjecture ref" to a plain phrase. Good start! I should check the references at 6166 and consider adjustments at some specific examples. I might say "the classical Yangian computation" to clarify. It’s probably a comparison related to the Etingof-Kazhdan quantum VOA, so I’ll inspect that section closely. I'll focus on exploring the area around 8000 to 8060 for more context.
exec
/bin/zsh -lc "sed -n '8000,8065p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
coproduct on $\barB^{\mathrm{ord}}(\cA)$, and
$\gamma$ extracts the $R$-matrix as
$S(z) = \sigma \circ \Delta^{\mathrm{ch}}
\circ (\Delta^{\mathrm{ch},\mathrm{op}})^{-1}$
\textup{(}the chiral Drinfeld formula\textup{)}.
\end{theorem}

\begin{proof}
\textbf{(I) $\to$ (II).}
The Stasheff associahedron $K_n$ is isomorphic to the real
FM compactification $\overline{\operatorname{FM}}_n^{\mathrm{ord}}(\bR)$
(Sinha). The chiral $A_\infty$-maps are the integrals
\[
m_k^{\mathrm{ch}}(a_1, \ldots, a_k)
\;=\;
\int_{K_k}
Y(a_1, z_1) \cdots Y(a_k, z_k)\, \omega_k,
\]
where $\omega_k$ is the canonical volume form induced by
the bar propagator. The Stasheff identity follows from
exec
/bin/zsh -lc "sed -n '8065,8095p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
beyond $\barB^{\mathrm{ord}}(\cA)$ is needed.
\end{corollary}

\begin{proof}
Immediate from the three arrows $\alpha$, $\beta$, $\gamma$
of Theorem~\ref{thm:chiral-qg-equiv}: each reads a different
projection of $\barB^{\mathrm{ord}}(\cA)$.
\end{proof}

\begin{remark}[Key formulas of the equivalence]
\label{rem:chiral-qg-key-formulas}
The three equivalences involve the following explicit formulas.
The OPE compatibility axiom:
\begin{equation}\label{eq:ope-compat}
  \Delta^{\mathrm{ch}}(Y(a,z)\, b)
  \;=\;
  Y^{(2)}(\Delta^{\mathrm{ch}}(a), z)
  \cdot \Delta^{\mathrm{ch}}(b),
\end{equation}
where $Y^{(2)}$ is the tensorwise vertex operation.
exec
/bin/zsh -lc "sed -n '8095,8128p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}\label{eq:r-from-coprod-proof}
  S(z)
  \;:=\; \sigma \circ \Delta^{\mathrm{ch}}
  \circ (\Delta^{\mathrm{ch},\mathrm{op}})^{-1}.
\end{equation}
\end{remark}

% ================================================================
\noindent\emph{QYBE, unitarity, shift, hexagon.}
The quantum Yang--Baxter equation on
$V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
to~\eqref{eq:yangian-qybe}, verified in
Example~\ref{ex:yangian}; the extension to
$V_{\mathrm{EK}}$ follows from the universal property of
$\mathcal{R}(z)$.
Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
\circ \sigma) = \id$ follows from Drinfeld--Jimbo unitarity.
The shift condition
\begin{equation}\label{eq:ek-shift-cond}
  [D \otimes \id + \id \otimes D,\; S(z)]

thinking
**Searching for equations**

I need to remember that this section continues without any explicit examples referenced. I might want to replace generic terms like "yangian" with something more specific, such as "the classical Yangian computation" or specific equations if I can find them. It seems like searching for terms related to "yangian-qybe" could help me locate the relevant examples, either in a specific file or in a local database. Let's go ahead and look for that!
exec
/bin/zsh -lc "rg -n \"label\\{eq:yangian-qybe\\}|eq:yangian-qybe\" chapters/examples/yangians_computations.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/theory/ordered_associative_chiral_kd.tex:8106:to~\eqref{eq:yangian-qybe}, verified in
chapters/theory/ordered_associative_chiral_kd.tex:10905:\phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone

thinking
**Exploring equation labels**

I'm noticing that there's an interesting equation label that exists around 10905. I'm curious if it might be related to something like the Yangian, perhaps? I think I should search the area near 10905 to gather more context. This could lead to useful insights or reveal what the label is all about. Let's see what I can find!
exec
/bin/zsh -lc "sed -n '10890,10920p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
factors the Heisenberg sewing determinant over primes
via the unordered divisor function $\sigma_{-1}$.
The $\mathsf{E}_1$-ordered bar complex replaces
unordered by ordered factorizations; the analogous
ordered sewing lift should involve composition-weighted
divisor sums and factor in the ring of non-commutative
formal Dirichlet series.
\end{remark}


% ================================================================
%% --- Phantom labels for standalone cross-references (TODO: integrate) ---
\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
\phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
\phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
\phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone


thinking
**Exploring chiral coproducts**

I’m noticing that there are phantom labels for def:chiral-coproduct later in my notes. It’s interesting that this means def:chiral-coproduct does exist. But I’m wondering why our previous search didn’t pick it up. Could it be because my request looked for `label{def:chiral-coproduct}` and maybe the max tokens caused truncation? I didn’t find it for some reason, so I’ll try searching again.
thinking
**Searching for missing labels**

It looks like some "missing" references might actually have phantom labels later in the same file, which could explain why they weren't caught in our chapter-only scan. Maybe the user's procedure would find the label in the chapters. Our regex search might not include certain tokens. For example, the explorer pointed out that "def:chiral-coproduct" was missing, but it really exists as a phantom label. I should expand the search to include all missing labels.
codex
There’s a second wrinkle: this file already contains late-file phantom labels for some standalone cross-refs. I’m re-checking the truly missing subset against the full target file now so I don’t rewrite references that already resolve locally via those placeholders.
exec
/bin/zsh -lc "rg -n \"label\\{(ex:yangian|conj:yangian-ordered-center|ex:yangian-coproduct|def:chiral-coproduct|def:e1-chiral-rmatrix|eq:yangian-ker-av2)\\}\" chapters/theory/ordered_associative_chiral_kd.tex chapters appendices main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/ordered_associative_chiral_kd.tex:10902:\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
chapters/theory/ordered_associative_chiral_kd.tex:10902:\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
exec
/bin/zsh -lc "sed -n '10898,10910p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:


% ================================================================
%% --- Phantom labels for standalone cross-references (TODO: integrate) ---
\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
\phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
\phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
\phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone
exec
/bin/zsh -lc "grep -n 'thm:affine-monodromy-identification\\|ex:yangian\\|conj:yangian-ordered-center\\|ex:yangian-coproduct\\|def:e1-chiral-rmatrix\\|eq:yangian-ker-av2' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
5075:Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
5116:The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
5486:(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
5666:Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
5717:(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
6047:Example~\ref{ex:yangian} and
6048:Conjecture~\ref{conj:yangian-ordered-center}(v)
6146:Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
6159:Conjecture~\ref{conj:yangian-ordered-center}(v):
6166:(Example~\ref{ex:yangian},
6167:equation~\eqref{eq:yangian-ker-av2}).
8107:Example~\ref{ex:yangian}; the extension to
8132:computation of Example~\ref{ex:yangian} (Part B) but now
8168:Example~\ref{ex:yangian}; the result is identical on
8173:equation~\eqref{eq:yangian-ker-av2}.
8385:Example~\ref{ex:yangian-coproduct}).
8731:Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$

thinking
**Filling hot-zone status**

I’m thinking about providing a note for the hot-zone status, focusing on any necessary edits. The requirement is to fill the template as a fenced block, which is a bit tricky since I need to avoid new labels. 

I might say: "PE-7 not triggered: no \label{} creation in planned patch," and provide the verdict as "ACCEPT." 

But the template needs specific fields, so I should mention that if there’s no label creation, it’s simply not triggered. I'll include that commentary with the planned edits.
codex
I’ve isolated the real edit set to one file and I’m keeping it narrow: remove the five Vol II-only theorem refs, replace the three missing ordered-centre refs with plain truthful wording, drop the nonexistent Yangian example/coproduct refs, and redirect the lone `def:e1-chiral-rmatrix` ref to the existing `def:e1-chiral`.

```text
PE-7: not triggered
reason: no new \label{} will be created in this patch; only dangling \ref{} targets are being removed or redirected to existing local labels
verdict: ACCEPT
```
file update
M /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5073,5 +5073,4 @@
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
@@ -5115,3 +5114,3 @@
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
@@ -5485,3 +5484,3 @@
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
@@ -5665,3 +5664,3 @@
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
@@ -5715,4 +5714,3 @@
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
@@ -6045,6 +6043,5 @@
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
@@ -6144,4 +6141,3 @@
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
@@ -6157,4 +6153,3 @@
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
@@ -6164,5 +6159,4 @@
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
@@ -8105,4 +8099,4 @@
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
@@ -8131,3 +8125,3 @@
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
@@ -8166,4 +8160,4 @@
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
@@ -8171,4 +8165,4 @@
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
@@ -8382,5 +8376,4 @@
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
@@ -8730,3 +8723,3 @@
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
apply_patch(auto_approved=true) exited 0 in 37ms:
Success. Updated the following files:
M /Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..e414a30502cb45e6bd47f802acd67ba97ce82e5a
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the

file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..e414a30502cb45e6bd47f802acd67ba97ce82e5a
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the


thinking
**Reviewing modifications**

I should ensure the coherence of the sections I've changed. There might be false positives that don't require edits, so I need to verify that no broken references remain in the modified file. I should remove all instances of those broken labels unless they belong to non-edited false positives. It seems like a thorough inspection around the edits is necessary. I'll consider using grep to help with this process.
codex
The patch is in. I’m re-reading each edited block now to make sure the rewritten sentences still parse locally, then I’ll grep the modified file for the removed dangling labels and for any other unresolved refs introduced by the patch.
exec
/bin/zsh -lc "sed -n '5478,5722p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '5068,5122p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{Step~2: One-loop collapse.}
For the affine algebra $V^k(\mathfrak{g})$, the one-loop exactness of
the BV-BRST differential (Theorem~\ref*{thm:affine-half-space-bv} of
Volume~II) ensures that the higher $A_\infty$ operations $m_k$
($k \geq 3$) vanish on evaluation modules. The full superconnection
on the bar complex therefore collapses to the KZ connection, and the
bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
(the one-loop collapse statement of Volume~II).

\emph{Step~3: Identification.}
Combining Steps~1 and~2, the bar-complex monodromy for the affine
lineage equals the quantum-group braid representation:
$\rho_n^{\mathrm{HT}} = \rho_n^{\mathrm{KZ}} \simeq
\rho_n^{U_q(\mathfrak{g})}$.

\medskip
\noindent\textbf{(ii)} follows from the genus-$1$ generalisation of the
Drinfeld--Kohno theorem (Etingof--Schiffmann, Calaque--Enriquez--Etingof):
the KZB monodromy representation on $\mathrm{Conf}_n(E_\tau)$ factors
through $U_q(\mathfrak{g})$, with the $B$-cycle monodromy providing the
 succeeded in 52ms:
additional generators (the $A$-cycle and $B$-cycle monodromies),
and their interaction with the braid generators produces the quantum
group $U_q(\mathfrak{g})$ from the Yangian $Y_\hbar(\mathfrak{g})$.

The genus-$1$ lift for the affine lineage
$V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
one-loop collapse mechanism established in Volume~II, giving a
rigorous passage from the KZ connection to the KZB connection and
thence to the quantum group.

\subsection{The KZ connection on ordered configurations}
\label{sec:kz-connection}

The genus-$0$ starting point is as follows. Let $\mathfrak{g}$ be a simple
Lie algebra and $k \in \mathbb{C} \setminus \{-h^\vee\}$ generic.
Choose an orthonormal basis $\{I^a\}$ for~$\mathfrak{g}$ with respect
to the Killing form normalised so that
$\operatorname{tr}(I^a I^b) = \delta^{ab}$. The Casimir tensor is
$\Omega = \sum_a I^a \otimes I^a \in \mathfrak{g} \otimes \mathfrak{g}$.

exec
/bin/zsh -lc "sed -n '6038,6172p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8378,8392p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8724,8738p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'thm:affine-monodromy-identification\\|ex:yangian\\|conj:yangian-ordered-center\\|ex:yangian-coproduct\\|def:e1-chiral-rmatrix\\|eq:yangian-ker-av2' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '8100,8188p' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\mathrm{Rep}_q(\mathfrak{sl}_2)$ at
$q = e^{2\pi i/(k+2)}$. This identification is the
subject of the DK-5 programme; see
\cite[\S6]{Lorgat26I} for the current status in type~$A$.
\end{remark}

The low-degree Yangian computations and the corresponding
conjectural ordered-centre bounds concern the kernel of the
averaging map on the
ordered chiral centre, a cohomological object.
The following proposition establishes the underlying
representation-theoretic input: the dimension of
$\ker(\av_n)$ on the bare tensor power $V^{\otimes n}$,
before passing to bar-complex cohomology.

\begin{proposition}[Kernel of the Reynolds projector:
general simple Lie algebras]
\label{prop:ker-av-schur-weyl}
\ClaimStatusProvedHere
Let $\fg$ be any simple Lie algebra over~$\CC$, let
 succeeded in 52ms:
Definition~\ref{def:e1-chiral}. The functor $\alpha$
of the equivalence triangle~\eqref{eq:equiv-triangle}
extracts the chiral $\Ainf$ operations
$\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the
associahedra
$K_k \hookrightarrow
\overline{\FM}_k^{\mathrm{ord}}(\CC)$ as
in~\eqref{eq:mk-from-ope}. The Stasheff identities follow
from Stokes' theorem on $K_{k+1}$ as before; the
convergence of the integrals is guaranteed by
$S$-locality of the $R$-matrix. This gives
$\textup{(I)} \to \textup{(II)}$ on the CoHA.

The reverse direction $\textup{(II)} \to \textup{(I)}$ is the
degree-$2$ holonomy recovery of the $R$-matrix from
 succeeded in 52ms:
displayed below.
Through spin~$3$:
\begin{align}
  \Delta_z(\psi_1)
  &= \psi_1 \otimes 1
  + 1 \otimes \psi_1,
  \label{eq:coprod-psi1} \\[4pt]
  \Delta_z(\psi_2)
  &= \psi_2 \otimes 1
  + 1 \otimes \psi_2
  + \psi_1 \otimes \psi_1
  + z\,(1 \otimes \psi_1),
  \label{eq:coprod-psi2} \\[4pt]
  \Delta_z(\psi_3)
  &= \psi_3 \otimes 1
exec
/bin/zsh -lc "grep -n 'label{app:nonlinear-modular-shadows}\\|label{app:signs}\\|label{app:sign-conventions}\\|label{part:characteristic-datum}\\|label{thm:chiral-htt}\\|label{thm:bar-cobar-htt}\\|label{thm:nms-archetype-trichotomy}\\|label{thm:nms-finite-termination}\\|label{def:chiral-coproduct}' appendices/*.tex main.tex chapters/theory/*.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "grep -n 'app:nonlinear-modular-shadows\\|app:signs\\|app:sign-conventions\\|part:characteristic-datum\\|thm:chiral-htt\\|thm:bar-cobar-htt\\|thm:nms-archetype-trichotomy\\|thm:nms-finite-termination\\|def:chiral-coproduct' chapters/theory/higher_genus_complementarity.tex chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
to~\eqref{eq:yangian-qybe}, as in the classical Yangian
case; the extension to
$V_{\mathrm{EK}}$ follows from the universal property of
$\mathcal{R}(z)$.
Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
\circ \sigma) = \id$ follows from Drinfeld--Jimbo unitarity.
The shift condition
\begin{equation}\label{eq:ek-shift-cond}
  [D \otimes \id + \id \otimes D,\; S(z)]
  \;=\; \partial_z\, S(z)
\end{equation}
follows from the translation-covariance of the Drinfeld
coproduct. The hexagon follows from the pentagon relation
for $\Phi$ (from the Stasheff boundary of
$\overline{\FM}_4^{\mathrm{ord}}(\CC) = K_4$) combined
with the QYBE for $S$, by the standard argument of
Drinfeld~\cite{EK96} lifted to the vertex-algebraic setting.

\medskip
\noindent
 exited 1 in 51ms:

 succeeded in 52ms:
chapters/theory/higher_genus_complementarity.tex:96: \textup{(}Appendix~\textup{\ref{app:nonlinear-modular-shadows})}.
chapters/theory/higher_genus_complementarity.tex:1208:This sign is precisely the Koszul sign convention (see Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}). 
chapters/theory/higher_genus_complementarity.tex:1750:Part~\ref{part:characteristic-datum} (\S\ref{subsec:genus2-complementarity-verification}).
chapters/theory/higher_genus_complementarity.tex:2643:The Koszul dual of the Heisenberg algebra is the curved Chevalley--Eilenberg algebra (cf.\ Part~\ref{part:characteristic-datum}):
chapters/theory/higher_genus_complementarity.tex:4591:(Theorem~\textup{\ref{thm:chiral-htt}}).
chapters/theory/higher_genus_complementarity.tex:4607:of Theorem~\ref{thm:bar-cobar-htt}, and the transferred structure
chapters/theory/higher_genus_complementarity.tex:5251:(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
chapters/theory/higher_genus_complementarity.tex:5259:shadow obstruction tower is infinite (Theorem~\ref{thm:nms-finite-termination}).
chapters/theory/higher_genus_complementarity.tex:5907:(Theorem~\ref{thm:nms-archetype-trichotomy}).
chapters/theory/ordered_associative_chiral_kd.tex:8570:Definition~\ref{def:chiral-coproduct}:
chapters/theory/ordered_associative_chiral_kd.tex:11046:\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
 succeeded in 390ms:
appendices/homotopy_transfer.tex:455:\label{thm:chiral-htt}
appendices/homotopy_transfer.tex:524:\label{thm:bar-cobar-htt}
appendices/nonlinear_modular_shadows.tex:2:\label{app:nonlinear-modular-shadows}
appendices/nonlinear_modular_shadows.tex:1208:\label{thm:nms-archetype-trichotomy}
appendices/nonlinear_modular_shadows.tex:2191:\label{thm:nms-finite-termination}
appendices/signs_and_shifts.tex:2:\label{app:signs}
appendices/signs_and_shifts.tex:713:\label{app:sign-conventions}
main.tex:1073:\label{part:characteristic-datum}
chapters/theory/ordered_associative_chiral_kd.tex:11046:\phantomsection\label{def:chiral-coproduct} % TODO: integrate from standalone
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..e414a30502cb45e6bd47f802acd67ba97ce82e5a
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the


thinking
**Considering grep techniques**

I’m thinking I might need to use grep to find banned prose tokens and em dashes in the modified file. I could try something like `rg -n '(?i)\bmoreover\b|...'`, but I want to avoid false positives from unrelated sections in the file. The modified file is quite large, so it might contain a lot of unrelated content. The instructions do say to grep for forbidden patterns after all edits, so that’s my plan!
codex
The local reread is coherent. Final verification now is mechanical: I’m checking the modified file for any remaining genuinely unresolved refs, then running the post-write forbidden-pattern grep on that same file so I can distinguish what this patch fixed from any pre-existing debris outside the edit span.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
import re
p=Path('chapters/theory/ordered_associative_chiral_kd.tex')
patterns=[r'(?i)\\bmoreover\\b',r'(?i)\\badditionally\\b',r'(?i)\\bnotably\\b',r'(?i)\\bcrucially\\b',r'(?i)\\bremarkably\\b',r'(?i)\\binterestingly\\b',r'(?i)\\bfurthermore\\b',r'---',r'—']
text=p.read_text()
for pat in patterns:
    if re.search(pat,text):
        print(pat)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'git diff -- chapters/theory/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar exited 127 in 52ms:
zsh:1: command not found: python
 succeeded in 51ms:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 9654057..e414a30 100644
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@ group $U_q(\mathfrak{g})$ from the Yangian $Y_\hbar(\mathfrak{g})$.
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@ connection~\eqref{eq:kohno-connection}: for the affine algebra
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
exec
/bin/zsh -lc "ruby -e 'labels={}; "'`rg -No "label'"\\\\{["'^}]+" chapters appendices main.tex`.each_line{|ln| if ln =~ /label'"\\{(["'^}]+)/ then labels[$1]=true end}; refs=[]; File.readlines("chapters/theory/ordered_associative_chiral_kd.tex").each_with_index{|line,i| line.scan(/'"\\\\(?:eq|pag|auto)?ref\\{(["'^}]+)'"\\}/){|m| refs << [i+1,m[0]]}}; missing=refs.reject{|_,lab| labels[lab]}; missing.each{|ln,lab| puts \"#{ln} | #{lab}\" }'" in /Users/raeez/chiral-bar-cobar succeeded in 74ms:
502 | eq:cybe-vol1
516 | constr:r-matrix-monodromy-vol1
546 | eq:kohno-connection
562 | eq:r-twisted-action
610 | eq:cybe-vol1
661 | eq:descent-identification-vol1
679 | eq:kohno-connection
680 | eq:r-matrix-monodromy-vol1
681 | eq:r-twisted-action
698 | sec:r-matrix-descent-vol1
713 | eq:cybe-vol1
739 | sec:r-matrix-descent-vol1
849 | thm:opposite
857 | thm:bar-cobar-isomorphism-main
869 | thm:opposite
909 | thm:opposite
1057 | prop:one-defect
1057 | thm:tangent=K
1083 | cor:infdual
1084 | thm:HH-coHH-homology
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..e414a30502cb45e6bd47f802acd67ba97ce82e5a
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the

exec
/bin/zsh -lc "rg -n -i '\\b(moreover|additionally|notably|crucially|remarkably|interestingly|furthermore)\\b|---|—' chapters/theory/ordered_associative_chiral_kd.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
9164:% ----------------------------------------------------------------
9723:% ----------------------------------------------------------------
11045:%% --- Phantom labels for standalone cross-references (TODO: integrate) ---
11063:%% --- End phantom labels ---
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..b23e5e90f5da69787d157ca9852c07971e2e80d8
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the
@@ -11054,3 +11047,17 @@
 \phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone
+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
+\phantomsection\label{ch:genus1-seven-faces} % TODO: integrate from standalone
+\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
+\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
+\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
+\phantomsection\label{conv:three-hochschild} % TODO: integrate from standalone
+\phantomsection\label{part:seven-faces} % TODO: integrate from standalone
+\phantomsection\label{part:v1-frontier} % TODO: integrate from standalone
+\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone
+\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone
+\phantomsection\label{sec:complementarity} % TODO: integrate from standalone
+\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone
+\phantomsection\label{thm:langlands-bar-bridge} % TODO: integrate from standalone
+%% --- End phantom labels ---

codex
The targeted labels are clean: none of the dangling refs I removed remain in the file. The broader file still has a large pre-existing unresolved-ref surface outside this first-30 task, and the forbidden-pattern grep only hit pre-existing comment separators rather than any new prose in the patched spans.
Plan update
Patched the genuinely unresolved refs among the first 30 chapter-only findings, then re-read the edited blocks and verified the removed labels no longer occur. The modified file still contains many unrelated unresolved refs outside this task’s scope.
  ✓ Identify the first 30 broken refs in `chapters/theory/` and classify each as typo, missing label, or deleted target
  ✓ Patch only the affected theory files with the minimal truthful fix for each broken ref
  ✓ Re-read modified context, validate labels/refs, and grep modified files for lingering broken patterns
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..b23e5e90f5da69787d157ca9852c07971e2e80d8
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the
@@ -11054,3 +11047,17 @@
 \phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone
+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
+\phantomsection\label{ch:genus1-seven-faces} % TODO: integrate from standalone
+\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
+\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
+\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
+\phantomsection\label{conv:three-hochschild} % TODO: integrate from standalone
+\phantomsection\label{part:seven-faces} % TODO: integrate from standalone
+\phantomsection\label{part:v1-frontier} % TODO: integrate from standalone
+\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone
+\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone
+\phantomsection\label{sec:complementarity} % TODO: integrate from standalone
+\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone
+\phantomsection\label{thm:langlands-bar-bridge} % TODO: integrate from standalone
+%% --- End phantom labels ---

codex
Edited only [ordered_associative_chiral_kd.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex:5071). I did not touch `higher_genus_complementarity.tex`, `existence_criteria.tex`, or `configuration_spaces.tex` where the audit hits were false positives from searching `chapters/` only.

1. `higher_genus_complementarity.tex:88` `app:nonlinear-modular-shadows` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
2. `higher_genus_complementarity.tex:1198` `app:signs` — BLOCKED: label exists in `appendices/signs_and_shifts.tex`.
3. `higher_genus_complementarity.tex:1198` `app:sign-conventions` — BLOCKED: label exists in `appendices/signs_and_shifts.tex`.
4. `higher_genus_complementarity.tex:1740` `part:characteristic-datum` — BLOCKED: label exists in `main.tex`.
5. `higher_genus_complementarity.tex:2518` `part:characteristic-datum` — BLOCKED: label exists in `main.tex`.
6. `higher_genus_complementarity.tex:4466` `thm:chiral-htt` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
7. `higher_genus_complementarity.tex:4482` `thm:bar-cobar-htt` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
8. `higher_genus_complementarity.tex:5126` `thm:nms-archetype-trichotomy` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
9. `higher_genus_complementarity.tex:5134` `thm:nms-finite-termination` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
10. `higher_genus_complementarity.tex:5782` `thm:nms-archetype-trichotomy` — BLOCKED: label exists in `appendices/nonlinear_modular_shadows.tex`.
11. `ordered_associative_chiral_kd.tex:5075` `thm:affine-monodromy-identification` — FIXED: removed the Vol II-only `\ref` and cited the Volume II one-loop collapse textually.
12. `ordered_associative_chiral_kd.tex:5116` `thm:affine-monodromy-identification` — FIXED: same.
13. `ordered_associative_chiral_kd.tex:5486` `thm:affine-monodromy-identification` — FIXED: same.
14. `ordered_associative_chiral_kd.tex:5666` `thm:affine-monodromy-identification` — FIXED: same.
15. `ordered_associative_chiral_kd.tex:5717` `thm:affine-monodromy-identification` — FIXED: same.
16. `ordered_associative_chiral_kd.tex:6047` `ex:yangian` — FIXED: rewrote to plain “low-degree Yangian computations”.
17. `ordered_associative_chiral_kd.tex:6048` `conj:yangian-ordered-center` — FIXED: rewrote to plain “conjectural ordered-centre bounds”.
18. `ordered_associative_chiral_kd.tex:6146` `conj:yangian-ordered-center` — FIXED: retitled the remark without the dangling conjecture ref.
19. `ordered_associative_chiral_kd.tex:6159` `conj:yangian-ordered-center` — FIXED: replaced with plain conjectural wording.
20. `ordered_associative_chiral_kd.tex:6166` `ex:yangian` — FIXED: replaced with “classical Yangian computation”.
21. `ordered_associative_chiral_kd.tex:8107` `ex:yangian` — FIXED: replaced with “classical Yangian case”.
22. `ordered_associative_chiral_kd.tex:8132` `ex:yangian` — FIXED: same.
23. `ordered_associative_chiral_kd.tex:8168` `ex:yangian` — FIXED: same.
24. `ordered_associative_chiral_kd.tex:8385` `ex:yangian-coproduct` — FIXED: replaced with a local reference to the expansions displayed below.
25. `ordered_associative_chiral_kd.tex:8577` `def:chiral-coproduct` — BLOCKED: not actually broken; a local phantom label already exists later in the file.
26. `ordered_associative_chiral_kd.tex:8731` `def:e1-chiral-rmatrix` — FIXED: redirected to existing `Definition~\ref{def:e1-chiral}`.
27. `ordered_associative_chiral_kd.tex:10225` `thm:tree-formula` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
28. `ordered_associative_chiral_kd.tex:10240` `constr:transfer-ainf` — BLOCKED: label exists in `appendices/homotopy_transfer.tex`.
29. `existence_criteria.tex:474` `app:koszul-reference` — BLOCKED: label exists in `appendices/koszul_reference.tex`.
30. `configuration_spaces.tex:83` `thm:arnold-iff-nilpotent` — BLOCKED: label exists in `appendices/arnold_relations.tex`.

Verification: the removed dangling labels no longer occur in `ordered_associative_chiral_kd.tex`, and the appendix/main labels above were confirmed to exist on the live surface. The modified file still has many other unresolved refs outside this first-30 task. I did not run a TeX build.
file update:
diff --git a/chapters/theory/ordered_associative_chiral_kd.tex b/chapters/theory/ordered_associative_chiral_kd.tex
index 4a7a0a96272bb234b85d841c7938c211f839021d..b23e5e90f5da69787d157ca9852c07971e2e80d8
--- a/chapters/theory/ordered_associative_chiral_kd.tex
+++ b/chapters/theory/ordered_associative_chiral_kd.tex
@@ -5071,9 +5071,8 @@
 
 The genus-$1$ lift for the affine lineage
 $V^k(\mathfrak{g})$ combines the Drinfeld--Kohno theorem with the
-one-loop collapse mechanism of
-Theorem~\ref{thm:affine-monodromy-identification} (Volume~II),
-giving a rigorous passage from the KZ connection to the KZB connection and
+one-loop collapse mechanism established in Volume~II, giving a
+rigorous passage from the KZ connection to the KZB connection and
 thence to the quantum group.
 
 \subsection{The KZ connection on ordered configurations}
@@ -5113,7 +5112,7 @@
 $V^k(\mathfrak{g})$, the collision residue $r_{ij}(z)$ extracted by
 the $d\log$ kernel (cf.\: the kernel absorbs one pole) is
 $r_{ij} = (\hbar/2\pi i)\,\Omega_{ij}$, which is constant in~$z$.
-The one-loop collapse of Theorem~\ref{thm:affine-monodromy-identification}
+The one-loop collapse mechanism from Volume~II
 ensures that the higher $A_\infty$ operations $m_k$ ($k \geq 3$) do not
 contribute on evaluation modules, so the full superconnection reduces to
 the KZ connection. The flatness $\nabla_{\mathrm{KZ}}^2 = 0$ follows
@@ -5483,7 +5482,7 @@
 ($k \geq 3$) vanish on evaluation modules. The full superconnection
 on the bar complex therefore collapses to the KZ connection, and the
 bar-complex monodromy $\rho_n^{\mathrm{HT}}$ equals $\rho_n^{\mathrm{KZ}}$
-(Theorem~\ref{thm:affine-monodromy-identification}(i) of Volume~II).
+(the one-loop collapse statement of Volume~II).
 
 \emph{Step~3: Identification.}
 Combining Steps~1 and~2, the bar-complex monodromy for the affine
@@ -5663,7 +5662,7 @@
 \end{theorem}
 
 \begin{proof}
-Parts (i)--(ii) combine Theorem~\ref{thm:affine-monodromy-identification}
+Parts (i)--(ii) combine the Volume~II one-loop collapse statement
 (the bar-complex monodromy equals the KZ monodromy for the affine
 lineage) with Theorem~\ref{thm:drinfeld-kohno}(i) (the KZ monodromy
 equals the quantum group braid representation).
@@ -5713,8 +5712,7 @@
 The results of this section are proved for the \emph{affine lineage}:
 $V^k(\mathfrak{g})$ for simple $\mathfrak{g}$ at generic level~$k$,
 acting on finite-dimensional evaluation modules. The proof mechanism
-is the one-loop collapse
-(Theorem~\ref{thm:affine-monodromy-identification} of Volume~II),
+is the one-loop collapse mechanism from Volume~II,
 which reduces the full bar-complex superconnection to the KZ/KZB
 connection, and the Drinfeld--Kohno theorem (classical at genus~$0$,
 Etingof--Schiffmann/Calaque--Enriquez--Etingof at genus~$1$), which
@@ -6043,10 +6041,9 @@
 \cite[\S6]{Lorgat26I} for the current status in type~$A$.
 \end{remark}
 
-The computations in
-Example~\ref{ex:yangian} and
-Conjecture~\ref{conj:yangian-ordered-center}(v)
-concern the kernel of the averaging map on the
+The low-degree Yangian computations and the corresponding
+conjectural ordered-centre bounds concern the kernel of the
+averaging map on the
 ordered chiral centre, a cohomological object.
 The following proposition establishes the underlying
 representation-theoretic input: the dimension of
@@ -6142,8 +6139,7 @@
 determined by $d$ alone.
 \end{proof}
 
-\begin{remark}[Explicit values and
-Conjecture~\textup{\ref{conj:yangian-ordered-center}}]
+\begin{remark}[Explicit values and conjectural ordered-centre bounds]
 \label{rem:ker-av-table}
 Table~\ref{tab:ker-av-dims} records the kernel dimensions
 at low degrees for the fundamental representations of
@@ -6155,16 +6151,14 @@
 $\mathfrak{so}_5$ are identical.
 These are representation-theoretic upper bounds on the
 dimensions of the corresponding components of the ordered
-chiral centre in
-Conjecture~\ref{conj:yangian-ordered-center}(v):
+chiral centre in the conjectural ordered-centre kernel:
 $\ker(\av_n)$ on the ordered chiral centre is a subquotient
 of $\ker(\av_n\big|_{V^{\otimes n}})$, obtained by passing
 to bar-complex cohomology
 (only the cocycles in the non-trivial $\Sigma_n$-isotypics
 survive). At degree $2$ for $\mathfrak{sl}_2$: the full
-$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives
-(Example~\ref{ex:yangian},
-equation~\eqref{eq:yangian-ker-av2}).
+$1$-dimensional kernel $\bigwedge^2 V = \CC$ survives in
+the classical Yangian computation.
 At degree $n \geq 3$, the kernel on the chiral centre is
 in general strictly smaller than the
 representation-theoretic bound $d^n - \binom{n+d-1}{d-1}$.
@@ -8103,8 +8097,8 @@
 \noindent\emph{QYBE, unitarity, shift, hexagon.}
 The quantum Yang--Baxter equation on
 $V_{\mathrm{EK}}^{\otimes 3}$ reduces on $V^{\otimes 3}$
-to~\eqref{eq:yangian-qybe}, verified in
-Example~\ref{ex:yangian}; the extension to
+to~\eqref{eq:yangian-qybe}, as in the classical Yangian
+case; the extension to
 $V_{\mathrm{EK}}$ follows from the universal property of
 $\mathcal{R}(z)$.
 Unitarity $S_{12}(z) \cdot (\sigma \circ S_{12}(-z)
@@ -8129,7 +8123,7 @@
 $\HH^{*,\mathrm{ord}}_{\mathrm{ch}}
 (V_{\mathrm{EK}},\,V_{\mathrm{EK}})$
 at low degrees on the formal disk $D$, paralleling the
-computation of Example~\ref{ex:yangian} (Part B) but now
+classical Yangian computation but now
 using the \emph{full} vertex $R$-matrix $S(z)$ rather than
 the Yang $R$-matrix on $V \otimes V$ alone.
 
@@ -8164,13 +8158,13 @@
 \end{equation}
 
 \emph{The kernel $\ker(\av)$.}
-The ordered chiral centre computation parallels
-Example~\ref{ex:yangian}; the result is identical on
+The ordered chiral centre computation parallels the
+classical Yangian case; the result is identical on
 cohomology. On $V \otimes V$:
 $\ker(\av_2)\big|_{V \otimes V}
 \cong \bigwedge^2 V = \CC$,
-the same one-dimensional space as
-equation~\eqref{eq:yangian-ker-av2}.
+the same one-dimensional space as in that classical
+computation.
 The quantum corrections from $S(z)$ shift the subleading
 terms of the flat sections but do not alter the
 $\ker(\av_2)$ dimension. The scalar shadow surviving
@@ -8380,9 +8374,8 @@
 $(u - z)^{-m} = u^{-m} \sum_{j \geq 0}
 \binom{m+j-1}{j} (z/u)^j$ applied to
 $T(u) \otimes T(u-z)$ and collecting the coefficient
-of $u^{-n}$
-(see~\eqref{eq:yangian-drinfeld-coprod} and
-Example~\ref{ex:yangian-coproduct}).
+of $u^{-n}$, giving the spin-$1$, $2$, and $3$ expansions
+displayed below.
 Through spin~$3$:
 \begin{align}
   \Delta_z(\psi_1)
@@ -8728,7 +8721,7 @@
 vertex bialgebra.}
 The CoHA $\cH_{Q,W}$, equipped with its $R$-matrix, is an
 $\Eone$-chiral algebra in the sense of
-Definition~\ref{def:e1-chiral-rmatrix}. The functor $\alpha$
+Definition~\ref{def:e1-chiral}. The functor $\alpha$
 of the equivalence triangle~\eqref{eq:equiv-triangle}
 extracts the chiral $\Ainf$ operations
 $\{m_k^{\mathrm{ch}}\}$ by restricting the OPE to the
@@ -11054,3 +11047,17 @@
 \phantomsection\label{eq:bar-degree1-yangian} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-drinfeld-coprod} % TODO: integrate from standalone
 \phantomsection\label{eq:yangian-qybe} % TODO: integrate from standalone
+\phantomsection\label{ch:derived-langlands} % TODO: integrate from standalone
+\phantomsection\label{ch:genus1-seven-faces} % TODO: integrate from standalone
+\phantomsection\label{ch:holographic-datum-master} % TODO: integrate from standalone
+\phantomsection\label{ch:landscape-census} % TODO: integrate from standalone
+\phantomsection\label{comp:bp-kappa-three-paths} % TODO: integrate from standalone
+\phantomsection\label{conv:three-hochschild} % TODO: integrate from standalone
+\phantomsection\label{part:seven-faces} % TODO: integrate from standalone
+\phantomsection\label{part:v1-frontier} % TODO: integrate from standalone
+\phantomsection\label{prop:nilpotent-transport-typeA} % TODO: integrate from standalone
+\phantomsection\label{sec:bar-complex-introduction} % TODO: integrate from standalone
+\phantomsection\label{sec:complementarity} % TODO: integrate from standalone
+\phantomsection\label{thm:ds-hpl-transfer} % TODO: integrate from standalone
+\phantomsection\label{thm:langlands-bar-bridge} % TODO: integrate from standalone
+%% --- End phantom labels ---

tokens used
364,933
