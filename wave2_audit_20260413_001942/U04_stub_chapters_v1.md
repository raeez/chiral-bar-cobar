# U04_stub_chapters_v1 (380s)

- [HIGH] chapters/frame/preface.tex:1198 — PROBLEM: the compiled preface is a 4,374-line technical chapter with zero `\begin{theorem}`/`\begin{proposition}` blocks, yet Section “The five theorems” states Theorems A/B/C/D/H as unnumbered bold prose at lines 1204–1253. That leaves a live, load-bearing chapter outside theorem/status discipline, while [chapters/frame/guide_to_main_results.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/guide_to_main_results.tex:6) already exists as the theorem digest. FIX: merge the theorem-summary material out of `preface.tex` into `guide_to_main_results.tex` and cut `preface.tex` back to actual front matter; if any technical claims remain in the preface, restate them as real theorem/proposition environments with the canonical labels instead of inline bold paragraphs.

- [HIGH] chapters/connections/thqg_preface_supplement.tex:1 — PROBLEM: this is a 2,056-line theorem-free pseudo-chapter whose own header says “Inserted near the end of the preface chapter via `\input`” at line 2, but it has no actual `\input`/`\include` path anywhere in `main.tex`, `preface.tex`, or other chapter files. It is an orphaned, uncompiled frontier surface living in the active `chapters/` tree. FIX: remove `thqg_preface_supplement.tex` from `chapters/connections/`; if any prose is still wanted, rehome it into the actual Volume II front matter before deletion, not as a dormant Vol I supplement.

- [HIGH] chapters/connections/physical_origins.tex:1 — PROBLEM: this is a 19-line chapter stub whose entire body says the chapter “has been absorbed into Volume II” (lines 5–19); `main.tex:1399` keeps it commented out as “19-line stub; content absorbed into Vol II.” This is dead chapter debris, not live manuscript content. FIX: remove `physical_origins.tex` from `chapters/connections/` and rebuild metadata so `chap:physical-origins` / `rem:programme-origins` disappear from the active label surface.

- [MEDIUM] chapters/frame/preface_section1_v2.tex:1 — PROBLEM: orphan alternate Section 1 draft, not included anywhere, with no theorem/proposition blocks and a duplicate live label `rem:pf1-zero-dim` at line 570 that already exists in `preface.tex:832`. FIX: remove this file from `chapters/frame/` (or move it to `archive/`), and keep `preface.tex` as the sole canonical Section 1 source.

- [MEDIUM] chapters/frame/preface_section1_draft.tex:1 — PROBLEM: the file explicitly says “To be integrated into preface.tex” at line 2, is not actually included anywhere, has no theorem/proposition blocks, and duplicates `rem:pf1-zero-dim` at line 656 already present in `preface.tex:832`. FIX: remove the draft from `chapters/frame/` or archive it outside the active chapter tree; do not keep an unintegrated duplicate beside the compiled preface.

- [MEDIUM] chapters/frame/preface_sections2_4_draft.tex:1 — PROBLEM: explicit orphan draft (“To be integrated into preface.tex”), not included anywhere, and it duplicates live preface labels `eq:preface-feynman-sum` (line 417 vs. `preface.tex:1330`), `eq:preface-fcom` (445 vs. 1358), `eq:preface-convolution-ladder` (485 vs. 1398), and `eq:preface-gmod` (516 vs. 1438). FIX: remove this draft from `chapters/frame/` and keep the merged material in `preface.tex` only.

- [MEDIUM] chapters/frame/preface_sections5_9_draft.tex:1 — PROBLEM: another explicit orphan draft (“To be integrated into preface.tex”), with no theorem/proposition blocks and section range already present in the compiled preface as Sections 5–9 at `preface.tex:2161`, `2435`, `2742`, `3147`, and `3279`. FIX: remove this draft from the active tree; the canonical text is already in `preface.tex`.

- [MEDIUM] chapters/frame/preface_sections10_13_draft.tex:1 — PROBLEM: stale closing-section draft, not included anywhere, with line 3 claiming it “replaces the current closing sections (lines 237--352 of preface.tex)” even though the active preface closing material now lives much later (`preface.tex:3731` and `4272`). This is inactive duplicate closure, not a live chapter surface. FIX: remove `preface_sections10_13_draft.tex` from `chapters/frame/`; if any missing material is still needed, patch `preface.tex` directly instead of keeping a second closing draft.

False positives rejected after file read: `chapters/theory/bar_cobar_adjunction.tex`, `chapters/theory/higher_genus.tex`, and `chapters/examples/yangians.tex` are pure dispatchers into theorem-bearing bodies; `chapters/connections/thqg_introduction_supplement.tex` is a live wrapper that inputs a theorem-bearing body; `chapters/connections/thqg_concordance_supplement.tex` is a pure concordance table, not a chapter stub.

## Summary
Checked: 113 | Findings: 8 | Verdict: FAIL


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
session id: 019d840a-fa35-7d82-b22b-3c4b4b9b0419
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


MISSION: UNFINISHED WORK AUDIT.

Find chapters that are <100 lines or have no \begin{theorem}/\begin{proposition}. These are stubs (AP114). For each: should it be developed, merged, or removed?

Run grep/find commands as needed. Be EXHAUSTIVE.
For each finding: PROBLEM (what's unfinished) + FIX (what should be done).
mcp startup: no servers
codex
Auditing the unfinished-work surface now. I’m using `deep-beilinson-audit` to enumerate every chapter-like `.tex` file under the manuscript, identify stubs by the AP114 criteria (`<100` lines or no `\begin{theorem}`/`\begin{proposition}`), then read each flagged file in context and return only grounded findings with exact fixes.
exec
/bin/zsh -lc "pwd && ls -la && sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md && printf '\\n---CLAUDE---\\n' && sed -n '1,220p' CLAUDE.md && printf '\\n---CONCORDANCE---\\n' && sed -n '1,220p' chapters/connections/concordance.tex && printf '\\n---REGISTRY---\\n' && sed -n '1,220p' metadata/theorem_registry.md && printf '\\n---REDTEAM---\\n' && if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar
total 172024
drwxr-xr-x@  85 raeez  staff      2720 Apr 13 01:29 .
drwxr-x---+  96 raeez  staff      3072 Apr 13 01:33 ..
-rw-r--r--@   1 raeez  staff     10244 Apr  7 19:37 .DS_Store
drwxr-xr-x@   3 raeez  staff        96 Apr  7 18:00 .agents
drwxr-xr-x@  50 raeez  staff      1600 Apr 13 01:31 .build_logs
drwxr-xr-x@   8 raeez  staff       256 Apr  9 13:18 .claude
drwxr-xr-x@   4 raeez  staff       128 Apr  7 18:00 .codex
drwxr-xr-x@  16 raeez  staff       512 Apr 13 00:23 .git
-rw-r--r--@   1 raeez  staff      1061 Apr  9 01:04 .gitignore
drwxr-xr-x@   6 raeez  staff       192 Mar 31 08:21 .pytest_cache
drwxr-xr-x@   8 raeez  staff       256 Mar  5 18:51 .venv
-rw-r--r--@   1 raeez  staff     43716 Apr 12 23:03 AGENTS.md
-rw-r--r--@   1 raeez  staff    114861 Apr 12 22:29 CLAUDE.md
-rw-r--r--@   1 raeez  staff      1697 Apr  9 00:43 COMMIT_MESSAGE.txt
-rw-r--r--@   1 raeez  staff  13942000 Apr 12 22:31 Chiral_Bar_Cobar_Duality__Geometric_Realization.pdf
-rw-r--r--@   1 raeez  staff     26796 Apr 12 21:44 FRONTIER.md
-rw-r--r--@   1 raeez  staff     20187 Apr 12 07:53 Makefile
-rw-r--r--@   1 raeez  staff    356279 Apr 12 22:35 N1_koszul_meta.pdf


thinking
**Evaluating audit requirements**

I need to audit the unfinished chapters that are fewer than 100 lines or lacking theorems and propositions. It seems essential to check the file structure, focusing on .tex files, particularly those under a "chapters" or "appendices" directory. The user specifically mentioned chapters, but I wonder if appendices might also fit the criteria, even as stubs. I’ll need to identify the relevant files, read them, and compute the necessary line counts to determine my approach for fixing stubs.
thinking
**Creating an audit plan**

I realize there may be a lot of flagged files to check, so I need to document my findings with exact file and line information. I'll examine `main.tex` to understand which files are included and how the chapter structure is laid out. I might use tools like `rg` on the chapters and consider if appendices should count as chapters too. The existing report, `foundation_audit_chapters_report.md`, could be helpful, but my findings will come from a direct file read. I'll create a step-by-step plan for this audit.
Plan update
Fixing the audit surface first: all `chapters/**/*.tex` files in Vol I, tested against the AP114 stub criteria. I’ll enumerate candidates mechanically, then read every flagged file plus its inclusion context before issuing only grounded findings.
  → Enumerate all chapter `.tex` files with line counts and theorem/proposition presence
  • Read every file flagged by AP114 in local context and classify develop/merge/remove
  • Re-verify flagged surfaces against inclusion structure and produce final findings

thinking
**Organizing chapter files**

I need to enumerate the chapter files efficiently. Using `rg` with `wc` could help, and maybe I should find all chapter files quickly with `rg --files chapters -g '*.tex'`. I could also create a script to count lines and theorems or propositions. I might read `main.tex` to include the list, and using parallel might make the process more efficient. It feels like using a simple shell script with `exec_command` could work without being destructive. I'll proceed with that!
codex
I’ve loaded the repo constitution and I’m switching to the mechanical pass now: enumerate every `chapters/**/*.tex` file, count lines, and mark whether it contains a theorem/proposition block. After that I’ll read each flagged file itself before classifying it as develop, merge, or remove.
exec
/bin/zsh -lc "printf '---INCLUDES---\\n' && rg -n '\\\\(include|input)\\{' main.tex chapters appendices -g '*.tex' && printf '\\n---CHAPTER-STUB-SCAN---\\n' && find chapters -type f -name '*.tex' | sort | while read -r f; do lines="'$(wc -l < "$f" | tr -d '"' '); if rg -q '\\\\begin\\{(theorem|proposition)\\}' \""'$f"; then has_tp=Y; else has_tp=N; fi; printf '"'%s\\t%s\\t%s\\n' \""'$lines" "$has_tp" "$f"; done | sort -n -k1,1' in /Users/raeez/chiral-bar-cobar succeeded in 420ms:
5	N	chapters/theory/bar_cobar_adjunction.tex
6	N	chapters/examples/yangians.tex
6	N	chapters/theory/higher_genus.tex
19	N	chapters/connections/physical_origins.tex
162	N	chapters/connections/thqg_concordance_supplement.tex
211	Y	chapters/connections/feynman_connection.tex
216	Y	chapters/theory/filtered_curved.tex
223	N	chapters/connections/thqg_introduction_supplement.tex
299	Y	chapters/connections/poincare_computations.tex
316	Y	chapters/examples/moonshine.tex
356	Y	chapters/theory/three_invariants.tex
368	Y	chapters/frame/guide_to_main_results.tex
448	Y	chapters/examples/n2_superconformal.tex
495	Y	chapters/examples/level1_bridge.tex
505	Y	chapters/connections/twisted_holography_quantum_gravity.tex
519	Y	chapters/examples/bershadsky_polyakov.tex
581	N	chapters/frame/preface_section1_v2.tex
589	Y	chapters/theory/spectral_sequences.tex
610	Y	chapters/connections/ym_boundary_theory.tex
616	Y	chapters/connections/kontsevich_integral.tex



thinking
**Analyzing flagged files**

I need to read the content of each flagged file, which could be around 12 or maybe 13 files. I should check if they contain any theorems or propositions; there are only 4 files under 100 lines, while the others have no TPs. It seems wise to inspect the whole content or enough to classify them correctly. I might want to use a shell loop to print whole files if they’re short or summarize sections and counts. I’ll need actual line references for the problems as well!
thinking
**Evaluating theorem classifications**

I need to read significant parts of lengthy files since the classification depends on their content. I'm considering using scripts to extract the structure. It looks like these files might be frame or preface chapters, which don't have to include theorems. However, the user refers to them as stubs AP114. I should decide whether to develop, merge, or remove them based on our mission, which indicates that chapters under 100 words or without theorems are stubs.
thinking
**Exploring file structure**

It seems like the project is wrapped with subfiles. I see that higher_genus.tex is included at line 1027, while physical_origins.tex is commented out at line 1399, labeled as a 19-line stub with its content absorbed into Volume II. There might be an inclusion of thqg_concordance_supplement via concordance.tex, but I'll need to read to confirm. I'll also check if sections in preface.tex and the preface drafts are properly included, as well as running a grep for theorem counts and labels in flagged files. A script could be helpful here.
codex
The raw AP114 surface is narrower than the full repo: 13 files under `chapters/` trip the mechanical rule. Some are obvious wrappers, some are active front-matter chapters, and some look like dormant drafts or migrated stubs; I’m reading each one now rather than treating every mechanical hit as the same kind of defect.
exec
/bin/zsh -lc "flagged=(
'chapters/theory/bar_cobar_adjunction.tex'
'chapters/examples/yangians.tex'
'chapters/theory/higher_genus.tex'
'chapters/connections/physical_origins.tex'
'chapters/connections/thqg_concordance_supplement.tex'
'chapters/connections/thqg_introduction_supplement.tex'
'chapters/frame/preface_section1_v2.tex'
'chapters/frame/preface_sections10_13_draft.tex'
'chapters/frame/preface_section1_draft.tex'
'chapters/frame/preface_sections5_9_draft.tex'
'chapters/frame/preface_sections2_4_draft.tex'
'chapters/connections/thqg_preface_supplement.tex'
'chapters/frame/preface.tex'
)
for f in \""'${flagged[@]}"; do
  echo "--- $f ---"
  wc -l "$f"
  echo "tp-count $(rg -c '"'\\\\begin\\{(theorem|proposition)\\}' \""'$f")"
  echo "inputs:"
  rg -n '"'"'^'"\\\\(include|input)\\{' \""'$f" || true
  echo "struct:"
  rg -n '"'"'^'"\\\\(part|chapter|section|subsection|subsubsection)\\{' \""'$f" | head -40 || true
  echo "claim-status:"
  rg -n '"'\\\\ClaimStatus|\\\\begin\\{(lemma|corollary|conjecture|remark|definition|example)\\}' \""'$f" | head -40 || true
  echo "refs-to-file:"
  rg -n -F "$f" main.tex chapters appendices || true
  echo
 done' in /Users/raeez/chiral-bar-cobar succeeded in 178ms:
claim-status:
570:\begin{remark}[The zero-dimensional shadow]\label{rem:pf1-zero-dim}
refs-to-file:

--- chapters/frame/preface_sections10_13_draft.tex ---
     630 chapters/frame/preface_sections10_13_draft.tex
tp-count 
inputs:
struct:
claim-status:
refs-to-file:

--- chapters/frame/preface_section1_draft.tex ---
     677 chapters/frame/preface_section1_draft.tex
tp-count 
inputs:
struct:
claim-status:
656:\begin{remark}[The zero-dimensional shadow]\label{rem:pf1-zero-dim}
refs-to-file:

thinking
**Investigating file references**

I'm trying to figure out why the refs-to-file didn’t show up. Maybe it’s because I’m using the path string without the extension. I think I might need to grep for the basename. For wrappers, they might not be showing due to searching for the exact path. I'll also want to check the active/inactive status and see if any draft files are included. It looks like I’ll use rg for basenames to narrow it down.
exec
/bin/zsh -lc 'for f in chapters/theory/bar_cobar_adjunction.tex chapters/examples/yangians.tex chapters/theory/higher_genus.tex chapters/connections/physical_origins.tex chapters/connections/thqg_concordance_supplement.tex chapters/connections/thqg_introduction_supplement.tex chapters/frame/preface_section1_v2.tex chapters/frame/preface_sections10_13_draft.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/frame/preface_sections2_4_draft.tex chapters/connections/thqg_preface_supplement.tex chapters/frame/preface.tex; do b=$(basename "$f" .tex); echo "--- $b ---"; rg -n "$b" main.tex chapters appendices || true; echo; done' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
--- bar_cobar_adjunction ---
main.tex:996:\include{chapters/theory/bar_cobar_adjunction}
main.tex:1754: % lem:pushforward-preserves-qi — real label in bar_cobar_adjunction_inversion.tex; phantom removed
chapters/theory/bar_cobar_adjunction_inversion.tex:3:%% The first half of this chapter (bar_cobar_adjunction_curved.tex)
chapters/theory/bar_cobar_adjunction.tex:1:% Dispatcher: bar_cobar_adjunction.tex
chapters/theory/bar_cobar_adjunction.tex:4:\input{chapters/theory/bar_cobar_adjunction_curved}
chapters/theory/bar_cobar_adjunction.tex:5:\input{chapters/theory/bar_cobar_adjunction_inversion}

--- yangians ---
main.tex:1328:\input{chapters/examples/yangians}
main.tex:1698: % cor:dk23-all-types: real label in yangians_drinfeld_kohno.tex (always compiled)
chapters/examples/lattice_foundations.tex:2125:Chapter~\ref{chap:yangians}.
chapters/examples/lattice_foundations.tex:3502: (Chapter~\ref{chap:yangians}): start with the RTT relations and
chapters/examples/lattice_foundations.tex:3558: \textup{(}Chapter~\ref{chap:yangians}\textup{)}}} \\
chapters/examples/lattice_foundations.tex:3625:the Yangian setting (Chapter~\ref{chap:yangians},
chapters/examples/lattice_foundations.tex:3858:(Chapter~\ref{chap:yangians}):
chapters/examples/yangians.tex:1:% Dispatcher: yangians.tex
chapters/examples/yangians.tex:4:\input{chapters/examples/yangians_foundations}
chapters/examples/yangians.tex:5:\input{chapters/examples/yangians_computations}
chapters/examples/yangians.tex:6:\input{chapters/examples/yangians_drinfeld_kohno}










thinking
**Evaluating chapter files**

I’m considering the dormant draft files under chapters in the repository. I need to determine if each finding should be flagged. I’m wondering if wrappers should be counted since they’re intentional dispatcher files and under 100 lines. They aggregate subfiles. According to AP114, a chapter file should be under 100 lines or lack theorems. I need to read them to see if they’re intentional dispatchers, as they might not be stubs but instead useful wrappers.
thinking
**Assessing flagged files**

I need to likely exclude wrappers from my findings and summarize what I checked. I should note that I flagged N files and marked M findings after excluding false positives. My focus needs to be on real stubs. I should look at each flagged file to determine if they are false positives or unfinished. For example, inspecting the entire "physical_origins" file and checking "thqg_concordance_supplement" could reveal it’s not a stub if it’s intentionally a tabular supplement, but the user asked specifically for chapters without theorems or propositions.
thinking
**Clarifying chapter identification**

I’m considering whether to exclude certain files like AP114, which seems to involve metadata supplements rather than actual chapters. I need to figure out if it’s false positives. Also, thqg_introduction_supplement appears to support section-level content, not stand-alone chapters, but still may belong in chapters. I need to focus on identifying main chapter files while adhering to the user’s request for files with less than 100 lines or without theorems. It's about defining the audit surface correctly.
thinking
**Auditing flagged files**

I’m thinking we need to classify files during the audit: some might get removed as “dead stubs,” some merged as support fragments, and others may turn out to be false positives that we don’t need to report. If files in the `chapters/` directory lack theorems or propositions, they could still be unfinished. The preface, for example, seems heavy but might not fulfill the theorem requirement. The user's specifications suggest that chapters under 100 lines or lacking these elements are considered stubs, so I’ll have to weigh these criteria carefully.
thinking
**Developing the preface**

It seems that the active preface should actually be developed rather than removed. I’m contemplating the best approach to fix it—maybe promoting existing claims to numbered propositions or moving mathematical content into chapters that bear theorems would work. I could also keep the preface to just 2-3 pages for orientation. It's crucial that I read enough to understand the content and its unfinished elements without making assumptions, so I might reference comments like "To be integrated into preface.tex" in draft files.
thinking
**Evaluating draft files**

I need to make an exact fix: I should remove the draft files and keep only the canonical preface.tex. However, I need to make sure they're not included and that the content is largely duplicated. I could consider using `diff -q`, but it might not show them as identical since I've actively integrated and expanded the preface. The comments do say "To be integrated into preface.tex," indicating they are still in draft status. Should I reference those comment lines and their absence elsewhere?
thinking
**Considering document integration**

I need to confirm whether the content is included in preface.tex or the main document. It seems like it could be an orphan supplement without any theorems or propositions, which raises the question of whether to merge it or remove it entirely. If the comment suggests it's supposed to be inserted near the end but isn't, that needs fixing. I should check if this content belongs to preface or connections/frontier, or if it should stand alone. I might also check for other instances of the material.
thinking
**Examining document structure**

I need to take a closer look at the structure and lines of the document. It looks like I could use a search tool on the sections. It seems the thqg_introduction_supplement might be included through heisenberg_frame, yet it doesn't contain any theorems or propositions. The user is asking for chapters, but this could just be a section-level narrative supplement. Since it has 223 lines and no formalized claims, it might be unfinished. I’ll need to clarify this.
thinking
**Planning an audit**

I need to audit all mechanically flagged `.tex` surfaces under `chapters/`. There are likely some false positives since some files are dispatchers or supplements rather than standalone chapters. I should reference specific lines and fixes, since the findings could be more than just a few.

I'll check if there are some files under 100 lines that lack theorems or propositions. It’s important not to report false positives, but maybe I’ll note that we checked 13 flagged surfaces and found 9. Let’s inspect all flagged files in chunks and use line numbers for short files!
thinking
**Drafting preface files**

For the preface draft files, I think I should focus on lines 1-40 and any lines with unique labels or comments. In `preface.tex`, I'll check the initial lines and the structure, ensuring there are no theorems, propositions, or conjectures. I can search for specific commands like `\begin{(lemma|remark|conjecture|corollary|definition)}` to identify any claim surfaces. It’s good to confirm we know there shouldn't be any theorems or propositions in there. Let’s get started!
exec
/bin/zsh -lc "printf '--- short files full ---\\n'
for f in \\
  chapters/theory/bar_cobar_adjunction.tex \\
  chapters/examples/yangians.tex \\
  chapters/theory/higher_genus.tex \\
  chapters/connections/physical_origins.tex; do
  echo \"FILE "'$f"; nl -ba "$f"; echo; done

printf '"'--- targeted excerpts ---\\n'
for f in \\
  chapters/connections/thqg_concordance_supplement.tex \\
  chapters/connections/thqg_introduction_supplement.tex \\
  chapters/frame/preface_section1_v2.tex \\
  chapters/frame/preface_sections10_13_draft.tex \\
  chapters/frame/preface_section1_draft.tex \\
  chapters/frame/preface_sections5_9_draft.tex \\
  chapters/frame/preface_sections2_4_draft.tex \\
  chapters/connections/thqg_preface_supplement.tex \\
  chapters/frame/preface.tex; do
  echo \"FILE "'$f"
  echo '"'-- head --'; nl -ba \""'$f" | sed -n '"'1,40p'
  echo '-- key claims/struct --'; rg -n '"'^'"\\\\(chapter|section|subsection)|\\\\begin\\{(remark|conjecture|definition|lemma|corollary|example)\\}|To be integrated|Inserted near the end|Draft|supplement|table|tabular|longtable' \""'$f" | head -80
  echo '"'-- tail --'; nl -ba \""'$f" | tail -25
  echo
 done' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
--- short files full ---
FILE chapters/theory/bar_cobar_adjunction.tex
     1	% Dispatcher: bar_cobar_adjunction.tex
     2	% Split into two semantic units for maintainability.
     3	% The compiled PDF is byte-for-byte identical.
     4	\input{chapters/theory/bar_cobar_adjunction_curved}
     5	\input{chapters/theory/bar_cobar_adjunction_inversion}

FILE chapters/examples/yangians.tex
     1	% Dispatcher: yangians.tex
     2	% Split into three semantic units for maintainability.
     3	% The compiled PDF is byte-for-byte identical.
     4	\input{chapters/examples/yangians_foundations}
     5	\input{chapters/examples/yangians_computations}
     6	\input{chapters/examples/yangians_drinfeld_kohno}

FILE chapters/theory/higher_genus.tex
     1	% Dispatcher: higher_genus.tex
     2	% Split into three semantic units for maintainability.
     3	% The compiled PDF is byte-for-byte identical.

thinking
**Researching section titles**

I'm considering whether the preface contains a unique section title like "Twisted holography and quantum gravity." It seems possible it could be integrated in some way. I’ll definitely check for that; it would be interesting! I might find clues or insights that relate to the overall theme. So, let’s search for that specific title to see if it appears. It could really enhance my understanding of the text!
codex
The false-positive pass is done for the tiny wrapper files: `bar_cobar_adjunction.tex`, `higher_genus.tex`, and `yangians.tex` are just dispatchers that immediately `\input` theorem-bearing bodies. I’m now on the subtler unfinished surfaces: dead migrated stubs, dormant draft fragments, and active front-matter chapters that carry technical load without any theorem/proposition boundary.
exec
/bin/zsh -lc "printf '--- preface / supplement cross-checks ---\\n'
rg -n 'Twisted holography and quantum gravity|The open/closed world|The holographic modular Koszul datum|Perturbative finiteness|Gravitational complexity|The modular bootstrap|The critical-string dichotomy' chapters/frame/preface.tex chapters/connections/thqg_preface_supplement.tex
printf '\\n--- theorem/proposition/cor/lem env counts in flagged long files ---\\n'
for f in chapters/connections/thqg_concordance_supplement.tex chapters/connections/thqg_introduction_supplement.tex chapters/frame/preface_section1_v2.tex chapters/frame/preface_sections10_13_draft.tex chapters/frame/preface_section1_draft.tex chapters/frame/preface_sections5_9_draft.tex chapters/frame/preface_sections2_4_draft.tex chapters/connections/thqg_preface_supplement.tex chapters/frame/preface.tex; do
  echo \""'$f"
  printf '"' theorem/proposition: '; rg -o '\\\\begin\\{(theorem|proposition)\\}' \""'$f" | wc -l | tr -d '"' '
  printf ' lemma/cor/conj/rem/def/example: '; rg -o '\\\\begin\\{(lemma|corollary|conjecture|remark|definition|example)\\}' \""'$f" | wc -l | tr -d '"' '
 done
printf '\\n--- exact inclusion of draft/supplement files ---\\n'
for b in preface_section1_v2 preface_sections10_13_draft preface_section1_draft preface_sections5_9_draft preface_sections2_4_draft thqg_preface_supplement; do
  echo \""'$b"
  rg -n "$b" main.tex chapters appendices || true
  echo
 done
printf '"'\\n--- preface section 4-13 markers ---\\n'
rg -n '"'^'"\\\\section\\*\\{(4|5|6|7|8|9|10|11|12|13)\\.' chapters/frame/preface.tex | head -40
printf '\\n--- preface theorem section excerpt ---\\n'
nl -ba chapters/frame/preface.tex | sed -n '1190,1275p'
printf '\\n--- thqg supplement section markers ---\\n'
rg -n '"'^'"\\\\subsection\\*\\{' chapters/connections/thqg_preface_supplement.tex | head -40" in /Users/raeez/chiral-bar-cobar succeeded in 75ms:

preface_sections2_4_draft
chapters/frame/preface_sections2_4_draft.tex:1:% preface_sections2_4_draft.tex — Sections 2-4 of the Restored Preface

thqg_preface_supplement


--- preface section 4-13 markers ---
1737:\section*{4.\quad The universal Maurer--Cartan element}
2161:\section*{5.\quad The modular tangent complex and Chern--Weil theory}
2435:\section*{6.\quad The shadow obstruction tower}
2742:\section*{7.\quad The standard landscape}
3147:\section*{8.\quad Arithmetic of the shadow obstruction tower}
3279:\section*{9.\quad The Koszulness programme}
3522:\section*{10.\quad The $E_n$ operadic circle}

--- preface theorem section excerpt ---
  1190	The collision divisors are the algebraic boundary (controlled by
  1191	the Borcherds identity); the degeneration divisors are the
  1192	geometric boundary (controlled by the period map and the
exec
/bin/zsh -lc "printf 'thqg_introduction_supplement_body theorem/proposition count: '; rg -o '\\\\begin\\{(theorem|proposition)\\}' chapters/connections/thqg_introduction_supplement_body.tex | wc -l | tr -d ' '; printf '\\n'
printf 'thqg_concordance_supplement direct theorem refs count: '; rg -o 'Theorem~\\\\ref|Proposition~\\\\ref|Corollary~\\\\ref' chapters/connections/thqg_concordance_supplement.tex | wc -l | tr -d ' '; printf '\\n'
printf 'preface theorem-like inline labels count: '; rg -n '\\\\noindent\\\\textbf\\{Theorem~[A-ZH]' chapters/frame/preface.tex | wc -l | tr -d ' '; printf '\\n'
printf 'thqg_preface_supplement theorem-like inline labels count: '; rg -n '\\\\noindent\\\\textbf\\{(Theorem|Proposition|Corollary)' chapters/connections/thqg_preface_supplement.tex | wc -l | tr -d ' '; printf '\\n'
printf 'preface section markers 10-13: \\n'; rg -n '"'^'"\\\\section\\*\\{(10|11|12|13)\\.' chapters/frame/preface.tex" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
thqg_introduction_supplement_body theorem/proposition count: 8

thqg_concordance_supplement direct theorem refs count: 0

preface theorem-like inline labels count: 5

thqg_preface_supplement theorem-like inline labels count: 0

preface section markers 10-13: 
3522:\section*{10.\quad The $E_n$ operadic circle}

thinking
**Checking sections and formatting**

I should look over the preface sections 11-13. It seems like the section numbering might use bold, and I'm curious if that's standard. Let's also search a bit beyond the 3520 mark to gather more context or details. I wonder what I'll find that could help clarify things! It's a good idea to double-check these elements before moving forward. Every little detail can make a difference, right?
exec
/bin/zsh -lc "nl -ba chapters/frame/preface.tex | sed -n '3518,4305p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  3518	invisible to $\Sigma_n$-coinvariants and therefore absent from the
  3519	symmetric shadow. The natural habitat for both structures
  3520	simultaneously is three-dimensional.
  3521	
  3522	\section*{10.\quad The $E_n$ operadic circle}
  3523	
  3524	The five theorems above live in the symmetric bar
  3525	$\barB^\Sigma(\cA)$: they are invariants that survive the
  3526	averaging map $\mathrm{av}\colon\barB^{\mathrm{ord}}(\cA)
  3527	\to\barB^\Sigma(\cA)$. The $E_n$ operadic circle explains
  3528	why the averaging map exists, what it loses, and how the
  3529	lost information can be recovered.
  3530	
  3531	\subsection*{10.1.\enspace Five arrows}
  3532	
  3533	The circle is a sequence of five functorial operations, each
  3534	changing the operadic level by one:
  3535	\[
  3536	E_3(\text{bulk})
  3537	\;\xrightarrow{\;\text{restrict}\;}




thinking
**Deciding on document structure**

I’m weighing options for merging the theorem summary into a specific file while considering cutting down another to nontechnical content. Alternatively, I could formalize the inline theorem summaries into actual environments if I keep the preface as a technical chapter. The user has asked for a specific fix, so I need to focus on one approach. It’s about deciding whether to develop, merge, or remove content. I need to make a clear choice here!
thinking
**Considering classification**

Since the preface is active, it seems like “develop” is the classification intended here. I believe I need to preserve the file while also adding some formal claim scaffolding. I want to make sure I’m capturing the essence of the document while enhancing its structure. By doing that, I can ensure it meets the required standards. It feels like a careful balance between maintaining the original intent and making improvements, which I’m aiming to achieve!
thinking
**Evaluating document structure**

I'm assessing how to restate theorems A/B/C/D/H and highlight principles like the four-test interface with explicit labels. However, I wonder if I can say "promote `\begin{principle}`," since the task mentions theorem/proposition. To fix this, adding a theorem could work, but the preface is quite lengthy. Maybe I should split out technical sections 1-10, merging them into the introduction while keeping the narrative. Given the duplication in the preface, merging seems to be a better approach.
thinking
**Assessing document integration**

The presence of multiple draft files indicates that the preface might be bloated and unstable. It feels unfinished, especially since it's 4374 lines without theorems. Merging this into the guide to main results could be a solution, so I’ll check `chapters/frame/guide_to_main_results.tex` to see if there's a suitable spot for it. The user only asked for an audit, but I can reference the target file accurately. If `guide_to_main_results.tex` is invoked in `main.tex`, I'll consider merging the theorem summary there. I'll need to inspect the structure to confirm.
codex
I’m checking the active front matter against the actual inclusion graph before I lock the recommendations. The key distinction is whether a file is a live compiled chapter, a wrapper around theorem-bearing bodies, or an orphaned draft that sits in `chapters/` with no inclusion path.
exec
/bin/zsh -lc "printf '--- guide_to_main_results head/struct ---\\n'
nl -ba chapters/frame/guide_to_main_results.tex | sed -n '1,120p'
printf '\\n--- guide theorem/proposition counts ---\\n'
printf 'theorem/proposition: '; rg -o '\\\\begin\\{(theorem|proposition)\\}' chapters/frame/guide_to_main_results.tex | wc -l | tr -d ' '; printf '\\n'
printf 'other claim envs: '; rg -o '\\\\begin\\{(lemma|corollary|conjecture|remark|definition|example|principle)\\}' chapters/frame/guide_to_main_results.tex | wc -l | tr -d ' '; printf '\\n'
printf '\\n--- preface draft labels duplicated in preface.tex ---\\n'
for label in rem:pf1-zero-dim eq:preface-feynman-sum eq:preface-fcom eq:preface-convolution-ladder eq:preface-gmod; do
  echo \""'$label"
  rg -n "$label" chapters/frame/preface*.tex chapters/connections/thqg_preface_supplement.tex
  echo
 done' in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
--- guide_to_main_results head/struct ---
     1	% ======================================================================
     2	% GUIDE TO MAIN RESULTS
     3	% A compact reference for the five main theorems and their dependencies.
     4	% ======================================================================
     5	
     6	\chapter*{Guide to main results}
     7	\addcontentsline{toc}{chapter}{Guide to main results}
     8	\label{ch:guide}%
     9	
    10	\noindent
    11	The principal results, with labels, locations, and logical
    12	dependencies. All five theorems hold for augmented chiral
    13	algebras~$\cA$ on a smooth projective curve~$X$ satisfying the
    14	standing finiteness conditions (\S\ref{sec:standing-assumptions}).
    15	
    16	\medskip
    17	
    18	\renewcommand{\arraystretch}{1.3}
    19	\begin{longtable}{@{}lp{8.5cm}l@{}}



thinking
**Evaluating guide structure**

There's a guide to the main results that seems to already exist, possibly with one theorem or proposition. I’m considering merging the theorem-summary content into the guide or just keeping an overview. I should inspect the top of the guide to see if it overlaps with what the preface duplicates. I also need to confirm sections 10-13 of the preface. It looks like there’s a draft for sections 10-13, but that may not be fully integrated yet. I’ll need to check for shared closing lines.
thinking
**Assessing draft integration**

The draft is partially integrated, which is good. I might check line 623 to see if the content appears at the preface's tail, and if so, it should be removed. I need to look for labels or phrases from sections 5-9 in the preface since many are already present in specific lines. I might want to cite top comments and existing duplicates. Also, I should consider checking for duplicates in `preface_section1_v2` against `preface.tex`. The focus here is on streamlining and ensuring everything is accurately referenced.
thinking
**Checking for references**

I need to search for any references to `chap:physical-origins` to see if they still exist. I'll use a search command to look for `physical-origins` and `programme-origins`. Since these are commented out, it’s possible that any references I find are outdated. I just want to ensure everything is up-to-date and relevant. It'll be good to clarify what's still applicable and what might need to be removed or updated.
exec
/bin/zsh -lc "printf '--- physical_origins refs ---\\n'
rg -n 'chap:physical-origins|rem:programme-origins|Physical origins' main.tex chapters appendices metadata README.md || true
printf '\\n--- thqg_preface_supplement refs/overlap ---\\n'
rg -n 'eq:holo-datum-preface-supp|eq:hs-sewing-preface-supp|eq:Ahat-preface-supp|eq:mc-g0-a3-preface-supp' chapters/main.tex main.tex chapters appendices metadata README.md || true" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
--- physical_origins refs ---
metadata/label_index.json:498:  "chap:physical-origins": {
metadata/label_index.json:34674:  "rem:programme-origins": {
chapters/connections/physical_origins.tex:1:\chapter{Physical origins}
chapters/connections/physical_origins.tex:2:\label{chap:physical-origins}
chapters/connections/physical_origins.tex:3:\label{rem:programme-origins}

--- thqg_preface_supplement refs/overlap ---
rg: chapters/main.tex: No such file or directory (os error 2)
metadata/label_index.json:8662:  "eq:Ahat-preface-supp": {
metadata/label_index.json:14198:  "eq:holo-datum-preface-supp": {
metadata/label_index.json:14262:  "eq:hs-sewing-preface-supp": {
metadata/label_index.json:15326:  "eq:mc-g0-a3-preface-supp": {
chapters/connections/thqg_preface_supplement.tex:50:\begin{equation}\label{eq:holo-datum-preface-supp}
chapters/connections/thqg_preface_supplement.tex:489:\begin{equation}\label{eq:hs-sewing-preface-supp}
chapters/connections/thqg_preface_supplement.tex:500:sector growth, \emph{then}~\eqref{eq:hs-sewing-preface-supp}
chapters/connections/thqg_preface_supplement.tex:558:\begin{equation}\label{eq:Ahat-preface-supp}
chapters/connections/thqg_preface_supplement.tex:575:equation~\eqref{eq:Ahat-preface-supp} states that, on the proved
chapters/connections/thqg_preface_supplement.tex:1208:\begin{equation}\label{eq:mc-g0-a3-preface-supp}
chapters/connections/thqg_preface_supplement.tex:1247:The MC equation~\eqref{eq:mc-g0-a3-preface-supp}, after extracting



thinking
**Evaluating file integration**

I need to note that the metadata might include labels for obsolete files, possibly compiled at some point. However, since the user is asking about file contents, this might not be necessary. I should inspect `metadata/theorem_registry` for origins, but that may not actually be relevant. It seems that the `thqg_preface_supplement.tex` has metadata labels, although the file isn't included anywhere, indicating it might be outdated. I need to decide if I should merge or remove the draft `preface_sections10_13_draft`, as its content overlaps with `preface.tex`.
thinking
**Identifying duplicate content**

I could cite the duplicated phrase at preface.tex lines 3731 or 4272. The exact fix would be to remove the unnecessary file and keep the merged text in `preface.tex`. It seems that the labels for sections 2-4 in the draft are also duplicated in the preface. I need to check if sections 5-9 have similar issues as their headings are exact titles too. If they are, I should remove them as well. I should include evidence from the other file to clarify the problem within the fix description.
thinking
**Calculating file counts**

I need to compute the total number of `.tex` files under the chapters. This should be straightforward, so I'll try to do it quickly. I also want to count the flagged files, which is 13, and there are 5 false positives. I'll use the necessary commands to get this information efficiently. It feels a bit tedious, but I'm getting there!
codex
I’ve narrowed the audit to the genuine unfinished surfaces. The remaining work is one last verification pass: total chapter-file count, exact flagged count, and whether any dormant draft is secretly included through a second path before I finalize the findings.
exec
/bin/zsh -lc "printf 'total_tex='; find chapters -type f -name '*.tex' | wc -l | tr -d ' '; printf '\\n'
printf 'flagged_stub_surface='; find chapters -type f -name '*.tex' | sort | while read -r f; do lines="'$(wc -l < "$f" | tr -d '"' '); if [ \""'$lines" -lt 100 ] || ! rg -q '"'\\\\begin\\{(theorem|proposition)\\}' \""'$f"; then echo "$f"; fi; done | wc -l | tr -d '"' '; printf '\\n'
printf 'preface_draft_inclusions='; rg -n 'preface_section1_v2|preface_section1_draft|preface_sections2_4_draft|preface_sections5_9_draft|preface_sections10_13_draft' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'
printf 'thqg_preface_supplement_inclusions='; rg -n 'thqg_preface_supplement' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'
printf 'physical_origins_inclusions='; rg -n 'chapters/connections/physical_origins|physical_origins' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'" in /Users/raeez/chiral-bar-cobar succeeded in 421ms:
13

preface_draft_inclusions=4

thqg_preface_supplement_inclusions=0

physical_origins_inclusions=1



thinking
**Considering draft inclusions**

I need to note that I should have a count of preface draft inclusions at 4 because there are references in the preface files comments. Maybe I won't actually include those. I already understand there are no input or include lines, but I could confirm by searching for any matches in the current context. If necessary, I’ll follow through with that check to be sure.
thinking
**Considering physical origins**

I'm thinking about how physical origins can be included or counted, which seems like a main comment. It feels important to note whether I'm actually including or inputting occurrences. I should do a quick count to see how many I've included. Getting this right is crucial, and I want to make sure I'm clear about all the inputs or occurrences being counted. Let's check and confirm that next!
exec
/bin/zsh -lc "printf 'actual_preface_draft_input_include='; rg -n '\\\\(input|include)\\{["'^}]*preface_(section1_v2|section1_draft|sections2_4_draft|sections5_9_draft|sections10_13_draft)'"' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'
printf 'actual_thqg_preface_supplement_input_include='; rg -n '\\\\(input|include)\\{["'^}]*thqg_preface_supplement'"' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'
printf 'actual_physical_origins_input_include='; rg -n '"'^[''^%]*'"\\\\(input|include)\\{["'^}]*physical_origins'"' main.tex chapters appendices | wc -l | tr -d ' '; printf '\\n'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
actual_preface_draft_input_include=0

actual_thqg_preface_supplement_input_include=0

actual_physical_origins_input_include=0






thinking
**Determining audit priorities**

The user has an unfinished work audit, and it seems important to choose the right documents. I’m considering which items to categorize by priority. It looks like I should label "preface.tex" and "thqg_preface_supplement" as HIGH. Then I might label "physical_origins" as HIGH too, because it has an active surface label despite being dead. I think drafts should be marked as MEDIUM, while I definitely want to avoid marking anything as LOW.
thinking
**Summarizing counts for report**

I’m thinking about how to summarize the counts clearly. I might go with “Checked: 113 files scanned, 13 AP114 hits read, Findings: 8, Verdict: FAIL.” However, the contract specifies the format should be “Checked: N | Findings: N | Verdict: PASS/FAIL.” So, I need to ensure I'm following that requirement while still conveying the necessary details. Let's make sure it’s done accurately!
thinking
**Clarifying draft notes**

I need to note that the `preface_sections10_13_draft` duplicates a closing phrase at preface 4272, so I should search for that. I might mention `The open/closed world (VolumeII)` and the phrase `Every formula in this preface has been verified`. It’s also worth pointing out that `thqg_preface_supplement` has no inclusion path since we verified zero input occurrences. Additionally, `physical_origins.tex` mentions that its content is absorbed into Volume II, which might be useful for explaining the dead chapter stub issue.
thinking
**Deciding on format details**

I might not mention `main.tex` in the summary since it doesn't fit the file:line format, but I can refer to it in prose. I'll also consider including findings for `preface.tex` using the exact lines, such as 1200 or 1204. It's all about keeping the information clear and easily referenced, so the user can understand the context without any confusion. I want to make sure my summary remains consistent and accurate!
thinking
**Drafting detailed revisions**

The user asked for a precise separation of each item, so I’ll need to draft them carefully. For instance, with "preface.tex," I plan to merge it. For "thqg_preface_supplement.tex," I need to decide whether to remove it or move it to Volume II. I think the right call is to remove it, but if any content is necessary, I'll rehome it. Then, I’ll note that files like "physical_origins.tex," and several "preface_sections" need to be removed. Finally, I want to address any findings clearly.
codex
- [HIGH] chapters/frame/preface.tex:1198 — PROBLEM: the compiled preface is a 4,374-line technical chapter with zero `\begin{theorem}`/`\begin{proposition}` blocks, yet Section “The five theorems” states Theorems A/B/C/D/H as unnumbered bold prose at lines 1204–1253. That leaves a live, load-bearing chapter outside theorem/status discipline, while [chapters/frame/guide_to_main_results.tex](/Users/raeez/chiral-bar-cobar/chapters/frame/guide_to_main_results.tex:6) already exists as the theorem digest. FIX: merge the theorem-summary material out of `preface.tex` into `guide_to_main_results.tex` and cut `preface.tex` back to actual front matter; if any technical claims remain in the preface, restate them as real theorem/proposition environments with the canonical labels instead of inline bold paragraphs.

- [HIGH] chapters/connections/thqg_preface_supplement.tex:1 — PROBLEM: this is a 2,056-line theorem-free pseudo-chapter whose own header says “Inserted near the end of the preface chapter via `\input`” at line 2, but it has no actual `\input`/`\include` path anywhere in `main.tex`, `preface.tex`, or other chapter files. It is an orphaned, uncompiled frontier surface living in the active `chapters/` tree. FIX: remove `thqg_preface_supplement.tex` from `chapters/connections/`; if any prose is still wanted, rehome it into the actual Volume II front matter before deletion, not as a dormant Vol I supplement.

- [HIGH] chapters/connections/physical_origins.tex:1 — PROBLEM: this is a 19-line chapter stub whose entire body says the chapter “has been absorbed into Volume II” (lines 5–19); `main.tex:1399` keeps it commented out as “19-line stub; content absorbed into Vol II.” This is dead chapter debris, not live manuscript content. FIX: remove `physical_origins.tex` from `chapters/connections/` and rebuild metadata so `chap:physical-origins` / `rem:programme-origins` disappear from the active label surface.

- [MEDIUM] chapters/frame/preface_section1_v2.tex:1 — PROBLEM: orphan alternate Section 1 draft, not included anywhere, with no theorem/proposition blocks and a duplicate live label `rem:pf1-zero-dim` at line 570 that already exists in `preface.tex:832`. FIX: remove this file from `chapters/frame/` (or move it to `archive/`), and keep `preface.tex` as the sole canonical Section 1 source.

- [MEDIUM] chapters/frame/preface_section1_draft.tex:1 — PROBLEM: the file explicitly says “To be integrated into preface.tex” at line 2, is not actually included anywhere, has no theorem/proposition blocks, and duplicates `rem:pf1-zero-dim` at line 656 already present in `preface.tex:832`. FIX: remove the draft from `chapters/frame/` or archive it outside the active chapter tree; do not keep an unintegrated duplicate beside the compiled preface.

- [MEDIUM] chapters/frame/preface_sections2_4_draft.tex:1 — PROBLEM: explicit orphan draft (“To be integrated into preface.tex”), not included anywhere, and it duplicates live preface labels `eq:preface-feynman-sum` (line 417 vs. `preface.tex:1330`), `eq:preface-fcom` (445 vs. 1358), `eq:preface-convolution-ladder` (485 vs. 1398), and `eq:preface-gmod` (516 vs. 1438). FIX: remove this draft from `chapters/frame/` and keep the merged material in `preface.tex` only.

- [MEDIUM] chapters/frame/preface_sections5_9_draft.tex:1 — PROBLEM: another explicit orphan draft (“To be integrated into preface.tex”), with no theorem/proposition blocks and section range already present in the compiled preface as Sections 5–9 at `preface.tex:2161`, `2435`, `2742`, `3147`, and `3279`. FIX: remove this draft from the active tree; the canonical text is already in `preface.tex`.

- [MEDIUM] chapters/frame/preface_sections10_13_draft.tex:1 — PROBLEM: stale closing-section draft, not included anywhere, with line 3 claiming it “replaces the current closing sections (lines 237--352 of preface.tex)” even though the active preface closing material now lives much later (`preface.tex:3731` and `4272`). This is inactive duplicate closure, not a live chapter surface. FIX: remove `preface_sections10_13_draft.tex` from `chapters/frame/`; if any missing material is still needed, patch `preface.tex` directly instead of keeping a second closing draft.

False positives rejected after file read: `chapters/theory/bar_cobar_adjunction.tex`, `chapters/theory/higher_genus.tex`, and `chapters/examples/yangians.tex` are pure dispatchers into theorem-bearing bodies; `chapters/connections/thqg_introduction_supplement.tex` is a live wrapper that inputs a theorem-bearing body; `chapters/connections/thqg_concordance_supplement.tex` is a pure concordance table, not a chapter stub.

## Summary
Checked: 113 | Findings: 8 | Verdict: FAIL
tokens used
100,524
