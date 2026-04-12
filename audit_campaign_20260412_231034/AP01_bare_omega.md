# AP01_bare_omega (524s, gpt-5.4)

- [CRITICAL] Vol II `standalone/preface_full_survey.tex:507` — exact text `\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2}`. This strips the level from the simple-pole term, then the same block immediately says the collision residue is `r(z)=k\,\Omega/z` at line 513.
- [CRITICAL] Vol II `chapters/connections/log_ht_monodromy_core.tex:1905` — exact text `= \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2}`. The same paragraph then says the braiding is governed by `r(z)=k\,\Omega/z` at line 1914.
- [CRITICAL] Vol I `chapters/connections/thqg_gravitational_yangian.tex:728` — exact text `\frac{\Omega_\fg}{z}`. The displayed equality immediately rewrites the same term as `\sum (e_a\otimes e^a)/(k+h^\vee)z` at line 732, so the first term is level-stripped.
- [CRITICAL] Vol II `chapters/connections/thqg_gravitational_yangian.tex:731` — same defect as Vol I: exact text `\frac{\Omega_\fg}{z}` while the next line carries the hidden `1/(k+h^\vee)` normalization.
- [CRITICAL] Vol I `chapters/examples/yangians_foundations.tex:1059` — exact text `r(z) = \Omega_{\mathrm{tr}}/z.` after defining `\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)` at line 1058. This conflicts with the canonical bridge `k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)`.

- [HIGH] Vol I `chapters/frame/preface_section1_v2.tex:481` — exact text `r(z) \;=\; \frac{\Omega}{z}` in a Kac-Moody overview; the same block averages `k\Omega/z`, so the surface is internally inconsistent.
- [HIGH] Vol I `chapters/frame/preface_section1_draft.tex:634` — same bare formula `r(z) \;=\; \frac{\Omega}{z}` on the same affine surface.
- [HIGH] Vol I `chapters/frame/preface_sections5_9_draft.tex:542,581,582` — table cells use bare `\Omega/z` for `\widehat{\fg}_k`, plus `\mathrm{av}(\Omega/z)` and `\Omega/z` for `Y(\fg)`.
- [HIGH] Vol I `chapters/connections/thqg_preface_supplement.tex:224` — tuple slot records `\frac{\Omega_N}{z}` while line 230 in the same block states the collision `r`-matrix is `r(z)=k\,\Omega_N/z`.
- [HIGH] Vol I `chapters/connections/holographic_datum_master.tex:466` — exact text `\frac{\Omega}{z}` in `r^{\mathrm{Dr}}(z)`. The same chapter elsewhere uses level-explicit normalizations, so this is an unqualified bare surface.
- [HIGH] Vol I `chapters/connections/holographic_datum_master.tex:717` — the master diagram repeats the same bare entry as `\frac{\Omega}{z}\;\textrm{(Drinfeld85)}`.

- [MEDIUM] Vol I `chapters/connections/frontier_modular_holography_platonic.tex:4731,4764` — prose specializes `r(z)=k\Omega/z` to `\Omega/z` at `k=1`. Numerically true at fixed level, but it violates the repo’s no-level-stripping convention on display.
- [MEDIUM] Vol II `chapters/examples/rosetta_stone.tex:2795` — same specialization drift: `at level~k=1 the collision residue is \Omega_{\mathfrak{sl}_3}/z`.

- [LOW] Vol I `chapters/theory/introduction.tex.bak:346` — stale backup still contains `r(z) = \Omega/z`.
- [LOW] Vol I `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:2912` — stale backup still contains `r(z) = \Omega/z`.

False positives removed: explicit KZ forms `\Omega/((k+h^\vee)z)`, absorbed-normalization sites such as `standalone/genus1_seven_faces.tex:695,724`, and generic Yangian definitions where the residue tensor itself is the datum rather than an affine level-stripped KM formula. No genuine Vol III hit survived context review.

## Summary
Instances checked: 31 | Violations found: 17 | Verdict: FAIL


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
session id: 019d83a0-9832-7d23-ad3f-38e2b4b8c9e2
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


MISSION: Sweep for AP126: bare Omega/z without level prefix across all three volumes.

Run: grep -rn '\\\\Omega.*z\b' chapters/ standalone/ | grep -v 'k.*Omega' | grep -v 'level' | head -50

Expected: Every Omega/z MUST have k prefix

For EACH hit:
1. Read surrounding context to determine if it's a genuine violation
2. Distinguish false positives from real violations
3. Report file:line and the exact violating text
4. Assess severity (CRITICAL if mathematical, HIGH if structural, MEDIUM if prose)
mcp startup: no servers
codex
I’m treating this as a read-only adversarial audit of AP126 across Volumes I–III. I’ll load the relevant audit workflow, run the requested sweep, then inspect each candidate in context and keep only genuine bare `\Omega/z` violations.
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
I’ve loaded the audit workflow. Next I’m locking the AP126 surface in the repo’s own constitutive files so the sweep is judged against the live convention, not memory.
exec
/bin/zsh -lc "rg -n \"AP126|Omega/z|r-matrix|bare \\\\Omega/z\" CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"AP126|Omega/z|r-matrix|bare \\\\Omega/z\" chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"AP126|Omega/z|r-matrix|bare \\\\Omega/z\" archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"AP126|Omega/z|r-matrix|bare \\\\Omega/z\" metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar exited 2 in 50ms:
rg: regex parse error:
    (?:AP126|Omega/z|r-matrix|bare \Omega/z)
                                   ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:AP126|Omega/z|r-matrix|bare \Omega/z)
                                   ^^
error: unrecognized escape sequence
 exited 2 in 52ms:
rg: regex parse error:
    (?:AP126|Omega/z|r-matrix|bare \Omega/z)
                                   ^^
error: unrecognized escape sequence
 exited 2 in 50ms:
rg: regex parse error:
    (?:AP126|Omega/z|r-matrix|bare \Omega/z)
                                   ^^
error: unrecognized escape sequence
codex
The first grep failed on an escaped pattern, so I’m simplifying to direct AP126 searches and then reading the local context around the hits.
exec
/bin/zsh -lc 'rg -n "AP126" CLAUDE.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP126" archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP126" metadata/theorem_registry.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "AP126" chapters/connections/concordance.tex' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
29:### HZ-1. AP126/AP141 (r-matrix level prefix) -- 6 waves, 90+ instances
237:**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).
289:- B1. `r(z) = \Omega/z` (bare, no level). CORRECT: trace-form `r(z) = k\Omega/z` or KZ `r(z) = \Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z` (catches bare form without any level prefix or Sugawara denominator).
292:- B4. `\Omega\,d\log z` (no k prefix). CORRECT: `k\Omega\,d\log z`. AP117/AP126.
348:- B39. KM r-matrix not vanishing at k=0. AP126/AP141.
400:**FM1. Generic-formula reaching ("pretty version" attractor).** Opus falls back to the canonical textbook form when memory is uncertain. For affine KM, training-data weight makes `Omega/z` the default; the level-prefixed `k*Omega/z` is less prevalent. Evidence: AP126/AP141, 42+ instances. Counter: append to every r-matrix prompt: "After writing ANY r-matrix, substitute k=0 and verify r vanishes. Do not proceed until k=0 -> r=0."
581:**PE-1. r-matrix write** (AP126, AP141, AP19, AP20)
593:AP126 check (trace-form):  r(z)|_{k=0} = [_]    expected: 0
797:AP126: Level-stripped r-matrix. Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. The level k survives d-log absorption. Verify: at k=0 the r-matrix MUST vanish. 42+ instances found across all three volumes (12 in first commit, 30 more in full-volume CG sweep). THE MOST VIOLATED AP in the manuscript. After writing ANY r-matrix, verify k=0 -> r=0.
814:AP141: AP126 is systemic. The original AP126 noted "12 instances across 5 files." This rectification session found 30 MORE instances across all three volumes. The error survives because Ω/z and kΩ/z look similar and both give valid-looking formulas. ENFORCEMENT: after writing ANY r-matrix formula, (a) check that k=0 gives r=0, (b) grep the manuscript for bare Ω/z without level prefix.
823:AP144: Convention coexistence without bridge. Different chapters independently develop conventions for the same object (r-matrix: trace-form k*Omega/z vs KZ Omega/((k+h^v)*z); kappa: several families). The conventions agree at generic parameter values but diverge at boundary values (k=0, k=-h^v). When multiple conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site, and boundary behavior must be checked in EACH convention separately. The r-matrix normalization issue (C9/C13/AP126 inconsistency, resolved April 2026) is the canonical example. After introducing ANY convention for a shared object, grep all three volumes for alternative conventions of the same object and install bridge identities.
827:AP148: r-matrix normalization is convention-dependent (see corrected C9). Two conventions for affine KM: trace-form r(z)=k*Omega/z (AP126 k=0 check applies; av(r)=kappa_dp only; Sugawara shift dim(g)/2 needed for full kappa) and KZ r(z)=Omega/((k+h^v)*z) (k=0 gives nonzero for non-abelian; av not simply related to kappa). Bridge: k*Omega_tr = Omega/(k+h^v) at generic k. BEFORE writing any r-matrix formula for affine KM, state which convention and verify boundary behavior in that convention.
 exited 1 in 50ms:

 succeeded in 51ms:
99:| `prop:frame-drinfeld-classical-limit` | `proposition` | 2084 | Classical limit and AP126 check |
 exited 1 in 51ms:

exec
/bin/zsh -lc "sed -n '228,246p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '789,806p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '90,108p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).

**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).

**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).

**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).

**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).

**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).

**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.

**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).

 succeeded in 51ms:
AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
AP122: Test tolerance proportional to magnitude. For Q~10^17, absolute tol 1e-4 is meaningless. Use relative: abs(computed-expected)/abs(expected) < rtol. Always verify tolerance achievable at float precision.
AP123: Combinatorial enumeration completeness. Verify count against known formula or generating function BEFORE hardcoding. Genus-2 stable graphs: 7 (not 6). Hand enumeration without cross-check = future AP10 violation.

### Deep Empirical (AP124-AP128, from 300-commit deep archaeology)
AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
AP126: Level-stripped r-matrix. Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. The level k survives d-log absorption. Verify: at k=0 the r-matrix MUST vanish. 42+ instances found across all three volumes (12 in first commit, 30 more in full-volume CG sweep). THE MOST VIOLATED AP in the manuscript. After writing ANY r-matrix, verify k=0 -> r=0.
AP127: Cross-refs to migrated chapters. When migrating \input{chapter} between volumes, immediately add \phantomsection\label{} stubs for EVERY label in the migrated file, and grep for all \ref{} pointing to those labels. Never leave a bare \ref to a label that no longer exists in the build.
AP128: Engine-test synchronized to same wrong value. When correcting a compute engine formula, NEVER update test expectations from engine output. Derive correct expected value INDEPENDENTLY (different formula, limiting case, literature). Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### Full-Volume Rectification (AP129-AP141, from 48-agent cross-volume CG sweep)
AP129: Reciprocal formula. When a formula involves a ratio a/b, the most common transcription error is b/a or -b/a. Both "look right" because they contain the same symbols. S_4(Vir) = 10/[c(5c+22)] was written as -(5c+22)/(10c) (the negative reciprocal). VERIFY: substitute a known value (e.g. c=1) and check the NUMBER before trusting the symbolic form.
AP130: Fiber-base level confusion. Objects on the fiber (dτ ∈ H^{1,0}(E_τ)) are NOT objects on the base (c_1(λ) ∈ H^2(M̄_g)). The Hodge CLASS ω_g = c_1(E) lives on moduli space; the holomorphic FORM dτ lives on the elliptic curve. Before writing ω_g = [expression], verify: does [expression] live on M̄_g or on Σ_g?
AP131: Generating depth != algebraic depth. d_gen (the degree at which all higher operations are determined by lower ones) ≠ d_alg (whether the tower terminates). Virasoro: m_3 generates all m_k (finite generating depth), but ALL m_k are nonzero (d_alg = ∞, class M). Writing d_alg(Vir) = 1 because "m_3 generates everything" conflates the two. Always specify WHICH depth.
AP132: Augmentation ideal in bar complex. B(A) = T^c(s^{-1} Ā), where Ā = ker(ε) is the AUGMENTATION IDEAL, NOT T^c(s^{-1} A). Using A instead of Ā includes the unit and breaks the construction. Found twice in the same chapter: the error survives visual inspection because A and Ā look similar. Mnemonic: bar complex uses bar A.
AP133: Catalan index shift. C_n counts binary trees with n+1 leaves (equivalently n internal nodes). The most common error: writing C_k when you mean C_{k-1} (or vice versa). C_3=5 (4 leaves) ≠ C_4=14 (5 leaves). VERIFY: count the leaves, subtract 1, THEN look up the Catalan number.
 succeeded in 50ms:
|---|---|---:|---|
| `prop:frame-arnold` | `proposition` | 506 | Arnold relation |
| `thm:frame-heisenberg-bar` | `theorem` | 855 | Heisenberg bar complex at genus~\texorpdfstring{$0$}{0} |
| `prop:frame-twisting-MC` | `proposition` | 954 | Maurer--Cartan equation for Heisenberg |
| `thm:frame-heisenberg-koszul-dual` | `theorem` | 1156 | Heisenberg Koszul dual |
| `thm:genus1-heisenberg` | `theorem` | 1379 | Genus-1 Heisenberg partition function |
| `thm:frame-genus1-curvature` | `theorem` | 1401 | Genus-1 curvature |
| `thm:frame-genus2-curvature` | `theorem` | 1549 | Genus-2 curvature |
| `thm:frame-complementarity` | `theorem` | 1740 | Quantum complementarity for Heisenberg |
| `prop:frame-drinfeld-classical-limit` | `proposition` | 2084 | Classical limit and AP126 check |
| `prop:frame-thesis-shadow-termination` | `proposition` | 2144 | Shadow tower termination for Heisenberg |
| `thm:rosetta-sl2-swiss` | `theorem` | 2717 | $\mathfrak{sl}_2$ bar complex as Swiss-cheese coalgebra |
| `prop:rosetta-sl2-m2` | `proposition` | 2789 | The $m_2$ operation |
| `thm:rosetta-feigin-frenkel` | `theorem` | 2838 | Feigin--Frenkel involution as Verdier duality |
| `prop:rosetta-sl2-pva` | `proposition` | 2921 | Affine PVA from bar cohomology |
| `prop:rosetta-jacobi` | `proposition` | 2959 | PVA Jacobi identity for $\widehat{\mathfrak{sl}}_{2,k}$ |
| `thm:rosetta-cs-r-matrix` | `theorem` | 3886 | Odd current $R$-matrix from the bar complex |
| `comp:heisenberg-center` | `computation` | 4785 | The Heisenberg center |


thinking
**Evaluating command options**

I'm thinking about piping and whether it's okay to use, especially since the mentions mainly focus on separators like echo. It seems like parallel might work too. I should take a look at the file structures, maybe using `ls` to check repo roots. Running `rg --files` might be excessive, but perhaps the command itself will indicate if something is missing. It sounds like I can run it to find out!
codex
I’ve locked the convention: AP126 only condemns the trace-form bare `\Omega/z`, not the KZ form `\Omega/((k+h^\vee)z)`. I’m now running the exact sweep across Volumes I, II, and III, then I’ll inspect each candidate in context and discard false positives.
exec
/bin/zsh -lc "grep -rn '\\\\\\\\Omega.*z\\b' chapters/ standalone/ 2>/dev/null | grep -v 'k.*Omega' | grep -v 'level' | head -50" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "grep -rn '\\\\\\\\Omega.*z\\b' chapters/ standalone/ 2>/dev/null | grep -v 'k.*Omega' | grep -v 'level' | head -50" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

exec
/bin/zsh -lc "grep -rn '\\\\\\\\Omega.*z\\b' chapters/ standalone/ 2>/dev/null | grep -v 'k.*Omega' | grep -v 'level' | head -50" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

 succeeded in 172ms:



thinking
**Analyzing regex usage**

I’m thinking about how the pattern `\\\\Omega.*z\\b` didn't match, possibly due to differences between grep and ripgrep. When using grep, I wonder if the backslashes are causing confusion. The file has `\Omega`, so my pattern might need adjustment. Considering basic regex, each `\\` represents a literal backslash, meaning `\\\\Omega` could match `\\Omega`. I should probably run a robust search to ensure I catch all potential matches effectively. Let's explore this further!
thinking
**Investigating occurrences of Omega**

I want to check all occurrences of `\Omega`, as there could be many in the repo. Using ripgrep (rg) with the pattern `\\Omega` might reveal them. I should narrow the search to those instances close to `/z` or `(k+h`. Since my network is restricted, I can run a command like `rg -n --no-heading '\\Omega[^$]*z'` to get results without extra headings. Let’s see what I can find!
codex
The literal grep returned zero hits in all three repos, but that pattern is brittle for TeX and can miss variants. I’m doing a broader second pass on `\Omega` contexts to rule out false negatives before concluding PASS.
exec
/bin/zsh -lc "rg -n '\\\\Omega' chapters standalone 2>/dev/null | head -200" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n '\\\\Omega' chapters standalone 2>/dev/null | head -200" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\Omega' chapters standalone 2>/dev/null | head -200" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/w-algebras-stable.tex:1739:$\Omega_{B_2}$ has root-length-dependent coefficients (short
chapters/examples/w-algebras-stable.tex:1741:collision residue $r^{B_2}(z) = k \cdot \Omega_{B_2}/z$ that
standalone/preface_full_survey.tex:73:The E$_1$ bar complex $\barB(\cA)$ on $\FM_k(\C) \times \Conf_k^{<}(\R)$ is one coalgebra; three functors extract three objects: cobar $\Omega(\barBch(\cA)) \simeq \cA$ recovers the original algebra (bar-cobar inversion), Verdier duality $\mathbb{D}_{\mathrm{Ran}}(\barBch(\cA)) \simeq \barBch(\cA^!)$ produces the line-side Koszul dual, and chiral Hochschild cochains $C^\bullet_{\mathrm{ch}}(\cA,\cA)$ compute the bulk observables. The $\SCchtop$~structure is not carried by $\barB(\cA)$ itself but by the chiral derived center: the pair $(C^\bullet_{\mathrm{ch}}(\cA,\cA),\,\cA)$ is the bulk-acting-on-boundary datum. Every chapter of this volume is a different projection of the bar coalgebra.
standalone/preface_full_survey.tex:173:\Omega^\bullet\bigl(\FM_n(\C) \times \Conf_n^<(\R)\bigr).
standalone/preface_full_survey.tex:261:\Omega\mathbf{B}(\SCchtop) \;\xrightarrow{\;\sim\;}\; \SCchtop.
standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
standalone/preface_full_survey.tex:507:\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2},
standalone/preface_full_survey.tex:509:where $\Omega = \sum_a J^a \otimes J_a$ is the split Casimir
standalone/preface_full_survey.tex:513:r-matrix is $r(z) = k\,\Omega/z$.
standalone/preface_full_survey.tex:514:The KZ connection $\nabla_{\mathrm{KZ}} = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$ is
standalone/preface_full_survey.tex:520:k\,\Omega/z$ is the Lie-algebra Jacobi identity for $\fg$: the
standalone/preface_full_survey.tex:871: $\Omegach(\barBch(\cA)) \xrightarrow{\sim} \cA$ is a
standalone/preface_full_survey.tex:1140:$r(z) = k\,\Omega/z$ as classical limit.
standalone/preface_full_survey.tex:1261:$r(z) = k\,\Omega/z$. The KZ connection is the degree-$(2,0)$
standalone/preface_full_survey.tex:1563: $\Omega\mathbf{B}(\SCchtop) \xrightarrow{\sim} \SCchtop$
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
standalone/bar_chain_models_chiral_quantum_groups.tex:210:The cobar construction $\Omega$ provides a left adjoint:
standalone/bar_chain_models_chiral_quantum_groups.tex:211:$\Omega B(\cA) \simeq \cA$ for augmented $\cA$.
standalone/bar_chain_models_chiral_quantum_groups.tex:224:r(z) = \frac{k\,\Omega}{z},
standalone/bar_chain_models_chiral_quantum_groups.tex:226:where $\Omega \in \fg \otimes \fg$ is the Casimir.  This $r(z)$
 succeeded in 52ms:
Total output lines: 200

chapters/examples/quantum_group_reps.tex:126:where $r(z) = \frac{k\,\Omega}{z} + O(1)$ is the classical $r$-matrix with
chapters/examples/quantum_group_reps.tex:127:Casimir $\Omega \in \frakg \otimes \frakg$ and level prefix $k$
chapters/examples/quantum_group_reps.tex:142: \item $r(z) = \frac{k\,\Omega}{z}$: the classical $r$-matrix at level $k$
chapters/examples/quantum_group_reps.tex:267:$r(z) = \frac{k\,\Omega}{z}$
chapters/examples/quantum_group_reps.tex:396: \Omega(\gamma; \sigma) \cdot \hat{e}_{n\gamma}
chapters/examples/quantum_group_reps.tex:399:where $\Omega(\gamma; \sigma) \in \Z$ is the (numerical)
chapters/examples/quantum_group_reps.tex:410:individual $\Omega(\gamma; \sigma)$ jump, but the ordered product
chapters/examples/quantum_group_reps.tex:416:The numerical DT invariants $\Omega(\gamma; \sigma) \in \Z$ are
chapters/examples/quantum_group_reps.tex:420:replaces $\Omega$ by the motivic class, and the quantum torus by
chapters/examples/quantum_group_reps.tex:441: \item The individual BPS invariants $\Omega(\gamma; \sigma)$ are
chapters/examples/quantum_group_reps.tex:553:$R(z) = 1 + r(z) + O(r^2)$ where $r(z) = \frac{k\,\Omega}{z}$:
chapters/examples/quantum_group_reps.tex:560: $r(z) = \frac{k\,\Omega}{z} \mapsto \kappa_{\mathrm{cat}}$: the full
chapters/examples/toric_cy3_coha.tex:227: \item \emph{Feynman diagrams}: the tree-level $n$-point amplitudes of the holomorphic CS theory on $\C^3$ are the structure constants of the affine Yangian $Y(\widehat{\fgl}_1)$, computed from Witten diagrams on $\C^3$ with the holomorphic $3$-form $\Omega = dx \wedge dy \wedge dz$ as the propagator kernel.
chapters/examples/toric_cy3_coha.tex:328: H_i \;=\; \sum_{j \neq i} \frac{\Omega_{ij}^{Y(\widehat{\fg}_{Q_X})}}{z_i - z_j},
chapters/examples/toric_cy3_coha.tex:331:where $\Omega_{ij}^{Y(\widehat{\fg}_{Q_X})} \in
chapters/examples/toric_cy3_coha.tex:333:Casimir $\Omega \in Y(\widehat{\fg}_{Q_X}) \otimes
chapters/examples/toric_cy3_coha.tex:348:$[\Omega_{ik}, \Omega_{jk}]/(z_i - z_k)(z_j - z_k)$ and cyclic
chapters/examples/toric_cy3_coha.tex:360:$\Omega = \sum_a J_a \otimes J^a$ with $J_a$ the
 succeeded in 52ms:
chapters/examples/deformation_quantization.tex:175:\[\Omega^*_{\text{ch}} = \Omega^*_{\text{log}}(\overline{C}_n(X)) \otimes \mathcal{A}^{\boxtimes n}\]
chapters/examples/deformation_quantization.tex:178:\item $\Omega^*_{\text{log}}$ are logarithmic forms with poles along collision divisors:
chapters/examples/deformation_quantization.tex:436:\[\mathcal{Q}(\mathcal{A}_{\text{cl}}) \cong \prod_{n=2}^\infty H^0(\overline{C}_n^{\text{ch}}(X), \Omega^{\dim C_n}_{\text{closed}})/\text{exact}\]
chapters/examples/deformation_quantization.tex:563:\[w_\Gamma^{(g)} = \sum_{k=0}^\infty c_k(\Gamma) \cdot E_{2k}^{(g)}(\Omega)\]
chapters/examples/deformation_quantization.tex:1029:\text{cobar differential component } d_\Omega
chapters/examples/deformation_quantization.tex:1481:\;:=\; \Omega(\JacF{F}{p})
chapters/examples/deformation_quantization.tex:1720:\;=\; \cO_M \;\otimes^{L}_{\mathrm{Sym}(\Omega_M)}\; \cO_M,
chapters/examples/deformation_quantization.tex:1722:where $\mathrm{Sym}(\Omega_M)$ acts on the first factor via the zero
chapters/examples/deformation_quantization.tex:1747:\textup{(}the total space of~$\Omega[-1]$\textup{)}.
chapters/examples/w_algebras_deep.tex:120:\mathcal{W}^{-h^\vee}(\mathfrak{g}, e) \cong H^*_{\mathrm{DS}}(\Omega^{\mathrm{ch}}_{G/P_e})
chapters/examples/w_algebras_deep.tex:124:\item $\Omega^{\mathrm{ch}}_{G/P_e}$ is the chiral de Rham complex of the partial flag variety
chapters/examples/w_algebras_deep.tex:131:\emph{Step 1: Factorization algebra model.} The chiral de Rham complex defines a factorization algebra $U \mapsto \Omega^{\mathrm{ch}}(U \times_{X} G/P_e)$ for open $U \subset X$.
chapters/examples/w_algebras_deep.tex:1055:$\Omega^{\mathrm{fact}}(\barB^{\mathrm{fact}}(\mathcal{W}_3))
chapters/examples/w_algebras_deep.tex:1156: \Omega^{\mathrm{fact}}(\barB^{\mathrm{fact}}(W_N)) \to W_N
chapters/examples/w_algebras_deep.tex:1185: \Omega^{\mathrm{fact}}\bigl(
chapters/examples/w_algebras_deep.tex:1308:\Omega^{\mathrm{fact}}(
chapters/examples/w_algebras_deep.tex:1751:each tensored with a basis element of $\Omega^2(\overline{C}_3)$.
chapters/examples/w_algebras_deep.tex:1860:\bar{B}^3_6 = \bC\{[T|T|T]\} \otimes \Omega^2(\overline{C}_3)
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a

thinking
**Testing regex functionality**

I’m considering how the shell single quotes pass two backslashes to the `rg` regex, interpreting `\\Omega` as a literal backslash plus Omega. In PCRE, that should be the case. I want to test this on a repository. I’m using "maybe" since previously I was working with `grep`, not `rg`. So, I think I’ll run the test on vol1 to pinpoint candidate lines that match the regex. Let’s see how it goes!
codex
I’ve confirmed the exact `grep` undercounts because of regex/TeX quirks. I’m switching to a broader `rg` candidate set and then narrowing manually, which is the safer adversarial path for false-negative-sensitive formula audits.
exec
/bin/zsh -lc "rg -n '\\\\Omega.*z\\b' chapters standalone 2>/dev/null | rg -v 'k.*Omega' | rg -v 'level' | head -200" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
standalone/computations.tex:542:$r^{\mathrm{aff}}(z) = \Omega/((k{+}2)z)$. The HPL transfer through the
standalone/computations.tex:559:The affine $r$-matrix $r^{\mathrm{aff}}(z) = \Omega/((k{+}2)z)$ has a
standalone/computations.tex:586:where $\Omega(w{+}z, w) = J^0(w{+}z) \otimes J^0(w)
standalone/computations.tex:747:gauge theory, the affine $r$-matrix $r^{\mathrm{aff}}(z) = \Omega/((k{+}h^\vee)z)$
standalone/computations.tex:776: & $\Omega/((k{+}h^\vee)z)$ (simple pole)
standalone/gaudin_from_collision.tex:197: \frac{\Omega}{(k + h^\vee) z}.
standalone/gaudin_from_collision.tex:238:$r(z) = \Omega/((k+h^\vee)z)$ into \eqref{eq:gz-connection} gives
standalone/gaudin_from_collision.tex:541: is $r(z) = \Omega/((k+h^\vee)z)$; the Gaudin Hamiltonian is its
chapters/examples/heisenberg_eisenstein.tex:519:$\Omega = \begin{pmatrix} \tau_1 & z \\ z & \tau_2 \end{pmatrix} \in \mathcal{H}_2$, 
chapters/examples/heisenberg_eisenstein.tex:1238:E(z,w|\Omega) = (z-w)\bigl(1 + c_2(\Omega)(z-w)^2
chapters/examples/heisenberg_eisenstein.tex:1239:+ c_4(\Omega)(z-w)^4 + \cdots\bigr)
standalone/ordered_chiral_homology.tex:669:$r(z) = \hbar\,\Omega/z$ is in KZ normalisation;
standalone/ordered_chiral_homology.tex:817:$r(z) = \hbar\,\Omega/z
standalone/ordered_chiral_homology.tex:866:$r(z) = \hbar\,\Omega/z$. The full quantum $R$-matrix
standalone/ordered_chiral_homology.tex:1259:  classical $r$-matrix $r(z) = \hbar\,\Omega/z$
standalone/ordered_chiral_homology.tex:3378:  Y(T^{(n)}\,\Omega,\, z)
standalone/ordered_chiral_homology.tex:3392:  Y(J^a\,\Omega,\, z)
standalone/ordered_chiral_homology.tex:3435:  S(z) = \id + \frac{\hbar\,\Omega}{z}
standalone/ordered_chiral_homology.tex:3445:$r(z) = \hbar\,\Omega/z$ is recovered.
standalone/ordered_chiral_homology.tex:3463:holds at $N = 2$: the $\hbar\,\Omega/(z-w)$ correction from

thinking
**Classifying candidate sets**

I’ve got a candidate set now, but I need to check across volumes 2 and 3 as well. It’s important to inspect each suspicious hit, since many seem to clearly match the KZ formula or hbar/h_KZ instead of AP126. I think I might need to search in volumes 2 and 3 in a similar way to classify these properly. It’s a step-by-step process, but I’m determined to get it right!
exec
/bin/zsh -lc "rg -n '\\\\Omega.*z\\b' chapters standalone 2>/dev/null | rg -v 'k.*Omega' | rg -v 'level' | head -200" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n '\\\\Omega.*z\\b' chapters standalone 2>/dev/null | rg -v 'k.*Omega' | rg -v 'level' | head -200" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:4215:$\Omega = \bigl(\begin{smallmatrix} \tau & z \\ z & \sigma
chapters/examples/toroidal_elliptic.tex:4276:$\Omega = \bigl(\begin{smallmatrix} \tau & z \\
chapters/examples/toroidal_elliptic.tex:5168:The vanishing $\chi(K3 \times E) = 0$ is the enumerative shadow of the CY$_3$ condition: the holomorphic $3$-form $\Omega_X = \omega_S \wedge dz$ on $K3 \times E$ provides a cosection of the obstruction sheaf, forcing the degree-zero virtual class to vanish after integration.
chapters/examples/toroidal_elliptic.tex:5328:where $\Omega = \bigl(\begin{smallmatrix} \tau & z \\ z & \sigma \end{smallmatrix}\bigr) \in \mathbb{H}_2$, $q = e^{2\pi i \tau}$, $y = e^{2\pi i z}$, $p = e^{2\pi i \sigma}$, the exponents $f(D)$ are the Fourier coefficients of $\phi_{0,1}$, and the ordering $(n,l,m) > 0$ means $m > 0$, or $m = 0$ and $n > 0$, or $m = n = 0$ and $l < 0$.
chapters/examples/toroidal_elliptic.tex:5352: \Delta_5(\Omega) = \sum_{m \geq 1} \phi_m(\tau, z) \, p^m,
chapters/connections/cy_holographic_datum_master.tex:506: \;=\; \frac{\Psi\,\Omega_{Y(\widehat{\fg}_{Q_X})}}{z}
chapters/connections/cy_holographic_datum_master.tex:717:the collision residue is normalized so that $\Omega = r_{CY}(z)\cdot z$
 succeeded in 51ms:
chapters/examples/rosetta_stone.tex:2345: The $R$-matrix is $R(z) = 1 + \hbar\,\Omega/z + \cdots$
chapters/examples/rosetta_stone.tex:2674:$r^{E_\tau}(z) = \Omega \cdot \zeta(z|\tau) + \kappa \cdot \wp(z|\tau)$,
chapters/examples/rosetta_stone.tex:2798:R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
chapters/examples/rosetta_stone.tex:2825:$r^{E_\tau}(z) = \Omega_{\mathfrak{sl}_3}\cdot\zeta(z|\tau)
chapters/examples/rosetta_stone.tex:2867:R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{so}_8}}{z}\,.
chapters/examples/rosetta_stone.tex:5762:\frac{\Omega^{(1)}}{z}
chapters/examples/rosetta_stone.tex:5764:\frac{\Omega^{(2)}}{z}\,,
chapters/frame/preface.tex:274:\Omega\,dz/((k + h^\vee)z)$, a rational one-form in $z$.
standalone/preface_full_survey.tex:507:\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2},
standalone/bar_chain_models_chiral_quantum_groups.tex:226:where $\Omega \in \fg \otimes \fg$ is the Casimir.  This $r(z)$
chapters/connections/spectral-braiding-core.tex:1007: \frac{\Omega_m}{z^{m+1}},
chapters/connections/spectral-braiding-core.tex:1436: r_{12}(z)\,r_{21}(-z) \;=\; -\frac{(\Omega,\Omega)}{z^2}\,\mathrm{id},
chapters/connections/spectral-braiding-core.tex:4179: $r^{E_\tau}(z) = \Omega \cdot \zeta(z|\tau) +
chapters/connections/spectral-braiding-core.tex:4232: \underbrace{\Omega \cdot \zeta(z|\tau)}_{\text{Sector I:
chapters/connections/spectral-braiding-core.tex:4251: \Omega \cdot \zeta(z|\tau)
chapters/connections/spectral-braiding-core.tex:4253: \frac{\Omega}{z}
chapters/connections/spectral-braiding-core.tex:4254: \;-\; \Omega \cdot G_2(\tau)\,z
chapters/connections/spectral-braiding-core.tex:4255: \;-\; \Omega \cdot G_4(\tau)\,z^3
chapters/connections/spectral-braiding-core.tex:4258:The leading correction $-\Omega\,G_2(\tau)\,z$ is
chapters/connections/spectral-braiding-core.tex:4384:$-\Omega\,G_2(\tau)\,z$, and

thinking
**Searching for equations**

I’m thinking about searching for lines where r(z)=Omega/z directly. I could use a command like `rg -n 'r[^\\n]*Omega[^\\n]*/z'` to find those. Also, there's an equation R(z)=1+Omega/z, which I should consider. I want to inspect the outcomes, but there might be a lot to sift through. I should probably run this search across all volumes to ensure I cover everything I need.
codex
I’ve got the broad candidate pool. Now I’m tightening it to actual bare `r(z)=\Omega/z`-type surfaces, since KZ denominators and quantum `\hbar\,\Omega/z` terms are not automatically AP126 violations.
exec
/bin/zsh -lc "rg -n 'r["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|R\\(z\\)["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n 'r["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|R\\(z\\)["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n 'r["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|R\\(z\\)["'^'"\\n]{0,120}\\\\Omega["'^'"\\n]{0,40}/z|\\\\frac\\{\\\\Omega\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
chapters/examples/w-algebras-stable.tex:1741:collision residue $r^{B_2}(z) = k \cdot \Omega_{B_2}/z$ that
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
standalone/preface_full_survey.tex:507:\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2},
standalone/preface_full_survey.tex:513:r-matrix is $r(z) = k\,\Omega/z$.
standalone/preface_full_survey.tex:1140:$r(z) = k\,\Omega/z$ as classical limit.
standalone/preface_full_survey.tex:1261:$r(z) = k\,\Omega/z$. The KZ connection is the degree-$(2,0)$
chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
chapters/examples/examples-worked.tex:2729:$r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:2860: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$,
chapters/examples/examples-worked.tex:3150:\item The collision residue $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$
chapters/examples/examples-worked.tex:3280: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$.
chapters/examples/examples-worked.tex:3394: $r(z) = k\,\Omega_{\mathfrak{sl}_2}/z$ is the same for both
chapters/examples/examples-worked.tex:3438: via the collision residue $r(z) = k\,\Omega/z$.
chapters/examples/examples-worked.tex:3467:classical limit: $r(z) = k\,\Omega/z$ is the classical
chapters/examples/examples-worked.tex:3569:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
chapters/examples/examples-worked.tex:3626: $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
chapters/examples/examples-worked.tex:3678:$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
chapters/examples/examples-worked.tex:4593:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
 succeeded in 51ms:
chapters/examples/w_algebras_deep.tex:2125:class-$L$ r-matrix $r^{\mathrm{KM}}(z) = k\,\Omega/z$) are confined
chapters/examples/w_algebras_deep.tex:2135: $r^{\mathrm{KM}}(z) = k\,\Omega/z$ (class~$L$) maps to a
chapters/examples/w_algebras_deep.tex:2821: r^{\mathrm{KM}}(z) = k\,\Omega/z
chapters/examples/w_algebras_deep.tex:2867: The simple-pole KM $r$-matrix $k\,\Omega/z$ acquires
standalone/chiral_chern_weil.tex:146:$r(z) = k\,\Omega/z$ is valued in $\fg \otimes \fg$, and
standalone/chiral_chern_weil.tex:762:The $r$-matrix is $r(z) = k\,\Omega/z$.
standalone/chiral_chern_weil.tex:840:The $r$-matrix is $r(z) = k\,\Omega/z$ with $\Omega = \sum_{a=1}^8
standalone/chiral_chern_weil.tex:1044:$r(z) = k\,\Omega/z$ (trace-form convention). The averaging
chapters/examples/lattice_foundations.tex:5003:The classical $r$-matrix is $r(z) = k\Omega/z$ \textup{(}simple pole,
chapters/examples/lattice_foundations.tex:5018:The $r$-matrix identification $r(z) = k\Omega/z$ follows from the
chapters/examples/lattice_foundations.tex:5022:$r(z) = k\Omega/z$: the double pole $k\kappa^{ab}/(z{-}w)^2$
standalone/three_parameter_hbar.tex:197: \cdot \frac{\Omega}{z}.
standalone/three_parameter_hbar.tex:225: \hbar \cdot \frac{\Omega}{z}
standalone/three_parameter_hbar.tex:233:$r(z) = \hbar\,\Omega/z$. The loop parameter is the formal deformation
standalone/three_parameter_hbar.tex:294:$r(z) = (k/(k+h^\vee)) \cdot \Omega/z + (1/(k+h^\vee)) \cdot
standalone/three_parameter_hbar.tex:337:$R(z;\hbar) = 1 + \hbar\,\Omega/z + O(\hbar^2)$. The classical
standalone/programme_summary_sections5_8.tex:132:$\mathrm{av}(k\,\Omega/z) = \dim(\fg)(k + h^\vee)/(2h^\vee)$.
standalone/programme_summary_section1.tex:525:\mathrm{av}(k\,\Omega/z)
standalone/survey_track_a_compressed.tex:321:r(z)\;=\;k\,\Omega/z,\qquad\Omega=\sum_a J^a\otimes J_a
standalone/survey_track_a_compressed.tex:325:\mathrm{av}(k\Omega/z)\;=\;\frac{(k+h^\vee)\dim\mathfrak g}{2h^\vee}\;=\;\kappa(\widehat{\mathfrak g}_k).
 succeeded in 51ms:
chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
chapters/examples/toroidal_elliptic.tex:5993:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
chapters/theory/braided_factorization.tex:524:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
chapters/connections/cy_holographic_datum_master.tex:775:For $X = \C^3$, $r_{CY}^{\C^3}(z) = k\,\Omega_{Y(\widehat{\fgl}_1)}/z$ has
chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.

thinking
**Examining level prefixes**

I’m looking into the rule that says the level prefix k is mandatory, and in AP126 checks, it substitutes k=0. But wait, if I've already specialized to k=1 in a specific case, there might not be a free k left to substitute! That's tricky. The warning about losing dependence makes sense, but in a fixed level-1 example, it seems like Ω/z is indeed correct. It’s a fine line to navigate!
codex
I’m narrowing further to literal bare numerators `\Omega/z` and `\frac{\Omega}{z}`. That catches the actual AP126 surface more cleanly than the earlier broad `\Omega.*z` sweep.
exec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | head -250" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
chapters/examples/toroidal_elliptic.tex:2759:$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
chapters/examples/toroidal_elliptic.tex:5993:The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
chapters/connections/geometric_langlands.tex:38:At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
chapters/theory/braided_factorization.tex:524:$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
chapters/theory/e1_chiral_algebras.tex:89:not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
chapters/theory/quantum_chiral_algebras.tex:152:The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
 succeeded in 52ms:
standalone/preface_full_survey.tex:439:(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
standalone/preface_full_survey.tex:507:\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2},
standalone/preface_full_survey.tex:513:r-matrix is $r(z) = k\,\Omega/z$.
standalone/preface_full_survey.tex:520:k\,\Omega/z$ is the Lie-algebra Jacobi identity for $\fg$: the
standalone/preface_full_survey.tex:1140:$r(z) = k\,\Omega/z$ as classical limit.
standalone/preface_full_survey.tex:1261:$r(z) = k\,\Omega/z$. The KZ connection is the degree-$(2,0)$
chapters/examples/w-algebras-w3.tex:1970:$V_k(\mathfrak{sl}_2)$ $R$-matrix $R(z) = 1 + \hbar\,k\,\Omega/z
chapters/examples/examples-worked.tex:1244: $r(z) = k\,\Omega_\fg / z$, satisfying the classical Yang--Baxter
chapters/examples/examples-worked.tex:1296:= k\,\Omega_\fg / z$. The CYBE follows from the MC equation at
chapters/examples/examples-worked.tex:2512:The $r$-matrix $r(z) = k\,\Omega/z$ is the standard rational
chapters/examples/examples-worked.tex:2529:for $r(z) = k\,\Omega/z$ follows from the Jacobi identity
chapters/examples/examples-worked.tex:3438: via the collision residue $r(z) = k\,\Omega/z$.
chapters/examples/examples-worked.tex:3467:classical limit: $r(z) = k\,\Omega/z$ is the classical
chapters/examples/examples-worked.tex:3569:Collision residue & $k\,\Omega/z$ & $k\,\Omega/z$ (same) \\
chapters/examples/examples-worked.tex:3626: $r(z) = k\,\Omega_\fg/z$, where $\Omega_\fg$ is the quadratic
chapters/examples/examples-worked.tex:3678:$r(z) = k\,\Omega_\fg/z$ has the same analytic structure
chapters/examples/examples-worked.tex:3688:is $k\,\Omega_\fg/z$ (by bar-kernel absorption), and the Jacobi
chapters/examples/examples-worked.tex:4593:$r(z) = k\,\Omega/z$ of the Yangian, where $\Omega$ is the
chapters/examples/examples-worked.tex:4700:k\,\Omega_\fg/z,\;\;
chapters/examples/examples-worked.tex:4743: $r(z) = k\,\Omega_\fg / z$
 succeeded in 51ms:
standalone/ordered_chiral_homology.tex:669:$r(z) = \hbar\,\Omega/z$ is in KZ normalisation;
standalone/ordered_chiral_homology.tex:817:$r(z) = \hbar\,\Omega/z
standalone/ordered_chiral_homology.tex:866:$r(z) = \hbar\,\Omega/z$. The full quantum $R$-matrix
standalone/ordered_chiral_homology.tex:1259:  classical $r$-matrix $r(z) = \hbar\,\Omega/z$
standalone/ordered_chiral_homology.tex:3445:$r(z) = \hbar\,\Omega/z$ is recovered.
standalone/ordered_chiral_homology.tex:3586:$r(z) = \hbar\,\Omega/z$), and the kernel
standalone/ordered_chiral_homology.tex:5975:$S(z) = \id + h_{\mathrm{KZ}}\,\Omega/z + O(z^{-2})$. Does
standalone/ordered_chiral_homology.tex:6236:  $r(z) = h_{\mathrm{KZ}}\,\Omega/z$ has a simple pole and no
standalone/ordered_chiral_homology.tex:6894:  $r(z) = k\,\Omega/z$
standalone/ordered_chiral_homology.tex:8574:$r^{\mathrm{rat}}(z) = k\,\Omega/z$.
standalone/programme_summary_section1.tex:525:\mathrm{av}(k\,\Omega/z)
standalone/programme_summary_sections5_8.tex:132:$\mathrm{av}(k\,\Omega/z) = \dim(\fg)(k + h^\vee)/(2h^\vee)$.
standalone/genus1_seven_faces.tex:695:$r^{\mathrm{ell}}_\fg(z,\tau) \to \Omega/z$ through the intermediate
standalone/genus1_seven_faces.tex:724:recovering the level-normalised $\Omega/z$ form (the
standalone/genus1_seven_faces.tex:726:$k\,\Omega/z$ is recovered by undoing the absorption
standalone/survey_modular_koszul_duality_v2.tex:519:r^{\mathrm{KM}}(z)\;=\;k\,\Omega/z,
standalone/survey_modular_koszul_duality_v2.tex:526:\mathrm{av}(k\,\Omega/z)
standalone/survey_modular_koszul_duality_v2.tex:585:nothing. For Kac--Moody, $r(z)=k\,\Omega/z$ carries the Casimir
standalone/survey_modular_koszul_duality_v2.tex:2506:$r^{\mathrm{KM}}(z)=k\,\Omega/z$ with
standalone/survey_modular_koszul_duality_v2.tex:2516:\mathrm{av}(k\,\Omega/z)=\frac{k\dim\fg}{2h^\vee}=\kappa_{\mathrm{dp}},


thinking
**Inspecting mathematical concepts**

I'm diving into specific elements from Volume II, like the standalone preface and whether OPE relates to r-matrix. There's some thought about the log_ht_monodromy_frontier and the residue Omega/(k+2), but I'm unsure about its connection to AP126. I’m also considering `r_{M2}(z)` but am questioning whether it stays at affine level. For Volume III, I think I need to pinpoint the false positives and focus on suspicious lines that match a certain pattern.
thinking
**Exploring equation extraction**

I'm looking into the command for extracting specific equations related to resistance, along with some conditions for tables with cells instead of just equations. That might expand the search a bit. So, for now, I think I'll focus on ensuring I cover all relevant volumes. It seems like a broader search might yield better results while ensuring I capture the right information. Let's see how this shapes up!
codex
I’ve isolated the obvious bare cases. I’m reading those in context now, because some are genuine level-stripping errors and some are legitimate expansions or fixed-normalization quantum formulas.
exec
/bin/zsh -lc "rg -n -P '=\\s*(?:\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?/z\\b)' chapters standalone 2>/dev/null | head -200" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -P '=\\s*(?:\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?/z\\b)' chapters standalone 2>/dev/null | head -200" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "rg -n -P '=\\s*(?:\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}|\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?/z\\b)' chapters standalone 2>/dev/null | head -200" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 51ms:
chapters/connections/spectral-braiding-core.tex:792:$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
chapters/connections/log_ht_monodromy_core.tex:151: r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
chapters/connections/log_ht_monodromy_core.tex:1905: = \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2},
chapters/connections/thqg_gravitational_yangian.tex:623:nondegenerate pairing, and $r_\cA(z) = \Omega_\cA/z + \cdots$.
chapters/connections/thqg_gravitational_yangian.tex:1123:where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
chapters/connections/thqg_gravitational_yangian.tex:1186:$r_{ij}(z) = \Omega_{ij}/z$ becomes
chapters/connections/thqg_gravitational_yangian.tex:1688:= \Omega_{\alpha\beta}/z$.
chapters/connections/log_ht_monodromy.tex:158: r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 succeeded in 51ms:
chapters/examples/yangians_foundations.tex:1059: $r(z) = \Omega_{\mathrm{tr}}/z$.
chapters/theory/introduction.tex.bak:346:discarded.  For affine Kac--Moody, $r(z) = \Omega/z$ contains the
chapters/connections/thqg_gravitational_yangian.tex:622:nondegenerate pairing, and $r_\cA(z) = \Omega_\cA/z + \cdots$.
chapters/connections/thqg_gravitational_yangian.tex:1120:where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
chapters/connections/thqg_gravitational_yangian.tex:1174:$r_{ij}(z) = \Omega_{ij}/z$ becomes
chapters/connections/thqg_gravitational_yangian.tex:1617:= \Omega_{\alpha\beta}/z$.
chapters/theory/higher_genus_modular_koszul.tex:26939: the level-stripped form $r_0(z) = \Omega/z^3$ carries no
chapters/connections/frontier_modular_holography_platonic.tex:4731: $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:2912:For the rational $r$-matrix $r(z) = \Omega/z$

thinking
**Inspecting backup files**

I need to check if there are only backup hits captured by a strict search. In the output, I see files like intro.tex.bak and heisenberg_frame.tex.bak. I’m curious if these are low-quality or stale backups that I should look into further. It feels like a task that could reveal important information about what went wrong. Let’s dig deeper to ensure nothing critical is being overlooked!
codex
I’ve reduced the likely real violations to a smaller set. I’m reading those exact local windows now so the final report only contains genuine level-stripping, not regex artifacts.
exec
/bin/zsh -lc "sed -n '1048,1064p' chapters/examples/yangians_foundations.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 = \frac{\Omega}{(k + h^\vee)\,z}
 \;\in\; \fg \otimes \fg(z^{-1}),
 \end{equation}
 where $\Omega = \sum_a \kappa^{ab}\, I_a \otimes I_b$ is the
 quadratic Casimir tensor (inverse Killing form) and the Sugawara
 denominator $k + h^\vee$ arises from dualizing the zeroth product
 via the level-shifted Killing form
 (Computation~\ref{comp:sl2-collision-residue-kz}).
 %: this is a section on C_2(X), not a formula over a point.
 Equivalently, in the trace-form normalization where
 $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
 $r(z) = \Omega_{\mathrm{tr}}/z$.
 This $r$-matrix satisfies
 the classical Yang--Baxter equation in spectral-parameter form
 \textup{(}equivalently, the infinitesimal braid relations for
 $\Omega$\textup{)}, for all simple~$\fg$
 \textup{(}\texttt{quantum\_rmatrix\_barcomplex.py}, verified
exec
/bin/zsh -lc "sed -n '628,646p' chapters/frame/preface_section1_draft.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
product contributes the curvature~$\kappa$. The coexistence of
both poles, absent in the pure second-order-pole Heisenberg case,
makes $\widehat{\mathfrak g}_k$ the first nontrivial example.

The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
\[
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\]
where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
matrix-valued: $\Omega \in \mathfrak g \otimes \mathfrak g$
carries the full Lie-algebraic structure. Averaging collapses the
Casimir to its trace:
\[
\mathrm{av}\bigl(k\Omega/z\bigr)
\;=\;
\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
\;=\;
exec
/bin/zsh -lc "sed -n '475,493p' chapters/frame/preface_section1_v2.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

\medskip
\noindent\textbf{The Casimir $R$-matrix.}\enspace
The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
collision residue
\begin{equation}\label{eq:pf1-km-rmatrix}
r(z) \;=\; \frac{\Omega}{z}\,,
\qquad
\Omega \;=\; \sum_a J^a \otimes J_a\,,
\end{equation}
where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
tensor. This is matrix-valued: $\Omega$ carries the full
Lie-algebraic structure that was invisible in the Heisenberg
scalar~$k/z$. The averaging map collapses the Casimir to a
scalar:
\begin{equation}\label{eq:pf1-km-kappa}
\mathrm{av}\bigl(k\Omega/z\bigr)
\;=\;
\frac{\dim(\mathfrak g)\cdot(k+h^\vee)}{2h^\vee}
exec
/bin/zsh -lc "sed -n '536,586p' chapters/frame/preface_sections5_9_draft.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '458,476p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
 & G
 & $0$
 & Gaussian archetype\\[2pt]
$\widehat{\fg}_k$
 & $J^a$ (wt~$1$)
 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
 & $\Omega/z$
 & $3$
 & L
 & $0$
 & FF center at $k{=}{-}h^\vee$\\[4pt]
$\mathrm{Vir}_c$
 & $T$ (wt~$2$)
 & $c/2$
 & $\frac{c/2}{z^3}+\frac{2T}{z}$
 & $\infty$
 & M
 & $13$
 & self-dual at $c{=}13$\\[4pt]
$\cW_3{}_c$
exec
/bin/zsh -lc "sed -n '709,723p' chapters/connections/holographic_datum_master.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:

The original spectral $r$-matrix is Drinfeld's~\cite{Drinfeld85},
introduced in connection with the quantum Yang--Baxter equation and
the Yangian deformation $Y_\hbar(\fg)$ of the universal enveloping
algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
r^{\mathrm{Dr}}(z)
\;=\;
\frac{\Omega}{z}
\;\in\;
\fg \otimes \fg [\![z^{-1}]\!],
\qquad
\Omega \;=\; \sum_a J^a \otimes J^a,
\end{equation}
where $\{J^a\}$ is an orthonormal basis of $\fg$ with respect to the
Killing form, satisfies the classical
Yang--Baxter equation
$[r^{\mathrm{Dr}}_{12}(z), r^{\mathrm{Dr}}_{13}(z+w)]
+ [r^{\mathrm{Dr}}_{12}(z), r^{\mathrm{Dr}}_{23}(w)]
 succeeded in 51ms:
\{\cdot_\lambda \cdot\}\;\textrm{(KZ25)}
 \ar@{<->}[r]
 \ar@{<->}[d]
& \{H_i^{\mathrm{GZ}}\}\;\textrm{(GZ26)}
 \ar@{<->}[d]^{\textrm{(F4)}}\\
\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
 \ar@{<->}[r]^-{\textrm{(F6)}}
& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
 \ar@{<->}[u]^{\textrm{(F5--F7)}}
}
\end{equation}

\begin{theorem}[Seven-way master theorem; \ClaimStatusProvedHere]
\label{thm:hdm-seven-way-master}
exec
/bin/zsh -lc "sed -n '688,727p' standalone/genus1_seven_faces.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '4726,4768p' chapters/connections/frontier_modular_holography_platonic.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '342,349p' chapters/theory/introduction.tex.bak" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '2908,2915p' chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
+ [r_{13}(z_1 - z_3),\, r_{23}(z_2 - z_3)]
\;=\; 0
\end{equation}
is a statement about three points $z_1, z_2, z_3$ on the curve.
For the rational $r$-matrix $r(z) = \Omega/z$
(where $\Omega \in \fg \otimes \fg$ is the Casimir tensor of an
affine Kac--Moody algebra), the three terms are respectively
$[\Omega_{12}, \Omega_{13}]/(z_{12}\,z_{13})$,
 succeeded in 52ms:
$\wp^{(m)}(z,\tau) \to (-1)^m(m+1)!/z^{m+2} + O(z^{-m})$.

\item \textup{(KZB $\to$ KZ.)} The $dz$-component degenerates to
the KZ connection: $\zeta_\tau(z_{ij}) \to 1/z_{ij}$. The
$d\tau$-component has no genus-$0$ counterpart.

\item \textup{(Elliptic $\to$ rational $r$-matrix.)}
$r^{\mathrm{ell}}_\fg(z,\tau) \to \Omega/z$ through the intermediate
trigonometric $r$-matrix:
$r^{\mathrm{ell}} \to r^{\mathrm{trig}} \to r^{\mathrm{rat}}$,
in the level-normalised convention where the
$1/(k+h^\vee)$ prefactor is absorbed into the rescaled $\Omega$.

\item \textup{(Elliptic $\to$ rational Gaudin.)}
$H_i^{\mathrm{ell}} \to H_i^{\mathrm{Gaudin}} = \sum_{j \neq i}
\Omega_{ij}/(z_i - z_j)$.
\end{enumerate}
\end{theorem}

\begin{proof}
 succeeded in 52ms:
 \kappa(\mathfrak{gl}_N,\, k{=}1)
 \;=\;
 \frac{(N^2{-}1)(N{+}1)}{2N} + 1.
 \]
 The holographic R-matrix at level $k=1$ is
 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
 The anomaly matching condition
 $\kappa_{\mathrm{eff}}
 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
 is a consistency check.

\item \emph{Sphere reconstruction.}
 The genus-$0$, $n$-point shadow amplitudes
 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
 diagram amplitudes of the holomorphic twist. The
 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
 succeeded in 52ms:
records the non-symmetric components of the line-operator data.
For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
the symmetrization recovers the scalar
$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
discarded.  For affine Kac--Moody, $r(z) = \Omega/z$ contains the
full Yangian double; the symmetrization recovers
$\kappa(\widehat{\mathfrak g}_k) = (k + h^\vee)\dim\mathfrak g/(2h^\vee)$
and discards the entire Drinfeld--Jimbo deformation.


thinking
**Identifying convention errors**

I'm noticing a potential conflict in the definitions of `Ω_tr` based on the equation provided. It suggests a redefined symbol absorbing the factor, indicating a possible convention error. The user’s mission is referring to `Ω/z`, without a level prefix, which could be a violation as the subscripted `Ω_tr` lacks the `k` prefix.  

The backup files have explicit `Ω/z`, and since they are stale, they might be reported as low priority. I need to inspect the gravitational Yangian contexts further for consistency across volumes.
thinking
**Inspecting volume contexts**

I want to read through volumes 1 and 2 separately to see if they contain the same lines. I'll use `sed` to isolate the potentially suspicious lines for a closer inspection. It's essential to ensure that I'm examining both sets thoroughly. By checking them individually, I can identify any discrepancies or shared content that might need further attention. Let’s see what we find in each volume!
codex
Some candidates are now clearly false positives because they explicitly absorb the prefactor into a redefined symbol or state a different normalization. I’m checking the remaining ambiguous ones, especially the generic `r_\mathcal A(z)=\Omega_\mathcal A/z` and table entries, before I assign severity.
exec
/bin/zsh -lc "sed -n '614,629p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1114,1189p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '617,630p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1554,1578p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1117,1190p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1428,1450p' chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '145,188p' chapters/connections/log_ht_monodromy.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1680,1694p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '145,188p' chapters/connections/log_ht_monodromy_core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1609,1623p' chapters/connections/thqg_gravitational_yangian.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Theorem~\ref{thm:collision-residue-twisting}, reproduced here for
the gravitational context. For the three properties:

\emph{Property~(i).}
At the leading pole, the collision residue extracts $a_{(0)}b$,
which on the Koszul dual $\cA^!$ produces the natural pairing.
The Casimir $\Omega_\cA = \sum_\alpha e_\alpha \otimes e^\alpha
\in \cA^! \otimes \cA^!$ is the image of the identity under the
nondegenerate pairing, and $r_\cA(z) = \Omega_\cA/z + \cdots$.

\emph{Property~(ii).}
The chiral OPE satisfies
$(a_{(0)}b)(z) = -(b_{(0)}a)(z) + \partial(a_{(-1)}b)(z)$
(the Borcherds commutator formula). On Koszul dual generators,
the exact term vanishes in cohomology, giving
$r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
 succeeded in 51ms:
\frac{\Omega_{31}\,\Omega_{12}
 - \Omega_{12}\,\Omega_{31}}{z_{31}\,z_{12}}
&\;=\;
\bigl[r_{31}(z_{31}),\;r_{12}(z_{12})\bigr],
\label{eq:thqg-V-cybe-term3}
\end{align}
where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
(For algebras with higher-order poles in the $r$-matrix, such as
$\mathrm{Vir}_c$, additional terms appear at higher collision depth;
the leading-order CYBE is the universal statement valid for all
modular Koszul algebras.)

Using $z_{31} = -z_{13}$ (the sign is absorbed into the skew-symmetry
$r_{31}(z_{31}) = r_{31}(-z_{13}) = -r_{13}(z_{13})$
by the relabeling convention), the sum
\eqref{eq:thqg-V-cybe-term1}--\eqref{eq:thqg-V-cybe-term3}
gives exactly the CYBE~\eqref{eq:thqg-V-cybe}.
\end{proof}

\begin{remark}[Gravitational interpretation of the CYBE]
 succeeded in 52ms:

\emph{Property~(i).}
At the leading pole, the collision residue extracts $a_{(0)}b$,
which on the Koszul dual $\cA^!$ produces the natural pairing.
The Casimir $\Omega_\cA = \sum_\alpha e_\alpha \otimes e^\alpha
\in \cA^! \otimes \cA^!$ is the image of the identity under the
nondegenerate pairing, and $r_\cA(z) = \Omega_\cA/z + \cdots$.

\emph{Property~(ii).}
The chiral OPE satisfies
$(a_{(0)}b)(z) = -(b_{(0)}a)(z) + \partial(a_{(-1)}b)(z)$
(the Borcherds commutator formula). On Koszul dual generators,
the exact term vanishes in cohomology, giving
$r_\cA(z)_{12} = -r_\cA(-z)_{21}$.
 succeeded in 51ms:
\frac{\Omega_{31}\,\Omega_{12}
 - \Omega_{12}\,\Omega_{31}}{z_{31}\,z_{12}}
&\;=\;
\bigl[r_{31}(z_{31}),\;r_{12}(z_{12})\bigr],
% label removed: eq:thqg-V-cybe-term3
\end{align}
where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
(For algebras with higher-order poles in the $r$-matrix, such as
$\mathrm{Vir}_c$, additional terms appear at higher collision depth;
the leading-order CYBE is the universal statement valid for all
modular Koszul algebras.)

The spectral parameter $z_{ij} = z_i - z_j$ satisfies
$z_{ji} = -z_{ij}$. Skew-symmetry of~$r$ gives
$r(z_{ji}) = r(-z_{ij}) = -P \cdot r(z_{ij}) \cdot P$, where
$P$ is the permutation operator exchanging the two tensor factors.
In particular $z_{31} = -z_{13}$, and
$r_{31}(z_{31}) = r_{31}(-z_{13}) = -r_{13}(z_{13})$
by the skew-symmetry property
(Theorem~\ref{V1-thm:thqg-V-collision-twisting}(ii)).
 succeeded in 52ms:
\begin{computation}[Formal $R$-matrix expansion; \ClaimStatusProvedHere]
\label{comp:formal-R-expansion}
\index{R-matrix@$R$-matrix!formal expansion}
The formal monodromy operator, equivalently the asymptotic $R$-matrix,
admits the $z^{-1}$-expansion (with $\Omega$ denoting the Sugawara-normalized
residue tensor $k\,\Omega_{\mathrm{Cas}}/(k+h^\vee)$ absorbing the level prefix and the level-explicit form at~\eqref{eq:R-level-explicit} below)
\begin{equation}\label{eq:R-formal-expansion}
 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
\end{equation}
More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
(Magnus series). On $V\otimes V$ one can diagonalize:
\[
 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
 \qquad
 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
\]
The leading-order formula
\begin{equation}\label{eq:R-level-explicit}
 succeeded in 51ms:
$\widehat{\mathfrak{sl}}_2$ level-$1$ WZW fusion rules.
\end{computation}

\begin{computation}[Formal $R$-matrix expansion; \ClaimStatusProvedHere]
% label removed: comp:formal-R-expansion
\index{R-matrix@$R$-matrix!formal expansion}
The formal monodromy operator, equivalently the asymptotic $R$-matrix,
admits the $z^{-1}$-expansion
\begin{equation}% label removed: eq:R-formal-expansion
 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
\end{equation}
More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
(Magnus series). On $V\otimes V$ one can diagonalize:
\[
 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
 \qquad
 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
\]
 succeeded in 51ms:
\]
where $u_{ij}$ is a unit and $P(i,j)$ is the set of tree edges separating $i$ from $j$. Thus collisions become normal-crossings divisors in logarithmic coordinates.

\subsection{Strict rational dg-shifted Yangians}
The full notion of dg-shifted Yangian belongs to a broader program \cite{DNP25}. For the strict rational theory developed below we isolate only the structure used.

\begin{definition}[Strict rational dg-shifted Yangian]% label removed: def:strict-yangian
A \emph{strict rational dg-shifted Yangian} consists of the following data:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item an associative dg algebra $Y$;
 \item a degree-zero derivation $T$ (the translation operator);
 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
 \[
 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 \]
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
 \]
\end{enumerate}
 succeeded in 51ms:
A \emph{strict rational dg-shifted Yangian} consists of the following data:
\begin{enumerate}[label=\textup{(\alph*)}]
 \item an associative dg algebra $Y$;
 \item a degree-zero derivation $T$ (the translation operator);
 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
 \[
 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
 \]$, the residue element absorbs
 the level $k$, so the affine realization reads
 $r(z)=k\,\Omega_{\mathrm{aff}}/z$ with $\Omega_{\mathrm{aff}}$ the
 quadratic Casimir tensor of $\mathfrak g$, vanishing at $k=0$, cf.\
 the affine specialization at the start of Section~\ref{sec:strict}.)
 \item the parameter-dependent classical Yang-Baxter equation
 \[
 [r_{12}(u),r_{13}(u+v)] + [r_{12}(u),r_{23}(v)] + [r_{13}(u+v),r_{23}(v)] = 0.
 \]
\end{enumerate}
\end{definition}

The datum $(Y,r,T)$ is the strict shadow of the full $A_\infty$ structure treated later.
 succeeded in 51ms:
\index{Yangian!generators from weight filtration}
The weight filtration on $\Ydg_\cA$ at genus zero
(the degree filtration) produces Yangian generators.
Let $\{e_\alpha\}$ be a basis of $\cA^!$ homogeneous with respect
to the conformal weight grading.

\emph{Level~$0$ generators.}
$T_{\alpha\beta}^{(0)} := \langle e_\alpha,\,r_\cA(z)\,e_\beta\rangle
= \Omega_{\alpha\beta}/z$.
These are the $\fg$-currents at degree~$2$.

\emph{Level~$r$ generators.}
$T_{\alpha\beta}^{(r)}$ is the coefficient of $z^{-r-1}$ in the
Laurent expansion of $r_\cA(z)$ at $z = 0$:
\begin{equation}% label removed: eq:thqg-V-yangian-generators
 succeeded in 51ms:
\index{Yangian!generators from weight filtration}
The weight filtration on $\Ydg_\cA$ at genus zero
(the degree filtration) produces Yangian generators.
Let $\{e_\alpha\}$ be a basis of $\cA^!$ homogeneous with respect
to the conformal weight grading.

\emph{Level~$0$ generators.}
$T_{\alpha\beta}^{(0)} := \langle e_\alpha,\,r_\cA(z)\,e_\beta\rangle
= \Omega_{\alpha\beta}/z$.
These are the $\fg$-currents at degree~$2$.

\emph{Level~$r$ generators.}
$T_{\alpha\beta}^{(r)}$ is the coefficient of $z^{-r-1}$ in the
Laurent expansion of $r_\cA(z)$ at $z = 0$:
\begin{equation}\label{eq:thqg-V-yangian-generators}


thinking
**Evaluating mathematical discrepancies**

I recognize that the user is interested in a mathematical generalization of rational Yangian, but specifically mentioned AP126. The formulas in the repo could coexist generically, and if I report all of them, it could get complicated. I need to determine if there’s a genuine discrepancy from AP126 or if it’s a separate object. The search instructions seem to suggest that any generic formulas without an affine level should be treated carefully, considering false positives versus real violations.
thinking
**Identifying potential false positives**

I see that the log_ht_monodromy definition and the formal R-expansion define a generic Yangian with residue Ω/z, and they mention affine specialization later. These seem likely to be false positives for AP126, but there are still convention risks to consider. I’ll need to take a closer look at volume 2, specifically line 792 in `spectral-braiding-core`. It could indicate that Ω_k/z equals kΩ/z, which likely isn't a violation since it directly corresponds to kΩ/z.
codex
The generic Yangian definitions are not automatic AP126 hits; they absorb the normalization into the residue object. I’m checking the remaining explicit affine/Drinfeld prose and table surfaces, which are the likely genuine violations.
exec
/bin/zsh -lc "sed -n '432,516p' standalone/preface_full_survey.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '423,430p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '786,794p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '4248,4256p' chapters/connections/spectral-braiding-core.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '1964,1976p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "sed -n '2788,2801p' chapters/examples/rosetta_stone.tex" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:

\smallskip
\noindent\textbf{Classical $r$-matrix.}\enspace
The bar complex uses the propagator $d\log(z-w)$, which absorbs one pole order from the OPE: the OPE $J(z)J(w)\sim k/(z-w)^2$ has a double pole, and the $d\log$ kernel reduces this to a simple-pole collision residue. The classical $r$-matrix is therefore
\[
r(z) \;=\; \frac{k}{z}.
\]
(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
The quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$. Yang--Baxter
holds trivially (the exponential of a scalar commutes with itself).

\smallskip
\noindent\textbf{Line operators.}\enspace
The chiral Koszul dual is
$\cA^!_{\mathrm{ch}} = \mathrm{Sym}^{\mathrm{ch}}(V^*)$
(Vol~I, Theorem~\ref*{V1-thm:heisenberg-bar}; note
$\cH_k^!\neq\cH_{-k}$). The open-colour dual is
$\cA^!_{\mathrm{line}} = Y(\mathfrak{u}(1)) \simeq \cH_{-k}$.
The line side is modeled by modules for
$\cA^!_{\mathrm{line}} = Y(\mathfrak{u}(1)) \simeq \cH_{-k}$:
 succeeded in 51ms:
how operators collide---the multiplicative structure.  The coproduct
$\Delta$ encodes \emph{splitting}: how a single operator decomposes
into a tensor product of two operators.  Splitting is independent
structure, invisible in the shadow tower and not determined by the
$r$-matrix alone.

Concretely, the deconcatenation coproduct on
$B^{\mathrm{ord}}(A) = T^c(s^{-1}\bar A)$ is \emph{structural}:
 succeeded in 52ms:
Hence the Casimir-zeta sector contributes only \emph{odd}
$z$-powers, with leading correction
\begin{equation}\label{eq:sector-I-leading}
 \Omega \cdot \zeta(z|\tau)
 \;=\;
 \frac{\Omega}{z}
 \;-\; \Omega \cdot G_2(\tau)\,z
 \;-\; \Omega \cdot G_4(\tau)\,z^3
 \;-\; \cdots
 succeeded in 52ms:
vertex algebra at level~$k$
(Frenkel--Ben-Zvi \cite{FBZ04}).
Generators: currents $J^a(z)$, $a = 1, \ldots, \dim \fg$.
OPE relations:
\begin{equation}\label{eq:cs-km-ope}
J^a(z)\, J^b(w)
\;\sim\;
\frac{k\,\kappa^{ab}}{(z-w)^2}
\;+\;
\frac{f^{ab}{}_c\, J^c(w)}{z-w},
\end{equation}
where $\kappa^{ab}$ is the Killing form and $f^{ab}{}_c$
are the structure constants of~$\fg$. In modes:
 succeeded in 52ms:

\begin{proof}
The invariant bilinear form at level $k$ on $\fg$ is
$(\cdot,\cdot)_k = k\,\kappa(\cdot,\cdot)$. The associated
Casimir tensor is $\Omega_k = k\,\kappa^{IJ}\,t_I \otimes t_J
= k\,\Omega$. The standard rational solution of the CYBE for
$\widehat{\fg}_k$ is $r(z) = \Omega_k/z = k\,\Omega/z$.
This is confirmed by the Laplace transform
\textup{(}Proposition~\textup{\ref{prop:field-theory-r}}\textup{)}:
 succeeded in 51ms:
\smallskip
\noindent
\emph{$R$-matrix and Koszul dual.}
The collision residue is the $\mathfrak{sl}_3$ classical
$r$-matrix:
$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
the Yang $R$-matrix
\begin{equation}\label{eq:A2-lattice-R}
R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
\end{equation}
The Koszul dual is the Yangian
$Y_\hbar(\mathfrak{sl}_3)$.





thinking
**Evaluating mathematical inconsistencies**

I’m looking at the formula from line 507, which involves a Laplace transform of the λ-bracket. There seems to be an inconsistency with the terms: the formula has no k in the Ω/z term, but the final residue does include it. I thought Ω would include structure constants, but it turns out Ω is defined independently of k. This could be a critical issue in the derivation, so I might need to report the problem with lines 507-513.
thinking
**Assessing severity of violations**

I’m considering the severity of various mathematical violations mentioned. It seems any real mathematical issue should be assessed as CRITICAL, while structural issues might only be HIGH. There are lots of wrong formulas that could indeed fall under CRITICAL. For instance, line 4253 expands a zeta sector without including k. Also, in a case from line 2795, the specialization could imply medium severity. I'll have to decide if this counts as a genuine violation since the repository seems to expect every Ω/z term to have a k prefix.
thinking
**Classifying severity of line issues**

This line clearly omits k at a fixed level, which makes me wonder about its severity. I think it might be best to categorize this as MEDIUM or possibly HIGH. While it does have a mathematical element, it’s specialized to a unit level rather than being numerically incorrect. Maybe MEDIUM is appropriate here, since it suggests a prose specialization that goes against convention, but it maintains its value at k=1.
thinking
**Checking survey lines**

I need to check the preface_full_survey, focusing on line 507 and maybe line 439. There’s a comment there about separating Ω/z from the kK/z^2 term. This could potentially violate something since it treats Ω/z as a collision residue term. However, I think the formula in line 507 and the correction in line 513 should be sufficient on their own. It’s a bit tricky, but I’ll get to the bottom of it!
thinking
**Inspecting monodromy formula**

I’m thinking about the monodromy formula and how it relates to the position-space kernel, just like in the preface_full_survey. I need to focus on the specific period between 1898 and 1914. That's an interesting timeframe to explore, so let’s dig into it! I’m curious about what insights or findings we might uncover. I’ll keep my approach thorough to ensure I gather relevant information.
codex
I’ve got a small set of likely true positives now. I’m re-reading the last ambiguous cases with line-numbered context so the final report is exact and free of false positives.
exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy_core.tex | sed -n '1898,1916p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/examples/rosetta_stone.tex | sed -n '2791,2799p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface_section1_v2.tex | sed -n '478,486p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
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
  1911	(proportional to the identity on $V_i \otimes V_j$). The
  1912	scalar term does not contribute to the braiding (it exponentiates
  1913	to a scalar phase), so the braiding is governed by
  1914	$r(z) = k\,\Omega/z$ at level~$k$ up to scalars.
  1915	
  1916	\smallskip\noindent
exec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '713,719p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba standalone/preface_full_survey.tex | sed -n '502,514p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/frame/preface_section1_draft.tex | sed -n '631,639p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/holographic_datum_master.tex | sed -n '462,470p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface_sections5_9_draft.tex | sed -n '539,544p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/yangians_foundations.tex | sed -n '1054,1061p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/preface_sections5_9_draft.tex | sed -n '578,583p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2791	The collision residue is the $\mathfrak{sl}_3$ classical
  2792	$r$-matrix:
  2793	$r(z) = k\,\Omega_{\mathfrak{sl}_3}/z$,
  2794	where $\Omega_{\mathfrak{sl}_3}$ is the quadratic Casimir
  2795	of~$\mathfrak{sl}_3$; at level~$k=1$ the collision residue is $\Omega_{\mathfrak{sl}_3}/z$. The spectral $R$-matrix is
  2796	the Yang $R$-matrix
  2797	\begin{equation}\label{eq:A2-lattice-R}
  2798	R(z) \;=\; 1 + \frac{\hbar\,\Omega_{\mathfrak{sl}_3}}{z}\,.
  2799	\end{equation}
 succeeded in 51ms:
   478	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the
   479	collision residue
   480	\begin{equation}\label{eq:pf1-km-rmatrix}
   481	r(z) \;=\; \frac{\Omega}{z}\,,
   482	\qquad
   483	\Omega \;=\; \sum_a J^a \otimes J_a\,,
   484	\end{equation}
   485	where $\Omega \in \mathfrak g \otimes \mathfrak g$ is the Casimir
   486	tensor. This is matrix-valued: $\Omega$ carries the full
 succeeded in 51ms:
   713	 \ar@{<->}[d]^{\textrm{(F4)}}\\
   714	\{\cdot,\cdot\}_{\mathrm{STS}}\;\textrm{(STS83)}
   715	 \ar@{<->}[r]^-{\textrm{(F6)}}
   716	& \{H_i^{\mathrm{Gaudin}}\}\;\textrm{(FFR94)}\\
   717	& \frac{\Omega}{z}\;\textrm{(Drinfeld85)}
   718	 \ar@{<->}[u]^{\textrm{(F5--F7)}}
   719	}
 succeeded in 52ms:
   631	
   632	The ordered bar complex of $\widehat{\mathfrak g}_k$ carries the $R$-matrix
   633	\[
   634	r(z) \;=\; \frac{\Omega}{z}\,,
   635	\qquad
   636	\Omega \;=\; \sum_a J^a \otimes J_a\,,
   637	\]
   638	where $\Omega$ is the Casimir tensor of~$\mathfrak g$. This is
   639	matrix-valued: $\Omega \in \mathfrak g \otimes \mathfrak g$
 succeeded in 52ms:
   502	\;\otimes\; J_a \otimes J_b
   503	\;=\;
   504	\frac{f^{ab}{}_c\,J^c}{z}\,J_a\otimes J_b
   505	 + \frac{k\,\delta^{ab}}{z^2}\,J_a\otimes J_b
   506	\;=\;
   507	\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2},
   508	\]
   509	where $\Omega = \sum_a J^a \otimes J_a$ is the split Casimir
   510	and $K_{\fg} = \sum_a J_a \otimes J^a$ is the Killing form
   511	tensor. The scalar term $k\,K_{\fg}/z^2$ is ad-invariant
   512	and contributes trivially to the CYBE; the collision residue
   513	r-matrix is $r(z) = k\,\Omega/z$.
   514	The KZ connection $\nabla_{\mathrm{KZ}} = d - \frac{1}{k+h^\vee}\,\Omega\,d\log z$ is
 succeeded in 51ms:
   462	algebra of a simple Lie algebra~$\fg$. The classical $r$-matrix
   463	\begin{equation}\label{eq:hdm-drinfeld-rmatrix}
   464	r^{\mathrm{Dr}}(z)
   465	\;=\;
   466	\frac{\Omega}{z}
   467	\;\in\;
   468	\fg \otimes \fg [\![z^{-1}]\!],
   469	\qquad
   470	\Omega \;=\; \sum_a J^a \otimes J^a,
 succeeded in 51ms:
   539	$\widehat{\fg}_k$
   540	 & $J^a$ (wt~$1$)
   541	 & $\frac{(k{+}h^\vee)\dim\fg}{2h^\vee}$
   542	 & $\Omega/z$
   543	 & $3$
   544	 & L
 succeeded in 51ms:
  1054	 via the level-shifted Killing form
  1055	 (Computation~\ref{comp:sl2-collision-residue-kz}).
  1056	 %: this is a section on C_2(X), not a formula over a point.
  1057	 Equivalently, in the trace-form normalization where
  1058	 $\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$, the $r$-matrix reads
  1059	 $r(z) = \Omega_{\mathrm{tr}}/z$.
  1060	 This $r$-matrix satisfies
  1061	 the classical Yang--Baxter equation in spectral-parameter form
 succeeded in 51ms:
   578	 & arithmetic from~$q$\\[2pt]
   579	$Y(\fg)$
   580	 & line operators
   581	 & $\mathrm{av}(\Omega/z)$
   582	 & $\Omega/z$
   583	 & $3$

thinking
**Inspecting inconsistencies in logs**

I need to take a look at line 1905 in the log_ht_monodromy_core because it seems to show a similar issue to preface_full_survey. The formula says Ω/z + kκ/z^2, but then it claims braiding is governed by kΩ/z, which feels inconsistent. I should probably report this since it’s not just a definition in a generic manuscript surface. I need to check if the same issue exists in the non-core file too, especially since I've found both versions.
exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy.tex | sed -n '156,160p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/log_ht_monodromy.tex | sed -n '1435,1449p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   156	 \item a meromorphic element $r(z)\in (Y\otimes Y)(z)$, regular at infinity, with a simple pole at the origin,
   157	 \[
   158	 r(z)=\frac{\Omega}{z}+r_{\mathrm{reg}}(z),\qquad \Omega\in Y\otimes Y;
   159	 \]
   160	 \item the parameter-dependent classical Yang-Baxter equation
exec
/bin/zsh -lc "nl -ba standalone/genus1_seven_faces.tex | sed -n '692,726p'" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
  1435	admits the $z^{-1}$-expansion
  1436	\begin{equation}% label removed: eq:R-formal-expansion
  1437	 R(z) \;=\; 1 + \frac{\Omega}{z} + \frac{\Omega^2}{2z^2} + \frac{\Omega^3}{6z^3}+\cdots
  1438	 \;=\; \exp\!\Bigl(\frac{\Omega}{z}\Bigr)\quad (\text{leading order}).
  1439	\end{equation}
  1440	More precisely, at level~$k$ the ratio $\Omega/(k+2)$ replaces $\Omega$
  1441	and corrections of order $O(z^{-3})$ arise from the non-abelian exponentiation
  1442	(Magnus series). On $V\otimes V$ one can diagonalize:
  1443	\[
  1444	 R(z)\big|_{V_1} = e^{1/(2z)}\bigl(1+O(z^{-3})\bigr),
  1445	 \qquad
  1446	 R(z)\big|_{V_0} = e^{-3/(2z)}\bigl(1+O(z^{-3})\bigr).
  1447	\]
  1448	The leading-order formula $R(z)=1+k\,\Omega/z+O(z^{-2})$
  1449	at level~$k$ identifies $k\,\Omega$ as the collision residue, consistent with
exec
/bin/zsh -lc "nl -ba standalone/preface_full_survey.tex | sed -n '436,440p'" in /Users/raeez/chiral-bar-cobar-vol2exec
/bin/zsh -lc "nl -ba chapters/connections/frontier_modular_holography_platonic.tex | sed -n '4729,4766p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
   692	$d\tau$-component has no genus-$0$ counterpart.
   693	
   694	\item \textup{(Elliptic $\to$ rational $r$-matrix.)}
   695	$r^{\mathrm{ell}}_\fg(z,\tau) \to \Omega/z$ through the intermediate
   696	trigonometric $r$-matrix:
   697	$r^{\mathrm{ell}} \to r^{\mathrm{trig}} \to r^{\mathrm{rat}}$,
   698	in the level-normalised convention where the
   699	$1/(k+h^\vee)$ prefactor is absorbed into the rescaled $\Omega$.
   700	
   701	\item \textup{(Elliptic $\to$ rational Gaudin.)}
   702	$H_i^{\mathrm{ell}} \to H_i^{\mathrm{Gaudin}} = \sum_{j \neq i}
   703	\Omega_{ij}/(z_i - z_j)$.
   704	\end{enumerate}
   705	\end{theorem}
   706	
   707	\begin{proof}
   708	As $q \to 0$, the Weierstrass functions have the standard
   709	degenerations. The zeta function:
   710	$\zeta_\tau(z) = \pi\cot(\pi z) + O(q)$, giving
   711	$1/z + O(z)$ for $|z| < 1$. The $\wp$-function:
exec
/bin/zsh -lc "nl -ba chapters/theory/introduction.tex.bak | sed -n '343,347p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix | sed -n '2910,2914p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | wc -l" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | wc -l" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n -P '(?<"'![A-Za-z0-9_])'"\\\\Omega(?:_[A-Za-z0-9{}\\\\]+)?\\s*/\\s*z\\b|\\\\frac\\{\\\\Omega(?:_["'^}]*)?'"\\}\\{z\\}' chapters standalone 2>/dev/null | wc -l" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 52ms:
   436	\[
   437	r(z) \;=\; \frac{k}{z}.
   438	\]
   439	(The formal Laplace transform of the full $\lambda$-bracket $\{J_\lambda J\}=k\lambda$ gives $\int_0^\infty e^{-\lambda z}k\lambda\,d\lambda = k/z^2$, which is the position-space OPE kernel; the collision residue is the simple-pole coefficient $k/z$ after the $d\log$ absorption, in the same way the Kac--Moody section below separates $\Omega/z$ from the $kK_\fg/z^2$ term.)
   440	The quantum $R$-matrix: $R(z) = \exp(k\hbar/z)$. Yang--Baxter
 succeeded in 51ms:
  4729	 \]
  4730	 The holographic R-matrix at level $k=1$ is
  4731	 $r(z) = k\Omega/z = \Omega/z$ (classical Yang--Baxter at
  4732	 $k=1$; the level-prefixed form $k\Omega/z$ vanishes at $k=0$; $\Omega$ the Casimir element), and the genus expansion
  4733	 $F_g = \kappa\cdot\lambda_g^{\mathrm{FP}}$ computes
  4734	 twisted $\mathcal{N} = 4$ amplitudes at genus~$g$.
  4735	 The anomaly matching condition
  4736	 $\kappa_{\mathrm{eff}}
  4737	 = \kappa(\mathrm{matter}) + \kappa(\mathrm{ghost}) = 0$
  4738	 is a consistency check.
  4739	
  4740	\item \emph{Sphere reconstruction.}
  4741	 The genus-$0$, $n$-point shadow amplitudes
  4742	 $\mathrm{Sh}_{0,n}(\Theta_\cA)$ are the Witten
  4743	 diagram amplitudes of the holomorphic twist. The
  4744	 commuting differentials of Gaiotto--Zinenko~\cite{GZ26}
  4745	 are the scalar shadow of $\mathrm{Sh}_{0,n}$.
  4746	\end{enumerate}
  4747	\end{theorem}
  4748	
 succeeded in 51ms:
   343	For Heisenberg, $r(z) = k\,\Omega/z$ with $\Omega$ the Casimir;
   344	the symmetrization recovers the scalar
   345	$\kappa(\cH_k) = k$, but the matrix structure of~$\Omega$ is
   346	discarded.  For affine Kac--Moody, $r(z) = \Omega/z$ contains the
   347	full Yangian double; the symmetrization recovers
 succeeded in 51ms:
  2910	\end{equation}
  2911	is a statement about three points $z_1, z_2, z_3$ on the curve.
  2912	For the rational $r$-matrix $r(z) = \Omega/z$
  2913	(where $\Omega \in \fg \otimes \fg$ is the Casimir tensor of an
  2914	affine Kac--Moody algebra), the three terms are respectively
 succeeded in 50ms:
     153
 succeeded in 51ms:
     155
 succeeded in 51ms:
       6


thinking
**Evaluating candidate extraction methods**

I'm considering how to compile a candidate list using a script, maybe opting for Perl or even simpler tools like `awk`. There's a thought about using `rg -n -P` with a specific regex pattern, but it seems like it can still catch unwanted substrings after `k\,`. I think I need to incorporate a negative lookbehind to effectively address patterns like `k\,` or `\hbar\,`, especially if there's optional punctuation or spaces involved. This requires some careful tweaking!
thinking
**Inspecting candidate list**

I’m considering the initial candidate list from a strict search, which may include numerators with subscripts. I need to inspect this more closely because I'm unsure if they’re at the affine level. It might be necessary to evaluate possible examples in a table or verify if they align with generic line-operator formulas. Since the user asked for a sweep across three volumes, I think I should include suspicious table cells in the inspection.
codex
I’ve ruled out the generic Yangian definitions. I’m checking the remaining table cells and example specializations, since those are the places convention drift often hides after a formula is fixed in prose.
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_preface_supplement.tex | sed -n '220,231p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_preface_supplement.tex | sed -n '341,347p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '724,734p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '828,834p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '1118,1125p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '1614,1619p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '1171,1178p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   220	\Bigl(
   221	\widehat{\mathfrak{sl}}_N{}_k,\;
   222	\widehat{\mathfrak{sl}}_N{}_{-k-2N},\;
   223	\mathcal O_q^{\mathrm{sh}},\;
   224	\frac{\Omega_N}{z},\;
   225	\Theta_k,\;
   226	\nabla^{\mathrm{KZ}}_k
   227	\Bigr),
   228	\]
   229	with $\Omega_N=\sum_a J^a\otimes J_a$ the Casimir,
   230	$q=e^{i\pi/(k+N)}$, $\kappa_k=(N^2-1)(k+N)/(2N)$. The collision $r$-matrix $r(z)=k\,\Omega_N/z$ satisfies
   231	the CYBE because $\Omega$ is ad-invariant and the triple Casimir
 succeeded in 51ms:
   341	\mathcal H(V_\Lambda)
   342	\;=\;
   343	\Bigl(
   344	V_\Lambda,\;V_{\Lambda^*}^{\mathrm{tw}},\;
   345	\cC_\Lambda,\;\frac{\Omega_\Lambda}{z},\;
   346	\Theta_\Lambda,\;\nabla^{\mathrm{hol}}_\Lambda
   347	\Bigr),
 succeeded in 51ms:
   724	The $r$-matrix is the classical Casimir $r$-matrix:
   725	\begin{equation}\label{eq:thqg-V-affine-r}
   726	r_{\widehat{\fg}_k}(z)
   727	\;=\;
   728	\frac{\Omega_\fg}{z}
   729	\;=\;
   730	\frac{1}{z}\,
   731	\sum_{a=1}^{\dim\fg}
   732	\frac{e_a \otimes e^a}{k + h^\vee},
   733	\end{equation}
   734	where $\{e_a\}$ is an orthonormal basis of $\fg$ with respect to the
 succeeded in 51ms:
   828	$\mathcal{H}^N_\kappa$ & $\Omega_{\mathcal{H}}/(\kappa z)$
   829	 & simple & none \\
   830	$\widehat{\fg}_k$ & $\Omega_\fg/((k{+}h^\vee)z)$
   831	 & simple & none \\
   832	$\beta\gamma$ & $\Omega_{\beta\gamma}/z$
   833	 & simple & quartic contact \\
   834	$\mathrm{Vir}_c$ & $r_{\mathrm{Vir}}(z)$
 succeeded in 52ms:
  1614	
  1615	\emph{Level~$0$ generators.}
  1616	$T_{\alpha\beta}^{(0)} := \langle e_\alpha,\,r_\cA(z)\,e_\beta\rangle
  1617	= \Omega_{\alpha\beta}/z$.
  1618	These are the $\fg$-currents at degree~$2$.
  1619	
 succeeded in 52ms:
  1118	\label{eq:thqg-V-cybe-term3}
  1119	\end{align}
  1120	where $r_{ij}(z) = \Omega_{ij}/z$ is the leading-order $r$-matrix.
  1121	(For algebras with higher-order poles in the $r$-matrix, such as
  1122	$\mathrm{Vir}_c$, additional terms appear at higher collision depth;
  1123	the leading-order CYBE is the universal statement valid for all
  1124	modular Koszul algebras.)
  1125	
 succeeded in 52ms:
  1171	
  1172	\begin{proof}
  1173	The CYBE~\eqref{eq:thqg-V-cybe} with
  1174	$r_{ij}(z) = \Omega_{ij}/z$ becomes
  1175	\[
  1176	\frac{[\Omega_{12},\Omega_{13}]}{z_{12}\,z_{13}}
  1177	+
  1178	\frac{[\Omega_{12},\Omega_{23}]}{z_{12}\,z_{23}}
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '724,740p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   724	The $r$-matrix is the classical Casimir $r$-matrix:
   725	\begin{equation}\label{eq:thqg-V-affine-r}
   726	r_{\widehat{\fg}_k}(z)
   727	\;=\;
   728	\frac{\Omega_\fg}{z}
   729	\;=\;
   730	\frac{1}{z}\,
   731	\sum_{a=1}^{\dim\fg}
   732	\frac{e_a \otimes e^a}{k + h^\vee},
   733	\end{equation}
   734	where $\{e_a\}$ is an orthonormal basis of $\fg$ with respect to the
   735	Killing form scaled by $1/(2h^\vee)$, and $\Omega_\fg$ is the
   736	quadratic Casimir.
   737	
   738	The normalization by $(k + h^\vee)^{-1}$ arises from the propagator:
   739	the bar-complex propagator is $\eta(z,w) = d\log(z - w)$ with the
   740	OPE coefficient $k\,(a,b)$ in the numerator, giving
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '738,748p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   738	The normalization by $(k + h^\vee)^{-1}$ arises from the propagator:
   739	the bar-complex propagator is $\eta(z,w) = d\log(z - w)$ with the
   740	OPE coefficient $k\,(a,b)$ in the numerator, giving
   741	$r_{ab}(z) = \delta_{ab}/(k + h^\vee)\,z$ after inverting the
   742	level-shifted Killing form.
   743	
   744	For $\fg = \mathfrak{sl}_2$:
   745	\begin{equation}\label{eq:thqg-V-sl2-r}
   746	r_{\widehat{\mathfrak{sl}}_2}(z)
   747	\;=\;
   748	\frac{1}{(k+2)\,z}\,
exec
/bin/zsh -lc "nl -ba chapters/connections/thqg_gravitational_yangian.tex | sed -n '724,742p'" in /Users/raeez/chiral-bar-cobar-vol2 succeeded in 51ms:
   724	f^{ab}_{\phantom{ab}c}\,J^c(z),
   725	\end{equation}
   726	the Lie bracket of the underlying finite-dimensional algebra~$\fg$.
   727	The $r$-matrix is the classical Casimir $r$-matrix:
   728	\begin{equation}% label removed: eq:thqg-V-affine-r
   729	r_{\widehat{\fg}_k}(z)
   730	\;=\;
   731	\frac{\Omega_\fg}{z}
   732	\;=\;
   733	\frac{1}{z}\,
   734	\sum_{a=1}^{\dim\fg}
   735	\frac{e_a \otimes e^a}{k + h^\vee},
   736	\end{equation}
   737	where $\{e_a\}$ is an orthonormal basis of $\fg$ with respect to the
   738	Killing form scaled by $1/(2h^\vee)$, and $\Omega_\fg$ is the
   739	quadratic Casimir.
   740	
   741	The normalization by $(k + h^\vee)^{-1}$ arises from the propagator:
   742	the bar-complex propagator is $\eta(z,w) = d\log(z - w)$ with the

thinking
**Organizing data by severity**

I'm noticing that I need to categorize the information by severity. It might help to group duplicates under each severity level. Plus, I should determine the exact number of instances I checked and the violations I found. I could set something like "Instances checked: 20" to indicate that 20 suspicious contexts were evaluated. It's also a good idea to count how many candidate contexts I actually inspected.
codex
Volume III hasn’t produced a genuine bare `\Omega/z` surface so far, but I’m doing one last direct read of the small candidate set there before I close the audit.
exec
/bin/zsh -lc "nl -ba chapters/theory/braided_factorization.tex | sed -n '521,526p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '5990,5995p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/examples/toroidal_elliptic.tex | sed -n '2756,2761p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/connections/geometric_langlands.tex | sed -n '36,40p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/quantum_chiral_algebras.tex | sed -n '149,153p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "nl -ba chapters/theory/e1_chiral_algebras.tex | sed -n '86,90p'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
  2756	$A = A_E$ ($c = 24$, $\kappa_{\mathrm{ch}} = 24$),
  2757	$A^! = A_E^!$ ($\kappa_{\mathrm{ch}} = -24$),
  2758	$C = Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ (universal bulk),
  2759	$r(z) = \kappa_{\mathrm{ch}}\,\Omega/z$ (Casimir, $24$-dim: level prefix $\kappa_{\mathrm{ch}} = 24$),
  2760	$\Theta_A$ (bar-intrinsic MC element),
  2761	$\nabla^{\mathrm{hol}}$ (shadow connection, class~G).
 succeeded in 51ms:
   521	For a K3 surface $S$ with $\cC = D^b(\Coh(S))$, the
   522	$\Etwo$-chiral algebra has $\kappa_{\mathrm{cat}} = 2$. The
   523	$R$-matrix is the Casimir
   524	$\cR(z) = 1 + \kappa_{\mathrm{cat}}\,\Omega/z + O(z^{-2})$,
   525	where $\Omega$ is the Mukai pairing on $H^*(S, \Z)$. The braided
   526	bar cohomology $H^*(B_{E_2}(\Phi(\cC)))$ recovers the lattice
 succeeded in 51ms:
  5990	\section{The elliptic Sklyanin bracket and the three-parameter $\hbar$}
  5991	\label{sec:elliptic-sklyanin-three-param}
  5992	
  5993	The rational $r$-matrix $r(z) = k\,\Omega/z$ and the trigonometric
  5994	$r$-matrix $r(z) = k\,\Omega \cdot \cot(z)$ both admit a single
  5995	deformation parameter $\hbar = 1/(k + h^\vee)$. The elliptic
 succeeded in 50ms:
    36	Feigin--Frenkel is a statement about the chiral center $\mathfrak{z}(\hat{\frakg}) \subset V_{-h^\vee}(\frakg)$. The relevant legs of the four-functor picture are the derived center of item~(d), and the Verdier leg of item~(b). It is not an instance of inversion (item~(c)). In particular one should not describe Feigin--Frenkel as ``bar followed by cobar produces the spectral side.'' For $A = V_{-h^\vee}(\frakg)$, the bar complex $B(A)$ carries the deconcatenation coproduct of $T^c(s^{-1}\bar{A})$ (Volume~I); the Verdier-dual complex is the habitat in which $\mathrm{Fun}(\mathrm{Op}_{G^L})$ should be located.
    37	
    38	At the critical level $\kappa_{\mathrm{ch}}(V_{-h^\vee}(\frakg)) = \dim(\frakg) \cdot (k + h^\vee) / (2 h^\vee) = 0$. (level-stripped $r$-matrix), the classical $r$-matrix of $V_k(\frakg)$ is $r(z) = k\,\Omega/z$, so at $k = -h^\vee$ the surviving structure is \emph{not} the collision $r$-matrix but the chiral-bar-level obstruction encoded by $\Theta_A$.
    39	
    40	\begin{conjecture}[Critical-level Verdier-intertwining; \ClaimStatusConjectured]
 succeeded in 50ms:
   149	\end{center}
   150	Equivalently: $K_{A_\cC}(z) = 1$ iff the boundary coproduct is primitive iff $d_{\mathrm{alg}} = 0$ iff $\cC$ is class $\mathbf{G}$. The correspondence $K_{A_\cC}(z) = 1 \Longleftrightarrow \mathbf{G} \Longleftrightarrow d_{\mathrm{alg}} = 0$ is the CY analogue of the Vol~II biconditional.
   151	
   152	The $K$-matrix modifies the coproduct, not the product, so the $r$-matrix vanishing check does not apply directly to $K_{A_\cC}(z)$. The corresponding $r$-matrix check is the affine one: the classical $r$-matrix $k_{\mathrm{ch}}\,\Omega/z$ vanishes at $k_{\mathrm{ch}} = 0$, in which case $A_\cC$ collapses to the trivial Heisenberg and $K_{A_\cC}(z) = 1$, consistent with class $\mathbf{G}$.
   153	\end{remark}
 succeeded in 50ms:
    86	\[
    87	 r(z) = \frac{k\,\Omega}{z},
    88	\]
    89	not the level-stripped $\frac{\Omega}{z}$. The level survives the $d\log$ absorption because the ordered bar complex builds in one factor of the level per collision. At $k=0$ the $r$-matrix vanishes identically. The collision residue of the Heisenberg $r$-matrix is $k$, not $k/2$, and the monodromy of the $E_1$ representation category around a puncture is $\exp(-2\pi i k)$.
    90	\end{remark}





thinking
**Considering reporting discrepancies**

I’m weighing whether we should report findings. I’m thinking we might label something as MEDIUM severity and inspect rosetta_stone 2795 in vol2, as it could be similar to frontier. Including one example might lead to others, but there’s a chance it might not be worth reporting if it's just conventional. The user wants sweep AP126, so maybe I should mention lower severity examples while keeping it concise without overwhelming and maintaining clarity. Each bullet might summarize findings by severity.
thinking
**Deciding bullet format**

I'm considering using the `file:line` format with multiple line references separated by commas in the same bullet point. However, I remember the user asked for each hit specifically, so it might be safer to keep them in separate bullets. But then I worry about having too many bullets, which could make things overwhelming. It's a bit of a balancing act, deciding how to present the information clearly without cluttering the response. I’ll have to find the best approach.
thinking
**Considering combining findings**

I’m thinking about whether to combine related sections, specifically preface_sections5_9_draft:542 and 581-582, since they’re from the same table. The user asked about each hit individually, though, which makes me hesitate to merge them. Hmm, I also notice there are three instances of violating texts. It might be worth keeping them separate to fully address what the user wants, despite the overlap. I’ll need to weigh the pros and cons carefully!
thinking
**Evaluating text verification**

I need to check if `rosetta_stone 2795` is genuine. If I include it, the count goes to 17, and if I exclude it, it's 16. I might also consider counting `thqg_preface_supplement 345`, but it seems like a false positive, so I’ll probably exclude that. I should report the exact violation from `standalone/preface_full_survey.tex:507`. I could also note the absence of `Vol III` in the summary. It could look like this: `Instances checked: 31 | Violations found: 17 | Verdict: FAIL`.
thinking
**Finalizing report format**

I'm checking the instances and, well, I noted that 31 were checked, with a fail outcome. I should probably mention that "Vol III candidate set produced 0 genuine violations." Perhaps I could put that in the false positives section or the summary? Also, ensuring there are no nested bullets seems crucial; I think just listing bullet points would be cleaner. I’ll use markdown without a heading until the summary, and I’m focused on making the final output concise but still thorough enough.
codex
- [CRITICAL] Vol II `standalone/preface_full_survey.tex:507` — exact text `\frac{\Omega}{z} + \frac{k\,K_{\fg}}{z^2}`. This strips the level from the simple-pole term, then the same block immediately says the collision residue is `r(z)=k\,\Omega/z` at line 513.
- [CRITICAL] Vol II `chapters/connections/log_ht_monodromy_core.tex:1905` — exact text `= \frac{\Omega}{z} + \frac{k\,\kappa_\fg}{z^2}`. The same paragraph then says the braiding is governed by `r(z)=k\,\Omega/z` at line 1914.
- [CRITICAL] Vol I `chapters/connections/thqg_gravitational_yangian.tex:728` — exact text `\frac{\Omega_\fg}{z}`. The displayed equality immediately rewrites the same term as `\sum (e_a\otimes e^a)/(k+h^\vee)z` at line 732, so the first term is level-stripped.
- [CRITICAL] Vol II `chapters/connections/thqg_gravitational_yangian.tex:731` — same defect as Vol I: exact text `\frac{\Omega_\fg}{z}` while the next line carries the hidden `1/(k+h^\vee)` normalization.
- [CRITICAL] Vol I `chapters/examples/yangians_foundations.tex:1059` — exact text `r(z) = \Omega_{\mathrm{tr}}/z.` after defining `\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)` at line 1058. This conflicts with the canonical bridge `k\,\Omega_{\mathrm{tr}} = \Omega/((k+h^\vee)z)`.

- [HIGH] Vol I `chapters/frame/preface_section1_v2.tex:481` — exact text `r(z) \;=\; \frac{\Omega}{z}` in a Kac-Moody overview; the same block averages `k\Omega/z`, so the surface is internally inconsistent.
- [HIGH] Vol I `chapters/frame/preface_section1_draft.tex:634` — same bare formula `r(z) \;=\; \frac{\Omega}{z}` on the same affine surface.
- [HIGH] Vol I `chapters/frame/preface_sections5_9_draft.tex:542,581,582` — table cells use bare `\Omega/z` for `\widehat{\fg}_k`, plus `\mathrm{av}(\Omega/z)` and `\Omega/z` for `Y(\fg)`.
- [HIGH] Vol I `chapters/connections/thqg_preface_supplement.tex:224` — tuple slot records `\frac{\Omega_N}{z}` while line 230 in the same block states the collision `r`-matrix is `r(z)=k\,\Omega_N/z`.
- [HIGH] Vol I `chapters/connections/holographic_datum_master.tex:466` — exact text `\frac{\Omega}{z}` in `r^{\mathrm{Dr}}(z)`. The same chapter elsewhere uses level-explicit normalizations, so this is an unqualified bare surface.
- [HIGH] Vol I `chapters/connections/holographic_datum_master.tex:717` — the master diagram repeats the same bare entry as `\frac{\Omega}{z}\;\textrm{(Drinfeld85)}`.

- [MEDIUM] Vol I `chapters/connections/frontier_modular_holography_platonic.tex:4731,4764` — prose specializes `r(z)=k\Omega/z` to `\Omega/z` at `k=1`. Numerically true at fixed level, but it violates the repo’s no-level-stripping convention on display.
- [MEDIUM] Vol II `chapters/examples/rosetta_stone.tex:2795` — same specialization drift: `at level~k=1 the collision residue is \Omega_{\mathfrak{sl}_3}/z`.

- [LOW] Vol I `chapters/theory/introduction.tex.bak:346` — stale backup still contains `r(z) = \Omega/z`.
- [LOW] Vol I `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:2912` — stale backup still contains `r(z) = \Omega/z`.

False positives removed: explicit KZ forms `\Omega/((k+h^\vee)z)`, absorbed-normalization sites such as `standalone/genus1_seven_faces.tex:695,724`, and generic Yangian definitions where the residue tensor itself is the datum rather than an affine level-stripped KM formula. No genuine Vol III hit survived context review.

## Summary
Instances checked: 31 | Violations found: 17 | Verdict: FAIL
tokens used
162,080
