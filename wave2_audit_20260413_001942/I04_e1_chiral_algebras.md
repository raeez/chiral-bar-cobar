# I04_e1_chiral_algebras (1s)



---
STDERR:
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/calabi-yau-quantum-groups
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d8434-142e-7410-a9f0-1708ca577470
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


MISSION: COMPLETE DEEP AUDIT of chapters/theory/e1_chiral_algebras.tex

Read the ENTIRE file. Audit for ALL of the following:

1. Mathematical correctness: every theorem, proof, formula
2. CY-to-chiral functor: is CY-A only proved for d=2? d=3 conditioned?
3. Bare kappa FORBIDDEN (AP113): must be kappa_ch/cat/BKM/fiber
4. pi_3(BU)=0 (NOT Z): any Bott periodicity errors?
5. kappa_ch = chi(S)/2: only for local surfaces Tot(K_S -> S)?
6. CoHA is NOT automatically E_1-chiral (AP-CY7)
7. Borcherds denominator != bar Euler product automatically (AP-CY8)
8. Drinfeld center != derived center unless hypotheses stated
9. Objects defined before use? Unconstructed d=3 objects marked?
10. AI slop, em dashes, markdown?
11. ClaimStatus accurate?
12. Cross-volume claims match Vol I/II actual theorems?

For each finding: PROBLEM + exact FIX.
mcp startup: no servers
ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 4:09 AM.
