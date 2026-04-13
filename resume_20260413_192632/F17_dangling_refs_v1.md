# F17_dangling_refs_v1 (1101s)



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
session id: 019d880f-5694-7ac2-a0da-f2aa2fbf4d6f
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


MISSION: FOUNDATION AUDIT of chapters/

Find all \ref{} that don't resolve. Run: grep -roh '\\ref{[^}]*}' chapters/ | sort -u > /tmp/refs.txt; grep -roh '\\label{[^}]*}' chapters/ | sort -u > /tmp/labels.txt; comm -23 /tmp/refs.txt /tmp/labels.txt. Every unresolved ref is a finding with fix.

Be MAXIMALLY harsh. Every missing definition, hidden import, unresolved reference, or
unjustified step is a finding. For each finding: PROBLEM + exact FIX.
mcp startup: no servers


thinking
**Evaluating search methods**

The developer suggests I should prioritize using explorers for codebase questions over manual searches or file reading. However, I can still utilize the shell when needed. I’m considering whether to spawn an explorer to find unresolved references, but since the user has given explicit commands, I might just run shell commands directly. The instruction emphasizes trusting explorer results, yet since the user wants actual file contents, shell might be the better choice for that.
thinking
**Creating an action plan**

I might need to create a plan if the task is substantial. It’s possible to use the update_plan tool for this, providing regular, even brief, updates as needed. I expect to finish quickly, with maybe one or two updates. I should also follow AGENTS for non-trivial tasks, running the Resonance Loop. Since the task involves auditing labels and refs, I should read the SKILL.md. I’m considering using deep-beilinson-audit, but I need to keep my approach minimal.
codex
Using `deep-beilinson-audit` because this is an adversarial audit of the manuscript surface. I’m starting with the exact unresolved-reference sweep the task specifies, then I’ll read the implicated files in context and verify each finding against live source before reporting fixes.
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
I’ve locked the scope to `chapters/` unresolved references. Next I’m loading the required audit constitution files and the raw `\\ref`/`\\label` surface so the findings are grounded before I inspect each hit in context.
Plan update
Adversarial audit of unresolved chapter references, with context reads and line-accurate fixes.
  → Load required audit context files and collect unresolved refs in chapters/
  • Open each implicated chapter location and verify whether the reference is truly unresolved in source
  • Report line-accurate findings with exact fixes and summary counts
exec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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

 succeeded in 52ms:
# Theorem Registry

Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.

This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.

## Concordance Cross-Check

- `thm:modular-koszul-duality-main` is cited in `chapters/connections/concordance.tex` as the flag theorem, but `chapters/theory/introduction.tex` currently provides only a `\phantomsection` label and no tagged claim block. It is therefore intentionally absent from the structured registry below.
- `thm:shifted-symplectic-complementarity` is the conditional C2 theorem cited by concordance. Its `\ClaimStatusConditional` block contributes to the status totals below, but it does not appear in the proved-only registry tables.

## Snapshot

| Metric | Value |
|---|---:|
| ProvedHere claims | 2367 |
| Total tagged claims | 3112 |
| Active files in `main.tex` | 90 |
| Total `.tex` files scanned | 104 |

 succeeded in 52ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3-TOPOLOGICAL with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3-TOPOLOGICAL output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3-TOPOLOGICAL(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3-TOPOLOGICAL(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3-topological).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3-TOPOLOGICAL. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

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

thinking
**Considering command execution**

I'm thinking about including only unresolved references with an exact fix. If there aren't any unresolved refs, it looks like I’ll need to compute something. I should run the specified grep commands precisely and then carefully inspect the output. I want to ensure that everything is functioning correctly before moving forward. Let's proceed with executing the command to get the results needed!
codex
The constitution files are loaded. I’m running the exact `\\ref` vs `\\label` sweep now, then I’ll open every surviving hit in context and check whether the surrounding sentence exposes a second-order failure beyond the raw missing label.
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sort -u > /tmp/refs.txt
grep -roh '\\\\label{["'^}]*}'"' chapters/ | sort -u > /tmp/labels.txt
comm -23 /tmp/refs.txt /tmp/labels.txt" in /Users/raeez/chiral-bar-cobar succeeded in 196ms:
\ref{D1}
\ref{D2}
\ref{D3}
\ref{D4}
\ref{D5}
\ref{D6}
\ref{D:genus-tower}
\ref{MK:koszul-htpy}
\ref{MK:koszul}
\ref{MK:modular-htpy}
\ref{MK:modular}
\ref{MK:verdier-htpy}
\ref{MK:verdier}
\ref{alg:NAP-koszul}
\ref{app:arnold-relations}
\ref{app:branch-line-reductions}
\ref{app:coderived-models}
\ref{app:coderived}
\ref{app:combinatorial-frontier}
\ref{app:curved-ainfty-formulas}

thinking
**Evaluating findings and methods**

I’m considering whether to report a finding about potential flaws in the mission command itself. The user requested findings for specific chapters, so maybe this could fit in as part of an audit meta. I think it might be more effective to summarize that the raw communication is unusable unless we strip certain references. To tackle unresolved references, I could use tools like shell commands or Perl for extraction and transformation, and count occurrences for better context analysis. Let's see how that goes!
codex
The raw `comm` output is a trap: it compares literal `\\ref{...}` strings against literal `\\label{...}` strings, so it reports almost everything. I’m normalizing both sides to label keys now; otherwise the audit would be garbage and violate the verification requirement.
exec
/bin/zsh -lc "grep -roh '\\\\ref{["'^}]*}'"' chapters/ | sed -E 's/"'^'"\\\\ref\\{(["'^}]*)'"\\}"'$/'"\\1/' | sort -u > /tmp/ref_keys.txt
grep -roh '\\\\label{["'^}]*}'"' chapters/ | sed -E 's/"'^'"\\\\label\\{(["'^}]*)'"\\}"'$/'"\\1/' | sort -u > /tmp/label_keys.txt
comm -23 /tmp/ref_keys.txt /tmp/label_keys.txt | tee /tmp/unresolved_ref_keys.txt
wc -l /tmp/unresolved_ref_keys.txt" in /Users/raeez/chiral-bar-cobar succeeded in 190ms:
app:arnold-relations
app:branch-line-reductions
app:coderived-models
app:combinatorial-frontier
app:curved-ainfty-formulas
app:homotopy-transfer
app:koszul-reference
app:nonlinear-modular-shadows
app:sign-conventions
app:signs
app:theta
app:w3-jacobi-full
ch:bv-brst
ch:feynman
ch:ht-boundary
ch:kontsevich-integral
ch:ym-boundary-theory
ch:ym-instanton-screening
chap:ordered-associative-chiral-kd
chap:shifted-rtt-orthogonal-coideals



thinking
**Locating unresolved keys**

I’ve identified 206 unresolved keys that require detailed attention. I need to locate all occurrences and ensure I can track them accurately, since there could be multiple instances of the same missing label. Each unresolved reference needs a corresponding fix, but I wonder if I should consider just unique keys or all occurrences. It might be manageable with a script to generate a mapping of findings, although I must determine if any keys resolve outside the main chapters.
thinking
**Evaluating reference resolution**

I need to clarify that the raw command is limited to checking labels within chapters, as the user specified to use `grep ... chapters/`. Should I stick to just chapters, or consider LaTeX resolution throughout the entire repository? The task is focused on chapters. If references in chapters point to appendix labels, they technically resolve in the build, leading to potential false positives. I need to verify this with the actual file contents and consider the overall project context to avoid misrepresenting the unresolved references.
thinking
**Running a global search**

The user is insisting on using a specific command, but I know I need actual unresolved references for verification. I should examine whether many of the 206 unresolved references are located in appendices or volumes, as labels like `app:*` will likely be there, and some `op:` might even be in the introduction. I’ll probably have to search each key globally, potentially using a tool across the entire repository to check for `\label{key}` and filter only the globally unresolved references.
codex
A second false-positive layer is showing up: many “missing” keys are appendix labels or non-chapter labels, so a `chapters/`-only label scan is still not the real resolution surface. I’m checking the unresolved set against all live `\\label{...}` definitions in the repo before I accuse the manuscript of anything.
exec
/bin/zsh -lc "rg -o '\\\\label\\{["'^}]*'"\\}' -g '*.tex' . | sed -E 's/.*\\\\label\\{(["'^}]*)'"\\}.*/\\1/' | sort -u > /tmp/all_label_keys.txt
comm -23 /tmp/ref_keys.txt /tmp/all_label_keys.txt | tee /tmp/truly_unresolved_ref_keys.txt
wc -l /tmp/truly_unresolved_ref_keys.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
ch:bv-brst
ch:feynman
chap:ordered-associative-chiral-kd
conj:toroidal-e1
conj:toroidal-koszul-dual
cor:thqg-I-heisenberg-selberg
cor:thqg-III-complementarity-exchange
cor:thqg-III-dimension-parity
def:conilpotent-chiral-coalgebra
lem:thqg-X-composition-decay
prop:heisenberg-kappa
prop:mixed-product-decomposition
prop:pixton-genus2-planted-forest
prop:thqg-V-c13-self-duality
prop:thqg-X-second-quantization
rem:free-field-three-theorems
rem:thqg-I-admissible
rem:thqg-X-pants-independence
rem:toroidal-three-theorems
rem:w-algebra-three-theorems


thinking
**Exploring unresolved keys**

I’m trying to tackle 47 unresolved keys. I need to find where each occurs and their context. It's likely that some might just be typos linked to existing labels. So, I want to inspect these occurrences and search for similar labels, maybe by using prefixes or simplified versions. I could automate this process by listing occurrences with their file and line context. I wonder if using a shell or Python script would work best for parsing these unresolved keys.
thinking
**Building a report effectively**

I’m considering building a report and wondering if Perl might be a good choice, but the shell should work just fine since I’m not editing anything. I could use a command like `while read k; do rg -n --fixed-strings "\\ref{$k}" chapters; done`. That seems okay for what I need. I’ll just ensure that the output is manageable before saving everything to a file. Let’s run this and see how it goes!
exec
/bin/zsh -lc "while IFS= read -r k; do rg -n --fixed-strings \"\\\\ref{"'$k}" chapters; done < /tmp/truly_unresolved_ref_keys.txt | tee /tmp/truly_unresolved_ref_occurrences.txt' in /Users/raeez/chiral-bar-cobar succeeded in 292ms:
chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
chapters/connections/editorial_constitution.tex:468:Remark~\ref{rem:thqg-I-admissible}). What remains conjectural in
chapters/examples/heisenberg_eisenstein.tex:2420:Remark~\ref{rem:thqg-X-pants-independence}.)
chapters/examples/yangians_foundations.tex:994:(Remark~\ref{rem:toroidal-three-theorems})
chapters/examples/landscape_census.tex:1467:Remark~\ref{rem:w-algebra-three-theorems} (W-algebras),
chapters/examples/landscape_census.tex:4016: (Remark~\ref{rem:w-algebra-three-theorems}).
chapters/examples/y_algebras.tex:857:(\S\ref{sec:concordance-holographic-programme}), the junction
chapters/examples/y_algebras.tex:641:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
chapters/examples/landscape_census.tex:4041: (\S\ref{sec:elliptic-bar-heisenberg}).
chapters/connections/editorial_constitution.tex:2896: (\S\ref{sec:elliptic-bar-heisenberg}).
chapters/examples/bar_complex_tables.tex:4155:Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
chapters/examples/bar_complex_tables.tex:4200:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
chapters/connections/entanglement_modular_koszul.tex:525:in~\S\ref{sec:thqg-soft-graviton-theorems}).
chapters/connections/thqg_entanglement_programme.tex:793:\S\ref{sec:thqg-ten-theorems} to the entanglement domain.
chapters/connections/outlook.tex:605:Section~\ref{subsec:dr-hierarchy-string}).
chapters/connections/thqg_entanglement_programme.tex:521:(\S\ref{subsec:thqg-III-shifted-symplectic}).
chapters/connections/thqg_open_closed_realization.tex:1241:\S\ref{subsec:thqg-open-sector-factorization-category}.
chapters/examples/free_fields.tex:5095: \textup{(}Theorem~\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}.
chapters/examples/free_fields.tex:5106:Theorem~\ref{thm:bar-cobar-path-integral-heisenberg} by
codex
I’ve reduced the surface to 47 globally missing keys, but that still includes dead refs inside comments and cross-volume placeholders. I’m reading each occurrence in context now; anything not on the live TeX path gets cut, and anything real gets a concrete repair instead of a vague accusation.
exec
/bin/zsh -lc 'while IFS=: read -r file line rest; do start=$((line>3?line-3:1)); end=$((line+3)); printf '"'=== %s:%s ===\\n' \""'$file" "$line"; sed -n "${start},${end}p" "$file"; printf '"'\\n'; done < /tmp/truly_unresolved_ref_occurrences.txt" in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
obstruction; the ratio
$c/\kappa$ is family-dependent (equal to~$2$ for Virasoro but not in general).
The Verdier involution $\sigma$
(Theorem~\ref{thm:thqg-g4-s-duality})
exchanges the two summands, enforcing~\eqref{eq:ent-complementarity-sum}.
\end{remark}


=== chapters/connections/thqg_entanglement_programme.tex:623 ===
Parts (i)--(ii) are the bar and cobar functors.
Part (iii) is Theorem~B.
Part (iv) is the definition of $\cA^!$ and
Theorem~\ref{thm:thqg-g5-yangian}.
\end{proof}

\begin{remark}[Structural analogy with holographic error correction]

=== chapters/connections/entanglement_modular_koszul.tex:524 ===
Proposition~\ref{prop:ent-complexity-classification}.
For part~(iii), the shadow connection



thinking
**Analyzing unresolved keys**

I need to look at each unresolved key, which might appear multiple times. Some could be in comments, so I'll exclude those. I believe there might be around 46 keys with actual occurrences. I should search for label names or similar to see if there are obvious fixes for existing labels. Perhaps I can use a tool to generate suggestions automatically by prefix or substring. While fuzzy matching with shell may work, I wonder if a small Python script could be beneficial instead.
thinking
**Considering label fixes**

I find Python easier to work with, especially since I'm not editing files. It seems appropriate for data analysis, so I think it’s acceptable. I need to get actual line numbers and implement fixes, which could involve several steps. For instance, I might add or rename a missing target label, replace incorrect chapter references, or add a `\label{...}` to an existing environment if it's unlabeled. If no target exists, the best fix might involve editing or refactoring sentences due to unresolved references. It could also be useful to search across volumes for context.
thinking
**Examining cross-volume rules**

The user didn't explicitly mention cross-volumes, but I think the AGENTS cross-volume rule suggests that when a task involves shared formulas or theorem labels, I should update all genuine duplicates. For auditing, it seems necessary to include all three volumes when handling shared elements like formulas, definitions, and chapter references. So, it makes sense that I might need to inspect the other volumes for these labels. Since I have filesystem access, I should consider reading sibling volumes too.
codex
Several of these are not typos at all; they look like cross-volume references that were written as if Vol II labels could resolve inside Vol I. I’m checking the sibling volumes now so I can distinguish “wrong label” from “wrong cross-document citation mechanism.”
exec
/bin/zsh -lc "while IFS= read -r k; do printf '=== %s ===\\n' \""'$k"; rg -n --fixed-strings "'"\\\\label{"'$k}" /Users/raeez/chiral-bar-cobar-vol2 /Users/raeez/calabi-yau-quantum-groups 2>/dev/null || true; done < /tmp/truly_unresolved_ref_keys.txt' in /Users/raeez/chiral-bar-cobar succeeded in 529ms:
=== lem:thqg-X-composition-decay ===
=== prop:heisenberg-kappa ===
=== prop:mixed-product-decomposition ===
/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/modular_swiss_cheese_operad.tex:1048:\label{prop:mixed-product-decomposition}
=== prop:pixton-genus2-planted-forest ===
=== prop:thqg-V-c13-self-duality ===
=== prop:thqg-X-second-quantization ===
=== rem:free-field-three-theorems ===
=== rem:thqg-I-admissible ===
=== rem:thqg-X-pants-independence ===
=== rem:toroidal-three-theorems ===
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:395:\label{rem:toroidal-three-theorems}
=== rem:w-algebra-three-theorems ===
=== sec:concordance-holographic-programme ===
=== sec:concordance-three-tier-r-matrix ===
=== sec:elliptic-bar-heisenberg ===
/Users/raeez/calabi-yau-quantum-groups/chapters/examples/toroidal_elliptic.tex:783:\label{sec:elliptic-bar-heisenberg}
=== sec:sl3-bar-table ===
=== sec:thqg-soft-graviton-theorems ===
=== sec:thqg-ten-theorems ===

thinking
**Exploring label existence**

I'm noticing that some cross-volume labels are missing, and this seems to be a global issue. I need to determine if this is due to the absence of labels or if similar names exist locally. Maybe I'll search for approximate matches. I could try using a command like `rg -n --glob '*.tex' 'title substring'` or the theorem_registry for labels. It may help to compute close matches using Python’s difflib to generate suggestions from the repo for each missing key. This approach could simplify my manual search. Let's do a quick Python run!
exec
/bin/zsh -lc "python3 - <<'PY'
import difflib
from pathlib import Path
labels=[]
for path in Path('.').rglob('*.tex'):
    text=path.read_text(errors='ignore')
    import re
    for m in re.finditer(r'\\\\label\\{(["'^}]*)'"\\}', text):
        labels.append(m.group(1))
missing=[line.strip() for line in Path('/tmp/truly_unresolved_ref_keys.txt').read_text().splitlines() if line.strip()]
for k in missing:
    matches=difflib.get_close_matches(k, labels, n=5, cutoff=0.5)
    print('===',k,'===')
    for m in matches:
        print(m)
PY" in /Users/raeez/chiral-bar-cobar
thinking
**Improving efficiency**

I think the session might be complete, but I didn't get an output due to some maximum limit. So, I want to rerun it more efficiently. I’m considering using `rg` to parse labels with a shell pipeline. There are many files, but I believe they’re still manageable. I’m planning to use `rg -o` to quickly retrieve labels, then process them in Python using a temporary file. That should help streamline the process!
exec
/bin/zsh -lc "rg -o '\\\\label\\{["'^}]*'"\\}' -g '*.tex' . | sed -E 's/.*\\\\label\\{(["'^}]*)'"\\}.*/\\1/' | sort -u > /tmp/all_labels_repo.txt
python3 - <<'PY'
import difflib
from pathlib import Path
labels=Path('/tmp/all_labels_repo.txt').read_text().splitlines()
missing=Path('/tmp/truly_unresolved_ref_keys.txt').read_text().splitlines()
for k in missing:
    matches=difflib.get_close_matches(k, labels, n=5, cutoff=0.55)
    print('===',k,'===')
    for m in matches:
        print(m)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 6.84s:
=== ch:bv-brst ===
ch:v1-bv-brst
conj:master-bv-brst
subsec:bv-bar
thm:kfc-bv-bar
rem:mc5-vs-bv-brst
=== ch:feynman ===
ch:v1-feynman
rem:ss-feynman
rem:feynman-htt
eq:feynman-rule
sec:feynman_genus_g
=== chap:ordered-associative-chiral-kd ===
ch:ordered-associative-chiral-kd
sec:ordered-associative-core
thm:ordered-associative-ds-principal
thm:ordered-associative-modular-mc
thm:ordered-master
=== conj:toroidal-e1 ===
sec:toroidal

thinking
**Exploring fix for conjecture**

I’m considering a fix for `conj:toroidal-e1`, which might involve adding a matching label to the corresponding local conjecture if the chapter exists. I wonder if my local repository has a chapter named `toroidal_elliptic.tex`. So, the next step is to search for that chapter. I need to ensure everything lines up properly for clarity and consistency. Let’s see what I find!
exec
/bin/zsh -lc 'rg -n "toroidal|elliptic" chapters/examples/toroidal_elliptic.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"label\\{chap:toroidal-elliptic\\}|label\\{ch:ordered-associative-chiral-kd\\}|label\\{chap:casimir-divisor\\}|label\\{thm:thqg-intro-heisenberg-sewing\\}|label\\{thm:thqg-intro-collision-twisting\\}|label\\{thm:thqg-annulus-trace\\}|label\\{subsec:thqg-intro-shifted-symplectic\\}|label\\{sec:thqg-intro\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: chapters/examples/toroidal_elliptic.tex: IO error for operation on chapters/examples/toroidal_elliptic.tex: No such file or directory (os error 2)
 succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:633:\label{thm:thqg-annulus-trace}
chapters/connections/thqg_introduction_supplement_body.tex:11:\label{sec:thqg-intro-bar-to-holographic}
chapters/connections/thqg_introduction_supplement_body.tex:260:\label{thm:thqg-intro-collision-twisting}
chapters/connections/thqg_introduction_supplement_body.tex:336:\label{sec:thqg-intro-shadow-connection}
chapters/connections/thqg_introduction_supplement_body.tex:674:\label{sec:thqg-intro-gravitational-complexity}
chapters/connections/thqg_introduction_supplement_body.tex:917:\label{sec:thqg-intro-duality-phase-space}
chapters/connections/thqg_introduction_supplement_body.tex:963:\label{subsec:thqg-intro-shifted-symplectic}
chapters/connections/thqg_introduction_supplement_body.tex:1124:\label{sec:thqg-intro-collision-yang-baxter}
chapters/connections/thqg_introduction_supplement_body.tex:1396:\label{sec:thqg-intro-perturbative-finiteness}
chapters/connections/thqg_introduction_supplement_body.tex:1471:\label{thm:thqg-intro-heisenberg-sewing}
chapters/connections/thqg_introduction_supplement_body.tex:1615:\label{sec:thqg-intro-guide}
chapters/theory/ordered_associative_chiral_kd.tex:37:\label{ch:ordered-associative-chiral-kd}
exec
/bin/zsh -lc "rg -n \"label\\{chap:toroidal-elliptic\\}|label\\{chap:casimir-divisor\\}|label\\{chap:ordered-associative-chiral-kd\\}|label\\{sec:sl3-bar-table\\}|label\\{rem:free-field-five-theorems\\}|label\\{rem:free-fields-three-pillar\\}|label\\{rem:w-algebra-bar-cobar\\}|label\\{rem:yangian-three-theorems\\}|label\\{rem:sl2-three-theorems\\}|label\\{rem:lattice-three-theorems\\}|label\\{def:three-tier-r-matrix\\}|label\\{subsec:concordance-holographic-completion\\}|label\\{subsec:concordance-three-bar-complexes\\}|label\\{chap:casimir-divisor\\}|label\\{v1-chap:casimir-divisor\\}\" chapters appendices -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:1941:\label{rem:lattice-three-theorems}
chapters/examples/free_fields.tex:94:\label{rem:free-fields-three-pillar}
chapters/examples/free_fields.tex:5446:\label{rem:free-field-five-theorems}
chapters/examples/yangians_foundations.tex:871:\label{rem:yangian-three-theorems}
chapters/examples/kac_moody.tex:3935:\label{rem:sl2-three-theorems}
chapters/connections/bv_brst.tex:1272:\label{rem:w-algebra-bar-cobar}%
chapters/connections/concordance.tex:3762:\label{subsec:concordance-three-bar-complexes}
chapters/connections/concordance.tex:6563:\label{subsec:concordance-holographic-completion}
chapters/theory/introduction.tex:1598:\label{def:three-tier-r-matrix}



thinking
**Searching for missing labels**

I need to conduct more searches for the missing labels related to actual candidates. I’m thinking about searching for theorem names or titles in the text. Since some unresolved labels are not found, it seems like different environments might exist with varying labels. I should ensure I find the exact fixes based on theorem titles and consider using references from current files. I also need to verify by checking the target lines and systematically work through the categories to produce accurate findings.
thinking
**Listing findings comprehensively**

The user wants a detailed listing of every finding, which adds up to around 48 occurrences! I need to ensure the counts are accurate and line-specific. I should exclude any instances of `thm:modular` inside comments, and check for others within the `\ifannalsedition\else` context. For `rem:toroidal-three-theorems`, if it’s inside that environment, it may or may not evaluate based on the build flag, so I have to treat it as live. Additionally, I need to identify any missing labels that might come from `\externaldocument` or the xr package.
thinking
**Checking cross-volume references**

I need to see if the book uses external documents for Volume II and III since that might help resolve any cross-volume references. I’ll check the repository to confirm this. It’s crucial to ensure that these references are accurate and well-documented. By searching through the repo, I can gather the necessary information to clarify any unresolved references between the volumes. This feels like a good step to take!
exec
/bin/zsh -lc "rg -n \"externaldocument|xr-hyper|xrsetup|externaldocument\" . -g '*.tex' -g '*.sty' -g '*.cls'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./tmp_standalone_audit/survey_v2_xr.tex:16:\usepackage{xr-hyper}
./tmp_standalone_audit/survey_v2_xr.tex:17:\externaldocument{../main}
codex
I’m past the raw search stage. The remaining work is mapping each bad key to the actual target: typo, renamed local label, or illegal cross-volume reference. That is where the audit either becomes useful or useless, so I’m reading the target theorem/section surfaces now instead of guessing.
exec
/bin/zsh -lc 'rg -n "thqg-g3|thqg-g4|thqg-g5|thqg-g6|thqg-III|thqg-intro|Page constraint|Lagrangian constraint|soft graviton|annulus trace|Verdier involution|eigenspace" chapters/connections/thqg_entanglement_programme.tex chapters/connections/entanglement_modular_koszul.tex chapters/connections/thqg_introduction_supplement_body.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"heisenberg-kappa|pixton-genus2|free-field-three|w-algebra-three|conilpotent chiral coalgebra|mixed-product-decomposition|composition-decay|second quantization|pants independence|heisenberg bar complex at genus|rtt-all-types|dk-fd-typeA|FM-convergence|bar-cobar-path-integral-heisenberg|hook-type-transport-koszul-duality\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:5481:\label{rem:pixton-genus2-verification}
chapters/examples/symmetric_orbifolds.tex:345:% Section: The DMVV formula and second quantization
chapters/examples/symmetric_orbifolds.tex:348:\section{The DMVV formula and second quantization}\label{sec:symn-dmvv}
chapters/examples/symmetric_orbifolds.tex:627:exponential implements second quantization. The modular
chapters/examples/lattice_foundations.tex:1722:(Proposition~\ref{prop:pixton-genus2-planted-forest})
chapters/examples/lattice_foundations.tex:4534:theorem \textup{(}Theorem~\textup{\ref{conj:dk-fd-typeA}} for
chapters/examples/lattice_foundations.tex:4558:Theorem~\ref{conj:dk-fd-typeA}.
chapters/examples/y_algebras.tex:340: \textup{(}Proposition~\textup{\ref{prop:heisenberg-kappa}}\textup{)}.
chapters/examples/heisenberg_eisenstein.tex:200: Pair-of-pants sewing is the second quantization of a
chapters/examples/heisenberg_eisenstein.tex:1086:\begin{equation}\label{eq:heisenberg-kappa-formula}
chapters/examples/heisenberg_eisenstein.tex:2071:vertex $v$ contributes the second quantization
chapters/examples/heisenberg_eisenstein.tex:2190:(Lemma~\ref{lem:thqg-X-composition-decay}). In particular,
chapters/examples/heisenberg_eisenstein.tex:2194:The full cocomposition is the second quantization
chapters/examples/heisenberg_eisenstein.tex:2220:the second quantization of a one-particle operator:
chapters/examples/heisenberg_eisenstein.tex:2303:on $A^2(D)$, and the second quantization functor $\secquant$ is
chapters/examples/free_fields.tex:2005:\bar{B}^{\mathrm{ch}}(\mathcal{H}_k) &\simeq \mathrm{coLie}^{\mathrm{ch}}(V^*) \quad \text{(conilpotent chiral coalgebra)} \\
chapters/examples/free_fields.tex:5099: \textup{(}Theorem~\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}.
chapters/examples/free_fields.tex:5110:Theorem~\ref{thm:bar-cobar-path-integral-heisenberg} by
chapters/examples/yangians_foundations.tex:1228:Theorem~\textup{\ref{thm:rtt-all-types}(iv)} likewise operates
chapters/examples/landscape_census.tex:793:type~$A$, Theorem~\ref{conj:dk-fd-typeA} gives only the corresponding
 succeeded in 52ms:
chapters/connections/entanglement_modular_koszul.tex:336:The Verdier involution $\sigma$
chapters/connections/entanglement_modular_koszul.tex:337:(Theorem~\ref{thm:thqg-g4-s-duality})
chapters/connections/entanglement_modular_koszul.tex:524:$(\nabla^{\mathrm{hol}})^2 = 0$ (proved as Theorem~\ref{thm:thqg-g6-soft-graviton}
chapters/connections/thqg_introduction_supplement_body.tex:11:\label{sec:thqg-intro-bar-to-holographic}
chapters/connections/thqg_introduction_supplement_body.tex:27:\label{subsec:thqg-intro-swiss-cheese}
chapters/connections/thqg_introduction_supplement_body.tex:43:\begin{equation}\label{eq:thqg-intro-swiss-cheese-decomposition}
chapters/connections/thqg_introduction_supplement_body.tex:52:\begin{equation}\label{eq:thqg-intro-swiss-cheese-squares}
chapters/connections/thqg_introduction_supplement_body.tex:60:\label{def:thqg-intro-swiss-cheese-structure}
chapters/connections/thqg_introduction_supplement_body.tex:63:pair $(d_C, d_R)$ satisfying~\eqref{eq:thqg-intro-swiss-cheese-squares}.
chapters/connections/thqg_introduction_supplement_body.tex:81:\label{subsec:thqg-intro-bbl-triangle}
chapters/connections/thqg_introduction_supplement_body.tex:101:\begin{equation}\label{eq:thqg-intro-bar-to-ambient}
chapters/connections/thqg_introduction_supplement_body.tex:131:\label{subsec:thqg-intro-triangle-edges}
chapters/connections/thqg_introduction_supplement_body.tex:140: map~\eqref{eq:thqg-intro-bar-to-ambient} projects the bar
chapters/connections/thqg_introduction_supplement_body.tex:165:\label{subsec:thqg-intro-holographic-from-mc}
chapters/connections/thqg_introduction_supplement_body.tex:185: \begin{equation}\label{eq:thqg-intro-r-matrix-extraction}
chapters/connections/thqg_introduction_supplement_body.tex:191: (\S\ref{subsec:thqg-intro-collision-definition}).
chapters/connections/thqg_introduction_supplement_body.tex:197: (\S\ref{sec:thqg-intro-shadow-connection}).
chapters/connections/thqg_introduction_supplement_body.tex:208:\label{subsec:thqg-intro-reconstruction}
chapters/connections/thqg_introduction_supplement_body.tex:251:\label{subsec:thqg-intro-four-recovery}
chapters/connections/thqg_introduction_supplement_body.tex:260:\label{thm:thqg-intro-collision-twisting}
exec
/bin/zsh -lc "rg -n --fixed-strings '\\ref{ch:bv-brst}' chapters && rg -n --fixed-strings '\\ref{ch:feynman}' chapters && rg -n --fixed-strings '\\ref{chap:ordered-associative-chiral-kd}' chapters" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "grep -Rnoh '\\\\ref{ch:bv-brst}' chapters/ || true
grep -Rnoh '\\\\ref{ch:feynman}' chapters/ || true
grep -Rnoh '\\\\ref{chap:ordered-associative-chiral-kd}' chapters/ || true" in /Users/raeez/chiral-bar-cobar succeeded in 274ms:
1256:\ref{ch:feynman}
1520:\ref{ch:feynman}
1493:\ref{chap:ordered-associative-chiral-kd}

thinking
**Troubleshooting command failure**

I'm figuring out why the `rg` command failed—it might be due to some special characters, right? I'm also considering that it could be related to files with CRLF line endings. I think I should try using `grep` with context options to troubleshoot further. That might help narrow down the issue. I want to make sure I get this right to avoid future problems! Let's see how this goes.
exec
/bin/zsh -lc "grep -RnoH -C 2 '\\\\ref{ch:bv-brst}' chapters/ | sed -n '1,120p'
grep -RnoH -C 2 '\\\\ref{ch:feynman}' chapters/ | sed -n '1,120p'
grep -RnoH -C 2 '\\\\ref{chap:ordered-associative-chiral-kd}' chapters/ | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 357ms:
chapters/theory/introduction.tex.bak-1051-\textup{(}Theorem~\ref{thm:brst-bar-genus0}\textup{)}.  The identification
chapters/theory/introduction.tex.bak-1052-of the ghost system with the cobar of the matter bar complex
chapters/theory/introduction.tex.bak:1053:\ref{ch:bv-brst}
chapters/theory/introduction.tex.bak-1054-the bosonic string critical dimension follows from Koszul duality at
chapters/theory/introduction.tex.bak-1055-the scalar level without this bridge.
--
chapters/theory/introduction.tex.bak-1254-(Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
chapters/theory/introduction.tex.bak-1255-The physics column is made precise in
chapters/theory/introduction.tex.bak:1256:\ref{ch:bv-brst}
chapters/theory/introduction.tex.bak-1257-\end{remark}
chapters/theory/introduction.tex.bak-1258-
--
chapters/theory/introduction.tex.bak-1520-Feynman diagrams (Ch.~\ref{ch:feynman}) &
chapters/theory/introduction.tex.bak-1521-  Perturbative incarnation: Feynman graphs on $\overline{C}_n(X)$; higher operations from nested collapses \\
chapters/theory/introduction.tex.bak:1522:\ref{ch:bv-brst}
chapters/theory/introduction.tex.bak-1523-  Genus-$0$ bar/BRST quasi-iso; BV/bar dictionary; QME/MC comparison \\
chapters/theory/introduction.tex.bak-1524-Open/closed realization (\S\ref{sec:thqg-open-closed-realization}) &
chapters/theory/introduction.tex.bak-1254-(Chapters~\ref{chap:kac-moody-koszul}--\ref{chap:yangians}).
chapters/theory/introduction.tex.bak-1255-The physics column is made precise in
chapters/theory/introduction.tex.bak:1256:\ref{ch:feynman}

thinking
**Filtering backup files**

I'm dealing with .bak files in the scan results. The global labels scan included all .tex files but ended up excluding the .bak ones since I used `rg -g '*.tex'`. However, the reference scan with `grep -roh` over the chapters mistakenly included .tex.bak files because it didn't have a specific pattern, leading to many false positives. It's essential to focus only on the live .tex files. I'll need to redo the filter and confirm results without including backups. Great catch!
codex
A third false-positive layer just collapsed: the user’s `grep -roh` walks backup artifacts like `introduction.tex.bak`, so some “missing refs” are not in the manuscript at all. I’m restricting the audit to live `*.tex` sources now.
exec
/bin/zsh -lc "rg -o '\\\\ref\\{["'^}]*'"\\}' chapters -g '*.tex' | sed -E 's/.*\\\\ref\\{(["'^}]*)'"\\}.*/\\1/' | sort -u > /tmp/ref_keys_live.txt
rg -o '\\\\label\\{["'^}]*'"\\}' -g '*.tex' . | sed -E 's/.*\\\\label\\{(["'^}]*)'"\\}.*/\\1/' | sort -u > /tmp/label_keys_all_live.txt
comm -23 /tmp/ref_keys_live.txt /tmp/label_keys_all_live.txt | tee /tmp/truly_unresolved_ref_keys_live.txt
wc -l /tmp/truly_unresolved_ref_keys_live.txt
while IFS= read -r k; do rg -n --fixed-strings \"\\\\ref{"'$k}" chapters -g '"'*.tex'; done < /tmp/truly_unresolved_ref_keys_live.txt | tee /tmp/truly_unresolved_ref_occurrences_live.txt" in /Users/raeez/chiral-bar-cobar succeeded in 319ms:
chapters/connections/thqg_entanglement_programme.tex:203:Part (iii): Corollary~\ref{cor:thqg-III-dimension-parity}.
chapters/connections/thqg_entanglement_programme.tex:738:Part (iii): Corollary~\ref{cor:thqg-III-dimension-parity}.
chapters/theory/bar_construction.tex:1523:every section; see Definition~\ref{def:conilpotent-chiral-coalgebra})
chapters/examples/heisenberg_eisenstein.tex:2190:(Lemma~\ref{lem:thqg-X-composition-decay}). In particular,
chapters/examples/y_algebras.tex:340: \textup{(}Proposition~\textup{\ref{prop:heisenberg-kappa}}\textup{)}.
chapters/connections/thqg_open_closed_realization.tex:507:(Volume~II, Proposition~\ref{prop:mixed-product-decomposition} in the
chapters/examples/lattice_foundations.tex:1722:(Proposition~\ref{prop:pixton-genus2-planted-forest})
chapters/connections/thqg_entanglement_programme.tex:758:(Proposition~\ref{prop:thqg-V-c13-self-duality}).
chapters/examples/heisenberg_eisenstein.tex:2197:Proposition~\ref{prop:thqg-X-second-quantization}, $\secquant(T)$ is
chapters/examples/heisenberg_eisenstein.tex:2412:determinant (Proposition~\ref{prop:thqg-X-second-quantization}).
chapters/examples/landscape_census.tex:1465:(Kac--Moody), Remark~\ref{rem:free-field-three-theorems} (free fields),
chapters/examples/landscape_census.tex:3978: (Remark~\ref{rem:free-field-three-theorems}).
chapters/connections/editorial_constitution.tex:468:Remark~\ref{rem:thqg-I-admissible}). What remains conjectural in
chapters/examples/heisenberg_eisenstein.tex:2420:Remark~\ref{rem:thqg-X-pants-independence}.)
chapters/examples/yangians_foundations.tex:994:(Remark~\ref{rem:toroidal-three-theorems})
chapters/examples/landscape_census.tex:1467:Remark~\ref{rem:w-algebra-three-theorems} (W-algebras),
chapters/examples/landscape_census.tex:4016: (Remark~\ref{rem:w-algebra-three-theorems}).
chapters/examples/y_algebras.tex:857:(\S\ref{sec:concordance-holographic-programme}), the junction
chapters/examples/y_algebras.tex:641:(\S\ref{sec:concordance-three-tier-r-matrix}): it is
chapters/examples/landscape_census.tex:4041: (\S\ref{sec:elliptic-bar-heisenberg}).
exec
/bin/zsh -lc 'wc -l /tmp/truly_unresolved_ref_occurrences_live.txt' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
      53 /tmp/truly_unresolved_ref_occurrences_live.txt
exec
/bin/zsh -lc "rg -n \"toroidal|elliptic\" chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/deformation_quantization.tex:461:For $X = E$ (elliptic curve): The deformation quantization on $E$ exists but the level $\kappa$ depends on the choice of propagator (Green's function on $E$). The Euler characteristic $\chi(E) = 0$ constrains the anomaly but does not force $\kappa = 0$; rather, the star product on $E$ is governed by the elliptic propagator $\partial_z G(z,w)$.
chapters/examples/deformation_quantization.tex:546:\subsubsection{Genus 1: elliptic corrections}
chapters/examples/deformation_quantization.tex:548:On an elliptic curve $E_\tau$, the genus-1 propagator is:
chapters/examples/deformation_quantization.tex:1156:(Proposition~\ref{prop:km-bar-curvature}) measures the failure of the star product to extend to $E_\tau$. At critical level $k = -h^\vee$, $m_0 = 0$ and the extension is unobstructed. At generic level, the genus-1 correction involves $E_2(\tau)$ (Theorem~\ref{thm:elliptic-vs-rational}).
chapters/examples/w_algebras_deep.tex:5409:\label{rem:n2-elliptic-genus}
chapters/examples/w_algebras_deep.tex:5410:\index{elliptic genus!K3}
chapters/examples/w_algebras_deep.tex:5413:the elliptic genus is $Z_{\mathrm{ell}}(\tau, z) = 2\phi_{0,1}(\tau, z)$,
chapters/examples/w_algebras_deep.tex:5425:construction at $k = -4 + \varepsilon$, packages the elliptic genus
chapters/examples/symmetric_orbifolds.tex:354:for a surface~$X$ with elliptic genus
chapters/examples/symmetric_orbifolds.tex:382:product whose exponent is the elliptic genus of~$X$.
chapters/examples/symmetric_orbifolds.tex:608:seed elliptic genus:
chapters/examples/lattice_foundations.tex:1887:elliptic genus decomposition. The shadow obstruction tower of
chapters/examples/lattice_foundations.tex:3577:\multicolumn{5}{l}{\textit{Elliptic/toroidal
chapters/examples/lattice_foundations.tex:3578: \textup{(}Chapter~\ref{chap:toroidal-elliptic}\textup{)}}} \\
chapters/examples/lattice_foundations.tex:4691:On an elliptic curve $E_\tau = \bC/(\bZ + \tau\bZ)$, the genus-$0$
chapters/examples/lattice_foundations.tex:5087:the elliptic modular parameter $\tau = iK'/K$ (where $K$, $K'$
chapters/examples/lattice_foundations.tex:5088:are complete elliptic integrals). The genus-$1$ shadow
chapters/examples/beta_gamma.tex:1049:$\beta\gamma$ system on the elliptic curve
chapters/examples/beta_gamma.tex:1056:elliptic propagator. For the $\beta\gamma$ system with conformal
chapters/examples/beta_gamma.tex:1066:\label{def:elliptic-betagamma-propagator}

thinking
**Figuring out reference issues**

I see there's no local toroidal file, so I’m thinking about replacing cross-volume references with `Chapter\ref{chap:toroidal-elliptic}`. But wait, the local label `chap:toroidal-elliptic` already exists from the lattice_foundations reference! I should search for that label to clarify things. There’s definitely a bit of a tangle here, but it seems I’m on the right path to resolve it.
exec
/bin/zsh -lc "rg -n 'label\\{chap:toroidal-elliptic\\}' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
./main.tex:1690: \phantomsection\label{chap:toroidal-elliptic}% % toroidal_elliptic.tex (moved to Vol III)
exec
/bin/zsh -lc "sed -n '246,290p' chapters/theory/cobar_construction.tex
printf '\\n---\\n'
sed -n '1428,1460p' chapters/theory/higher_genus_foundations.tex
printf '\\n---\\n'
sed -n '248,280p' chapters/theory/bar_cobar_adjunction_curved.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 equation~\eqref{eq:borcherds-axiom}) holds for the
 iterated comultiplication on codimension-$2$ strata.
\end{enumerate}
This is the Verdier dual of a chiral algebra: if $\cA$
is a chiral algebra, then $\cC = \barB(\cA)$ (the bar
coalgebra) is a factorization coalgebra, and conversely
the cobar $\Omega(\cC)$ recovers a chiral algebra
structure.
\end{definition}

\begin{definition}[Intrinsic geometric cobar complex]\label{def:geom-cobar-intrinsic}
\index{cobar construction!geometric|textbf}
Let $\mathcal{C}$ be a conilpotent chiral coalgebra on a smooth algebraic
curve $X$, valued in holonomic $\mathcal{D}$-modules, with comultiplication
$\Delta\colon \mathcal{C} \to \mathcal{C} \boxtimes \mathcal{C}$ and
coaugmentation $\eta\colon \omega_X \to \mathcal{C}$. Write
$\mathcal{C}^\vee := \mathbb{D}_X(\mathcal{C})$ for the $\mathcal{D}$-module
Verdier dual on $X$, which is a chiral algebra with multiplication dual to
$\Delta$.


thinking
**Clarifying definitions**

I notice that there's no specific labeled definition. The earlier definition refers to "Intrinsic geometric cobar complex," but then there's a reference in line 1523 about "conilpotent chiral coalgebra." To resolve this, I should add a label to the actual definition of conilpotent chiral coalgebra. I need to figure out where that definition is located, so I’ll search for "begin{definition}[Conilpotent chiral coalgebra.”
exec
/bin/zsh -lc "rg -n \"begin\\{definition\\}\\[.*conilpotent chiral coalgebra|Conilpotent chiral coalgebra|conilpotent dg coalgebras\" chapters/theory chapters/connections -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/bar_construction.tex:1521:on conilpotent dg coalgebras over $\operatorname{Ran}(X)$
chapters/theory/bar_construction.tex:2264:\begin{definition}[Conilpotent chiral coalgebra]
chapters/theory/ordered_associative_chiral_kd.tex:263:Hence there is a filtered quasi-isomorphism of conilpotent dg coalgebras
chapters/theory/ordered_associative_chiral_kd.tex:800:coaugmented conilpotent dg coalgebras
chapters/theory/ordered_associative_chiral_kd.tex:912:Then there is a canonical quasi-isomorphism of conilpotent dg coalgebras
chapters/theory/ordered_associative_chiral_kd.tex:1604:There is a quasi-isomorphism of conilpotent dg coalgebras
exec
/bin/zsh -lc "sed -n '2258,2285p' chapters/theory/bar_construction.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
up to unique natural isomorphism.

It defines a functor from chiral algebras to filtered conilpotent chiral coalgebras, with essential image the coalgebras having logarithmic coderivations supported on collision divisors.
\end{theorem}

 
\begin{definition}[Conilpotent chiral coalgebra]
A chiral coalgebra $C$ is \emph{filtered conilpotent} if the iterated comultiplication 
$\Delta^{(n)} : C \to C^{\otimes(n+1)}$ satisfies: For each $c \in C$, there exists 
$N$ such that $\Delta^{(n)}(c) = 0$ for all $n \geq N$. This ensures the cobar 
construction $\Omega^{\text{ch}}(C)$ is well-defined without completion.
\end{definition}



\begin{proof}
\emph{Step 1: Existence.} We verify each axiom explicitly:
\begin{itemize}
\item \emph{Locality:} For $j: U \hookrightarrow X$ open,
we have $C_n(U) = j^{-1}(C_n(X))$.
exec
/bin/zsh -lc "sed -n '1678,1700p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 \phantomsection\label{thm:growth-mode-factorization}% % casimir_divisor_core_transport.tex (migrated to Vol II)
 \phantomsection\label{chap:dg-shifted-factorization}% % dg_shifted_factorization_bridge.tex (removed; in Vol II)
 \phantomsection\label{thm:derived-additive-kz}% % dg_shifted_factorization_bridge.tex (removed; in Vol II)
 \phantomsection\label{rem:transport-not-invariance}% % dg_shifted_factorization_bridge.tex (removed; in Vol II)
 \phantomsection\label{prop:kz-from-bar}% % kontsevich_integral.tex (migrated to Vol II)
 \phantomsection\label{ch:ym-boundary-theory}% % ym_boundary_theory.tex (migrated to Vol II)
 \phantomsection\label{ch:ym-higher-body-couplings}% % ym_higher_body_couplings.tex (migrated to Vol II)
 \phantomsection\label{ch:ym-instanton-screening}% % ym_instanton_screening.tex (migrated to Vol II)
 \phantomsection\label{app:typeA-baxter-rees-theta}% % typeA_baxter_rees_theta.tex (migrated to Vol II)
 \phantomsection\label{chap:shifted-rtt-orthogonal-coideals}% % shifted_rtt_duality_orthogonal_coideals.tex (migrated to Vol II)
 \phantomsection\label{thm:novikov-completion-theorem}% % ym_instanton_screening.tex (migrated to Vol II)
 \phantomsection\label{chap:detailed-computations}% % bar_complex_tables.tex
 \phantomsection\label{chap:toroidal-elliptic}% % toroidal_elliptic.tex (moved to Vol III)
 %% Phantom labels for toroidal_elliptic.tex content (now in Vol III):
 \phantomsection\label{subsec:cy-research-programmes}%
 \phantomsection\label{thm:shadow-siegel-gap}%
 \phantomsection\label{prop:shadow-k3e}%
 \phantomsection\label{prop:kappa-bps-decomposition}%
 \phantomsection\label{prop:shadow-gf-convergence}%
 \phantomsection\label{op:programme-a-cy-gluing}%
exec
/bin/zsh -lc "sed -n '1700,1735p' main.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \phantomsection\label{conj:universal-moonshine-multiplier}%
 \phantomsection\label{op:programme-c-second-quantization}%
 \phantomsection\label{conj:kappa-bps-universality}%
 \phantomsection\label{op:programme-d-schottky}%
 \phantomsection\label{conj:shadow-taut-projection}%
 \phantomsection\label{op:programme-e-mock-modularity}%
 \phantomsection\label{conj:mock-shadow-tower}%
 \phantomsection\label{op:programme-f-factorization-envelope}%
 \phantomsection\label{conj:modular-fact-envelope}%
 \phantomsection\label{op:programme-g-bkm-scattering}%
 \phantomsection\label{conj:scattering-tropical-shadow}%
 \phantomsection\label{op:programme-h-descent}%
 \phantomsection\label{op:programme-i-higher-dim}%
 \phantomsection\label{conj:cy-product-shadow}%
 \phantomsection\label{op:programme-j-convergence}%
 % --- Concordance section labels ---
 \phantomsection\label{sec:concordance-non-principal-w}%
 \phantomsection\label{sec:concordance-e1-modular-theory}%
 \phantomsection\label{sec:concordance-structural-upgrades}%
 \phantomsection\label{sec:concordance-analytic-sewing}%


thinking
**Evaluating labeling issues**

The fix for the missing cross-volume theorem labels seems to be adding phantom labels to `main.tex` in the moved-content stub block instead of rewriting each reference. The current book has already done this for several moved labels. I need to inspect the numbering context since these phantom labels may share the same chapter counter rather than the theorem counter. There could be mechanisms at play, like `\newlabel`, but if they used phantom labels just as anchors, that might lead to incorrect references.
thinking
**Analyzing mathematical integrity**

I’m questioning whether the current approach is mathematically sound. For our audit, we need to ensure an exact fix. If the project's pattern involves phantom stub labels for moved surfaces, I should recommend that for the missing ones too. I need to check if the existing phantom labels correspond to missing references, like `ch:ym-boundary-theory`. It looks like they do, but using a `\ref` to phantom labels in a theorem context will probably yield incorrect numbering, which is concerning.
exec
/bin/zsh -lc "sed -n '150,230p' chapters/connections/thqg_entanglement_programme.tex
printf '\\n---\\n'
sed -n '690,770p' chapters/connections/thqg_entanglement_programme.tex
printf '\\n---\\n'
sed -n '920,1015p' chapters/connections/thqg_introduction_supplement_body.tex
printf '\\n---\\n'
sed -n '1458,1498p' chapters/connections/thqg_introduction_supplement_body.tex
printf '\\n---\\n'
sed -n '630,660p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\subsection{Dimensional constraints from the Lagrangian structure}
\label{subsec:thqg-entanglement-dimensional}
\index{entanglement!dimensional constraints|textbf}

\begin{definition}[Lagrangian capacity]
\label{def:thqg-lagrangian-capacity}
\index{Lagrangian capacity|textbf}
For a gravitational input $(\cA, X, \langle \cdot, \cdot \rangle, k)$
and genus $g \ge 1$, the \emph{Lagrangian capacity} is
\begin{equation}\label{eq:thqg-lagrangian-capacity}
C_g(\cA)
\;:=\;
\dim Q_g(\cA).
\end{equation}
This is the dimension of the $\cA$-eigenspace in the
Lagrangian decomposition
$\cH_g(\cA) = Q_g(\cA) \oplus Q_g(\cA^!)$
(Theorem~\ref{thm:thqg-III-eigenspace-decomposition}).
\end{definition}
exec
/bin/zsh -lc "rg -n \"dimension parity|self-dual halving|halving|complementarity exchange|Page transition|c13-self|second quantization|composition decay|pants independence|Heisenberg sewing|determinant formula|Selberg\" chapters/connections chapters/examples -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/editorial_constitution.tex:183:Theorem~\ref{thm:heisenberg-sewing}: Heisenberg sewing via
chapters/connections/editorial_constitution.tex:464:and Theorem~\ref{thm:heisenberg-sewing} (Heisenberg sewing via
chapters/connections/editorial_constitution.tex:908:at all genera) and the Heisenberg sewing theorem
chapters/examples/symmetric_orbifolds.tex:345:% Section: The DMVV formula and second quantization
chapters/examples/symmetric_orbifolds.tex:348:\section{The DMVV formula and second quantization}\label{sec:symn-dmvv}
chapters/examples/symmetric_orbifolds.tex:627:exponential implements second quantization. The modular
chapters/connections/genus_complete.tex:1740:\item The Heisenberg sewing theorem
chapters/connections/genus_complete.tex:2236:Eisenstein/Rankin--Selberg interface and universal up to the
chapters/connections/genus_complete.tex:2449:The Rankin--Selberg unfolding argument of
chapters/connections/genus_complete.tex:2721:\textup{(}Sewing--Selberg recovery.\textup{)}
chapters/connections/genus_complete.tex:2724:Sewing--Selberg formula
chapters/connections/genus_complete.tex:2738:holomorphic points of the Rankin--Selberg integral
chapters/connections/genus_complete.tex:2759:Rankin--Selberg unfolding replaces the modular integral by
chapters/connections/genus_complete.tex:2790:(Rankin--Selberg) and the prime-side variable~$u$
chapters/connections/genus_complete.tex:2793:The Sewing--Selberg formula
chapters/connections/genus_complete.tex:2802:$s = (1{+}\rho)/2$ when $u = 0$ (the Sewing--Selberg
chapters/connections/genus_complete.tex:2814:The Sewing--Selberg formula and the Higgs field of
chapters/connections/genus_complete.tex:2818:Rankin--Selberg $L$-function $L_\cA(s,u)$ encodes the spectral data
chapters/connections/thqg_introduction_supplement_body.tex:1460:\subsection{The Heisenberg sewing theorem}
chapters/connections/thqg_introduction_supplement_body.tex:1463:\index{Fredholm determinant!Heisenberg sewing}

thinking
**Inspecting theorems**

It looks like the search results are pointing toward an existing theorem named `thm:self-dual-halving`. I want to dive in and understand its context and implications. There’s probably a lot to unpack here, like how this theorem relates to the overall topic I'm exploring. It could tie into broader concepts, and I might need to check out related resources to clarify its meaning. Let’s see where this takes me!
exec
/bin/zsh -lc "rg -n \"label\\{thm:self-dual-halving\\}|label\\{cor:.*dimension.*parity\\}|label\\{cor:.*complementarity.*exchange\\}|label\\{prop:c13-full-self-duality\\}|label\\{thm:heisenberg-sewing\\}|label\\{prop:heisenberg-r-matrix\\}|label\\{eq:heisenberg-kappa-formula\\}\" chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:188:\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
chapters/examples/heisenberg_eisenstein.tex:248:\label{prop:heisenberg-r-matrix}
chapters/examples/heisenberg_eisenstein.tex:1086:\begin{equation}\label{eq:heisenberg-kappa-formula}
chapters/theory/higher_genus_modular_koszul.tex:27801:\label{prop:c13-full-self-duality}
chapters/theory/higher_genus_complementarity.tex:2466:\begin{theorem}[Self-dual halving; \ClaimStatusProvedHere]\label{thm:self-dual-halving}
exec
/bin/zsh -lc "sed -n '2440,2495p' chapters/theory/higher_genus_complementarity.tex
printf '\\n---\\n'
sed -n '27780,27825p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = Q_g(\mathcal{A}) \oplus Q_g(\mathcal{A}^!)
\end{equation}

If $Q_g(\mathcal{A}) = 0$, then $Q_g(\mathcal{A}^!) \cong H^*(\overline{\mathcal{M}}_g, 
Z(\mathcal{A}))$.

\emph{Second statement}: If both vanish, then by exhaustion:
\begin{equation}
0 = \dim Q_g(\mathcal{A}) + \dim Q_g(\mathcal{A}^!) = \dim H^*(\overline{\mathcal{M}}_g, 
Z(\mathcal{A}))
\end{equation}

Thus $H^*(\overline{\mathcal{M}}_g, Z(\mathcal{A})) = 0$.
\end{proof}

\begin{remark}[Examples of vanishing]
At genus~$0$: $Q_0(\cA)=\mathbb{C}$, $Q_0(\cA^!)=0$ (tree-level,
no obstruction).
For TFTs: $Q_g(\cA)=0$ for all~$g$.
For $bc$--$\beta\gamma$: opposite obstructions cancel in the
exec
/bin/zsh -lc "sed -n '5428,5465p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '1260,1288p' chapters/connections/bv_brst.tex
printf '\\n---\\n'
sed -n '3928,3958p' chapters/examples/kac_moody.tex
printf '\\n---\\n'
sed -n '860,885p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:w-classical-integrability}. Passing from the
classical Poisson algebra to the quantum $\mathcal{W}$-algebra
introduces the higher multilinear operations supplied by the
bar-side $A_\infty$ structure; these higher terms are exactly the
non-binary correction data measured by the Li/PBW filtration.
\end{proof}



\section{Comparison and filtered structures}\label{sec:comparison-filtered}

This final section collects comparison results: the holographic Witten-diagram shadow, the interaction between filtrations and bar complexes, and a summary of the main theorems verified by free-field examples.

\subsection{Comparison of free-field examples}

Geometric complexity correlates inversely with algebraic simplicity: the free fermion (one generator) vanishes above degree~$1$; the $\beta\gamma$ system grows as $2 \cdot 3^{n-1}$; the Heisenberg gains a central charge class; the Virasoro connects to $\overline{\mathcal{M}}_{0,n}$; W-algebras link to flag varieties.

\begin{remark}[Five projections of $\Theta_\cA$: free-field archetypes]
\label{rem:free-field-five-theorems}
\index{main theorems!free field verification}
exec
/bin/zsh -lc 'rg -n "w-algebra.*theorems|main theorems!W|five projections|five theorems|bar-cobar" chapters/examples/w_algebras.tex chapters/examples/w_algebras_deep.tex chapters/connections/bv_brst.tex -g '"'*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:79:bar-cobar formalisms are related by the following dictionary:
chapters/connections/bv_brst.tex:265:$B(\cA)$ by bar-cobar inversion, Theorem~\ref{thm:bar-cobar-isomorphism-main}).
chapters/connections/bv_brst.tex:271:\label{rem:qme-bar-cobar}
chapters/connections/bv_brst.tex:313:(Theorem~\ref{thm:bar-cobar-isomorphism-main}),
chapters/connections/bv_brst.tex:1235: (MC4 closed; Vol~I Theorem~\ref{thm:completed-bar-cobar-strong}).
chapters/connections/bv_brst.tex:1270:\label{rem:bar-cobar-ht-boundary}%
chapters/connections/bv_brst.tex:1271:% conj:holographic-bar-cobar defined in genus_complete.tex
chapters/connections/bv_brst.tex:1272:\label{rem:w-algebra-bar-cobar}%
chapters/connections/bv_brst.tex:1338:should be solved by the bar-cobar pairing. This is a heuristic
chapters/connections/bv_brst.tex:1342:\begin{remark}[BV quantization and bar-cobar duality; \ClaimStatusHeuristic]
chapters/connections/bv_brst.tex:1343:\label{rem:bv-equals-bar-cobar}%
chapters/connections/bv_brst.tex:1345:equivalent to computing the bar-cobar homology:
chapters/connections/bv_brst.tex:1352:bar-cobar quasi-isomorphism
chapters/connections/bv_brst.tex:1353:\textup{(}Theorem~\ref{thm:bar-cobar-isomorphism-main}\textup{)}
chapters/connections/bv_brst.tex:1375:\textup{(}Theorem~\textup{\ref{thm:verdier-bar-cobar}}\textup{)}.
chapters/connections/bv_brst.tex:2049:operadic bar-cobar datum, but they live in different colours. What is
chapters/connections/bv_brst.tex:2065:setting through the homotopy-Koszulity package, and the general bar-cobar
chapters/connections/bv_brst.tex:2217:and Theorem~\ref{thm:completed-bar-cobar-strong} already provide the
chapters/examples/w_algebras_deep.tex:12:secondary Borcherds operation nonzero). The bar-cobar adjunction
chapters/examples/w_algebras_deep.tex:24:nilpotent currents) reduces, through the bar-cobar engine, to
exec
/bin/zsh -lc "sed -n '2692,2840p' chapters/examples/w_algebras.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
duality at every degree. The entire Koszul pair
$(\mathcal{W}^k(\mathfrak{g}),
\mathcal{W}^{k^\vee}({}^L\mathfrak{g}))$ is
a shadow-level realization of gauge-theoretic S-duality.
\end{remark}


\section{The five theorems for $\mathcal{W}$-algebras}
\label{sec:w-five-theorems}

The five main theorems of Part~\ref{part:bar-complex} specialize to $\mathcal{W}$-algebras
through DS reduction from the affine Kac--Moody package. We record
the specializations for the Virasoro algebra ($\mathcal{W}_2$) and
$\mathcal{W}_3$ in a verification table, then state the general
$\mathcal{W}_N$ pattern.

\begin{remark}[Five-theorem verification: Virasoro]
\label{rem:vir-five-theorems}
\index{main theorems!Virasoro verification}
\index{Virasoro algebra!five-theorem verification}
exec
/bin/zsh -lc "sed -n '1070,1096p' chapters/examples/heisenberg_eisenstein.tex
printf '\\n---\\n'
sed -n '2148,2185p' chapters/theory/higher_genus_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
is the first Chern class of the Hodge bundle,
represented by the $B$-cycle monodromy class $(-2\pi i)$.

\emph{Step~4: Trace over generators.}
The genus-1 curvature of the \emph{full} rank-$d$
algebra is obtained by summing over the diagonal
self-contraction of each generator:
\begin{align}
m_0^{(ij)} &= \kappa\delta^{ij}\cdot\omega_1,
\label{eq:rank-d-curvature}
\\
m_0 &= \sum_{i=1}^d m_0^{(ii)}
= d\kappa\cdot\omega_1.
\end{align}
The obstruction coefficient is the scalar
prefactor:
\begin{equation}\label{eq:heisenberg-kappa-formula}
\boxed{\;\kappa(\mathcal{H}_\kappa^{\oplus d})
= d\kappa.\;}
\end{equation}

thinking
**Refining mathematical references**

I think the best fix in y_algebras is changing to either `\eqref{eq:heisenberg-kappa-formula}` or `Convention\ref{conv:heisenberg-kappa-notation}`. The sentence currently refers to "contributes kappa = k by the Heisenberg formula," and since it's an exact formula, I should consider adjusting it to `equation\eqref{eq:heisenberg-kappa-formula}`. Since it currently uses the Proposition label, it would be better to replace `Proposition\ref{prop:heisenberg-kappa}` with the precise reference.
exec
/bin/zsh -lc "rg -n \"planted forest|planted-forest|delta_{\\\\mathrm\\{pf\\}}|Pixton\" chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:planted forest|planted-forest|delta_{\mathrm\{pf\}}|Pixton)
                                            ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n \"planted forest|planted-forest|Pixton|delta_\\{\\\\mathrm\\{pf\\}\" chapters -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:planted forest|planted-forest|Pixton|delta_\{\mathrm\{pf\})
                                                    ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n \"planted\" chapters -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:54:(Theorem~\ref{thm:planted-forest-tropicalization}) organizes the
chapters/examples/w_algebras_deep.tex:55:boundary contributions by planted-forest type, and the screening
chapters/examples/lattice_foundations.tex:1696:\item The planted-forest correction vanishes:
chapters/examples/lattice_foundations.tex:1722:(Proposition~\ref{prop:pixton-genus2-planted-forest})
chapters/examples/lattice_foundations.tex:5133:$S_3, S_4, \ldots$ through the planted-forest formula.
chapters/examples/beta_gamma.tex:186:level kills iterated cubic-loop interactions; the planted-forest
chapters/examples/beta_gamma.tex:2208:nonzero: the quartic contact stratum of the planted-forest boundary
chapters/examples/beta_gamma.tex:2241:corolla $K_{0,2}$ through the planted-forest boundary of $\overline{M}_{2,n}$,
chapters/examples/y_algebras.tex:829: The log FM compactification contributes no planted-forest
chapters/examples/heisenberg_eisenstein.tex:1885:residues $R_\rho$ arise from planted-forest strata of the
chapters/examples/free_fields.tex:118:(Theorem~\ref{thm:planted-forest-tropicalization}) reduces to the
chapters/examples/free_fields.tex:121:so the planted-forest coefficient algebra
chapters/examples/kac_moody.tex:219:separating/non-separating clutching), but NOT the planted-forest
chapters/examples/kac_moody.tex:223:implies no quartic contact contribution, and the planted-forest
chapters/examples/kac_moody.tex:4728:residues vanish because the planted-forest boundary strata require
chapters/connections/master_concordance.tex:426:\texttt{theorem\_genus2\_planted\_forest\_gz26\_engine}
chapters/examples/yangians_drinfeld_kohno.tex:6294:extended to all degrees by the planted-forest expansion.
chapters/examples/yangians_drinfeld_kohno.tex:6336:the planted-forest expansion of all-degree, all-genera
chapters/examples/genus_expansions.tex:58:(Theorem~\ref{thm:planted-forest-tropicalization}) extends these
chapters/examples/genus_expansions.tex:60:$\overline{\mathcal{M}}_g$, and the planted-forest tropicalization
exec
/bin/zsh -lc "sed -n '1688,1730p' chapters/examples/lattice_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\textup{(}UNIFORM-WEIGHT\textup{}) for all $g \geq 1$,
identical for all twenty-four lattices. In particular,
\begin{equation}\label{eq:niemeier-genus-amplitudes}
F_1 = 1,\qquad
F_2 = \tfrac{7}{240},\qquad
F_3 = \tfrac{31}{40320},\qquad
F_4 = \tfrac{127}{6451200}.
\end{equation}
\item The planted-forest correction vanishes:
$\delta_{\mathrm{pf}}^{(g,0)}(V_\Lambda) = 0$ for all $g \geq 2$,
since $S_3 = 0$.
\item The complementarity pairing for the lattice VOA family is
the free-field / $\mathrm{Ext}\leftrightarrow\mathrm{Sym}$ pattern
$\kappa_{\mathrm{latt}}(V_\Lambda) + \kappa_{\mathrm{latt}}(V_\Lambda^!) = 0_{\text{(lattice,\\,type\,i)}}$
\textup{(}not the Virasoro value~$13$;
	Theorem~\textup{\ref{thm:complementarity-root-datum}}\textup{)}.
\end{enumerate}
\end{theorem}

\begin{proof}
exec
/bin/zsh -lc "rg -n \"S_3\\(10 S_3 - \\\\kappa\\)/48|delta_\\{\\\\mathrm\\{pf\\}\\}\\"'^'"\\{\\(2,0\\)\\}|10 S_3 - \\\\kappa|planted-forest correction vanishes\" chapters/theory chapters/connections chapters/examples -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 2 in 52ms:
rg: regex parse error:
    (?:S_3\(10 S_3 - \kappa\)/48|delta_\{\mathrm\{pf\}\}\^\{\(2,0\)\}|10 S_3 - \kappa|planted-forest correction vanishes)
                     ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'S_3(10 S_3 - \\kappa)/48' chapters -g '*.tex'
rg -n -F '\\delta_{\\mathrm{pf}}"'^{(2,0)}'"' chapters -g '*.tex' | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/lattice_foundations.tex:1721:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:20450:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$:
chapters/theory/higher_genus_modular_koszul.tex:28365: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:32291:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/connections/concordance.tex:2143: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$;
chapters/examples/lattice_foundations.tex:1721:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$
chapters/examples/genus_expansions.tex:2933:\delta_{\mathrm{pf}}^{(2,0)}(\mathcal{W}_3)
chapters/examples/genus_expansions.tex:2958:$\delta_{\mathrm{pf}}^{(2,0)} = (40{-}c)/48$ is a
chapters/examples/genus_expansions.tex:2969:$\delta_{\mathrm{pf}}^{(2,0)} = (40 - c)/48$ is the first explicit
chapters/connections/concordance.tex:2143: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10 S_3 - \kappa)/48$;
chapters/connections/concordance.tex:2144: for Virasoro $\delta_{\mathrm{pf}}^{(2,0)} = -(c-40)/48$.
chapters/connections/concordance.tex:4287:$\delta_{\mathrm{pf}}^{(2,0)}$ receives contributions from
chapters/connections/concordance.tex:4296:\delta_{\mathrm{pf}}^{(2,0)}
chapters/connections/concordance.tex:4369:\delta_{\mathrm{pf}}^{(2,0)}(\cW_3)
chapters/connections/frontier_modular_holography_platonic.tex:5255: $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48
chapters/theory/higher_genus_modular_koszul.tex:3472:the three planted-forest graphs contribute~$\delta_{\mathrm{pf}}^{(2,0)}
chapters/theory/higher_genus_modular_koszul.tex:3533:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$
chapters/theory/higher_genus_modular_koszul.tex:3540:$\delta_{\mathrm{pf}}^{(2,0)}$), and the shadow visibility genus
chapters/theory/higher_genus_modular_koszul.tex:18360:$\delta_{\mathrm{pf}}^{(2,0)}
chapters/theory/higher_genus_modular_koszul.tex:18416:$\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$,

thinking
**Investigating theorems**

I think there must be a theorem or remark related to `rem:planted-forest-correction-explicit` or `thm:planted-forest-structure` that offers an explicit formula. This should be more precise than a proposition that's not defined. Since something referred to as lattice_foundations utilizes a proposition and an explicit formula, I could potentially cite `Theorem\ref{thm:planted-forest-structure}(ii)` or `Remark\ref{rem:planted-forest-correction-explicit}`. I’ll need to closely inspect the lines around theorem 25774 for clarity.
exec
/bin/zsh -lc "sed -n '25790,25820p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
sed -n '25323,25345p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 \textup{(}Corollary~\textup{\ref{cor:shadow-visibility-genus}}\textup{)}.}
 The shadow coefficient~$S_r$ ($r \geq 3$) first contributes to
 the integrated planted-forest at genus~$\lfloor r/2 \rfloor + 1$.
 At the class level, the cyclic marking breaks the parity
 obstruction: $S_4$ is visible in the descendant pairing
 $\int \delta_{\mathrm{pf}}\,\psi_1^2 = S_3\kappa/48 + S_4/8$
 at genus~$2$
 \textup{(}Remark~\textup{\ref{rem:class-vs-integrated-visibility}}\textup{)}.
\item \emph{Genus-$2$ planted-forest
 \textup{(}eq.~\textup{\eqref{eq:delta-pf-genus2-explicit}}\textup{)}.}
 On the rank-$1$ primary line:
 $\delta_{\mathrm{pf}}^{(2,0)} = S_3(10S_3 - \kappa)/48$
 \textup{(exact: all vertex weights are genus-$0$ shadow coefficients)}.
\item \emph{Rank-$1$ Pixton triviality.}
 For $\dim V = 1$ and $S_3 \neq 0$:
 the Givental $R$-matrix is $R = 1$
 \textup{(}Givental--Teleman for rank-$1$ semisimple\textup{)},
 the shadow CohFT equals the Witten--Kontsevich CohFT, and the
 MC-descended relations automatically lie in the Pixton ideal.
 For $S_3 = 0$ \textup{(}Heisenberg\textup{)}:

thinking
**Verifying theorem references**

I think I need to fix the reference to Theorem\ref{thm:planted-forest-structure}(ii) since it states the exact formula. I'll check if line 1722 mentions "proposition" and consider changing that to "theorem." Also, I need to look into equation\eqref{eq:delta-pf-genus2-explicit}. I should verify if the label exists and confirm that it's correct, shown as eq:delta-pf-genus2-explicit. I'll need to search for the exact info to be sure.
exec
/bin/zsh -lc "rg -n 'label\\{eq:delta-pf-genus2-explicit\\}' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
25381: \begin{equation}\label{eq:delta-pf-genus2-explicit}
exec
/bin/zsh -lc "rg -n \"composition decay|second quantization|pants independence|Selberg|determinant formula|admissible levels|admissible level|Heisenberg sewing theorem|one-particle Bergman|rankin|sewing theorem|partition function\" chapters/examples/heisenberg_eisenstein.tex chapters/connections/bv_brst.tex chapters/connections/arithmetic_shadows.tex -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/bv_brst.tex:322:\begin{remark}[Genus-$1$ partition function]\label{rem:genus1-bv}
chapters/connections/bv_brst.tex:1414:\index{Heisenberg!BV partition function}
chapters/connections/bv_brst.tex:1458:The BV partition function of $\kappa$ free bosons on a compact
chapters/connections/bv_brst.tex:1524:\noindent\textbf{Path \textup{(b)}: Selberg zeta function.}
chapters/connections/bv_brst.tex:1525:\index{Selberg zeta function!BV/bar proof|(}
chapters/connections/bv_brst.tex:1526:The D'Hoker--Phong determinant formula~\cite{DP86} expresses
chapters/connections/bv_brst.tex:1536:is the Selberg zeta function, the product running
chapters/connections/bv_brst.tex:1540:The Heisenberg partition function factorizes as
chapters/connections/bv_brst.tex:1560:\index{Selberg zeta function!BV/bar proof|)}
chapters/connections/bv_brst.tex:1629:\emph{scalar} \textup{(}partition function\slash free energy\textup{)}
chapters/connections/bv_brst.tex:1688: whose partition function is determined by a zeta-regularized
chapters/examples/heisenberg_eisenstein.tex:187:\begin{theorem}[Heisenberg sewing theorem;
chapters/examples/heisenberg_eisenstein.tex:189:\index{Heisenberg!sewing theorem}%
chapters/examples/heisenberg_eisenstein.tex:200: Pair-of-pants sewing is the second quantization of a
chapters/examples/heisenberg_eisenstein.tex:201: one-particle Bergman restriction/composition operator.
chapters/examples/heisenberg_eisenstein.tex:204: one-particle Bergman space.
chapters/examples/heisenberg_eisenstein.tex:220:$\det(1 - K)$ on the one-particle Bergman space, where~$K$ is the
chapters/examples/heisenberg_eisenstein.tex:494:The genus-1 partition function is:
chapters/examples/heisenberg_eisenstein.tex:506:The coefficients are the partition function $p(n)$ counting partitions of $n$.
chapters/examples/heisenberg_eisenstein.tex:651:The genus-2 partition function is:

thinking
**Inspecting the theorem**

I need to inspect the theorem regarding the Heisenberg-Eisenstein lines, specifically looking at lines 187 and 2178 to 2420. I'm wondering if there might be any unlabeled lemmas, propositions, or remarks within that section. It seems wise to focus particularly on the content starting around line 2178. Let’s see what I can uncover in those lines and make sure to clarify everything necessary!
exec
/bin/zsh -lc "sed -n '2176,2430p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\begin{proof}
The proof exploits the one-particle Bergman reduction
(Theorem~\ref{thm:heisenberg-one-particle-sewing}): every statement
about the Fock-space cooperad reduces to an operator-algebraic
statement on the one-particle Bergman space $A^2(D)$, where the
arguments are elementary.

\medskip\noindent
\textit{Proof of~\textup{(I)}: well-definedness and equivariance.}
Fix a stable bordered graph $\Gamma$ of type $(g,n)$ with internal
edges $E(\Gamma)$. Each internal edge $e$ contributes a sewing
operator $\sewop_{q_e}$ with exponentially decaying matrix
coefficients $|(\sewop_{q_e})_{n,m}| \leq C\,q_e^{(n+m)/2}$
(Lemma~\ref{lem:thqg-X-composition-decay}). In particular,
$\sewop_{q_e}$ is trace class on $A^2(D)$ with
$\|\sewop_{q_e}\|_1 = q_e/(1-q_e)$.

The full cocomposition is the second quantization
$\secquant(\cdot)^\kappa$ applied to a product of trace-class

thinking
**Investigating missing labels**

I'm noticing that the proof mentions missing local labels, so I think I should find the actual theorem, lemma, or remark either in the same file or elsewhere. The one-particle sewing theorem could potentially replace several labels. I need to search for labels related to one-particle reduction, particularly `thm:heisenberg-one-particle-sewing`. I should inspect the text around line 187, specifically between lines 187-230, to gather more context.
exec
/bin/zsh -lc "sed -n '180,236p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
of the affine Heisenberg vertex algebra. This suggests that the
sewing envelope (\S\ref{sec:analytic-completion}) of the algebraic
Heisenberg VOA is exactly $\operatorname{Sym} A^2(D)$, making
the Heisenberg the first model in which the entire analytic
completion programme is explicit.
\end{remark}

\begin{theorem}[Heisenberg sewing theorem;
\ClaimStatusProvedHere]\label{thm:heisenberg-sewing}%
\index{Heisenberg!sewing theorem}%
Under the mode--Bergman correspondence~$\Theta$
\textup{(}Remark~\textup{\ref{rem:heisenberg-mode-bergman}}\textup{)}:
\begin{enumerate}[label=\textup{(\roman*)}]
\item \textup{(\ClaimStatusProvedElsewhere, Moriwaki~\cite{Moriwaki26b})}
 The sewing envelope of the algebraic Heisenberg VOA is exactly
 $\operatorname{Sym} A^2(D)$.
\item \textup{(\ClaimStatusProvedHere)}
 The completed bar differential is the closure of the Gaussian
 collision operator on Bergman tensors.
\item \textup{(\ClaimStatusProvedHere)}
exec
/bin/zsh -lc "rg -n 'label\\{thm:heisenberg-one-particle-sewing\\}|label\\{prop:hs-trace-class\\}|label\\{eq:thqg-X-polyakov\\}|label\\{thm:analytic-algebraic-comparison\\}' chapters/examples/heisenberg_eisenstein.tex chapters/connections -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/genus_complete.tex:1371:\ClaimStatusProvedHere]\label{prop:hs-trace-class}%
chapters/connections/genus_complete.tex:1475:\label{thm:heisenberg-one-particle-sewing}%
exec
/bin/zsh -lc "sed -n '1468,1525p' chapters/connections/genus_complete.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
d^{-1} \geq 0$ for all $N \geq 1$: each summand is
a positive rational number. This is the input to
Theorem~\ref{thm:gram-positivity}.
\end{proof}

\begin{theorem}[Heisenberg: one-particle sewing;
\ClaimStatusProvedHere]%
\label{thm:heisenberg-one-particle-sewing}%
\index{Heisenberg!sewing|textbf}%
\index{Fredholm determinant!Heisenberg}%
\index{Bergman space!sewing operator}%
The Heisenberg pair-of-pants amplitude is the second
quantisation $\Gamma(R)$ of the one-particle Bergman
restriction $R \colon A^2(D_{\mathrm{out}}) \to
A^2(D_{\mathrm{in},1}) \otimes A^2(D_{\mathrm{in},2})$,
with $|R_{n,m}| \leq Cq^{(n+m)/2}$.
The sewing operator $T_q$ on the reduced Bergman space
$A^2_0(\partial D)$ (constant mode removed) has
eigenvalues~$q^n$ ($n \geq 1$) and is trace class:
$\|T_q\|_1 = q/(1-q)$.
exec
/bin/zsh -lc "rg -n \"secquant\\(|second quanti|trace class on \\\\operatorname\\{Sym\\}|Gamma\\(R\\)|symmetric Fock|Fock space\" chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
rg: regex parse error:
    (?:secquant\(|second quanti|trace class on \operatorname\{Sym\}|Gamma\(R\)|symmetric Fock|Fock space)
                                               ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'secquant(' chapters -g '*.tex'
rg -n -F 'second quantization' chapters -g '*.tex' | sed -n '1,220p'
rg -n -F 'trace class on \\operatorname{Sym}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:
chapters/examples/heisenberg_eisenstein.tex:2072:$\secquant(R_v)$ of its vertex restriction operator.
chapters/examples/heisenberg_eisenstein.tex:2195:$\secquant(\cdot)^\kappa$ applied to a product of trace-class
chapters/examples/heisenberg_eisenstein.tex:2197:Proposition~\ref{prop:thqg-X-second-quantization}, $\secquant(T)$ is
chapters/examples/heisenberg_eisenstein.tex:2221:$A_P = \secquant(R)$ for a pair-of-pants amplitude. The Fredholm
chapters/examples/heisenberg_eisenstein.tex:2228:\secquant(T_1 \circ T_2)\bigr)
chapters/examples/heisenberg_eisenstein.tex:2324:$\operatorname{Tr}_{\mathrm{Sym}}(\secquant(\sewop_q)^\kappa)
chapters/examples/heisenberg_eisenstein.tex:2494: sewing is $\secquant(R)$, and every closed amplitude is
chapters/examples/symmetric_orbifolds.tex:345:% Section: The DMVV formula and second quantization
chapters/examples/symmetric_orbifolds.tex:348:\section{The DMVV formula and second quantization}\label{sec:symn-dmvv}
chapters/examples/symmetric_orbifolds.tex:627:exponential implements second quantization. The modular
chapters/examples/heisenberg_eisenstein.tex:200: Pair-of-pants sewing is the second quantization of a
chapters/examples/heisenberg_eisenstein.tex:2071:vertex $v$ contributes the second quantization
chapters/examples/heisenberg_eisenstein.tex:2194:The full cocomposition is the second quantization
chapters/examples/heisenberg_eisenstein.tex:2220:the second quantization of a one-particle operator:
chapters/examples/heisenberg_eisenstein.tex:2303:on $A^2(D)$, and the second quantization functor $\secquant$ is
chapters/connections/concordance.tex:10909: second quantization (single-copy vs DMVV symmetric product),
exec
/bin/zsh -lc "sed -n '2298,2338p' chapters/examples/heisenberg_eisenstein.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\operatorname{Tr}_{\mathrm{Sym}}\!\bigl(
\delta_{\Gamma_1 \circ_e \Gamma_2}(\cdot)\bigr),
\]
because both sides reduce to the same one-particle operator
$\prod_{e \in E(\Gamma_1 \circ_e \Gamma_2)} \sewop_{q_e}$
on $A^2(D)$, and the second quantization functor $\secquant$ is
a monoidal functor (it preserves composition).

\medskip\noindent
\textit{Proof of~\textup{(III)}: self-sewing = trace.}
The non-separating degeneration $\Gamma_{\mathrm{ns}}$ is the graph
with one vertex of genus $g-1$ and one self-loop. The cocomposition
$\delta_{\Gamma_{\mathrm{ns}}}$ identifies the two half-edges of the
self-loop and traces over the corresponding Fock space:
\[
\delta_{\Gamma_{\mathrm{ns}}}(Z)
\;=\;
\sum_{\mu}
\langle\mu|\, Z\, |\mu\rangle
\;=\;
exec
/bin/zsh -lc "rg -n \"pants decomposition|pants decompositions|independence|all decompositions give the same Fredholm|same Fredholm\" chapters/examples/heisenberg_eisenstein.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
2399:\sum_{\text{pants decompositions}}
2417:Laplacian determinant. (The summation over pants decompositions
2418:is redundant: all decompositions give the same Fredholm
2420:Remark~\ref{rem:thqg-X-pants-independence}.)

thinking
**Verifying citations**

I need to check that the same line references `\eqref{eq:thqg-X-polyakov}` which wasn't included in the direct `\ref{}` sweep. It's important to verify this to ensure completeness. I want to make sure I've covered all the necessary references accurately. Let’s make it a point to include this in our validation process to maintain thoroughness in my work! I hope this doesn't get overlooked.
exec
/bin/zsh -lc "rg -n 'label\\{eq:thqg-X-polyakov\\}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:


thinking
**Checking labels in TeX**

I want to compare the normalized `\eqref{}` labels with all the labels in my live .tex document. This process might involve looking through a lot of entries, but I think it should be manageable. I'll run a quick count to see how many labels I actually have, which will help determine what needs to be included in my findings. It's interesting to see what I uncover!
codex
The `thqg-X` cluster just exposed a deeper defect: one of the broken theorem refs sits next to a broken `\\eqref` as well. I’m running a quick `\\eqref` normalization pass so I don’t miss the same class of failure under a different macro name.
exec
/bin/zsh -lc "rg -o '\\\\eqref\\{["'^}]*'"\\}' chapters -g '*.tex' | sed -E 's/.*\\\\eqref\\{(["'^}]*)'"\\}.*/\\1/' | sort -u > /tmp/eqref_keys_live.txt
comm -23 /tmp/eqref_keys_live.txt /tmp/label_keys_all_live.txt | tee /tmp/truly_unresolved_eqref_keys_live.txt
wc -l /tmp/truly_unresolved_eqref_keys_live.txt
while IFS= read -r k; do rg -n --fixed-strings \"\\\\eqref{"'$k}" chapters -g '"'*.tex'; done < /tmp/truly_unresolved_eqref_keys_live.txt | tee /tmp/truly_unresolved_eqref_occurrences_live.txt" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
comp:sl2-kappa
eq:molien-weyl-g
eq:riordan-recurrence-explicit
eq:thqg-X-polyakov
       4 /tmp/truly_unresolved_eqref_keys_live.txt
chapters/theory/higher_genus_modular_koszul.tex:34026:(equation~\eqref{comp:sl2-kappa}), the same value as at
chapters/examples/landscape_census.tex:2564:series~\eqref{eq:molien-weyl-g}, which has $r$~independent
chapters/examples/landscape_census.tex:2520:The recurrence~\eqref{eq:riordan-recurrence-explicit} is
chapters/examples/heisenberg_eisenstein.tex:2414:(\eqref{eq:thqg-X-polyakov}, Theorem~\ref{thm:thqg-X-heisenberg-sewing-full}(IV)),
exec
/bin/zsh -lc "sed -n '1200,1245p' chapters/examples/yangians_foundations.tex
printf '\\n---\\n'
sed -n '1138,1172p' chapters/examples/yangians_computations.tex
printf '\\n---\\n'
rg -n 'label\\{thm:rtt-all-classical-types\\}|All classical types|RTT.*all' chapters/examples/yangians_drinfeld_kohno.tex chapters/examples/yangians_computations.tex chapters/examples/yangians_foundations.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
representation-dependent data is the evaluation
$\rho_V \otimes \rho_V(\Omega)$ on $V \otimes V$.
The CYBE holds universally by the infinitesimal braid relations,
which depend only on the Lie algebra structure of~$\fg$, not on
the specific representation.
\end{remark}

\begin{remark}[MC3, the DK bridge, and the ordered bar]
\label{rem:mc3-ordered-bar-bridge}
\index{MC3!ordered bar interpretation}
\index{Drinfeld--Kohno!ordered bar provenance}
\index{ordered bar complex!MC3 and DK bridge}
The MC3 programme is natively an ordered-bar phenomenon. The
$R$-matrix $r(z) = k\Omega/z$ of
equation~\eqref{eq:r-matrix-all-types} lives in bar bidegree
$(g,n) = (0,2)$ of $\barB^{\Eone}(\hat{\fg}_k)$: it is the
genus-$0$, degree-$2$ component of the ordered MC element
$\Theta_\cA^{\Eone}$ of
\S\textup{\ref{subsec:e1-as-primitive}}. The Drinfeld--Kohno
theorem, which identifies geometric braid-group monodromy on
exec
/bin/zsh -lc "rg -n \"hook-type|subregular|transport corridor|transport-koszul|type-A transport|hook transport\" chapters -g '*.tex' | sed -n '1,240p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:229:part of the proved core; the $\mathfrak{sl}_3$ minimal/subregular
chapters/examples/w_algebras_deep.tex:230:computations and the hook-type family results provide the first
chapters/examples/w_algebras_deep.tex:237:paired DS seed transport beyond the present hook/subregular theorematic
chapters/examples/w_algebras_deep.tex:1522:hook-type nilpotents in type~$A$ but not for all orbits in
chapters/examples/w_algebras_deep.tex:2573:\item subregular/minimal $f = f_{\min}$ in
chapters/examples/w_algebras_deep.tex:2575:\item hook-type $f = f_{(n-r,1^r)}$ in
chapters/examples/w_algebras_deep.tex:2954:\textup{(}principal, $\mathfrak{sl}_3$ subregular/minimal,
chapters/examples/w_algebras_deep.tex:2955:hook-type in type~$A$;
chapters/examples/w_algebras_deep.tex:3103:$(3,1)$ & $12$ & $T, W^{(3)}, J$ & $3$ & subregular \\
chapters/examples/w_algebras_deep.tex:3124:subregular $(3,1)$ at $-k-8$, and the rectangular $(2^2)$ is
chapters/examples/landscape_census.tex:154: \textup{(}subregular DS reduction\textup{)}}} \\
chapters/examples/bershadsky_polyakov.tex:72:Partition & $(2,1)$ (self-transpose, hook-type) \\
chapters/examples/bershadsky_polyakov.tex:188:the hook-type transport theorem (Fehily \cite{FehilyHook},
chapters/examples/bershadsky_polyakov.tex:484:\section{The hook-type corridor}\label{sec:bp-hook}
chapters/examples/bershadsky_polyakov.tex:486:The Bershadsky--Polyakov algebra is the seed of the hook-type
chapters/examples/bershadsky_polyakov.tex:487:transport corridor. A hook partition
chapters/examples/bershadsky_polyakov.tex:495:\index{hook-type corridor}
chapters/examples/w_algebras.tex:486:and the hook-type family in type~$A$ is the first structured
chapters/examples/w_algebras.tex:487:transport corridor, presently kept conditional
chapters/examples/w_algebras.tex:523:Nilpotent orbits are partially ordered by closure: $e = 0$ gives $\mathcal{W}^k(\fg, 0) = \widehat{\fg}_k$; $e = e_{\mathrm{prin}}$ gives $\mathcal{W}_N$ (generators of spins $d_i + 1$). For $\fg = \mathfrak{sl}_3$: $\widehat{\mathfrak{sl}}_{3,k} \supset \mathcal{W}^k(\mathfrak{sl}_3, f_{\min}) \supset \mathcal{W}_3$ (Computation~\ref{comp:sl3-ds-hierarchy}). The principal row is proved; the minimal/subregular and hook-type rows provide the leading non-principal audit corridor, with explicit local computations and a proved transport mechanism, but their full duality transport remains conditional or conjectural (Theorem~\ref{thm:hook-transport-corridor}, Conjecture~\ref{conj:bp-duality}, Conjecture~\ref{conj:type-a-transport-to-transpose}).
exec
/bin/zsh -lc "sed -n '224,240p' chapters/connections/subregular_hook_frontier.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The \emph{transport-closure} of a set $S$ of vertices is the set
of all vertices reachable from $S$ by paths in $\Gamma_N$.
\end{definition}

\begin{theorem}[Hook-type transport corridor under DS--bar compatibility; \ClaimStatusConditional]
\label{thm:hook-transport-corridor}
\index{W-algebra@$\mathcal{W}$-algebra!hook transport corridor}
Assume that, at generic level, bar--cobar/Koszul duality intertwines
with the reduction and inverse-reduction functors along the hook
network in type~$A$. Then for every hook partition
$\eta = (N-r, 1^r)$ in $\mathfrak{sl}_N$:
\[
\mathcal{W}^k(\mathfrak{sl}_N, f_\eta)^!
\;\simeq\;
\mathcal{W}^{-k-2N}(\mathfrak{sl}_N, f_{\eta^t}).
\]
\end{theorem}

thinking
**Clarifying theorem labels**

I need to fix a label from `thm:hook-type-transport-koszul-duality` to `thm:hook-transport-corridor`. I think the severity is medium since it’s a wrong label, but the theorem is still conditional. I noticed that the outlook text mentions "proved corridor," which aligns with the theorem conditional. I need to inspect the context, possibly looking at line 276 in the outlook document where it states, "Hook-type in type A is the proved corridor (Theorem...)". This needs further examination!
exec
/bin/zsh -lc "sed -n '268,282p' chapters/connections/outlook.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Corollary~\ref{cor:mc3-all-types}). The remaining open frontiers:
non-principal W-algebra duality, analytic completion, and the full MC5
chain-level BV/BRST/bar identification.

Active growth directions:
\begin{enumerate}[label=\textup{(\arabic*)}]
\item \emph{Non-principal W-algebra duality.} Hook-type in type~$A$
 is the proved corridor
 (Theorem~\ref{thm:hook-type-transport-koszul-duality}).
 Full arbitrary-nilpotent BV duality is conjectural.
\item \emph{Factorization-envelope technology.} The modular factorization adjunction
 $U_X^{\mathrm{mod}} \dashv \operatorname{Prim}^{\mathrm{mod}}$
 (Theorem~\ref{thm:platonic-adjunction}) and DS as package functor.
\item \emph{Analytic sewing.} The sewing envelope $\cA^{\mathrm{sew}}$,
 HS-sewing proved for the entire standard landscape of universal
exec
/bin/zsh -lc "sed -n '38,95p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
(Definition~\ref{def:thqg-holographic-datum}) encodes six algebraic
structures. Each has a precise counterpart in the holographic
entanglement programme:

\begin{center}
\renewcommand{\arraystretch}{1.4}
\small
\begin{tabular}{l@{\;\;}l@{\;\;}l@{\;\;}c}
\textbf{Algebraic object} & \textbf{Holographic role}
 & \textbf{Entanglement concept} & \textbf{Status} \\
\midrule
$Q_g(\cA) \oplus Q_g(\cA^!)$
 & Lagrangian splitting of phase space
 & dimensional Page constraint
 & \ref{thm:thqg-g3-polarization} \\
$\sigma$ (Verdier involution)
 & gravitational CPT
 & Tomita--Takesaki $J$ (structural)
 & \S\ref{subsec:thqg-entanglement-modular-flow} \\
$\langle \cdot, \cdot \rangle_g$ (Verdier pairing)
exec
/bin/zsh -lc "rg -n 'quantum-complementarity-main|genus-1 structure|dim H_1|Q_1\\(|lambda_1|genus-1 complementarity|Verdier pairing' chapters/theory/higher_genus_complementarity.tex chapters/theory/higher_genus_modular_koszul.tex -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_complementarity.tex:41:(Theorem~\ref{thm:quantum-complementarity-main}).
chapters/theory/higher_genus_complementarity.tex:75: the Verdier involution~$\sigma$. For $g \geq 1$, the Verdier pairing
chapters/theory/higher_genus_complementarity.tex:80: \textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main})}.
chapters/theory/higher_genus_complementarity.tex:87: Verdier pairing $\langle -,- \rangle_{\mathbb{D}}$ on the ambient
chapters/theory/higher_genus_complementarity.tex:103:nondegeneracy of the Verdier pairing is a hypothesis verified
chapters/theory/higher_genus_complementarity.tex:171:$Q_1(\mathcal{H}_\kappa)=\mathbb{C}\cdot\kappa$ (central extension),
chapters/theory/higher_genus_complementarity.tex:172:$Q_1(\mathcal{H}_\kappa^!)=\mathbb{C}\cdot\lambda$ (curved structure),
chapters/theory/higher_genus_complementarity.tex:506:$\mathrm{C}_1$ (Theorem~\ref{thm:quantum-complementarity-main})
chapters/theory/higher_genus_complementarity.tex:527:\label{thm:quantum-complementarity-main}
chapters/theory/higher_genus_complementarity.tex:672:The proof of Theorem~\ref{thm:quantum-complementarity-main} given in
chapters/theory/higher_genus_complementarity.tex:996:anticipating Theorem~C (Theorem~\ref{thm:quantum-complementarity-main}),
chapters/theory/higher_genus_complementarity.tex:1019:Q_1(\mathcal{H}_\kappa) = \text{span}\{\kappa \cdot \lambda_1\} \cong \mathbb{C}
chapters/theory/higher_genus_complementarity.tex:1021:Here $\kappa$ is the level parameter and $\lambda_1 = c_1(\mathbb{E})$ is the Hodge class;
chapters/theory/higher_genus_complementarity.tex:1022:the obstruction class $\kappa \cdot \lambda_1$ is a genus-$1$ quantum correction
chapters/theory/higher_genus_complementarity.tex:1175:Combining with the Verdier pairing on $\Omega^*_{\log}$ from Theorem~\ref{thm:verdier-duality-config-complete}, we obtain:
chapters/theory/higher_genus_complementarity.tex:1181:This pairing is perfect because both the Koszul pairing and the Verdier pairing are 
chapters/theory/higher_genus_complementarity.tex:1248:with respect to the Verdier pairing. At genus $0$, the
chapters/theory/higher_genus_complementarity.tex:1252:\textup{(}Theorem~\textup{\ref{thm:quantum-complementarity-main}}\textup{)}.
chapters/theory/higher_genus_complementarity.tex:1268:Theorem~\ref{thm:quantum-complementarity-main}.
chapters/theory/higher_genus_complementarity.tex:1453:\rho(\kappa)(\alpha) = \lambda_1 \cup \alpha
 succeeded in 7m 51s:
=== ch:bv-brst ===
ch:bv-brst
ch:bv-brst
ch:bv-brst
ch:bv-brst
ch:bv-brst
=== ch:feynman ===
ch:feynman
ch:feynman
ch:feynman
ch:feynman
ch:feynman
=== chap:ordered-associative-chiral-kd ===
ch:ordered-associative-chiral-kd
ch:ordered-associative-chiral-kd
ch:ordered-associative-chiral-kd
ch:ordered-associative-chiral-kd
ch:ordered-associative-chiral-kd
=== conj:toroidal-e1 ===
conj:toroidal-e1

thinking
**Analyzing proof justification**

I’m considering how to express that the cited proof doesn’t support the universal claim. It seems the only relevant local theorem is `thm:quantum-complementarity-main`. While it addresses decomposition, it doesn't cover the genus-1 dimension count. I need to be careful not to assert anything false, just to clarify it's unsupported. I think I’ve got a clearer perspective now!
exec
/bin/zsh -lc "sed -n '600,632p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
 bar coalgebra $B(\cA)$.

\item \emph{Decoding.}
 $\Omega \colon B(\cA) \to \Omega(B(\cA))$:
 the cobar construction provides recovery.

\item \emph{Exact inversion on the Koszul locus.}
 Theorem~B gives $\Omega(B(\cA)) \xrightarrow{\sim} \cA$:
 the recovery map is a quasi-isomorphism, recovering $\cA$
 exactly from $B(\cA)$.

\item \emph{Dual algebra.}
 $\cA^! = (H^*(B(\cA)))^\vee$: the Koszul dual is
 the cohomology of the bar complex, dualized.
 The line-operator category
 $\mathcal{C} \simeq \cA^!\text{-}\mathsf{mod}$.
\end{enumerate}
\end{proposition}

\begin{proof}
exec
/bin/zsh -lc "sed -n '566,608p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The shadow connection provides the bridge: its monodromy
$-1$ is the algebraic KMS periodicity, and
$\sigma$ interchanges the two halves.
The precise relationship requires the analytic completion
(sewing envelope) to make the von~Neumann algebra structure
available.
\end{remark}

% ======================================================================
%
% 7. ERROR CORRECTION FROM KOSZUL DUALITY
%
% ======================================================================

\subsection{Error correction from Koszul duality}
\label{subsec:thqg-entanglement-error-correction}
\index{error correction!from Koszul duality|textbf}
\index{holographic error correction|textbf}

The bar-cobar adjunction provides a natural encoding/decoding

thinking
**Searching for theorems**

Okay, part (iv) mentions the line-operator category C being equivalent to A^!-mod, which doesn't seem to be specific to Yangians. I think I should look into local theorems about line categories or modules. Possible options might include `thm:line-category`, `thm:full-derived-module-equiv-proved`, or `thm:factorization-dk-eval`. So, I'll need to conduct a search to gather more information on these theorems. This should help clarify things further.
exec
/bin/zsh -lc "rg -n 'label\\{thm:line-category\\}|label\\{thm:full-derived-module-equiv-proved\\}|label\\{thm:full-derived-module-equiv\\}|label\\{thm:factorization-dk-eval\\}|line-operator category|A\\"'^!'"\\\\text-\\\\mathsf\\{mod\\}|Koszul dual.*module|cA\\"'^!'"' chapters -g '*.tex' | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 200

chapters/examples/w_algebras_deep.tex:2754:$\mathfrak{T} = (\cA,\, \cA^!,\, r(z))$, where:
chapters/examples/w_algebras_deep.tex:2756:\item $(\cA, \cA^!)$ is a chiral Koszul pair
chapters/examples/w_algebras_deep.tex:2759: \in \cA^! \,\widehat{\otimes}\, \cA^!(\!(z^{-1})\!)$
chapters/examples/w_algebras_deep.tex:2779:The modular Koszul triple $(\cA, \cA^!, r(z))$ is
chapters/examples/w_algebras_deep.tex:2789:= (\cA, \cA^!, C, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$
chapters/examples/w_algebras_deep.tex:2793:(\cA,\, \cA^!,\, r(z))
chapters/examples/w_algebras_deep.tex:3553:The complementarity sum $\kappa(\cA) + \kappa(\cA^!)$
chapters/examples/lattice_foundations.tex:3185:Then the Koszul dual $\cA^!$ is the same algebra with the
chapters/examples/lattice_foundations.tex:3195: & \textbf{Koszul dual $\cA^!$}
chapters/examples/lattice_foundations.tex:3494:the logarithm changes sign under duality: $\log(\cA^!) = -\log(\cA)$,
chapters/examples/beta_gamma.tex:2931: \cA^! \otimes \cA^!\,[\![z^{-1}]\!].
chapters/examples/beta_gamma.tex:2936:$\Convstr(\bar{B}^{\mathrm{ch}}(\cA),\, \cA^!)$.
chapters/examples/w3_holographic_datum.tex:20:$H(\Walg_3) = (\cA, \cA^!, \mathcal{C}, r(z), \Theta_\cA,
chapters/examples/w3_holographic_datum.tex:70:$H(\cA) = (\cA, \cA^!, \mathcal{C}, r(z), \Theta_\cA,
chapters/examples/w3_holographic_datum.tex:101:\subsection{The Koszul dual \texorpdfstring{$\cA^! = \Walg_3(100-c)$}{A! = W3(100-c)}}
chapters/examples/w3_holographic_datum.tex:110:DS construction is symmetric in $k \leftrightarrow k'$, so $\cA^!$
chapters/examples/w3_holographic_datum.tex:114:\subsection{The line-operator category \texorpdfstring{$\mathcal{C}$}{C}}
chapters/examples/w3_holographic_datum.tex:117:On the evaluation-generated core of the line-operator category,
exec
/bin/zsh -lc "sed -n '165,190p' chapters/connections/thqg_introduction_supplement_body.tex
printf '\\n---\\n'
sed -n '1028,1048p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\label{subsec:thqg-intro-holographic-from-mc}
\index{holographic modular Koszul datum!construction from MC}

The holographic datum
$\mathcal{H}(\cA) = (\cA, \cA^!, \mathcal{C}, r(z), \Theta_\cA,
\nabla^{\mathrm{hol}})$
of~\eqref{eq:supp-holographic-datum-intro} is not defined by listing
six independent objects. It is extracted from the single
Maurer--Cartan element $\Theta_\cA$ by a sequence of projections.

\begin{enumerate}[label=\textup{(\roman*)}]
\item The boundary algebra~$\cA$ is the input.
\item The Koszul dual~$\cA^!$ is the graded linear dual of the bar
 cohomology coalgebra: $\cA^! = (H^*(\barB_X(\cA)))^\vee$. By Theorem~A,
 $\mathbb{D}_{\operatorname{Ran}}\,\barB_X(\cA) \simeq \cA^!_\infty$
 (the homotopy Koszul dual algebra, whose underlying complex is
 equivalent to $\barB_X(\cA^!)$).
\item The line-operator category is $\mathcal{C} = \cA^!\text{-}\mathsf{mod}$.
\item The spectral $r$-matrix is the binary genus-$0$ collision residue
 of~$\Theta_\cA$:
exec
/bin/zsh -lc "rg -n 'label\\{def:thqg-holographic-datum\\}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

exec
/bin/zsh -lc "rg -n 'thqg-holographic-datum' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
./main.tex:1654: \phantomsection\label{def:thqg-holographic-datum}%
./chapters/connections/thqg_open_closed_realization.tex:1044:(Definition~\ref{def:thqg-holographic-datum})
./chapters/connections/thqg_open_closed_realization.tex:1571: & Def.~\ref{def:thqg-holographic-datum}(c) \\
./chapters/connections/thqg_open_closed_realization.tex:1573: & modular shadow connection & Def.~\ref{def:thqg-holographic-datum}(e) \\
./chapters/connections/thqg_open_closed_realization.tex:1581:$\mathcal{H}(\cA)$ (Definition~\ref{def:thqg-holographic-datum})
./chapters/connections/frontier_modular_holography_platonic.tex:88:(Definition~\ref{def:thqg-holographic-datum}) is now subsumed by
./chapters/connections/thqg_entanglement_programme.tex:38:(Definition~\ref{def:thqg-holographic-datum}) encodes six algebraic
./chapters/connections/thqg_entanglement_programme.tex:375:Definition~\textup{\ref{def:thqg-holographic-datum}},
exec
/bin/zsh -lc "sed -n '6548,6588p' chapters/connections/concordance.tex
printf '\\n---\\n'
sed -n '3748,3782p' chapters/connections/concordance.tex
printf '\\n---\\n'
rg -n 'holographic programme|three-tier r-matrix|sl3-bar-table|soft graviton|ten theorems|DR hierarchy|string equation|open-sector factorization category' chapters -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\subsection{Summary}

The historical rhyme is this. Classical operadic Koszul duality
says: quadratic presentation plus bar-cobar formalism produces
homotopy theory. The theory sought here says: factorization
presentation on curves plus Verdier duality on modular
compactifications produces \emph{modular homotopy theory}. Just as
Drinfeld--Kohno related KZ monodromy to quantum groups, the theory
sought here would relate configuration-space/Deligne--Mumford
monodromy to curved chiral Koszul duality. And just as \'etale
cohomology supplied the correct ambient cohomology theory for
Frobenius and zeta functions, factorization homology on
$\operatorname{Ran}(X)$ together with Verdier duality on
$\overline{\mathcal{M}}_{g,n}$ is the correct ambient cohomology
theory for OPE, monodromy, and bar-cobar duality on curves.

\subsection{The holographic completion}
\label{subsec:concordance-holographic-completion}
\index{holographic modular Koszul datum!concordance}

exec
/bin/zsh -lc "rg -n 'three-tier|tier.*r-matrix|r-matrix classification' chapters/connections/concordance.tex chapters/theory/introduction.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/introduction.tex:1598:\label{def:three-tier-r-matrix}
chapters/theory/introduction.tex:1599:\index{R-matrix!three-tier classification|textbf}%
chapters/theory/introduction.tex:1635:\label{rem:three-tier-examples}
chapters/theory/introduction.tex:1636:\index{R-matrix!three-tier classification!examples}%
chapters/theory/introduction.tex:1682:\label{rem:three-tier-boundary-bulk}
chapters/theory/introduction.tex:1683:\index{boundary-bulk reconstruction!three-tier coupling}%
chapters/theory/introduction.tex:1686:tiers of Definition~\ref{def:three-tier-r-matrix} correspond to
chapters/theory/introduction.tex:2439: Definition~\ref{def:three-tier-r-matrix}, with $\Theta_\cA^{\Eone}$
exec
/bin/zsh -lc "rg -n 'label\\{sec:.*sl3|label\\{subsec:.*bar-table|sl3.*table' chapters/examples/bar_complex_tables.tex chapters/examples/kac_moody.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:568:\label{sec:sl3-degree3-details}
chapters/examples/bar_complex_tables.tex:750:bar complex]\label{comp:sl3-dim-table}
chapters/examples/bar_complex_tables.tex:926:\label{sec:sl3-spectral-sequence}
chapters/examples/bar_complex_tables.tex:4155:Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
chapters/examples/bar_complex_tables.tex:4200:\caption[Bar cohomology generating functions across standard families]{Generating functions for bar cohomology across standard families. The interacting families $\beta\gamma$, $\widehat{\mathfrak{sl}}_{2,k}$, and $\mathrm{Vir}_c$ share the universal discriminant $(1 - 3x)(1 + x)$ and growth rate $3^n$; $\widehat{\mathfrak{sl}}_{3,k}$ departs via the quadratic $1 - 3x - x^2$ whose dominant root is $(-3 + \sqrt{13})/2$. The free families $\cH, \cF$ have sub-exponential growth set by the Hardy-Ramanujan asymptotics of the partition function. The $\widehat{\mathfrak{sl}}_{2,k}$ entry is labelled \emph{modified} Riordan because the chiral bar cohomology gives $H^2 = 5$ whereas the standard Riordan recursion (or the Chevalley-Eilenberg count on $\mathfrak{g}_-$) gives $6$; see \ap{63} and Section~\ref{sec:sl3-bar-table}.}
chapters/examples/kac_moody.tex:778:\label{sec:sl3-computation}
chapters/examples/kac_moody.tex:3945:\label{sec:sl3-genus-one-pipeline}
exec
/bin/zsh -lc "sed -n '4138,4164p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Free fermion: $G_{\cF}(x) = x + x^2 + 2x^3 + 3x^4 + 5x^5 + \cdots$
(shifted by one degree).
Virasoro: $M(2) - M(1) = 1$, $M(3) - M(2) = 2$, $M(4) - M(3) = 5$,
$M(5) - M(4) = 12$, $M(6) - M(5) = 30$ (see
Proposition~\ref{prop:virasoro-koszul-acyclic}).
Betagamma: direct square-root expansion gives
$\sqrt{(1+x)/(1-3x)} = 1 + 2x + 4x^2 + 10x^3 + 26x^4 + 80x^5 + \cdots$
(verified by squaring: $(1 + 2x + 4x^2 + 10x^3 + 26x^4)^2 =
1 + 4x + 12x^2 + 36x^3 + 108x^4 + \cdots$, matching the expansion
of $(1+x)/(1-3x)$ through order $x^4$).
Affine $\widehat{\mathfrak{sl}}_{2,k}$: the bar cohomology yields
$\dim H^2 = 5$, \emph{not} $6$ (\ap{63}): the chiral bar complex
departs from the Chevalley-Eilenberg count on the negative
subalgebra, and the standard Riordan recursion fails.
We record this as the \emph{modified Riordan} generating function.
Affine $\widehat{\mathfrak{sl}}_{3,k}$: the dimensions
$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
Section~\ref{sec:sl3-bar-table} satisfy a quadratic recursion with
characteristic polynomial whose discriminant involves $\sqrt{13}$:
the dominant singularity sits at $x_* = (-3 + \sqrt{13})/2$,

thinking
**Identifying references**

I should mention either `Section\ref{sec:sl3-computation}` or `Computation\ref{comp:sl3-dim-table}` to clarify my point. It seems the dimensions list likely comes from the computation table `comp:sl3-dim-table`. I’ll want to look around line 750 for that information. This will help ensure that everything is firmly connected and accurate; I definitely want to get this right!
exec
/bin/zsh -lc "sed -n '736,770p' chapters/examples/bar_complex_tables.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
elements produce cycles in $\bar{B}^2$.

(iii): At $k = -3$ (critical level), the bar complex is uncurved ($\dfib^{\,2} = 0$ since $\kappa = 0$),
so the cycles $S$ and $\tilde{S}$ represent honest cohomology classes.
The Feigin--Frenkel theorem (Theorem~\ref{thm:critical-level-structure})
identifies $Z(\widehat{\mathfrak{sl}}_{3,-3})$ with a polynomial algebra
in two generators (degrees $2$ and $3$, corresponding to the fundamental
invariants of the Langlands dual $\mathfrak{sl}_3^\vee$). The degree-2
generator corresponds to the Casimir class in $H^2(\bar{B})$; the
degree-3 class arising from the Serre relations corresponds to the
cubic invariant.
\end{proof}

\begin{computation}[Dimension table for \texorpdfstring{$\widehat{\mathfrak{sl}}_3$}{sl-hat_3}
bar complex]\label{comp:sl3-dim-table}
\index{bar complex!dimension table!sl3@$\mathfrak{sl}_3$}
The dimensions of the bar complex components $\bar{B}^n = \mathfrak{sl}_3^{\otimes n}
\otimes \Omega^{n-1}(\overline{\mathrm{Conf}}_n)$ through degree~5:
\begin{center}
\renewcommand{\arraystretch}{1.2}

thinking
**Searching for complex dimensions**

I see that the table provides raw bar complex dimensions, but I need the cohomology values like `[1, 8, 36, 204, ...]`. I think I should search for these numbers in the Kac-Moody section, specifically in `sec:sl3-genus-one-pipeline`. However, there's a chance they might be in the `bar_complex_tables.tex` file, possibly in `sec:sl3-spectral-sequence`. I’ll make sure to search for the exact numbers to find the right information!
exec
/bin/zsh -lc "rg -n -F '[1, 8, 36, 204, 1352, 9892' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/examples/bar_complex_tables.tex:4154:$[1, 8, 36, 204, 1352, 9892, \ldots]$ of
exec
/bin/zsh -lc "sed -n '500,540p' chapters/connections/entanglement_modular_koszul.tex
printf '\\n---\\n'
sed -n '780,802p' chapters/connections/thqg_entanglement_programme.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{enumerate}[label=\textup{(\roman*)}]
\item The area term is the scalar entanglement entropy:
 $\mathrm{Area}(\gamma)/(4G_N) = S_{\EE}^{\mathrm{sc}}(\cA)
 = (c/3)\log(L/\varepsilon)$.

\item The bulk entropy $S_{\mathrm{bulk}}$ is the
 shadow correction series
 $\sum_{r \ge 3} \delta S_r(\cA)$,
 controlled by the shadow obstruction tower.

\item The stationarity condition
 $\nabla_\gamma S_{\QES} = 0$
 is a Ward identity of the modular shadow connection
 $\nabla^{\mathrm{hol}}_{g,n} = d - \Sh_{g,n}(\Theta_\cA)$
 restricted to the replica geometry.
\end{enumerate}
\end{conjecture}

\begin{remark}[Evidence]
Part~(i) is Theorem~\ref{thm:ent-scalar-entropy}.
exec
/bin/zsh -lc "rg -n 'label\\{thm:shadow-connection\\}|label\\{prop:thqg-intro-flatness\\}|shadow connection|flatness' chapters/connections -g '*.tex' | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/connections/thqg_open_closed_realization.tex:1573: & modular shadow connection & Def.~\ref{def:thqg-holographic-datum}(e) \\
chapters/connections/editorial_constitution.tex:1939: classical Maurer--Cartan = flatness,
chapters/connections/editorial_constitution.tex:1954:Maurer--Cartan/flatness identification, the affine
chapters/connections/genus_complete.tex:756:MC class, and shadow connection) is the \emph{holographic modular
chapters/connections/genus1_seven_faces.tex:334:modular shadow connection $\nabla^{\mathrm{hol}}_{1,n}$ on
chapters/connections/genus1_seven_faces.tex:415:shadow connection on $\overline{\cM}_{1,n}$ has a component in the
chapters/connections/genus1_seven_faces.tex:424:\begin{remark}[The KZB connection as the full genus-$1$ shadow connection]
chapters/connections/genus1_seven_faces.tex:429:\S\ref{sec:hdm-hbar-identification}: the shadow connection on
chapters/connections/genus1_seven_faces.tex:920:and the modular shadow connection are defined for all modular Koszul
chapters/connections/genus1_seven_faces.tex:1155:is controlled by the modular shadow connection, not by a quantum group.
chapters/connections/thqg_introduction_supplement_body.tex:3:% shadow connection, gravitational complexity, duality and phase space,
chapters/connections/thqg_introduction_supplement_body.tex:195:\item The shadow connection $\nabla^{\mathrm{hol}}$ is constructed
chapters/connections/thqg_introduction_supplement_body.tex:294:comparison surface, the shadow connection $\nabla^{\mathrm{hol}}$
chapters/connections/thqg_introduction_supplement_body.tex:335:\section{The shadow connection and conformal-block comparison surfaces}
chapters/connections/thqg_introduction_supplement_body.tex:337:\index{shadow connection|textbf}
chapters/connections/thqg_introduction_supplement_body.tex:338:\index{conformal blocks!and shadow connection}
chapters/connections/thqg_introduction_supplement_body.tex:351:equations. Its flatness is guaranteed by the MC equation.
chapters/connections/thqg_introduction_supplement_body.tex:353:\subsection{Construction of the shadow connection}
chapters/connections/thqg_introduction_supplement_body.tex:355:\index{shadow connection!construction}
chapters/connections/thqg_introduction_supplement_body.tex:386:\begin{definition}[The shadow connection]
exec
/bin/zsh -lc "rg -n 'label\\{thm:shadow-connection\\}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:18918:\label{thm:shadow-connection}
exec
/bin/zsh -lc "rg -n 'DR hierarchy|string equation|Buryak|forgetful property' chapters -g '*.tex' | sed -n '1,180p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w_algebras_deep.tex:5496:Buryak--Shadrin--Spitz--Zvonkine identification of the Pixton
chapters/connections/concordance.tex:7166:Vol.~II, rank-$1$ DR string equation
chapters/connections/concordance.tex:7167: & CohFT string equation at rank $1$ & DR cycle forgetful $+$ Buryak DR/DZ \\
chapters/connections/outlook.tex:517:D-module purity converse, CohFT string equation, Kontsevich graph
chapters/connections/outlook.tex:602:(string equation) requires the vacuum to lie in the generating
chapters/connections/outlook.tex:603:space~$V$. The rank-$1$ string equation is proved unconditionally via
chapters/connections/outlook.tex:604:the DR hierarchy (Buryak's forgetful property of DR cycles,
chapters/connections/outlook.tex:609:The modified string equation with $\psi$-class corrections from the
exec
/bin/zsh -lc "rg -n 'open-sector factorization category|label\\{subsec:.*open-sector.*category\\}|label\\{sec:thqg-open-closed-realization\\}' chapters/connections/thqg_open_closed_realization.tex chapters/connections/thqg_introduction_supplement_body.tex -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/thqg_open_closed_realization.tex:14:\label{sec:thqg-open-closed-realization}
exec
/bin/zsh -lc "sed -n '1228,1250p' chapters/connections/thqg_open_closed_realization.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
a \emph{modular cooperad} in the sense of Getzler--Kapranov
\cite{GetzlerKapranov98}, and whether the assembled structure is
determined by the open-closed MC element $\Theta^{\mathrm{oc}}_\cA$.
We record the expected answer as a conjecture and give a five-phase
road map whose first three phases are already proved.

\begin{conjecture}[CT-2: modular cooperad on the open sector]
\ClaimStatusConjectured
\label{conj:ct2}
Let $\cA$ be a gravitational input
(Definition~\ref{def:thqg-standing-hypotheses}) and let
$\mathcal{C}_{\mathrm{op}}$ denote the open-sector factorization
dg category of
\S\ref{subsec:thqg-open-sector-factorization-category}.
There exists a modular cooperad structure
\[
\Delta^{\mathrm{op}}_{\mathrm{mod}}
\colon
\mathcal{C}_{\mathrm{op}}
\longrightarrow
exec
/bin/zsh -lc "rg -n '\\\\mathcal\\{C\\}_\\{\\\\mathrm\\{op\\}\\}|open-sector|factorization dg category' chapters/connections/thqg_open_closed_realization.tex -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1146: The closed-sector genus-$g$ amplitude and the open-sector
1205:\item \emph{The independent open-sector derivation.}
1207: $\mathcal{C}_{\mathrm{op}}$ alone (without invoking the
1222:The open-sector factorization dg category $\mathcal{C}_{\mathrm{op}}$
1239:$\mathcal{C}_{\mathrm{op}}$ denote the open-sector factorization
1241:\S\ref{subsec:thqg-open-sector-factorization-category}.
1246:\mathcal{C}_{\mathrm{op}}
1248:\mathcal{C}_{\mathrm{op}} \mathbin{\widehat{\boxtimes}}
1249:\mathcal{C}_{\mathrm{op}}
1251:on $\mathcal{C}_{\mathrm{op}}$ with the following three properties.
1266: structures on $\mathcal{C}_{\mathrm{op}}$ that agree on
1278:The cooperad structure on $\mathcal{C}_{\mathrm{op}}$ lifts the
1281:Theorem~A. The lift exists because $\mathcal{C}_{\mathrm{op}}$
1283:(see the chapter on the open-sector PVA). Layer~1 is the content
1333: $\mathcal{C}_{\mathrm{cl}}$ to $\mathcal{C}_{\mathrm{op}}$,
1334: using homotopy Koszulness of $\mathcal{C}_{\mathrm{op}}$ (Vol~II
1348:$\mathcal{C}_{\mathrm{op}}$ exists and is unique up to
1361:homotopy-coherent $(\infty,2)$-category of open-sector

thinking
**Fixing references in text**

I think the reference might be introduced in the nearby text without a subsection label. One straightforward fix would be to replace `\S\ref{subsec:thqg-open-sector-factorization-category}` with “the discussion in the preceding paragraph” or just delete it. Actually, it looks like line 1239 defines `\mathcal C_op`, making the reference unnecessary. I’ll simply replace it with “Let $\mathcal{C}_{\mathrm{op}}$ denote the open-sector factorization dg category arising from the boundary sector of$\cA$.” 

For `thm:bar-cobar-path-integral-heisenberg`, it seems to be incorrectly referenced. I might need to search for local candidates to clarify that it's a conjecture, not a theorem.
exec
/bin/zsh -lc "sed -n '5088,5116p' chapters/examples/free_fields.tex
printf '\\n---\\n'
sed -n '130,150p' chapters/connections/feynman_connection.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\item Along a separating boundary divisor
 $D_\Gamma \cong \overline{\mathcal{M}}_{g_1,n_1+1}
 \times \overline{\mathcal{M}}_{g_2,n_2+1}$, its residue is the
 contracted tensor product of the corresponding lower-genus bar
 classes.
\item Along a non-separating boundary divisor
 $D_\Gamma \cong \overline{\mathcal{M}}_{g-1,n+2}$, its residue is
 the self-gluing contraction of the $(g-1,n+2)$ bar class.
\item For the Heisenberg algebra $\mathcal{H}_\kappa$, pairing the bar
 class with the Gaussian measure at all genera computes free boson
 correlation functions
 \textup{(}Theorem~\textup{\ref{thm:bar-cobar-path-integral-heisenberg})}.
\end{enumerate}
\end{theorem}

\begin{proof}
Items~(i) and~(ii) are the separating and non-separating boundary
components of the modular operad structure on the genus-graded bar
package: the bar differential on stable curves is assembled from
boundary residues, and Theorem~\ref{thm:genus-induction-strict}
exec
/bin/zsh -lc "sed -n '5068,5108p' chapters/examples/free_fields.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
$\hbar = g_s = 1/N$, which requires AdS/CFT.

\emph{Homotopy template} (Convention~\ref{conv:hms-levels}): Type~IV
(trace/index). The identification $\hbar = g_s$ asserts that the
genus expansion parameter is the image of the universal deformation
object under a trace functor.
\end{remark}


\subsection{String amplitudes via bar complex}

\begin{theorem}[Bar classes on moduli and boundary factorization;
\ClaimStatusProvedHere]
\label{thm:bar-string-integrand}
\index{bar complex!moduli class}
For vertex operators $V_1,\ldots,V_n$, the genus-$g$, $n$-point bar
class
$\barBgeom^{(g)}_n(V_1 \otimes \cdots \otimes V_n)$
satisfies the following properties:
\begin{enumerate}[label=\textup{(\roman*)}]
exec
/bin/zsh -lc "sed -n '878,900p' chapters/frame/heisenberg_frame.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The chain basis is special precisely because it diagonalizes the
``adjacency'' of the logarithmic forms.

\subsection{The general theorem}

\begin{theorem}[Heisenberg bar complex at genus~\texorpdfstring{$0$}{0}; \ClaimStatusProvedHere]
\label{thm:frame-heisenberg-bar}
For $\mathcal{H}_k$ on $\mathbb{P}^1$:
\begin{equation}\label{eq:frame-heisenberg-bar-cohomology}
H^n(\bar{B}^{\mathrm{ch}}_{\mathrm{geom}}(\mathcal{H}_k))
= \begin{cases}
\mathbb{C} & n = 0, \\
0 & n = 1, \\
\mathbb{C} \cdot c_k & n = 2, \\
0 & n > 2.
\end{cases}
\end{equation}
The class $c_k \in H^2$ arises from the triple-collision residue
and is the homological manifestation of the central extension.
The differential satisfies $d^2 = 0$ at all degrees by the
exec
/bin/zsh -lc "rg -n 'label\\{chap:casimir-divisor\\}' . -g '*.tex'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
./main.tex:1676: \phantomsection\label{chap:casimir-divisor}% % casimir_divisor_core_transport.tex (migrated to Vol II)
exec
/bin/zsh -lc "rg -n 'D.Hoker|determinant formula|Sewing--Selberg formula|Heisenberg partition function factorizes|Selberg zeta function|Belavin--Knizhnik formula|Heisenberg-selberg|lambda = c_1' chapters/connections/bv_brst.tex chapters/connections/arithmetic_shadows.tex chapters/examples/heisenberg_eisenstein.tex -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/heisenberg_eisenstein.tex:2222:determinant formula
chapters/connections/bv_brst.tex:1524:\noindent\textbf{Path \textup{(b)}: Selberg zeta function.}
chapters/connections/bv_brst.tex:1525:\index{Selberg zeta function!BV/bar proof|(}
chapters/connections/bv_brst.tex:1526:The D'Hoker--Phong determinant formula~\cite{DP86} expresses
chapters/connections/bv_brst.tex:1536:is the Selberg zeta function, the product running
chapters/connections/bv_brst.tex:1540:The Heisenberg partition function factorizes as
chapters/connections/bv_brst.tex:1550:$\lambda = c_1(\det\mathbb{E})$ combined with the
chapters/connections/bv_brst.tex:1551:Belavin--Knizhnik formula~\cite{BK86} gives
chapters/connections/bv_brst.tex:1560:\index{Selberg zeta function!BV/bar proof|)}
chapters/connections/arithmetic_shadows.tex:386:\begin{theorem}[Sewing--Selberg formula]
chapters/connections/arithmetic_shadows.tex:8618:of D'Hoker--Green--G\"urdo\u{g}an--Vanhove and
chapters/connections/arithmetic_shadows.tex:10246:\begin{remark}[The Selberg zeta function as geometric bridge]%
chapters/connections/arithmetic_shadows.tex:10248:\index{Selberg zeta function!arithmetic bridge}%
chapters/connections/arithmetic_shadows.tex:10250:Selberg zeta function
exec
/bin/zsh -lc "sed -n '386,420p' chapters/connections/arithmetic_shadows.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\begin{theorem}[Sewing--Selberg formula]
\label{thm:sewing-selberg-formula}
\ClaimStatusProvedHere
The Rankin--Selberg integral of the sewing Fredholm determinant
against the Eisenstein series over $\cM_{1,1}$ is
\begin{equation}\label{eq:sewing-selberg}
 \int_{\cM_{1,1}}
 \log\det(1-K(\tau))\cdot E_s(\tau)\,d\mu(\tau)
 = -2(2\pi)^{-(s-1)}\,\Gamma(s-1)\,\zeta(s-1)\,\zeta(s).
\end{equation}
\end{theorem}

\begin{proof}
Rankin--Selberg unfolding replaces the integral over the fundamental
domain by $\int_0^\infty a_0(y)\,y^{s-2}\,dy$, where
$a_0(y) = \int_0^1 \log\det(1-K(\tau))\,dx$ is the zeroth Fourier
mode. On the imaginary axis,
$a_0(y) = \log\lvert\eta(iy)\rvert^2+\pi y/6
= 2\log\det(1-K_q)$, and the Mellin transform of
$-\sum\sigma_{-1}(N)e^{-2\pi Ny}$ against $y^{s-2}$ gives

thinking
**Reviewing theorems and citations**

In the given lines 1539-1548 of the bv_brst, there are references to a missing theorem or correlation that might actually need to cite `thm:sewing-selberg-formula`. I’m thinking it would be a good idea to inspect those specific lines to confirm their relevance. It’s essential to ensure any necessary citations are accurate to maintain clarity and provide a proper framework for the context. Let's ensure we have everything in order!
exec
/bin/zsh -lc "sed -n '1524,1555p' chapters/connections/bv_brst.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\noindent\textbf{Path \textup{(b)}: Selberg zeta function.}
\index{Selberg zeta function!BV/bar proof|(}
The D'Hoker--Phong determinant formula~\cite{DP86} expresses
the Laplacian determinant on a compact hyperbolic
surface~$\Sigma_g$ as
\begin{equation}\label{eq:dhoker-phong-det}
\det\nolimits'_\zeta(\Delta_{\Sigma_g})
= Z_{\mathrm{Sel}}(1;\Sigma_g)\cdot e^{c_g},
\end{equation}
where $Z_{\mathrm{Sel}}(s;\Sigma_g)
= \prod_{\gamma\, \text{prim.}} \prod_{n=0}^\infty
(1 - e^{-(s+n)\ell(\gamma)})$
is the Selberg zeta function, the product running
over primitive closed geodesics, and $c_g$ is a genus-dependent
spectral constant
\textup{(}Theorem~\ref{thm:thqg-I-determinant-formula}\textup{)}.
The Heisenberg partition function factorizes as
\begin{equation}\label{eq:heisenberg-selberg}
Z_g(\cH_\kappa;\Sigma_g)
= \bigl(\det\operatorname{Im}\Omega\bigr)^{-\kappa/2}
exec
/bin/zsh -lc "sed -n '454,476p' chapters/connections/editorial_constitution.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
same logical level. Genus-$0$ algebraic BRST/bar comparison: proved
\textup{(}Theorem~\textup{\ref{thm:algebraic-string-dictionary})}; the
tree-level moduli-integration/amplitude pairing is only conditional
\textup{(}Corollary~\textup{\ref{cor:string-amplitude-genus0})}.}
\end{conjecture}

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
exec
/bin/zsh -lc "rg -n 'admissible level|admissible levels|simple quotients at admissible|quotients at admissible' chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
Total output lines: 193

chapters/examples/w_algebras_deep.tex:5018:\item the admissible levels of the parent superalgebra
chapters/examples/w_algebras_deep.tex:5085:$Y_{1,2,3}$). The admissible levels form a countable
chapters/examples/lattice_foundations.tex:4611: $\zeta = e^{2\pi i/(k+2)}$ for all admissible levels~$k$.
chapters/examples/y_algebras.tex:681:and the admissible levels of the parent superalgebra.
chapters/examples/kac_moody.tex:1036:\begin{remark}[Special values and admissible levels]
chapters/examples/kac_moody.tex:1038:\index{admissible level!bar cohomology jump}
chapters/examples/kac_moody.tex:2708:\index{admissible level!representations|textbf}
chapters/examples/kac_moody.tex:2721:\index{admissible level|textbf}
chapters/examples/kac_moody.tex:2743:\begin{theorem}[Representation theory at admissible level \cite{KW88, Arakawa17}; \ClaimStatusProvedElsewhere]
chapters/examples/kac_moody.tex:2745:\index{admissible level!representation theory}
chapters/examples/kac_moody.tex:2746:Let $k = -h^\vee + p/q$ be an admissible level.
chapters/examples/kac_moody.tex:2755: admissible level is rational if and only if the admissible level
chapters/examples/kac_moody.tex:2758: At non-degenerate admissible levels, $L_k(\mathfrak{g})$ has
chapters/examples/kac_moody.tex:2761: At degenerate admissible level, $L_k(\mathfrak{g})$ has
chapters/examples/kac_moody.tex:2769:\begin{proposition}[Bar complex at admissible level; \ClaimStatusProvedHere]
chapters/examples/kac_moody.tex:2771:\index{bar complex!admissible level}
chapters/examples/kac_moody.tex:2772:\index{admissible level!bar complex}
chapters/examples/kac_moody.tex:2773:Let $k = -h^\vee + p/q$ be an admissible level for
exec
/bin/zsh -lc "sed -n '4516,4532p' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{remark}

\begin{remark}[Scope boundary at admissible levels]
\label{rem:admissible-scope-boundary}
\index{admissible level!scope boundary}
\index{bar-cobar inversion!failure at admissible levels}
Theorem~B requires Koszulity (MK1). For simple admissible affine
quotients $L_k(\fg)$ at levels $k=-h^\vee+p/q$, that hypothesis is
not currently verified: null vectors obstruct the PBW/Shapovalov
route, and the bar-cobar counit is therefore not promoted here as a
derived equivalence. The obstruction is expected to be carried by
the nontrivial higher bar data encoded in $\Theta_\cA$.
The replacement is the coderived factorization co-contra comparison on
the bar-coalgebra surface
\textup{(}Theorem~\ref{thm:factorization-positselski}\textup{)},
which is available without Koszulness.
\end{remark}

thinking
**Considering label adjustments**

I'm thinking about fixing the labels in `Chapter\ref{chap:toroidal-elliptic}` or maybe adding missing phantom labels in main.tex. Right now, there are phantom labels for some moved labels from Vol III, but not for these. I could add those labels near line 1690 in main.tex to match the existing structure. 

But, wait, the numbering seems off. Still, the current pattern uses phantoms for theorem-like labels, which seems to be the fix in the repository.
exec
/bin/zsh -lc "rg -n 'label\\{prop:lagrangian-eigenspaces\\}|Verdier pairing and Lagrangian eigenspaces' chapters/theory/higher_genus_complementarity.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
1825:\begin{proposition}[Verdier pairing and Lagrangian eigenspaces; \ClaimStatusProvedHere]
1826:\label{prop:lagrangian-eigenspaces}

thinking
**Investigating the theorem**

I’m considering whether it could be both options, so I need to check the theorem around 260 in the supplement and see if there's anything related in the current repository. I’m curious about whether there’s a specific theorem labeled `thm:collision-residue-twisting`. It seems like a good idea to explore this further! I’ll need to conduct a search to gather more information and understand the context better. Let's see what I find!
exec
/bin/zsh -lc "rg -n 'label\\{thm:collision-residue-twisting\\}|label\\{thm:thqg-intro-collision-twisting\\}|twisting morphism|collision residue of Theta|universal twisting morphism' chapters -g '*.tex' | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 220

chapters/examples/deformation_quantization.tex:721:The bar complex $\barB(\cA)$ classifies twisting morphisms
chapters/examples/lattice_foundations.tex:928:The bar-cobar QI follows from Theorem~\ref{thm:lattice:koszul-morphism}: the twisting morphism $\tau$ is Koszul, so $\Omega^{\mathrm{ch}}(\barBgeom(\Vlat_\Lambda)) \xrightarrow{\sim} \Vlat_\Lambda$.
chapters/examples/lattice_foundations.tex:1002:The canonical twisting morphism
chapters/examples/free_fields.tex:1740:\begin{remark}[The twisting morphism for free-field dualities]
chapters/examples/free_fields.tex:1742:\index{twisting morphism!free fields}
chapters/examples/free_fields.tex:1744:universal twisting morphism
chapters/examples/free_fields.tex:1760:Dually, the twisting morphism for the $bc$ system
chapters/examples/free_fields.tex:1772:twisting morphisms}. Acyclicity of the twisted tensor product
chapters/examples/free_fields.tex:2821: canonical twisting morphism
chapters/examples/yangians_foundations.tex:703:\begin{remark}[Canonical twisting morphism for Yangians]
chapters/examples/yangians_foundations.tex:705:The canonical twisting morphism for the RTT Yangian
chapters/examples/yangians_foundations.tex:1365:\begin{remark}[Maurer--Cartan element as twisting morphism]
chapters/examples/yangians_foundations.tex:1367:\index{Maurer--Cartan element!twisting morphism}
chapters/examples/yangians_foundations.tex:1373:identification: $r(z)$ is the \emph{twisting morphism}
chapters/examples/yangians_foundations.tex:1555:The canonical H-level target already exists (Proposition~\ref{prop:yangian-canonical-hlevel-target}); the remaining MC4 problem is to equip it with compatible RTT-level quotients. Line-operator OPEs are organized by pole order, matching the RTT filtration, and the Maurer--Cartan element $r(z)$ appears as the degree-$2$ bar twisting morphism.
chapters/examples/yangians_foundations.tex:1560:Conjecture~\ref{conj:dg-shifted-yangian-rtt-package} reduces to four stagewise checks: (i)~RTT-level ideals are preserved by the differential and coproduct; (ii)~the level-$N$ quotient depends only on the first $N$ OPE modes; (iii)~that quotient is identified with $Y_{\le N}$ via $R$-matrix relations; (iv)~the induced degree-$2$ twisting morphism matches $\tau|_{\deg 2}$.
chapters/examples/kac_moody.tex:1324:\begin{remark}[Canonical twisting morphism for Kac--Moody]
chapters/examples/kac_moody.tex:1326:The canonical twisting morphism

thinking
**Looking for cross-volume surfaces**

I need to gather details on the cross-volume of the toroidal surfaces like `toroidal-e1`, `toroidal-koszul-dual`, and `toroidal-three-theorems`. I should also check the `elliptic-bar-heisenberg` for any relevant moves. Additionally, I suspect the main.tex might have phantom labels for some toroidal surfaces, but not exactly these. If I see multiple occurrences, I might mention them as a set to keep things clear. Let's sort through this!
exec
/bin/zsh -lc "rg -n 'Polyakov|Alvarez|label\\{eq:.*polyakov|Molien|Riordan recurrence|sl2-kappa|kappa\\(\\\\widehat\\{\\\\mathfrak\\{sl\\}_2' chapters -g '*.tex' | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
chapters/examples/w_algebras_deep.tex:263:operator) gives the \emph{Bershadsky--Polyakov algebra}
chapters/examples/w_algebras_deep.tex:1977:\begin{computation}[Non-principal DS: Bershadsky--Polyakov bar complex]
chapters/examples/w_algebras_deep.tex:1979:\index{Bershadsky--Polyakov algebra!bar complex}
chapters/examples/w_algebras_deep.tex:1981:The Bershadsky--Polyakov algebra $\mathcal{W}^k(\mathfrak{sl}_3,
chapters/examples/w_algebras_deep.tex:2017:Bershadsky--Polyakov algebra has $c = (k{-}15)/(k{+}3)\big|_{k=-1/2} = -31/5$
chapters/examples/w_algebras_deep.tex:2035:The Bershadsky--Polyakov algebra has more generators but simpler
chapters/examples/w_algebras_deep.tex:2338: (Bershadsky--Polyakov, generators
chapters/examples/w_algebras_deep.tex:2384:Bershadsky--Polyakov, a direct computation yields $K_{\mathrm{BP}} = 196$
chapters/examples/w_algebras_deep.tex:2417:Koszul conductor. For the Bershadsky--Polyakov algebra $\mathrm{BP}
chapters/examples/w_algebras_deep.tex:2456:spectrum alone. The Bershadsky--Polyakov algebra is a sharp
chapters/examples/heisenberg_eisenstein.tex:2413:The third is the Polyakov--Alvarez formula
chapters/examples/free_fields.tex:4591:that Polyakov introduces for gauge-fixing the worldsheet
chapters/examples/free_fields.tex:4609:\begin{remark}[Polyakov action as degree-$2$ shadow]
chapters/examples/free_fields.tex:4611:\index{Polyakov action!shadow tower interpretation}
chapters/examples/free_fields.tex:4612:\index{shadow tower!Polyakov action}
chapters/examples/free_fields.tex:4613:The Polyakov action
chapters/examples/free_fields.tex:4621:variation reproduces the Polyakov formula with coefficient
chapters/examples/free_fields.tex:4626:nonlinear OPE corrections that the quadratic Polyakov action
chapters/examples/free_fields.tex:4632:\index{Virasoro algebra!moduli correspondence!Polyakov significance}
chapters/examples/bershadsky_polyakov.tex:1:\chapter{The Bershadsky--Polyakov algebra}\label{chap:bershadsky-polyakov}
exec
/bin/zsh -lc "sed -n '34018,34032p' chapters/theory/higher_genus_modular_koszul.tex
printf '\\n---\\n'
rg -n 'sl2-kappa' chapters -g '*.tex' | sed -n '1,80p'
printf '\\n---\\n'
sed -n '2508,2574p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\end{proof}

\begin{remark}[The symmetric shadow at genus~$2$]
\label{rem:g2-shadow}
The averaging map $\av_2$ at degree~$2$ sends the
$12$-dimensional ordered de~Rham cohomology to
$\Sigma_2$-coinvariants. The scalar surviving $\av_2$ is
$\kappa = 3(k+2)/4$
(equation~\eqref{comp:sl2-kappa}), the same value as at
genus~$0$ and genus~$1$: the averaging map is a local
computation (residue extraction), independent of the global
topology.
The kernel $\ker(\av_2)$ at genus~$2$ is richer than at
genus~$1$: the four $B$-cycle monodromies contribute
independent antisymmetric classes that are invisible to the

---
chapters/examples/genus_expansions.tex:989:\begin{equation}\label{eq:sl2-kappa-decomp-genus2}
chapters/examples/genus_expansions.tex:1169:The decomposition~\eqref{eq:sl2-kappa-decomp-genus2} yields a
chapters/theory/higher_genus_modular_koszul.tex:34026:(equation~\eqref{comp:sl2-kappa}), the same value as at
exec
/bin/zsh -lc "rg -n 'label\\{eq:sl2-kappa\\}' chapters -g '*.tex'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

exec
/bin/zsh -lc "rg -n -F '\\kappa = 3(k+2)/4' chapters -g '*.tex' | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/kac_moody.tex:1527:$\kappa = 3(k+2)/4$. At $k=1$: $\kappa = 9/4$.
chapters/examples/kac_moody.tex:4121:Compare $\mathfrak{sl}_2$: $\kappa = 3(k+2)/4$ and $F_1 = (k+2)/32$. The ratio $F_1(\mathfrak{sl}_3)/F_1(\mathfrak{sl}_2) = 32(k+3)/(18(k+2))$ is not a universal constant: it reflects the different dimensions and dual Coxeter numbers. What \emph{is} universal is the factorization $F_g = \kappa \cdot \lambda_g$ from the genus universality theorem.
chapters/examples/genus_expansions.tex:493:By the genus universality theorem (Theorem~\ref{thm:genus-universality}), the genus-$g$ obstruction class factors as $\mathrm{obs}_g(\cA) = \kappa(\cA) \cdot \lambda_g$ \textup{(}UNIFORM-WEIGHT\textup{)}, where $\lambda_g = c_g(\mathbb{E})$ is the top Chern class of the Hodge bundle on $\overline{\mathcal{M}}_g$. For $\widehat{\mathfrak{sl}}_{2,k}$, the genus-1 curvature computation (Theorem~\ref{thm:sl2-genus1-curvature}) gives $\kappa = 3(k+2)/4$.
chapters/examples/genus_expansions.tex:503:Substituting $\kappa = 3(k+2)/4$ yields~\eqref{eq:sl2-Fg}.
chapters/examples/genus_expansions.tex:1077:\kappa \cdot \lambda_2$ with $\kappa = 3(k+2)/4$ is
chapters/examples/genus_expansions.tex:1187:\item \emph{Two-channel curvature.} $\kappa = 3(k+2)/4$ receives contributions from both the double-pole channel ($\propto k$) and the simple-pole channel ($\propto h^\vee$). For the Heisenberg, only the double-pole is active.
chapters/examples/genus_expansions.tex:1727:$\kappa = 3(k+2)/4$ to $\kappa' = -\kappa$. Since
chapters/examples/genus_expansions.tex:1898:using $(2^{2g}-2)/2^{2g} = (2^{2g-1}-1)/2^{2g-1}$. Multiplying by $\kappa = 3(k+2)/4$ gives~\eqref{eq:generating-function}. The radius of convergence is $|x| = 2\pi$, the first zero of $\sin(x/2)$.
chapters/examples/genus_expansions.tex:1933:Proposition~\ref{prop:complementarity-genus-series} is the specialization $\kappa = 3(k+2)/4$ (the $\widehat{\mathfrak{sl}}_2$ value from the Master Table). The all-genera generating function applies to all modular Koszul algebras on the uniform-weight lane: Heisenberg ($\kappa = k$), affine Kac--Moody, and Virasoro ($\kappa = c/2$). For multi-weight algebras such as $\mathcal{W}_N$ ($N \geq 3$, $\kappa = c(H_N - 1)$), the genus-$1$ clause $F_1 = \kappa/24$ is unconditional; at $g \geq 2$ the scalar formula receives a cross-channel correction $\delta F_g^{\mathrm{cross}}$ from mixed-channel boundary graphs (Theorem~\ref{thm:multi-weight-genus-expansion}, resolving Open Problem~\ref{op:multi-generator-universality} negatively).
chapters/theory/higher_genus_modular_koszul.tex:34025:$\kappa = 3(k+2)/4$
chapters/connections/frontier_modular_holography_platonic.tex:2774:$\kappa = 3(k+2)/4$.
chapters/theory/e1_modular_koszul.tex:1107:$\kappa = 3(k+2)/4$.
chapters/theory/ordered_associative_chiral_kd.tex:8422:$\av_2$ is $\kappa = 3(k+2)/4$ (equation~\eqref{eq:sl2-kappa}),
chapters/theory/ordered_associative_chiral_kd.tex:11356:\item $\kappa = 3(k+2)/4 = 0$: the bar complex is uncurved.

thinking
**Considering label addition**

I’m thinking maybe I should add a label to the equation in the higher_genus_modular_koszul section around line 34025. It's a good idea to inspect that area closely to see if it makes sense or if it will improve clarity. It seems like a small change, but it could really enhance understanding! So, I'll take a moment to evaluate the surrounding lines and decide on the best approach to implement this addition.
exec
/bin/zsh -lc "sed -n '34020,34028p' chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\begin{remark}[The symmetric shadow at genus~$2$]
\label{rem:g2-shadow}
The averaging map $\av_2$ at degree~$2$ sends the
$12$-dimensional ordered de~Rham cohomology to
$\Sigma_2$-coinvariants. The scalar surviving $\av_2$ is
$\kappa = 3(k+2)/4$
(equation~\eqref{comp:sl2-kappa}), the same value as at
genus~$0$ and genus~$1$: the averaging map is a local
computation (residue extraction), independent of the global

thinking
**Fixing document labels**

I notice there's an issue with line 34026; I need to remove the `equation\eqref{comp:sl2-kappa}` but keep the inline formula instead. That seems like the best approach. Then, for the landscape census in line 2520, I'll look for the `eq:riordan-recurrence-explicit` label and check for any existing similar labels. It’s important to keep everything consistent and clear, so I’ll make sure both fixes are implemented properly.
exec
/bin/zsh -lc "rg -n 'riordan recurrence|label\\{eq:.*riordan.*\\}|modified Riordan' chapters -g '*.tex' | sed -n '1,160p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/bar_complex_tables.tex:4152:We record this as the \emph{modified Riordan} generating function.
chapters/examples/bar_complex_tables.tex:4184:modified Riordan &
chapters/examples/landscape_census.tex:2145:\begin{equation}\label{eq:gf-sl2-riordan}
chapters/theory/computational_methods.tex:810: & modified Riordan \\
exec
/bin/zsh -lc "sed -n '2138,2150p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\emph{rational} (Remark~\ref{rem:garland-lepowsky-sl2}):
\begin{equation}\label{eq:gf-sl2-rational}
P_{\widehat{\mathfrak{sl}}_2}(x)
 \;=\; \frac{x(3-x)}{(1-x)^2}
 \;=\; \sum_{n \geq 1}(2n+1)\,x^n,
\end{equation}
superseding the original Riordan prediction
\begin{equation}\label{eq:gf-sl2-riordan}
P_{\widehat{\mathfrak{sl}}_2}(x)
 \stackrel{\times}{=} \frac{1 + x - \sqrt{1 - 2x - 3x^2}}{2x(1+x)}
\end{equation}
which yields $\dim(\widehat{\mathfrak{sl}}_2^!)_2 = 6$, conflicting
with the proved value $\dim H^2 = 5$

thinking
**Evaluating recurrence equation options**

I’m thinking about line 2520 and wondering if the recurrence equation should be `eq:gf-sl2-riordan`. But maybe there's another equation that fits better. I’ll need to take a look around line 2508 to see what’s happening there. It’s interesting to consider different options for these equations! I'll just make sure I'm checking all possibilities to get it right.
exec
/bin/zsh -lc "sed -n '2512,2524p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
\qquad
\operatorname{Spec}(T_{\mathrm{rec}}) = \{3, -1\},
\]
recovers the discriminant:
$\det(1 - x\, T_{\mathrm{rec}}) = (1-3x)(1+x) = \Delta(x)$.
\end{proposition}

\begin{proof}
The recurrence~\eqref{eq:riordan-recurrence-explicit} is
verified by direct computation from the Riordan generating
function (Theorem~\ref{thm:ds-bar-gf-discriminant}).
The Picard--Fuchs operator~$L$ is obtained by differentiating
the algebraic equation

thinking
**Searching for recurrence labels**

I’m thinking I need to find an actual recurrence equation label. It seems like searching for something labeled "recurrence" would help. This might clarify things more specifically. I'll focus on that and see if I can find the right information related to recurrence equations. I want to ensure I get this right so that I can provide useful details later.
exec
/bin/zsh -lc "rg -n 'label\\{eq:.*recurrence.*\\}|a_n =|a_{n\\+2}' chapters/examples/landscape_census.tex -g '*.tex' | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
rg: regex parse error:
    (?:label\{eq:.*recurrence.*\}|a_n =|a_{n\+2})
                                           ^
error: repetition quantifier expects a valid decimal
exec
/bin/zsh -lc "rg -n -F 'label{eq:' chapters/examples/landscape_census.tex | rg 'recurrence|riordan|molien|sl2'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
2139:\begin{equation}\label{eq:gf-sl2-rational}
2145:\begin{equation}\label{eq:gf-sl2-riordan}
2476:\begin{equation}\label{eq:sl2-bar-recurrence-corrected}
2592:\begin{equation}\label{eq:sl3-bar-recurrence}
exec
/bin/zsh -lc "sed -n '2472,2484p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
\index{Picard--Fuchs equation!bar cohomology}
For $\mathfrak{g} = \mathfrak{sl}_2$, the corrected bar
cohomology dimension sequence $a_n = 2n+1$ satisfies
the recurrence of order~$1$:
\begin{equation}\label{eq:sl2-bar-recurrence-corrected}
a_n \;=\; a_{n-1} + 2,
\qquad a_1 = 3.
\end{equation}
\textup{(}The original Riordan prediction $a_n = R(n+3)$
with recurrence
$(n+1)\, a_n = (2n{-}2)\, a_{n-1} + (3n{-}6)\, a_{n-2}$
is superseded; see Remark~\textup{\ref{rem:garland-lepowsky-sl2}}.\textup{)}
The rational generating function

thinking
**Clarifying recurrence equations**

I'm wondering if I should fix `eqref` to `eq:sl2-bar-recurrence-corrected` or `eq:gf-sl2-riordan`. The sentence mentions a recurrence as verified by direct computation from the Riordan generating function within a proposition about the Picard-Fuchs operator. I think this recurrence might relate to the current recurrence matrix `T_rec` with eigenvalues 3 and -1. I'll need to look for more context about this, particularly around lines 2484-2508.
exec
/bin/zsh -lc "sed -n '2484,2516p' chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
The rational generating function
$P(x) = x(3-x)/(1-x)^2$ is annihilated by the
first-order operator
$\widetilde{L} = (1-x)^2 \partial_x - (3-2x)$,
but the \emph{discriminant} $\Delta(x) = (1-3x)(1+x)$
of the DS reduction
(Theorem~\ref{thm:ds-bar-gf-discriminant})
still governs the Virasoro and $\beta\gamma$ generating
functions. The Picard--Fuchs $D$-module
$\mathcal{M}_{\mathfrak{sl}_2}
:= D_{\mathbb{A}^1} / D_{\mathbb{A}^1} \cdot L$,
where $L = (1 - 2x - 3x^2)\partial_x^2
+ (-1 + 3x)\partial_x + 1$
is the differential operator annihilating the
\emph{original} Riordan generating function
(retained here as it controls the DS-shared discriminant),
provides the canonical construction:
\[
H^{\mathrm{red}}_1(\widehat{\mathfrak{sl}}_2)
\;:=\; \mathcal{M}_{\mathfrak{sl}_2}\big|_{x=0}

thinking
**Addressing recurrence labeling**

I'm looking into the original Riordan recurrence. It seems there’s no labeled equation for it. I could add a label to the displayed recurrence at line 2480. The text isn't currently displayed as labeled, so I could fix this by changing `\eqref{eq:riordan-recurrence-explicit}` to something like `the original Riordan recurrence $(n+1)a_n = ...$ from \eqref{eq:gf-sl2-riordan}`. A simpler option is to just say `the original Riordan recurrence displayed above`. 

I also need to verify the label for `eq:molien-weyl-g` at line 2564, perhaps search for `eq:molien-weyl-bar`.
exec
/bin/zsh -lc "rg -n 'Molien|Weyl|label\\{eq:.*molien|series~\\\\eqref\\{eq:molien-weyl-g\\}' chapters/examples/landscape_census.tex chapters -g '*.tex' | sed -n '1,140p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/landscape_census.tex:2563:couples the Casimir eigenspace structure to the Molien--Weyl
chapters/examples/landscape_census.tex:2564:series~\eqref{eq:molien-weyl-g}, which has $r$~independent
chapters/examples/w_algebras_deep.tex:111:\text{Normal ordering} &\leftrightarrow \text{Weyl quantization}
chapters/examples/w_algebras_deep.tex:348:where $\rho = (\alpha_1 + \alpha_2)/2$ is the Weyl vector. The
chapters/examples/w_algebras_deep.tex:1541:duality (Weyl group representations of dual type).
chapters/examples/lattice_foundations.tex:665:have the same graded character: the level-$1$ Weyl--Kac character
chapters/examples/lattice_foundations.tex:851:since both adjacent pairs have inner product $-1$. Since $e^0 = \mathbf{1}$ lies in the augmentation (i.e., $[\mathbf{1}] = 0$ in the reduced bar complex $\bar{B} = B/\mathbb{C}\cdot\mathbf{1}$), this element is a \emph{cycle}, not an exact element. It realizes the Weyl group relation $s_{\alpha_1} s_{\alpha_2} s_{\alpha_1} = s_{\alpha_2} s_{\alpha_1} s_{\alpha_2}$ as a homology class in the bar complex.
chapters/examples/lattice_foundations.tex:868:The $D_4$ root lattice has 24 roots, all of the form $\pm e_i \pm e_j$ ($i \neq j$). These form a single orbit under the Weyl group $W(D_4)$. The outer automorphism group $\operatorname{Out}(D_4) \cong S_3$ acts as graph automorphisms of the $D_4$ Dynkin diagram, permuting the three ``legs'' and hence permuting the three nontrivial cosets of $D_4^*/D_4 \cong (\mathbb{Z}/2\mathbb{Z})^2$ (vector, spinor, and conjugate spinor representations). Note: the spinor and conjugate spinor vectors lie in $D_4^* \setminus D_4$, not in the root lattice itself.
chapters/examples/beta_gamma.tex:490:For $\mathcal{F}$: The dual of the Clifford relation $b \boxtimes c + c \boxtimes b$ is the Weyl/symplectic
chapters/examples/beta_gamma.tex:493:For $\beta\gamma$: The dual of the Weyl pairing is the Clifford relation, recovering $\mathcal{F}$.
chapters/examples/free_fields.tex:1572:The higher operations encode the Weyl group action.
chapters/examples/free_fields.tex:1588:\emph{Weyl group action.}
chapters/examples/free_fields.tex:1589:The Weyl group $W(A_2) \cong S_3$ acts on the lattice, permuting the roots $\{\alpha_1, \alpha_2, -\alpha_1-\alpha_2\}$. The bar complex is $W$-equivariant: the simple reflections $s_1, s_2$ act on bar complex elements by permuting lattice labels and adjusting cocycle signs. The higher $A_\infty$ operations $m_k$ for $k \geq 3$ arise from residues at higher collision strata and encode the relations in the Weyl group presentation $\langle s_1, s_2 \mid s_i^2 = 1,\, (s_1 s_2)^3 = 1 \rangle$.
chapters/examples/free_fields.tex:1683:The relations $R_{bc} \perp R_{\beta\gamma}$ under the residue pairing: the Clifford relation of the $bc$ system is orthogonal to the Weyl relation of the $\beta\gamma$ system.
chapters/examples/free_fields.tex:1689:The quadratic relations are $R_{bc} = b \otimes c + c \otimes b$ (Clifford/symmetric) and $R_{\beta\gamma} = \beta \otimes \gamma - \gamma \otimes \beta$ (Weyl/antisymmetric).
chapters/examples/free_fields.tex:3541:\begin{remark}[The Weyl group as non-abelian Poisson summation]
chapters/examples/free_fields.tex:3543:\index{Weyl group!as Fourier symmetry}
chapters/examples/free_fields.tex:3545:The Weyl--Kac character formula
chapters/examples/free_fields.tex:3553:admissible Weyl packet on the worked $\widehat{\mathfrak{sl}}_2$
chapters/examples/free_fields.tex:5203:The genus-$1$ bar complex transforms covariantly under $\mathrm{SL}_2(\mathbb{Z})$ with weight $c/24$ (Theorem~\ref{thm:modular-invariance}). Modular invariance of the full partition function requires the left-right central charge difference $c - \tilde{c} = 0 \bmod 24$ (for single-valuedness of the phase $e^{2\pi i (c-\tilde{c})/24}$). For the bosonic string ($c = \tilde{c} = 26$) and the superstring ($c = \tilde{c} = 15$), conformal anomaly cancellation arises from Weyl invariance on the worldsheet, not from $c \bmod 24$ alone. This is the Belavin--Knizhnik theorem \cite{BK86}; see also Polchinski \cite[Ch.~5]{Pol98} for the standard textbook treatment.
context compacted
ERROR: You've hit your usage limit. Visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 9:35 PM.
tokens used
371,136
