# AP15_duplicate_labels (429s, gpt-5.4)

- [CRITICAL] `Vol I chapters/connections/holomorphic_topological.tex:9` — `\label{conj:agt-bar-cobar}%` also appears at `Vol II chapters/connections/holomorphic_topological.tex:9` and `Vol II chapters/connections/ht_physical_origins.tex:1175`; one mathematical conjecture label is reused for two compatibility aliases and one live conjecture.
- [CRITICAL] `Vol II chapters/examples/w-algebras-stable.tex:1257` — `\label{comp:bulk-wn}` also appears at `Vol II chapters/examples/w-algebras-w3.tex:1269`; two active computation environments share one mathematical label.
- [CRITICAL] `Vol I chapters/connections/editorial_constitution.tex:2004` — `\label{conj:ads-cft-bar}` also appears at `Vol I chapters/connections/outlook.tex:671` as `\phantomsection\label{conj:ads-cft-bar}`; live conjecture plus alias collision.
- [CRITICAL] `Vol I chapters/connections/concordance.tex:5863` — `\label{comp:spectral-discriminants-standard}` also appears at `Vol I chapters/connections/outlook.tex:684` as `\phantomsection\label{comp:spectral-discriminants-standard}`; live computation plus alias collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:3274` — `\label{conj:ade-chart-k3}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:3397`; cross-volume conjecture label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:992` — `\label{comp:dybe-matrix-entries}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:1101`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:691` — `\label{comp:ell-bar-deg1}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:800`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:710` — `\label{comp:ell-bar-deg2}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:819`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:774` — `\label{comp:ell-curvature}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:883`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:1239` — `\label{comp:shuffle-generators}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:1348`; cross-volume computation label collision.

- [HIGH] `Vol I chapters/connections/typeA_baxter_rees_theta.tex:13` — `\label{app:typeA-baxter-rees-theta}` also appears at `Vol II chapters/connections/typeA_baxter_rees_theta.tex:13`; cross-volume structural label collision.
- [HIGH] `Vol I chapters/connections/holomorphic_topological.tex:2` — `\label{ch:ht-boundary}` also appears at `Vol II chapters/connections/holomorphic_topological.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol III chapters/examples/k3_times_e.tex:2` — `\label{ch:k3-times-e}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:4693` as `\phantomsection\label{ch:k3-times-e}`; intentional alias, but still a live structural collision.
- [HIGH] `Vol I chapters/connections/kontsevich_integral.tex:2` — `\label{ch:kontsevich-integral}` also appears at `Vol II chapters/connections/kontsevich_integral.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/theory/ordered_associative_chiral_kd.tex:37` — `\label{ch:ordered-associative-chiral-kd}` also appears at `Vol II chapters/connections/ordered_associative_chiral_kd_core.tex:37`; cross-volume core-chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_boundary_theory.tex:2` — `\label{ch:ym-boundary-theory}` also appears at `Vol II chapters/connections/ym_boundary_theory.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_higher_body_couplings.tex:2` — `\label{ch:ym-higher-body-couplings}` also appears at `Vol II chapters/connections/ym_higher_body_couplings.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_instanton_screening.tex:2` — `\label{ch:ym-instanton-screening}` also appears at `Vol II chapters/connections/ym_instanton_screening.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/casimir_divisor_core_transport.tex:7` — `\label{chap:casimir-divisor}` also appears at `Vol II chapters/connections/casimir_divisor_core_transport.tex:7`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/dg_shifted_factorization_bridge.tex:2` — `\label{chap:dg-shifted-factorization}` also appears at `Vol II chapters/connections/dg_shifted_factorization_bridge.tex:7`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/physical_origins.tex:2` — `\label{chap:physical-origins}` also appears at `Vol II chapters/connections/ht_physical_origins.tex:11`; the same `chap:` label is reused on a Vol II `\section`, not just another chapter.
- [HIGH] `Vol I chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:4` — `\label{chap:shifted-rtt-orthogonal-coideals}` also appears at `Vol II chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:4`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/examples/toroidal_elliptic.tex:6` — `\label{chap:toroidal-elliptic}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:55`; cross-volume chapter label collision.

Excluded false positives after context read: `SA:ground-field`, `SA:grading`, `SA:convergence`, `SA:curves`, `SA:completion` came from `chapters/theory/introduction.aux` and `chapters/theory/introduction.tex.bak`; `ch:heisenberg-frame` and `comp:heisenberg-center` came from `chapters/frame/heisenberg_frame.aux` and `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix`.

## Summary
Instances checked: 30 | Violations found: 23 | Verdict: FAIL

A `.tex`-only global count returned 937 duplicate labels across the three `chapters/` trees; the 23 findings above are the verified subset induced by the requested raw `head -30` sweep.


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
session id: 019d83aa-a959-72a1-b52e-6785bb50e4a5
--------
user
<task>
You are an ADVERSARIAL mathematical auditor for a 4,500-page research mathematics manuscript on operadic Koszul duality in the chiral realm (3 volumes). Your mission is FALSIFICATION — assume everything is WRONG until independently verified from first principles. DO NOT modify any files. Only READ and REPORT.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs you actually read. If a point is inference, label it clearly. Never present guesses as facts.
</grounding_rules>

<completeness_contract>
Resolve the audit fully. Do not stop at the first finding. Check for second-order failures, edge cases, and downstream propagation.
</completeness_contract>

<verification_loop>
Before finalizing, re-verify each finding against the actual file contents. Remove false positives. Keep only genuine discrepancies.
</verification_loop>

<structured_output_contract>
Return findings ordered by severity:
- [CRITICAL] file:line — description
- [HIGH] file:line — description
- [MEDIUM] file:line — description
- [LOW] file:line — description

End with:
## Summary
Instances checked: N | Violations found: N | Verdict: PASS/FAIL
</structured_output_contract>

<default_follow_through_policy>
Keep going until you have enough evidence. Do not stop to ask questions.
</default_follow_through_policy>


MISSION: Sweep for AP124: duplicate labels across volumes across all three volumes.

Run: grep -roh '\\label{[^}]*}' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30

Expected: Labels must be unique across volumes

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers



thinking
**Planning the audit process**

I need to ensure we follow the user's request for an audit where I only read and report, making no modifications. It seems I'll require various tools for this, especially since it touches on critical areas like AP124. I might need to read constitutional files and others, such as CLAUDE and theorem_registry, but again, no edits involved. Since this is an adversarial audit, using the skill deep-beilinson-audit would be necessary. I'll start by opening the relevant skill document and plan, using the exec_command.
thinking
**Clarifying audit tasks**

I’m considering the audit requirements and it looks like I need to read specific skills and gather duplicates using shell commands without making any edits, per the instructions. While I could look into using an explorer sub-agent, it seems that it’s mainly for codebase questions. However, since this is a repository audit, it makes sense to use it for finding duplicates and contexts. I should follow the guidance to always prefer explorer results over manual searches.
thinking
**Evaluating audit strategy**

I see the user wants a factual audit based on actual file contents, but the explorer returns summarized results, not direct file data. I should still consider using it to locate duplicates, though I’ll need to manually verify with shell commands. Maybe I can ask the explorer for a duplicate label sweep to parallelize the process. However, I need to be cautious not to re-read or re-search code that’s already covered, as that could conflict with the user's need for verified file contents.
codex
I’m treating this as a read-only AP124 cross-volume label audit. First step is to run the exact duplicate-label sweep, then open each hit in context and classify genuine collisions versus false positives.
exec
/bin/zsh -lc "grep -roh '\\\\label{["'^}]*}'"' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 276ms:
\label{SA:completion}
\label{SA:convergence}
\label{SA:curves}
\label{SA:grading}
\label{SA:ground-field}
\label{app:typeA-baxter-rees-theta}
\label{ch:heisenberg-frame}
\label{ch:ht-boundary}
\label{ch:k3-times-e}
\label{ch:kontsevich-integral}
\label{ch:ordered-associative-chiral-kd}
\label{ch:ym-boundary-theory}
\label{ch:ym-higher-body-couplings}
\label{ch:ym-instanton-screening}
\label{chap:casimir-divisor}
\label{chap:dg-shifted-factorization}
\label{chap:physical-origins}
\label{chap:shifted-rtt-orthogonal-coideals}
\label{chap:toroidal-elliptic}
\label{comp:bulk-wn}



thinking
**Evaluating duplicate labels**

I need to think through what it means to check for EACH hit; that sounds like I should consider every instance, not just the first 30 duplicates that the command "head -30" pulls. The mission is to sweep for AP124 duplicate labels across all volumes, so I should ensure I check all 30 duplicates. It seems essential to inspect these duplicates and determine if they are genuine violations of context, while also identifying the severity of those duplicates.
thinking
**Analyzing chapter labels**

I see that all paths are under active chapters, like section and chapter labels. Some could mis-reference mathematical content, which the user flags as CRITICAL. Duplicate labels for theorems and applications could improperly point to wrong information, so I need to classify these types carefully. It seems essential to read the surrounding context for each of the 30 labels to fully understand their implications. I think using "rg" across all volumes could help find occurrences while maintaining clarity without chaining commands improperly. Let's proceed with that!
thinking
**Exploring label querying**

I think using one command with regex for all 30 labels could lead to a huge output, which may not be helpful. It seems more efficient to query each label separately or maybe create a script in Python. However, the instructions suggest avoiding Python if simple shell commands are enough. Using "rg" with options like "-n -C 2" should produce manageable outputs while ensuring I'm capturing the necessary context. I’ll focus on absolute file paths too—this feels like the right direction!
codex
The duplicate set is nontrivial, and I’m now verifying each label against live chapter files to separate actual cross-volume collisions from harmless same-file repeats or generated noise. After that I’ll classify severity by what the duplicated label names.
exec
/bin/zsh -lc "rg -n -C 2 -F '\\label{SA:completion}' -F '\\label{SA:convergence}' -F '\\label{SA:curves}' -F '\\label{SA:grading}' -F '\\label{SA:ground-field}' -F '\\label{app:typeA-baxter-rees-theta}' -F '\\label{ch:heisenberg-frame}' -F '\\label{ch:ht-boundary}' -F '\\label{ch:k3-times-e}' -F '\\label{ch:kontsevich-integral}' -F '\\label{ch:ordered-associative-chiral-kd}' -F '\\label{ch:ym-boundary-theory}' -F '\\label{ch:ym-higher-body-couplings}' -F '\\label{ch:ym-instanton-screening}' -F '\\label{chap:casimir-divisor}' -F '\\label{chap:dg-shifted-factorization}' -F '\\label{chap:physical-origins}' -F '\\label{chap:shifted-rtt-orthogonal-coideals}' -F '\\label{chap:toroidal-elliptic}' -F '\\label{comp:bulk-wn}' -F '\\label{comp:dybe-matrix-entries}' -F '\\label{comp:ell-bar-deg1}' -F '\\label{comp:ell-bar-deg2}' -F '\\label{comp:ell-curvature}' -F '\\label{comp:heisenberg-center}' -F '\\label{comp:shuffle-generators}' -F '\\label{comp:spectral-discriminants-standard}' -F '\\label{conj:ade-chart-k3}' -F '\\label{conj:ads-cft-bar}' -F '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: \label{SA:convergence}: No such file or directory (os error 2)
rg: \label{SA:curves}: No such file or directory (os error 2)
rg: \label{SA:grading}: No such file or directory (os error 2)
rg: \label{SA:ground-field}: No such file or directory (os error 2)
rg: \label{app:typeA-baxter-rees-theta}: No such file or directory (os error 2)
rg: \label{ch:heisenberg-frame}: No such file or directory (os error 2)
rg: \label{ch:ht-boundary}: No such file or directory (os error 2)
rg: \label{ch:k3-times-e}: No such file or directory (os error 2)
rg: \label{ch:kontsevich-integral}: No such file or directory (os error 2)
rg: \label{ch:ordered-associative-chiral-kd}: No such file or directory (os error 2)
rg: \label{ch:ym-boundary-theory}: No such file or directory (os error 2)
rg: \label{ch:ym-higher-body-couplings}: No such file or directory (os error 2)
rg: \label{ch:ym-instanton-screening}: No such file or directory (os error 2)
rg: \label{chap:casimir-divisor}: No such file or directory (os error 2)
rg: \label{chap:dg-shifted-factorization}: No such file or directory (os error 2)
rg: \label{chap:physical-origins}: No such file or directory (os error 2)
rg: \label{chap:shifted-rtt-orthogonal-coideals}: No such file or directory (os error 2)
rg: \label{chap:toroidal-elliptic}: No such file or directory (os error 2)
rg: \label{comp:bulk-wn}: No such file or directory (os error 2)
rg: \label{comp:dybe-matrix-entries}: No such file or directory (os error 2)
codex
The first context pass had a bad `rg` invocation; I’m rerunning with explicit pattern flags so the results are only file-backed matches, not shell noise.
exec
/bin/zsh -lc "rg -n -C 2 -e '\\\\label{SA:completion}' -e '\\\\label{SA:convergence}' -e '\\\\label{SA:curves}' -e '\\\\label{SA:grading}' -e '\\\\label{SA:ground-field}' -e '\\\\label{app:typeA-baxter-rees-theta}' -e '\\\\label{ch:heisenberg-frame}' -e '\\\\label{ch:ht-boundary}' -e '\\\\label{ch:k3-times-e}' -e '\\\\label{ch:kontsevich-integral}' -e '\\\\label{ch:ordered-associative-chiral-kd}' -e '\\\\label{ch:ym-boundary-theory}' -e '\\\\label{ch:ym-higher-body-couplings}' -e '\\\\label{ch:ym-instanton-screening}' -e '\\\\label{chap:casimir-divisor}' -e '\\\\label{chap:dg-shifted-factorization}' -e '\\\\label{chap:physical-origins}' -e '\\\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\\\label{chap:toroidal-elliptic}' -e '\\\\label{comp:bulk-wn}' -e '\\\\label{comp:dybe-matrix-entries}' -e '\\\\label{comp:ell-bar-deg1}' -e '\\\\label{comp:ell-bar-deg2}' -e '\\\\label{comp:ell-curvature}' -e '\\\\label{comp:heisenberg-center}' -e '\\\\label{comp:shuffle-generators}' -e '\\\\label{comp:spectral-discriminants-standard}' -e '\\\\label{conj:ade-chart-k3}' -e '\\\\label{conj:ads-cft-bar}' -e '\\\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\\label{SA:completion})|(?:\\label{SA:convergence})|(?:\\label{SA:curves})|(?:\\label{SA:grading})|(?:\\label{SA:ground-field})|(?:\\label{app:typeA-baxter-rees-theta})|(?:\\label{ch:heisenberg-frame})|(?:\\label{ch:ht-boundary})|(?:\\label{ch:k3-times-e})|(?:\\label{ch:kontsevich-integral})|(?:\\label{ch:ordered-associative-chiral-kd})|(?:\\label{ch:ym-boundary-theory})|(?:\\label{ch:ym-higher-body-couplings})|(?:\\label{ch:ym-instanton-screening})|(?:\\label{chap:casimir-divisor})|(?:\\label{chap:dg-shifted-factorization})|(?:\\label{chap:physical-origins})|(?:\\label{chap:shifted-rtt-orthogonal-coideals})|(?:\\label{chap:toroidal-elliptic})|(?:\\label{comp:bulk-wn})|(?:\\label{comp:dybe-matrix-entries})|(?:\\label{comp:ell-bar-deg1})|(?:\\label{comp:ell-bar-deg2})|(?:\\label{comp:ell-curvature})|(?:\\label{comp:heisenberg-center})|(?:\\label{comp:shuffle-generators})|(?:\\label{comp:spectral-discriminants-standard})|(?:\\label{conj:ade-chart-k3})|(?:\\label{conj:ads-cft-bar})|(?:\\label{conj:agt-bar-cobar})
               ^
error: repetition quantifier expects a valid decimal

thinking
**Debugging command options**

I need a fixed string with -F and perhaps each -e pattern? I think rg supports -F and multiple -e options. It seems that one -F might apply to all patterns, which could simplify things. Maybe I should try using -F with -e to see if that works as intended. Let's rerun the command with this adjustment and see what happens!
exec
/bin/zsh -lc "rg -F -n -C 2 -e '\\label{SA:completion}' -e '\\label{SA:convergence}' -e '\\label{SA:curves}' -e '\\label{SA:grading}' -e '\\label{SA:ground-field}' -e '\\label{app:typeA-baxter-rees-theta}' -e '\\label{ch:heisenberg-frame}' -e '\\label{ch:ht-boundary}' -e '\\label{ch:k3-times-e}' -e '\\label{ch:kontsevich-integral}' -e '\\label{ch:ordered-associative-chiral-kd}' -e '\\label{ch:ym-boundary-theory}' -e '\\label{ch:ym-higher-body-couplings}' -e '\\label{ch:ym-instanton-screening}' -e '\\label{chap:casimir-divisor}' -e '\\label{chap:dg-shifted-factorization}' -e '\\label{chap:physical-origins}' -e '\\label{chap:shifted-rtt-orthogonal-coideals}' -e '\\label{chap:toroidal-elliptic}' -e '\\label{comp:bulk-wn}' -e '\\label{comp:dybe-matrix-entries}' -e '\\label{comp:ell-bar-deg1}' -e '\\label{comp:ell-bar-deg2}' -e '\\label{comp:ell-curvature}' -e '\\label{comp:heisenberg-center}' -e '\\label{comp:shuffle-generators}' -e '\\label{comp:spectral-discriminants-standard}' -e '\\label{conj:ade-chart-k3}' -e '\\label{conj:ads-cft-bar}' -e '\\label{conj:agt-bar-cobar}' chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-53-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-54-\chapter{Toroidal and elliptic algebras}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:55:\label{chap:toroidal-elliptic}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-56-% Regime IV --- Programmatic (Vol~I, Convention~\ref{conv:regime-tags}).
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-57-
--
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-798-Weierstrass zeta function on $E_\tau$.
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-799-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:800:\begin{computation}[Degree-1 bar elements]\label{comp:ell-bar-deg1}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-801-\index{bar complex!elliptic!degree 1}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-802-In bar degree~$1$, the generators of $\B^{\mathrm{ell}}_1(\cH_{\kappa_{\mathrm{ch}}})$
--
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-817-
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-818-\begin{computation}[Degree-2 bar elements and the elliptic differential]
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:819:\label{comp:ell-bar-deg2}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-820-\index{bar complex!elliptic!degree 2}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-821-In bar degree~$2$, the generators are:
--
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-881-\end{computation}
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex-882-


thinking
**Analyzing duplicate labels**

I’m considering how the command `uniq -d` identifies duplicates across files, including repeated labels within the same file. My goal is to differentiate between genuine violations and aliases within one volume. For instance, the label ch:k3-times-e appears twice in Volume III, but it's not across volumes. The user's task specifically mentions identifying duplicates across volumes, so I need to distinguish real violations from false positives related to AP124. Each hit must be evaluated for its authenticity.
thinking
**Assessing label duplicates**

I'm contemplating whether ch:k3-times-e counts as a false positive for cross-volume duplicates. It's a genuine duplicate label, but it doesn’t cross into other volumes. Still, the user wants labels to be unique across volumes, so there may be a need to report it as a violation anyway. Even duplicates within the same volume also violate this uniqueness. I think I should list all occurrences with file counts and perhaps run a script to clarify label matches.
codex
I have confirmed at least three distinct patterns already: true cross-volume collisions, same-volume duplicate aliases, and one same-volume duplicate theorem label inside Vol II. I’m extracting the full occurrence table now so the final report only keeps genuine, file-backed collisions.
exec
/bin/zsh -lc 'labels=$(grep -roh '"'\\\\label{["'^}]*}'"' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30)
for l in "'$labels; do
  printf '"'LABEL %s\\n' \""'$l"
  rg -n -F "$l" chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 328ms:
LABEL \label{SA:completion}
\label{SA:convergence}
\label{SA:curves}
\label{SA:grading}
\label{SA:ground-field}
\label{app:typeA-baxter-rees-theta}
\label{ch:heisenberg-frame}
\label{ch:ht-boundary}
\label{ch:k3-times-e}
\label{ch:kontsevich-integral}
\label{ch:ordered-associative-chiral-kd}
\label{ch:ym-boundary-theory}
\label{ch:ym-higher-body-couplings}
\label{ch:ym-instanton-screening}
\label{chap:casimir-divisor}
\label{chap:dg-shifted-factorization}
\label{chap:physical-origins}
\label{chap:shifted-rtt-orthogonal-coideals}
\label{chap:toroidal-elliptic}
\label{comp:bulk-wn}

thinking
**Fixing variables in shell script**

I'm encountering an issue where my variable contains newlines, which is causing problems with my loop. The command substitution seems to be preserving newlines in the first printf. I'm also realizing that the for loop isn't running properly because my labels variable includes newlines. Maybe I quoted it incorrectly? To simplify, I think it's better to use `while IFS= read -r l` to handle the input correctly. Let’s try that approach instead!
exec
/bin/zsh -lc "grep -roh '\\\\label{["'^}]*}'"' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30 | while IFS= read -r l; do
  printf 'LABEL %s\\n' \""'$l"
  rg -n -F "$l" chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 978ms:
LABEL \label{SA:completion}
chapters/theory/introduction.tex:2595:\item\label{SA:completion} Completed chiral algebras at

LABEL \label{SA:convergence}
chapters/theory/introduction.tex:2589:\item\label{SA:convergence} Formal power series in completed

LABEL \label{SA:curves}
chapters/theory/introduction.tex:2593:\item\label{SA:curves} Smooth projective geometrically connected

LABEL \label{SA:grading}
chapters/theory/introduction.tex:2587:\item\label{SA:grading} Cohomological grading: $|d| = +1$.

LABEL \label{SA:ground-field}
chapters/theory/introduction.tex:2584:\item\label{SA:ground-field} Ground field $\mathbb{C}$. All

LABEL \label{app:typeA-baxter-rees-theta}
/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex:13:\label{app:typeA-baxter-rees-theta}
chapters/connections/typeA_baxter_rees_theta.tex:13:\label{app:typeA-baxter-rees-theta}

LABEL \label{ch:heisenberg-frame}

thinking
**Searching for specific labels**

I’m thinking about using grep to find the exact label for "SA." I'll check if it might be under other volume chapters. I’ll use the command "grep -Rno" to search thoroughly in the relevant directories. It’s important to make sure I’m checking in the right places, so I’ll keep an eye out for where the volume chapters are located. This approach should provide clear results, so I’m feeling good about this method!
exec
/bin/zsh -lc "for l in '\\\\label{SA:completion}' '\\\\label{SA:convergence}' '\\\\label{SA:curves}' '\\\\label{SA:grading}' '\\\\label{SA:ground-field}' '\\\\label{ch:heisenberg-frame}' '\\\\label{comp:heisenberg-center}'; do
  printf 'LABEL %s\\n' \""'$l"
  grep -Rno --include='"'*.tex' -- \""'$l" chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters 2>/dev/null
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 1.81s:
chapters/theory/introduction.tex:2595:\label{SA:completion}

LABEL \\label{SA:convergence}
chapters/theory/introduction.tex:2589:\label{SA:convergence}

LABEL \\label{SA:curves}
chapters/theory/introduction.tex:2593:\label{SA:curves}

LABEL \\label{SA:grading}
chapters/theory/introduction.tex:2587:\label{SA:grading}

LABEL \\label{SA:ground-field}
chapters/theory/introduction.tex:2584:\label{SA:ground-field}

LABEL \\label{ch:heisenberg-frame}
chapters/frame/heisenberg_frame.tex:1:\label{ch:heisenberg-frame}

LABEL \\label{comp:heisenberg-center}
chapters/frame/heisenberg_frame.tex:4821:\label{comp:heisenberg-center}



thinking
**Investigating grep command issues**

I'm looking into potential false positives with the `grep` command. It seems like directories can point to the same file via symlinks, which could lead to duplicates. I'm considering if `chapters/` is symlinked in other volumes. 

Also, I wonder if `grep -r` might be following symlink loops, but I'm not entirely convinced that's the case. I plan to check the duplicate count using `sort uniq -c` to clarify this situation. I'll keep investigating and differentiate the sources of these labels.
thinking
**Exploring grep behavior**

I'm considering if `grep -r` on BSD might follow symlinks and if `chapters/` includes a symlink to itself. However, since `grep` with `-r`, `-h`, and `-o` only outputs matches, the same label could appear multiple times on one line. I'm also curious if there's a hidden copy in `chapters_old`, but that seems unlikely.

I need to examine if shell expansions are causing the duplication. Additionally, maybe BSD's grep is interpreting my regex differently, which could lead to unexpected duplicates. I'll keep investigating how the command processes the labels.
codex
Some of the `uniq -d` hits are already looking suspect: the live repo search only shows a single occurrence for several labels. I’m now checking raw occurrence counts to determine whether the initial sweep is being polluted by same-file aliasing or path duplication before I keep anything as a real AP124 violation.
exec
/bin/zsh -lc "grep -roh '\\\\label{["'^}]*}'"' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -c | egrep 'SA:completion|SA:convergence|SA:curves|SA:grading|SA:ground-field|ch:heisenberg-frame|comp:heisenberg-center|app:typeA-baxter-rees-theta|ch:ht-boundary|ch:k3-times-e|ch:kontsevich-integral|ch:ordered-associative-chiral-kd|ch:ym-boundary-theory|ch:ym-higher-body-couplings|ch:ym-instanton-screening|chap:casimir-divisor|chap:dg-shifted-factorization|chap:physical-origins|chap:shifted-rtt-orthogonal-coideals|chap:toroidal-elliptic|comp:bulk-wn|comp:dybe-matrix-entries|comp:ell-bar-deg1|comp:ell-bar-deg2|comp:ell-curvature|comp:heisenberg-center|comp:shuffle-generators|comp:spectral-discriminants-standard|conj:ade-chart-k3|conj:ads-cft-bar|conj:agt-bar-cobar'" in /Users/raeez/chiral-bar-cobar succeeded in 544ms:
   2 \label{SA:completion}
   2 \label{SA:convergence}
   2 \label{SA:curves}
   2 \label{SA:grading}
   2 \label{SA:ground-field}
   2 \label{app:typeA-baxter-rees-theta}
   2 \label{ch:heisenberg-frame}
   2 \label{ch:ht-boundary}
   2 \label{ch:k3-times-e}
   2 \label{ch:kontsevich-integral}
   1 \label{ch:ordered-associative-chiral-kd-extensions}
   2 \label{ch:ordered-associative-chiral-kd}
   2 \label{ch:ym-boundary-theory}
   2 \label{ch:ym-higher-body-couplings}
   2 \label{ch:ym-instanton-screening}
   2 \label{chap:casimir-divisor}
   2 \label{chap:dg-shifted-factorization}
   2 \label{chap:physical-origins}
   2 \label{chap:shifted-rtt-orthogonal-coideals}
   2 \label{chap:toroidal-elliptic}

thinking
**Searching for duplicates**

I’m confirming there’s a count of duplicates, but it doesn’t specify the locations. I might need to use grep with the -R option across all file types, but I’m currently focused on .tex files. I wonder if there’s a single occurrence hiding somewhere, possibly in other file types like .md. The user asked for the surrounding context of the actual file contents, so I should search all files under chapters to ensure I capture everything. I'll try searching with grep across all files.
exec
/bin/zsh -lc "for l in '\\\\label{SA:completion}' '\\\\label{SA:convergence}' '\\\\label{SA:curves}' '\\\\label{SA:grading}' '\\\\label{SA:ground-field}' '\\\\label{ch:heisenberg-frame}' '\\\\label{comp:heisenberg-center}'; do
  printf 'LABEL %s\\n' \""'$l"
  grep -Rno --binary-files=without-match -- "$l" chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters 2>/dev/null
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 1.93s:
chapters/theory/introduction.tex:2595:\label{SA:completion}
chapters/theory/introduction.tex.bak:1904:\label{SA:completion}

LABEL \\label{SA:convergence}
chapters/theory/introduction.tex:2589:\label{SA:convergence}
chapters/theory/introduction.tex.bak:1898:\label{SA:convergence}

LABEL \\label{SA:curves}
chapters/theory/introduction.tex:2593:\label{SA:curves}
chapters/theory/introduction.tex.bak:1902:\label{SA:curves}

LABEL \\label{SA:grading}
chapters/theory/introduction.tex:2587:\label{SA:grading}
chapters/theory/introduction.tex.bak:1896:\label{SA:grading}

LABEL \\label{SA:ground-field}
chapters/theory/introduction.tex:2584:\label{SA:ground-field}
chapters/theory/introduction.tex.bak:1893:\label{SA:ground-field}

LABEL \\label{ch:heisenberg-frame}
exec
/bin/zsh -lc "grep -roh '\\\\label{["'^}]*}'"' chapters/ ~/chiral-bar-cobar-vol2/chapters/ ~/calabi-yau-quantum-groups/chapters/ 2>/dev/null | sort | uniq -d | head -30 | while IFS= read -r l; do
  printf 'LABEL %s\\n' \""'$l"
  grep -Rno --binary-files=without-match -- "$l" chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters 2>/dev/null
  printf '"'\\n'
done" in /Users/raeez/chiral-bar-cobar succeeded in 8.31s:
LABEL \label{SA:completion}
chapters/theory/introduction.aux:236:label{SA:completion}
chapters/theory/introduction.tex:2595:label{SA:completion}
chapters/theory/introduction.tex.bak:1904:label{SA:completion}

LABEL \label{SA:convergence}
chapters/theory/introduction.aux:234:label{SA:convergence}
chapters/theory/introduction.tex:2589:label{SA:convergence}
chapters/theory/introduction.tex.bak:1898:label{SA:convergence}

LABEL \label{SA:curves}
chapters/theory/introduction.aux:235:label{SA:curves}
chapters/theory/introduction.tex:2593:label{SA:curves}
chapters/theory/introduction.tex.bak:1902:label{SA:curves}

LABEL \label{SA:grading}
chapters/theory/introduction.aux:233:label{SA:grading}
chapters/theory/introduction.tex:2587:label{SA:grading}
chapters/theory/introduction.tex.bak:1896:label{SA:grading}



thinking
**Evaluating violation context**

The user requested that for each hit, I check the surrounding context to determine if it’s a genuine violation. I think I might need commands to read the lines around suspicious cases. Yeah, not every backup file is a false positive, but I should inspect enough to classify them properly. I’ll consider potential categories like false positives from `.aux` or `.bak` files, and genuine duplicates across volumes. I need the exact line text for each violation, and I think I already have it, but I might need to adjust for regex issues.
thinking
**Clarifying output patterns**

It looks like the output shows `label{...}` without a backslash because the grep pattern used `\\label`, which might have caused the output to collapse. Earlier, the rg output provided the full line, so I can report the exact violating text by quoting those earlier results. For some cases, I might need to open the file at specific lines to capture the text accurately. I'll consider using tools like `sed -n` or `nl -ba`. I think I’ll need around 17 genuine violations, so I should prepare commands accordingly.
codex
I’m using the `deep-beilinson-audit` skill for this pass because this is a falsification-oriented, cross-volume claim-surface audit. I’m reading just the workflow sections relevant to evidence discipline and second-order checks, then continuing the label verification.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: deep-beilinson-audit
description: Use when the user asks to audit, falsify, red-team, pressure-test, or verify a theorem, chapter, proof, compute module, or frontier claim in this repository. Not for straightforward local edits that do not require an adversarial audit.
---

# Deep Beilinson Audit

Run this skill when correctness matters more than speed and the task is to challenge a claim, not merely improve its presentation.

## Load first

- `CLAUDE.md`
- `chapters/connections/concordance.tex`
- `metadata/theorem_registry.md`
- `archive/raeeznotes/raeeznotes100/red_team_summary.md`
- the target files
- the directly cited dependencies

For status-heavy work, also load the relevant metadata files.

codex
I’ve switched to the repository’s audit workflow. Before final classification I’m loading the repo’s live status surfaces for AP124 so the report matches the monograph’s own claim-discipline, not just the raw grep output.
exec
/bin/zsh -lc 'rg -n "AP124|duplicate label|label uniqueness|AP125" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP124|duplicate label|label uniqueness|AP125" chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
63:Vol III default: `\begin{conjecture}` regardless. Label prefix follows environment (AP125).
95:### HZ-5. AP125/AP124 (label prefix and uniqueness) -- 3 waves, 25+ instances
340:- B34. Duplicate `conj:kappa-bps-universality` across Vol I and Vol III. AP124/FM15.
341:- B35. `\begin{conjecture} \label{thm:foo}` prefix mismatch. AP125/FM14.
426:**FM14. AP125 label/environment mismatch on tag changes.** Downgrading a theorem to a conjecture changes `\begin{theorem}` to `\begin{conjecture}` but forgets to rename `thm:foo` to `conj:foo`. Counter: atomic 3-step edit -- rename environment, rename label, grep-and-replace all refs, in the same tool-call batch.
660:**PE-7. Label creation** (AP124, AP125)
668:prefix match (AP125):      theorem->thm, prop->prop, conj->conj, def->def, rem->rem, lem->lem
670:AP124 duplicate check (grep all three volumes):
794:### Deep Empirical (AP124-AP128, from 300-commit deep archaeology)
795:AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
796:AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
829:AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
 succeeded in 51ms:
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
 exited 1 in 50ms:

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


thinking
**Evaluating label duplicates**

I need to confirm the context around certain label duplicates to determine if they're intentional aliases meant for cross-reference compatibility. For example, there's `conj:agt-bar-cobar` in a specific file, which is duplicated intentionally. However, the same label appears in another file, causing a violation since it's defined multiple times. This could be a serious issue since it involves a conjecture label. Another case is `ch:k3-times-e`, which is also a label alias leading to a real collision. I should inspect these lines to clarify.
thinking
**Inspecting phantom aliases**

I need to look into the context for `comp:spectral-discriminants-standard` in `outlook.tex`. It seems like it might be a phantom alias that links to the concordance computation. I need to determine if that link is valid or if it could cause any issues. Getting a clearer understanding of how this alias functions will help in resolving any potential conflicts or confusion. I should check the relevant sections to clarify its purpose.
codex
The remaining work is classification, not discovery. I’ve narrowed the list to active-source collisions versus artifacts, and I’m reading the alias-heavy cases now because those are where a deliberate compatibility label can still be a real AP124 failure.
exec
/bin/zsh -lc "sed -n '4688,4696p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex
sed -n '1,6p' /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_times_e.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '666,686p' chapters/connections/outlook.tex
sed -n '1998,2008p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,20p' chapters/connections/holomorphic_topological.tex
sed -n '1168,1180p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1252,1272p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-stable.tex
sed -n '1264,1274p' /Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-w3.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '680,686p' chapters/connections/outlook.tex
sed -n '5860,5866p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
%% relative chiral algebra, and CY-specific content originally
%% in a separate chapter. All labels preserved for cross-reference.
%% ===============================================================

% Label alias for the original chapter label
\phantomsection\label{ch:k3-times-e}

This chapter develops the prototypical example of a quantum vertex chiral group: the generalized BKM superalgebra $\mathfrak{g}_{\Delta_5}$ attached to the CY3 family $X = (S \times E)/(\mathbb{Z}/N\mathbb{Z})$, whose denominator identity is the Igusa cusp form $\Delta_5$.

\chapter{The $K3 \times E$ Tower and the Igusa Cusp Form}
\label{ch:k3-times-e}

The threefold $K3 \times E$ is a fibration of a CY$_2$ over a CY$_1$. Does its chiral algebra decompose accordingly? A naive Fubini argument would predict $A_{K3 \times E} \simeq A_{K3} \otimes A_E$, and the modular characteristic would split additively as $\kappa_{\mathrm{ch}}(K3 \times E) = \kappa_{\mathrm{ch}}(K3) + \kappa_{\mathrm{ch}}(E) = 2 + 1 = 3$. But the Oberdieck--Pixton DT partition function of $K3 \times E$ is $C / (\Delta_5)^2$, where $\Delta_5$ is the Gritsenko--Nikulin automorphic form of weight~$5$ on $\mathrm{O}^+(3,2)$. The weight $5$ does not match the sum $3$: $5 \neq 2 + 1$.

Two different modular characteristics are in play, and conflating them is the source of the subscripted-$\kappa_{\bullet}$ confusion that was introduced to prevent. The chiral de Rham complex gives $\kappa_{\mathrm{ch}}(K3 \times E) = 3 = \dim_\C$, honestly additive over the fibration. The Borcherds lift weight gives $\kappa_{\mathrm{BKM}} = 5 = \mathrm{wt}(\Delta_5)$, which is not a modular characteristic of any constructed chiral algebra: it is a weight attached to a generalized Borcherds--Kac--Moody superalgebra $\mathfrak{g}_{\Delta_5}$ through its denominator identity. The chiral algebra $A_{K3 \times E}$ of a putative CY-to-chiral functor at $d = 3$ is not constructed.
 succeeded in 52ms:
\phantomsection\label{thm:lagrangian-complementarity}
\phantomsection\label{thm:anomaly-koszul}
\phantomsection\label{conj:derived-drinfeld-kohno}
\phantomsection\label{conj:categorical-modular-kd}
\phantomsection\label{conj:cumulant-recognition}
\phantomsection\label{conj:ads-cft-bar}
\phantomsection\label{conj:master-dk-kl}
\phantomsection\label{conj:master-infinite-generator}
\phantomsection\label{conj:master-bv-brst}
\phantomsection\label{conj:anomaly-physical}
\phantomsection\label{conj:vassiliev-bar}
% conj:platonic-adjunction removed: now proved as thm:platonic-adjunction
\phantomsection\label{conj:jet-principle}
\phantomsection\label{conj:standard-tower-mc5-reduction}
\phantomsection\label{prop:vassiliev-genus0}
\phantomsection\label{cor:standard-tower-mc5-closure}
\phantomsection\label{def:cumulant-coalgebra}
\phantomsection\label{def:spectral-branch-object}
\phantomsection\label{comp:spectral-discriminants-standard}
\phantomsection\label{eq:modular-cumulant-transform}
 succeeded in 52ms:
\chapter{Holomorphic-topological boundary conditions and 4d origins}
\label{ch:ht-boundary}

\index{holomorphic-topological theory|textbf}
\index{Chriss--Ginzburg principle!holomorphic-topological}
\index{convolution algebra!holomorphic-topological}

% Labels preserved for cross-reference compatibility.
\label{conj:agt-bar-cobar}%
\label{conj:nc-cs}%
\label{conj:q-agt}%
% conj:agt-w-algebra defined in w_algebras_framework.tex
\label{def:w-algebra-cft}%
\label{thm:genus-graded-bar}%

A four-dimensional holomorphic-topological field theory restricts to a
chiral algebra on each holomorphic boundary. The bar complex of that
chiral algebra classifies twisting morphisms (couplings to the
Koszul dual); the chiral derived centre
$C^\bullet_{\mathrm{ch}}(\cA,\cA)$ computes the universal
 succeeded in 51ms:
\subsubsection{Chiral Hochschild cohomology of $\mathcal{W}_N$}
\label{subsubsec:wn-hochschild}

\begin{computation}[Bulk algebra for $\mathcal{W}_N$;
\ClaimStatusProvedHere]
\label{comp:bulk-wn}
\index{W-algebra!bulk algebra}%
\index{Hochschild cohomology!W-algebra}%
Let $\cA = \mathcal{W}_{N,c}$.
\begin{enumerate}[label=\textup{(\roman*)}]
\item $H^0(C^*_{\mathrm{ch}}(\cA, \cA)) = \Bbbk$.
\item $H^1(C^*_{\mathrm{ch}}(\cA, \cA))
 = \Bbbk\langle \partial_c W_2,\, \partial_c W_3,\,
 \ldots,\, \partial_c W_N \rangle$,
 which is $(N-1)$-dimensional. Each basis element
 $\partial_c W_s$ records the infinitesimal deformation of
 the $\lambda$-brackets under $c \to c + \varepsilon$:
 \[
 \partial_c W_s \;:\;
 W_{s'} \;\longmapsto\;
 succeeded in 52ms:
\phantomsection\label{prop:vassiliev-genus0}
\phantomsection\label{cor:standard-tower-mc5-closure}
\phantomsection\label{def:cumulant-coalgebra}
\phantomsection\label{def:spectral-branch-object}
\phantomsection\label{comp:spectral-discriminants-standard}
\phantomsection\label{eq:modular-cumulant-transform}

\begin{computation}[Spectral discriminants of standard families;
\ClaimStatusProvedHere]
\label{comp:spectral-discriminants-standard}
\index{spectral discriminant!standard families}
\begin{center}
\renewcommand{\arraystretch}{1.3}




thinking
**Evaluating output structure**

I need to consider that the output contract requires findings to be ordered by severity. When it says “for EACH hit,” I wonder if I should treat each hit individually. Still, if there are multiple labels that belong to the same file pair with the same severity, I could group them in one bullet point. But the user is asking for EACH hit, so maybe it’s better to keep one bullet per label group to maintain clarity.
thinking
**Cross-checking file labels**

I need to check if some labels are duplicated just because the same file appears in both volume 1 and volume 2, but they compile separately. AP124 is a real cross-volume violation based on repo policy. So, I might extract the exact line text for each group. I have plenty from the grep output without a backslash. It could be useful to use `rg -n -F` output with full lines for all 23 groups.
thinking
**Considering output structure**

I’m thinking that it could be helpful to include a short section titled "Excluded false positives." But, I realize that the structured output contract didn’t specifically mention including this. It might be good to place it after the findings and just before the summary to keep things concise. I want to make sure the final output is clear and well-organized for users!
thinking
**Checking for duplicates in .tex files**

I’m looking to list occurrences in actual file contents, specifically focusing on active `.tex` files. I think using grep for duplicates can help, but I need to watch out for false positives, like those from aux or bak files. I’m considering using the command `rg --glob '*.tex'` for searching. Let’s focus on counting active duplicates among 30 files and see if that gives me the confirmation I need. I'll verify the count as well.
codex
I’ve reduced the set to 23 active `.tex` collisions and 7 artifact-only hits. I’m doing one last `.tex`-only pass now so the final report contains no `.aux`/`.bak` false positives.
exec
/bin/zsh -lc "find chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters -type f -name '*.tex' -print0 | xargs -0 grep -ho '\\\\label{["'^}]*}'"' 2>/dev/null | sort | uniq -d | head -30" in /Users/raeez/chiral-bar-cobar succeeded in 224ms:
\label{app:typeA-baxter-rees-theta}
\label{ch:ht-boundary}
\label{ch:k3-times-e}
\label{ch:kontsevich-integral}
\label{ch:ordered-associative-chiral-kd}
\label{ch:ym-boundary-theory}
\label{ch:ym-higher-body-couplings}
\label{ch:ym-instanton-screening}
\label{chap:casimir-divisor}
\label{chap:dg-shifted-factorization}
\label{chap:physical-origins}
\label{chap:shifted-rtt-orthogonal-coideals}
\label{chap:toroidal-elliptic}
\label{comp:bulk-wn}
\label{comp:dybe-matrix-entries}
\label{comp:ell-bar-deg1}
\label{comp:ell-bar-deg2}
\label{comp:ell-curvature}
\label{comp:shuffle-generators}
\label{comp:spectral-discriminants-standard}



thinking
**Evaluating duplicate findings**

I’m realizing there might be duplicates beyond the first 30 from the original command. The user wants each hit from that command, but after filtering, I see additional active duplicates. The mission specifically mentions focusing on head30, yet there are more duplicates to consider. The user suggests fully resolving the audit, which means I shouldn’t stop at the first finding. I’ll need to sweep for AP124 duplicate labels across all three volumes to ensure completeness.
thinking
**Considering duplicate audit risks**

I need to highlight the potential risk that more active duplicates may exist beyond the first 30 after excluding artifacts. The initial head30 command masked later duplicates, but since the user wants EACH hit, it’s crucial to note. While the command trailed off at 30, the completeness contract expects a thorough resolution. I wonder if I should expand the audit to cover all duplicates across active `.tex` files for a more complete check, especially since artifact files might contaminate our findings.
thinking
**Inspecting additional duplicates**

I’m wondering if I should continue to look for more active duplicates beyond the original 30. The user’s mission involves sweeping for AP124 duplicate labels across three volumes, which implies we need more than just a sample. Although they specified head-30, “Resolve audit fully” suggests a deeper inspection. It might be better to list all active `.tex` duplicates across volumes, though that could be quite a lot. First, I’ll count how many active duplicates exist to see if it’s manageable to inspect all of them.
exec
/bin/zsh -lc "find chapters ~/chiral-bar-cobar-vol2/chapters ~/calabi-yau-quantum-groups/chapters -type f -name '*.tex' -print0 | xargs -0 grep -ho '\\\\label{["'^}]*}'"' 2>/dev/null | sort | uniq -d | wc -l" in /Users/raeez/chiral-bar-cobar succeeded in 246ms:
     937



thinking
**Checking for label consistency**

I'm reviewing the labeling for the `chap:physical-origins` in volume 1 and the corresponding section in volume 2. I noticed that the label in volume 2 corresponds to a section, not a chapter, which complicates things. The section is correctly labeled as `\section{Physical origins}`, but the `chap:` prefix on a section seems mismatched. This could lead to confusion, and it feels like there's a potential issue that needs addressing!
thinking
**Analyzing structural duplicates**

I need to address the issue with mission AP124 regarding duplicate labels. It seems like there's a structural duplication, along with an AP125 concern since a `chap:` label is assigned to a section. This is significant, and I should only base my comments on the file content. 

The severity is high, and there might be a secondary failure with the chapter labels in volume one and volume two. For example, `chap:physical-origins` is particularly relevant for cross-reference compatibility, but it appears as a section instead of a chapter in volume two. That's an additional structural issue worth mentioning!
thinking
**Examining chapter labels**

I’m reviewing some files to check the chapter labels. It looks like `holomorphic_topological.tex` at line 1 has a `\chapter`, which is good. I also see that `ordered_associative_chiral_kd_core.tex` at line 36 has a `\chapter` too. 

Now, `app:typeA-baxter-rees-theta` may have an appendices prefix, which could be another AP125, but maybe we can ignore it. I need to look for any secondary mismatches. There's `chap:dg-shifted-factorization` that seems fine between volumes one and two, as do several other chapter labels. I should inspect `chap:physical-origins` for context and also check `app:typeA...` to confirm it's a chapter!
codex
One second-order problem is now clear: some duplicates are not just repeated names, but alias labels attached to a different structural object than the original. I’m checking those mismatch cases so the report distinguishes pure duplication from duplication plus structural drift.
exec
/bin/zsh -lc "sed -n '1,18p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex
sed -n '1,8p' chapters/connections/physical_origins.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '10,16p' chapters/connections/typeA_baxter_rees_theta.tex
sed -n '10,16p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/typeA_baxter_rees_theta.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '34,40p' chapters/theory/ordered_associative_chiral_kd.tex
sed -n '34,40p' /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\chapter{Physical Origins of Holomorphic-Topological Field Theory}
\label{chap:ht-physical-origins}

%================================================================
% SECTION: PHYSICAL ORIGINS
% (from physical_origins.tex)
%================================================================

\section{Physical origins}
\label{sec:physical-origins-overview}
\label{chap:physical-origins}
\label{rem:programme-origins}

String amplitudes, gauge theory partition functions, and conformal
blocks each produce bar-cobar structures: the generating function of
$n$-point functions is the bar complex; the factorization of
amplitudes under degeneration is the coproduct. Theorem-labeled
statements below are proved; all others are conjectural.
\chapter{Physical origins}
\label{chap:physical-origins}
 succeeded in 52ms:
%================================================================

\chapter{Type-$A$ Baxter--Rees compactification, weightwise MC4, and boundary tensor geometry}
\label{app:typeA-baxter-rees-theta}

\begin{quote}
This appendix reorganizes the Yangian frontier from the Chriss--Ginzburg
%================================================================

\chapter{Type-$A$ Baxter--Rees compactification, weightwise MC4, and boundary tensor geometry}
\label{app:typeA-baxter-rees-theta}

\begin{quote}
This appendix reorganizes the Yangian frontier from the Chriss--Ginzburg
 succeeded in 52ms:
\providecommand{\barBgeom}{\bar{\mathbf{B}}}

\chapter{Ordered Associative Chiral Koszul Duality}
\label{ch:ordered-associative-chiral-kd}

\section{Introduction}

\providecommand{\cA}{\mathcal{A}}

\chapter{Ordered Associative Chiral Koszul Duality}
\label{ch:ordered-associative-chiral-kd}
\label{chap:ordered-associative}% phantom: referenced from frontier/hochschild chapters

\section{Introduction: the diagonal as the universal boundary}





thinking
**Considering path formats**

I think I could use relative paths for the current repo and absolute paths for other volumes. I need to be sure about the exact format, like plain text paths such as `/Users/.../file.tex:13`. My final answer might need to be bullet points, maybe with monospace formatting to keep it concise yet informative. 

There’s also the question of using clickable links; the output contract specifies a `file:line` format, which complicates things a bit. I wonder if balancing between clarity and simplicity would work best.
thinking
**Refining bullet points**

Since I have over 23 bullets, using plain text might be better. I’m considering wrapping the `file:line` format in a code font for clarity. However, I see that the instructions suggest using clickable markdown links when referencing real local files. I wonder if I could group file pairs with clickable links for just one or two bullets, but that might make things tricky with so many bullets. Balancing clarity and usability is really important here.
thinking
**Evaluating false positives in reporting**

I’m considering how to handle false-positive contamination in my report. For example, 7 out of 30 hits on active-source AP124 violations aren’t actually violations. I could provide references like `chapters/theory/introduction.aux:232`, but including a short paragraph that excludes false positives might be more effective. It’s important to keep the report concise, ideally not exceeding 70 lines. I’m thinking about organizing bullets by severity and importance for clarity.
thinking
**Organizing bullets for clarity**

I’m thinking it might be best to list critical items first, perhaps starting with the highest ones. I want to ensure that each bullet point is concise, but they may need to wrap if they’re long. For example: “- [CRITICAL] chapters/connections/holomorphic_topological.tex:9 — \label{conj:agt-bar-cobar}% is duplicated…” could definitely wrap.

I’ll aim for about 23 bullets total, likely keeping within 35 lines if I’m careful to use semicolons and shorthand where possible. I might abbreviate with “V1,” “V2,” “V3” for clarity and brevity.
thinking
**Structuring output summary**

I think I need to mention that there are a total of 937 active duplicates. It might be useful to add this after the summary section. So I could format it like: “Instances checked: 30 | Violations found: 23 | Verdict: FAIL.” Then I could include the global count of the duplicates from the `.tex` file. I should definitely group the violations by severity, starting with CRITICAL and then HIGH, since there are no low or medium ones to mention. I'll craft this carefully!
codex
- [CRITICAL] `Vol I chapters/connections/holomorphic_topological.tex:9` — `\label{conj:agt-bar-cobar}%` also appears at `Vol II chapters/connections/holomorphic_topological.tex:9` and `Vol II chapters/connections/ht_physical_origins.tex:1175`; one mathematical conjecture label is reused for two compatibility aliases and one live conjecture.
- [CRITICAL] `Vol II chapters/examples/w-algebras-stable.tex:1257` — `\label{comp:bulk-wn}` also appears at `Vol II chapters/examples/w-algebras-w3.tex:1269`; two active computation environments share one mathematical label.
- [CRITICAL] `Vol I chapters/connections/editorial_constitution.tex:2004` — `\label{conj:ads-cft-bar}` also appears at `Vol I chapters/connections/outlook.tex:671` as `\phantomsection\label{conj:ads-cft-bar}`; live conjecture plus alias collision.
- [CRITICAL] `Vol I chapters/connections/concordance.tex:5863` — `\label{comp:spectral-discriminants-standard}` also appears at `Vol I chapters/connections/outlook.tex:684` as `\phantomsection\label{comp:spectral-discriminants-standard}`; live computation plus alias collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:3274` — `\label{conj:ade-chart-k3}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:3397`; cross-volume conjecture label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:992` — `\label{comp:dybe-matrix-entries}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:1101`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:691` — `\label{comp:ell-bar-deg1}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:800`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:710` — `\label{comp:ell-bar-deg2}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:819`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:774` — `\label{comp:ell-curvature}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:883`; cross-volume computation label collision.
- [CRITICAL] `Vol I chapters/examples/toroidal_elliptic.tex:1239` — `\label{comp:shuffle-generators}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:1348`; cross-volume computation label collision.

- [HIGH] `Vol I chapters/connections/typeA_baxter_rees_theta.tex:13` — `\label{app:typeA-baxter-rees-theta}` also appears at `Vol II chapters/connections/typeA_baxter_rees_theta.tex:13`; cross-volume structural label collision.
- [HIGH] `Vol I chapters/connections/holomorphic_topological.tex:2` — `\label{ch:ht-boundary}` also appears at `Vol II chapters/connections/holomorphic_topological.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol III chapters/examples/k3_times_e.tex:2` — `\label{ch:k3-times-e}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:4693` as `\phantomsection\label{ch:k3-times-e}`; intentional alias, but still a live structural collision.
- [HIGH] `Vol I chapters/connections/kontsevich_integral.tex:2` — `\label{ch:kontsevich-integral}` also appears at `Vol II chapters/connections/kontsevich_integral.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/theory/ordered_associative_chiral_kd.tex:37` — `\label{ch:ordered-associative-chiral-kd}` also appears at `Vol II chapters/connections/ordered_associative_chiral_kd_core.tex:37`; cross-volume core-chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_boundary_theory.tex:2` — `\label{ch:ym-boundary-theory}` also appears at `Vol II chapters/connections/ym_boundary_theory.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_higher_body_couplings.tex:2` — `\label{ch:ym-higher-body-couplings}` also appears at `Vol II chapters/connections/ym_higher_body_couplings.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/ym_instanton_screening.tex:2` — `\label{ch:ym-instanton-screening}` also appears at `Vol II chapters/connections/ym_instanton_screening.tex:2`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/casimir_divisor_core_transport.tex:7` — `\label{chap:casimir-divisor}` also appears at `Vol II chapters/connections/casimir_divisor_core_transport.tex:7`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/dg_shifted_factorization_bridge.tex:2` — `\label{chap:dg-shifted-factorization}` also appears at `Vol II chapters/connections/dg_shifted_factorization_bridge.tex:7`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/connections/physical_origins.tex:2` — `\label{chap:physical-origins}` also appears at `Vol II chapters/connections/ht_physical_origins.tex:11`; the same `chap:` label is reused on a Vol II `\section`, not just another chapter.
- [HIGH] `Vol I chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:4` — `\label{chap:shifted-rtt-orthogonal-coideals}` also appears at `Vol II chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex:4`; cross-volume chapter label collision.
- [HIGH] `Vol I chapters/examples/toroidal_elliptic.tex:6` — `\label{chap:toroidal-elliptic}` also appears at `Vol III chapters/examples/toroidal_elliptic.tex:55`; cross-volume chapter label collision.

Excluded false positives after context read: `SA:ground-field`, `SA:grading`, `SA:convergence`, `SA:curves`, `SA:completion` came from `chapters/theory/introduction.aux` and `chapters/theory/introduction.tex.bak`; `ch:heisenberg-frame` and `comp:heisenberg-center` came from `chapters/frame/heisenberg_frame.aux` and `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix`.

## Summary
Instances checked: 30 | Violations found: 23 | Verdict: FAIL

A `.tex`-only global count returned 937 duplicate labels across the three `chapters/` trees; the 23 findings above are the verified subset induced by the requested raw `head -30` sweep.
tokens used
47,273
