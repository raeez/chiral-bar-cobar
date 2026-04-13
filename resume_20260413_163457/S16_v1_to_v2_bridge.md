# S16_v1_to_v2_bridge (831s)

- [CRITICAL] `chapters/connections/log_ht_monodromy_core.tex:1903` — PROBLEM: the affine lambda-bracket is Laplace-transformed to `\Omega/z + k\kappa_\fg/z^2`. That is wrong twice: the Laplace kernel of `\{J^a{}_\lambda J^b\}=f^{ab}{}_cJ^c+k\kappa^{ab}\lambda` is `f^{ab}{}_cJ^c/z + k\kappa^{ab}/z^2`, and the Casimir residue `k\,\Omega/z` appears only after the `d\log` absorption / evaluation-module reduction. The file even self-corrects at line 1914. FIX: replace the display by `r^{\mathrm{Lap}}(z)=f^{ab}{}_cJ^c/z+k\,\kappa_\fg^{ab}/z^2`, rename it `r^{\mathrm{Lap}}`, and then state separately: `after bar-kernel absorption and passage to the collision residue, the braiding is governed by r^{\mathrm{KM}}(z)=k\,\Omega/z`.

- [CRITICAL] `chapters/connections/3d_gravity.tex:8322` — PROBLEM: this table still identifies the Virasoro shadow coefficient with the lambda-bracket coefficient by writing `S_2=c/12`; the row at line 8334 repeats the same error. Earlier in the same active chapter `S_2=\kappa=c/2` is already used. FIX: replace the sentence by `the entries for r=2,3 are the low-degree shadow data S_2=\kappa=c/2 and S_3=-c; c/12 is only the divided-power coefficient of \lambda^3 in \{T_\lambda T\}` and change the `r=2` row from `c/12` to `c/2` in both columns.

- [HIGH] `chapters/connections/ordered_associative_chiral_kd_core.tex:1274` — PROBLEM: Vol I’s five main theorems are described as an `E_\infty` package. That is stale hierarchy language and contradicts Vol I’s live ordered `E_1` A–H package. FIX: replace the opening sentence with: `Volume~I establishes five main theorems for augmented chiral algebras on curves and also proves their ordered ($E_1$) variants at all genera; the genus-zero ordered statements collected here are the local ordered face of that package.` Also replace `leading coefficient` with `modular characteristic`.

- [HIGH] `chapters/theory/introduction.tex:143` — PROBLEM: Theorem D is imported as `d_{\barB}^2=\kappa\cdot\omega_g`; the same false formula recurs at line 535. Vol I’s live source separates the square-zero bar differential from the fiberwise genus correction. FIX: in both places replace `d_{\barB}^2 = ...` by `d_{\mathrm{fib}}^{\,2} = \kappa(\cA)\cdot\omega_g`, and add one clause that the underlying bar differential remains square-zero.

- [HIGH] `chapters/theory/foundations.tex:2192` — PROBLEM: the foundations chapter states that the bar differential squares to `\kappa(\cA)\cdot\omega_g`; the same error is built into the local definition at lines 2208–2225 and the gauge-theory dictionary row at line 2382. FIX: replace the affected formulas by `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g` and rewrite the definition to say the genus-dependent fiberwise differential is curved, while `d_{\barB}^2=0` for the bar differential itself.

- [HIGH] `chapters/connections/spectral-braiding-core.tex:3847` — PROBLEM: the active spectral-braiding chapter repeats the same Vol I drift: `d_{\barB}^2=\kappa(\cA)\cdot\omega_g`; it recurs again at lines 3895–3896 and 3925–3926. FIX: change each occurrence to `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g`, and in the remark at 3925–3926 rewrite `the closed-color component gives ...` as `the closed-color fiberwise component gives ...`.

- [HIGH] `chapters/connections/conclusion.tex:447` — PROBLEM: the conclusion still summarizes the genus correction as `d_{\barB}^2=\kappa(\cA)\cdot\omega_g`; the same seam error reappears at line 1643. FIX: replace both by `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g` and keep the bar differential square-zero.

- [HIGH] `chapters/connections/3d_gravity.tex:9159` — PROBLEM: the gravity climax still states `d_{\barB}^2=\kappa\cdot\omega_1`, with bare `\kappa` on top of the wrong differential. FIX: replace it by `d_{\mathrm{fib}}^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_1`, and carry the same argument into the modular-weight sentence that follows.

- [HIGH] `chapters/connections/3d_gravity.tex:8853` — PROBLEM: the large-`c` asymptotic is still `2/(5c^2)`, off by a factor of `5`. The same chapter already gives the correct `2/c^2` elsewhere. FIX: change `2/(5c^2)` to `2/c^2`.

- [HIGH] `chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1490` — PROBLEM: the split movement file keeps the same wrong asymptotic `S_4\sim 2/(5c^2)`. FIX: change it to `S_4\sim 2/c^2`.

- [MEDIUM] `chapters/connections/spectral-braiding-core.tex:3182` — PROBLEM: the nonzero `\kappa+\kappa^!` statement for `\mathcal W`-algebras is attributed to Vol I Theorem D; that is a complementarity statement, so the citation should be to Theorem C. The same wrong attribution recurs at line 3882. FIX: change both citations from `Vol~I, Theorem~D` to `Vol~I, Theorem~C`, and spell the example with arguments, e.g. `\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13`.

- [MEDIUM] `chapters/connections/holomorphic_topological.tex:808` — PROBLEM: the file defines `\kappa(\widehat{\mathfrak g}_k)` and then immediately drops the argument, writing bare `F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}` and bare `\kappa=\dim(\mathfrak g)/2`; the same bare-`\kappa` drift recurs at line 1250. FIX: write `F_g=\kappa(\widehat{\mathfrak g}_k)\cdot\lambda_g^{\mathrm{FP}}`, and at `k=0` write `\kappa(\widehat{\mathfrak g}_0)=\dim(\mathfrak g)/2`; at line 1250 write `F_g=\kappa(\cA_{\mathrm{Burns}})\cdot\lambda_g^{\mathrm{FP}}`.

- [MEDIUM] `chapters/connections/twisted_holography_quantum_gravity.tex:2745` — PROBLEM: Theorem H is summarized as “the chiral Hochschild cohomology is polynomial in the cumulants.” Vol I’s live theorem says polynomial growth / degree-`2` Hilbert polynomial, not cumulant polynomiality. FIX: replace that item with `Theorem H (chiral Hochschild): on the Koszul locus the Hochschild--Hilbert series is polynomial of degree at most 2, equivalently \ChirHoch^n(\cA)=0 for n\notin\{0,1,2\}; for affine KM one excludes the critical level k=-h^\vee.`

## Summary
Checked: 15 | Findings: 13 | Verdict: FAIL


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
session id: 019d8744-63ff-7bf0-8f9a-ee52ad256857
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


MISSION: SEAM AUDIT between cross-volume and cross-volume.

Vol I→Vol II bridge. Check across ~/chiral-bar-cobar and ~/chiral-bar-cobar-vol2: (a) theorem status claims about Vol I results in Vol II are accurate, (b) formula conventions converted (OPE→lambda-bracket), (c) the E1/E_inf hierarchy (V2-AP1-AP24) is respected, (d) no bare Omega/z or bare kappa in Vol II

Search the relevant files. Read the transition points carefully.
For EVERY inconsistency, mismatch, or gap at the seam:
state the PROBLEM precisely with file:line, then state the EXACT FIX.
mcp startup: no servers



thinking
**Auditing codebase for inconsistencies**

I need to address the user's task of auditing across two volumes, focusing on deep-beilinson-audit and possibly cross-volume-propagation. The user specified they want problems identified at the seam between Vol I and II, without edits. They want a clear statement of each issue and the exact fix. Although I won’t be making changes unless requested, I should still consider all relevant instructions before proceeding, especially regarding mathematical content. It might be helpful to read all associated files.
thinking
**Planning the audit process**

I need to ensure that every claim is backed by the contents of the files I've actually read. It's essential to exhaust the audit surface thoroughly. I should start with a commentary update before diving into any substantial work. Using explorer agents will help me navigate the codebase and search relevant files more efficiently. I'll also consider parallelizing file reads with multi-tool usage. My findings will need to specify exact file and line numbers for each issue, especially at the seam points between volumes.
thinking
**Reviewing file permissions**

I want to confirm that the sandbox allows reading files without needing additional approval. Editing in other directories may require permission, but I believe reading should be fine. I’ll need to inspect and utilize relevant skill files. It makes sense to open the SKILL.md for deep-beilinson-audit, although it seems I might not need to focus on cross-volume-propagation since I'm not editing. I should proceed with a commentary update to keep everything documented.
codex
Using `deep-beilinson-audit` for the seam review, with `multi-path-verify` where formula/status checks need independent confirmation. I’m starting by locating the Vol I and Vol II bridge surfaces, then I’ll read the cited transition text and only report findings I can pin to exact lines.
exec
/bin/zsh -lc "rg -n \"Vol I|Volume I|Vol\\. I|Volume II|Vol\\. II|Theorem [A-H]|thm:|kappa|\\\\Omega/z|Omega/z|lambda-bracket|OPE|E_1|E_\\{1\\}|E_inf|E_\\\\infty|Swiss|SC\\"'^'"\\{ch,top\\}|derived center|bar complex|ordered bar|B\\"'^ord|bare kappa" .' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pwd && rg -n \"Vol I|Volume I|Vol\\. I|Volume II|Vol\\. II|Theorem [A-H]|thm:|kappa|\\\\Omega/z|Omega/z|lambda-bracket|OPE|E_1|E_\\{1\\}|E_inf|E_\\\\infty|Swiss|SC\\"'^'"\\{ch,top\\}|derived center|bar complex|ordered bar|B\\"'^ord|bare kappa" chapters CLAUDE.md metadata/theorem_registry.md chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
---
name: multi-path-verify
description: Use when the user asks to verify a formula, invariant, theorem status, computational claim, or family-specific value in this repository. Best for one claim or a small claim family where independent verification paths matter.
---

# Multi-Path Verify

Use this skill when one claim needs real verification rather than informal confidence.

## State the claim precisely

Write down:

- the exact formula or assertion
- the object or family it refers to
- the convention in force
- the claimed scope

If that statement is still ambiguous, do not verify a blurred version.

 succeeded in 51ms:
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

 exited 2 in 52ms:
rg: regex parse error:
    (?:Vol I|Volume I|Vol\. I|Volume II|Vol\. II|Theorem [A-H]|thm:|kappa|\Omega/z|Omega/z|lambda-bracket|OPE|E_1|E_\{1\}|E_inf|E_\infty|Swiss|SC\^\{ch,top\}|derived center|bar complex|ordered bar|B\^ord|bare kappa)
                                                                          ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
/Users/raeez/chiral-bar-cobar
rg: regex parse error:
    (?:Vol I|Volume I|Vol\. I|Volume II|Vol\. II|Theorem [A-H]|thm:|kappa|\Omega/z|Omega/z|lambda-bracket|OPE|E_1|E_\{1\}|E_inf|E_\infty|Swiss|SC\^\{ch,top\}|derived center|bar complex|ordered bar|B\^ord|bare kappa)
                                                                          ^^
error: unrecognized escape sequence
codex
I’ve loaded the audit workflow and I’m pulling the constitutional surfaces next: `CLAUDE.md`, `concordance.tex`, `theorem_registry.md`, and the red-team summary. After that I’ll isolate the actual Vol I→Vol II bridge files and audit status, convention conversion, hierarchy, and banned bare formulas line by line.
Plan update
Cross-volume seam audit needs the global claim/status surfaces first, then the actual bridge passages, then a second pass for duplicated formula/convention drift.
  → Read global audit surfaces: CLAUDE, concordance, theorem registry, red-team summary
  • Locate Vol I↔Vol II seam files and transition passages referencing Vol I results
  • Audit seam for status accuracy, OPE→lambda conversion, E1/E∞ hierarchy, and forbidden bare formulas
  • Re-verify each candidate finding against exact lines and produce final findings list

thinking
**Searching for relevant sections**

I need to focus on the relevant sections instead of diving into huge files. I could search within those files to pinpoint specific chapters in Volume II that refer back to Volume I. It seems logical to locate those references; I'll make use of commands to search for fixed string groups separately. Alright, let’s run those commands and see what I can find. This way, I'll streamline my search effectively!
exec
/bin/zsh -lc "rg -n \"OPE|lambda-bracket|bare kappa|Omega/z|E_1|E_\\\\infty|E_inf|SC\\"'^'"\\{ch,top\\}|Swiss|derived center|ordered bar|B\\"'^ord|Vol'"\\\\.? I|Volume I|Theorem [A-H]|thm:\" ." in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Volume I" .' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Vol I" .' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"V2-AP1|V2-AP24|OPE|lambda-bracket|bare kappa|Omega/z|E_1|E_\\\\infty|E_inf|SC\\"'^'"\\{ch,top\\}|Swiss|derived center|ordered bar|B\\"'^ord" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Volume I" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Vol I" CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:OPE|lambda-bracket|bare kappa|Omega/z|E_1|E_\infty|E_inf|SC\^\{ch,top\}|Swiss|derived center|ordered bar|B\^ord|Vol\.? I|Volume I|Theorem [A-H]|thm:)
                                                   ^^
error: unrecognized escape sequence
 succeeded in 52ms:
./CLAUDE.md:1:# CLAUDE.md -- Volume II: A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT
./AGENTS.md:1:# AGENTS.md - Volume II: A_infinity Chiral Algebras and 3D Holomorphic-Topological QFT
./AGENTS.md:5:This file is the Codex runtime constitution for Volume II. `CLAUDE.md` may contain a larger anti-pattern atlas, historical archaeology, and Claude-oriented orchestration, but `AGENTS.md` must stand on its own as the always-on operating system for Codex/GPT-5.4 in this repo.
./AGENTS.md:41:Volume I built the categorical logarithm: the bar construction `B(A)` for chiral algebras on curves, with theorems proving existence, inversion, branch structure, leading coefficient, and coefficient ring. Volume II reads that machine in three dimensions.
./main.tex:6:% FONTS: EB Garamond (matching Volume I)
./main.tex:1669:% --- Entries from Volume I (for moved chapters) ---
./working_notes.tex:170:Volume I took a $1$-form and followed where it led: into the
./compute/audit/vol2_mc5_status_sweep.md:96:  2504`: both are analytic-sewing references ("MC5 (Volume I, Theorem
./chapters/examples/rosetta_stone.tex:5:% Volume I: chapters/theory/rosetta_stone.tex
./chapters/examples/rosetta_stone.tex:6:% Volume II: chapters/examples/rosetta_stone.tex
./compute/audit/full_volume_math_catalogue_2026-04-08.md:1:# Full Mathematical Defect Catalogue — Volume II
./compute/audit/full_volume_math_catalogue_2026-04-08.md:6:- live/active Volume II input graph from `main.tex` (`64` active inputs);
./compute/audit/full_volume_math_catalogue_2026-04-08.md:268:The current live Volume II surface is not mathematically converged.
./README.md:3:**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
./README.md:16:## Connection to Volume I
./compute/audit/linear_read_notes.md:1049:   Issue: the W-algebra complementarity sentence said `κ + κ^! = ρ · K (Volume I, Theorem D)`. This was (a) tautological (K := κ + κ^!), (b) used the wrong symbol ρ (should be ϱ if referring to the exponent-sum invariant), and (c) attributed to Theorem D (leading coefficient) instead of Theorem C (complementarity).
./compute/audit/linear_read_notes.md:1050:   Fix: replaced with `κ + κ^!` is generally nonzero for W-algebras (e.g.\ κ + κ^! = 13 for Virasoro; Volume I, Theorem C).
./compute/audit/linear_read_notes.md:14262:## 2026-04-08 — Foundational Mathematical Audit of the Volume II Spine
 succeeded in 52ms:
Total output lines: 606

./AGENTS.md:188:3. the convention bridge: grading, shifts, OPE modes versus lambda-brackets, open/closed colors, genus and degree scope, Vol I versus Vol II versus Vol III normalization;
./AGENTS.md:215:6. propagation surface across Vol I, Vol II, and Vol III when the claim is cross-volume.
./AGENTS.md:221:- Vol I: FRONTIER.md and CLAUDE.md updated with Vol II session results (page count 1,704pp, E_3-top hierarchy, pentagon 10/10, modular operad breakthroughs). Compute surface unchanged.
./AGENTS.md:222:- Vol II: CLEAN working tree. All worktrees pruned. 1,704pp, 0 errors. Session produced 17 theorems, FM58-FM68, AP176-AP182, 25 arXiv papers, ~3,000 lines new content across 20+ files. All committed.
./AGENTS.md:223:- Vol III: Unchanged from prior session.
./AGENTS.md:231:- Vol I `CLAUDE.md`: `AP1` through `AP141` + `B1`-`B85` for the shared formula, status, propagation, and workflow hazards. **B74-B85 (new, 2026-04-13):** formal-series/analytic confusion, chain-vs-cohomology level, abstract-machine non-sequiturs, stale classification lists, Khan-Zeng scope, orbifold route.
./AGENTS.md:232:- Vol II `CLAUDE.md`: `V2-AP1` through `V2-AP39` + `FM58`-`FM68` for the local `E_1/E_infinity` hierarchy, lambda-bracket, standalone, and session-specific hazards.
./AGENTS.md:233:- Vol III `CLAUDE.md`: `AP-CY1` through `AP-CY19` for center discipline, conditionality propagation, CY3 existence boundaries, and cross-volume bridge hazards.
./AGENTS.md:239:These APs arose from the SC adversarial audit and deep mathematical audit sessions. They are load-bearing for Vol II.
./AGENTS.md:439:- Vol I versus Vol II versus Vol III terminology.
./AGENTS.md:495:- grep the active Vol II surface;
./AGENTS.md:558:   Vol I is compute-heavy right now, Vol II is concentrated in perturbative finiteness, and Vol III is concentrated in CY3 compute/test plus bridge exposition. Read these before making cross-volume claims.
./AGENTS.md:602:- Vol II lambda-brackets use divided powers;
./AGENTS.md:605:- `kappa` is family-specific, and in Vol III the subscript is mandatory;
./AGENTS.md:608:- Vol I uses OPE modes, Vol II uses lambda-brackets, Vol III may use motivic or categorical normalizations;
./AGENTS.md:617:- after any load-bearing change, grep active Vol II chapters, appendices, superseded split files, Vol I, Vol III, README, notes, and compute/tests as relevant;
./AGENTS.md:662:### Family F - Vol II Failure Modes (FM40-FM57) And Meta-Patterns (MP1-MP6)
./AGENTS.md:664:These are CRITICAL Vol II-specific errors from the 2026-04-12 session (55+ agents). They compress into three clusters: categorical level errors, factorisation/coproduct conflation, and E_3 overclaiming.
 exited 2 in 50ms:
rg: regex parse error:
    (?:V2-AP1|V2-AP24|OPE|lambda-bracket|bare kappa|Omega/z|E_1|E_\infty|E_inf|SC\^\{ch,top\}|Swiss|derived center|ordered bar|B\^ord)
                                                                  ^^
error: unrecognized escape sequence
 exited 2 in 51ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
archive/raeeznotes/raeeznotes100/red_team_summary.md:4:- Volume I formal claims: **2841**
archive/raeeznotes/raeeznotes100/red_team_summary.md:5:- Volume II formal claims: **2025**
archive/raeeznotes/raeeznotes100/red_team_summary.md:112:- Volume II foundations around Swiss-cheese recognition, PVA descent, FM/AOS cancellation, and bar-cobar rectification look substantially healthier than the speculative connection chapters.
archive/raeeznotes/raeeznotes100/red_team_summary.md:113:- Volume I core theory and the explicitly tagged examples are safer than the high-energy connection/frontier material, but still need local proof verification claim by claim.
chapters/connections/concordance.tex:4625:\index{Volume II!bridges from Volume I}
 exited 2 in 51ms:
rg: raeeznotes/raeeznotes100/red_team_summary.md: No such file or directory (os error 2)
CLAUDE.md:9:Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,704pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,613pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.
CLAUDE.md:21:**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).
CLAUDE.md:63:Vol III default: `\begin{conjecture}` regardless. Label prefix follows environment (AP125).
CLAUDE.md:122:### HZ-7. AP113 (bare kappa in Vol III) -- 3 waves, 165 baseline instances
CLAUDE.md:124:Bare `\kappa` in Vol III is permitted IFF the section begins with a local definition:
CLAUDE.md:187:Three separate cleanup commits in Vol II prove aspirational instructions insufficient. Post-write grep is the only reliable enforcement.
CLAUDE.md:303:- B12. Bare `\kappa` in Vol III. CORRECT: subscripted `\kappa_{ch|cat|BKM|fiber}`. AP113.
CLAUDE.md:304:- B13. `\kappa_{global|BPS|eff|total|naive}` in Vol III. CORRECT: approved set only. AP113.
CLAUDE.md:340:- B34. Duplicate `conj:kappa-bps-universality` across Vol I and Vol III. AP124/FM15.
CLAUDE.md:400:### Vol II Session 2026-04-12/13 Cross-Volume Patterns (B74-B85)
CLAUDE.md:489:**FM30. Lambda-bracket divided-power coefficient conflation.** Opus wrote the lambda-bracket coefficient c/12 where the shadow invariant S_2 = c/2 was required. The lambda-bracket {T_λ T} = (c/12)λ^3 uses divided powers (T_{(3)}T/3! = (c/2)/6 = c/12). Opus confused the PRESENTATION-DEPENDENT coefficient c/12 with the PRESENTATION-INDEPENDENT invariant S_2 = κ = c/2. The error was compounded by writing "which is the Virasoro central charge itself" (c/12 is NOT c). Counter: shadow invariants S_r are NUMBERS (family invariants), not convention-dependent coefficients. S_2 = κ ALWAYS. After writing any S_r value, verify against Vol I census: S_2(Vir) = c/2.
CLAUDE.md:583:**grading/signs** (AP22, AP23, AP44, AP45, AP46, AP49): Desuspension LOWERS: |s^{-1}v|=|v|-1. In LaTeX: ALWAYS s^{-1}, NEVER bare s in bar-complex formula. T^c(s^{-1} A-bar), NOT T^c(s A-bar). Mnemonic: bar=down=desuspension=s^{-1}. eta(q) includes q^{1/24}. OPE mode vs lambda-bracket: T_{(3)}T=c/2 becomes {T_lambda T}=(c/12)*lambda^3 (divided power 1/n!). A-hat(ix)-1 starts at x^2; verify F_1 matches leading order. sqrt(Q_L) is flat section; H(t)=t^2*sqrt(Q_L) NOT horizontal. Cross-volume conventions: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic. NEVER paste without conversion.
CLAUDE.md:718:**PE-5. Vol III kappa write** (AP113)
CLAUDE.md:723:## PRE-EDIT: Vol III kappa
CLAUDE.md:727:census citation:           Vol III landscape_census_cy.tex:LINE
CLAUDE.md:745:  Vol I matches:           [N]
CLAUDE.md:746:  Vol II matches:          [N]
CLAUDE.md:747:  Vol III matches:         [N]
CLAUDE.md:762:Vol I grep:                [hits, canonical form]
codex
I’ve got the global hazard map. Next pass is constrained to active manuscript files in Vol II that explicitly bridge to Vol I, so I can separate live seam defects from stale audit notes or compute comments.
exec
/bin/zsh -lc 'rg -n -F "Volume I" chapters README.md main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Vol I" chapters README.md main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
README.md:3:**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
README.md:16:## Connection to Volume I
main.tex:6:% FONTS: EB Garamond (matching Volume I)
main.tex:1669:% --- Entries from Volume I (for moved chapters) ---
chapters/examples/rosetta_stone.tex:5:% Volume I: chapters/theory/rosetta_stone.tex
chapters/examples/rosetta_stone.tex:6:% Volume II: chapters/examples/rosetta_stone.tex
 succeeded in 51ms:
main.tex:57:% Cross-volume label import from Vol I (V1- prefix on all cross-refs)
main.tex:58:% Uses flat export: run python3 scripts/export_vol1_xrefs.py in Vol I
main.tex:59:% to regenerate ../chiral-bar-cobar/vol1-xrefs.aux after each Vol I build.
main.tex:76:% THEOREM ENVIRONMENTS (Garamond style, matching Vol I)
main.tex:101:% Claim provenance tags (matching Vol I)
main.tex:225:% Compatibility with Vol I notation in moved chapters
main.tex:270:% Operads (sans-serif, matching Vol I convention)
main.tex:350:% Bar-cobar (matching Vol I)
main.tex:368:% Differentials (matching Vol I notation)
main.tex:376:% MODULAR GRAPH VISUAL CALCULUS (matching Vol I)
main.tex:409:% Cross-volume phantom labels (Vol I references)
main.tex:411:% from chapters that were migrated from Vol I to Vol II.
main.tex:412:% The xr-hyper/externaldocument mechanism requires Vol I to be
main.tex:685:% Internal phantom labels: Vol I labels referenced without V1- prefix
main.tex:686:% These are cross-volume references to Vol I theorems/definitions
main.tex:687:% that appear in Vol II text without the V1- prefix.
main.tex:2221:%% ---- Vol II Seven Faces missing bibitems (Batch 7b coverage) ----
README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
README.md:18:Every chapter depends on Vol I's five theorems:
README.md:20:| Vol I Theorem | What it supplies |
exec
/bin/zsh -lc 'rg -n -F "Theorem D" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Theorem A" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Theorem C" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Theorem B" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:1278:\index{five main theorems!E1@$E_1$ variant!Theorem A}
chapters/connections/concordance.tex:137:Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
chapters/connections/ordered_associative_chiral_kd.tex:1220:\index{five main theorems!E1@$E_1$ variant!Theorem A}
chapters/connections/twisted_holography_quantum_gravity.tex:2736:\item \textbf{Theorem A} (bar-cobar adjunction): $D_\cA$ defines
 succeeded in 51ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:1327:\index{five main theorems!E1@$E_1$ variant!Theorem D}
chapters/connections/ordered_associative_chiral_kd.tex:1269:\index{five main theorems!E1@$E_1$ variant!Theorem D}
chapters/connections/twisted_holography_quantum_gravity.tex:2742:\item \textbf{Theorem D} (modular characteristic): the first
 succeeded in 50ms:
chapters/connections/ordered_associative_chiral_kd.tex:1252:\index{five main theorems!E1@$E_1$ variant!Theorem C}
chapters/connections/twisted_holography_quantum_gravity.tex:2740:\item \textbf{Theorem C} (complementarity): the cumulant
chapters/connections/ordered_associative_chiral_kd_core.tex:1310:\index{five main theorems!E1@$E_1$ variant!Theorem C}
 succeeded in 50ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:1293:\index{five main theorems!E1@$E_1$ variant!Theorem B}
chapters/connections/ordered_associative_chiral_kd.tex:1235:\index{five main theorems!E1@$E_1$ variant!Theorem B}
chapters/connections/twisted_holography_quantum_gravity.tex:2738:\item \textbf{Theorem B} (bar-cobar inversion): the cumulant

thinking
**Searching for references**

I need to open the README and look at specific chapters, particularly in Vol II. I'll check if there are connections in the concordance.tex file, and it seems like I should actively search for relevant information. Identifying the seams is essential, so I'll search for references like `V1-` and look for bare theorem references. It's important to focus on the exact transition points around the theorem package summary while searching for `V1-`.
exec
/bin/zsh -lc 'rg -n -F "kappa" chapters/connections chapters/theory chapters/examples README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "V1-" chapters README.md main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Vol I" chapters/connections README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Omega/z" chapters/connections chapters/theory chapters/examples README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"\\\\Omega/z\" chapters/connections chapters/theory chapters/examples README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "lambda" chapters/connections chapters/theory chapters/examples README.md' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
Total output lines: 3380

README.md:25:| **(D)** Modular characteristic | Curvature kappa(A) * omega_g governs curved A_infinity structure at genus >= 1 |
chapters/examples/w-algebras-stable.tex:308:$d^2_{\mathrm{fib}} = \kappa(\mathrm{Vir}_c) \cdot \omega_g$
chapters/examples/w-algebras-stable.tex:840:Here $K_{\mathcal{W}_N} = \kappa + \kappa^! = (H_N - 1)\alpha_N$
chapters/examples/w-algebras-stable.tex:854:K_N \;:=\; \kappa(\mathcal{W}_{N,c})
chapters/examples/w-algebras-stable.tex:855: + \kappa(\mathcal{W}_{N,\alpha_N - c})
chapters/examples/w-algebras-stable.tex:867:$\kappa(\mathcal{W}_{N,c}) = c\,(H_N - 1)$, where $H_N - 1
chapters/examples/w-algebras-stable.tex:872:$\kappa(\mathcal{W}_{N,\alpha_N - c}) = (\alpha_N - c)(H_N - 1)$.
chapters/examples/w-algebras-stable.tex:896:the curvature $\kappa(\cW_{N,c^*}) = c^*(H_N - 1)
chapters/examples/w-algebras-stable.tex:898:= \tfrac{1}{2}\kappa(\cW_{N,\alpha_N})$.
chapters/examples/w-algebras-stable.tex:900:$F_1 = \kappa \cdot \lambda_1^{\mathrm{FP}}$ holds
chapters/examples/w-algebras-stable.tex:904:scalar formula $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$
chapters/examples/w-algebras-stable.tex:1237:$\kappa + \kappa^! = 0$. For $\mathcal{W}_N$,
chapters/examples/w-algebras-stable.tex:1239:$\kappa(\mathcal{W}_{N,c}) + \kappa(\mathcal{W}_{N,c}^!)
chapters/examples/w-algebras-stable.tex:1284: $h_{ss} = \kappa_c + \delta_s$ where $\delta_s$ depends on
chapters/examples/w-algebras-stable.tex:1293: Hessian: $1 \times 1$, the scalar $\kappa_c$.
chapters/examples/w-algebras-stable.tex:1298: $\kappa_c$ and $\kappa_c + 48/(5c+22)$.
chapters/examples/w-algebras-w3.tex:1242:$\kappa + \kappa^! = 0$. For $\mathcal{W}_N$,
chapters/examples/w-algebras-w3.tex:1244:$\kappa(\mathcal{W}_{N,c}) + \kappa(\mathcal{W}_{N,c}^!)
 succeeded in 50ms:
Total output lines: 1724

main.tex:57:% Cross-volume label import from Vol I (V1- prefix on all cross-refs)
main.tex:61:\externaldocument[V1-]{../chiral-bar-cobar/vol1-xrefs}
main.tex:410:% These provide target anchors for \ref{V1-...} cross-references
main.tex:415:\phantomsection\label{V1-chap:concordance}%
main.tex:416:\phantomsection\label{V1-chap:yangians}%
main.tex:417:\phantomsection\label{V1-comp:holographic-ss-vir}%
main.tex:418:\phantomsection\label{V1-comp:thqg-I-hs-fermion}%
main.tex:419:\phantomsection\label{V1-comp:thqg-I-hs-heisenberg}%
main.tex:420:\phantomsection\label{V1-comp:thqg-V-affine-yangian}%
main.tex:421:\phantomsection\label{V1-comp:vir-physical-cc}%
main.tex:422:\phantomsection\label{V1-conj:master-bv-brst}%
main.tex:423:\phantomsection\label{V1-constr:beta-map}%
main.tex:424:\phantomsection\label{V1-constr:bordered-fm}%
main.tex:425:\phantomsection\label{V1-constr:clifford-spectral}%
main.tex:426:\phantomsection\label{V1-constr:htt-alg}%
main.tex:427:\phantomsection\label{V1-constr:nms-sewing-product}%
main.tex:428:\phantomsection\label{V1-constr:thqg-oc-mc-element}%
main.tex:429:\phantomsection\label{V1-conv:bar-coalgebra-identity}%
 succeeded in 51ms:
README.md:6:The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
README.md:18:Every chapter depends on Vol I's five theorems:
README.md:20:| Vol I Theorem | What it supplies |
README.md:56:# Build Vol II
README.md:60:# Build Vol I (dependency)
chapters/connections/conclusion.tex:2163:%% Cross-volume forward references (Vol I, planned)
chapters/connections/dnp_identification_master.tex:2:% Vol II Master Chapter: The seven faces of r(z) in 3d HT QFT
chapters/connections/dnp_identification_master.tex:4:% This chapter is the Vol II centerpiece of the seven-face programme.
chapters/connections/thqg_bv_ht_extensions.tex:1617:Proved (Thm A, Vol I) \\
chapters/connections/thqg_bv_ht_extensions.tex:1649:Proved (Vol I, all families) \\
chapters/connections/thqg_bv_construction_extensions.tex:7:% higher_genus_modular_koszul.tex (Vol I, modular bar).
chapters/connections/ht_bulk_boundary_line_frontier.tex:1065:\index{Lagrangian!self-intersection!recovering Vol I}
 succeeded in 51ms:
chapters/connections/thqg_celestial_holography_extensions.tex:2439:$r_{\mathrm{BF}}(z)=k_{\mathrm{BF}}\,\Omega/z$ satisfies the classical Yang--Baxter equation
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
chapters/theory/introduction.tex:1529:$\alpha_T^{\mathrm{mix}} = k\,\Omega/z$, the level-weighted split Casimir; the
chapters/theory/introduction.tex:1532:for $r(z) = k\,\Omega/z$.
chapters/theory/introduction.tex:2027: $k\,\Omega/z$ &
chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
chapters/examples/examples-worked.tex:3441:  via the collision residue $r(z) = k\,\Omega/z$.
chapters/examples/examples-worked.tex:3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
chapters/examples/examples-worked.tex:3687:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
chapters/examples/examples-worked.tex:4689:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
chapters/connections/spectral-braiding-core.tex:11:The Yangian $Y(\fg)$ is the universal quantization of the classical $r$-matrix $r(z) = k\,\Omega/z$. Yet the RTT formalism that defines it treats the spectral parameter $z$ as a formal variable, the Hopf coproduct as a given axiom, and the Yang--Baxter equation as a constraint to be verified. None of these are \emph{explained}: the spectral parameter has no geometric origin, the Hopf coproduct has no universal property, and the YBE is an identity without a cause.
chapters/connections/spectral-braiding-core.tex:48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
chapters/connections/spectral-braiding-core.tex:413:The classical $r$-matrix $r(z) = k\,\Omega/z$ extracted from collision
chapters/connections/spectral-braiding-core.tex:562:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
chapters/connections/spectral-braiding-core.tex:777:$r(z) = k\,\Omega/z$ has mode components
chapters/connections/spectral-braiding-core.tex:791:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
chapters/connections/spectral-braiding-core.tex:809:$r(z) = k\,\kappa^{IJ}\,z^{-1} = k\,\Omega/z$;
chapters/connections/spectral-braiding-core.tex:813:$r(z) = k\,\Omega/z$ has a single Laurent
chapters/connections/spectral-braiding-core.tex:920:the $r(z) = k\,\Omega/z$ has no further poles, and the
 succeeded in 51ms:
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
chapters/connections/thqg_celestial_holography_extensions.tex:2439:$r_{\mathrm{BF}}(z)=k_{\mathrm{BF}}\,\Omega/z$ satisfies the classical Yang--Baxter equation
chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
chapters/examples/examples-worked.tex:3441:  via the collision residue $r(z) = k\,\Omega/z$.
chapters/examples/examples-worked.tex:3470:classical limit: $r(z) = k\,\Omega/z$ is the classical
chapters/examples/examples-worked.tex:3687:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
chapters/examples/examples-worked.tex:4689:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
chapters/examples/examples-complete.tex:722:$k\,\delta^{ab}/z^2$ gives, after $d\log$ absorption, the collision $r$-matrix $r(z) = k\,\Omega/z$, the standard rational
chapters/connections/spectral-braiding-core.tex:11:The Yangian $Y(\fg)$ is the universal quantization of the classical $r$-matrix $r(z) = k\,\Omega/z$. Yet the RTT formalism that defines it treats the spectral parameter $z$ as a formal variable, the Hopf coproduct as a given axiom, and the Yang--Baxter equation as a constraint to be verified. None of these are \emph{explained}: the spectral parameter has no geometric origin, the Hopf coproduct has no universal property, and the YBE is an identity without a cause.
chapters/connections/spectral-braiding-core.tex:48:For $V_k(\mathfrak{sl}_2)$, the collision residue is $r(z) = k\,\Omega/z$, where $\Omega = \sum e_a \otimes e^a \in \mathfrak{sl}_2 \otimes \mathfrak{sl}_2$ is the Casimir tensor. Again $k=0$ gives $r=0$. At leading order, $R(z) = 1 + \hbar\, k\,\Omega/z + \cdots$ is the Yang $R$-matrix. The YBE at order $\hbar^2$ reduces to the infinitesimal braid relation $[\Omega_{12},\, \Omega_{13} + \Omega_{23}] = 0$, which is the Jacobi identity on $\mathfrak{sl}_2$. This is class~L: depth $1$, the $r$-matrix carries non-trivial Lie structure, but the twisted coproduct $\Delta_z$ on the Koszul dual is still cocommutative at the classical level.
chapters/connections/spectral-braiding-core.tex:413:The classical $r$-matrix $r(z) = k\,\Omega/z$ extracted from collision
chapters/connections/spectral-braiding-core.tex:562:\item \emph{vanishing check : $k = 0$ collapse.} At level $k = 0$ (the abelian limit) the level-stripped $r$-matrix $r(z) = k\,\Omega/z$ of Heisenberg and affine type vanishes identically, hence $R(z;u) = \id$ for all $u$ and all $z$. The meromorphic braided category $(\cC_\partial, \otimes_z, R(z))$ then degenerates to the symmetric monoidal category $(\cC_\partial, \otimes, \tau)$ with trivial flip $\tau$: no meromorphic dependence on $z$ survives, and the braiding hexagon reduces to the symmetric-monoidal coherence. This is the vanishing check (``after writing any $R$-matrix, verify $k=0 \Rightarrow r = 0$'') applied at the categorical level.
chapters/connections/spectral-braiding-core.tex:777:$r(z) = k\,\Omega/z$ has mode components
chapters/connections/spectral-braiding-core.tex:791:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
chapters/connections/spectral-braiding-core.tex:809:$r(z) = k\,\kappa^{IJ}\,z^{-1} = k\,\Omega/z$;
chapters/connections/spectral-braiding-core.tex:813:$r(z) = k\,\Omega/z$ has a single Laurent
chapters/connections/spectral-braiding-core.tex:920:the $r(z) = k\,\Omega/z$ has no further poles, and the
chapters/connections/spectral-braiding-core.tex:1228: $r(z) = k\,\Omega/z$ acquires additional poles under DS
chapters/connections/spectral-braiding-core.tex:1439:$r(z) = k\,\Omega/z$, one computes
 succeeded in 51ms:
Total output lines: 3874

README.md:35:- **VI. Three-Dimensional Quantum Gravity**: The climax; Virasoro lambda-bracket generates the full gravitational theory; critical string dichotomy c=26 vs c!=26
chapters/examples/w-algebras-stable.tex:11:Let $\mathcal{V} = \Sym(\C[\partial]\langle \phi^i \rangle)$ be a freely generated Poisson vertex algebra with generators $\phi^i$ of conformal spins $s_i$. The $\lambda$-bracket
chapters/examples/w-algebras-stable.tex:13:\{\phi^i{}_\lambda \phi^j\} = \sum_{n \geq 0} \Pi^{ij}_n \lambda^n, \quad \Pi^{ij}_n \in \mathcal{V},
chapters/examples/w-algebras-stable.tex:29:where $\Pi^{ij}(\partial) = \sum_n \Pi^{ij}_n \partial^n$ is the differential operator encoding the $\lambda$-bracket.
chapters/examples/w-algebras-stable.tex:72:The Virasoro Poisson vertex algebra is generated by a single field $T$ of spin 2 (the stress tensor) with $\lambda$-bracket
chapters/examples/w-algebras-stable.tex:74:% label removed: eq:vir-lambda-bracket
chapters/examples/w-algebras-stable.tex:75:\{T_\lambda T\} = \partial T + 2T\lambda + \frac{c}{12}\lambda^3.
chapters/examples/w-algebras-stable.tex:80:The $\lambda^3$ term arises from the Schwarzian derivative in the transformation law
chapters/examples/w-algebras-stable.tex:115:We verify $Q^2 = 0$ on each generator. The inputs are the Virasoro $\lambda$-bracket $\{T_\lambda T\} = \partial T + 2\lambda T + \frac{c}{12}\lambda^3$ and the ghost OPE $\{(c_{\mathrm{gh}})_\lambda c_{\mathrm{gh}}\} = 0$, $\{(c_{\mathrm{gh}})_\lambda \mu\} = -1$.
chapters/examples/w-algebras-stable.tex:119:\emph{On $T$:} $Q(T) = \partial T \cdot c_{\mathrm{gh}} + 2T\partial c_{\mathrm{gh}} + \frac{c}{12}\partial^3 c_{\mathrm{gh}}$. Computing $Q^2(T)$ requires applying $Q$ to each term and using the Leibniz rule. The result is a polynomial in $T, c_{\mathrm{gh}}, \mu$ and their derivatives. The cancellation follows from the Jacobi identity for the $\lambda$-bracket: the coefficient of each monomial in $Q^2(T)$ is a specific linear combination of structure constants of $\{T_\lambda T\}$, and the Jacobi identity $\{T_\lambda \{T_\mu T\}\} - \{T_\mu \{T_\lambda T\}\} = \{\{T_\lambda T\}_{\lambda+\mu} T\}$ ensures these cancel. This is a standard calculation in BRST cohomology; see~\cite{FMS86}.
chapters/examples/w-algebras-stable.tex:132:\begin{proposition}[Virasoro $\lambda$-bracket from Propagator; \ClaimStatusProvedHere]
chapters/examples/w-algebras-stable.tex:136:The $\lambda$-bracket $m_2$ computed from \eqref{eq:vir-propagator} reproduces \eqref{eq:vir-lambda-bracket}:
chapters/examples/w-algebras-stable.tex:138:m_2(T, T)_\text{sing} = \{T_\lambda T\} = \sum_{n=1}^3 \frac{a_n}{\lambda^n},
chapters/examples/w-algebras-stable.tex:139: \qquad\text{(OPE convention: $\tfrac{1}{\lambda^n} \leftrightarrow \tfrac{\lambda^{n-1}}{(n-1)!}$ in $\lambda$-bracket notation)}
chapters/examples/w-algebras-stable.tex:164:Setting $\lambda = z_1 - z_2$ and extracting singular terms gives \eqref{eq:vir-lambda-bracket}.
chapters/examples/w-algebras-stable.tex:212:where indices are cyclic. The propagator $K(z,t) = \Theta(t)/(2\pi z)$ contributes one holomorphic 1-form per edge, giving total form degree $k$ on $\FM_k(\C)$ (real dimension $2(k-1)$), which matches the dimension for a non-degenerate integral at each~$k$. The $\partial_z$ derivatives from the $V_3 = T\mu\partial\mu$ vertex structure produce polynomial dependence on the spectral parameters $\lambda_i = z_i - z_{i+1}$, ensuring non-trivial contributions at every degree.
chapters/examples/w-algebras-stable.tex:358:m_2\bigl(m_2(T,T;\lambda_1),\, T;\, \lambda_1+\lambda_2\bigr)
chapters/examples/w-algebras-stable.tex:359:\;-\; m_2\bigl(T,\, m_2(T,T;\lambda_2);\, \lambda_1\bigr)

thinking
**Planning seam audit strategy**

I need to be strategic about my outputs while working on this seam audit between volumes. There’s a lot to inspect, starting with the README connection table and various theorem package summaries. Comparing with Volume I for accuracy is crucial, especially for identifying inconsistencies. I’ll focus on exact line references in both volumes. I should also search for specific patterns in the files, confirming content instead of making guesses. It's all about getting those details right!
codex
The initial grep already exposed likely seam hot spots from the repo’s own archaeology, but I’m not treating those as findings yet. I’m now reopening only the live manuscript lines themselves and checking whether the defects still survive on the active Vol II surface, especially around theorem summaries, Virasoro/W-algebra convention bridges, and affine `r`/`R`-matrix passages.
exec
/bin/zsh -lc "rg -n \"R\\(z\\)=1\\+\\\\hbar\\\\,\\\\Omega/z|R\\(z\\)=1\\+\\\\hbar\\\\,\\Omega/z|R\\(z\\)=1\\+k\\\\Omega/z|R\\(z\\)=1\\+\\\\hbar\\\\,k\\\\,\\\\Omega/z|r_Y\\(z\\) = \\\\hbar\\\\,\\\\Omega/z|hbar\\\\Omega/z|1\\+\\\\hbar\\\\,\\\\Omega/z|1\\+k\\\\Omega/z\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"S_2|c/12|lambda-bracket coefficient|divided power|divided-power|S_4|2/\\(5c\\"'^2'"\\)|2/c\\"'^2|Virasoro central charge itself" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba README.md | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"SC\\"'^'"\\{ch,top\\}.*E_3|E_3.*SC\\"'^'"\\{ch,top\\}|B\\(A\\).*SC|bar complex.*SC|derived center|C\\"'^bullet_'"\\{ch\\}\\(A,A\\)|E_1.*E_\\\\infty|E_inf|E_\\\\infty|E_1.*derived center|B\\"'^ord|ordered bar" README.md chapters' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"bare kappa|\\\\bkappa\\\\b|\\bkappa\\b\" chapters/README.md README.md chapters/connections chapters/examples chapters/theory | head -n 0" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "E_3-chiral" chapters README.md CLAUDE.md' in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: regex parse error:
    (?:R\(z\)=1\+\hbar\,\Omega/z|R\(z\)=1\+\hbar\,\Omega/z|R\(z\)=1\+k\Omega/z|R\(z\)=1\+\hbar\,k\,\Omega/z|r_Y\(z\) = \hbar\,\Omega/z|hbar\Omega/z|1\+\hbar\,\Omega/z|1\+k\Omega/z)
                 ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/examples/w-algebras-w3.tex:604: S_4^W(\ell,\mu,\nu)\,{:}\Lambda W{:}
chapters/examples/w-algebras-w3.tex:815:r^{TT}(\lambda,\mu) &= \frac{c/12}{\lambda^3 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{\lambda^2 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{\lambda \mu},\\
chapters/examples/w-algebras-w3.tex:890: pole (the $c/360$ term in divided-power convention),
chapters/examples/examples-worked.tex:133:+ (c/12)\lambda^3$ gives Laplace kernel $r^L(z) = \partial T/z + 2T/z^2
chapters/examples/examples-worked.tex:1329:  $\Delta = 8\kappa S_4 = 0$ confirms class~$\mathbf{L}$.
chapters/examples/examples-worked.tex:1337:class~$\mathbf{L}$.  Item (iv): the quartic contact invariant $S_4$ vanishes
chapters/examples/examples-worked.tex:1732:  $\Delta = 8\kappa S_4 \ne 0$ because $S_4 \ne 0$ for
chapters/examples/examples-worked.tex:1747:The non-vanishing of $S_4$ for $\mathcal{W}$-algebras
chapters/examples/examples-worked.tex:1749:$S_4^{\mathrm{Vir}} = 10/[c(5c + 22)]$
chapters/examples/examples-worked.tex:3813:algebras have $S_4 = 0$, so the shadow obstruction tower terminates.
chapters/examples/examples-worked.tex:3991:$S_4^{G^\pm} = 0$ because the $G^\pm$ generators transform
chapters/examples/examples-worked.tex:4847:  at each genus $g$.  Since $S_4 = 0$ (the quartic contact invariant
chapters/examples/examples-worked.tex:4862:  $\Delta = 8\kappa S_4 = 0$.
chapters/examples/examples-worked.tex:4942:  $\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
chapters/examples/examples-worked.tex:4987:  $\Delta = 8\kappa S_4 = 8 \cdot (c/2) \cdot 10/[c(5c+22)]
chapters/examples/examples-worked.tex:5046:  $\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,\;
chapters/examples/examples-worked.tex:5128:  $S_4^W = 40/(5c+22)$.
chapters/examples/examples-worked.tex:5208:  Class $\mathbf{L}$: the quartic invariant $S_4 = 0$
chapters/examples/examples-worked.tex:5312:  $S_4 \ne 0$ and $\Delta \ne 0$, giving an infinite shadow obstruction tower.
chapters/examples/w-algebras.tex:829:r^{TT}(\lambda,\mu) &= \frac{c/12}{\lambda^3 \mu} + \frac{T \otimes \mathbf{1} + \mathbf{1} \otimes T}{\lambda^2 \mu} + \frac{(\partial T) \otimes \mathbf{1}}{\lambda \mu},\\
 exited 2 in 50ms:
rg: regex parse error:
    (?:SC\^\{ch,top\}.*E_3|E_3.*SC\^\{ch,top\}|B\(A\).*SC|bar complex.*SC|derived center|C\^bullet_\{ch\}\(A,A\)|E_1.*E_\infty|E_inf|E_\infty|E_1.*derived center|B\^ord|ordered bar)
                                                                                                                        ^^
error: unrecognized escape sequence
 succeeded in 50ms:
     1	# A-infinity Chiral Algebras and 3D Holomorphic-Topological QFT
     2	
     3	**Volume II** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
     4	by Raeez Lorgat.
     5	
     6	The bar complex B(A) is an E_1 chiral coassociative coalgebra: the differential encodes the chiral product (holomorphic, from FM_k(C)), the deconcatenation coproduct encodes topological factorization on R. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). The five Vol I theorems are the modular invariants that survive Sigma_n-coinvariance.
     7	
     8	## The Three Volumes
     9	
    10	| Volume | Title | Role |
    11	|:------:|-------|------|
    12	| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
    13	| **II** | *A-infinity Chiral Algebras and 3D HT QFT* (this volume) | The 3D interpretation: what the engine computes |
    14	| **III** | *Calabi-Yau Quantum Groups* | The categorical completion: CY categories as quantum chiral algebras |
    15	
    16	## Connection to Volume I
    17	
    18	Every chapter depends on Vol I's five theorems:
    19	
    20	| Vol I Theorem | What it supplies |
 exited 1 in 51ms:
head: illegal line count -- 0
rg: chapters/README.md: No such file or directory (os error 2)
 succeeded in 51ms:
CLAUDE.md:45:The E_2-to-E_3 step: the A_inf-chiral algebra structure. An A_inf-algebra in E_1-chiral algebras is the 3d HT bulk factorisation algebra. Z(A) with E_2 gives the bulk observables; the transverse E_1 gives the topological direction; together E_3. This is the CLIMAX: 3d quantum gravity = E_3-chiral algebra = derived center of boundary with transverse E_1 extension.
CLAUDE.md:74:- E_3-chiral = E_2-chiral x E_1-top: the HT bulk. Holomorphic on X, topological on R. Factorisation algebra on X x R. This is the HOLOMORPHIC-TOPOLOGICAL structure. NOT AUTOMATIC from the chiral algebra. Requires a 3d HT theory whose boundary is A. For gauge-theoretic examples (Kac-Moody): the 3d holomorphic CS theory (from 6d holomorphic gauge theory) provides this — proved by Costello-Li / CFG. For W-algebras via DS (including Virasoro): the Costello-Gaiotto theorem provides the 3d HT theory (holomorphic CS with DS boundary conditions); the remaining gap is T_DS = [Q_tot, G'] in the DS-modified BV complex. For chiral algebras without gauge-theoretic origin: requires quantizing the Poisson vertex model (hard open work). The E_2 -> E_3-chiral step is CONJECTURAL for non-gauge-theoretic algebras.
CLAUDE.md:75:- E_3-topological = E_2-top x E_1-top = full TQFT: INDEPENDENT of complex structure. Requires BOTH a 3d HT theory (for E_3-chiral) AND a conformal vector at non-critical level (for topologization). This is Chern-Simons. CFG (arXiv:2602.12412) construct the E_3-topological structure from BV quantisation of CS. THE VOLUME'S CLIMAX IS CONSTRUCTING E_3-TOPOLOGICAL ON Z^{der}_{ch}(A) WHEN A HAS A CONFORMAL VECTOR AT NON-CRITICAL LEVEL AND A 3D HT ORIGIN.
CLAUDE.md:80:- E_3: E_3-chiral + conformal vector = E_3-topological. This is the passage from HT theory to fully topological (TQFT/Chern-Simons). The conformal vector "integrates out" the holomorphic direction.
CLAUDE.md:82:Without conformal vector: stuck at E_3-chiral (HT, depends on complex structure).
CLAUDE.md:99:The preface walks through topologico-combinatoric stratified spaces from a point to E_3. At each stage a degree of freedom is gained, a new configuration space appears, and a new algebraic structure emerges on a specific object. The volume climbs to E_3-TOPOLOGICAL (not E_3-chiral).
CLAUDE.md:114:Stage 9 = E_3-TOPOLOGICAL is the POINT OF THE VOLUME. NOT E_3-chiral: the conformal vector KILLS the chiral direction at the cohomological level. Sugawara at non-critical level: T(z) = {Q, G(z)}, so C-translations are Q-exact, the complex structure on C becomes irrelevant in cohomology, the two colors of SC^{ch,top} collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra independent of the complex structure on C. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct, holomorphic direction carries nontrivial cohomological information). At critical level k = -h^v: Sugawara undefined, center jumps, topologization fails.
CLAUDE.md:263:FM47: E_inf → E_3-chiral automatic. Claimed E_inf chiral algebra automatically produces E_3-chiral. WRONG. E_2 on Z(A) is automatic (Deligne conjecture). E_3-chiral requires a 3d HT theory whose boundary is A. For KM: proved (holomorphic CS from 6d). For GENERAL vertex algebras: requires quantizing the Poisson vertex model — HARD OPEN WORK, not automatic. Counter: nothing beyond E_2 on Z(A) is automatic.
CLAUDE.md:287:MP2: AUTOMATIC vs REQUIRES CONSTRUCTION. E_2 on Z(A) is automatic (Deligne). Everything above E_2 requires a specific construction (3d HT theory for E_3-chiral, conformal vector for E_3-top). Never say "automatic" above E_2.
CLAUDE.md:301:FM57: Costello-Gaiotto already provides 3d HT for Virasoro. The manuscript says "quantizing the PV model is hard open work" for Virasoro E_3-chiral. UPDATED 2026-04-12: The T_DS = [Q_tot, G'] gap is NOW CLOSED (thm:E3-topological-DS). The improvement term is always Cartan currents, even for non-principal nilpotents (thm:E3-topological-DS-general).


thinking
**Evaluating audit surfaces**

The user is asking me to exhaustively audit the surfaces, but I can't list everything. I should focus on relevant seam transition points to find inconsistencies or gaps. There might be representative seam issues where bare κ shows up in the cross-volume bridge summaries. It’s important to identify exact fixes. I’ll concentrate on the "MISSION: SEAM AUDIT" between cross-volume and cross-volume, specifically looking at the Vol I to Vol II bridge.
thinking
**Comparing theorem statuses**

I need to compare the theorem statuses and claim names with Vol I. I think I should open Vol II and look for the relevant rows in the concordance. There’s definitely a connection to explore between the two volumes that could clarify things. I’ll make sure to gather all the necessary information and insights, so I can provide a thorough comparison. It feels important to examine the details closely!
exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '1260,1345p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '120,175p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/twisted_holography_quantum_gravity.tex | sed -n '2728,2746p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n "Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|bar-cobar adjunction|modular characteristic|complementarity|Hochschild ring|Koszul inversion" chapters/connections/concordance.tex metadata/theorem_registry.md README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '1,180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|bar-cobar adjunction|modular characteristic|complementarity|Hochschild ring|Koszul inversion" chapters/connections/concordance.tex metadata/theorem_registry.md chapters/connections/concordance.tex README.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2728	connection.
  2729	\end{definition}
  2730	
  2731	\begin{remark}[Five theorems as cumulant relations]
  2732	% label removed: rem:thqg-five-theorems-cumulants
  2733	The five main theorems of Volume~I (A, B, C, D, H) are the first
  2734	five cumulant relations of the modular cumulant transform:
  2735	\begin{enumerate}[label=\textup{(\roman*)}]
  2736	\item \textbf{Theorem A} (bar-cobar adjunction): $D_\cA$ defines
  2737	 the cumulant generating function.
  2738	\item \textbf{Theorem B} (bar-cobar inversion): the cumulant
  2739	 generating function is invertible on the Koszul locus.
  2740	\item \textbf{Theorem C} (complementarity): the cumulant
  2741	 generating function splits into bulk and defect components.
  2742	\item \textbf{Theorem D} (modular characteristic): the first
  2743	 cumulant is $\kappa(\cA)$.
  2744	\item \textbf{Theorem H} (Hochschild, at generic level): the chiral Hochschild
  2745	 cohomology is polynomial in the cumulants. The critical level $k = -h^\vee$
  2746	 is excluded because $\dim \ChirHoch^0$ can be infinite there
 succeeded in 52ms:
  1260	$C^\bullet_{\mathrm{GS}}(\cA,\cA)$ that governs $\Sigma_n$-equivariant
  1261	descent (Remark~\ref{rem:r-matrix-mc}); the Yang--Baxter equation is the
  1262	MC equation; the classical $r$-matrix $r_0$ is its linearisation
  1263	(Corollary~\ref{cor:classical-ybe}); and the Yangian $Y_\hbar(\mathfrak g)$
  1264	is the algebra of symmetries of this MC datum. The passage from the master
  1265	theorem's algebraic core to the spectral data of ordered
  1266	configuration spaces is the passage from the abstract MC moduli to its
  1267	explicit coordinatisation.
  1268	\end{remark}
  1269	
  1270	\section{The \texorpdfstring{$E_1$}{E1} five main theorems at genus zero}
  1271	\label{sec:e1-five-theorems-genus0}
  1272	\index{five main theorems!E1@$E_1$ variant!genus zero|textbf}
  1273	
  1274	Volume~I establishes five main theorems for $E_\infty$-chiral algebras: bar-cobar adjunction, Koszul inversion, complementarity, leading coefficient, and the Hochschild ring. Each has an $E_1$-chiral counterpart, obtained by replacing symmetric coinvariants with the ordered bar complex and its braid-group equivariance. The five $E_1$ theorems at genus zero are formal consequences of the master theorem (Theorem~\ref{thm:master}) together with the explicit constructions of Appendix~\ref{sec:ordered-bar-explicit}; they are collected here to make the parallel with Vol~I explicit.
  1275	
  1276	\begin{theorem}[Theorem~$\mathrm{A}^{E_1}$; \ClaimStatusProvedHere]
  1277	\label{thm:e1-theorem-A}
  1278	\index{five main theorems!E1@$E_1$ variant!Theorem A}
  1279	$\Cobar \dashv \Barch\colon
 succeeded in 52ms:
   120	LG $Q^2=0$ with interaction & ProvedHere & $m_1=Q$ is linear, independent of $W$ \\
   121	Abelian CS boundary $= \widehat{\mathfrak{u}(1)}_k$ & ProvedHere & OPE computed from propagator \\
   122	Virasoro: $m_k \ne 0$ all $k \ge 3$ (wheel diagrams) & Conditional on (H1)--(H4) & Loop counting + Hamiltonian cycle \\
   123	Virasoro $Q^2=0$ & ProvedHere & Lem.~\ref{lem:vir-nilpotent}; explicit verification \\
   124	Virasoro recursive $m_k$ & ProvedHere & Thm.~\ref{thm:vir-recursive}; from BV master equation \\
   125	$W_3$ classical YBE & ProvedHere & From $\lambda$-bracket Jacobi identity \\
   126	$W_3$ central charge shift & ProvedHere & Ghost system counting \\
   127	\end{tabular}
   128	\end{center}
   129	
   130	\subsection{Cross-volume bridges to the monograph}
   131	
   132	\begin{center}
   133	\renewcommand{\arraystretch}{1.3}
   134	\begin{tabular}{p{0.12\textwidth}p{0.35\textwidth}p{0.18\textwidth}p{0.25\textwidth}}
   135	\textbf{Bridge} & \textbf{Statement} & \textbf{Status} & \textbf{Monograph frontier} \\
   136	\hline
   137	Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
   138	DS-bar & Bar-cobar commutes with DS reduction (monograph Thm~ds-koszul-intertwine) & Proved (Vol~I) & W-algebra axis \\
   139	Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
 exited 2 in 52ms:
rg: metadata/theorem_registry.md: No such file or directory (os error 2)
chapters/connections/concordance.tex:137:Bar-cobar & $\mathsf{SC}^{\mathrm{ch,top}}$ bar-cobar specializes monograph Thm A when curve${}=\C$, topological${}=\R$ & Proved & Theorem A specialization \\
chapters/connections/concordance.tex:139:Hochschild & BV-BRST origin of monograph's Theorem H complex (Vol~I Theorem~H is proved at generic level; the critical level $k=-h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}) & Proved (all genera, generic level) & Theorem H physical origin \\
chapters/connections/concordance.tex:222:\begin{theorem}[Feynman curvature = modular characteristic at genus~$1$;
chapters/connections/concordance.tex:246: modular characteristic of Volume~I. The curvature arises from
chapters/connections/concordance.tex:327:definition, the modular characteristic $\kappa(\cA)$
chapters/connections/concordance.tex:541:(Lagrangian complementarity, pending
chapters/connections/concordance.tex:659:\item \textbf{Formality obstruction}: \emph{Resolved at all genera.} At genus~$1$ (Corollary~\ref{cor:mc5-genus-one-bridge}), the $d'=1$ formality failure is the modular characteristic: the Arnold defect on $E_\tau$ produces curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1$ in the Feynman-defined $A_\infty$ operations, absorbed by the Faber--Pandharipande constant $\lambda_1^{FP} = 1/24$. At genus~$g \geq 2$, the resolution proceeds by inductive genus determination (Volume~I, Theorem~\ref*{V1-thm:inductive-genus-determination}), $2$D convergence (Volume~I, Proposition~\ref*{V1-prop:2d-convergence}), and the analytic-algebraic comparison (Volume~I, Theorem~\ref*{V1-thm:analytic-algebraic-comparison}); see Remark~\ref{rem:mc5-higher-genus-open}.
README.md:23:| **(B)** Koszul inversion | Lifted to raviolo VA setting and completed towers |
README.md:26:| **(H)** Hochschild ring | BV-BRST origin; bulk = chiral Hochschild |
 succeeded in 51ms:
     1	# Theorem Registry
     2	
     3	Auto-generated on 2026-04-13 from the structured claim extractor in `scripts/generate_metadata.py`.
     4	
     5	This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
     6	
     7	## Snapshot
     8	
     9	| Metric | Value |
    10	|---|---:|
    11	| ProvedHere claims | 2845 |
    12	| Total tagged claims | 3673 |
    13	| Active files in `main.tex` | 85 |
    14	| Total `.tex` files scanned | 128 |
    15	
    16	## Status Totals
    17	
    18	| Status | Count |
    19	|---|---:|
    20	| `ProvedHere` | 2845 |
 succeeded in 51ms:
README.md:80:- **Part I** (The Bar Complex): Theorems A-D+H, bar-cobar adjunction, inversion, complementarity
metadata/theorem_registry.md:61:| `chapters/theory/higher_genus_complementarity.tex` | 80 |
metadata/theorem_registry.md:98:| `thm:frame-complementarity` | `theorem` | 1774 | Quantum complementarity for Heisenberg |
metadata/theorem_registry.md:473:| `prop:ext-koszul-dual-level` | `proposition` | 3244 | \texorpdfstring{$\mathrm{Ext}$}{Ext} complementarity at dual levels |
metadata/theorem_registry.md:643:| `thm:e1-theorem-C-modular` | `theorem` | 2003 | Theorem~$\mathrm{C}^{E_1}$ at all genera: ordered complementarity |
metadata/theorem_registry.md:721:#### `chapters/theory/higher_genus_complementarity.tex` (80)
metadata/theorem_registry.md:728:| `thm:quantum-complementarity-main` | `theorem` | 525 | Quantum complementarity as Lagrangian polarization |
metadata/theorem_registry.md:756:| `prop:complementarity-landscape` | `proposition` | 3048 | Complementarity landscape |
metadata/theorem_registry.md:787:| `thm:ambient-complementarity-tangent` | `theorem` | 4924 | Ambient complementarity in tangent form |
metadata/theorem_registry.md:788:| `thm:ambient-complementarity-fmp` | `theorem` | 4967 | Ambient complementarity as shifted symplectic formal moduli problem |
metadata/theorem_registry.md:793:| `prop:fake-complementarity-criterion` | `proposition` | 5343 | Criterion for fake complementarity |
metadata/theorem_registry.md:803:| `prop:non-critical-liouville` | `proposition` | 6254 | Non-critical complementarity and the Liouville sector |
metadata/theorem_registry.md:804:| `cor:complementarity-discriminant-cancellation` | `corollary` | 6299 | Degree-$4$ discriminant cancellation |
metadata/theorem_registry.md:836:| `thm:genus1-universal-curvature` | `theorem` | 4159 | Universal genus-1 curvature via the modular characteristic |
metadata/theorem_registry.md:854:| `cor:kappa-sum-wn` | `corollary` | 5924 | Obstruction complementarity for \texorpdfstring{$\mathcal{W}_N$}{W(N)} |
metadata/theorem_registry.md:972:| `thm:ds-complementarity-tower-main` | `theorem` | 12767 | DS complementarity tower |
metadata/theorem_registry.md:990:| `prop:critical-locus-complementarity` | `proposition` | 14723 | Critical-locus form of complementarity |
metadata/theorem_registry.md:1166:| `thm:central-charge-complementarity` | `theorem` | 1017 | Central charge complementarity |
metadata/theorem_registry.md:1183:| `cor:hochschild-ring-koszul` | `corollary` | 715 | Hochschild ring isomorphism under Koszul duality |
metadata/theorem_registry.md:1403:| `prop:bp-complementarity` | `proposition` | 293 | Complementarity;\ |


thinking
**Inspecting theorem statuses**

I need to compare the statuses of various theorems, specifically focusing on Theorem A and its specializations. I’m thinking about inspecting Volume I for the corresponding claims and seeing how theorems A-D+H correspond to each other. I should search for a summary of theorem statuses in the concordance section around a specific line. It looks like most entries in the theorem registry indicate they are "ProvedHere," but I need to look for relevant labels or names to confirm their details.
thinking
**Identifying potential issues**

I see there are some discrepancies between Volume II and Volume I concerning theorems for E_infty-chiral algebras. Volume I mentions five notions of E1-chiral algebra, focusing on E1-E1 operadic duality, which seems to contradict Volume II's claims. I need to verify this in Volume I to propose a fix, like replacing E_infty with "modular chiral algebras." It seems I should search for the phrase "E_1" in the relevant sections to confirm the correct content and details.
codex
I’ve got one likely hierarchy defect already: a live Vol II chapter currently says Vol I’s five main theorems are for `E_\infty`-chiral algebras, which would directly violate the current E1-first architecture if Vol I source no longer says that. I’m checking the Vol I theorem package now before promoting that to a finding.
exec
/bin/zsh -lc 'rg -n -F "E_3-chiral" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4600,4668p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"five main theorems|Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|E_1|E_\\\\infty|E_inf|ordered bar|B\\"'^ord|symmetric bar|coinvariant" chapters/connections/concordance.tex chapters/theory/bar_construction.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/theory/algebraic_foundations.tex chapters/frame/guide_to_main_results.tex' in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 51ms:
  4600	 flat connection on the Teichm\"uller space~$\mathcal{T}_g$,
  4601	 with monodromy encoding the mapping-class group
  4602	 representation.
  4603	 \hfill\textup{(To be developed)}
  4604	\end{enumerate}
  4605	
  4606	\paragraph{Bibliographic pointers.}
  4607	Polyakov~1981 (Polyakov action),
  4608	Belavin--Polyakov--Zamolodchikov~1984 (conformal symmetry),
  4609	Belavin--Knizhnik~1986 (factorization on~$\overline{\cM}_g$),
  4610	Alvarez~1983 (Polyakov--Alvarez formula).
  4611	
  4612	\paragraph{Cross-references.}
  4613	Proposition~\ref{prop:polyakov-degree-two-projection}
  4614	(\S\ref{sec:koszul-across-genera});
  4615	Remark~\ref{rem:complementarity-polyakov-cancellation}
  4616	(\S\ref{sec:complementarity-theorem});
  4617	Remark~\ref{rem:ghost-koszul-identification}
  4618	(Chapter~\ref{chap:free-fields});
  4619	Proposition~\ref{prop:polyakov-chern-weil}
 exited 2 in 51ms:
rg: regex parse error:
    (?:five main theorems|Theorem A|Theorem B|Theorem C|Theorem D|Theorem H|E_1|E_\infty|E_inf|ordered bar|B\^ord|symmetric bar|coinvariant)
                                                                                  ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '8308,8860p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_3d_gravity_movements_vi_x.tex | sed -n '1484,1550p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  8308	determined by $\arg(t_\pm)$. Since the branch points are
  8309	complex conjugate with nonzero imaginary part, the oscillation
  8310	is genuine and persists to all orders.
  8311	\end{remark}
  8312	
  8313	\subsubsection*{The shadow table through $S_9$}
  8314	
  8315	The shadow-metric integral
  8316	$G_{\mathrm{scal}}(t) = \int_0^t s\sqrt{Q_{\mathrm{Vir}}(s)}\,ds$
  8317	produces the scalar shadow coefficients for $r \ge 4$ in closed form via
  8318	$S_r = [t^r]G_{\mathrm{scal}}$ (equivalently, $S_r = [t^r]H/r$
  8319	with $H(t) = t^2\sqrt{Q_{\mathrm{Vir}}(t)}$).
  8320	The following table extends the tower through degree~$9$;
  8321	the entries for $r = 2,3$ are the physical shadow coefficients
  8322	$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations
  8323	(these determine the shadow metric but are not its Taylor coefficients).
  8324	
  8325	\begin{center}
  8326	\small
  8327	\renewcommand{\arraystretch}{1.3}
 succeeded in 51ms:
  1484	\frac{10}{c(5c+22)}
  1485	\left\langle
  1486	 \omega^{(4)} \cdot
  1487	 \cO_1\cO_2\cO_3
  1488	\right\rangle.
  1489	\end{equation}
  1490	At $c \to \infty$ (semiclassical gravity): $S_4 \sim 2/(5c^2)
  1491	\to 0$, and the quartic correction vanishes; semiclassical
  1492	gravity is controlled by $S_2$ alone. At $c = -22/5$
  1493	(Lee--Yang): $S_4$ diverges, signaling the reorganization of
  1494	the shadow obstruction tower.
  1495	
  1496	\subsubsection*{Degree-$5$: the first new higher-degree celestial soft factor}
  1497	
  1498	\begin{theorem}[Quintic celestial soft factor; \ClaimStatusProvedHere]
  1499	\label{thm:gravity-quintic-soft}
  1500	\index{quintic celestial soft factor}
  1501	The degree-$5$ component $S_5$ of the shadow connection is
  1502	nonzero for generic~$c$:
  1503	\begin{equation}\label{eq:gravity-S5-nonzero}
exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '2118,2142p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  2118	\emph{The $R$-matrix from the ordered bar complex.}
  2119	The $R$-matrix $R(z)\in\operatorname{End}(V\otimes V)(\!(z)\!)$
  2120	for $V=\mathfrak{sl}_2$ is the operator that intertwines
  2121	the two orderings:
  2122	\[
  2123	R(z)\colon
  2124	\Barchord_2(e_i\otimes e_j;\,z_1<z_2)
  2125	\;\xrightarrow{\;\sim\;}
  2126	\Barchord_2(e_j\otimes e_i;\,z_2<z_1).
  2127	\]
  2128	For $\widehat{\mathfrak{sl}}_2$ at level~$k$:
  2129	$R(z)=1+\hbar\,\Omega/z+O(z^{-2})$ with
  2130	$\hbar=1/(k+2)$, where
  2131	$\Omega=e\otimes f+f\otimes e+\tfrac12 h\otimes h$
  2132	is the Casimir. (At $k=0$ the level-stripped
  2133	coefficient $\hbar\to 1/2$ remains nonzero because
  2134	the $\widehat{\mathfrak{sl}}_2$ Sugawara shift
  2135	$k+2$ survives; the strict classical $r$-matrix
  2136	on the underlying affine current algebra is
  2137	$k\,\Omega/z$, which vanishes at $k=0$ in accordance



thinking
**Identifying inconsistencies**

I see that I need to gather other findings. In the file `3d_gravity.tex`, lines 8322-8334 are still using `S_2 = c/12`, but earlier lines 121 and 1628 correctly use `c/2`. This inconsistency indicates a clear failure in the OPE to lambda-bracket conversion, which is a self-contradiction in the same file. It's important for me to address this as I continue my analysis.
thinking
**Clarifying shadow coefficients**

I need to update lines 8322-8334 by changing "physical shadow coefficients S_2 = c/12" to "S_2 = \kappa = c/2." It looks like if the table refers to the lambda-bracket coefficient, I should rename that column or description. I need to inspect the surrounding text for the exact fix. This involves verifying S3, where it seems to be -c, unless that's not standard. I’ll confirm that from Volume I. The key change is for line 8322 and entry 8334 to be c/2.
thinking
**Identifying coefficient issues**

I should note that \(c/12\) is the lambda-bracket divided-power coefficient, not the shadow invariant. If preserving the coefficient table, I might suggest a rename. Additionally, I need to check line 8853, where it states \(S^{(2)}_{\text{contact}} \sim 2/(5c^2)\) is still wrong and should actually be \(2/c^2\). I found a contradiction since similar corrections happen in lines 8123 and 9101. I’ll verify the movement file line 1490 for the same asymptotic issue. Also, I want to check which files are actively referenced in main.tex before proceeding.
codex
A second live defect is confirmed in `3d_gravity.tex`: one late-table passage still redefines `S_2` as `c/12`, contradicting both Vol I and earlier corrected lines in the same chapter. I’m checking whether that is isolated or paired with downstream stale asymptotics / soft-factor summaries before I finalize it.
exec
/bin/zsh -lc 'rg -n -F "3d_gravity" main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '8116,8130p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "thqg_3d_gravity_movements_vi_x" main.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '100,132p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '9088,9105p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "S_2 = c/12" chapters/connections/3d_gravity.tex chapters/connections/thqg_3d_gravity_movements_vi_x.tex chapters/examples/rosetta_stone.tex chapters/theory/introduction.tex chapters/connections/holomorphic_topological.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1426:\input{chapters/connections/3d_gravity}
1427:\input{chapters/connections/thqg_3d_gravity_movements_vi_x}
 succeeded in 51ms:
1427:\input{chapters/connections/thqg_3d_gravity_movements_vi_x}
 succeeded in 51ms:
  8116	 S^{(2)}_{\mathrm{graviton}}
  8117	 \;\propto\;
  8118	 \mathfrak{Q}^{\mathrm{contact}}_{\mathrm{Vir}}
  8119	 \;=\;
  8120	 \frac{10}{c(5c+22)}.
  8121	 \end{equation}
  8122	\end{enumerate}
  8123	At large $c$: $S^{(2)} \sim 2/c^2 \to 0$, confirming that
  8124	semiclassical gravity is controlled by the leading and
  8125	subleading soft theorems alone.
  8126	\end{theorem}
  8127	
  8128	\begin{proof}
  8129	(i): For primary $\cO_i$ of weight $h_i$,
  8130	$T(z)\cO_i(w) \sim h_i(z-w)^{-2} + \partial\cO_i(z-w)^{-1}$,
 succeeded in 51ms:
   100	makes this concrete. Four identifications:
   101	\begin{enumerate}[label=\textup{(\alph*)},leftmargin=*]
   102	\item The boundary chiral algebra $A = \mathrm{Vir}_c$ is the
   103	 conformal boundary datum.
   104	\item The bulk theory $\Zder^{\mathrm{ch}}(\mathrm{Vir}_c)$
   105	 is the derived chiral center: Hochschild cochains of the
   106	 boundary algebra, living on the slab
   107	 $\R_{\ge 0} \times \C$. These cochains are (conjecturally)
   108	 the bulk gravity observables. Bar-cobar inversion provides the
   109	 dictionary.
   110	\item The Drinfeld double $U_A = A \bowtie A^!$, with
   111	 $A^! = \mathrm{Vir}_{26-c}$, conjecturally reconstructs the full algebra of
   112	 bulk observables coupled to boundary states. Bulk line
   113	 operators are conjecturally $\mathrm{Vir}_{26-c}$-modules
   114	 (Conjecture~\ref{conj:gravity-line-identification}).
   115	\item The curvature $\kappa(\mathrm{Vir}_c) = c/2$ controls
   116	 every holographic observable: Cardy degeneracy, BTZ
   117	 entropy, and the genus tower are all $\kappa$-polynomials.
   118	\end{enumerate}
   119	The shadow obstruction tower $\{S_r(\mathrm{Vir}_c)\}_{r \ge 2}$
 succeeded in 51ms:
  9088	\index{conformal bootstrap!large-$c$}%
  9089	At $c \to \infty$ ($G \to 0$, semiclassical gravity), the shadow
  9090	tower organises into a $1/c$ expansion that matches the large-$c$
  9091	conformal bootstrap:
  9092	\begin{enumerate}[label=\textup{(\roman*)}]
  9093	\item \textup{(Leading order.)}
  9094	 $S_2 = \kappa = c/2$, the modular characteristic of the
  9095	 Virasoro algebra.
  9096	 In the bootstrap, this controls the normalisation of the
  9097	 stress-tensor two-point function
  9098	 $\langle T(z)T(0)\rangle = c/(2z^4)$:
  9099	 the Weinberg soft factor.
  9100	\item \textup{(First correction.)}
  9101	 $S_4 = 10/[c(5c+22)] \sim 2/c^2$ at large $c$.
  9102	 This is the first non-trivial contact invariant: the
  9103	 quartic correction to the four-point graviton amplitude.
  9104	 In the bootstrap, it corresponds to the $O(1/c^2)$
  9105	 correction to the four-point function from the identity
 succeeded in 51ms:
chapters/connections/3d_gravity.tex:8322:$S_2 = c/12$, $S_3 = -c$ from the binary and ternary operations

thinking
**Investigating movement file issues**

I need to check for potential duplicates in the movement file related to S_4 asymptotic, possibly including line 1490 of the movement file. It’s unclear if `S_2 = c/12` is relevant here. Additionally, the movement file may still reference 2/(5c^2), which is included because it’s active in main.tex. I should identify this as a separate finding and search for the fixed string 2/(5c^2) to clarify the situation.
exec
/bin/zsh -lc 'rg -n -F "2/(5c''^2)" chapters/connections/3d_gravity.tex chapters/connections/thqg_3d_gravity_movements_vi_x.tex chapters/connections/thqg_perturbative_finiteness.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_3d_gravity_movements_vi_x.tex | sed -n '1488,1494p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_perturbative_finiteness.tex | sed -n '1454,1462p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"c/12\" chapters/connections/3d_gravity.tex chapters/connections/thqg_3d_gravity_movements_vi_x.tex chapters/connections/holomorphic_topological.tex chapters/examples/rosetta_stone.tex chapters/theory/introduction.tex | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1490:At $c \to \infty$ (semiclassical gravity): $S_4 \sim 2/(5c^2)
chapters/connections/3d_gravity.tex:8853:(order $G^0$); $S^{(2)}_{\text{contact}} \sim 2/(5c^2)$
 succeeded in 51ms:
  1488	\right\rangle.
  1489	\end{equation}
  1490	At $c \to \infty$ (semiclassical gravity): $S_4 \sim 2/(5c^2)
  1491	\to 0$, and the quartic correction vanishes; semiclassical
  1492	gravity is controlled by $S_2$ alone. At $c = -22/5$
  1493	(Lee--Yang): $S_4$ diverges, signaling the reorganization of
  1494	the shadow obstruction tower.
 succeeded in 51ms:
  1454	\index{quartic contact invariant!3d gravity}
  1455	The scalar channel captures only the degree-$0$ information. The first non-scalar correction comes from the quartic contact invariant
  1456	\begin{equation}% label removed: eq:thqg-I-quartic-contact
  1457	Q^{\mathrm{contact}}_{\mathrm{Vir}} \;=\; \frac{10}{c(5c+22)}\,,
  1458	\end{equation}
  1459	which is the degree-$4$, genus-$0$ component of the shadow obstruction tower. For $c = 3\ell/(2G)$, this gives $Q^{\mathrm{contact}} = 10/(c(5c+22)) = 2/c^2 + O(1/c^3)$, a two-loop correction in Newton's constant. The genus-$1$ Hessian correction is
  1460	\begin{equation}% label removed: eq:thqg-I-genus1-hessian
  1461	\delta_{H,\mathrm{Vir}}^{(1)} \;=\; \frac{120}{c^2(5c+22)}\,x^2\,.
  1462	\end{equation}
 succeeded in 51ms:
chapters/theory/introduction.tex:1848:$\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
chapters/theory/introduction.tex:1867: converts $\lambda$-bracket coefficients $\partial T, 2T, c/12$ to
chapters/theory/introduction.tex:2324:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1408:$m_2(X,T;\mu) = 2\mu X + \mu^2 X' + (c/12)\mu^3\delta_{X=T}$,
chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1426:+ (c/12)\lambda_{23}^3$. Substituting into $m_3$ and
chapters/connections/3d_gravity.tex:238: $c/12$\textup{)}, the $\Ainf$ tower is infinite, and
chapters/connections/3d_gravity.tex:888: to $c/12 = \kappa/6$.
chapters/connections/3d_gravity.tex:1581:$m_2|_{\text{scalar}} = (c/12)\lambda^3$ has degree $3 = 2+1$,
chapters/connections/3d_gravity.tex:1597:scalar contact term) is proportional to $c/12 = \kappa/6$.
chapters/connections/3d_gravity.tex:1658: = \partial T + 2T\lambda + (c/12)\lambda^3$
chapters/connections/3d_gravity.tex:1711:+ (c/12)\lambda^3$: the coefficient of $\partial T$ is $1$, the
chapters/connections/3d_gravity.tex:1724: $(c/12)\lambda^{j+1}$ (a constant, not a field). Constants
chapters/connections/3d_gravity.tex:2054:contact amplitudes proportional to $c/12$): its convergence for
chapters/connections/3d_gravity.tex:3337:= c/12$. The sewing integral over
chapters/connections/3d_gravity.tex:3921:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
chapters/connections/3d_gravity.tex:3948:(c/12)\epsilon'''$, the Virasoro coadjoint action with
chapters/connections/3d_gravity.tex:4401:$\{T_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$.
chapters/connections/3d_gravity.tex:7972:+ (c/12)\lambda^3$. Output: the $\Ainf$ tower
chapters/connections/3d_gravity.tex:8013:$\{T{}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$
chapters/connections/3d_gravity.tex:8293:and symmetrising: $S_5 = -(17c/6)\lambda^6 / [(c/12)^2

thinking
**Searching theorem details**

I’m considering that the Vol I theorem registry might include `thm:w-algebra-hochschild`. I need to find a direct source for that and maybe also look at the summary of Theorem H in Volume I, checking sources like the guide to main results or concordance. I wonder if there’s been any misrepresentation of Theorem H, so gathering accurate information is essential. Let's explore that to clarify!
exec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '174,210p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/chiral_hochschild_koszul.tex | sed -n '700,860p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "Hochschild ring|polynomial growth|polynomial in the cumulants|ChirHoch|derived center" chapters/frame/guide_to_main_results.tex chapters/connections/concordance.tex chapters/theory/chiral_hochschild_koszul.tex chapters/theory/algebraic_foundations.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "Theorem H" chapters README.md metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	\chapter{Chiral Hochschild cohomology and Koszul duality}
     2	\label{chap:deformation-theory}
     3	
     4	\index{deformation theory!chiral|textbf}
     5	\index{Hochschild cohomology!chiral|textbf}
     6	
     7	The MC element $\Theta_\cA \in \MC(\gAmod)$ controls all of chiral
     8	Koszul duality, but how rigid is the moduli it lives in? Without
     9	knowing the tangent complex to
    10	$\MC(\gAmod)/\mathrm{gauge}$, every deformation, obstruction, and
    11	bulk-field coupling remains inaccessible. The chiral Hochschild
    12	complex $\ChirHoch^*(\cA)$ is that tangent complex;
    13	Theorem~H proves it is concentrated in degrees $\{0,1,2\}$ on the
    14	Koszul locus, so the MC moduli has cohomological
    15	amplitude~$[0,2]$, and the Koszul duality
    16	$\ChirHoch^n(\cA) \cong \ChirHoch^{2-n}(\cA^!)^\vee \otimes \omega_X$
    17	is Verdier duality on this tangent space.
    18	
    19	The cyclic deformation complex $\Defcyc(\cA)$
    20	(Definition~\ref{def:cyclic-deformation-elementary}) is the cyclic
 succeeded in 51ms:
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
    20	\textsc{Label} & \textsc{Statement} & \textsc{Location} \\
 succeeded in 51ms:
   174	Riccati algebraicity, the formality identification, and
   175	complementarity (Theorem~C).
   176	Theorems~D and~H are \emph{projectional outputs}: $\kappa$ is the scalar
   177	trace of~$\Theta_\cA$, and the chiral Hochschild ring is a
   178	polynomial consequence of Koszul functoriality.
   179	
   180	\begin{itemize}
   181	\item \textbf{Algebraicity}
   182	 (Theorem~\ref{thm:riccati-algebraicity}).
   183	 On any one-dimensional primary slice~$L$ of the cyclic
   184	 deformation complex, the weighted shadow generating function
   185	 $H(t) = \sum r\,S_r\,t^r$ satisfies
   186	 $H(t)^2 = t^4 Q_L(t)$
   187	 for an explicit quadratic polynomial~$Q_L$.
   188	 The shadow obstruction tower is therefore algebraic of degree~$2$
   189	 over $k(c)[t]$, determined by three invariants:
   190	 the modular characteristic~$\kappa$, the cubic coefficient~$\alpha$,
   191	 and the quartic shadow~$S_4$.
   192	
   193	\item \textbf{Formality identification}
 succeeded in 51ms:
chapters/theory/algebraic_foundations.tex:2325:Each notion admits its own derived center construction, and the
chapters/theory/algebraic_foundations.tex:2341:  $\operatorname{ChirHoch}^*(\cA)$, governed by the
chapters/theory/algebraic_foundations.tex:2356:  $\operatorname{ChirHoch}^*_{\mathrm{ord}}(\cA)$, governed by
chapters/theory/algebraic_foundations.tex:2366:  Output: mixed chiral-topological center: the derived center in
chapters/frame/guide_to_main_results.tex:57: Chiral Hochschild: $\ChirHoch^*(\cA)$ has polynomial
chapters/frame/guide_to_main_results.tex:364:$\ChirHoch^*$: chiral Hochschild cohomology.
chapters/connections/concordance.tex:71: $\ChirHoch^*(\cA)$ is concentrated in $\{0,1,2\}$,
chapters/connections/concordance.tex:74: $\ChirHoch^1(V_k(\fg))\cong\fg$ for affine KM;
chapters/connections/concordance.tex:131: $\ChirHoch^*(\cA) = \ChirHoch^*(\cA, \cA)$.
chapters/connections/concordance.tex:177:trace of~$\Theta_\cA$, and the chiral Hochschild ring is a
chapters/connections/concordance.tex:339: with the derived center in the coderived category unconditionally,
chapters/connections/concordance.tex:404: $\FM_m(\mathbb{C})$ is formal. Hence $\ChirHoch^*(\cA)$ is
chapters/connections/concordance.tex:411: $\ChirHoch^1(V_k(\fg)) \cong \fg$
chapters/connections/concordance.tex:2381:$\pi_{\mathrm{HH}}(\Theta_\cA)$ & H & $\mathrm{ChirHoch}^*(\cA)$ polynomial \\
chapters/connections/concordance.tex:2476: $\ChirHoch^*(\cA)$ is concentrated in cohomological degrees
chapters/connections/concordance.tex:2485: $\ChirHoch^*(\mathrm{Vir}_c)\cong \mathbb{C}\oplus \mathbb{C}[-2]$
chapters/connections/concordance.tex:3191:ChirHoch polynomial
chapters/connections/concordance.tex:3304:bar-cobar inversion via Theorem~H, polynomial growth, and
chapters/connections/concordance.tex:4397:$\ChirHoch^{\bullet}(\cA)$ arises as the $\Sigma$-coinvariant
chapters/connections/concordance.tex:4399:$\ChirHoch^{\bullet}(\cA) \cong
 succeeded in 51ms:
   700	dual~$\cA^!$ on a smooth projective curve~$X$, the bigraded chiral
   701	Hochschild complex
   702	\textup{(}Definition~\textup{\ref{def:bigraded-hochschild})} satisfies
   703	the \emph{derived-level} duality:
   704	\begin{equation}\label{eq:hochschild-H-derived}
   705	RHH_{\mathrm{ch}}(\cA)
   706	\;\simeq\;
   707	R\mathrm{Hom}\bigl(RHH_{\mathrm{ch}}(\cA^!),\, \omega_X[2]\bigr).
   708	\end{equation}
   709	On cohomology:
   710	\[
   711	\ChirHoch^n(\mathcal{A}) \cong \ChirHoch^{2-n}(\mathcal{A}^!)^{\vee} \otimes \omega_X.
   712	\]
   713	The shift by~$2$ is the output of the
   714	Fulton--MacPherson collapse
   715	\textup{(}Lemma~\textup{\ref{lem:hochschild-shift-computation}}\textup{)}:
   716	the collision-depth spectral sequence has $E_2$-page
   717	given by curve-level $\mathcal{D}_X$-Ext, so the geometric
   718	shift~$[p+2]$ on $\overline{C}_{p+2}(X)$ is cancelled by the
   719	totalization shift~$[-p]$ and only the base-curve shift~$[2]$
 succeeded in 50ms:
chapters/frame/guide_to_main_results.tex:56:\textbf{Theorem H} &
chapters/theory/higher_genus_modular_koszul.tex:30459:\index{Theorem H!holographic finite-dimensionality}
chapters/theory/introduction.tex:2396: Extends the Theorem H environment to the ordered bar.
chapters/theory/chiral_hochschild_koszul.tex:986:\index{Lagrangian self-intersection!Theorem H}
chapters/theory/e1_modular_koszul.tex:2116:\index{five main theorems!E1@$E_1$ (ordered)!Theorem H (modular)}



thinking
**Identifying output inconsistencies**

I’m noticing that the output format has some inconsistencies, mismatches, or gaps, and that could be a medium issue, but not necessarily explicit. However, if there’s a more severe problem, I might need to dig deeper to find any actual wrong claim status or broken labels. It's important to clarify everything to ensure I’m providing accurate information. Let’s figure this out together!
thinking
**Examining transition points carefully**

I need to check key seam files like README and others for transition points. It’s possible to find severe cases of bare kappa causing confusion, especially in theorem summaries. For instance, there are mentions like `README.md:25` and `ordered_associative_chiral_kd_core.tex:1335` that use kappa correctly. However, the user wants to avoid bare kappa in Volume II totally. I’ll focus on critical areas where undefined bare kappa arises and search specifically around cross-volume references.
thinking
**Searching for specific terms**

It looks like I need to search for instances of `V1-` and find any bare `\kappa` nearby. This could be a bit tricky since I want to be thorough but also focused. I’m wondering how to effectively narrow down my search, maybe by using a regex expression or something similar to pinpoint those terms. I just want to make sure I don’t miss anything critical in my findings! Let’s get started on that search.
codex
I’m now checking the affine convention bridge itself. The risky pattern is Vol II passages that start from a lambda-bracket, write a Laplace kernel, and then slide into calling it the same `r(z)` as Vol I’s collision residue without explicitly separating the two conventions. That’s where bare `\Omega/z` and wrong status claims tend to hide.
exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '1894,1910p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
  1894	\[
  1895	 r(z) = \int_0^\infty e^{-\lambda z}
  1896	 \{\cdot{}_\lambda\cdot\}\, d\lambda.
  1897	\]
  1898	For $V^k(\fg)$, the $\lambda$-bracket is
  1899	$\{J^a {}_\lambda J^b\} = f^{ab}_c J^c + k\,\kappa_\fg^{ab}\lambda$
  1900	(where $\kappa_\fg$ is the Killing form and $f^{ab}_c$ are the
  1901	structure constants). Evaluating the Laplace transform:
  1902	\[
  1903	 r(z) = \frac{\sum_{a,b} J^a \otimes J^b \cdot (\kappa_\fg)_{ab}}{z}
  1904	 + \frac{k\,\kappa_\fg}{z^2}
  1905	 = \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2},
  1906	\]
  1907	where $\Omega = \sum_a J^a \otimes J_a \in \fg \otimes \fg$
  1908	is the quadratic Casimir tensor. On evaluation modules
  1909	$V_i, V_j$, the representation $\rho_{ij}(\Omega)$ acts as
  1910	a finite-rank operator, and the $z^{-2}$ term is a scalar
exec
/bin/zsh -lc "nl -ba chapters/connections/celestial_holography_core.tex | sed -n '948,990p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_frontier.tex | sed -n '768,778p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd_core.tex | sed -n '3996,4011p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding.tex | sed -n '768,780p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '785,798p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   768	The family $\fS_b \to D^* = \Spec \CC((z))$ acquires a flat connection from the bar-complex structure of $V^k(\mathfrak{sl}_2)$. By Theorem~\ref{thm:reduced-equals-kz}, on the reduced evaluation comparison surface the reduced connection identifies with the KZ connection. On the full Steinberg object, the connection is
   769	\[
   770	 \nabla_\fS \;=\; d \;+\; \frac{1}{k+2}\,\Omega\,\frac{dz}{z},
   771	\]
   772	where $\Omega = e \ot f + f \ot e + \tfrac{1}{2} h \ot h$ is the split Casimir of $\mathfrak{sl}_2$.
   773	
   774	The connection is regular singular at $z = 0$ with residue $\Omega/(k+2)$. The regularity follows from bar-kernel absorption: the $d\log$ kernel absorbs one pole from the $z^{-2}$ OPE singularity $J^a(w)J^b(z) \sim k\kappa^{ab}/(w-z)^2 + f^{ab}_c J^c(z)/(w-z)$, so the collision $r$-matrix has a simple pole $r(z) = k\,\Omega/z + O(1)$ at level~$k$ The overall normalization $(k+2)^{-1}$ from Theorem~\ref{thm:reduced-equals-kz} converts this to the residue $\Omega/(k+2)$, and the $d\log z$ kernel absorbs the pole from $dz/z$, producing the claimed form.
   775	\end{construction}
   776	
   777	\subsection{Casimir spectrum and eigenvalue computation for general representations}
   778	\label{subsec:casimir-general}
 succeeded in 52ms:
  3996	All $3^3 \cdot (\text{mode triples}) = 27 \cdot
  3997	\text{(modes)}$ checks reduce to the Jacobi identity
  3998	for $\mathfrak{sl}_2[t]$.
  3999	
  4000	The \emph{classical Yang--Baxter equation} for the
  4001	Yangian $r$-matrix
  4002	$r_Y(z) = \hbar\,\Omega/z$ is:
  4003	\[
  4004	[r_{Y,12}(z_{12}),\,r_{Y,13}(z_{13})]
  4005	+ [r_{Y,12}(z_{12}),\,r_{Y,23}(z_{23})]
  4006	+ [r_{Y,13}(z_{13}),\,r_{Y,23}(z_{23})]
  4007	\;=\;0,
  4008	\]
  4009	which reduces (since $r_Y(z) = \hbar\,\Omega/z$ with
  4010	$\Omega$ the $\mathfrak{sl}_2$ Casimir) to the
  4011	classical YBE for $\Omega$, proved by the Jacobi
 succeeded in 52ms:
   948	The celestial holography programme maps $4$-dimensional scattering amplitudes to $2$-dimensional celestial CFT correlators via Mellin transform. The boundary chiral algebras of the holomorphic-topological framework (affine Kac--Moody for gauge theory, Virasoro for gravity) encode celestial OPE data through their bar complexes. The collision residues of the bar differential $d_{\barBch}$ extract these OPE coefficients via the $d\log$ absorption mechanism: the bar kernel $d\log(z_1 - z_2)$ absorbs one pole order, so an OPE singularity $\sim z^{-N}$ produces an $r$-matrix pole $\sim z^{-(N-1)}$.
   949	
   950	\subsection{Gluon celestial OPE from $\barBch(\widehat{\fg}_k)$}
   951	\label{subsec:ch-core-gluon-celestial-ope}
   952	
   953	The holomorphic-topological twist of $4$d $\mathcal{N} = 2$ Yang--Mills with gauge algebra $\fg$ on $\mathbb{C} \times \mathbb{R}_{\ge 0}$ produces a boundary Kac--Moody algebra $\widehat{\fg}_k$. The positive-helicity gluon maps to the affine current $J^a(z)$. The $\lambda$-bracket $\{J^a {}_\lambda J^b\} = f^{ab}{}_c\, J^c + k\,\kappa^{ab}\,\lambda$ Laplace-transforms to $r^{\mathrm{Lap}}(z) = f^{ab}{}_c\, J^c / z + k\,\kappa^{ab}/z^2$. After $d\log$ absorption, the $z^{-1}$ structure-constant term drops to $z^0$ and the $z^{-2}$ level term becomes $z^{-1}$:
   954	\[
   955	r^{\mathrm{KM}}(z) \;=\; \frac{k\,\Omega}{z}
   956	\;=\; \frac{k\,\kappa^{ab}\,t_a \otimes t_b}{z},
   957	\]
   958	where $\Omega$ is the Casimir tensor.
   959	
   960	\begin{evidence}[Celestial gluon OPE from the bar complex; \ClaimStatusHeuristic]
   961	\label{ev:ch-core-celestial-gluon-ope}
   962	Let $\mathcal{O}^{+,a}_{\Delta}(z)$ denote the celestial primary of a positive-helicity gluon of colour~$a$ and conformal dimension~$\Delta$. The celestial OPE extracted from the collision residue of $\barBch(\widehat{\fg}_k)$ is
   963	\[
   964	\mathcal{O}^{+,a}_{\Delta_1}(z_1)\,\mathcal{O}^{+,b}_{\Delta_2}(z_2)
   965	\;\sim\;
   966	\frac{f^{ab}{}_c}{z_1 - z_2}\;
   967	\mathcal{O}^{+,c}_{\Delta_1 + \Delta_2 - 1}(z_2)
 succeeded in 51ms:
   768	Poles in $z - w$ &
   769	 Poles in $u - v$ &
   770	 holomorphic $\leftrightarrow$ spectral \\[2pt]
   771	$\lambda$-bracket &
   772	 Sklyanin bracket~\eqref{eq:sklyanin-bracket} &
   773	 PVA $\leftrightarrow$ PVA \\[2pt]
   774	$r(z) = k\,\Omega/z$ &
   775	 $r_{\mathrm{cl}}(u) = P/u$ &
   776	 same Casimir \\[2pt]
   777	$\kappa = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$ &
   778	 $\kappa^! = -\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ &
   779	 complementarity \\[2pt]
   780	$\SCchtop$-algebra &
 succeeded in 50ms:
   785	
   786	\begin{proof}
   787	The invariant bilinear form at level $k$ on $\fg$ is
   788	$(\cdot,\cdot)_k = k\,\kappa(\cdot,\cdot)$. The associated
   789	Casimir tensor is $\Omega_k = k\,\kappa^{IJ}\,t_I \otimes t_J
   790	= k\,\Omega$. The standard rational solution of the CYBE for
   791	$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
   792	This is confirmed by the Laplace transform
   793	\textup{(}Proposition~\textup{\ref{prop:field-theory-r}}\textup{)}:
   794	the $\lambda$-bracket $\{J^I{}_\lambda\, J^J\}
   795	= f^{IJ}{}_K\, J^K + k\,\kappa^{IJ}\,\lambda$ gives
   796	the Laplace kernel
   797	\[
   798	 r^L(z) \;=\; \frac{f^{IJ}{}_K\,J^K}{z}

thinking
**Evaluating mathematical notation**

I'm noticing that writing this as `sum J^a\otimes J^b κ_ab / z` seems incorrect. The structure constant should actually transform into `J^a \otimes J^b κ_ab / z = Ω/z`, rather than `f^{ab}_c J^c / z`. That’s an important distinction since they replaced the Lie term with the Casimir, which isn’t the same. I need to inspect this further, especially looking at the λ-bracket and considering how the Laplace transform should connect to the structure constants.
codex
A more serious affine seam failure is live in `log_ht_monodromy_core.tex`: it turns the Laplace transform of the affine lambda-bracket directly into `\Omega/z + k\kappa/z^2`. That is not just a missing bridge label; it swaps the structure-constant term for the Casimir and skips the `d\log` absorption step that Vol I uses to get `k\Omega/z`. I’m checking whether the same faulty derivation survives in the active duplicate file.
exec
/bin/zsh -lc "rg -n -F \"= \\frac{\\Omega}{z} + \\frac{k\\,\\kappa_\\fg}{z"'^2}" chapters/connections/log_ht_monodromy_core.tex chapters/connections/log_ht_monodromy.tex chapters/connections/celestial_holography_core.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy.tex | sed -n '224,240p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '182,190p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 50ms:
chapters/connections/log_ht_monodromy_core.tex:1905: = \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2},
 succeeded in 51ms:
   224	\]
   225	which vanishes by the classical Yang-Baxter equation. Summing over all triples gives $A\wedge A=0$, hence $F=0$.
   226	\end{proof}
   227	
   228	\begin{lemma}[Residues and infinitesimal braid operators; \ClaimStatusProvedHere]% label removed: lem:inf-braid
   229	If $r(z)=k\,\Omega/z+O(1)$ at level~$k$ near $z=0$ and $\Omega_{ij}$ denotes the action of $\Omega$ in factors $i,j$, then
   230	\[
   231	 [\Omega_{ij},\Omega_{kl}]=0 \qquad \text{if }\{i,j\}\cap\{k,l\}=\varnothing,
   232	\]
   233	and
   234	\[
   235	 [\Omega_{ij},\Omega_{ik}+\Omega_{jk}]=0
   236	\]
   237	for distinct $i,j,k$.
   238	\end{lemma}
   239	
   240	\begin{proof}
exec
/bin/zsh -lc 'rg -n -F "all five theorems hold in the ordered" chapters/frame/guide_to_main_results.tex chapters/theory/e1_modular_koszul.tex chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   182	
   183	When $r(z)=k\,\Omega/z$ (the affine collision residue at level~$k$), this is exactly the classical rational KZ connection.
   184	
   185	\subsection{Flatness and residues}
   186	
   187	\begin{theorem}[Flatness of the shifted KZ/FM connection; \ClaimStatusProvedHere]\label{thm:strict-flatness}
   188	For every strict rational dg-shifted Yangian, the shifted KZ/FM connection is flat:
   189	\[
   190	 (\nabla_n^Y)^2=0.
exec
/bin/zsh -lc "nl -ba chapters/theory/e1_modular_koszul.tex | sed -n '2098,2130p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '1844,1869p'" in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:

 succeeded in 51ms:
  2098	${\Barch}^{\mathrm{ord}}(\cA_1 \otimes \cA_2) \cong
  2099	{\Barch}^{\mathrm{ord}}(\cA_1) \otimes
  2100	{\Barch}^{\mathrm{ord}}(\cA_2)$
  2101	(ordered shuffle theorem), and the monodromy of a product
  2102	connection is additive.
  2103	
  2104	(iii)~Anti-symmetry: opposite-duality gives
  2105	${\Barch}^{\mathrm{ord}}(\cA^{\op}) \cong
  2106	{\Barch}^{\mathrm{ord}}(\cA)^{\cop}$,
  2107	and the monodromy of the co-opposite is the inverse.
  2108	
  2109	(iv)~Coinvariant: by
  2110	Theorem~\ref{thm:e1-coinvariant-shadow} at degree~$2$.
  2111	\end{proof}
  2112	
  2113	\begin{theorem}[Theorem~$\mathrm{H}^{E_1}$ at all genera: ordered Hochschild at genus~$g$; \ClaimStatusProvedHere]
  2114	\label{thm:e1-theorem-H-modular}
  2115	\label{thm:e1-theorem-H}
  2116	\index{five main theorems!E1@$E_1$ (ordered)!Theorem H (modular)}
  2117	For every genus~$g$ and complete $\cA$-bimodule~$M$, the
 succeeded in 51ms:
  1844	
  1845	\subsection*{Virasoro and $\mathcal{W}_3$: the nonlinear tests}
  1846	
  1847	The Virasoro algebra ($\lambda$-bracket
  1848	$\{T {}_\lambda T\} = \partial T + 2T\lambda + (c/12)\lambda^3$,
  1849	in the Kac convention $\{a_\lambda b\} = \sum a_{(n)}b\,\lambda^n/n!$;
  1850	equivalently $(c/2)\lambda^{(3)}$ in divided-power notation, since $\lambda^{(3)} = \lambda^3/3! = \lambda^3/6$)
  1851	and the $\mathcal{W}_3$ algebra have genuinely infinite $\Ainf$
  1852	structures:
  1853	\begin{itemize}
  1854	\item OPE poles of order~$4$ (Virasoro) and~$6$ ($\mathcal{W}_3$):
  1855	 the bar complex has non-vanishing coderivations in all degrees.
  1856	 The $\Ainf$ structure is genuinely infinite.
  1857	\item Recursive construction of $m_k$ from the BV master equation
  1858	 (Theorem~\ref{thm:vir-recursive}): each $m_k$ is computed as a
  1859	 tree-level Feynman sum on $\FM_k(\C) \times \Conf_k^{<}(\R)$,
  1860	 with the vertices determined by the interaction term
  1861	 $\eta \Pi^{ij}(\partial) \eta$ of the Khan--Zeng 3d HT Poisson
  1862	 sigma model.
  1863	\item Classical Yang--Baxter: the $\lambda$-bracket of Virasoro

thinking
**Addressing seam issues**

I see that the introduction correctly distinguishes between c/12 and c/2, and mentions the Laplace kernel. This can potentially help with the log_ht_monodromy_core and the c/12 issue in 3d_gravity. However, I still need to look into other seam problems. The user specifically requested no bare kappa in Volume II, so I need to locate live seam transition passages, such as in `3d_gravity.tex:834`. It's definitely worth checking the seam table in `spectral-braiding.tex:777-778` as well.
exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding.tex | sed -n '772,780p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '800,816p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '136,146p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4898,4912p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"\\\\kappa(?"'!'"\\()|\\bkappa\\b\" chapters/connections/spectral-braiding.tex chapters/connections/holomorphic_topological.tex chapters/theory/introduction.tex chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"r(z) = \\Omega/z\" chapters/connections/log_ht_monodromy_core.tex chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/holomorphic_topological.tex chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   772	 Sklyanin bracket~\eqref{eq:sklyanin-bracket} &
   773	 PVA $\leftrightarrow$ PVA \\[2pt]
   774	$r(z) = k\,\Omega/z$ &
   775	 $r_{\mathrm{cl}}(u) = P/u$ &
   776	 same Casimir \\[2pt]
   777	$\kappa = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$ &
   778	 $\kappa^! = -\dim(\fg)(k{+}h^\vee)/(2h^\vee)$ &
   779	 complementarity \\[2pt]
   780	$\SCchtop$-algebra &
 succeeded in 51ms:
   800	 fiber~\cite{Costello2111}. This shifts the effective level to
   801	 $k_{\mathrm{eff}} = k - h^\vee$.
   802	
   803	\item $\kappa(\widehat{\mathfrak{g}}_k)
   804	 = \dim(\mathfrak{g})(k + h^\vee)/(2h^\vee)$: the modular
   805	 characteristic of the boundary VOA
   806	 \textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)},
   807	 controlling the genus expansion
   808	 $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ At $k = 0$: $\kappa = \dim(\mathfrak{g})/2$.
   809	\end{enumerate}
   810	There is no universal proportionality constant between these
   811	invariants. The ratio $b_0^{4\mathrm{d}}/\kappa$
   812	depends on~$N$: for $\mathrm{SU}(2)$ it is $22/9$; for
   813	$\mathrm{SU}(3)$ it is $11/4$; as $N \to \infty$ it tends
   814	to zero.
   815	
   816	The correct bridge is the \emph{one-loop level shift}:
 succeeded in 52ms:
   136	boundary fixes the shifted-cotangent side of the bulk
   137	reconstruction (Theorem~\ref{thm:holographic-reconstruction}),
   138	but recovering the actual formal neighborhood requires the
   139	formal Darboux theorem for $(-2)$-shifted symplectic stacks.
   140	The holographic principle, on this surface, is the Darboux
   141	theorem.
   142	
   143	The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
   144	
   145	\section*{The differential: holomorphic factorisation}
   146	
 exited 2 in 50ms:
rg: regex parse error:
    (?:\kappa(?!\()|\bkappa\b)
       ^^
error: unrecognized escape sequence
 succeeded in 51ms:

 exited 1 in 50ms:



thinking
**Troubleshooting regex issues**

I think `rg` regex isn’t working, possibly due to PCRE? Maybe I could try `rg -n -P`, but I wonder if it’s necessary. I need to find instances of bare kappa in line 143, which mentions `\kappa(\cA)` and later `d_barB^2 = \kappa \cdot \omega_g`. This seems like a seam issue since the same sentence defines \(\kappa(\cA)\). I should replace occurrences with `\kappa(\cA)` or `\kappa(\widehat{\fg}_k)`. Also, I found other instances where I need to ensure there are no bare Omega/z, as the user pointed out!
thinking
**Searching for bare Ω/z instances**

I suspect there are actual bare `Ω/z` instances in the text. I need to search for the exact fixed string `\Omega/z`, while making sure it's not preceded by "k" or "\hbar," which could be tricky. Using simple grep for `Ω/z` already shows many entries with `kΩ/z`. I’ll look for `\\Omega/z` specifically and inspect lines that don’t have preceding "k" or "\hbar." The active file `log_ht_monodromy_core.tex:1905` has this exact string. I’ll run a search with `rg -n "\\Omega/z"` to list all occurrences and check for any additional bare instances.
codex
I have enough to separate three defect types now: an E1/E∞ hierarchy drift, a Virasoro divided-power drift, and an affine Laplace/collision conflation. I’m doing one last scan for live seam lines where Vol II still uses bare `\kappa` or bare `\Omega/z` in summary tables, because those tend to survive after the formula-level fixes.
exec
/bin/zsh -lc 'rg -n -P "(?<![A-Za-z0-9_'"\\\\])\\\\Omega/z\" chapters/README.md README.md chapters/connections chapters/theory chapters/examples" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P \"\\\\kappa(?"'!'"\\()\" chapters/connections/concordance.tex chapters/theory/introduction.tex chapters/connections/holomorphic_topological.tex chapters/connections/spectral-braiding.tex README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '904,968p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding.tex | sed -n '1276,1324p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '1895,1908p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4898,4911p'" in /Users/raeez/chiral-bar-cobar-vol2 exited 2 in 51ms:
rg: PCRE2: error compiling pattern at offset 23: unrecognized character follows \
 exited 2 in 50ms:
rg: PCRE2: error compiling pattern at offset 5: \k is not followed by a braced, angle-bracketed, or quoted name
 succeeded in 50ms:
   904	 insertion. This recursion is the
   905	 Britto--Cachazo--Feng--Witten on-shell recursion for the
   906	 holomorphic twist.
   907	
   908	\item \emph{Soft limits.}
   909	 The $(n{+}1)$-point amplitude in the conformally soft limit
   910	 $z_{n+1} \to \infty$ satisfies
   911	 $\mathcal{A}_{n+1} \to S^{(0)} \cdot \mathcal{A}_n$
   912	 with leading soft factor
   913	 $S^{(0)} = \sum_k (z_{n+1} - z_k)^{-1}$.
   914	 The coefficient of the leading soft factor is
   915	 $\kappa = S_2$\textup{;}
   916	 the subleading soft graviton theorem is controlled by the
   917	 cubic shadow
   918	 $S_3 = 2$
   919	 \textup{(}universal for all chiral algebras with a stress
   920	 tensor\textup{)}.
   921	
   922	\item \emph{Color-ordered amplitudes.}
   923	 For affine $\mathfrak{sl}_N$ at level~$k$, the color-ordered
 succeeded in 51ms:
  1276	 $\R$ is contractible at all genera. The Arnold defect
  1277	 (quasi-periodic monodromy of $\FM_k(\Sigma_g)$) contributes
  1278	 only to the closed color.
  1279	\item \emph{Complementarity.}
  1280	 $\kappa(\cA) + \kappa(\cA^!) = 0$ for Kac--Moody and free-field algebras
  1281	 (Vol~I, Theorem~C; for Virasoro, $\kappa + \kappa^! = 13$).
  1282	 The total bulk--boundary pair $(\cA, \cA^!)$
  1283	 is ``uncurved on average'' in the KM case: the closed-color curvature of
  1284	 $\cA$ and $\cA^!$ cancel, so the full bulk theory
  1285	 sees no net genus-$g$ anomaly.
  1286	\end{enumerate}
  1287	\end{theorem}
  1288	
  1289	\begin{proof}
  1290	(i) is Theorem~\ref{cor:mc5-genus-one-bridge} at genus~$1$,
  1291	extended to all genera by the genus tower of Vol~I\@. The bar
  1292	differential on $\Sigma_g$ acquires curvature from the period
  1293	matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
  1294	$\omega_g$ is the canonical Arakelov $(1,1)$-form
  1295	(equation~\eqref{eq:curved-R-fact}).
 succeeded in 50ms:
  1895	 r(z) = \int_0^\infty e^{-\lambda z}
  1896	 \{\cdot{}_\lambda\cdot\}\, d\lambda.
  1897	\]
  1898	For $V^k(\fg)$, the $\lambda$-bracket is
  1899	$\{J^a {}_\lambda J^b\} = f^{ab}_c J^c + k\,\kappa_\fg^{ab}\lambda$
  1900	(where $\kappa_\fg$ is the Killing form and $f^{ab}_c$ are the
  1901	structure constants). Evaluating the Laplace transform:
  1902	\[
  1903	 r(z) = \frac{\sum_{a,b} J^a \otimes J^b \cdot (\kappa_\fg)_{ab}}{z}
  1904	 + \frac{k\,\kappa_\fg}{z^2}
  1905	 = \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2},
  1906	\]
  1907	where $\Omega = \sum_a J^a \otimes J_a \in \fg \otimes \fg$
  1908	is the quadratic Casimir tensor. On evaluation modules
 succeeded in 51ms:

codex
Another seam defect surfaced in the main Vol II introduction: it states `d_{\barB}^2 = \kappa \cdot \omega_g`. That is not a wording quibble; it contradicts Vol I’s corrected distinction between the bar differential (always square-zero) and the fiberwise genus correction (`d_{\mathrm{fib}}^{\,2} = \kappa(\cA)\cdot\omega_g`). I’m checking whether that bad equation survives elsewhere in live Vol II summaries.
exec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 = '"\\kappa\" chapters README.md" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 =" chapters README.md' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '140,144p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '236,247p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '4898,4907p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"d_{\\mathrm{fib}}"'^{'"\\,2} = \\kappa\" chapters README.md" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
chapters/connections/spectral-braiding-core.tex:3847:matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
chapters/connections/spectral-braiding-core.tex:3926: genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
chapters/connections/3d_gravity.tex:9159:$d_{\barB}^2 = \kappa\cdot\omega_1$ at genus~$1$ encodes both
chapters/connections/thqg_bv_ht_extensions.tex:1447:d_{\barB}^2 = \kappa(\cA) \cdot \omega_g,
chapters/connections/thqg_bv_ht_extensions.tex:1502:d_{\barB}^2 = \kappa \cdot \hbar.
chapters/connections/thqg_bv_ht_extensions.tex:1575:bar construction). Since $d_{\barB}^2 = \kappa_{\mathrm{tot}} \cdot
chapters/connections/conclusion.tex:1643:confirming\/ $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at\/ $g = 1$
chapters/connections/spectral-braiding.tex:1293:matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
chapters/connections/spectral-braiding.tex:1368: genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
chapters/connections/ht_bulk_boundary_line_frontier.tex:1131: $d_{\barB}^2 = \kappa \cdot \omega_g$ records that the
chapters/theory/foundations.tex:2192:cohomology class: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$.
chapters/theory/foundations.tex:2225: The equation $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ is the
chapters/theory/foundations.tex:2382:Curvature $F = dA + A \wedge A$ & $d_{\barB}^2 = \kappa \cdot \omega_g$ & Theorem (Vol~I, Thm~D) \\
chapters/theory/introduction.tex:143:The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
chapters/theory/introduction.tex:535:The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.
chapters/theory/axioms.tex:72:When $m_0 = \kappa(\cA) \cdot \omega_g$ for a scalar $\kappa$ and a base class $\omega_g$, the $n=1$ relation reduces to $d_{\barB}^2 = \kappa \cdot \omega_g$ (Volume~I, Theorem~D): the bar differential fails to square to zero by exactly the curvature obstruction, and this failure IS the non-formality at genus $g \geq 1$. Setting $m_0 = 0$ recovers Definition~\ref{def:ainfty_chiral}.
chapters/theory/foundations_recast_draft.tex:524: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_1$ is the Hodge anomaly:
chapters/theory/foundations_recast_draft.tex:715: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \ge 1$.
 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:168:The nilpotence $d_{\barB}^2 = 0$ is the Arnold relation
chapters/examples/rosetta_stone.tex:612:d_{\barB})$ is an honest chain complex: $d_{\barB}^2 = 0$,
chapters/examples/rosetta_stone.tex:781:conformally invariant: $d_{\barB}^2 = 0$ and the partition function
chapters/examples/rosetta_stone.tex:1093:reduces to $d_{\barB}^2 = 0$ (the Arnold relation, verified in
chapters/connections/thqg_bv_ht_extensions.tex:1447:d_{\barB}^2 = \kappa(\cA) \cdot \omega_g,
chapters/connections/thqg_bv_ht_extensions.tex:1458:The bar differential $d_{\barB}$ satisfies $d_{\barB}^2 = 0$ at genus 0
chapters/connections/thqg_bv_ht_extensions.tex:1502:d_{\barB}^2 = \kappa \cdot \hbar.
chapters/connections/thqg_bv_ht_extensions.tex:1553:The bar complex of the combined system satisfies $d_{\barB}^2 = 0$ at
chapters/connections/thqg_bv_ht_extensions.tex:1575:bar construction). Since $d_{\barB}^2 = \kappa_{\mathrm{tot}} \cdot
chapters/connections/thqg_bv_ht_extensions.tex:1588:vanishes and the bar complex satisfies $d_{\barB}^2 = 0$ at all genera.
chapters/connections/3d_gravity.tex:2333:the same cancellation that gives $d_{\barB}^2 = 0$, projected to
chapters/connections/3d_gravity.tex:8911:\begin{theorem}[Crossing = $d_{\barB}^2 = 0$; \ClaimStatusProvedHere]
chapters/connections/3d_gravity.tex:8945:d_{\barB}^2 = 0
chapters/connections/3d_gravity.tex:9159:$d_{\barB}^2 = \kappa\cdot\omega_1$ at genus~$1$ encodes both
chapters/connections/3d_gravity.tex:9182: & Stasheff identity ($d_{\barB}^2 = 0$)
chapters/connections/ht_bulk_boundary_line_frontier.tex:1131: $d_{\barB}^2 = \kappa \cdot \omega_g$ records that the
chapters/connections/spectral-braiding.tex:1293:matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
chapters/connections/spectral-braiding.tex:1367: closed-color component gives $d_{\barB}^2 = 0$ (at
chapters/connections/spectral-braiding.tex:1368: genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
chapters/connections/bar-cobar-review.tex:623:\textbf{Step 3: Flatness.} The flatness of the connection is equivalent to $d_{\barB}^2 = 0$:
 succeeded in 52ms:
   236	\item The cogenerator projection of the fiberwise bar differential
   237	 $\dfib$ coincides with the Feynman-defined operations:
   238	 $\pi_1 \circ \dfib|_{\barB^k(\cA)} = m_k^{E_\tau}$.
   239	\item The fiberwise bar differential satisfies
   240	 \begin{equation}
   241	 % label removed: eq:mc5-genus1-curvature
   242	 \dfib^{\,2} = \kappa(\cA) \cdot \omega_1,
   243	 \end{equation}
   244	 where $\omega_1 = \frac{i}{2\operatorname{Im}(\tau)}\,dz \wedge
   245	 d\bar{z}$ is the Arakelov $(1,1)$-form and $\kappa(\cA)$ is the
   246	 modular characteristic of Volume~I. The curvature arises from
   247	 the Arnold defect on the torus: the quasi-periodicity of the
 succeeded in 52ms:
   140	The holographic principle, on this surface, is the Darboux
   141	theorem.
   142	
   143	The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
   144	
 succeeded in 51ms:

 succeeded in 52ms:
chapters/connections/3d_gravity.tex:8793:$d_{\mathrm{fib}}^{\,2} = \kappa\,\omega_1$ introduces a correction:



thinking
**Analyzing audit scope**

I’m noticing several issues related to `d_barB^2`. The user asked for a seam audit that includes an introduction, theory, conclusions, and other components, but I’m realizing I might not need to cover everything across the whole repository. The task indicates we need to exhaustively audit every inconsistency at seams. So, I’ll need to decide on the scope, focusing on transition points rather than all uses. We may want to include all verified active seam files, possibly listing each relevant line for clarity.
thinking
**Examining cross-volume findings**

Since this is related to Volume I corrections, I should consider listing each file and line I checked. I might include around 5-6 occurrences, but that could be excessive. However, to fulfill the task, listing all lines I reviewed makes sense. I’ll inspect a few key files, like introduction lines 143 and 535, and specific lines from spectral-braiding and conclusions. It's a lot, but not every line may be a transition point, even though they connect to Theorem D. A final summary with about 10-15 findings could work well.
thinking
**Considering finding format**

I'm thinking about whether I can group multiple line references from the same file into a single finding. The suggested format is `[SEVERITY] file:line — PROBLEM: ... FIX: ...`, which makes it seem like I should focus on one line at a time. I could mention multiple lines under the same problem, but maybe it would be clearer to keep them separate or list the first line and mention any duplicates within the same sentence for better clarity.
exec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 = '"\\kappa\\cdot\\omega_1\" chapters/connections/3d_gravity.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"Volume~I establishes five main theorems for E_\\infty-chiral algebras\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "cohomology is polynomial in the cumulants" chapters' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 = '"\\kappa \\cdot \\omega_g\" chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/connections/spectral-braiding.tex chapters/connections/spectral-braiding-core.tex chapters/connections/conclusion.tex chapters/connections/3d_gravity.tex chapters/connections/thqg_bv_ht_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"F_g = \\kappa \\cdot \\lambda_g"'^{'"\\mathrm{FP}}\" chapters/connections/holomorphic_topological.tex chapters/connections/concordance.tex chapters/theory/introduction.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 = '"\\kappa(\\cA) \\cdot \\omega_g\" chapters/theory/introduction.tex chapters/theory/foundations.tex chapters/connections/spectral-braiding.tex chapters/connections/spectral-braiding-core.tex chapters/connections/conclusion.tex chapters/connections/3d_gravity.tex chapters/connections/thqg_bv_ht_extensions.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
9159:$d_{\barB}^2 = \kappa\cdot\omega_1$ at genus~$1$ encodes both
 exited 1 in 51ms:

 succeeded in 51ms:
chapters/connections/twisted_holography_quantum_gravity.tex:2745: cohomology is polynomial in the cumulants. The critical level $k = -h^\vee$
 succeeded in 51ms:
chapters/connections/spectral-braiding.tex:1368: genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
chapters/connections/spectral-braiding-core.tex:3926: genus~$0$) or $d_{\barB}^2 = \kappa \cdot \omega_g$ (at
chapters/theory/foundations.tex:2382:Curvature $F = dA + A \wedge A$ & $d_{\barB}^2 = \kappa \cdot \omega_g$ & Theorem (Vol~I, Thm~D) \\
chapters/theory/introduction.tex:143:The $(-2)$-shifted symplectic geometry of the formal neighborhood is governed by three representation-theoretic invariants computed in Volume~I. The modular characteristic $\kappa(\cA)$ controls the curvature of the Lagrangian embedding: it is the scalar such that $d_{\barB}^2 = \kappa \cdot \omega_g$, where $\omega_g$ is the Hodge class on $\overline{\cM}_g$. The complementarity theorem (Volume~I, Theorem~C) lifts to the bulk-boundary-line triangle: the decomposition $Q_g(\cA) + Q_g(\cA^!) = H^*(\overline{\cM}_g, Z(\cA))$ becomes a Lagrangian splitting of the self-intersection complex, under perfectness and chain-level nondegeneracy hypotheses (satisfied for all standard families; conditional in general). Three structure theorems from Volume~I govern the formal neighborhood. \emph{Algebraicity} (the Riccati theorem: $H(t)^2 = t^4 Q_L(t)$, with $Q_L$ quadratic) determines the growth rate $\rho$ of the shadow obstruction tower and hence the convergence of the genus expansion. \emph{Formality identification} (the shadow obstruction tower equals the $L_\infty$ formality obstruction tower at all degrees, proved by induction on~$r$ in Volume~I) explains why the Lagrangian extension terminates for some algebras and accumulates infinitely for others: tower termination is $L_\infty$ formality. \emph{Complementarity} lifts to the holomorphic-topological split: the $(-1)$-shifted symplectic structure on the self-intersection complex $C_g(\cA)$ (inherited from the $(-2)$-shifted ambient stack) is the geometric incarnation of the Lagrangian decomposition $C_g(\cA) = Q_g(\cA) + Q_g(\cA^!)$, under perfectness and chain-level nondegeneracy hypotheses satisfied by all standard families. The shadow depth classification $\mathbf{G}/\mathbf{L}/\mathbf{C}/\mathbf{M}$ of Volume~I becomes a classification of bulk-boundary pairs by the critical discriminant $\Delta = 8\kappa S_4$. Class~$\mathbf{G}$ ($\Delta = 0$) is formal: the bulk is determined classically, the Lagrangian self-intersection is clean, and no higher $\Ainf$ operations survive. Classes $\mathbf{L}$, $\mathbf{C}$, and $\mathbf{M}$ ($\Delta \neq 0$) are genuinely curved: the self-intersection carries excess Tor, and the higher $\Ainf$ operations encode the successive obstruction classes. The boundary algebra $A_b$ is recovered from the genus-$0$ closed data of the universal MC element~$\Theta_\cA$ from Volume~I, while the higher-genus shadow data descend through the shadow obstruction tower.
 succeeded in 50ms:
chapters/connections/holomorphic_topological.tex:808: $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ At $k = 0$: $\kappa = \dim(\mathfrak{g})/2$.
chapters/connections/holomorphic_topological.tex:1250:gives $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ at
 succeeded in 51ms:
chapters/connections/conclusion.tex:1643:confirming\/ $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at\/ $g = 1$
chapters/connections/thqg_bv_ht_extensions.tex:1447:d_{\barB}^2 = \kappa(\cA) \cdot \omega_g,
chapters/connections/spectral-braiding-core.tex:3847:matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
chapters/connections/spectral-braiding.tex:1293:matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
chapters/theory/foundations.tex:2192:cohomology class: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$.
chapters/theory/foundations.tex:2225: The equation $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ is the
chapters/theory/introduction.tex:535:The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.
exec
/bin/zsh -lc 'rg -n -F "Volume~I establishes five main theorems for" chapters/connections/ordered_associative_chiral_kd_core.tex chapters/connections/ordered_associative_chiral_kd.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/ordered_associative_chiral_kd.tex | sed -n '1218,1276p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '1246,1254p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '1910,1924p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '8848,8856p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "The $E_1$ vs. $E_'"\\infty"'$ content." chapters/connections/concordance.tex chapters/theory/e1_modular_koszul.tex chapters/theory/introduction.tex chapters/theory/bar_cobar_adjunction_curved.tex chapters/frame/guide_to_main_results.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/connections/ordered_associative_chiral_kd_core.tex:1274:Volume~I establishes five main theorems for $E_\infty$-chiral algebras: bar-cobar adjunction, Koszul inversion, complementarity, leading coefficient, and the Hochschild ring. Each has an $E_1$-chiral counterpart, obtained by replacing symmetric coinvariants with the ordered bar complex and its braid-group equivariance. The five $E_1$ theorems at genus zero are formal consequences of the master theorem (Theorem~\ref{thm:master}) together with the explicit constructions of Appendix~\ref{sec:ordered-bar-explicit}; they are collected here to make the parallel with Vol~I explicit.
 succeeded in 52ms:
  1218	\begin{theorem}[Theorem~$\mathrm{A}^{E_1}$; \ClaimStatusProvedHere]
  1219	% label removed: thm:e1-theorem-A
  1220	\index{five main theorems!E1@$E_1$ variant!Theorem A}
  1221	$\Cobar \dashv \Barch\colon
  1222	\mathsf{Alg}^{E_1}_{\mathrm{ch}} \rightleftarrows
  1223	\mathsf{Coalg}^{E_1}_{\mathrm{ch}}$.
  1224	Koszul exchange acts by $R^{-1}(z)$
  1225	\textup{(}Theorem~\textup{\ref{thm:opposite}}).
  1226	\end{theorem}
  1227	
  1228	\begin{proof}
  1229	Ordered bar--cobar equivalence (\S\ref{sec:setup}) plus
  1230	opposite-duality (Theorem~\ref{thm:opposite}).
  1231	\end{proof}
  1232	
  1233	\begin{theorem}[Theorem~$\mathrm{B}^{E_1}$; \ClaimStatusProvedHere]
  1234	% label removed: thm:e1-theorem-B
  1235	\index{five main theorems!E1@$E_1$ variant!Theorem B}
  1236	On the $E_1$ Koszul locus,
  1237	$\Cobar(\Barch(\cA)) \xrightarrow{\sim} \cA$.
 succeeded in 51ms:
  1910	a finite-rank operator, and the $z^{-2}$ term is a scalar
  1911	(proportional to the identity on $V_i \otimes V_j$). The
  1912	scalar term does not contribute to the braiding (it exponentiates
  1913	to a scalar phase), so the braiding is governed by
  1914	$r(z) = k\,\Omega/z$ at level~$k$ up to scalars.
  1915	
  1916	\smallskip\noindent
  1917	\emph{Step (iii-c): Exponentiation to KZ monodromy.}
  1918	The flat connection with connection form
  1919	$\Omega_{ij}\, d\log(z_i - z_j)/(k + h^\vee)$ is precisely
  1920	the KZ connection of Theorem~\ref{thm:reduced-equals-kz}.
  1921	Its half-monodromy (the braiding operator obtained by
  1922	analytically continuing $z_i$ around $z_j$ along a half-circle)
  1923	is
  1924	\[
 succeeded in 51ms:
  1246	$\kappa(\cA_{\mathrm{Burns}}) = 4$ (free-field additivity:
  1247	four copies of $\kappa(\beta\gamma_1) = 1$).
  1248	Since all generators have conformal weight~$\lambda = 1$
  1249	(uniform-weight), Theorem~\ref{thm:genus-universality}
  1250	gives $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ at
  1251	all genera. At genus~$2$:
  1252	\[
  1253	F_2(\cA_{\mathrm{Burns}})
  1254	\;=\;
 succeeded in 51ms:
  8848	\end{tabular}
  8849	\end{center}
  8850	
  8851	\begin{remark}[Semiclassical hierarchy]
  8852	At large $c$ ($G \to 0$): $S^{(0)}$ and $S^{(1)}$ are exact
  8853	(order $G^0$); $S^{(2)}_{\text{contact}} \sim 2/(5c^2)$
  8854	(order $G^2$); $S_5 \sim -48/(5c^3)$
  8855	(order $G^3$).
  8856	The entire infinite tower beyond $S^{(1)}$ is invisible
 exited 1 in 51ms:

exec
/bin/zsh -lc "nl -ba chapters/theory/foundations.tex | sed -n '2188,2230p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  2188	
  2189	At genus~$0$ the bar complex is honest: $d_{\barB}^2 = 0$.
  2190	At genus~$g \geq 1$, Volume~I Theorem~D shows that the
  2191	bar differential squares to a scalar multiple of a moduli-space
  2192	cohomology class: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$.
  2193	This curvature is not a defect but
  2194	a structure: it measures exactly how much monodromy the
  2195	$D$-module connection acquires around the $B$-cycles
  2196	of~$\Sigma_g$, and it controls the genus tower of the theory.
  2197	This subsection develops the consequences: the
  2198	curved bar complex lives in the coderived category (Positselski's
  2199	framework), the bar-cobar
  2200	adjunction lifts to the curved setting, and the delooping of a
  2201	curved algebra determines a line bundle over the moduli space whose
  2202	first Chern class is the modular characteristic.
  2203	
  2204	\begin{definition}[Curved $\Ainf$ chiral algebra]
  2205	\label{def:curved-Ainf-chiral}
  2206	A logarithmic $\SCchtop$-algebra $\cA$
  2207	(Definition~\ref{def:log-SC-algebra}) is \emph{curved}
exec
/bin/zsh -lc "nl -ba chapters/theory/foundations.tex | sed -n '2378,2385p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  2378	\toprule
  2379	\textbf{Gauge theory} & \textbf{Chiral bar complex} & \textbf{Status} \\
  2380	\midrule
  2381	Connection $A$ & Bar differential $d_{\barB}$ & Structural analogy \\
  2382	Curvature $F = dA + A \wedge A$ & $d_{\barB}^2 = \kappa \cdot \omega_g$ & Theorem (Vol~I, Thm~D) \\
  2383	First Chern number $c_1$ & Modular characteristic $\kappa(\cA)$ & Structural analogy \\
  2384	Flat connection ($F = 0$) & Uncurved ($\kappa = 0$, genus $0$) & Tautology \\
  2385	Holonomy of flat connection & $R$-matrix $R(z) = \cP\exp(\int r)$ & Theorem (affine lineage) \\
exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding.tex | sed -n '1288,1324p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/conclusion.tex | sed -n '442,455p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/conclusion.tex | sed -n '1638,1645p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '3842,3928p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  1288	
  1289	\begin{proof}
  1290	(i) is Theorem~\ref{cor:mc5-genus-one-bridge} at genus~$1$,
  1291	extended to all genera by the genus tower of Vol~I\@. The bar
  1292	differential on $\Sigma_g$ acquires curvature from the period
  1293	matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
  1294	$\omega_g$ is the canonical Arakelov $(1,1)$-form
  1295	(equation~\eqref{eq:curved-R-fact}).
  1296	
  1297	(ii): The deconcatenation coproduct $\Delta$ on the cofree
  1298	coalgebra $T^c(V)$ is defined purely combinatorially by
  1299	$(v_1 | \cdots | v_n) \mapsto
  1300	\sum_{i=0}^n (v_1 | \cdots | v_i) \otimes
  1301	(v_{i+1} | \cdots | v_n)$. This involves no integrals, no
  1302	propagators, and no curve geometry. Coassociativity
  1303	$(\Delta \otimes \id) \circ \Delta
  1304	= (\id \otimes \Delta) \circ \Delta$ is an identity of graded
  1305	vector spaces, valid at every genus.
  1306	
  1307	(iii): The $\SCchtop$ operad has closed-color spaces
 succeeded in 51ms:
   442	
   443	\subsection{Geometric Langlands as the $\kappa=0$ slice}
   444	
   445	The bar-cobar programme parametrises a family of Swiss-cheese
   446	coalgebras indexed by the modular characteristic~$\kappa$. At
   447	generic~$\kappa$, the bar complex is curved: $d_{\barB}^2 =
   448	\kappa(\cA)\cdot\omega_g$, and the genus tower is controlled by the
   449	$\hat{A}$-genus. The curvature is the obstruction to extending the
   450	genus-$0$ Lagrangian through the boundary strata of~$\Mbar_{g,n}$.
   451	
   452	At $\kappa = 0$, the bar complex is uncurved at all genera: $d_{\barB}^2 =
   453	0$, and the genus tower collapses. For an affine Kac--Moody algebra
   454	$\widehat{\fg}_k$, this occurs at the critical level $k = -h^\vee$,
   455	where $\kappa(\widehat{\fg}_{-h^\vee}) = 0$. The bar complex is
 succeeded in 51ms:
  1638	\label{eq:genus-1-bar-curvature}
  1639	 d_{\barB}^2\big|_{g=1}
  1640	 \;=\;
  1641	 \kappa(\cA) \cdot E_2(\tau) \cdot \omega_1,
  1642	\end{equation}
  1643	confirming\/ $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at\/ $g = 1$
  1644	\textup{(}Vol~I, Theorem~D\textup{)}. The period correction
  1645	$F_1(\cA) = \kappa(\cA)/24$ restores the total differential
 succeeded in 51ms:
  3842	
  3843	\begin{proof}
  3844	(i) is Theorem~\ref{cor:mc5-genus-one-bridge} at genus~$1$,
  3845	extended to all genera by the genus tower of Vol~I\@. The bar
  3846	differential on $\Sigma_g$ acquires curvature from the period
  3847	matrix: $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ where
  3848	$\omega_g$ is the canonical Arakelov $(1,1)$-form
  3849	(equation~\eqref{eq:curved-R-fact}).
  3850	
  3851	(ii): The deconcatenation coproduct $\Delta$ on the cofree
  3852	coalgebra $T^c(V)$ is defined purely combinatorially by
  3853	$(v_1 | \cdots | v_n) \mapsto
  3854	\sum_{i=0}^n (v_1 | \cdots | v_i) \otimes
  3855	(v_{i+1} | \cdots | v_n)$. This involves no integrals, no
  3856	propagators, and no curve geometry. Coassociativity
  3857	$(\Delta \otimes \id) \circ \Delta
  3858	= (\id \otimes \Delta) \circ \Delta$ is an identity of graded
  3859	vector spaces, valid at every genus.
  3860	
  3861	(iii): The $\SCchtop$ operad has closed-color spaces


thinking
**Clarifying mathematical terms**

I'm noticing a potential issue in the reference to "leading coefficient" instead of "modular characteristic" at `ordered_associative_chiral_kd_core:1274`. This seems crucial since it lists five main theorems: bar-cobar adjunction, Koszul inversion, complementarity, leading coefficient, and Hochschild ring. Maybe I need to confirm if that terminology is correct or if it needs revisiting. It's intriguing how terminology can shift understanding in mathematics!
thinking
**Reviewing theorem attributions**

I’m noticing that in `spectral-braiding.tex`, lines 1318-1319 might correctly attribute complementarity to Theorem C, with only a core duplicate being wrong. I’ll need to make an exact fix by changing `VolI, TheoremD` to `VolI, TheoremC`, which feels like a crisp adjustment. I wonder if there are other theorem-attribution issues. I should search for `TheoremD` near complementarity or `TheoremC` with modular characteristics, possibly checking Vol II chapters and using rg patterns for efficiency.
codex
I found a clean status-attribution bug too: one active `spectral-braiding-core` line cites Vol I Theorem D for the nonzero `\kappa+\kappa^!` statement, but that is Theorem C territory, not D. I’m scanning for other nearby C/D swaps before I lock the findings list.
exec
/bin/zsh -lc "nl -ba chapters/connections/holomorphic_topological.tex | sed -n '806,812p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex | sed -n '528,537p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '3872,3882p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n \"Theorem~C; for .*\\\\kappa|Theorem~D; for .*\\\\kappa|Theorem~D\\).*\\\\kappa \\+ \\\\kappa|Theorem~C\\).*modular characteristic|Theorem~D\\).*complementarity|Theorem~C\\).*leading coefficient\" chapters" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Vol~I, Theorem~C" chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding.tex chapters/connections/twisted_holography_quantum_gravity.tex chapters/connections/holomorphic_topological.tex chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc 'rg -n -F "Vol~I, Theorem~D" chapters/connections/spectral-braiding-core.tex chapters/connections/spectral-braiding.tex chapters/connections/twisted_holography_quantum_gravity.tex chapters/connections/holomorphic_topological.tex chapters/theory/introduction.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
  3872	(iv): For the affine lineage (where the Feigin--Frenkel
  3873	involution $k \mapsto -k - 2\hvee$ ensures
  3874	$\kappa(\cA) + \kappa(\cA^!) = 0$; Vol~I, Theorem~C
  3875	specialized to Kac--Moody and free-field algebras),
  3876	the closed-color curvatures
  3877	$\kappa(\cA) \cdot \omega_g$ and
  3878	$\kappa(\cA^!) \cdot \omega_g = -\kappa(\cA) \cdot \omega_g$
  3879	cancel when one passes to the full bulk theory controlled by
  3880	the Koszul pair $(\cA, \cA^!)$. For $\mathcal{W}$-algebras
  3881	the sum $\kappa + \kappa^!$ is in general nonzero
  3882	(Vol~I, Theorem~D).
 succeeded in 51ms:
   806	 \textup{(}Theorem~\textup{\ref{thm:modular-characteristic}}\textup{)},
   807	 controlling the genus expansion
   808	 $F_g = \kappa \cdot \lambda_g^{\mathrm{FP}}$ At $k = 0$: $\kappa = \dim(\mathfrak{g})/2$.
   809	\end{enumerate}
   810	There is no universal proportionality constant between these
   811	invariants. The ratio $b_0^{4\mathrm{d}}/\kappa$
   812	depends on~$N$: for $\mathrm{SU}(2)$ it is $22/9$; for
 succeeded in 51ms:
   528	
   529	At genus~$1$, the Arnold relation acquires a defect from the
   530	period matrix of the elliptic curve. The bar differential
   531	acquires curvature:
   532	\[
   533	d^2 \;=\; k \cdot \omega_1.
   534	\]
   535	The \emph{modular characteristic} $\kappa(\cA)$ (Volume~I, Theorem~D) is the unique scalar such that the bar differential satisfies $d_{\barB}^2 = \kappa(\cA) \cdot \omega_g$ at genus $g \geq 1$, where $\omega_g = c_1(\lambda) \in H^2(\overline{\cM}_g, \Z)$ is the first Chern class of the Hodge bundle. For $\cA = \cH_k$: $\kappa(\cH_k) = k$. For $\cA = \hat{\fg}_k$ with simple~$\fg$: $\kappa(\hat{\fg}_k) = \dim\fg \cdot (k + h^\vee)/(2h^\vee)$.
   536	
   537	The modular characteristic is $\kappa(\cH_k) = k$: the same
 succeeded in 51ms:
chapters/connections/spectral-braiding-core.tex:3182:(Vol~I, Theorem~D); see \S\ref{subsubsec:virasoro-complementarity-offset} below.
chapters/connections/spectral-braiding-core.tex:3882:(Vol~I, Theorem~D).
 exited 2 in 51ms:
rg: regex parse error:
    (?:Theorem~C; for .*\kappa|Theorem~D; for .*\kappa|Theorem~D\).*\kappa \+ \kappa|Theorem~C\).*modular characteristic|Theorem~D\).*complementarity|Theorem~C\).*leading coefficient)
                        ^^
error: unrecognized escape sequence
 succeeded in 51ms:
chapters/connections/spectral-braiding-core.tex:3168:For Kac--Moody and free-field algebras, Koszul complementarity (Vol~I, Theorem~C) gives
chapters/connections/spectral-braiding-core.tex:3207:Kac--Moody algebras, where complementarity (Vol~I, Theorem~C)
chapters/connections/spectral-braiding-core.tex:3810: Vol~I, Theorem~C at all genera). The bar complex
chapters/connections/spectral-braiding-core.tex:3836: (Vol~I, Theorem~C). For the affine and free-field
chapters/connections/spectral-braiding-core.tex:3874:$\kappa(\cA) + \kappa(\cA^!) = 0$; Vol~I, Theorem~C
chapters/connections/spectral-braiding.tex:801:Koszul complementarity (Vol~I, Theorem~C) gives
chapters/connections/spectral-braiding.tex:1258: Vol~I, Theorem~C at all genera). The bar complex
chapters/connections/spectral-braiding.tex:1281: (Vol~I, Theorem~C; for Virasoro, $\kappa + \kappa^! = 13$).
chapters/connections/spectral-braiding.tex:1319:(Vol~I, Theorem~C; for $\mathcal{W}$-algebras, $\kappa + \kappa^! = K(\fg)$).




thinking
**Evaluating status mismatch**

I’m thinking about the potential status mismatch in the user’s prompt. It might seem too nitpicky, but they did ask to "tear apart every weakness" and provide exact fixes. I wonder if the strongest findings will be sufficient. It’s essential for me to verify any statements against the actual source in Volume I to ensure accuracy. I want to make sure I’m giving the user reliable information!
thinking
**Deciding on N's meaning**

I need to figure out what N stands for. One option could be the number of seam files I've checked. I've directly read several files like the Vol I guide to main results, chiral hochschild koszul, and concordance. There’s a lot of information to sift through, so I want to make sure I get this right. Each reference seems important, so it's worth ensuring clarity when I choose what N represents.
thinking
**Evaluating findings and formatting**

I'm considering whether to have one high finding for two files or separate findings for each file. I could report two high findings or keep it concise, noting a high for the 3d_gravity line and another lower one for the movement file. The user wants details about seam inconsistencies, so it seems best to include both since they both involve active files. The exact fix is straightforward, with a candidate for a high finding related to a misstatement. I should also mention that the "leading coefficient" should be a modular characteristic.
thinking
**Reviewing technical details**

I'm diving into "braiding.tex" and I'm considering if there's an issue with the bare kappa in the introduction line. I think it could be good to replace it with κ(ℵ) to resolve a couple of problems simultaneously. There are also references in "spectral-braiding" that need checking to ensure they're correct. I want to verify that if I find 10 issues while checking 15 files, that would be an acceptable summary. I'll focus on those relevant sections for now.
exec
/bin/zsh -lc "nl -ba chapters/connections/3d_gravity.tex | sed -n '9154,9162p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  9154	(Proposition~\ref{V1-prop:mcg-equivariance-tower}), forces
  9155	$Z(\tau)$ to be modular invariant.
  9156	
  9157	The modular bootstrap is therefore not an independent constraint
  9158	but a \emph{consequence} of the bar-complex structure:
  9159	$d_{\barB}^2 = \kappa\cdot\omega_1$ at genus~$1$ encodes both
  9160	the curvature (which determines $Z(\tau) = \eta(\tau)^{-\kappa}$)
  9161	and the modular anomaly (which constrains $Z$ to transform
  9162	with weight $-\kappa/2$ under $S$). At $\kappa_{\mathrm{eff}}

thinking
**Searching for sources**

I realize the chiral Hochschild source isn't relevant right now. I'm thinking I need a direct source from Volume I, perhaps the `guide_to_main_results` or Theorem D. Maybe I could search for `dfib`. I want to get the exact reference from Volume I, possibly looking into `higher_genus_modular_koszul` or `concordance`. It sounds like searching could help me pin down what I need!
exec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '122,126p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/guide_to_main_results.tex | sed -n '54,61p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '236,244p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F \"d_{\\barB}"'^2 = 0" chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/bar_construction.tex chapters/frame/guide_to_main_results.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "d_fib" chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex chapters/theory/higher_genus_foundations.tex chapters/frame/guide_to_main_results.tex' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n -F "dfib''^{'"\\,2} = \\kappa(\\cA) \\cdot \\omega_1\" chapters/connections/concordance.tex chapters/theory/higher_genus_modular_koszul.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
chapters/theory/higher_genus_modular_koszul.tex:2619: fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
 succeeded in 52ms:
   236	formal-disk restriction, but the embedding is not an
   237	equivalence: vertex algebras live on the formal disk~$D$,
   238	not on a bare point; the deformation retract
   239	$\mathbb{A}^1 \to \mathrm{pt}$ is additional data
   240	(specifying it and the attendant homotopy transfer is part
   241	of the comparison); and
   242	on~$\mathbb{P}^1$ the global topology of FM
   243	compactifications introduces Arnold relations absent over
   244	a point.
 succeeded in 52ms:
   122	\textbf{$\Eone$ A--H} &
   123	 All five main theorems proved in the ordered ($\Eone$)
   124	 setting at all genera: ribbon modular operad, planar
   125	 planted forests, formal ordered degree-$2$ shadow package. &
   126	 Thms~\ref{thm:e1-theorem-A-modular}--\ref{thm:e1-theorem-H-modular} \\[4pt]
 succeeded in 52ms:
    54	 Thm~\ref{thm:modular-characteristic} \\[4pt]
    55	
    56	\textbf{Theorem H} &
    57	 Chiral Hochschild: $\ChirHoch^*(\cA)$ has polynomial
    58	 growth, is Koszul-functorial, and admits an explicit
    59	 Koszul resolution of length bounded by the number
    60	 of generators. &
    61	 Thm~\ref{thm:hochschild-polynomial-growth} \\[4pt]
 exited 1 in 52ms:

 succeeded in 52ms:
chapters/theory/higher_genus_modular_koszul.tex:29156:from $d_{\barB}^2 = 0$. The cyclic admissibility conditions
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_modular_koszul.tex | sed -n '2614,2622p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
  2614	(Definition~\ref{def:modular-koszul-chiral}). The
  2615	\emph{scalar modular characteristic package} of~$\cA$ consists of:
  2616	\begin{enumerate}[label=\textup{(\roman*)}]
  2617	\item The \emph{obstruction invariant}
  2618	 $\kappa(\cA) \in \mathbb{C}$, the scalar controlling genus-$1$
  2619	 fiberwise curvature $\dfib^{\,2} = \kappa(\cA) \cdot \omega_1 \cdot \operatorname{id}$
  2620	 (Theorem~\ref{thm:genus-universality}).
  2621	\item The \emph{genus tower} $\{F_g(\cA)\}_{g \geq 1}$, the sequence
  2622	 of free energies determined by the bar complex at genus~$g$


thinking
**Evaluating potential issues**

I’m noticing a potential issue in the ordered_associative_chiral_kd_core at line 1274. It mentions each has an E1-chiral counterpart, which is obtained by replacing symmetric coinvariants with an ordered bar complex. However, it seems like the E∞ label might be incorrect given that ordered versions exist for all genera. Moving to line 2206, I see a similar concern regarding the bar differential's definition. The user is looking for exact lines, so I should focus on those.
thinking
**Considering citations**

I’m thinking about potentially citing line 2192 and mentioning that the same defect appears again in lines 2210-2225 and 2382. It seems like that could be an acceptable approach, as it would help clarify the recurring issue without overwhelming the user with too much information. I want to ensure that I’m addressing the problem effectively while providing clear references to the relevant lines. This way, the user can easily follow along.
exec
/bin/zsh -lc 'rg -n -F "spectral-braiding" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
760:\phantomsection\label{thm:spectral-braiding-core}%
1324:\input{chapters/connections/spectral-braiding-core}
1447:\input{chapters/connections/spectral-braiding-frontier}

thinking
**Checking active files**

I need to focus on the core active file, avoiding anything to do with spectral-braiding. It's essential to steer clear of findings that are marked inactive. Also, I should check the status of `ordered_associative_chiral_kd.tex` to see if it's currently active. This means I need to perform a thorough search for active inputs to ensure I'm working with the right data. Keeping everything relevant is key!
exec
/bin/zsh -lc 'rg -n -F "ordered_associative_chiral_kd" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1299:\input{chapters/connections/ordered_associative_chiral_kd_core}
1453:\input{chapters/connections/ordered_associative_chiral_kd_frontier}

thinking
**Searching for files**

I think I should perform an active check for the file `holomorphic_topological.tex`. It seems like the next step would be to search for it to ensure I can access the right information. I'm wondering if there are specific criteria or locations I should focus on during the search. Let's see what I can uncover to make sure everything's in order. I'll get started on that search now!
exec
/bin/zsh -lc 'rg -n -F "holomorphic_topological" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
1407:\input{chapters/connections/holomorphic_topological}
exec
/bin/zsh -lc 'rg -n -F "twisted_holography_quantum_gravity" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 exited 1 in 51ms:



thinking
**Considering relevant files**

I’m thinking about whether to look for relevant files, even if they're not active. The user didn’t limit the search to just active files, so it could include what I find in the cross-volume seam too. There are some active issues, but if a file isn't active, maybe the severity is lower, even if it’s still relevant. I’ll prioritize active files for stronger findings, but the user’s request means we might consider non-active ones too.
thinking
**Deciding on file inclusion**

I’m contemplating whether to exclude a file since it’s not active, but the user requested the entire Vol II bridge. I think I should include it, considering it’s still a manuscript file, even if its severity might be medium. If I summarize, I’ll note “Checked: 18.” Now, I also need to check if `log_ht_monodromy_core` is active, so I’ll search in the main files to confirm that status.
exec
/bin/zsh -lc 'rg -n -F "log_ht_monodromy_core" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1403:\input{chapters/connections/log_ht_monodromy_core}
exec
/bin/zsh -lc 'rg -n -F "conclusion" main.tex' in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
1464:\input{chapters/connections/conclusion}

thinking
**Checking document details**

I need to make sure that I have `foundations.tex` and `introduction.tex` active. That seems good! I also wonder about `spectral-braiding-core` and `log_ht_monodromy_core`, should they be active too? 

There's a potential issue on line 3182 in `spectral-braiding-core` related to "Theorem D" and possibly incorrect theorem attribution. I might need to inspect this further and search for the relevant context to clarify the matter.
exec
/bin/zsh -lc "nl -ba chapters/connections/spectral-braiding-core.tex | sed -n '3176,3184p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
  3176	$\kappa = \dim(\fg)(k{+}h^\vee)/(2h^\vee)$, so
  3177	$\kappa(\cA^!) = -\kappa(\cA)$. The complementarity
  3178	potential $F_1(\cA) + F_1(\cA^!) = 0$ vanishes: the bulk
  3179	theory carries no net genus-$1$ anomaly.
  3180	For $\mathcal{W}$-algebras, the complementarity sum
  3181	$\kappa + \kappa^!$ is in general nonzero
  3182	(Vol~I, Theorem~D); see \S\ref{subsubsec:virasoro-complementarity-offset} below.
  3183	
  3184	The all-genus generating function:


thinking
**Reassessing instructions**

I’m wondering if it specifies "SC datum not bar complex," but I’m not sure. The AGENTS instructions might not allow mentioning file contents. So, I think I should avoid mentioning SC coalgebras and focus on dbarB^2 instead. It seems essential to stay within guidelines and make sure I’m being careful about what information I include. Let’s clarify that!
thinking
**Organizing findings and notes**

I think I need to include the log_ht_monodromy_core line 1903 as critical and also mention that line 1914 recovers the correct collision residue, which helps avoid self-contradiction. That's a strong point to make. I should also look into including the 3d_gravity asymptotic duplicate in a separate movement file. Alright, I’ll craft the final document carefully with my 12 findings, but I need to ensure my summary has a total of 15 checked items.
codex
- [CRITICAL] `chapters/connections/log_ht_monodromy_core.tex:1903` — PROBLEM: the affine lambda-bracket is Laplace-transformed to `\Omega/z + k\kappa_\fg/z^2`. That is wrong twice: the Laplace kernel of `\{J^a{}_\lambda J^b\}=f^{ab}{}_cJ^c+k\kappa^{ab}\lambda` is `f^{ab}{}_cJ^c/z + k\kappa^{ab}/z^2`, and the Casimir residue `k\,\Omega/z` appears only after the `d\log` absorption / evaluation-module reduction. The file even self-corrects at line 1914. FIX: replace the display by `r^{\mathrm{Lap}}(z)=f^{ab}{}_cJ^c/z+k\,\kappa_\fg^{ab}/z^2`, rename it `r^{\mathrm{Lap}}`, and then state separately: `after bar-kernel absorption and passage to the collision residue, the braiding is governed by r^{\mathrm{KM}}(z)=k\,\Omega/z`.

- [CRITICAL] `chapters/connections/3d_gravity.tex:8322` — PROBLEM: this table still identifies the Virasoro shadow coefficient with the lambda-bracket coefficient by writing `S_2=c/12`; the row at line 8334 repeats the same error. Earlier in the same active chapter `S_2=\kappa=c/2` is already used. FIX: replace the sentence by `the entries for r=2,3 are the low-degree shadow data S_2=\kappa=c/2 and S_3=-c; c/12 is only the divided-power coefficient of \lambda^3 in \{T_\lambda T\}` and change the `r=2` row from `c/12` to `c/2` in both columns.

- [HIGH] `chapters/connections/ordered_associative_chiral_kd_core.tex:1274` — PROBLEM: Vol I’s five main theorems are described as an `E_\infty` package. That is stale hierarchy language and contradicts Vol I’s live ordered `E_1` A–H package. FIX: replace the opening sentence with: `Volume~I establishes five main theorems for augmented chiral algebras on curves and also proves their ordered ($E_1$) variants at all genera; the genus-zero ordered statements collected here are the local ordered face of that package.` Also replace `leading coefficient` with `modular characteristic`.

- [HIGH] `chapters/theory/introduction.tex:143` — PROBLEM: Theorem D is imported as `d_{\barB}^2=\kappa\cdot\omega_g`; the same false formula recurs at line 535. Vol I’s live source separates the square-zero bar differential from the fiberwise genus correction. FIX: in both places replace `d_{\barB}^2 = ...` by `d_{\mathrm{fib}}^{\,2} = \kappa(\cA)\cdot\omega_g`, and add one clause that the underlying bar differential remains square-zero.

- [HIGH] `chapters/theory/foundations.tex:2192` — PROBLEM: the foundations chapter states that the bar differential squares to `\kappa(\cA)\cdot\omega_g`; the same error is built into the local definition at lines 2208–2225 and the gauge-theory dictionary row at line 2382. FIX: replace the affected formulas by `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g` and rewrite the definition to say the genus-dependent fiberwise differential is curved, while `d_{\barB}^2=0` for the bar differential itself.

- [HIGH] `chapters/connections/spectral-braiding-core.tex:3847` — PROBLEM: the active spectral-braiding chapter repeats the same Vol I drift: `d_{\barB}^2=\kappa(\cA)\cdot\omega_g`; it recurs again at lines 3895–3896 and 3925–3926. FIX: change each occurrence to `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g`, and in the remark at 3925–3926 rewrite `the closed-color component gives ...` as `the closed-color fiberwise component gives ...`.

- [HIGH] `chapters/connections/conclusion.tex:447` — PROBLEM: the conclusion still summarizes the genus correction as `d_{\barB}^2=\kappa(\cA)\cdot\omega_g`; the same seam error reappears at line 1643. FIX: replace both by `d_{\mathrm{fib}}^{\,2}=\kappa(\cA)\cdot\omega_g` and keep the bar differential square-zero.

- [HIGH] `chapters/connections/3d_gravity.tex:9159` — PROBLEM: the gravity climax still states `d_{\barB}^2=\kappa\cdot\omega_1`, with bare `\kappa` on top of the wrong differential. FIX: replace it by `d_{\mathrm{fib}}^{\,2}=\kappa(\mathrm{Vir}_c)\cdot\omega_1`, and carry the same argument into the modular-weight sentence that follows.

- [HIGH] `chapters/connections/3d_gravity.tex:8853` — PROBLEM: the large-`c` asymptotic is still `2/(5c^2)`, off by a factor of `5`. The same chapter already gives the correct `2/c^2` elsewhere. FIX: change `2/(5c^2)` to `2/c^2`.

- [HIGH] `chapters/connections/thqg_3d_gravity_movements_vi_x.tex:1490` — PROBLEM: the split movement file keeps the same wrong asymptotic `S_4\sim 2/(5c^2)`. FIX: change it to `S_4\sim 2/c^2`.

- [MEDIUM] `chapters/connections/spectral-braiding-core.tex:3182` — PROBLEM: the nonzero `\kappa+\kappa^!` statement for `\mathcal W`-algebras is attributed to Vol I Theorem D; that is a complementarity statement, so the citation should be to Theorem C. The same wrong attribution recurs at line 3882. FIX: change both citations from `Vol~I, Theorem~D` to `Vol~I, Theorem~C`, and spell the example with arguments, e.g. `\kappa(\mathrm{Vir}_c)+\kappa(\mathrm{Vir}_{26-c})=13`.

- [MEDIUM] `chapters/connections/holomorphic_topological.tex:808` — PROBLEM: the file defines `\kappa(\widehat{\mathfrak g}_k)` and then immediately drops the argument, writing bare `F_g=\kappa\cdot\lambda_g^{\mathrm{FP}}` and bare `\kappa=\dim(\mathfrak g)/2`; the same bare-`\kappa` drift recurs at line 1250. FIX: write `F_g=\kappa(\widehat{\mathfrak g}_k)\cdot\lambda_g^{\mathrm{FP}}`, and at `k=0` write `\kappa(\widehat{\mathfrak g}_0)=\dim(\mathfrak g)/2`; at line 1250 write `F_g=\kappa(\cA_{\mathrm{Burns}})\cdot\lambda_g^{\mathrm{FP}}`.

- [MEDIUM] `chapters/connections/twisted_holography_quantum_gravity.tex:2745` — PROBLEM: Theorem H is summarized as “the chiral Hochschild cohomology is polynomial in the cumulants.” Vol I’s live theorem says polynomial growth / degree-`2` Hilbert polynomial, not cumulant polynomiality. FIX: replace that item with `Theorem H (chiral Hochschild): on the Koszul locus the Hochschild--Hilbert series is polynomial of degree at most 2, equivalently \ChirHoch^n(\cA)=0 for n\notin\{0,1,2\}; for affine KM one excludes the critical level k=-h^\vee.`

## Summary
Checked: 15 | Findings: 13 | Verdict: FAIL
tokens used
424,850
