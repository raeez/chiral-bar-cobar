# K08_lattice_voa (1s)



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
session id: 019d8434-1f61-7b13-938c-ffd98ea6f47b
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


MISSION: CONVENTION CONSISTENCY AUDIT for Lattice VOAs.

CANONICAL DATA: class G, kappa=rank/2 (?), SC-formal

Search ALL .tex files across all three volumes for mentions of this family.
For EACH mention:
1. Is the kappa formula correct?
2. Is the r-matrix correct (with level prefix)?
3. Is the classification (G/L/C/M) correct?
4. Are boundary values correct?
5. Are convention conversions between volumes correct?
6. Is the family name/notation consistent?

Be EXHAUSTIVE. Cross-check every instance against the canonical data above.
For each discrepancy: PROBLEM + exact FIX.
mcp startup: no servers
ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:09 AM.
