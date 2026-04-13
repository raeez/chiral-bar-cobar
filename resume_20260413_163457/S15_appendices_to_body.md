# S15_appendices_to_body (978s)

- [CRITICAL] appendices/nonlinear_modular_shadows.tex:2110 — PROBLEM: the appendix states the all-degree master equation only under the extra hypothesis that the complementarity potential satisfies the classical master equation, but chapters/theory/higher_genus_modular_koszul.tex:12703 proves the same equation unconditionally from the Maurer-Cartan equation for `\Theta_\cA`. The seam disagrees on what is actually proved. FIX: rewrite `thm:nms-all-degree-master-equation` to match `prop:master-equation-from-mc`: remove the CME hypothesis, state the equation as a projection of `\Theta_\cA \in \MC(\Defcyc^{\mathrm{mod}}(\cA))`, and move the Hamiltonian/CME presentation into a remark/corollary instead of the main theorem surface.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:1172 — PROBLEM: the proof imports `thm:nms-all-degree-master-equation` as if it directly gave vanishing of all obstruction classes, but the appendix theorem does not say that, and it carries the extra CME hypothesis anyway. The same bad seam import recurs at chapters/theory/higher_genus_modular_koszul.tex:16970. FIX: in both places replace the appendix citation with `Proposition~\ref{prop:master-equation-from-mc}`; at 1172 explicitly write `\mathrm{Sh}_r(\cA)=0` for `r\ge3`, so the projected MC equation gives `\mathfrak o_\cA^{(r)}=0` for `r\ge3` (equivalently `o^{(r+1)}(\cA)=0` for `r\ge2`); at 16970 explicitly state that `o_5(\mathrm{Vir})\neq0` is the induction seed and `prop:master-equation-from-mc` supplies the recursion.

- [HIGH] chapters/theory/chiral_koszul_pairs.tex:3329 — PROBLEM: this cites `thm:nms-archetype-trichotomy` for a four-class `G/L/C/M` classification; the same scope error reappears at chapters/theory/chiral_koszul_pairs.tex:3450, chapters/theory/higher_genus_modular_koszul.tex:32054, chapters/theory/higher_genus_modular_koszul.tex:32294, and chapters/theory/higher_genus_complementarity.tex:6092. But appendices/nonlinear_modular_shadows.tex:1208 only proves a quartic-order trichotomy for the three primitive frame families Heisenberg / affine `\widehat{\mathfrak{sl}}_2` / `\beta\gamma`. FIX: replace those body citations with `Theorem~\ref{thm:shadow-archetype-classification}`; reserve `Theorem~\ref{thm:nms-archetype-trichotomy}` only for statements explicitly limited to those three primitive families through quartic order.

- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:3478 — PROBLEM: the “Conilpotent?” checklist item does not match the appendix theorem it cites. The body writes `\bigcap_n \text{coker}(\Delta^n)=0`, while appendices/koszul_reference.tex:268 defines conilpotency by eventual vanishing under iterates of the reduced coproduct: `\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar{\Delta}^{(n)})`. This is not the same criterion. FIX: replace the checkbox text with the appendix theorem’s actual condition, e.g. `Conilpotent? ($\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar{\Delta}^{(n)})$)`.

- [HIGH] metadata/theorem_registry.md:59 — PROBLEM: the live registry still indexes both `appendices/ordered_associative_chiral_kd.tex` and `chapters/theory/ordered_associative_chiral_kd.tex` as separate 89-claim surfaces, even though the main build only inputs the theory copy at main.tex:1140. The seam is therefore split between a live theory chapter and a shadow appendix duplicate with the same label namespace (for example `ch:ordered-associative-chiral-kd` at appendices/ordered_associative_chiral_kd.tex:37 and chapters/theory/ordered_associative_chiral_kd.tex:37). FIX: make `chapters/theory/ordered_associative_chiral_kd.tex` the sole live source by moving `appendices/ordered_associative_chiral_kd.tex` to `archive/` or otherwise excluding it from registry/label-index generation, then regenerate `metadata/theorem_registry.md` and `metadata/label_index.json`.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:1 — PROBLEM: the canonical theory section carries an appendix-style label `app:koszul_higher_genus`, and appendices/koszul_reference.tex then cites that theory section as if it were an appendix at lines 5, 7, 11, 28, 89, 125, and 172. This blurs appendix/theory ownership right at the seam. FIX: delete `\label{app:koszul_higher_genus}` from line 1, keep `\label{sec:koszul-across-genera}`, and replace every `\ref{app:koszul_higher_genus}` in `appendices/koszul_reference.tex` with `\ref{sec:koszul-across-genera}`.

- [LOW] chapters/theory/introduction.tex:1954 — PROBLEM: appendix-owned labels are called “Chapter/Ch.” instead of “Appendix/App.” at chapters/theory/introduction.tex:1954, 2226, 2379 and chapters/theory/chiral_hochschild_koszul.tex:5733; chapters/theory/introduction.tex:2253 also writes a chapter-range ending in an appendix label; chapters/theory/higher_genus_foundations.tex:1103 calls the section label `sec:ainfty-historical` an “Appendix” rather than a section inside an appendix. FIX: change those nouns to match the target labels: use `Appendix~\ref{app:nonlinear-modular-shadows}` / `App.~\ref{app:nonlinear-modular-shadows}`, rewrite introduction.tex:2253 as `Ch.~\ref{chap:detailed-computations} and Appendix~\ref{app:combinatorial-frontier}`, and change higher_genus_foundations.tex:1103 to `\S\ref{sec:ainfty-historical}` or `the Historical origins section of Appendix~\ref{app:homotopy-transfer}`.

## Summary
Checked: 20 | Findings: 7 | Verdict: FAIL


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
session id: 019d8744-635e-74a2-bcba-20e4c9de1419
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


MISSION: SEAM AUDIT between appendices/ and chapters/theory/.

Appendices→Theory. Check: (a) appendix results cited correctly in body, (b) no circular dependencies, (c) notation consistent

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers

thinking
**Planning file exploration**

I’m checking whether this is part of the codebase, but it seems like it’s still related to repo questions. I can use explorer agents to locate seam files and citations, which might help with searches. I should be careful though. It might be good to spawn multiple explorers for references. Additionally, I need to inspect the files myself. I should provide the user with updates during this exploration process. Frequent updates could be helpful, so a plan for updates might be a good idea.
codex
Using `deep-beilinson-audit` for an adversarial seam audit. I’m starting by locating every appendix/theory cross-reference, then I’ll read the cited transition points in source context and only keep findings that survive a second pass.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'pwd && rg -n "appendix|Appendix|appendices|app:" chapters/theory appendices CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md raeeznotes/raeeznotes100/red_team_summary.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 exited 2 in 51ms:
/Users/raeez/chiral-bar-cobar
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
archive/raeeznotes/raeeznotes100/red_team_summary.md:107:- `conj:modular` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1278:Associative modular Maurer--Cartan class || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1396: || V2:ProvedHere:chapters/connections/ordered_associativ...
archive/raeeznotes/raeeznotes100/red_team_summary.md:108:- `conj:DS` has statuses **Conjectured,ProvedHere** across instances: V1:Conjectured:appendices/ordered_associative_chiral_kd.tex:1309:Reduction commutes with associative chiral duality || V2:ProvedHere:chapters/connections/ordered_associative_chiral_kd.tex:1457: || V2:ProvedHere:chapters/connections/ordered_...
CLAUDE.md:869:AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
CLAUDE.md:934:AP176: CONSTITUTIONAL — "arity" is BANNED. The word "arity" does NOT appear anywhere in the manuscript. "Degree" is the universal term for: bar complex grading, operadic input count, tree vertex valence, Stasheff identity level, SC mixed sector parameters, cooperad/operad component indices, endomorphism operad components, brace insertion count, and all other contexts where Loday-Vallette would use "arity." This is a deliberate, permanent terminological decision. NEVER reintroduce "arity." NEVER suggest reverting "degree" to "arity." NEVER flag the use of "degree" in operadic contexts as an error. If an agent proposes restoring "arity" anywhere, the proposal is WRONG. The ~25 instances of "an degree" (article mismatch) should be corrected to "a degree." Grep check after every .tex edit: `grep -rn '\\barity\\b' chapters/ appendices/ standalone/` must return ZERO hits.
appendices/general_relations.tex:2:\label{app:geometric-dictionary}
appendices/general_relations.tex:34:\label{app:sign-conventions-general}
appendices/general_relations.tex:48:\label{app:ope-tables}
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/general_relations.tex:98:\label{app:curved-ainfty-formulas}
appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
appendices/homotopy_transfer.tex:322:\label{app:minimal-chiral}
metadata/theorem_registry.md:59:| `appendices/ordered_associative_chiral_kd.tex` | 89 |
metadata/theorem_registry.md:63:| `appendices/nonlinear_modular_shadows.tex` | 69 |
metadata/theorem_registry.md:2702:| `prop:stage-one-cartan-collapse-appendix` | `proposition` | 774 | Stage $N=1$ twist is trivial; naive Cartan fixing collapses the root sector |
metadata/theorem_registry.md:3155:| `cor:what-remains-after-present-appendix` | `corollary` | 1403 | What remains after the present appendix |
metadata/theorem_registry.md:3215:#### `appendices/_sl2_yangian_insert.tex` (8)
metadata/theorem_registry.md:3228:#### `appendices/arnold_relations.tex` (6)
metadata/theorem_registry.md:3239:#### `appendices/branch_line_reductions.tex` (21)



thinking
**Auditing transition points**

I need to follow the user's request for a thorough audit, focusing on the seam between appendices and chapters. I'll locate the relevant cross-references and transition points, ensuring they are cited correctly without circular dependencies. I might not need to examine every appendix in detail, but I'll search for references accurately, especially between directories. Since I have limited time, I’ll aim to identify all critical transition points and inspect them carefully, focusing on the audit seam specifically.
thinking
**Planning cross-reference extraction**

I'm considering using scripts for cross-referencing extraction to help streamline this process. I could use a command-line tool to list labels in the appendices and references in theory and vice versa. It might require parsing those labels and cross-references. I can't use subagents since the user didn't authorize it, so I'll handle everything directly. I think it’s best to start by reading key files like CLAUDE.md and focusing on relevant sections to ensure I capture essential information, keeping in mind to search for specific patterns as needed.
thinking
**Setting a plan**

Since the task is substantial, I need to establish a clear plan to navigate through it effectively. I'll outline the key steps that need to be taken, considering the complexities involved. This might include defining specific goals, prioritizing tasks, and allocating time for each component. I'll ensure that I'm organized and focused, so I can manage everything efficiently and meet the user's expectations. It’s important to have a well-structured approach to tackle this successfully!
codex
I’ve mapped the cross-reference surface and confirmed the audit is local to appendix/theory transition points, not a free-form scan of all chapters. Next I’m extracting the actual label graph in both directions so I can test citation correctness, circularity, and notation drift against source context rather than summaries.
Plan update
Audit the appendix/theory seam by extracting the live cross-reference graph, reading each transition in source context, then validating citation correctness, dependency direction, and notation consistency before reporting only re-verified findings.
  → Read required constitutional files and target seam-related passages
  • Extract appendix↔theory label/reference graph and identify transition points
  • Inspect each seam citation for correctness, circularity, and notation drift
  • Re-verify surviving findings and prepare exact fixes with line references

thinking
**Searching constitutional files**

I need to read constitutional files and look for passages related to seams. I’ll use rg to search for appendix-related terms, as the user’s task centers around seams. I should search within the CLAUDE/concordance/registry/red_team summary for relevant terms like app:nonlinear-modular-shadows, app:coderived, nilpotent, and homotopy-transfer. Additionally, I need to check for signs, theorems, and possible circular references. It’s all about finding the right patterns in those files!
exec
/bin/zsh -lc "rg -n \"\\\\label\\{(app:["'^}]+|sec:[''^}]+|chap:[''^}]+|thm:[''^}]+|prop:[''^}]+|lem:[''^}]+|def:[''^}]+|cor:[''^}]+|rem:[''^}]+)'"\\}\" appendices chapters/theory" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "appendix|Appendix|app:|coderived|nilpotent|signs|homotopy-transfer|arnold|nonlinear-modular-shadows|branch-line|circular|dependency" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:\label\{(app:[^}]+|sec:[^}]+|chap:[^}]+|thm:[^}]+|prop:[^}]+|lem:[^}]+|def:[^}]+|cor:[^}]+|rem:[^}]+)\})
       ^^
error: unrecognized escape sequence
 succeeded in 50ms:
CLAUDE.md:536:| B | PROVED | Bar-cobar inversion: on-locus qi unconditional; off-locus coderived equivalence unconditional (independent proof, non-circular); off-locus chain qi conditional on kappa=0 or class G/L. ALT PROOF: Keller deformation + Kontsevich formality (H02). |
CLAUDE.md:537:| C | PROVED | C0 in D^co unconditional (curved well-typedness resolved via coderived fiber-center); C0 ordinary-cohomology conditional on perfectness. C1 g>=1 duality (genus-0 separated); reflexivity from perfectness (not hidden). C2 conditional on uniform-weight; object identity fixed; center-to-bar lift proved. ALT PROOF: PTVV shifted symplectic (H03). |
CLAUDE.md:538:| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross. Circularity BROKEN: routing remark rem:non-circular-logical-chain installed; non-circular path: shadow tower -> genus universality -> family index. ALT PROOF: GRR on universal curve (H04), independent of thm:genus-universality. |
CLAUDE.md:583:**grading/signs** (AP22, AP23, AP44, AP45, AP46, AP49): Desuspension LOWERS: |s^{-1}v|=|v|-1. In LaTeX: ALWAYS s^{-1}, NEVER bare s in bar-complex formula. T^c(s^{-1} A-bar), NOT T^c(s A-bar). Mnemonic: bar=down=desuspension=s^{-1}. eta(q) includes q^{1/24}. OPE mode vs lambda-bracket: T_{(3)}T=c/2 becomes {T_lambda T}=(c/12)*lambda^3 (divided power 1/n!). A-hat(ix)-1 starts at x^2; verify F_1 matches leading order. sqrt(Q_L) is flat section; H(t)=t^2*sqrt(Q_L) NOT horizontal. Cross-volume conventions: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic. NEVER paste without conversion.
CLAUDE.md:587:**ratios/reciprocals** (AP129, AP137): AP129: When a formula involves a/b, the most common transcription error is b/a. ALWAYS substitute a known numerical value to verify. AP137: Bosonic c_{βγ} and fermionic c_{bc} satisfy c_{βγ}+c_{bc}=0. They look similar but have opposite signs. VERIFY: check c_total=0.
CLAUDE.md:823:AP11: Single-point external dependency -> flag in concordance with source, status, fallback.
CLAUDE.md:884:AP137: Bosonic/fermionic partner confusion. c_{βγ}(λ) = 2(6λ²-6λ+1) and c_{bc}(λ) = 1-3(2λ-1)² are DIFFERENT formulas satisfying c_{βγ}+c_{bc}=0. They involve the same variable λ, similar polynomial structure, and opposite signs. VERIFY: check c_total=0 after substitution. At λ=1: c_{βγ}=2, c_{bc}=-2. Writing one when you mean the other gives the wrong sign of c.
CLAUDE.md:900:AP147: Circular proof routing. Theorem B and def:koszul-chiral-algebra appeared mutually circular until the routing was made explicit: twisted-tensor → cone identification → bar-cobar (commit 65262ee). When a proof chain involves multiple theorems that reference each other, insert a ROUTING REMARK citing the primitive non-circular anchor. If no such anchor exists, the proof is genuinely circular and must be restructured.
CLAUDE.md:963:RS-15: Koszul programme before higher_genus in the dependency DAG.
CLAUDE.md:1079:**Specialized from existing (AP186-AP210):** AP186 (ProvedHere without proof block, 99C), AP187 (orphaned chapters), AP188 (empty sections), AP189 (dead labels), AP190 (hidden imports — cited result doesn't prove what's claimed, 119 findings), AP191 (circular proof chains, systematic detection), AP192 (scope inflation in statement vs proof), AP193 (biconditional stated, only forward proved), AP194 (curved complex treated with flat tools, 45 findings), AP195 (five-object conflation in prose, 47 findings), AP196 (SC misattribution in non-formula contexts), AP197 (bare Hochschild without qualifier, 89 findings), AP198 (Whitehead lemma scope — semisimple g only), AP199 (strong filtration inequality direction), AP200 (transfer theorem gap — H*(A) results applied to A), AP201 (Baxter constraint not vacuous at lambda=0), AP202 (coderived category element-wise argument invalid), AP203 (class-M harmonic mechanism unproved), AP204 (genus-0 boundary case contradiction), AP205 (reflexivity hidden in duality), AP206 (object switch mid-proof: Verdier ≠ cobar), AP207 (center-side vs bar-side lift missing), AP208 (Theorem A Verdier algebra/coalgebra flip), AP209 (missing lemma cited but never proved), AP210 (topologization chain-level vs cohomological conflation).
CLAUDE.md:1083:**Deep structural (AP225-AP233, from mega rescue 2026-04-13):** AP225 (CRITICAL: genus-universality gap — all-genera scalar factorization NOT proved; genus-1 unconditional; clutching-uniqueness needed for all g; affects Theorem D status), AP226 (K_0-class vs scalar — kappa is complex, K_0 multiplicity requires integer; use Chern character), AP227 (ProvedHere forwarding — proof body "By Theorem X" is ProvedElsewhere, not ProvedHere), AP228 (anomaly-Koszul dependency inversion — Thm D cites thm:anomaly-koszul which imports cor:kappa-additivity; backwards), AP229 (SC-formality propagation debt — Vol III compute carries stale class G/L), AP230 (genus-1 sufficient but claimed all-genera — route through genus-1 when only genus-1 needed), AP231 (draft artifacts in theorem statements — raw LOCAL/DRAFT markers in theorem envs), AP232 (duality clause overclaiming family scope — "affine KM and free-field" but proof only principal W_N), AP233 (compact/completed comparison gap in MC3 — bounded generation doesn't extend to completed category automatically).
CLAUDE.md:1089:**New failure modes (FM35-FM38):** FM35 (rate-limit cascade in parallel agent campaigns: batch<=5), FM36 (agent timeout on >15K line files: scope to line ranges), FM37 (agent confabulation of "vacuous constraint": always substitute and verify), FM38 (agent fails to detect circular proof chains: need dedicated DAG tracing).
CLAUDE.md:1115:**Unconditional (high confidence):** Theorems A (fixed-curve), B (on-locus), C0 (D^co), C1 (g>=1), D (non-circular), H, MC1, MC2, MC4, SC-formality, depth gap, D^2=0, Theta_A existence, ChirHoch^1, 10 Koszul equivs, Verlinde recovery, ker(av), Miura coefficient, critical level jump, E_3 identification (simple g), chiral QG equiv, gl_N chiral QG.
archive/raeeznotes/raeeznotes100/red_team_summary.md:68:## Highest-density suspicious proved-here dependency clusters
archive/raeeznotes/raeeznotes100/red_team_summary.md:88:- `rem:conjecture-attack-strategies` (V1 `chapters/connections/editorial_constitution.tex:954`): proved here, but cites `conj:scalar-saturation-universality:Conjectured ; conj:w3-bar-gf:Conjectured ; conj:sl3-bar-gf:Conjectured ; conj:yangian-bar-gf:Conjectured ; conj:non-simply-laced-discriminant:Conjectured ; conj:baxter-exact-triangles:Conjectured ; conj:pro-weyl-recovery:Conjectured ; conj:dk-compacts-completion:Conjectured ; conj:kl-periodic-cdg:Conjectured ; conj:kl-coderived:Conjectured ; conj:kl-braided:Conjectured ; conj:master-bv-brst:Conjectured ; conj:bar-cobar-path-integral:Conjectured ; conj:string-amplitude-bar:Conjectured ; conj:ads-cft-bar:Conjectured ; conj:holographic-koszul:Conjectured ; conj:agt-bar-cobar:Conjectured ; conj:agt-w-algebra:Conjectured ; conj:q-agt:Conjectured ; conj:nc-cs:Conjectured ; conj:cs-factorization:Conjectured ; conj:disk-local-perturbative-fm:Conjectured ; conj:reflected-modular-periodicity:Conjectured ; conj:derived-bc-betagamma:Conjectured ; conj:w-orbit-duality:Conjectured ; conj:type-a-transport-to-transpose:Conjectured`.
metadata/theorem_registry.md:91:| `prop:frame-arnold` | `proposition` | 535 | Arnold relation |
metadata/theorem_registry.md:253:| `thm:bar-cobar-inversion-qi` | `theorem` | 1606 | Bar-cobar inversion: strict on the Koszul locus, coderived off it |
metadata/theorem_registry.md:308:| `thm:arnold-three` | `theorem` | 1189 | Arnold relations |
metadata/theorem_registry.md:431:| `cor:circularity-free-koszul` | `corollary` | 4730 | Circularity-free Koszul duality |
metadata/theorem_registry.md:532:#### `chapters/theory/coderived_models.tex` (7)
codex
The first pass already exposed a seam pattern worth testing hard: several “appendix” surfaces actually live under `chapters/theory/`, so I’m separating true cross-directory dependencies from internal chapter refs before I score anything as a failure. After that I’ll trace the remaining edges both ways to catch circular routes instead of just broken labels.
exec
/bin/zsh -lc "sed -n '2010,2075p' chapters/connections/concordance.tex && printf '\\n---\\n' && sed -n '4918,5035p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if("'$ARGV ne $old){$ln=0;$old=$ARGV} $ln++; while(/'"\\\\label\\{(["'^}]+)'"\\}/g){print \""'$ARGV:$ln:$1'"\\n\"}' appendices/*.tex chapters/theory/*.tex | sort > /tmp/seam_labels.txt && sed -n '1,260p' /tmp/seam_labels.txt" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "perl -ne 'if("'$ARGV ne $old){$ln=0;$old=$ARGV} $ln++; while(/'"\\\\(?:ref|eqref|autoref|Cref|cref|Sref|textup\\{\\\\ref)\\{(["'^}]+)'"\\}/g){print \""'$ARGV:$ln:$1'"\\n\"}' appendices/*.tex chapters/theory/*.tex | sort > /tmp/seam_refs.txt && sed -n '1,320p' /tmp/seam_refs.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

\subsection*{Ring~1: The proved modular Koszul core}
Theorems~A/B/C/D/H, MC1/MC2/MC4, the proved lanes of MC5
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
 succeeded in 52ms:
appendices/_sl2_yangian_insert.tex:101:eq:d-ef
appendices/_sl2_yangian_insert.tex:104:eq:d-fe
appendices/_sl2_yangian_insert.tex:107:eq:d-he
appendices/_sl2_yangian_insert.tex:110:eq:d-eh
appendices/_sl2_yangian_insert.tex:113:eq:d-hf
appendices/_sl2_yangian_insert.tex:116:eq:d-fh
appendices/_sl2_yangian_insert.tex:119:eq:d-ee
appendices/_sl2_yangian_insert.tex:122:eq:d-ff
appendices/_sl2_yangian_insert.tex:125:eq:d-hh
appendices/_sl2_yangian_insert.tex:133:rem:ordered-vs-symmetric-sl2
appendices/_sl2_yangian_insert.tex:164:prop:ybe-from-d-squared
appendices/_sl2_yangian_insert.tex:168:eq:cybe-sl2
appendices/_sl2_yangian_insert.tex:227:thm:yang-r-matrix
appendices/_sl2_yangian_insert.tex:234:eq:yang-r-matrix
appendices/_sl2_yangian_insert.tex:279:eq:r-eigenvalue-sym
appendices/_sl2_yangian_insert.tex:281:eq:r-eigenvalue-wedge
appendices/_sl2_yangian_insert.tex:28:eq:sl2-ope
appendices/_sl2_yangian_insert.tex:302:thm:rtt-sl2
appendices/_sl2_yangian_insert.tex:304:eq:transfer-matrix-sl2
appendices/_sl2_yangian_insert.tex:313:eq:rtt-sl2
 succeeded in 51ms:
appendices/_sl2_yangian_insert.tex:148:eq:d-ef
appendices/_sl2_yangian_insert.tex:148:eq:d-hh
appendices/_sl2_yangian_insert.tex:196:eq:cybe-sl2
appendices/_sl2_yangian_insert.tex:293:prop:ybe-from-d-squared
appendices/_sl2_yangian_insert.tex:323:eq:rtt-sl2
appendices/_sl2_yangian_insert.tex:349:rtt:AA
appendices/_sl2_yangian_insert.tex:349:rtt:CC
appendices/_sl2_yangian_insert.tex:351:rtt:AB
appendices/_sl2_yangian_insert.tex:351:rtt:AD
appendices/_sl2_yangian_insert.tex:359:eq:rtt-sl2
appendices/_sl2_yangian_insert.tex:35:eq:sl2-ope
appendices/_sl2_yangian_insert.tex:471:eq:pbw-iso-sl2
appendices/_sl2_yangian_insert.tex:510:thm:yang-r-matrix
appendices/_sl2_yangian_insert.tex:567:comp:ordered-bar-sl2
appendices/_sl2_yangian_insert.tex:575:prop:ybe-from-d-squared
appendices/_sl2_yangian_insert.tex:577:thm:yang-r-matrix
appendices/_sl2_yangian_insert.tex:578:thm:rtt-sl2
appendices/_sl2_yangian_insert.tex:581:thm:pbw-sl2
appendices/_sl2_yangian_insert.tex:588:eq:sl2-collision-residue
appendices/_sl2_yangian_insert.tex:593:eq:koszul-dual-id-sl2

thinking
**Auditing Appendices and Theory**

I need to audit the appendices and their relation to the theory. It sounds like the user is suggesting a two-way connection between them. I should check that the appendix results are cited correctly in the main body and ensure there are no circular dependencies. It's possible that the appendices might refer back to the theory, which could lead to some circularity issues. I'll need to extract references and cross-check them in both directions.
exec
/bin/zsh -lc "perl -e '
my %lab;
for my "'$f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) {
  open my $fh, "<", $f or die $!;
  my $ln=0;
  while(<$fh>){ $ln++; while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$lab{$1}}, "$f:$ln"; } }
  close $fh;
}
for my $f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) {
  open my $fh, "<", $f or die $!;
  my $ln=0;
  while(<$fh>){ $ln++; while(/'"\\\\(?:ref|eqref|autoref|Cref|cref|Sref)\\{(["'^}]+)'"\\}/g){
      my "'$t=$1; next unless exists $lab{$t};
      for my $def (@{$lab{$t}}){
        my $src = $f =~ m{''^appendices/} ? "A" : "T";
        my $dst = $def =~ m{''^appendices/} ? "A" : "T";
        next if $src eq $dst;
        print "$f:$ln -> $t -> $def'"\\n\";
      }
  }}
  close "'$fh;
}
'"' | sort > /tmp/cross_edges.txt && sed -n '1,260p' /tmp/cross_edges.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/arnold_relations.tex:169 -> thm:bar-nilpotency-complete -> chapters/theory/bar_construction.tex:788
appendices/arnold_relations.tex:175 -> sec:genus-2-complete -> chapters/theory/higher_genus_foundations.tex:4215
appendices/arnold_relations.tex:175 -> sec:genus-3-complete -> chapters/theory/higher_genus_foundations.tex:4318
appendices/arnold_relations.tex:175 -> thm:arnold-genus1 -> chapters/theory/higher_genus_foundations.tex:4067
appendices/arnold_relations.tex:175 -> thm:arnold-higher-genus -> chapters/theory/higher_genus_foundations.tex:2887
appendices/arnold_relations.tex:175 -> thm:arnold-quantum -> chapters/theory/higher_genus_foundations.tex:2888
appendices/arnold_relations.tex:515 -> thm:bar-nilpotency-complete -> chapters/theory/bar_construction.tex:788
appendices/arnold_relations.tex:523 -> thm:bar-nilpotency-complete -> chapters/theory/bar_construction.tex:788
appendices/branch_line_reductions.tex:1064 -> thm:modular-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:2844
appendices/branch_line_reductions.tex:130 -> thm:modular-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:2844
appendices/branch_line_reductions.tex:134 -> thm:spectral-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:3538
appendices/branch_line_reductions.tex:138 -> thm:universal-theta -> chapters/theory/higher_genus_modular_koszul.tex:3571
appendices/branch_line_reductions.tex:139 -> thm:mc2-full-resolution -> chapters/theory/higher_genus_modular_koszul.tex:8164
appendices/branch_line_reductions.tex:181 -> thm:universal-theta -> chapters/theory/higher_genus_modular_koszul.tex:3571
appendices/branch_line_reductions.tex:192 -> thm:universal-theta -> chapters/theory/higher_genus_modular_koszul.tex:3571
appendices/branch_line_reductions.tex:208 -> thm:spectral-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:3538
appendices/branch_line_reductions.tex:24 -> thm:modular-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:2844
appendices/branch_line_reductions.tex:25 -> thm:spectral-characteristic -> chapters/theory/higher_genus_modular_koszul.tex:3538
appendices/branch_line_reductions.tex:27 -> thm:mc2-full-resolution -> chapters/theory/higher_genus_modular_koszul.tex:8164
appendices/branch_line_reductions.tex:27 -> thm:universal-theta -> chapters/theory/higher_genus_modular_koszul.tex:3571


thinking
**Evaluating output organization**

I’m looking at a large output and wondering how to inspect it effectively. I should focus on relevant sections like appendices or chapters, but not on huge duplicated chapters. It seems important to audit transition points carefully. I might target surfaces where appendix results are cited in theory and vice versa, looking for patterns of inconsistency. I also need to check for broken labels and circular references, especially around high-level appendices. This could be a challenging audit!
thinking
**Checking label inconsistencies**

I'm looking for mismatched labels, like how theory cites something as app:coderived-models while the actual label might be app:coderived or sec:coderived-models. I noticed that higher_genus_foundations.tex references both, which could indicate a problem. I need to confirm that each label is defined. The focus should be on the seams between appendices and chapters/theory. I might run a script to find references that aren't defined properly. The user is interested in identifying undefined references or mismatches!
codex
I’ve got the live cross-directory reference graph now. The next filter is stricter: undefined seam refs, theory→appendix↔theory two-cycles, and references whose target statement does not actually match the wording imported at the seam.
exec
/bin/zsh -lc "perl -e '
my %lab;
for my "'$f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) { open my $fh, "<", $f or die $!; my $ln=0; while(<$fh>){$ln++; while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$lab{$1}}, "$f:$ln"; }} close $fh; }
for my $f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) { open my $fh, "<", $f or die $!; my $ln=0; while(<$fh>){$ln++; while(/'"\\\\(?:ref|eqref|autoref|Cref|cref|Sref)\\{(["'^}]+)'"\\}/g){ my "'$t=$1; next if exists $lab{$t}; print "$f:$ln -> $t'"\\n\"; }} close "'$fh; }
'"' | sort > /tmp/undefined_refs.txt && sed -n '1,240p' /tmp/undefined_refs.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/branch_line_reductions.tex:1111 -> thm:ds-bar-gf-discriminant
appendices/branch_line_reductions.tex:1152 -> part:bar-complex
appendices/branch_line_reductions.tex:251 -> thm:ds-bar-gf-discriminant
appendices/branch_line_reductions.tex:512 -> thm:ds-bar-gf-discriminant
appendices/combinatorial_frontier.tex:1066 -> conj:yangian-bar-gf
appendices/combinatorial_frontier.tex:107 -> conj:sl3-bar-gf
appendices/combinatorial_frontier.tex:107 -> conj:w3-algebraicity
appendices/combinatorial_frontier.tex:108 -> conj:yangian-bar-gf
appendices/combinatorial_frontier.tex:1115 -> cor:growth-rate-dimg
appendices/combinatorial_frontier.tex:119 -> thm:master-pbw
appendices/combinatorial_frontier.tex:1256 -> thm:motzkin-path-model
appendices/combinatorial_frontier.tex:142 -> thm:heisenberg-bar
appendices/combinatorial_frontier.tex:150 -> thm:genus1-heisenberg
appendices/combinatorial_frontier.tex:153 -> cor:subexp-free-field
appendices/combinatorial_frontier.tex:172 -> rem:eval-stability-recursive-kernel
appendices/combinatorial_frontier.tex:211 -> thm:universal-kac-moody-koszul
appendices/combinatorial_frontier.tex:226 -> rem:garland-lepowsky-sl2
appendices/combinatorial_frontier.tex:232 -> thm:motzkin-path-model
appendices/combinatorial_frontier.tex:235 -> cor:growth-rate-dimg
appendices/combinatorial_frontier.tex:238 -> rem:garland-lepowsky-sl2
exec
/bin/zsh -lc "perl -e '
my (%lab,%edges);
for my "'$f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) { open my $fh, "<", $f or die $!; my $ln=0; while(<$fh>){$ln++; while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$lab{$1}}, "$f:$ln"; }} close $fh; }
for my $f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) { open my $fh, "<", $f or die $!; my $ln=0; while(<$fh>){$ln++; while(/'"\\\\(?:ref|eqref|autoref|Cref|cref|Sref)\\{(["'^}]+)'"\\}/g){ my "'$t=$1; next unless exists $lab{$t}; for my $def (@{$lab{$t}}){ my $srcdir = $f =~ m{''^appendices/} ? "A" : "T"; my $dstdir = $def =~ m{''^appendices/} ? "A" : "T"; next unless $srcdir ne $dstdir; $edges{"$f:$ln"}{$def}=1; } }} close $fh; }
for my $src (sort keys %edges){ for my $dst (sort keys %{$edges{$src}}){ my ($dfile,$dline)=split(/:/,$dst,2); if(exists $edges{$dst}{$src}){ print "$src <-> $dst'"\\n\"; } } }
' | sort -u > /tmp/cross_cycles.txt && sed -n '1,240p' /tmp/cross_cycles.txt" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

exec
/bin/zsh -lc "rg -n \"app:coderived-models|sec:coderived-models|app:coderived\\b|sec:coderived\\b|app:nilpotent-completion|app:homotopy-transfer|app:signs|app:branch-line-reductions|app:nonlinear-modular-shadows|app:koszul_higher_genus|app:koszul-reference|app:arnold-relations\" appendices chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/general_relations.tex:68:\label{app:arnold-relations-small-n}
appendices/homotopy_transfer.tex:2:\label{app:homotopy-transfer}
appendices/branch_line_reductions.tex:2:\label{app:branch-line-reductions}
chapters/theory/bar_construction.tex:641:The standard Koszul sign rule (Appendix~\ref{app:signs}, \S\ref{app:sign-conventions}; see also \S\ref{sec:sign-dictionary-complete}) applies with total degree $|\phi| + k$ for a field $\phi \in \mathcal{A}$ tensored with a form in $\Omega^k$.
chapters/theory/bar_construction.tex:955:Proposition~\ref{prop:master-sign} in Appendix~\ref{app:signs}.
chapters/theory/bar_construction.tex:1225:By Arnol'd~\cite{Arnold69}, the 1-forms $\eta_{ij} = d\log(z_i - z_j)$ generate $H^*(C_n(\mathbb{C}); \mathbb{Q})$ and satisfy the Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$. That these generate \emph{all} relations follows from Cohen's computation of $H^*(C_n(\mathbb{C}))$ as the cohomology of the Arnol'd--Brieskorn braid arrangement complement~\cite{Coh76}. See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph.
appendices/nonlinear_modular_shadows.tex:2:\label{app:nonlinear-modular-shadows}
appendices/nonlinear_modular_shadows.tex:207:of Appendix~\ref{app:signs}.
chapters/theory/coderived_models.tex:3:\label{app:coderived}
chapters/theory/coderived_models.tex:17:\label{subsec:coderived-abstract}
chapters/theory/coderived_models.tex:188:\label{sec:coderived-models}
chapters/theory/coderived_models.tex:373:The full theory (\S\ref{subsec:coderived-ran-formalism}) also
chapters/theory/coderived_models.tex:448:\label{subsec:coderived-ran-formalism}
chapters/theory/higher_genus_foundations.tex:293:see Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:407: $D^{\mathrm{co}}$~(Appendix~\ref{app:coderived-models}).
chapters/theory/higher_genus_foundations.tex:831: \textup{(}Appendix~\textup{\ref{app:coderived-models})}.
chapters/theory/higher_genus_foundations.tex:1190:(Appendix~\ref{app:signs}, \S\ref{sec:sign-dictionary-complete}).
chapters/theory/higher_genus_foundations.tex:1582: (Appendix~\ref{app:homotopy-transfer}) produces a \emph{minimal}
chapters/theory/higher_genus_foundations.tex:2077:\textup{(}Appendix~\textup{\ref{sec:coderived-models})}.
chapters/theory/higher_genus_modular_koszul.tex:1:\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

thinking
**Inspecting file dependencies**

I need to read target files and lines around cross-references to check for circular dependencies. I'll inspect specific lines in `chapters/theory/bar_construction.tex` and `appendices/arnold_relations.tex`. There are also issues with inconsistent references like `sec:coderived-models`. I might need to change labels in the text to ensure they point correctly either to the appendix or section. I'll start by examining the context in these files to clarify their intended targets.
exec
/bin/zsh -lc "sed -n '1,80p' appendices/nonlinear_modular_shadows.tex && printf '\\n---\\n' && sed -n '1948,1962p' chapters/theory/introduction.tex && printf '\\n---\\n' && sed -n '5728,5748p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1200,1232p' chapters/theory/bar_construction.tex && printf '\\n---\\n' && sed -n '150,188p' appendices/arnold_relations.tex && printf '\\n---\\n' && sed -n '500,528p' appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,80p' chapters/theory/coderived_models.tex && printf '\\n---\\n' && sed -n '284,308p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '399,414p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '2068,2082p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '288,304p' chapters/theory/algebraic_foundations.tex && printf '\\n---\\n' && sed -n '268,282p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter[Ambient complementarity and nonlinear modular shadows]{Ambient complementarity, nonlinear modular shadows, and the quartic resonance class}
\label{app:nonlinear-modular-shadows}

The modular characteristic $\kappa(\cA)$ (Theorem~D) and the spectral
discriminant~$\Delta_{\cA}$ are the linear face of a single ambient
deformation problem. The ambient problem carries a $(-1)$-shifted
symplectic form, and the two dual packages $\mathcal{Q}_g(\cA)$
and~$\mathcal{Q}_g(\cA^{!})$ are complementary Lagrangians inside it.
Their interaction produces an infinite nonlinear tower
\[
\kappa \;\longrightarrow\; \Delta \;\longrightarrow\;
\mathfrak{C} \;\longrightarrow\; \mathfrak{Q}
\;\longrightarrow\; \Theta,
\]
the \emph{shadow obstruction tower}: the sequence of finite-order
projections $\Theta_\cA^{\leq r}$ of the universal MC element
$\Theta_\cA \in \MC(\gAmod)$
(Theorem~\ref{thm:mc2-bar-intrinsic}: $\Theta_\cA := D_\cA - d_0$
is MC because $D_\cA^2 = 0$; all-degree convergence
$\Theta_\cA = \varprojlim_r \Theta_\cA^{\leq r}$ by
 succeeded in 51ms:

\emph{Formulation 3 (cohomological).}
The cohomology ring $H^*(\overline{C}_n(X); \mathbb{Q})$ is generated by classes $[\eta_{ij}]$ subject to the Arnold relations.
\end{theorem}

\begin{proof}
See Theorem~\ref{thm:arnold-relations} for the partial-fractions proof.
The topological, combinatorial, and operadic perspectives are developed in \S\ref{sec:arnold-three-proofs-comprehensive}.
\end{proof}

\begin{remark}[Arnold relations = Jacobi identity]\label{rem:arnold-jacobi-geometric}
The geometric content of $\dzero^2 = 0$ at degree~$3$ is precisely the Jacobi identity: the three boundary strata of $\overline{C}_4(\mathbb{P}^1)$ that contribute to $\dzero^2$ correspond to the three terms of the Jacobi identity for the chiral bracket. Concretely, the Arnold relation $\eta_{12} \wedge \eta_{23} + \eta_{23} \wedge \eta_{31} + \eta_{31} \wedge \eta_{12} = 0$ forces
\[
{f^{ab}}_d\,{f^{dc}}_e + {f^{bc}}_d\,{f^{da}}_e + {f^{ca}}_d\,{f^{db}}_e = 0,
\]
which is the Jacobi identity for the structure constants extracted by residues. The implication is bidirectional: the Arnold relations \emph{are} the Jacobi identity via the residue dictionary. See Computation~\ref{comp:geom-alg-comparison-deg3} for the complete term-by-term verification in $\widehat{\mathfrak{sl}}_{2,k}$ and Theorem~\ref{thm:arnold-jacobi} for the general CFT formulation.
\end{remark}

\begin{corollary}[Cohomology of configuration spaces {\cite{Arnold69}}; \ClaimStatusProvedElsewhere]\label{cor:cohomology-config}
The cohomology ring $H^*(C_n(\mathbb{C}); \mathbb{Q})$ of the open configuration space is:
 succeeded in 51ms:

\section{Coderived and contraderived categories}
\label{app:coderived}
\index{coderived category|textbf}
\index{contraderived category|textbf}

The bar-cobar adjunction at higher genus produces curved complexes
($d^2 \neq 0$), for which ordinary cohomological derived methods
are no longer the right invariant.
Positselski's theory of coderived and contraderived
categories~\cite{Positselski11} provides the correct
replacement. This appendix collects the definitions and key results
needed in this monograph; the chiral specialization appears in
\S\ref{subsec:chiral-coderived-contraderived}.

\subsection{Abstract definitions}
\label{subsec:coderived-abstract}

Let $\mathsf{A}$ be an abelian category with exact direct sums
(for the coderived case) or exact direct products

thinking
**Fixing reference formatting**

I see that the reference is likely using a section number instead of the appendix letter, which is odd for "Appendix 7.1." I’ll need to change all these mismatched prefixes across the files. My search has already shown many instances like `Appendix\ref{sec:coderived-models}` and `Chapter\ref{app:nonlinear-modular-shadows}`. I really should systematically find all occurrences of `Appendix\ref{sec:` and `Chapter\ref{app:` to ensure consistency. I'll use rg to help with that!
exec
/bin/zsh -lc "sed -n '2218,2230p' chapters/theory/introduction.tex && printf '\\n---\\n' && sed -n '2374,2382p' chapters/theory/introduction.tex && printf '\\n---\\n' && sed -n '5729,5738p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Appendix~\\\\ref\\{sec:["'^}]+'"\\}|Appendix~\\\\textup\\{\\\\ref\\{sec:["'^}]+'"\\}\\}|Chapter~\\\\ref\\{app:["'^}]+'"\\}|Ch\\.~\\\\ref\\{app:["'^}]+'"\\}\" chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '286,298p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '402,410p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '826,836p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '628,634p' chapters/theory/higher_genus_modular_koszul.tex && printf '\\n---\\n' && sed -n '292,299p' chapters/theory/algebraic_foundations.tex && printf '\\n---\\n' && sed -n '273,278p' chapters/theory/chiral_koszul_pairs.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
Higher genus (Ch.~\ref{chap:higher-genus}) &
 Genus tower; curvature $\dfib^2=\kappa\omega_g$; \textbf{Theorems~C+D} (complementarity, modular characteristic); Lagrangian upgrade \\
Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
 Chiral Koszul pairs; chiral modules; \textbf{Theorem~H} ($\ChirHoch^*$ polynomial, Koszul-functorial) \\
Quantum corrections (Ch.~\ref{ch:quantum-corrections}) &
 Higher-genus Arnold deformations; filtered-curved hierarchy \\[6pt]
\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:characteristic-datum}: The Characteristic Datum} \emph{(shadow obstruction tower; $E_1$ wing; $E_n$ Koszul duality)}} \\[3pt]
\hline
Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
 Shadow obstruction tower $\kappa\to\Delta\to\mathfrak C\to\mathfrak Q\to\cdots$; clutching law; archetypes G/L/C/M; branch-line reductions \\
$E_1$ modular Koszul duality (Ch.~\ref{chap:e1-modular-koszul}) &
 Ribbon modular operad; $F\!\Ass$; $E_1$ convolution; $E_1$ shadow tower; Thms $A^{E_1}$--$H^{E_1}$; ordered chiral homology (\S\ref{sec:ordered-chiral-homology}); formality bridge (Thm~\ref{thm:e1-formality-bridge}) \\
Ordered associative chiral KD (Ch.~\ref{ch:ordered-associative-chiral-kd}) &

---
\end{enumerate}

\textbf{Part~\ref{part:characteristic-datum}: The Characteristic Datum} (shadow tower; $\Eone$ wing).
\begin{enumerate}[label=\textup{\arabic*.}, start=12]
\item \emph{Nonlinear modular shadows}
 exited 1 in 50ms:

 succeeded in 52ms:
The strict differentials $\dzero$ and $\Dg{g}$ produce honest
chain complexes; the bar complex equipped with either lives in
the \emph{derived category}. The curved differential $\dfib$
produces a curved dg coalgebra with $\dfib^{\,2} \neq 0$
(for $\kappa \neq 0$); the bar complex equipped with $\dfib$
lives in the \emph{coderived category}
$D^{\mathrm{co}}$~(Positselski;
see Appendix~\ref{app:coderived-models}).
The derived/coderived comparison, established on the manuscript's
flat-side comparison locus together with the coderived treatment of
the curved model, ensures that the flat model carries the ordinary
derived package while the curved model is its coderived counterpart.


---
 uncurving identity~\eqref{eq:chain-uncurving} expresses the
 interplay between fiber curvature and base flatness.
 The resulting flat complex $(\barB^{(g)}(\cA), \Dg{g})$ lives in
 the derived category; the curved complex
 $(\barB^{(g)}(\cA), \dfib)$ lives in the coderived category
codex
I’m now checking the dangerous cases, not just the broken labels. The Arnold seam and the nonlinear-shadows seam both have bidirectional traffic, so I’m reading those in proof context to separate harmless navigation from actual logical backflow.
exec
/bin/zsh -lc "grep '"'^chapters/theory/'"' /tmp/cross_edges.txt | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/algebraic_foundations.tex:1079 -> app:sign-conventions -> appendices/signs_and_shifts.tex:713
chapters/theory/algebraic_foundations.tex:1079 -> app:signs -> appendices/signs_and_shifts.tex:2
chapters/theory/algebraic_foundations.tex:116 -> def:bar-complex-algebraic -> appendices/notation_index.tex:342
chapters/theory/algebraic_foundations.tex:2465 -> rem:three-bar-variants -> appendices/ordered_associative_chiral_kd.tex:687
chapters/theory/bar_cobar_adjunction_curved.tex:109 -> ch:ordered-associative-chiral-kd -> appendices/ordered_associative_chiral_kd.tex:37
chapters/theory/bar_cobar_adjunction_curved.tex:160 -> ch:ordered-associative-chiral-kd -> appendices/ordered_associative_chiral_kd.tex:37
chapters/theory/bar_cobar_adjunction_inversion.tex:1876 -> thm:htt -> appendices/homotopy_transfer.tex:69
chapters/theory/bar_cobar_adjunction_inversion.tex:3476 -> thm:essential-image-koszul -> appendices/koszul_reference.tex:268
chapters/theory/bar_construction.tex:1225 -> app:arnold-relations -> appendices/arnold_relations.tex:1
chapters/theory/bar_construction.tex:641 -> app:sign-conventions -> appendices/signs_and_shifts.tex:713
chapters/theory/bar_construction.tex:641 -> app:signs -> appendices/signs_and_shifts.tex:2
chapters/theory/bar_construction.tex:641 -> sec:sign-dictionary-complete -> appendices/signs_and_shifts.tex:1012
chapters/theory/bar_construction.tex:954 -> ver:d2-degree3 -> appendices/signs_and_shifts.tex:607
chapters/theory/bar_construction.tex:955 -> app:signs -> appendices/signs_and_shifts.tex:2
chapters/theory/bar_construction.tex:955 -> prop:master-sign -> appendices/signs_and_shifts.tex:576
chapters/theory/chiral_hochschild_koszul.tex:1172 -> thm:nms-all-degree-master-equation -> appendices/nonlinear_modular_shadows.tex:2110
chapters/theory/chiral_hochschild_koszul.tex:2462 -> app:sign-conventions -> appendices/signs_and_shifts.tex:713
chapters/theory/chiral_hochschild_koszul.tex:2462 -> app:signs -> appendices/signs_and_shifts.tex:2
chapters/theory/chiral_hochschild_koszul.tex:2900 -> app:homotopy-transfer -> appendices/homotopy_transfer.tex:2
chapters/theory/chiral_hochschild_koszul.tex:2932 -> app:homotopy-transfer -> appendices/homotopy_transfer.tex:2

thinking
**Addressing appendix issues**

I've got a lot of edges to consider when moving from theory to appendices. The user is asking about exhaust seams, but I can only report on what I’ve found. It's possible there aren't any issues on many edges. I might be able to run some automated checks. For instance, I need to look for mismatched prefixes, like `Appendix\ref{sec:...}`. Also, I should search for any undefined references to labels like `app:coderived-models`. Let's dig into this!
exec
/bin/zsh -lc "grep '"'^chapters/theory/.* -> app:'"' /tmp/undefined_refs.txt | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_foundations.tex:293 -> app:coderived-models
chapters/theory/higher_genus_foundations.tex:407 -> app:coderived-models
chapters/theory/higher_genus_foundations.tex:831 -> app:coderived-models

thinking
**Working on appendix labels**

I'm thinking about undefined appendix labels in the theory section. That's a positive sign! I might want to filter out any prefix mismatches across the theory and appendices. It could help to search for fixed strings as well. I’m considering using simpler fixed string commands like `rg -n 'Chapter\\ref\\{app:' chapters/theory`. By streamlining my approach, I can better locate the issues I need to address.
exec
/bin/zsh -lc "rg -n -F 'Chapter~\\ref{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Ch.~\\ref{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'Appendix~\\ref{sec:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/chiral_hochschild_koszul.tex:5733:in Chapter~\ref{app:nonlinear-modular-shadows}, where the quartic
chapters/theory/introduction.tex:1954:(Chapter~\ref{app:nonlinear-modular-shadows}).
 succeeded in 52ms:
chapters/theory/introduction.tex:2226:Nonlinear modular shadows (Ch.~\ref{app:nonlinear-modular-shadows}) &
chapters/theory/introduction.tex:2379: (Ch.~\ref{app:nonlinear-modular-shadows}).
 succeeded in 52ms:
chapters/theory/higher_genus_foundations.tex:1103:For historical background on $A_\infty$ algebras, see Appendix~\ref{sec:ainfty-historical}.
chapters/theory/algebraic_foundations.tex:296:the coderived category (Appendix~\ref{sec:coderived-models});
chapters/theory/algebraic_foundations.tex:377:(Appendix~\ref{sec:coderived-models}).%
chapters/theory/chiral_koszul_pairs.tex:276:(Appendix~\ref{sec:coderived-models}),
exec
/bin/zsh -lc "rg -n -F 'Appendix~\\textup{\\ref{sec:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:631:\textup{(}Appendix~\textup{\ref{sec:coderived-models})} off it.
chapters/theory/higher_genus_foundations.tex:2077:\textup{(}Appendix~\textup{\ref{sec:coderived-models})}.

thinking
**Inspecting appendix details**

I need to inspect `Appendix\ref{sec:ainfty-historical}` from higher_genus_foundations. I'll check if `sec:ainfty-historical` is defined in appendix/homotopy_transfer. It seems that it likely is on line 61, since that's where section labels are mentioned. I should read the context around that to understand the issue better and determine the exact fix needed. A search for the definition might help clarify things, too.
exec
/bin/zsh -lc "rg -n \"label\\{sec:ainfty-historical\\}\" appendices chapters/theory && sed -n '1098,1107p' chapters/theory/higher_genus_foundations.tex && printf '\\n---\\n' && sed -n '54,68p' appendices/homotopy_transfer.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/homotopy_transfer.tex:61:\label{sec:ainfty-historical}
character, while the higher obstruction classes are the Hodge Chern
classes selected by the same scalar recursion.

\section{\texorpdfstring{$A_\infty$ structures and higher operations}{A-infinity structures and higher operations}}

For historical background on $A_\infty$ algebras, see Appendix~\ref{sec:ainfty-historical}.

% ================================================================
% SECTION 4.2: THE GEOMETRIC BAR COMPLEX AND ITS A-INFINITY STRUCTURE
% ================================================================

---
 operations $m_k^V$ and internal edges decorated by the
 homotopy~$h$. Bar-cobar inversion re-absorbs these
 higher operations into the differential of~$\Omega(B(H))$.
\end{enumerate}
\end{proof}

\section{Historical origins}

thinking
**Clarifying fix instructions**

I think the fix involves renaming a label to `sec:koszul-across-genera` and updating references in `appendices/koszul_reference.tex`. The exact suggestion would be to change the label on `chapters/theory/higher_genus_modular_koszul.tex:1` from `\label{app:koszul_higher_genus}` to `\label{sec:koszul-across-genera-canonical}`. We should replace all references to `app:koszul_higher_genus` with the new one and then delete the old label since it overlaps with the new one. This change should improve clarity.
exec
/bin/zsh -lc "rg -n -F 'app:koszul_higher_genus' appendices chapters/theory" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:1:\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}
appendices/koszul_reference.tex:5:\begin{remark}[Relationship to \S\ref{app:koszul_higher_genus}]
appendices/koszul_reference.tex:7:\S\ref{app:koszul_higher_genus}. This appendix provides reference
appendices/koszul_reference.tex:11:\S\ref{app:koszul_higher_genus} is canonical.
appendices/koszul_reference.tex:28:\S\ref{app:koszul_higher_genus}, proved via the Prism Principle
appendices/koszul_reference.tex:89:\S\ref{app:koszul_higher_genus}, proved by applying the $\Eone$-chiral Koszul
appendices/koszul_reference.tex:125:\S\ref{app:koszul_higher_genus}, proved by combining the
appendices/koszul_reference.tex:172:\S\ref{app:koszul_higher_genus}. The proof applies the

thinking
**Verifying appendix references**

I need to check if other places specifically call it a chapter due to the compilation. Since the file is in the appendices directory and has the label prefix "app," labeling it as an Appendix seems more consistent. There's another issue where `higher_genus_foundations` references `Appendix\ref{app:coderived-models}`, but the label is undefined. I should see if the bar_construction theorem mentions Appendix for proofs and check for any circular references in the logic regarding `thm:bar-nilpotency-complete`.
exec
/bin/zsh -lc 'rg -n "thm:bar-nilpotency-complete|cor:bar-d-squared-zero-arnold|thm:arnold-iff-nilpotent|app:arnold-relations" chapters/theory/bar_construction.tex chapters/theory/configuration_spaces.tex appendices/arnold_relations.tex chapters/theory/en_koszul_duality.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
appendices/arnold_relations.tex:1:\chapter{Arnold relations}\label{app:arnold-relations}
appendices/arnold_relations.tex:78:This is a special case of Theorem~\ref{thm:arnold-iff-nilpotent}, which establishes the equivalence in full generality. We give the operadic decomposition here.
appendices/arnold_relations.tex:99:This is a restatement of the equivalence $(1) \Leftrightarrow (2)$ in Theorem~\ref{thm:arnold-iff-nilpotent}. The mixed terms $d_{\text{internal}} \circ d_{\text{residue}}$ and $d_{\text{de Rham}} \circ d_{\text{residue}}$ (and their reverses) vanish independently by type considerations; the nontrivial content is $d_{\text{residue}}^2 = 0$, which is equivalent to the Arnold relations by Theorem~\ref{thm:arnold-iff-nilpotent}.
appendices/arnold_relations.tex:164:\begin{corollary}[Bar differential squares to zero; \ClaimStatusProvedHere]\label{cor:bar-d-squared-zero-arnold}
appendices/arnold_relations.tex:169:This is the content of Theorem~\ref{thm:bar-nilpotency-complete}, where the nine pairwise compositions of the three bar differential components are shown to cancel. The Arnold relations enter in the $d_{\mathrm{res}} \circ d_{\mathrm{res}}$ component.
appendices/arnold_relations.tex:180:\begin{theorem}[Arnold relations \texorpdfstring{$\Leftrightarrow$}{iff} \texorpdfstring{$d_{\text{residue}}^2 = 0$}{d\_residue\textasciicircum 2 = 0}; \ClaimStatusProvedHere]\label{thm:arnold-iff-nilpotent}
appendices/arnold_relations.tex:462:(Theorem~\ref{thm:arnold-iff-nilpotent}), which controls the algebraic
appendices/arnold_relations.tex:515:cancellation of Theorem~\ref{thm:bar-nilpotency-complete} is recovered
appendices/arnold_relations.tex:523:Theorem~\ref{thm:bar-nilpotency-complete} is the local manifestation of
chapters/theory/bar_construction.tex:64:Theorem~\ref{thm:bar-nilpotency-complete} assembles these three
chapters/theory/bar_construction.tex:72:Throughout this chapter, the unadorned differential $d$ on the bar complex denotes the genus-$0$ collision differential $\dzero$ of Convention~\ref{conv:higher-genus-differentials}; it satisfies $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}). The fiberwise curved differential $\dfib$ and the total corrected differential $\Dg{g}$ appear only in Chapter~\ref{chap:higher-genus}.
chapters/theory/bar_construction.tex:788:\begin{theorem}[Nilpotency of bar differential; \ClaimStatusProvedHere]\label{thm:bar-nilpotency-complete}
chapters/theory/bar_construction.tex:1017:\emph{Property~(1).} In the double sum $d_{\mathrm{bracket}}^2$, the one-overlap terms (Case~(ii) of Theorem~\ref{thm:bar-nilpotency-complete}) produce iterated residues $\mathrm{Res}_{D_{j\ell}}\mathrm{Res}_{D_{ij}}[(\phi_i)_{(0)}(\phi_j)_{(0)}\phi_\ell \otimes \omega]$. The Borcherds identity for the chiral product asserts:
chapters/theory/bar_construction.tex:1024:\emph{Property~(3).} The full Borcherds identity~\eqref{eq:borcherds-pole-mix} cancels \emph{all} iterated residue terms simultaneously, regardless of pole decomposition. Since $d_{\mathrm{res}} = d_{\mathrm{bracket}} + d_{\mathrm{curvature}}$, the identity $d_{\mathrm{res}}^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}) together with $d_{\mathrm{curvature}}^2 = 0$ gives $d_{\mathrm{bracket}}^2 = -\{d_{\mathrm{bracket}}, d_{\mathrm{curvature}}\}$.
chapters/theory/bar_construction.tex:1225:By Arnol'd~\cite{Arnold69}, the 1-forms $\eta_{ij} = d\log(z_i - z_j)$ generate $H^*(C_n(\mathbb{C}); \mathbb{Q})$ and satisfy the Arnold relations $\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki} + \eta_{ki} \wedge \eta_{ij} = 0$. That these generate \emph{all} relations follows from Cohen's computation of $H^*(C_n(\mathbb{C}))$ as the cohomology of the Arnol'd--Brieskorn braid arrangement complement~\cite{Coh76}. See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph.
chapters/theory/bar_construction.tex:1443:Theorem~\ref{thm:bar-nilpotency-complete}.
chapters/theory/bar_construction.tex:1657:This assembles Theorem~\ref{thm:bar-nilpotency-complete} ($d^2 = 0$), Theorem~\ref{thm:coassociativity-complete} (coassociativity of $\Delta$), and Theorem~\ref{thm:counit-axioms} (counit axioms). The compatibility $d \circ \Delta = \Delta \circ d$ is Theorem~\ref{thm:bar-coalgebra}.
chapters/theory/bar_construction.tex:1707:oriented at each genus. It is the determinant line of $T_{C_{p+1}(\Sigma_g)}$ with genus-dependent corrections, ensuring consistent signs across all face maps. At genus~$0$, this guarantees $\dzero^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}); at genus~$g \geq 1$, the fiberwise differential satisfies $\dfib^{\,2} = \kappa(\cA)\cdot\omega_g$ and the total corrected differential $\Dg{g}^2 = 0$ is established in Chapter~\ref{chap:higher-genus}.
chapters/theory/bar_construction.tex:1803: vanishes by the associativity of the chiral product, as verified in Case~(ii) of Theorem~\ref{thm:bar-nilpotency-complete}.
chapters/theory/bar_construction.tex:1852:The nine-term proof of $d^2 = 0$ (Theorem~\ref{thm:bar-nilpotency-complete}) uses geometric signs throughout. Translating to operadic conventions via the dictionary above preserves $d^2 = 0$.

thinking
**Inspecting proof dependencies**

I need to look closely at the proof of `thm:bar-nilpotency-complete` to determine if it relies on an appendix or the external Arnold theorem. If the bar construction theorem directly shows that d²=0, then the appendix could be used fine. However, the user asked me to check for circular dependencies. I also want to see if `appendices/arnold_relations.tex` uses a theorem from the theory in proofs of the same proposition mentioned by the theory. I'll inspect the context around `en_koszul_duality` at line 500 to clarify.
exec
/bin/zsh -lc "sed -n '492,512p' chapters/theory/en_koszul_duality.tex && printf '\\n---\\n' && sed -n '788,860p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{definition}

\begin{theorem}[\texorpdfstring{$d^2 = 0$}{d squared = 0} from Totaro relations;
\ClaimStatusProvedHere]
\label{thm:e2-d-squared}
\index{Totaro relations!and $d^2 = 0$}
The differential $d_{\Etwo}$ of
Definition~\textup{\ref{def:e2-bar-complex}} satisfies
$d_{\Etwo}^2 = 0$.
\end{theorem}

\begin{proof}
The proof follows the same structure as the chiral case
(Corollary~\ref{cor:bar-d-squared-zero-arnold}), with the Arnold
relations replaced by Totaro relations.

We compute $d_{\Etwo}^2$ on a bar element
$\alpha \in \Omega^*(\overline{\Conf}_k(\bR^2))
\otimes (s^{-1} \bar{A})^{\otimes k}$.
The square decomposes into three terms:
exec
/bin/zsh -lc "sed -n '68,86p' chapters/theory/configuration_spaces.tex && printf '\\n---\\n' && sed -n '3818,3836p' chapters/theory/configuration_spaces.tex && printf '\\n---\\n' && sed -n '180,236p' appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
(Theorem~\ref{thm:arnold-relations}):
\begin{equation}\tag{$\star$}
\eta_{ij} \wedge \eta_{jk}
+ \eta_{jk} \wedge \eta_{ki}
+ \eta_{ki} \wedge \eta_{ij} = 0
\qquad (i,j,k \text{ distinct}).
\end{equation}
Third, this relation forces $d_{\mathrm{residue}}^2 = 0$
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


thinking
**Continuing to explore proof reliance**

I need to continue investigating whether this proof depends on the bar theorem. I’ll look deeper to see how the theorem might affect the argument or support my findings. It’s important to ensure I have a solid grasp of its implications. I wonder if there are specific cases or examples I could check to clarify this. Let's dive in and see what connections I can make!
exec
/bin/zsh -lc "sed -n '236,290p' appendices/arnold_relations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\[\text{Res}_{D_{ij}} \text{Res}_{D_{jk}}[\eta_{ij} \wedge \eta_{jk}]
+ \text{Res}_{D_{jk}} \text{Res}_{D_{ki}}[\eta_{jk} \wedge \eta_{ki}]
+ \text{Res}_{D_{ki}} \text{Res}_{D_{ij}}[\eta_{ki} \wedge \eta_{ij}].\]
Since $d_{\text{residue}}^2 = 0$ by assumption, this
sum must vanish. Taking into account the Koszul signs from the ordering of iterated
residues, this yields (cf.\ Computation~\ref{comp:explicit-residues}):
\[\text{Res}_{D_{ij}} \circ \text{Res}_{D_{jk}} + \text{Res}_{D_{jk}} \circ
\text{Res}_{D_{ki}} + \text{Res}_{D_{ki}} \circ \text{Res}_{D_{ij}} = 0,\]
which is statement~(3). Statement~(1) follows from~(3) via the residue
correspondence: under $\partial_{ij} \leftrightarrow \text{Res}_{D_{ij}}$,
the composition identity $\partial_{ij} \circ \partial_{jk}
+ \text{cyclic} = 0$ is equivalent to
$\eta_{ij} \wedge \eta_{jk} + \eta_{jk} \wedge \eta_{ki}
+ \eta_{ki} \wedge \eta_{ij} = 0$ by the explicit calculation
in Computation~\ref{comp:explicit-residues}.
\end{proof}

\subsection{Explicit residue calculations}

\begin{computation}[Residues of logarithmic forms]\label{comp:explicit-residues}
exec
/bin/zsh -lc "rg -n \"label\\{thm:nms-virasoro-quartic-explicit\\}|label\\{thm:nms-archetype-trichotomy\\}|label\\{thm:nms-all-degree-master-equation\\}|label\\{thm:nms-finite-termination\\}|label\\{lem:nms-euler-inversion\\}\" appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1208:\label{thm:nms-archetype-trichotomy}
1344:\label{thm:nms-virasoro-quartic-explicit}
2110:\label{thm:nms-all-degree-master-equation}
2191:\label{thm:nms-finite-termination}
3555:\label{lem:nms-euler-inversion}%



thinking
**Evaluating reporting standards**

I'm thinking it's best not to report uncertain issues unless the label is clearly undefined or mismatched with the expected label type. This approach should help minimize confusion and ensure the information is accurate. I want to be cautious here and ensure clarity in communication, as it could help others understand the specifics better. Let's stick to reporting what we’re sure about to keep everything straightforward!
thinking
**Analyzing label inconsistencies**

I realize that prefix mismatches are apparent since the label is defined within an appendix section. If I use `\section` numbering, it might show something like A.1, which sounds awkward as "Appendix A.1." Instead, I prefer "Section A.1." It makes sense to consider this notation inconsistency valid. I also want to check how `appendices/koszul_reference.tex` connects to `app:koszul_higher_genus`, especially since it says that section's canonical reference. I need to explore any potential mislabeling issues further.
thinking
**Searching for misprefixes**

I’m thinking about whether I could find any more misprefix issues in the labeling if the environment is a section. I plan to use a regular expression search with `rg` to help identify any inconsistencies. This way, I can scan through the relevant files efficiently and see if there are any other prefixes that don’t match or could cause confusion. It sounds like a good step to ensure everything is properly labeled.
exec
/bin/zsh -lc "rg -n \"\\\\(chapter|section|subsection)\\{.*\\\\label\\{app:["'^}]+'"\\}\" chapters/theory appendices" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:\(chapter|section|subsection)\{.*\label\{app:[^}]+\})
                                        ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -P '"'^'"\\\\(chapter|section|subsection).*label\\{app:' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/arnold_relations.tex:1:\chapter{Arnold relations}\label{app:arnold-relations}
chapters/theory/higher_genus_modular_koszul.tex:1:\section{Koszul duality across genera}\label{sec:koszul-across-genera}\label{app:koszul_higher_genus}

thinking
**Considering theoretical seams**

I'm thinking about whether to include references to the "appendix" from the theory, especially since the target is also in the theory. However, I realize it might not fit well with the actual directory seam. It seems better to focus on the actual directory seam instead. I wonder if I should mention coderived at all, or just note it as a false appendix or theory seam. That might clarify things.
codex
The first round on the true cross-directory surface narrowed down to a smaller set of real seam problems. I’m excluding internal `chapters/theory` appendix-label mess unless it distorts an actual appendix↔theory edge, and I’m now checking the remaining appendix-owned labels that the body treats as theory chapters.
exec
/bin/zsh -lc "sed -n '1,40p' appendices/koszul_reference.tex && printf '\\n---\\n' && sed -n '1,16p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1160,1182p' chapters/theory/chiral_hochschild_koszul.tex && printf '\\n---\\n' && sed -n '2100,2142p' appendices/nonlinear_modular_shadows.tex && printf '\\n---\\n' && sed -n '5728,5740p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,60p' appendices/ordered_associative_chiral_kd.tex && printf '\\n---\\n' && rg -n -F 'ch:ordered-associative-chiral-kd' appendices chapters/theory && printf '\\n---\\n' && sed -n '1738,1754p' chapters/theory/introduction.tex && printf '\\n---\\n' && sed -n '100,114p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\chapter{Koszul duality reference tables}
\label{app:koszul-reference}


\begin{remark}[Relationship to \S\ref{app:koszul_higher_genus}]
The genus-graded Koszul duality theory is developed in
\S\ref{app:koszul_higher_genus}. This appendix provides reference
tables and the essential image characterization; the core definitions
and theorems are stated there and should not be duplicated. Where a
result appears in both locations, the version in
\S\ref{app:koszul_higher_genus} is canonical.
\end{remark}

\section{Genus-graded Koszul duality}

\begin{theorem}[Extended Koszul duality; \ClaimStatusProvedElsewhere]
\label{thm:extended-koszul-appendix}
If $(\mathcal{A}, \mathcal{A}^!)$ form a genus-0 Koszul dual pair with central curvature at
all genera, then under suitable finiteness and convergence conditions:
\[\left(\bigoplus_{g \geq 0} \mathcal{A}^{(g)}, \bigoplus_{g \geq 0} (\mathcal{A}^!)^{(g)}\right)\]
 succeeded in 52ms:
hence $A_\infty$-depth $d_\infty(\cA) = 2$ and
$L_\infty$-formality level $f_\infty(\cA) = 2$.
The genus-$0$ transferred $L_\infty$ brackets therefore
satisfy $\ell_k^{(0),\mathrm{tr}} = 0$ for $k \geq 3$:
the genus-$0$ convolution algebra is formal.

For the full scalar orbit, the shadow
obstruction tower terminates at degree~$2$:
$\Theta_{\cA}^{(\le r)} = \kappa \cdot \eta \otimes \Lambda$
for all~$r$. The obstruction classes
$o^{(r+1)}(\cA) \in H^2(F^{r+1}\gAmod / F^{r+2}\gAmod, d_2)$
vanish for all $r \geq 2$
(Theorem~\ref{thm:nms-all-degree-master-equation}).
Since the genus-$g$ quantum brackets $\ell_k^{(g)}$ for
$g \geq 1$ are induced by sewing on $\overline{\cM}_{g,n}$,
and sewing applied to the scalar element
$\kappa \cdot \eta \otimes \Lambda$ produces the scalar
genus-$g$ curvature $\kappa^g \cdot \eta_g \otimes \Lambda_g$
(which lies in the image of the differential, not in
independent cohomology), the transferred higher-genus brackets
 succeeded in 51ms:
% Ordered Associative Chiral Koszul Duality
% Integration-ready chapter file (stripped from standalone amsart draft).
% Uses only \providecommand for macros that may not be in main.tex preamble.

\providecommand{\Assch}{\mathrm{Ass}^{\mathrm{ch}}}
\providecommand{\Barch}{\overline{B}^{\mathrm{ch}}}
\providecommand{\Cobar}{\Omega^{\mathrm{ch}}}
\providecommand{\coHoch}{\operatorname{coHH}}
\providecommand{\Cotor}{\operatorname{Cotor}}
\providecommand{\Coext}{\operatorname{Coext}}
\providecommand{\RHom}{R\!\operatorname{Hom}}
\providecommand{\Tot}{\operatorname{Tot}}
\providecommand{\KK}{\mathbb{K}}
\providecommand{\Dpbw}{D^{\mathrm{pbw}}}
\providecommand{\Dco}{D^{\mathrm{co}}}
\providecommand{\chotimes}{\mathbin{\otimes^{\mathrm{ch}}}}
\providecommand{\wt}{\widetilde}
\providecommand{\eps}{\varepsilon}
\providecommand{\susp}{s}
\providecommand{\coeq}{\operatorname{coeq}}

thinking
**Examining appendix dependencies**

The user is asking about the relationship between the appendices and the main theory in the report. It’s crucial to identify if the theorem in the main body relies on an appendix theorem that is presented as an extension. I need to ensure there are no circular dependencies, especially if the appendix theorem depends on the main body theorem. I’ll take a closer look at the context around the chiral Hochschild-Koszul line 1172 for better clarity.
exec
/bin/zsh -lc "sed -n '1138,1186p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{equation}\label{eq:one-channel-formality}
\Theta_{\cA}
\;=\;
\kappa(\cA) \cdot \eta \otimes \Lambda.
\end{equation}
Then the quantum $L_\infty$-structure is formal along the
distinguished scalar Maurer--Cartan orbit of\/~$\Theta_{\cA}$:
the higher transferred brackets vanish on the one-dimensional
scalar line $\mathbb{C}\!\cdot\!\eta \otimes \Lambda$, and the MC
equation restricts there to the scalar genus identities.
No converse is proved here. In particular, one-channel
minimal-model concentration
$\Theta_{\cA}^{\min} = \eta \otimes \Gamma_{\cA}$ does
\emph{not} by itself imply the scalar identity
\eqref{eq:one-channel-formality}.
\end{theorem}

\begin{proof}
Throughout this proof we write $\kappa$ for $\kappa(\cA)$.
Suppose $\Theta_{\cA} = \kappa \cdot \eta \otimes \Lambda$.
exec
/bin/zsh -lc "rg -n 'convolution-formality-cg|one-channel-formality|Theorem~\\\\ref\\{thm:nms-all-degree-master-equation\\}|thm:nms-all-degree-master-equation|thm:operadic-complexity-detailed' appendices/nonlinear_modular_shadows.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:87:(Theorem~\ref{thm:nms-all-degree-master-equation}),
appendices/nonlinear_modular_shadows.tex:2110:\label{thm:nms-all-degree-master-equation}
appendices/nonlinear_modular_shadows.tex:2490:Parts~(i)--(iii) are Theorems~\ref{thm:nms-shadow-master-equations}, \ref{thm:nms-separating-boundary-recursion}, and \ref{thm:nms-shadow-cocycle-characterization}. Part~(iv) is Theorem~\ref{thm:nms-archetype-trichotomy}. Part~(v) is Theorems~\ref{thm:nms-virasoro-mixed-shadow} and \ref{thm:nms-principal-wn-contact-nonvanishing} together with Corollary~\ref{cor:nms-principal-wn-mixed}. Part~(vi) is Construction~\ref{constr:nms-gram-determinant-line} and Definition~\ref{def:nms-modular-quartic-resonance-class}. Part~(vii) is Theorems~\ref{thm:nms-clutching-law-modular-resonance} and \ref{thm:nms-first-nonlinear-shadow-theta}. Part~(viii) is Theorems~\ref{thm:nms-all-degree-master-equation} and~\ref{thm:nms-finite-termination}. Parts~(ix) and~(x) are Theorem~\ref{thm:nms-nonseparating-clutching-law}, Corollary~\ref{cor:nms-genus-one-hessian-correction}, and Theorem~\ref{thm:nms-genus-loop-model-families}.\qedhere
appendices/nonlinear_modular_shadows.tex:3543:(Theorem~\ref{thm:nms-all-degree-master-equation}) generates
chapters/theory/chiral_hochschild_koszul.tex:1138:\begin{equation}\label{eq:one-channel-formality}
chapters/theory/chiral_hochschild_koszul.tex:1152:\eqref{eq:one-channel-formality}.
chapters/theory/chiral_hochschild_koszul.tex:1158:By Theorem~\ref{thm:operadic-complexity-detailed},
chapters/theory/chiral_hochschild_koszul.tex:1172:(Theorem~\ref{thm:nms-all-degree-master-equation}).
chapters/theory/chiral_hochschild_koszul.tex:1186:\label{rem:convolution-formality-cg}
chapters/theory/higher_genus_modular_koszul.tex:12708:(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
chapters/theory/higher_genus_modular_koszul.tex:15273:\label{thm:operadic-complexity-detailed}%
chapters/theory/higher_genus_modular_koszul.tex:15361:Theorem~\ref{thm:operadic-complexity-detailed} is
chapters/theory/higher_genus_modular_koszul.tex:15387:Theorem~\ref{thm:operadic-complexity-detailed}.
chapters/theory/higher_genus_modular_koszul.tex:16472:of Theorem~\textup{\ref{thm:operadic-complexity-detailed}}
chapters/theory/higher_genus_modular_koszul.tex:16970:equation (Theorem~\ref{thm:nms-all-degree-master-equation}) then
chapters/theory/higher_genus_modular_koszul.tex:29364:By Theorem~\textup{\ref{thm:operadic-complexity-detailed}},
chapters/theory/higher_genus_modular_koszul.tex:29375:(Theorem~\ref{thm:operadic-complexity-detailed}), the shadow




thinking
**Investigating theorem citations**

I'm noticing that my search isn't showing anything about the appendix theorem related to the chiral Hochschild theorem, which is good because it avoids circular reasoning. However, I might have issues with nomenclature and citation correctness. I need to inspect the file for specific relations and ensure the statements align. It seems the theorem about Arnold relations includes a discussion on nilpotency, but I'm concerned about whether the body cites the appendix properly. There could be issues with notation but not logic.
thinking
**Finding inconsistencies in theorems**

I need to identify any inconsistencies or mismatches in titles or mathematical content. For instance, I see a statement about the quartic shadow cocycle and its connection to various frame families. I should confirm that the appendix theorem indeed includes these families. I’m also considering if there’s a seam issue, where a theorem in the higher genus modular Koszul paper uses appendices, potentially leading to circular reasoning. I’ll need to check the order of proofs and ensure everything supports the main theory without contradictions.
thinking
**Verifying appendix citations**

I need to check the body citations to make sure they correctly reference the appendix results. It’s important to confirm that there are no mismatches and that everything aligns with the intended content. Additionally, I want to ensure there’s no circular reasoning involved in these citations. This step is crucial in maintaining the integrity of the arguments and results presented. Making sure references are accurate will help prevent confusion down the line.
thinking
**Considering theorem citations**

I’m thinking about which ones to choose that are commonly used in proofs or statements. I might automate the process by checking the target theorem statement alongside the surrounding source text. However, that might take some time. There’s also a potential mismatch to consider: from `chapters/theory/chiral_koszul_pairs.tex` to `thm:nms-archetype-trichotomy`. I need to inspect if the body correctly uses the theorem and search its context for clarity.
exec
/bin/zsh -lc "sed -n '5430,5450p' chapters/theory/higher_genus_complementarity.tex && printf '\\n---\\n' && sed -n '2186,2202p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '16892,16978p' chapters/theory/higher_genus_modular_koszul.tex && printf '\\n---\\n' && sed -n '946,1048p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '3318,3338p' chapters/theory/chiral_koszul_pairs.tex && printf '\\n---\\n' && sed -n '3440,3458p' chapters/theory/chiral_koszul_pairs.tex && printf '\\n---\\n' && sed -n '1198,1226p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
\label{rem:shadow-tower-period-correction}
\index{period correction!shadow tower}
 succeeded in 51ms:
  S_r = 0 \quad (r \geq 5).
 \]
 Thus the charged quartic contact class is nonzero and is the last
 non-vanishing shadow component; the quintic obstruction vanishes by
 rank-one abelian rigidity and stratum separation
 \textup{(}Theorem~\textup{\ref{thm:betagamma-global-depth}};
 Corollary~\textup{\ref{cor:nms-betagamma-mu-vanishing}};
 Remark~\textup{\ref{rem:contact-stratum-separation}}\textup{)}.

\item \emph{Mixed \textup{(}$\mathbf{M}$,
$d_{\mathrm{alg}} = \infty$, $r_{\max} = \infty$\textup{)}:}
 Virasoro $\mathrm{Vir}_c$, $\mathcal{W}_N$ ($N \geq 3$).
 The cubic shadow $\mathfrak{C}_{\mathrm{Vir}} = 2x^3$ and quartic
 shadow $\mathfrak{Q}^{\mathrm{ct}}_{\mathrm{Vir}} =
 \tfrac{10}{c(5c{+}22)}\,x^4$ are both non-vanishing, and
 $o_5(\mathrm{Vir}) = \{\mathfrak{C}, \mathfrak{Q}\}_{H} \neq 0$
 for generic~$c$
 \textup{(}Theorem~\textup{\ref{thm:w-virasoro-quintic-forced}}).
 The tower is infinite by induction on the all-degree master equation.
 For multi-generator algebras $\mathcal{W}_N$ ($N \geq 3$),
 succeeded in 51ms:
Proposition~\ref{prop:pbw-universality};
MC4 compl.\ =
Theorem~\ref{thm:completed-bar-cobar-strong};
lattice filt.\ =
Theorem~\ref{thm:lattice:koszul-morphism};
null vect.\ = Kac--Shapovalov obstruction
(Theorem~\ref{thm:kac-shapovalov-koszulness});
Cartan~$H^2$ = abelian Cartan subalgebra classes
surviving in $H^2(\barB)$
(Remark~\ref{rem:admissible-koszul-status}).
\textit{Shadow}: archetype class $G$/$L$/$C$/$M$
(Theorem~\ref{thm:nms-archetype-trichotomy})
and shadow depth $r_{\max}$;
all four classes contain Koszul algebras
(shadow depth $\neq$ Koszulness).

\smallskip\noindent
${}^{\dagger}$\,The symplectic fermion
($\beta\gamma$ at $\lambda = \tfrac{1}{2}$,
$c = -1$) \emph{is} chirally Koszul:
exec
/bin/zsh -lc "sed -n '16840,16920p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\bottomrule
\multicolumn{6}{l}{\textsuperscript{$\ast$}%
 Stratum-separated global family:
 $S_2 = 6\lambda^2 - 6\lambda + 1$, $S_3 = 0$,
 $S_4 = -5/12$, $S_r = 0$ for $r \geq 5$.
 The charged quartic lies off the $T$-line, so the single-line
 discriminant is not the class-$\mathbf{C}$ witness.}
\end{tabular}
\end{center}
\end{example}

\begin{theorem}[Shadow archetype classification]
\label{thm:shadow-archetype-classification}
\ClaimStatusProvedHere
\index{shadow depth!classification theorem|textbf}
\index{shadow archetype classification|textbf}
Every chirally Koszul algebra in the standard landscape has algebraic
shadow depth
\[
 d_{\mathrm{alg}}(\cA) \in \{0,\, 1,\, 2,\, \infty\}.
exec
/bin/zsh -lc "rg -n 'thm:nms-archetype-trichotomy' chapters/theory appendices | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:1208:\label{thm:nms-archetype-trichotomy}
appendices/nonlinear_modular_shadows.tex:2490:Parts~(i)--(iii) are Theorems~\ref{thm:nms-shadow-master-equations}, \ref{thm:nms-separating-boundary-recursion}, and \ref{thm:nms-shadow-cocycle-characterization}. Part~(iv) is Theorem~\ref{thm:nms-archetype-trichotomy}. Part~(v) is Theorems~\ref{thm:nms-virasoro-mixed-shadow} and \ref{thm:nms-principal-wn-contact-nonvanishing} together with Corollary~\ref{cor:nms-principal-wn-mixed}. Part~(vi) is Construction~\ref{constr:nms-gram-determinant-line} and Definition~\ref{def:nms-modular-quartic-resonance-class}. Part~(vii) is Theorems~\ref{thm:nms-clutching-law-modular-resonance} and \ref{thm:nms-first-nonlinear-shadow-theta}. Part~(viii) is Theorems~\ref{thm:nms-all-degree-master-equation} and~\ref{thm:nms-finite-termination}. Parts~(ix) and~(x) are Theorem~\ref{thm:nms-nonseparating-clutching-law}, Corollary~\ref{cor:nms-genus-one-hessian-correction}, and Theorem~\ref{thm:nms-genus-loop-model-families}.\qedhere
appendices/nonlinear_modular_shadows.tex:2917:These names are a proposal, not yet a theorem; the shadow obstruction tower determines the singularity type of the wavefunction, so the archetype trichotomy of Theorem~\ref{thm:nms-archetype-trichotomy} becomes a classification of local wavefunctions by catastrophe type.
chapters/theory/higher_genus_modular_koszul.tex:32054:(Theorem~\ref{thm:nms-archetype-trichotomy}):
chapters/theory/higher_genus_modular_koszul.tex:32294:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/chiral_koszul_pairs.tex:3329:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/chiral_koszul_pairs.tex:3450:(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
chapters/theory/higher_genus_complementarity.tex:5436:(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
chapters/theory/higher_genus_complementarity.tex:6092:(Theorem~\ref{thm:nms-archetype-trichotomy}).
exec
/bin/zsh -lc "sed -n '32044,32066p' chapters/theory/higher_genus_modular_koszul.tex && printf '\\n---\\n' && sed -n '32286,32304p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

The separating-clutching shell
$\Theta^{(2)}_{\mathrm{sep}\circ\mathrm{loop}} =
-\Delta(\Theta^{(1)}) - d_{\mathrm{sew}}^{(2)}$
is nonzero iff $\Theta^{(1)}$ has nontrivial
separating-node data, which occurs iff the cubic
shadow $\mathfrak{C}(\cA) \neq 0$, i.e.,
$\ell_3^{(0),\mathrm{tr}}|_{H^*} \neq 0$
(Proposition~\ref{prop:shadow-formality-low-degree}(ii)).
By the archetype classification
(Theorem~\ref{thm:nms-archetype-trichotomy}):
$\mathfrak{C} = 0$ for classes $G$ and $C$ (Heisenberg
and $\beta\gamma$); $\mathfrak{C} \neq 0$ for classes
$L$ and $M$ (affine and Virasoro).

The planted-forest shell
$\Theta^{(2)}_{\mathrm{pf}} = -d_{\mathrm{pf}}^{(2)}$
depends on all shadow data through the genus-$2$
planted-forest graph sum. The scalar trace is
$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$

thinking
**Evaluating theorem classification**

I’m considering that the table I’m working on should include all relevant classes. But it seems I might have the wrong theorem here, as `thm:nms-archetype-trichotomy` doesn’t effectively classify the G/L/C/M classes. That feels off, so I definitely need to inspect this more thoroughly to get it right. Let’s make sure everything is classified properly!
exec
/bin/zsh -lc "sed -n '32304,32326p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
 & 2 & \text{all vertices binary}
 & 42/42\text{ scalar (}\kappa\text{-only)} \\
L\;\text{(Lie/tree)}
 & 3 & \operatorname{val}(v) \geq 3\text{ activates cubic}
 & \text{cubic corrections at graphs with 3-valent vertices} \\
C\;\text{(contact)}
 & 4 & \operatorname{val}(v) \geq 4\text{ activates quartic}
 & \text{quartic at 4-valent vertices; cubic absent} \\
M\;\text{(mixed)}
 & \infty & \text{all degrees active}
 & \text{all 42 graphs carry higher-degree corrections}
\end{array}
\]
For class~$G$ (Heisenberg), every graph contributes
$\kappa^{|E|}/|\operatorname{Aut}|$ and the sum recovers
$F_3 = \kappa\cdot 31/967680$.
For class~$L$ (affine), graphs with a vertex of valence~${\geq}\,3$
acquire cubic shadow corrections from $\mathfrak{C}(\cA)$.
For class~$C$ ($\beta\gamma$), the quartic contact invariant
$\mathfrak{Q}^{\mathrm{contact}}$ contributes at graphs with a
exec
/bin/zsh -lc "sed -n '6086,6098p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 The shadow obstruction tower is infinite. All trace-log terms
 $\operatorname{Tr}((C_1 B_2)^m)$ contribute, and the anomaly
 series does not truncate. The full metaplectic cocycle carries
 infinite-order modular data.
\end{itemize}
This is the holographic restatement of the archetype trichotomy
(Theorem~\ref{thm:nms-archetype-trichotomy}).
\end{remark}

\begin{remark}[Shadow tower as $A_\infty$ coproduct corrections (Vol~III)]
\label{rem:shadow-ainfty-coproduct-vol3}
The shadow invariants $S_k$ have a second interpretation discovered in Vol~III: they are the coefficients of the $A_\infty$ corrections $\delta^{(k)}$ to the Yangian coproduct $\Delta_z$. The full $A_\infty$ coproduct is $\Delta_z^{A_\infty} = \Delta_z^{\mathrm{Yangian}} + \sum_{k \geq 3} \hbar^{k-1} \delta^{(k)}$, where $\delta^{(3)}$ has coefficient $\alpha = 2$ (from $m_3(T,T,T) = -2T$) and $\delta^{(4)}$ has coefficient $S_4 = 10/27$ (from $m_4(T,T,T,T) = (40/27)T$). For class~$G$: all $\delta^{(k)} = 0$ and the Yangian coproduct is exact. For class~$M$: the coproduct has infinite corrections whose coefficients are precisely the shadow tower $\{S_k\}$. The shadow tower is therefore not merely a classification invariant: it encodes the $A_\infty$ corrections to the chiral quantum group coproduct. See Vol~III, Remark~\texttt{rem:ainfty-coproduct-shadow}.
\end{remark}
exec
/bin/zsh -lc "sed -n '16962,16976p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$S_4 = -5/12$, and Theorem~\ref{thm:betagamma-global-depth} gives
$S_r = 0$ for $r \geq 5$. Hence $d_{\mathrm{alg}} = 2$ and
$r_{\max} = 4$.

(iv)~For Virasoro, the cubic and quartic shadows coexist, and their
Poisson bracket $\{\mathfrak{C}, \mathfrak{Q}\}_H$ is non-zero for
generic $c$
(Theorem~\ref{thm:w-virasoro-quintic-forced}); the all-degree master
equation (Theorem~\ref{thm:nms-all-degree-master-equation}) then
forces all higher obstructions to be non-zero by induction.

That all four families are Koszul follows from
Proposition~\ref{prop:pbw-universality} (PBW implies Koszulness)
for affine and W-algebras, and from the diagonal
Ext-vanishing criterion

thinking
**Inspecting theorem assumptions**

I’m wondering if the theorem provides a recurrence relationship, and I'm cautious not to overcomplicate matters. I think there might be an issue with the assumption that `S_A` satisfies CME when concluding about the vanishing in `chiral_hochschild`. I need to check if the theorem’s statement, especially around 1138, explicitly mentions this assumption. It seems it doesn't address complementarity potential or CME, which could be a hidden seam in the hypothesis. Let’s take a closer look at the theorem.
exec
/bin/zsh -lc "sed -n '1120,1160p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
The modular convolution algebra
\[
\gAmod
\;=\;
\prod_{g,n}\,
\operatorname{Hom}_{\Sigma_n}\!\bigl(
 C_*(\overline{\cM}_{g,n}),\;
 \operatorname{End}_{\cA}(n)
\bigr)
\]
carries the five-component differential
$D = d_{\mathrm{int}} + [\tau,-] + d_{\mathrm{sew}}
 + d_{\mathrm{pf}} + \hbar\Delta$
and the universal Maurer--Cartan element
$\Theta_{\cA} := D_{\cA} - d_0
\in \MC(\gAmod)$
\textup{(}Theorem~\textup{\ref{thm:mc2-bar-intrinsic})}.
Assume the full universal Maurer--Cartan element is scalar:
\begin{equation}\label{eq:one-channel-formality}
\Theta_{\cA}
exec
/bin/zsh -lc "sed -n '1100,1128p' chapters/theory/chiral_hochschild_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$n \geq 3$, and $\Etwo$-formality is automatic from
PBW concentration, not an additional hypothesis.

The converse ($\Etwo$-formality implies Koszulness) is false.
A non-Koszul algebra whose Hochschild cohomology happens
to concentrate in three degrees would also be $\Etwo$-formal
by the same argument. A stronger converse would require
the scalar-orbit formality problem discussed
below, for which no converse is proved here
\textup{(}Theorem~\textup{\ref{thm:convolution-formality-one-channel}}\textup{)}.
\end{remark}

\begin{theorem}[Scalar universal class implies convolution
formality along its distinguished orbit;
\ClaimStatusProvedHere]
\label{thm:convolution-formality-one-channel}
\index{formality!convolution algebra}
\index{one-channel!scalar-orbit formality problem}
\index{scalar saturation|see{one-channel}}
Let $\cA$ be a modular Koszul chiral algebra.


thinking
**Analyzing the fix**

The user wants an exact solution, not just a diagnosis. A safe minimal fix would be to add the missing hypothesis to both the theorem statement and the proof. For instance, in the theorem statement, I could add that the complementarity potential exists and satisfies the classical master equation. In the proof, I’d adjust the cited sentence for clarity regarding conditions. However, the severity might be rated HIGH or even CRITICAL due to the hidden hypothesis not being stated clearly. Let's solidify that perspective!
thinking
**Assessing theorem validity**

The theorem isn't necessarily false, but the proof as it's currently written is invalid or scoped improperly. Under a developer review mindset, the findings could be rated as CRITICAL since the theorem is marked as ProvedHere but depends on a conditional appendix theorem. I should look for other hidden-hypothesis citations from the theory to appendix theorems that might have similar assumptions. For example, the `thm:nms-finite-termination` might be relevant, but it doesn't seem to cover class M. I’ll need to inspect additional theorem assumptions and their applications.
exec
/bin/zsh -lc "sed -n '3466,3484p' chapters/theory/bar_cobar_adjunction_inversion.tex && printf '\\n---\\n' && sed -n '580,606p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 produces the homotopy Koszul dual \emph{algebra}; equivalently,
 $\mathbb{D}_{\mathrm{Ran}}(\widehat{\mathcal{C}}) \simeq \barB(\cA^!)$
 as factorization coalgebras
 \textup{(}Convention~\ref{conv:bar-coalgebra-identity}\textup{)}.
 These are two descriptions of the same object: the
 identification of $\cA^!_\infty$ with $\barB(\cA^!)$ is the content
 of Theorem~A.
\end{itemize}

\emph{Step 1: Check necessary conditions}
(Theorem~\ref{thm:essential-image-koszul}):
\begin{itemize}
\item[$\square$] Conilpotent? ($\bigcap_n \text{coker}(\Delta^n) = 0$)
\item[$\square$] Connected? ($\epsilon\colon \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}$)
\item[$\square$] Geometrically representable? (arises from configuration spaces)
\item[$\square$] Curvature central? (if curved)
\item[$\square$] Formally complete? (with respect to coaugmentation)
\end{itemize}


exec
/bin/zsh -lc "rg -n \"label\\{thm:essential-image-koszul\\}\" -n appendices/koszul_reference.tex && sed -n '590,634p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
268:\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
\textup{(Positselski \cite{Positselski11})}
A coalgebra $\widehat{\mathcal{C}}$ satisfying the conditions of Theorem~\ref{thm:essential-image-koszul} (conilpotency, connectedness, geometric representability, curvature centrality) is the Koszul dual of some algebra $\mathcal{A}$ if and only if it is \emph{complete} with respect to its coaugmentation coideal:
\[\widehat{\mathcal{C}} = \varprojlim_n \widehat{\mathcal{C}} / \bar{\mathcal{C}}^n\]
\end{theorem}

\begin{proof}
\emph{($\Rightarrow$) Necessity.}
If $\widehat{\mathcal{C}} = \mathcal{A}^!$, then the filtration on $\mathcal{A}$ by 
powers of the augmentation ideal induces a cofiltration on $\widehat{\mathcal{C}}$:
\[F^n\widehat{\mathcal{C}} = \{c : \Delta^k(c) \in (\bar{\mathcal{C}})^{\otimes k} 
\text{ for } k \leq n\}\]

The completion is:
\[\widehat{\mathcal{C}} = \varprojlim_n \widehat{\mathcal{C}} / \bar{\mathcal{C}}^n\]

This holds by construction of $\mathcal{A}^!$.

\emph{($\Leftarrow$) Sufficiency.}
If $\widehat{\mathcal{C}}$ is complete, define:

thinking
**Investigating circular references**

I noticed something odd: the section starts printing at 590, but it’s referencing text from 268. This could be a result of using `rg` with `sed`. There's also a self-reference in the theorem text that points to itself, creating a circular reference. But wait, it’s only in the appendix. Still, it seems relevant since the main body mentions it at line 3476. I need to check the lines around 260-280 for more context.
codex
This exposed a stronger seam problem than a bad noun. One body theorem proof is importing an appendix theorem under a hypothesis that never appears in the body statement, and another body chapter cites an appendix theorem whose target doesn’t say what the body claims it says. I’m verifying both directly against the target theorem text now.
exec
/bin/zsh -lc "sed -n '1110,1178p' chapters/theory/chiral_hochschild_koszul.tex && printf '\\n---\\n' && sed -n '2106,2126p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '260,282p' appendices/koszul_reference.tex && printf '\\n---\\n' && sed -n '3468,3480p' chapters/theory/bar_cobar_adjunction_inversion.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '32048,32060p' chapters/theory/higher_genus_modular_koszul.tex && printf '\\n---\\n' && sed -n '3444,3452p' chapters/theory/chiral_koszul_pairs.tex && printf '\\n---\\n' && sed -n '1208,1230p' appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{remark}

\begin{theorem}[Scalar universal class implies convolution
formality along its distinguished orbit;
\ClaimStatusProvedHere]
\label{thm:convolution-formality-one-channel}
\index{formality!convolution algebra}
\index{one-channel!scalar-orbit formality problem}
\index{scalar saturation|see{one-channel}}
Let $\cA$ be a modular Koszul chiral algebra.
The modular convolution algebra
\[
\gAmod
\;=\;
\prod_{g,n}\,
\operatorname{Hom}_{\Sigma_n}\!\bigl(
 C_*(\overline{\cM}_{g,n}),\;
 \operatorname{End}_{\cA}(n)
\bigr)
\]
 succeeded in 51ms:
\end{question}

\begin{remark}\label{rem:why-essential-image-matters}
The essential image question decomposes into four subproblems: \emph{recognition} (given a coalgebra, determine whether it is a Koszul dual), \emph{completeness} (whether every coalgebra arises), \emph{uniqueness} (whether $\mathcal{A}$ is determined by $\mathcal{A}^!$), and \emph{reconstruction} (recovering $\mathcal{A}$ from $\widehat{\mathcal{C}}$).
\end{remark}

\subsection{Main characterization theorem}

\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
A chiral coalgebra $\widehat{\mathcal{C}}$ is (isomorphic to) the Koszul dual 
$\mathcal{A}^!$ of some chiral algebra $\mathcal{A}$ if and only if:

\begin{enumerate}
\item \emph{Conilpotency.} $\widehat{\mathcal{C}}$ is conilpotent: every element of $\ker(\epsilon)$ is annihilated by a sufficiently high iterate of the reduced coproduct $\bar{\Delta}$:
 \[\ker(\epsilon) = \bigcup_{n \geq 0} \ker(\bar{\Delta}^{(n)})\]
 
\item \emph{Connected.} The counit is surjective onto the ground field:
 \[\epsilon: \widehat{\mathcal{C}} \twoheadrightarrow \mathbb{C}\]
 
\item \emph{Geometric representability.} $\widehat{\mathcal{C}}$ admits a presentation as sections of a $\mathcal{D}_X$-module coalgebra on the Ran space of~$X$; equivalently, there exists a factorization coalgebra~$\mathcal{F}$ such that $\widehat{\mathcal{C}} \simeq \Gamma(\mathrm{Ran}(X),\, \mathcal{F})$, compatible with the operadic structure of the Fulton--MacPherson compactification
 succeeded in 51ms:
is nonzero iff $\Theta^{(1)}$ has nontrivial
separating-node data, which occurs iff the cubic
shadow $\mathfrak{C}(\cA) \neq 0$, i.e.,
$\ell_3^{(0),\mathrm{tr}}|_{H^*} \neq 0$
(Proposition~\ref{prop:shadow-formality-low-degree}(ii)).
By the archetype classification
(Theorem~\ref{thm:nms-archetype-trichotomy}):
$\mathfrak{C} = 0$ for classes $G$ and $C$ (Heisenberg
and $\beta\gamma$); $\mathfrak{C} \neq 0$ for classes
$L$ and $M$ (affine and Virasoro).

The planted-forest shell
$\Theta^{(2)}_{\mathrm{pf}} = -d_{\mathrm{pf}}^{(2)}$

---
\end{tabular}
\end{center}
All five are chirally Koszul (genus-$0$ slice is formal), yet the
Virasoro algebra has infinite shadow depth
($\mathfrak{o}^{(5)}_{\mathrm{Vir}} \neq 0$

thinking
**Clarifying geometric concepts**

I'm thinking about geometric representability and curvature centrality. There's a theorem stating that curvature is a central term in dual algebra. The bullet point is asking if curvature is central when curved, which is an interesting question. I should look into the remaining lines of the theorem statement after line 282 to ensure everything is confirmed and complete. There's a bit of detail to sort through here! Let's keep digging!
exec
/bin/zsh -lc "sed -n '282,324p' appendices/koszul_reference.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 is central in the dual algebra
 
\item \emph{Formal completeness.} $\widehat{\mathcal{C}}$ is complete with respect 
 to its coaugmentation coideal
\end{enumerate}

Each condition reflects a structural property of bar coalgebras:
conilpotency ensures the cobar differential converges,
connectedness ensures augmentation,
geometric representability ensures the coalgebra lives on configuration spaces (not abstractly),
curvature centrality ensures $d^2 = [\mu_0, -]$ (the curved $A_\infty$ relation),
and formal completeness ensures the inverse limit over finite stages is well-behaved.

When these conditions hold, the algebra $\mathcal{A}$ is recovered by:
\[\mathcal{A} = \Omega(\widehat{\mathcal{C}})\]
(cobar construction), and this is unique up to quasi-isomorphism.
\end{theorem}

\begin{proof}[Proof outline]
The proof has two directions, each established by the lemmas and theorems in the following subsections.






thinking
**Checking citation correctness**

I realized that the checklist bullet is inaccurate—it's about citation correctness. The severity might be high or medium since the body theorem step misstates the criterion from the appendix theorem, which can lead to different mathematical implications. I’ll report the exact fix. Other checklist items might be okay, but I should inspect if Step 1 uses the theorem properly. There could be more cross-directory mismatches, so I could search for theory sources citing the appendix theorem and compare. I've identified at least four findings already.
thinking
**Searching for citation discrepancies**

I might take a while, but I'll search for citations related to `thm:nms-finite-termination`, particularly around body lines that mention four classes. It's important to focus on the theorem's framing of families and Virasoro. For instance, line 5444 in `higher_genus_complementarity` references an infinite shadow tower from that theorem, but it contrasts with Virasoro without mentioning W_N specifically. I should also look into citations for `thm:nms-archetype-trichotomy` and `thm:essential-image-koszul`, along with checking for potential misreferences in homotopy_transfer. Cross-directory inconsistencies could be insightful!
thinking
**Exploring comparison methods**

I'm considering whether to use cross_edges for a manual context comparison, but it seems not feasible. However, automating the process by matching label names might be a better approach. It could streamline things and make it easier to analyze. Hmm, I need to think through the details of how that would work. I should consider what steps are needed to implement this automation effectively. That way, I can ensure accuracy and efficiency in the comparison process!
thinking
**Analyzing theorem references**

I'm looking at line 3476, which references an appendix theorem later on, perhaps after the bar-cobar theorem has been proven. This doesn’t seem circular regarding earlier theorems. But if Step 1 is part of the section about determining if a coalgebra is in the essential image, that’s not related to theorem B proof. However, if the appendix theorem relies on theorem B, that could create a problematic dependency. But since line 3476 appears after theorem B, it seems okay — now I’ll check the `bar_cobar_adjunction_inversion.tex` around line 3476 to see if it’s a theorem or just an expository text.
thinking
**Identifying formula and nomenclature issues**

I’ve noticed that the body’s Step 1 bullet for conilpotent uses an incorrect formula, and that’s problematic. There might also be a nomenclature issue since the label `ch:ordered-associative-chiral-kd` appears in both the appendices and the chapters/theory. This could lead to confusion in referencing or understanding the content. It’s essential to clarify these discrepancies to maintain proper consistency throughout the work. I should highlight this as a potential area for revision.
thinking
**Identifying duplicate labels**

I see there's a problem with duplicate labels defined in different directories, specifically `ch:ordered-associative-chiral-kd`. This creates ambiguity in cross-references, which is significant. I need to verify this and search for any other duplicate labels as well. The last-definition rule in LaTeX could lead to unexpected resolutions based on inclusion order. It’s crucial to programmatically detect all duplicates defined across appendices and theory to resolve any issues. Great catch on this! Let's work on identifying those duplicates.
codex
I found a more structural seam defect: at least one chapter label is defined in both `appendices/` and `chapters/theory/`, so cross-references on that surface are ambiguous by construction. I’m enumerating cross-directory duplicate labels now because those can silently redirect citations even when the prose looks fine.
exec
/bin/zsh -lc "perl -e '
my %lab;
for my "'$f (glob("appendices/*.tex"), glob("chapters/theory/*.tex")) { open my $fh, "<", $f or die $!; my $ln=0; while(<$fh>){$ln++; while(/'"\\\\label\\{(["'^}]+)'"\\}/g){ push @{"'$lab{$1}}, "$f:$ln"; }} close $fh; }
for my $k (sort keys %lab){ my @a = grep { /''^appendices'"\\// } @{"'$lab{$k}}; my @t = grep { /''^chapters'"\\/theory\\// } @{"'$lab{$k}}; next unless @a && @t; print "$k'"\\n\"; print \"  "'$_'"\\n\" for (@a,@t); }
'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
D1
  appendices/ordered_associative_chiral_kd.tex:2805
  chapters/theory/ordered_associative_chiral_kd.tex:2491
D2
  appendices/ordered_associative_chiral_kd.tex:2807
  chapters/theory/ordered_associative_chiral_kd.tex:2493
D3
  appendices/ordered_associative_chiral_kd.tex:2810
  chapters/theory/ordered_associative_chiral_kd.tex:2496
D4
  appendices/ordered_associative_chiral_kd.tex:2812
  chapters/theory/ordered_associative_chiral_kd.tex:2498
D5
  appendices/ordered_associative_chiral_kd.tex:2814
  chapters/theory/ordered_associative_chiral_kd.tex:2500
D6
  appendices/ordered_associative_chiral_kd.tex:2818
  chapters/theory/ordered_associative_chiral_kd.tex:2504
ch:ordered-associative-chiral-kd
  appendices/ordered_associative_chiral_kd.tex:37






thinking
**Addressing duplicate chapters**

Wow, I’ve found many duplicates because the same chapter is in both directories, creating a significant seam issue. I need to verify if all copies are relevant since one might not be included. It’s essential to check whether the body cites those labels, causing ambiguity. I should report the global duplicate rather than listing hundreds of them, but the user wants every inconsistency. Maybe I should summarize the critical finding and provide exact fixes.
thinking
**Refining the fix for duplicates**

I think the exact solution is to avoid keeping the same chapter under both paths with identical labels. We should choose a canonical source and either stop including `appendices/ordered_associative_chiral_kd.tex` in the build or rename every label in that file with an `appendix-` or `v1-` suffix. The user asked for precise fixes, but providing one for each duplicate would be overwhelming. I might present the entire duplicated file surface as one systemic inconsistency. I'll cite necessary lines to clarify this.
thinking
**Identifying the duplication issue**

I can specify `appendices/ordered_associative_chiral_kd.tex:37` and `chapters/theory/ordered_associative_chiral_kd.tex:37`. The problem here is that the entire chapter is duplicated under the same label namespace in both directories, leading to ambiguous references throughout the seam, like `ch:ordered-associative-chiral-kd`, `thm:ordered-associative-ds-principal`, and others. This duplication creates confusion, so it's crucial to address it to ensure clarity in the references.
thinking
**Inspecting potential fixes**

I’m considering if I need to make exact fixes at those source lines. The adjustments might involve renaming duplicate labels and updating references to point to the canonical chapter label in `chapters/theory/ordered_associative_chiral_kd.tex`. But if they’re the same right now, that makes it tricky. I think the theory copy should own the chapter label, but I wonder if there could be other duplicate labels elsewhere. The duplicate scan only shows one file, so I’ll need to inspect the references further.
thinking
**Renaming chapter references**

I need to rename the chapter labels across the whole file, as there are so many. To do this, I could use a prefix like `v1-` or `appendix-`. The guidelines suggest suffixing duplicates with `v1-/v2-/v3-`, but for the appendix, I might just drop the duplicate copy. A better approach could be to exclude the appendix from the build if the canonical version is in the chapters folder. That way, it solves the duplicate issue nicely!
thinking
**Verifying file compilation**

I might need to check if both files are included in the compilation by inspecting main.tex. But maybe that won't be necessary, since if the appendix duplicate isn't included, the duplicate labels shouldn't cause any issues. However, I see that the cross_edges and the user's file set indicate both exist, which makes it a bit tricky. It’s important for me to verify if both are included in the build, as that really matters!
exec
/bin/zsh -lc "rg -n 'ordered_associative_chiral_kd' . | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./FRONTIER.md:535:**thm:glN-chiral-qg** in `ordered_associative_chiral_kd.tex`. W_N carries a chiral quantum group datum for ALL N ≥ 1: N×N transfer matrix T(u), Yang R-matrix R(u) = uI + Psi·P, Drinfeld coproduct Delta_z(T(u)) = T(u)·T(u-z) as matrix multiplication in C^N, non-trivial RTT for N ≥ 2.
./FRONTIER.md:575:**prop:critical-level-ordered** in `ordered_associative_chiral_kd.tex`. At k = -h^v for sl_2:
./foundation_audit_chapters_report.md:346:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:356 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 407, before the next claim at line 411.
./foundation_audit_chapters_report.md:347:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:411 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 504, before the next claim at line 508.
./foundation_audit_chapters_report.md:348:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1640 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1653, before the next claim at line 1655.
./foundation_audit_chapters_report.md:349:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1655 — PROBLEM: `\ClaimStatusProvedHere` proposition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1677, before the next claim at line 1679.
./foundation_audit_chapters_report.md:350:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1679 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1701, before the next claim at line 1706.
./foundation_audit_chapters_report.md:351:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1706 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1736, before the next claim at line 1738.
./foundation_audit_chapters_report.md:352:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1752 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1786, before the next claim at line 1791.
./foundation_audit_chapters_report.md:353:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1791 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1829, before the next claim at line 1834.
./foundation_audit_chapters_report.md:354:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1834 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1885, before the next claim at line 1887.
./foundation_audit_chapters_report.md:355:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1912 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 1955, before the next claim at line 1960.
./foundation_audit_chapters_report.md:356:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:1960 — PROBLEM: `\ClaimStatusProvedHere` construction has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2018, before the next claim at line 2020.
./foundation_audit_chapters_report.md:357:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:2875 — PROBLEM: `\ClaimStatusProvedHere` corollary has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 2888, before the next claim at line 2890.
./foundation_audit_chapters_report.md:358:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:3632 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 3662, before the next claim at line 3664.
./foundation_audit_chapters_report.md:359:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:4641 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 4668, before the next claim at line 4686.
./foundation_audit_chapters_report.md:360:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:5089 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 5108, before the next claim at line 5110.
./foundation_audit_chapters_report.md:361:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:5161 — PROBLEM: `\ClaimStatusProvedHere` definition has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 5196, before the next claim at line 5198.
./foundation_audit_chapters_report.md:362:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:5345 — PROBLEM: `\ClaimStatusProvedHere` observation has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 5360, before the next claim at line 5362.
./foundation_audit_chapters_report.md:363:- [CRITICAL] chapters/theory/ordered_associative_chiral_kd.tex:5362 — PROBLEM: `\ClaimStatusProvedHere` observation has no `\begin{proof}` within 50 lines. FIX: insert `\begin{proof}...\end{proof}` immediately after line 5378, before the next claim at line 5380.



thinking
**Evaluating document structure**

I'm considering how the main.tex inputs chapters and theories without including the appendix copy; this means duplicate labels might not disrupt the build. The user wants to check for relevant files, which could reveal whether the appendix copy is referenced in the main theory. This raises some questions about potential inconsistencies between the seams of the directories. While it may not cause build issues with duplicates dormant, the presence in the metadata could still lead to confusion.
thinking
**Analyzing appendices and theory**

The mission requires linking appendices to the theory without creating circular dependencies. If the appendix isn’t compiled, it seems less relevant. Still, the theorem registry reflects both files with 89 claims, potentially causing confusion within the metadata due to overlapping labels. The user asked for clarity on file contents. I should report on this seam issue since it could affect future references. It might need a fix by removing or renaming the appendix duplicate in the metadata, which could be considered a critical concern.
thinking
**Formatting findings for citation**

I need to cite exact lines from both the main document and theorem registry, even if that seems beyond the mission scope, as it relates to seam issues. The user requested a specific format of file:line. I can include references like appendices/ordered_associative_chiral_kd.tex:37, chapters/theory/ordered_associative_chiral_kd.tex:37, main.tex:1140, and metadata/theorem_registry.md:59-60. The final contract specifies findings must be in [SEVERITY] file:line format—but can one file have multiple citations? I need to clarify that.
exec
/bin/zsh -lc "sed -n '56,62p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
| `chapters/connections/arithmetic_shadows.tex` | 135 |
| `chapters/theory/bar_cobar_adjunction_curved.tex` | 113 |
| `chapters/examples/yangians_drinfeld_kohno.tex` | 97 |
| `appendices/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/ordered_associative_chiral_kd.tex` | 89 |
| `chapters/theory/higher_genus_complementarity.tex` | 80 |
| `chapters/examples/w_algebras.tex` | 70 |

thinking
**Evaluating potential issues**

I’m wondering if there are other mirrored duplicates not included in the build. Should I search the main inputs appendices? It might not be necessary. There could be an issue with `main.tex` only including theory while the introduction references the appendix path. I think cross-directory citations to appendix `signs_and_shifts` should be fine, but I need to check the `koszul_reference.tex` theorem statement and the body step on `bar_cobar_adjunction_inversion`. There might be a hidden issue related to the theorem's proof, and I need to investigate the condition with the wrong formula too, checking for similar errors elsewhere.
exec
/bin/zsh -lc "rg -n '\\\\bigcap_n \\\\text\\{coker\\}\\(\\\\Delta\\"'^n'"\\) = 0|coker\\(\\\\Delta\\"'^n'"\\)' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_cobar_adjunction_inversion.tex:3478:\item[$\square$] Conilpotent? ($\bigcap_n \text{coker}(\Delta^n) = 0$)

thinking
**Searching for essential image**

I'm thinking I need to search for `thm:essential-image-koszul` to gather relevant information. It seems like a specific term that's probably linked to a particular theory in my database. I'll check through the resources I have, looking for anything that can provide clarity. This could help in connecting the dots. Let's see what I can learn from this search!
exec
/bin/zsh -lc "rg -n 'thm:essential-image-koszul' chapters/theory appendices" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/koszul_reference.tex:268:\begin{theorem}[Essential image of Koszul duality; \ClaimStatusProvedHere]\label{thm:essential-image-koszul}
appendices/koszul_reference.tex:591:A coalgebra $\widehat{\mathcal{C}}$ satisfying the conditions of Theorem~\ref{thm:essential-image-koszul} (conilpotency, connectedness, geometric representability, curvature centrality) is the Koszul dual of some algebra $\mathcal{A}$ if and only if it is \emph{complete} with respect to its coaugmentation coideal:
chapters/theory/bar_cobar_adjunction_inversion.tex:3476:(Theorem~\ref{thm:essential-image-koszul}):
exec
/bin/zsh -lc "sed -n '2248,2256p' chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Yangians (Ch.~\ref{chap:yangians}) &
 $\Eone$-chiral bar on ordered configurations; $R$-matrix inversion; DK bridge; dg-shifted Yangian \\
Genus expansions (Ch.~\ref{ch:genus-expansions}) &
 Explicit expansions: modular forms, Eisenstein, Mumford, bosonization
 (Remark~\ref{rem:bosonization-not-koszul}: bosonization $\neq$ Koszul duality) \\
Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
 Bar tables through high degree; OEIS; growth rates \\[6pt]
\multicolumn{2}{@{}l}{\textbf{Part~\ref{part:physics-bridges}: Physics Bridges} \emph{(connections to physics and adjacent mathematics)}} \\[3pt]
\hline
exec
/bin/zsh -lc "rg -n -F 'Chs.~' chapters/theory appendices | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/theory/introduction.tex:2220:Koszul pairs + deformation theory (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}) &
chapters/theory/introduction.tex:2246:Deformation quantization (Chs.~\ref{ch:chiral-deformation}--\ref{chap:deformation-examples}) &
chapters/theory/introduction.tex:2253:Computations + combinatorial frontier (Chs.~\ref{chap:detailed-computations}--\ref{app:combinatorial-frontier}) &
chapters/theory/introduction.tex:2265:Yang--Mills boundary (Chs.~\ref{ch:ym-boundary-theory}--\ref{ch:ym-instanton-screening}) &
chapters/theory/introduction.tex:2363: (Chs.~\ref{chap:koszul-pairs}--\ref{chap:deformation-theory}).
exec
/bin/zsh -lc "rg -n 'thm:nms-all-degree-master-equation' chapters/theory appendices | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:87:(Theorem~\ref{thm:nms-all-degree-master-equation}),
appendices/nonlinear_modular_shadows.tex:2110:\label{thm:nms-all-degree-master-equation}
appendices/nonlinear_modular_shadows.tex:2490:Parts~(i)--(iii) are Theorems~\ref{thm:nms-shadow-master-equations}, \ref{thm:nms-separating-boundary-recursion}, and \ref{thm:nms-shadow-cocycle-characterization}. Part~(iv) is Theorem~\ref{thm:nms-archetype-trichotomy}. Part~(v) is Theorems~\ref{thm:nms-virasoro-mixed-shadow} and \ref{thm:nms-principal-wn-contact-nonvanishing} together with Corollary~\ref{cor:nms-principal-wn-mixed}. Part~(vi) is Construction~\ref{constr:nms-gram-determinant-line} and Definition~\ref{def:nms-modular-quartic-resonance-class}. Part~(vii) is Theorems~\ref{thm:nms-clutching-law-modular-resonance} and \ref{thm:nms-first-nonlinear-shadow-theta}. Part~(viii) is Theorems~\ref{thm:nms-all-degree-master-equation} and~\ref{thm:nms-finite-termination}. Parts~(ix) and~(x) are Theorem~\ref{thm:nms-nonseparating-clutching-law}, Corollary~\ref{cor:nms-genus-one-hessian-correction}, and Theorem~\ref{thm:nms-genus-loop-model-families}.\qedhere
appendices/nonlinear_modular_shadows.tex:3543:(Theorem~\ref{thm:nms-all-degree-master-equation}) generates
chapters/theory/higher_genus_modular_koszul.tex:12708:(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
chapters/theory/higher_genus_modular_koszul.tex:16970:equation (Theorem~\ref{thm:nms-all-degree-master-equation}) then
chapters/theory/chiral_hochschild_koszul.tex:1172:(Theorem~\ref{thm:nms-all-degree-master-equation}).
exec
/bin/zsh -lc "sed -n '12700,12714p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proof}

\begin{proposition}[All-degree master equation from MC]
\label{prop:master-equation-from-mc}
\ClaimStatusProvedHere
\index{all-degree master equation!from Maurer--Cartan}
The all-degree master equation
$\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$
(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
consequence of the Maurer--Cartan equation for
$\Theta_{\cA} \in \MC(\Defcyc^{\mathrm{mod}}(\cA))$: projecting
the MC equation $d\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ onto
the degree-$r$ component gives exactly
$\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$.
\end{proposition}

thinking
**Evaluating theorem implications**

Interesting! The theory proposes that the appendix theorem is a structural consequence of the MC equation. This might mean I can prove the all-degree master equation from MC without relying on complementarity potential assumptions. If that’s the case, it could challenge the appendix theorem's extra requirement and clarify some hidden hypotheses. I need to check whether this body proposition for Theta_A can support the chiral Hochschild theorem instead of the appendix theorem, thus avoiding that assumption. I should inspect the proof!
exec
/bin/zsh -lc "sed -n '12714,12740p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\end{proposition}

\begin{proof}
The MC equation $d\Theta + \tfrac{1}{2}[\Theta,\Theta] = 0$ holds
in $\Defcyc^{\mathrm{mod}}(\cA)$ by
Theorem~\ref{thm:mc2-bar-intrinsic}. Since the differential~$d$ and
the bracket $[-,-]$ respect the degree filtration, restricting to the
degree-$r$ component yields
$d(\operatorname{Sh}_r) + \sum_{r_1+r_2=r}
[\operatorname{Sh}_{r_1}, \operatorname{Sh}_{r_2}] = 0$,
which is exactly $\nabla_H(\operatorname{Sh}_r) + \mathfrak{o}^{(r)} = 0$.
\end{proof}

\begin{remark}[Shadow algebra as structural home]
\label{rem:shadow-algebra-structural-home}
\index{shadow algebra!structural role}
The shadow algebra governs the nonlinear modular characteristic.
The recursive obstruction construction
(Construction~\ref{constr:obstruction-recursion})
is the \emph{computational method} for extracting shadows; the


thinking
**Exploring classification inconsistencies**

I'm noticing a potential seam inconsistency between the appendix quartic trichotomy and the body full classification. It sounds like there might be similarities to explore. I wonder if looking more closely at these classifications could reveal some interesting patterns or issues. It’s definitely worth digging into to see how they align or where they might differ. Let’s see what I can uncover regarding their interactions and classifications!
thinking
**Verifying claims**

I need to make sure I’m not overclaiming anything here. It looks like `Checked: 182` might refer to a script that enumerated 182 cross-directory reference edges, but I should double-check that number. I want to ensure everything is accurate and nothing is being overstated. Counting these edges could help clarify my understanding and keep the information reliable. Let’s get down to the details!
exec
/bin/zsh -lc 'wc -l /tmp/cross_edges.txt && wc -l /tmp/undefined_refs.txt' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     813 /tmp/cross_edges.txt
     955 /tmp/undefined_refs.txt


thinking
**Analyzing edges and transitions**

I'm looking at the number of cross-directed edges, which is a hefty 813, including appendix and theory references. That's quite a lot, and it raises questions about how many were checked thoroughly. Another consideration is that I've read about 20 transition clusters. I want to summarize my findings accurately, possibly indicating checked edges and clusters. For line references, I need to choose between the appendix and the theory chapters, ensuring the theorem matches up. I'll propose a rewrite to clarify this.
thinking
**Clarifying citations and inconsistencies**

I’m considering the final format, which requires a single file reference with a specific line number. I could cite the appendix at line 2110 since the seam inconsistency starts there, but the body proposition has issues too. I might use "appendices/nonlinear_modular_shadows.tex:2110" and note the conflicting theory line as well. There are also other miscitations to address. Separating by file could enhance clarity while summarizing all miscitations related to the appendix theorem effectively.
exec
/bin/zsh -lc "rg -n 'prop:master-equation-from-mc|thm:shadow-archetype-classification|thm:nms-all-degree-master-equation|thm:nms-archetype-trichotomy' chapters/theory/higher_genus_modular_koszul.tex chapters/theory/chiral_koszul_pairs.tex chapters/theory/higher_genus_complementarity.tex chapters/theory/chiral_hochschild_koszul.tex appendices/nonlinear_modular_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
appendices/nonlinear_modular_shadows.tex:87:(Theorem~\ref{thm:nms-all-degree-master-equation}),
appendices/nonlinear_modular_shadows.tex:303:(Theorem~\ref{thm:shadow-archetype-classification}),
appendices/nonlinear_modular_shadows.tex:1208:\label{thm:nms-archetype-trichotomy}
appendices/nonlinear_modular_shadows.tex:2110:\label{thm:nms-all-degree-master-equation}
appendices/nonlinear_modular_shadows.tex:2490:Parts~(i)--(iii) are Theorems~\ref{thm:nms-shadow-master-equations}, \ref{thm:nms-separating-boundary-recursion}, and \ref{thm:nms-shadow-cocycle-characterization}. Part~(iv) is Theorem~\ref{thm:nms-archetype-trichotomy}. Part~(v) is Theorems~\ref{thm:nms-virasoro-mixed-shadow} and \ref{thm:nms-principal-wn-contact-nonvanishing} together with Corollary~\ref{cor:nms-principal-wn-mixed}. Part~(vi) is Construction~\ref{constr:nms-gram-determinant-line} and Definition~\ref{def:nms-modular-quartic-resonance-class}. Part~(vii) is Theorems~\ref{thm:nms-clutching-law-modular-resonance} and \ref{thm:nms-first-nonlinear-shadow-theta}. Part~(viii) is Theorems~\ref{thm:nms-all-degree-master-equation} and~\ref{thm:nms-finite-termination}. Parts~(ix) and~(x) are Theorem~\ref{thm:nms-nonseparating-clutching-law}, Corollary~\ref{cor:nms-genus-one-hessian-correction}, and Theorem~\ref{thm:nms-genus-loop-model-families}.\qedhere
appendices/nonlinear_modular_shadows.tex:2917:These names are a proposal, not yet a theorem; the shadow obstruction tower determines the singularity type of the wavefunction, so the archetype trichotomy of Theorem~\ref{thm:nms-archetype-trichotomy} becomes a classification of local wavefunctions by catastrophe type.
appendices/nonlinear_modular_shadows.tex:3543:(Theorem~\ref{thm:nms-all-degree-master-equation}) generates
chapters/theory/chiral_hochschild_koszul.tex:1172:(Theorem~\ref{thm:nms-all-degree-master-equation}).
chapters/theory/higher_genus_complementarity.tex:5436:(Theorem~\ref{thm:nms-archetype-trichotomy}) in geometric language.
chapters/theory/higher_genus_complementarity.tex:6092:(Theorem~\ref{thm:nms-archetype-trichotomy}).
chapters/theory/chiral_koszul_pairs.tex:78:(Theorem~\ref{thm:shadow-archetype-classification}), record the
chapters/theory/chiral_koszul_pairs.tex:2811:\textup{(}Theorem~\ref{thm:shadow-archetype-classification}; for
chapters/theory/chiral_koszul_pairs.tex:2927:degree~$2$. Theorem~\ref{thm:shadow-archetype-classification}
chapters/theory/chiral_koszul_pairs.tex:2947:\textup{(}Theorem~\ref{thm:shadow-archetype-classification}\textup{)}.
chapters/theory/chiral_koszul_pairs.tex:3329:(Theorem~\ref{thm:nms-archetype-trichotomy})
chapters/theory/chiral_koszul_pairs.tex:3450:(Theorem~\ref{thm:nms-archetype-trichotomy}) stratifies the
chapters/theory/higher_genus_modular_koszul.tex:106: (Proposition~\ref{prop:master-equation-from-mc}), the
chapters/theory/higher_genus_modular_koszul.tex:4590:(Theorem~\ref{thm:shadow-archetype-classification}), so
chapters/theory/higher_genus_modular_koszul.tex:12703:\label{prop:master-equation-from-mc}
chapters/theory/higher_genus_modular_koszul.tex:12708:(Theorem~\ref{thm:nms-all-degree-master-equation}) is a structural
exec
/bin/zsh -lc "sed -n '6076,6094p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\item \emph{Affine $\widehat{\mathfrak{sl}}_2$.}\;
 The shadow obstruction tower terminates at cubic order, so $C_1 B_2$ is
 nilpotent of order $\leq 2$ on the complementarity Hessian.
 The square $(C_1 B_2)^2$ typically survives, giving a nonzero
 $\mathfrak{N}_g$.
\item \emph{$\beta\gamma$.}\;
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





thinking
**Exploring duplicate surfaces**

I'm wondering if there are other duplicate surfaces in the theorem_registry across appendices or theory sections. It might make sense to search within just this specific file for clarity. I could potentially use excerpts from the theorem_registry itself as evidence. This thought has me thinking about how to effectively analyze the information for any overlaps or repetitions, which could be important for presenting accurate findings. Let's see what I can uncover!
thinking
**Considering label adjustments**

I think the exact fix I'm looking for is to keep just the `\label{sec:koszul-across-genera}` and change all appendix references to point to that label. This sounds straightforward, and it seems like it could work well. Now I'm feeling a bit better about that approach! It should help clarify my references, making things more organized in my document. So, let's go forward with that change!
thinking
**Evaluating criticality levels**

I'm trying to decide the criticality of several issues related to a theorem's surface disagreements and proofs with wrong hypotheses. The first is critical because of those disagreements. The second and third are high due to incorrect citations and formula issues affecting scope. There are two medium concerns: a metadata duplication and a namespace labeling issue. Lastly, a low concern involves a noun mismatch, but there's potential for another low one related to an appendix reference. It's quite detailed!
thinking
**Drafting final points**

I think I need to mention line numbers across multiple lines. That could help clarify things. I’ll aim to present my final points with seven clear bullets to make everything more organized. It seems like a good approach to create a structured summary that’s easy to follow. I wonder if that will help the user better understand the information! Let’s get started on drafting that!
codex
- [CRITICAL] appendices/nonlinear_modular_shadows.tex:2110 — PROBLEM: the appendix states the all-degree master equation only under the extra hypothesis that the complementarity potential satisfies the classical master equation, but chapters/theory/higher_genus_modular_koszul.tex:12703 proves the same equation unconditionally from the Maurer-Cartan equation for `\Theta_\cA`. The seam disagrees on what is actually proved. FIX: rewrite `thm:nms-all-degree-master-equation` to match `prop:master-equation-from-mc`: remove the CME hypothesis, state the equation as a projection of `\Theta_\cA \in \MC(\Defcyc^{\mathrm{mod}}(\cA))`, and move the Hamiltonian/CME presentation into a remark/corollary instead of the main theorem surface.

- [HIGH] chapters/theory/chiral_hochschild_koszul.tex:1172 — PROBLEM: the proof imports `thm:nms-all-degree-master-equation` as if it directly gave vanishing of all obstruction classes, but the appendix theorem does not say that, and it carries the extra CME hypothesis anyway. The same bad seam import recurs at chapters/theory/higher_genus_modular_koszul.tex:16970. FIX: in both places replace the appendix citation with `Proposition~\ref{prop:master-equation-from-mc}`; at 1172 explicitly write `\mathrm{Sh}_r(\cA)=0` for `r\ge3`, so the projected MC equation gives `\mathfrak o_\cA^{(r)}=0` for `r\ge3` (equivalently `o^{(r+1)}(\cA)=0` for `r\ge2`); at 16970 explicitly state that `o_5(\mathrm{Vir})\neq0` is the induction seed and `prop:master-equation-from-mc` supplies the recursion.

- [HIGH] chapters/theory/chiral_koszul_pairs.tex:3329 — PROBLEM: this cites `thm:nms-archetype-trichotomy` for a four-class `G/L/C/M` classification; the same scope error reappears at chapters/theory/chiral_koszul_pairs.tex:3450, chapters/theory/higher_genus_modular_koszul.tex:32054, chapters/theory/higher_genus_modular_koszul.tex:32294, and chapters/theory/higher_genus_complementarity.tex:6092. But appendices/nonlinear_modular_shadows.tex:1208 only proves a quartic-order trichotomy for the three primitive frame families Heisenberg / affine `\widehat{\mathfrak{sl}}_2` / `\beta\gamma`. FIX: replace those body citations with `Theorem~\ref{thm:shadow-archetype-classification}`; reserve `Theorem~\ref{thm:nms-archetype-trichotomy}` only for statements explicitly limited to those three primitive families through quartic order.

- [HIGH] chapters/theory/bar_cobar_adjunction_inversion.tex:3478 — PROBLEM: the “Conilpotent?” checklist item does not match the appendix theorem it cites. The body writes `\bigcap_n \text{coker}(\Delta^n)=0`, while appendices/koszul_reference.tex:268 defines conilpotency by eventual vanishing under iterates of the reduced coproduct: `\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar{\Delta}^{(n)})`. This is not the same criterion. FIX: replace the checkbox text with the appendix theorem’s actual condition, e.g. `Conilpotent? ($\ker(\epsilon)=\bigcup_{n\ge0}\ker(\bar{\Delta}^{(n)})$)`.

- [HIGH] metadata/theorem_registry.md:59 — PROBLEM: the live registry still indexes both `appendices/ordered_associative_chiral_kd.tex` and `chapters/theory/ordered_associative_chiral_kd.tex` as separate 89-claim surfaces, even though the main build only inputs the theory copy at main.tex:1140. The seam is therefore split between a live theory chapter and a shadow appendix duplicate with the same label namespace (for example `ch:ordered-associative-chiral-kd` at appendices/ordered_associative_chiral_kd.tex:37 and chapters/theory/ordered_associative_chiral_kd.tex:37). FIX: make `chapters/theory/ordered_associative_chiral_kd.tex` the sole live source by moving `appendices/ordered_associative_chiral_kd.tex` to `archive/` or otherwise excluding it from registry/label-index generation, then regenerate `metadata/theorem_registry.md` and `metadata/label_index.json`.

- [MEDIUM] chapters/theory/higher_genus_modular_koszul.tex:1 — PROBLEM: the canonical theory section carries an appendix-style label `app:koszul_higher_genus`, and appendices/koszul_reference.tex then cites that theory section as if it were an appendix at lines 5, 7, 11, 28, 89, 125, and 172. This blurs appendix/theory ownership right at the seam. FIX: delete `\label{app:koszul_higher_genus}` from line 1, keep `\label{sec:koszul-across-genera}`, and replace every `\ref{app:koszul_higher_genus}` in `appendices/koszul_reference.tex` with `\ref{sec:koszul-across-genera}`.

- [LOW] chapters/theory/introduction.tex:1954 — PROBLEM: appendix-owned labels are called “Chapter/Ch.” instead of “Appendix/App.” at chapters/theory/introduction.tex:1954, 2226, 2379 and chapters/theory/chiral_hochschild_koszul.tex:5733; chapters/theory/introduction.tex:2253 also writes a chapter-range ending in an appendix label; chapters/theory/higher_genus_foundations.tex:1103 calls the section label `sec:ainfty-historical` an “Appendix” rather than a section inside an appendix. FIX: change those nouns to match the target labels: use `Appendix~\ref{app:nonlinear-modular-shadows}` / `App.~\ref{app:nonlinear-modular-shadows}`, rewrite introduction.tex:2253 as `Ch.~\ref{chap:detailed-computations} and Appendix~\ref{app:combinatorial-frontier}`, and change higher_genus_foundations.tex:1103 to `\S\ref{sec:ainfty-historical}` or `the Historical origins section of Appendix~\ref{app:homotopy-transfer}`.

## Summary
Checked: 20 | Findings: 7 | Verdict: FAIL
tokens used
341,763
