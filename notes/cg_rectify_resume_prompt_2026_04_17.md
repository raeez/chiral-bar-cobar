# Clean-session kick-start prompt (paste this, verbatim, into a fresh Claude session)

---

You are resuming a chriss-ginzburg-rectify programme on Volume I of the *Modular Koszul Duality* monograph. The prior session (2026-04-17) cut corners — it ran only a single screening grep for cosmetic prose slop and declared files "CONVERGED" without running any of the five skill phases. You are the redo.

Before doing anything else, do the following, in order:

1. Read `/Users/raeez/chiral-bar-cobar/CLAUDE.md` in full. Internalize the hot zone (HZ-1 through HZ-10), the AP1–AP233 catalogue, the Pre-Edit Verification Protocol templates (PE-1 through PE-12), and the five-objects/five-E_1-chiral-notions/three-Hochschild distinctions.
2. Read `/Users/raeez/chiral-bar-cobar/notes/cg_rectify_redo_queue_2026_04_17.md`. This is the authoritative REDO queue. Every `[ ]` entry is pending. Editorial and shallow-screen passes from 2026-04-17 do not count as done — the files stay `[ ]` until they pass the full five-phase audit.
3. Read `/Users/raeez/chiral-bar-cobar/notes/cg_rectify_kickstart.md` for the cron architecture Vol III uses (one chapter per firing, fresh context each tick, `RemoteTrigger` with `environment_id`). Decide whether to keep driving interactively or install a cron. Vol III's reference: trigger `trig_01EwyA6My2f9sdmBdMYCcMZD`, queue file `notes/chriss_ginzburg_full_rectify_queue.md`.
4. Claim the next `[ ]` file at the top of the queue — do not skip around, do not pick the short ones, do not pattern-match across files.

For the claimed file, invoke the skill via `Skill(skill="chriss-ginzburg-rectify", args="<absolute path>")` and execute ALL FIVE phases. No shortcut is acceptable:

- **Phase 1**: read the entire file end-to-end (every line, not samples). Produce the 7-heading diagnostic (narrative thread, motivation gaps, define-before-use violations, opening/closing, physical insight labels, prose slop, formula red flags). Do not edit yet.
- **Phase 2**: platonic-ideal assessment. Answer the six questions (organizing question, climax, ideal section sequence, cut list, missing list, scope envelope). Execute structural edits only if `>= SERIOUS` issues exist. Never delete mathematical content — use `% MOVED TO <target>` stubs.
- **Phase 3**: chunk-by-chunk 5-gate loop, chunks of ~50–100 lines. Gate 1 (Mathematical Truth) requires recomputing every formula from first principles against `chapters/examples/landscape_census.tex` and the `compute/` layer — do NOT pattern-match against other occurrences (AP3). Gate 2 (Define-Before-Use) is HARD: every symbol defined at or before first use, including standard concepts with parenthetical first-principles definitions. Gate 3 (Concept Motivation) is HARD: every definition preceded by the question it answers. Gate 4 (Physical Realization) labels each physical claim theorem/heuristic/metaphor and verifies OPE/κ/factorization correctness. Gate 5 (Reconstitution) is the Chriss-Ginzburg standard: show-don't-tell, precise-moment pacing, synthesis, inevitability, courage in identifications, prose at the Kac-Etingof-Bezrukavnikov-Gelfand level. Each chunk advances only when ALL FIVE gates pass at severity ≥ MODERATE. Safety valve at 11 iterations: flag with `% RECTIFICATION-FLAG: [gate, reason]` and advance. Build after every 3 fixes. Grep all three volumes after every formula change (AP5).
- **Phase 4**: spawn three adversarial re-audit agents via `Agent(subagent_type="general-purpose", run_in_background=true)` — RED (falsify new formulas/proofs/definitions/claims), BLUE (check formulas against `landscape_census.tex` and compute layer, cross-references, AP5 consistency, build), GREEN (fifteen-peak standard, connective-tissue standard, Inventiones-referee read). Dispatch in a single message. Re-enter Phase 3 on affected chunks only if any agent finds severity ≥ MODERATE.
- **Phase 5**: re-read with fresh eyes. Build all three volumes (`pkill -9 -f pdflatex; sleep 2; cd ~/chiral-bar-cobar && make fast`; same for `~/chiral-bar-cobar-vol2` and `~/calabi-yau-quantum-groups`). Run `make test`. Report chunks/iterations/findings-by-severity/gate-failure-distribution/flags-left-open/Phase-4-verdicts/line-count/build-status/test-status.

Constitution (non-negotiable):

- Commits authored by Raeez Lorgat only. No AI attribution anywhere.
- `git stash` is forbidden. Use `git diff > patch.diff` and `git apply`.
- Never revert mathematical content to fix a build error (FM35 constitutional). Build errors are LaTeX; fix the LaTeX.
- Never downgrade a model without user permission (AAP13). On rate limit, wait and retry.
- Before every Edit touching an r-matrix / κ / bar complex / label / Vol III κ / cross-volume formula / scope quantifier / differential form: write the relevant PE-1..PE-12 template as a fenced block in your reply, fill it in, end with `verdict: ACCEPT` — only then invoke `Edit`.
- The "arity" ban (AP176) is constitutional. `grep -rn '\barity\b' chapters/ appendices/ standalone/` must return zero hits.
- Screening-grep for cosmetic slop (notably, crucially, em-dashes, empty cites, signposts, arity) is a pre-check, NOT a rectification phase. Running that grep and declaring a file done is what the prior session did and what the user wants undone. You must execute all five phases.

When you finish a file, mark it `[x]` in the queue, append to the Completion log with commit sha, commit (no co-authored-by, no AI mentions), push, then pick the next `[ ]`. One chapter per session tick if running under cron; otherwise sequential until context pressure or user interruption.

If context pressure forces you to stop mid-chapter (typically after Phase 3 on a >3000-line file), mark the entry `[~]` with a `% RESUME-FROM: <chunk cursor>` note so the next tick knows where to resume.

Start by reading the three files above. Do not invoke the skill until you have read all three.
