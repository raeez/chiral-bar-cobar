# Continuation Prompt for Next Context Window

## How to Use

Copy the text below (between the === markers) as your first message in a fresh Claude Code session in this repo.

## ===BEGIN PROMPT===

Read compute/audit/session_state_2026_04_01_final.md for the complete state of the previous session. That file contains: 12 manuscript fixes applied, 5 new manuscript sections written (including the DS-HPL Transfer Theorem), 281 new compute tests, key mathematical findings from a 101-agent adversarial swarm, 25 compute agents that were running when the session ended, and a prioritized list of remaining work.

Resume execution. The priorities are:

1. **Check which of the 25 compute agents completed successfully** — read their output files in /private/tmp/claude-501/-Users-raeez-chiral-bar-cobar/40d12181-72b5-411f-82fe-6236a2e045ff/tasks/. For each agent that produced a compute module + tests, verify the tests pass. For agents that hit rate limits, relaunch them.

2. **Integrate completed compute results into the manuscript** — every new quantity computed (shadow coefficients, F_g values, r-matrices, discriminants, depth classifications) should be written into the appropriate example chapter or table in landscape_census.tex.

3. **Continue the raeeznotes 114-119 absorption** — the battle catalogue at compute/audit/raeeznotes_114_119_battle_catalogue.md lists 10 high-impact ideas. Items 1 (DS-HPL) and 4 (YBE=arity-3) are done. Items 2 (Δ_z^grav), 3 (r(z)=KD inverse), 6 (full instantiation), 7 (chain-level caveat) are partially done or in progress. Items 5, 8, 9, 10 remain.

4. **Launch systematic compute swarms** — the user wants 20+ new quantities computed for 10+ algebras. The previous session launched 20 compute agents for this. Continue with: genus-4 and genus-5 F_g values, shadow obstruction towers through arity 12, multi-channel genus-2 graph sums for W₃/W₄, and any quantities the agents produced that need cross-verification.

5. **Write the standalone paper** — the plan is at compute/audit/standalone_paper_plan.md. Title: "Shadow Towers and the Algebraicity of Chiral Deformation Invariants." The main theorem is the Riccati algebraicity + G/L/C/M classification. Target: Compositio.

Standing directives: Do NOT build LaTeX or run pre-existing tests. Focus exclusively on mathematical writing and new computation. The Beilinson Principle applies: every claim is false until independently verified. The Chriss-Ginzburg standard: every object earns its place. The prose standard: Kac/Etingof/Serre — no AI slop, no hedging, no em dashes as parenthetical.

## ===END PROMPT===

## Notes on Prompt Design

This prompt is designed to:
1. **Minimize context waste** — points to a single state file rather than repeating all state inline
2. **Prioritize execution** — numbered priorities with clear success criteria
3. **Maintain standing directives** — Beilinson, Chriss-Ginzburg, prose standard carried forward
4. **Avoid known failure modes** — explicitly says no builds/tests (user's standing instruction)
5. **Enable agent swarms** — item 4 explicitly authorizes large-scale parallel computation
