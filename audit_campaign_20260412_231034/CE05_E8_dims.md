# CE05_E8_dims (493s, gpt-5.4)

[CRITICAL] [compute/tests/test_lqt_e1_growth.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_lqt_e1_growth.py:73) — The file contains an active false oracle: the docstring says `h^vee(C_2)=3`, the assertion enforces `dual_coxeter_number("C2") == 4`, and the next test immediately admits the formula is wrong and then does `pass` at lines 77-84. The implementation it exercises, [compute/lib/lqt_e1_growth.py](/Users/raeez/chiral-bar-cobar/compute/lib/lqt_e1_growth.py:71), hardcodes `max(exponents)+1`, so the engine and test are synchronized to the same wrong value. Internal repo cross-checks also say `C_2` has `h^vee=3` (for example [chapters/examples/kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1535) and [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1361)).

[HIGH] [compute/tests/test_bc_exceptional_categorical_zeta_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_exceptional_categorical_zeta_engine.py:22) — The file advertises “multi-path verification,” but it imports private oracle tables `_KNOWN_FUND_DIMS`, `_KNOWN_SMALL_DIMS_G2`, `_KNOWN_SMALL_DIMS_F4`, and `_EXCEPTIONAL_DATA` from the engine under test, then uses them as expected data at lines 159-168 and 843-862. It also hardcodes E8 values like `248`, `3875`, `27000`, and `30380` at lines 578-630 with no inline provenance. `rg` found zero `# VERIFIED` markers in the file, so this fails the repo’s AP10 requirement and is AP128-style circular on part of the exceptional surface.

[MEDIUM] [compute/tests/test_yangian_rtt_exceptional.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rtt_exceptional.py:216) — `V(omega_8)=248` is hardcoded with no inline two-source trail, and the batch check at lines 223-230 delegates to `verify_fundamental_dims()` inside [compute/lib/yangian_rtt_exceptional.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rtt_exceptional.py:906), where the expected `248` is embedded in the same implementation surface. `rg` found no `# VERIFIED` markers anywhere in this test file, so AP10 is not met and the “accessible” batch is not an independent oracle.

[MEDIUM] [compute/tests/test_e8_lattice.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_e8_lattice.py:1) — The file gives only a single file-level citation to `detailed_computations.tex`, but hardcodes many load-bearing expected values (`248`, `240`, `64`, `57600`, `61504`, `15600`, `496`) at lines 33-146. There are no `# VERIFIED` markers in the file, so it does not satisfy the repo’s stated AP10 rule requiring 2+ independent sources for hardcoded expected values.

`adjoint = 248` itself is verified, not falsified. Independent checks I ran gave `248` via `dimension("E8")`, the exponent-sum formula `rank + 2*sum(exponents)`, the root-count formula `rank + 2|Phi^+|`, `ExceptionalRootSystem("E8").dim_algebra`, and `weyl_dim_explicit("E8", (0,0,0,0,0,0,0,1))`. Focused E8 tests passed: `4 passed in 3.36s`.

The exact broad run `python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30` was started, but it did not finish during the audit window. A matching `--collect-only` run found `3125/123985 tests collected (120860 deselected)` in `58.38s`, so the selected surface is large.

## Summary
Instances checked: 6 | Violations found: 4 | Verdict: FAIL


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
session id: 019d83bd-599e-7322-94af-a705c2060b3e
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


Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30. Check: adjoint=248?

Also check: are hardcoded expected values in test files cited with 2+ independent sources (AP10/AP128)? Read the test file and verify.
mcp startup: no servers

thinking
**Planning tool usage**

I need to consider using a minimal set covering request. First, I’ll do a commentary update and then look at the skill files. I wonder if I should use multi_tool_use.parallel for parallel reads, focusing only on developer tools. I might execute commands in parallel or spawn an agent, but commentary comes first. I think I need to use `update_plan` to give a substantial plan, but I could also do a smaller one if necessary.
codex
Using `deep-beilinson-audit` for the falsification pass and `build-surface` for the targeted pytest check. I’ll read the relevant skill instructions, run the requested test surface, then inspect the exact test files and their source citations for the hardcoded exceptional values.
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

exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 122ms:
---
name: build-surface
description: Use when LaTeX builds, build logs, warning classification, metadata regeneration, or targeted pytest runs determine whether a change is actually verified. This is the Codex-native equivalent of `/build` from `CLAUDE.md`.
---

# Build Surface

Build output is evidence only after the surface is stable enough to trust.

## Standard prelude

```bash
pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
```

Then choose the narrowest command that can falsify the change:

- `make fast`
- `make`
codex
I’ve loaded the audit and build workflows. Next I’m fixing the audit surface: which `compute/tests` files cover `E8` or `exceptional`, where `248` is asserted, and whether those assertions carry the required independent-source citations.
exec
/bin/zsh -lc 'rg -n "E8|exceptional|248|AP10|AP128|VERIFIED|independent source|source" compute/tests CLAUDE.md chapters/connections/concordance.tex metadata/theorem_registry.md archive/raeeznotes/raeeznotes100/red_team_summary.md' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobar succeeded in 347ms:
CLAUDE.md:21:**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).
CLAUDE.md:39:source:               landscape_census.tex line [N] OR compute engine
CLAUDE.md:109:### HZ-6. AP10/AP128 (hardcoded expected values) -- 3 waves, 12+ engines
CLAUDE.md:111:Every hardcoded expected value in a test file requires a `# VERIFIED` comment citing at least TWO sources from different categories:
CLAUDE.md:120:Engine-test sync check: when correcting an engine formula, derive the new expected value from an INDEPENDENT source, NOT from the corrected engine output. Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.
CLAUDE.md:191:"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).
CLAUDE.md:193:**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.
CLAUDE.md:219:Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).
CLAUDE.md:251:**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.
CLAUDE.md:402:**FM2. Level-prefix dropping on summarisation.** When Opus summarises a displayed formula from an earlier file read, it omits scalar prefactors even if the source had them. Lost prefixes: k, c/2, kappa, 1/(2*pi*i). Counter: re-Read the source lines verbatim before typing; do not rely on context cache.
CLAUDE.md:440:**FM21. Dimensional analysis reconstruction with wrong prefactor.** Opus gets powers right but numerical prefactors (1/2, 1/24, 1/(2*pi*i), 7/5760) wrong. Counter: for any numerical coefficient in {F_g, lambda_g, Bernoulli numbers, Faber-Pandharipande values}, Read the canonical source file in compute/lib/ before writing.
CLAUDE.md:521:**computation discipline** (AP3, AP10, AP61): Compute independently. NEVER pattern-match across occurrences. Cross-family consistency checks are real verification; single-family hardcoded tests insufficient. Verify against OPE table, landscape_census.tex, cross-engine comparison. **AP10 strengthened**: every hardcoded expected value MUST have a comment citing 2+ independent derivation paths. For combinatorial counts, cite generating function or recursion. Bare numbers with no derivation trail are future AP10 violations.
CLAUDE.md:541:**operadic** (AP65, AP81, AP82, AP83, AP84, AP85, AP88, AP103, AP104): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebra structures: Lie^c (Harrison, coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered configs); R-matrix descent relates. B_{Com}(A) is coLie, NOT cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.
CLAUDE.md:545:**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.
CLAUDE.md:549:AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
CLAUDE.md:550:AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
CLAUDE.md:551:AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
CLAUDE.md:552:AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
CLAUDE.md:554:AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
CLAUDE.md:559:AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.

thinking
**Polling test session**

I see the output got truncated. I need to focus on specific lines from CLAUDE-related tests AP10 and E8. The pytest command might have timed out, so I should look into that. It seems I might need to identify the target tests using the command with '-k' for E8 or exceptional cases. I could also consider running a collection list. Polling the session might be the next step to gather more information!
codex
The repository-wide grep confirmed the governance rule I need to test against: `CLAUDE.md` explicitly requires `# VERIFIED` comments with two independent source categories for hardcoded expected values, and it separately records `E8` adjoint `= 248` as canonical. I’m now classifying the actual `pytest -k 'E8 or exceptional'` surface and then reading the specific test files where those values are asserted.

thinking
**Assessing output issues**

Hmm, still no output? I’m wondering if it’s hung or if the command is taking longer than expected. Maybe the tail is waiting for pipe output? It’s worth checking if the session is still running since pytest can take some time. I'll have to be patient and consider waiting a bit longer to see if anything comes through.
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobar
thinking
**Considering test management**

I’m working through whether the tests might hang for over 30 seconds. Maybe using the timeout command would help, like `timeout 120 python3 -m pytest... | tail -30`. Although, if the process is already running in the background, I might not need to worry or kill it. Still, listing collected file names with `pytest --collect-only` might clarify if there are too many tests. Since the user asked to run the command, I should let it finish and check relevant test files simultaneously.
exec
/bin/zsh -lc "sed -n '105,125p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '245,255p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -l "E8|exceptional" compute/tests' in /Users/raeez/chiral-bar-cobar succeeded in 104ms:
```

Downgrade atomicity: when downgrading theorem -> conjecture, rename `thm:foo -> conj:foo` AND update every `\ref{thm:foo}` across three volumes in the SAME tool-call batch. No intermediate commit.

### HZ-6. AP10/AP128 (hardcoded expected values) -- 3 waves, 12+ engines

Every hardcoded expected value in a test file requires a `# VERIFIED` comment citing at least TWO sources from different categories:

```
[DC] direct computation     [LT] literature (paper + eq #)
[LC] limiting case          [SY] symmetry
[CF] cross-family           [NE] numerical (>=10 digits)
[DA] dimensional analysis
```

Engine-test sync check: when correcting an engine formula, derive the new expected value from an INDEPENDENT source, NOT from the corrected engine output. Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### HZ-7. AP113 (bare kappa in Vol III) -- 3 waves, 165 baseline instances

Bare `\kappa` in Vol III is permitted IFF the section begins with a local definition:
 succeeded in 79ms:
**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).

**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).

**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).

**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).

**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).
 succeeded in 145ms:
compute/tests/test_lattice_prime_locality.py
compute/tests/test_shadow_period_integral_engine.py
compute/tests/test_e8_genus2_hecke.py
compute/tests/test_discriminant_atlas_complete.py
compute/tests/test_cy_mckay_quiver_engine.py
compute/tests/test_cy_gepner_k3_engine.py
compute/tests/test_arithmetic_packet_connection.py
compute/tests/test_bar_tqft_state_sum_engine.py
compute/tests/test_conformal_bootstrap_shadow.py
compute/tests/test_depth_separation_complete.py
compute/tests/test_cy_cech_descent_engine.py
compute/tests/test_arithmetic_shadow_connection.py
compute/tests/test_exceptional_shadow_engine.py
compute/tests/test_gap_closure.py
compute/tests/test_genus2_landscape.py
compute/tests/test_leech_chi12_projection.py
compute/tests/test_bar_cohomology_lattice_explicit_engine.py
compute/tests/test_modular_spectral_rigidity.py
compute/tests/test_chirhoch_dimension_engine.py
compute/tests/test_mc3_red_team.py

thinking
**Inspecting tests and engines**

I’m considering how to inspect the collect-only tests and identify any E8-specific ones. The user mentioned checking `adjoint=248`, which likely points to the `bc_exceptional_categorical_zeta_engine`. I need to look into that test file and the related engine. So, I’ll search for `adjoint` and `248` within the compute/tests. I'll also focus on the specific test file and engine constants, maybe using targeted searches with `rg`.
codex
The raw `-k` surface is much broader than one engine; there are many `E8`/`exceptional` matches across `compute/tests`. I’m narrowing to the tests that actually assert `248` or the exceptional Lie dimensions, because that is the falsifiable claim the user asked me to verify against the source and the AP10 citation rule.
exec
/bin/zsh -lc "rg -n \"adjoint|248|FUNDAMENTAL_DIMS\\['E8'\\]|dimension\\(\\\"E8\\\"\\)|dim\\(E8\\)|E_8 fundamental\" compute/tests compute/lib" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "pytest --collect-only -q compute/tests/ -k 'E8 or exceptional' 2>&1 | tail -40" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
Total output lines: 2162

compute/lib/theorem_hca_pillar_a_engine.py:20:    - B_kappa adjoint Omega_kappa is Quillen equivalence (thm:quillen-equivalence-chiral)
compute/lib/theorem_hca_pillar_a_engine.py:744:            "quillen_pair": "B_kappa left adjoint, Omega_kappa right adjoint",
compute/lib/theorem_hca_pillar_a_engine.py:1047:    - Quillen equivalence B_kappa adjoint Omega_kappa
compute/lib/euler_product_from_mc.py:919:        'E8': {2: 124.0 / 31},   # kappa(E_8) = 248*1/(2*30) * (1+30) = ...
compute/lib/mv_positivity_sl3.py:556:def adjoint_tensor_character(n: int) -> Dict[Tuple[int, int], int]:
compute/lib/mv_positivity_sl3.py:557:    """Character of the adjoint representation g^{⊗n} for sl₃.
compute/lib/mv_positivity_sl3.py:559:    The adjoint of sl₃ is V(1,1) (dimension 8).
compute/lib/mv_positivity_sl3.py:575:def adjoint_tensor_decomp(n: int) -> Dict[Tuple[int, int], int]:
compute/lib/mv_positivity_sl3.py:580:    char = adjoint_tensor_character(n)
compute/lib/mv_positivity_sl3.py:653:def verify_adjoint_decomp_positivity(max_n: int = 4) -> Dict[str, object]:
compute/lib/mv_positivity_sl3.py:654:    """Verify adjoint tensor power decompositions have positive coefficients.
compute/lib/mv_positivity_sl3.py:661:        decomp = adjoint_tensor_decomp(n)
compute/lib/mv_positivity_sl3.py:744:    adj_result = verify_adjoint_decomp_positivity(max_tensor_power)
compute/lib/mv_positivity_sl3.py:745:    results["adjoint_decomp"] = adj_result
compute/lib/mv_positivity_sl3.py:773:    # 6. MV cone check for adjoint tensor characters
compute/lib/mv_positivity_sl3.py:777:        adj_char = adjoint_tensor_character(n)
compute/lib/mv_positivity_sl3.py:797:        if n in results['adjoint_decomp']:
compute/lib/mv_positivity_sl3.py:798:            d = results['adjoint_decomp'][n]

thinking
**Investigating test files**

I’m noticing that Pytest is running in collect-only mode, which might be significant. I need to check specific test files like `test_yangian_rtt_exceptional.py`, `test_lqt_e1_growth.py`, and `test_bc_exceptional_categorical_zeta_engine.py`. The user asked me to verify a test file, so I need to identify which one is relevant. I'll focus on the files related to the adjoint=248, particularly the ones that test exceptional replications and E8. I think I need to use a tool for line numbers and context.
exec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,140p' compute/tests/test_lqt_e1_growth.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,320p' compute/tests/test_yangian_rtt_exceptional.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
r"""Tests for BC-82: Categorical zeta functions for exceptional Lie types.

Multi-path verification of dimensions, zeta values, Casimir eigenvalues,
and structural properties of the categorical zeta for G₂, F₄, E₆, E₇, E₈.

Verification paths used:
    Path 1: Weyl dimension formula from positive coroots (direct)
    Path 2: Closed-form G₂ dimension formula (independent)
    Path 3: Known fundamental representation dimensions (literature tables)
    Path 4: Langlands self-duality (all exceptional types are self-dual)
    Path 5: Casimir eigenvalue C₂(adj) = 2·h^∨ (independent invariant)
    Path 6: Dimension count asymptotics N(D) ~ D^{rank/|Φ⁺|}
    Path 7: Cross-check with bc_categorical_zeta_engine (classical types)
    Path 8: Root count |Φ⁺| = (dim g - rank) / 2
"""

import math
from fractions import Fraction

import pytest
 succeeded in 53ms:
"""Tests for LQT E₁ growth computation.

Verifies:
  - LQT generator degrees and counts
  - E₁ dimensions against manuscript tables
  - Sub-exponential growth rate for all simple types
  - Growth constant π√(r/12) convergence
  - Departure points between algebras
"""

import math
import pytest

from compute.lib.lqt_e1_growth import (
    EXPONENTS,
    rank,
    exponents,
    dimension,
    dual_coxeter_number,
    lqt_generator_degrees,
 succeeded in 71ms:
"""Tests for the exceptional type RTT scaffold.

Verifies root system data, representation dimensions, Yang-Baxter equation,
and prefundamental CG decomposition for exceptional Dynkin types G_2, E_6,
E_7, E_8 (and root system for F_4).

MC3 difficulty grades:
  G_2: grade C- (rank 2, 7-dim fundamental, fully accessible)
  E_6: grade B (27-dim fundamental, Weyl dim works, Freudenthal slow)
  E_7: grade C+ (56-dim fundamental)
  E_8: grade D (248-dim = adjoint, extreme)
  F_4: grade D (non-simply-laced, representation theory deferred)

References:
  - Humphreys, "Introduction to Lie Algebras and Representation Theory"
  - concordance.tex, conj:mc3-arbitrary-type
"""

import unittest


thinking
**Inspecting for citations**

I think I need to look into adding more lines for citations in the lqt section. It seems like they aren't there right now. I should inspect the test_bc_exceptional file, particularly near relevant tests and comments. Also, I might want to check out any test files with explicit `# VERIFIED` comments or see if there are any that are missing them. A search within those files for “VERIFIED” could be useful.
exec
/bin/zsh -lc "sed -n '260,520p' compute/tests/test_bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "VERIFIED|248|adjoint|Path 3|sources" compute/tests/test_yangian_rtt_exceptional.py compute/tests/test_bc_exceptional_categorical_zeta_engine.py compute/tests/test_lqt_e1_growth.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_yangian_rtt_exceptional.py:11:  E_8: grade D (248-dim = adjoint, extreme)
compute/tests/test_yangian_rtt_exceptional.py:132:        self.assertEqual(self.rs.dim_algebra, 248)
compute/tests/test_yangian_rtt_exceptional.py:164:    def test_adjoint_14(self):
compute/tests/test_yangian_rtt_exceptional.py:165:        """V(omega_2) = 14 (adjoint) for G_2."""
compute/tests/test_yangian_rtt_exceptional.py:197:        """V(omega_2) = 78 (adjoint)."""
compute/tests/test_yangian_rtt_exceptional.py:209:        """V(omega_1) = 133 (adjoint)."""
compute/tests/test_yangian_rtt_exceptional.py:216:    def test_omega8_is_248(self):
compute/tests/test_yangian_rtt_exceptional.py:217:        """V(omega_8) = 248 (adjoint = minimal)."""
compute/tests/test_yangian_rtt_exceptional.py:219:            weyl_dim_explicit("E8", (0, 0, 0, 0, 0, 0, 0, 1)), 248
compute/tests/test_yangian_rtt_exceptional.py:286:        """14-dim (G_2 adjoint)."""
compute/tests/test_lqt_e1_growth.py:65:        assert dimension("E8") == 248
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:9:    Path 3: Known fundamental representation dimensions (literature tables)
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:136:        """Path 3: Cartan matrix has 2s on diagonal."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:143:        """Path 3: off-diagonal entries of Cartan matrix are ≤ 0."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:160:        """Path 3: fundamental rep dimensions match literature tables."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:179:        """Path 3: G₂ small representation dimensions from literature."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:207:        """Path 3: F₄ fundamental dimensions are {26, 52, 273, 1274}."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:214:    def test_E6_adjoint_dim_78(self):
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:215:        """Path 3: E₆ adjoint representation has dim 78."""
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:227:        """Path 3: E₇ has a fundamental representation of dim 56."""
 succeeded in 52ms:
        for hw in dominant_weights(typ, 5):
            d = weyl_dimension(typ, hw)
            assert d > 0

    def test_G2_dim_77_multiplicity_2(self):
        """Path 3: G₂ has two irreps of dimension 77: V(3,0) and V(0,2)."""
        d1 = weyl_dimension('G2', (3, 0))
        d2 = weyl_dimension('G2', (0, 2))
        assert d1 == d2 == 77

    def test_E6_pair_27_conjugate(self):
        """Path 3: E₆ has two conjugate 27-dimensional representations."""
        rank = 6
        dims_27 = []
        for i in range(rank):
            hw = tuple(1 if j == i else 0 for j in range(rank))
            d = weyl_dimension('E6', hw)
            if d == 27:
                dims_27.append(i)
        assert len(dims_27) == 2  # Two fundamental reps of dim 27
exec
/bin/zsh -lc "sed -n '520,920p' compute/tests/test_bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '120,220p' compute/lib/bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/lib/yangian_rtt_exceptional.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
    def test_zeta_includes_trivial_larger(self, typ):
        """Path 1: including trivial rep increases zeta by 1."""
        z_no_triv = categorical_zeta(typ, 2.0, max_total_weight=5,
                                      include_trivial=False).real
        z_with_triv = categorical_zeta(typ, 2.0, max_total_weight=5,
                                        include_trivial=True).real
        assert abs(z_with_triv - z_no_triv - 1.0) < 1e-10

    def test_zeta_monotone_truncation(self):
        """Path 1: increasing max_total_weight increases zeta (all terms positive)."""
        z5 = categorical_zeta('G2', 2.0, max_total_weight=5).real
        z10 = categorical_zeta('G2', 2.0, max_total_weight=10).real
        z15 = categorical_zeta('G2', 2.0, max_total_weight=15).real
        assert z5 <= z10 <= z15

    @pytest.mark.parametrize("typ", ['G2', 'F4'])
    def test_zeta_real_for_real_s(self, typ):
        """Path 1: ζ(s) is real for real s > σ_c."""
        z = categorical_zeta(typ, 3.0, max_total_weight=8)
 succeeded in 51ms:
    'E8': {'rank': 8, 'n_pos_roots': 120, 'dim_g': 248, 'h_dual': 30},
}

# Known fundamental representation dimensions (sorted by dimension).
# These serve as verification data, independent of our computation.
_KNOWN_FUND_DIMS: Dict[str, List[int]] = {
    'G2': [7, 14],
    'F4': [26, 52, 273, 1274],
    'E6': [27, 27, 78, 351, 351, 2925],
    'E7': [56, 133, 912, 1539, 8645, 27664, 365750],
    'E8': [248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264],
}

# Known small representation dimensions for verification
# (dim, (hw_label) in some standard convention)
_KNOWN_SMALL_DIMS_G2 = [7, 14, 27, 64, 77, 77, 182, 189, 189, 273, 286, 378,
                         448, 714, 729, 748, 896, 924, 1254, 1547, 1728, 1729]
_KNOWN_SMALL_DIMS_F4 = [26, 52, 273, 324, 1053, 1053, 1274, 2652, 4096, 8424,
                         10829, 12376, 16302, 17901, 19278, 19448, 29172]

 succeeded in 52ms:
"""Exceptional type RTT scaffold: R-matrix and character infrastructure.

FRONTIER COMPUTATION for MC3 extension to exceptional Dynkin types
(conj:mc3-arbitrary-type). This module provides:

  1. Root systems and Cartan matrices for ALL exceptional types (G_2, F_4, E_6, E_7, E_8)
  2. Weyl dimension formulas and weight multiplicities via Freudenthal
  3. Character-level prefundamental CG verification
  4. R-matrix structure and Yang-Baxter verification for the standard
     R-matrix R(u) = I - P/u + Q/(u - kappa) with trace-projection Q

MC3 DIFFICULTY GRADES:
  D: grade B (orthogonal RTT, see yangian_rtt_typeD.py)
  G_2: grade C- (7-dim fundamental, rank 2, accessible)
  E_6: grade B (27-dim fundamental, large but structured)
  E_7: grade C+ (56-dim fundamental, very large)
  F_4: grade D (26-dim fundamental, non-simply-laced complications)
  E_8: grade D (248-dim = adjoint is smallest, extreme size)

ROOT SYSTEM CONVENTIONS:

thinking
**Evaluating code for dimensions**

I think I need to look more closely at `yangian_rtt_exceptional.py`, especially regarding `FUNDAMENTAL_DIMS` to verify its contents. It seems like I have enough information for now, but I might also want to inspect `compute/lib/lqt_e1_growth.py` for dimension data, particularly focusing on the exponents. This approach should help clarify any uncertainties I have about the dimensional aspects of my work.
exec
/bin/zsh -lc "sed -n '1,180p' compute/lib/lqt_e1_growth.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""LQT-based E₁ growth computation for Strategy IV spectral sequence.

Computes dim E_1^{0,p}(g[t]) via the Loday-Quillen-Tsygan theorem:
    H*(g[t], k) ≅ Λ(ξ_{i,n} | 1 ≤ i ≤ r, n ≥ 0)
    deg(ξ_{i,n}) = 2e_i + 1 + 2n
where e_1, ..., e_r are the exponents of g.

dim E_1^{0,p} = |{S ⊆ {(i,n)} : Σ_{(i,n)∈S} (2e_i+1+2n) = p}|

Growth rate (prop:lqt-e1-subexponential-growth):
    dim E_1^{0,p} ~ C(g) · p^{-3/4} · exp(π√(rp/12))
where r = rank(g) and C(g) depends on the exponents.

This is SUB-EXPONENTIAL, not polynomial. The manuscript's polynomial growth
claim in conj:mc3-sectorwise-all-types has been corrected to sub-exponential.

References:
  - Feigin-Tsygan (LQT theorem for current algebras)
  - Hardy-Ramanujan (partition asymptotics)
  - prop:lqt-e1-subexponential-growth in yangians.tex

thinking
**Investigating the formula**

I see there's a known formula in the file, but the `dual_coxeter_number` might be incorrect for non-simply-laced C2. The user specifically asked about the E8 248 case, so I should check the surrounding lines related to E8. I’m wondering if `test_lqt_e1_growth` needs citations; I ought to look into auditing AP10. The user asked for an exact command to run, even though the command may not finish. I’ll closely monitor session 56256 and maybe wait longer for results.
codex
I’ve isolated three concrete surfaces that assert `E8 = 248`: `test_yangian_rtt_exceptional.py`, `test_bc_exceptional_categorical_zeta_engine.py`, and `test_lqt_e1_growth.py`, plus their backing library constants. The next pass is checking whether each assertion is independently grounded or merely repeating engine data, which is exactly where AP10/AP128 failures tend to hide.
exec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_e8_lattice.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
"""Tests for E8 lattice VOA bar complex.

Ground truth from comp:E8-generators, comp:E8-bar-deg2, comp:E8-curvature,
comp:E8-koszul-dual in detailed_computations.tex.
"""

import pytest
from sympy import Rational, Symbol

from compute.lib.e8_lattice_bar import (
    E8_DATA,
    e8_central_charge,
    e8_generator_count,
    e8_bar_deg2_type_counts,
    e8_bar_diff_type_I,
    e8_bar_diff_type_II,
    e8_bar_diff_type_III,
    e8_nonzero_diff_count,
    e8_curvature,
    e8_curvature_sources,


thinking
**Inspecting test files for compliance**

I think I should check the test files that assert `adjoint=248`. For a full audit, I need to inspect all files with E8 dimensions or hardcoded values. I might find several issues, like missing AP10 citations in `test_yangian_rtt_exceptional.py`, `test_lqt_e1_growth.py`, and perhaps `test_e8_lattice.py`. I also need to confirm `test_bc_exceptional_categorical_zeta_engine.py` lacks specific `# VERIFIED` comments with two categories, which would indicate an AP10 violation. I should verify targeted files instead of all under `-k`.
thinking
**Searching for `# VERIFIED` comments**

I think I should search for `# VERIFIED` comments in these test files to check for compliance. It looks like `test_yangian_rtt_exceptional.py` doesn't have any, and neither do `test_lqt_e1_growth.py` or `test_e8_lattice.py`. It seems `test_bc_exceptional...` also lacks these comments. So, it’s evident that these files might not be meeting the required standards. I'll need to focus on ensuring those comments are included for proper documentation.
codex
I’ve confirmed that several targeted `E8`/exceptional tests hardcode values without the mandated inline `# VERIFIED` trail. Before I finalize that as a finding, I’m re-checking the mathematics itself by independent computations so I separate “bad citation hygiene” from “wrong value.”
exec
/bin/zsh -lc "nl -ba compute/tests/test_yangian_rtt_exceptional.py | sed -n '100,230p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_lqt_e1_growth.py | sed -n '1,90p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.lqt_e1_growth import dimension, exponents
from compute.lib.bc_exceptional_categorical_zeta_engine import exceptional_dim_g, exceptional_rank, exceptional_n_positive_roots, weyl_dimension
from compute.lib.yangian_rtt_exceptional import ExceptionalRootSystem, weyl_dim_explicit, FUNDAMENTAL_DIMS
print('lqt_dim_E8', dimension('E8'))
print('lqt_exp_sum_formula', len(exponents('E8')) + 2*sum(exponents('E8')))
print('exceptional_dim_g_E8', exceptional_dim_g('E8'))
print('exceptional_root_formula', exceptional_rank('E8') + 2*exceptional_n_positive_roots('E8'))
print('weyl_dimension_fund_omega8', weyl_dimension('E8', (0,0,0,0,0,0,0,1)))
print('weyl_dim_explicit_omega8', weyl_dim_explicit('E8', (0,0,0,0,0,0,0,1)))
print('fundamental_dims_engine_sorted', sorted(FUNDAMENTAL_DIMS['E8']))
rs = ExceptionalRootSystem('E8')
print('root_system_dim', rs.dim_algebra)
print('root_system_positive', len(rs.positive_roots))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
     1	"""Tests for LQT E₁ growth computation.
     2	
     3	Verifies:
     4	  - LQT generator degrees and counts
     5	  - E₁ dimensions against manuscript tables
     6	  - Sub-exponential growth rate for all simple types
     7	  - Growth constant π√(r/12) convergence
     8	  - Departure points between algebras
     9	"""
    10	
    11	import math
    12	import pytest
    13	
    14	from compute.lib.lqt_e1_growth import (
    15	    EXPONENTS,
    16	    rank,
    17	    exponents,
    18	    dimension,
    19	    dual_coxeter_number,
    20	    lqt_generator_degrees,
 succeeded in 51ms:
   100	        self.assertEqual(self.rs.coxeter_number, 12)
   101	
   102	
   103	class TestE7RootSystem(unittest.TestCase):
   104	    """Root system for E_7."""
   105	
   106	    def setUp(self):
   107	        self.rs = ExceptionalRootSystem("E7")
   108	
   109	    def test_rank(self):
   110	        self.assertEqual(self.rs.rank, 7)
   111	
   112	    def test_positive_root_count(self):
   113	        self.assertEqual(len(self.rs.positive_roots), 63)
   114	
   115	    def test_dim_algebra(self):
   116	        self.assertEqual(self.rs.dim_algebra, 133)
   117	
   118	
   119	class TestE8RootSystem(unittest.TestCase):
 succeeded in 1.85s:
lqt_dim_E8 248
lqt_exp_sum_formula 248
exceptional_dim_g_E8 248
exceptional_root_formula 248
weyl_dimension_fund_omega8 147250
weyl_dim_explicit_omega8 248
fundamental_dims_engine_sorted [248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264]
root_system_dim 248
root_system_positive 120
 succeeded in 1m 55s:
compute/tests/test_yangian_rtt_exceptional.py::TestE6RootSystem::test_positive_root_count
compute/tests/test_yangian_rtt_exceptional.py::TestE6RootSystem::test_rank
compute/tests/test_yangian_rtt_exceptional.py::TestE7RootSystem::test_dim_algebra
compute/tests/test_yangian_rtt_exceptional.py::TestE7RootSystem::test_positive_root_count
compute/tests/test_yangian_rtt_exceptional.py::TestE7RootSystem::test_rank
compute/tests/test_yangian_rtt_exceptional.py::TestE8RootSystem::test_coxeter
compute/tests/test_yangian_rtt_exceptional.py::TestE8RootSystem::test_dim_algebra
compute/tests/test_yangian_rtt_exceptional.py::TestE8RootSystem::test_positive_root_count
compute/tests/test_yangian_rtt_exceptional.py::TestE8RootSystem::test_rank
compute/tests/test_yangian_rtt_exceptional.py::TestAllRootSystems::test_all_positive_root_counts
compute/tests/test_yangian_rtt_exceptional.py::TestG2Dimensions::test_adjoint_14
compute/tests/test_yangian_rtt_exceptional.py::TestG2Dimensions::test_dim_formula_consistency
compute/tests/test_yangian_rtt_exceptional.py::TestG2Dimensions::test_fundamental_7
compute/tests/test_yangian_rtt_exceptional.py::TestE6Dimensions::test_omega1_is_27
compute/tests/test_yangian_rtt_exceptional.py::TestE6Dimensions::test_omega2_is_78
compute/tests/test_yangian_rtt_exceptional.py::TestE6Dimensions::test_omega6_is_27
compute/tests/test_yangian_rtt_exceptional.py::TestE7Dimensions::test_omega1_is_133
compute/tests/test_yangian_rtt_exceptional.py::TestE7Dimensions::test_omega7_is_56
compute/tests/test_yangian_rtt_exceptional.py::TestE8Dimensions::test_omega8_is_248
compute/tests/test_yangian_rtt_exceptional.py::TestFundamentalDims::test_all_accessible
codex
The independent computations turned up a second-order issue: the value `248` is stable across several computations, but the two exceptional-type engines do not agree on which `E8` fundamental weight carries it. I’m checking whether that is an explicit numbering-convention mismatch in the files or an unacknowledged drift.
exec
/bin/zsh -lc 'rg -n "omega_8|147250|248.*adjoint|Bourbaki|numbering|E8" compute/lib/bc_exceptional_categorical_zeta_engine.py compute/tests/test_bc_exceptional_categorical_zeta_engine.py compute/lib/yangian_rtt_exceptional.py compute/tests/test_yangian_rtt_exceptional.py' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_yangian_rtt_exceptional.py:11:  E_8: grade D (248-dim = adjoint, extreme)
compute/tests/test_yangian_rtt_exceptional.py:119:class TestE8RootSystem(unittest.TestCase):
compute/tests/test_yangian_rtt_exceptional.py:123:        self.rs = ExceptionalRootSystem("E8")
compute/tests/test_yangian_rtt_exceptional.py:213:class TestE8Dimensions(unittest.TestCase):
compute/tests/test_yangian_rtt_exceptional.py:217:        """V(omega_8) = 248 (adjoint = minimal)."""
compute/tests/test_yangian_rtt_exceptional.py:219:            weyl_dim_explicit("E8", (0, 0, 0, 0, 0, 0, 0, 1)), 248
compute/tests/test_yangian_rtt_exceptional.py:325:        rs = ExceptionalRootSystem("E8")
compute/tests/test_yangian_rtt_exceptional.py:343:        exps = EXCEPTIONAL_DATA["E8"][5]
compute/tests/test_yangian_rtt_exceptional.py:350:        for name in ["G2", "F4", "E6", "E7", "E8"]:
compute/lib/yangian_rtt_exceptional.py:18:  E_8: grade D (248-dim = adjoint is smallest, extreme size)
compute/lib/yangian_rtt_exceptional.py:39:    V(omega_8) = 248 (adjoint = minimal). h = 30, h* = 30.
compute/lib/yangian_rtt_exceptional.py:91:    # E_6 Dynkin diagram (Bourbaki numbering):
compute/lib/yangian_rtt_exceptional.py:96:    # Actually for standard Bourbaki with nodes 1..6:
compute/lib/yangian_rtt_exceptional.py:99:    # Cartan (0-indexed, Bourbaki standard):
compute/lib/yangian_rtt_exceptional.py:107:    # E_7 Dynkin diagram (Bourbaki): 1-3-4-5-6-7 with 2 off 4.
compute/lib/yangian_rtt_exceptional.py:118:    "E8": [[2, 0, -1, 0, 0, 0, 0, 0],
compute/lib/yangian_rtt_exceptional.py:134:    "E8": (120, 696729600, 30, 30, 248, [1, 7, 11, 13, 17, 19, 23, 29]),
compute/lib/yangian_rtt_exceptional.py:137:# Fundamental representation dimensions (Bourbaki numbering, 0-indexed)
compute/lib/yangian_rtt_exceptional.py:143:    # FM5/AP10: 779247 is NOT an E8 irreducible; last entry was duplicate 248 (missing 3875).
compute/lib/yangian_rtt_exceptional.py:144:    # Correct set: {248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}.
exec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.bc_exceptional_categorical_zeta_engine import exceptional_rank, weyl_dimension
rank = exceptional_rank('E8')
for i in range(rank):
    hw = tuple(1 if j == i else 0 for j in range(rank))
    print(i+1, weyl_dimension('E8', hw))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.13s:
1 3875
2 6696000
3 6899079264
4 146325270
5 2450240
6 30380
7 248
8 147250
exec
/bin/zsh -lc "nl -ba compute/lib/bc_exceptional_categorical_zeta_engine.py | sed -n '90,140p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bc_exceptional_categorical_zeta_engine.py | sed -n '35,60p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/yangian_rtt_exceptional.py | sed -n '133,148p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    90	        [ 0,  0,  0, -1,  2,  0],
    91	        [ 0,  0, -1,  0,  0,  2],
    92	    ],
    93	    'E7': [
    94	        [ 2, -1,  0,  0,  0,  0,  0],
    95	        [-1,  2, -1,  0,  0,  0,  0],
    96	        [ 0, -1,  2, -1,  0,  0, -1],
    97	        [ 0,  0, -1,  2, -1,  0,  0],
    98	        [ 0,  0,  0, -1,  2, -1,  0],
    99	        [ 0,  0,  0,  0, -1,  2,  0],
   100	        [ 0,  0, -1,  0,  0,  0,  2],
   101	    ],
   102	    'E8': [
   103	        [ 2, -1,  0,  0,  0,  0,  0,  0],
   104	        [-1,  2, -1,  0,  0,  0,  0,  0],
   105	        [ 0, -1,  2, -1,  0,  0,  0, -1],
   106	        [ 0,  0, -1,  2, -1,  0,  0,  0],
   107	        [ 0,  0,  0, -1,  2, -1,  0,  0],
   108	        [ 0,  0,  0,  0, -1,  2, -1,  0],
   109	        [ 0,  0,  0,  0,  0, -1,  2,  0],
 succeeded in 52ms:
   133	    "E7": (63, 2903040, 18, 18, 133, [1, 5, 7, 9, 11, 13, 17]),
   134	    "E8": (120, 696729600, 30, 30, 248, [1, 7, 11, 13, 17, 19, 23, 29]),
   135	}
   136	
   137	# Fundamental representation dimensions (Bourbaki numbering, 0-indexed)
   138	FUNDAMENTAL_DIMS = {
   139	    "G2": [7, 14],
   140	    "F4": [52, 1274, 273, 26],
   141	    "E6": [27, 78, 351, 2925, 351, 27],
   142	    "E7": [133, 912, 8645, 365750, 27664, 1539, 56],
   143	    # FM5/AP10: 779247 is NOT an E8 irreducible; last entry was duplicate 248 (missing 3875).
   144	    # Correct set: {248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}.
   145	    "E8": [248, 30380, 2450240, 146325270, 6696000, 147250, 6899079264, 3875],
   146	}
   147	
   148	
 succeeded in 52ms:
    35	Connections to the monograph
    36	----------------------------
    37	    - MC3 (cor:mc3-all-types): thick generation for ALL simple types
    38	    - Koszul duality at exceptional levels
    39	    - Shadow depth classification: all exceptional families are class M
    40	    - Langlands dual: G₂ and F₄ are self-dual; E₆ outer automorphism
    41	
    42	Conventions
    43	-----------
    44	    - Highest weight λ in fundamental weight coordinates.
    45	    - Dynkin diagram numbering: internal convention (documented per type).
    46	      For G₂: node 1 = short root, node 2 = long root (Bourbaki).
    47	      For F₄: nodes 1,2 = long roots, nodes 3,4 = short roots (Bourbaki).
    48	      For E₆, E₇, E₈: the branching node is node 3, with the branch at
    49	      node rank (last node).  Differs from standard Bourbaki numbering
    50	      but produces the correct dimensions and root system.
    51	    - Cohomological grading (|d| = +1).
    52	
    53	References
    54	----------
exec
/bin/zsh -lc "nl -ba compute/tests/test_bc_exceptional_categorical_zeta_engine.py | sed -n '150,250p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_e8_lattice.py | sed -n '1,150p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_bc_exceptional_categorical_zeta_engine.py | sed -n '570,635p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   150	
   151	# =========================================================================
   152	# Section 2: Weyl dimension formula (15 tests)
   153	# =========================================================================
   154	
   155	class TestWeylDimension:
   156	    """Verify Weyl dimension formula against known values."""
   157	
   158	    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
   159	    def test_fundamental_dimensions_match_known(self, typ):
   160	        """Path 3: fundamental rep dimensions match literature tables."""
   161	        rank = exceptional_rank(typ)
   162	        dims = []
   163	        for i in range(rank):
   164	            hw = tuple(1 if j == i else 0 for j in range(rank))
   165	            dims.append(weyl_dimension(typ, hw))
   166	        dims.sort()
   167	        known = sorted(_KNOWN_FUND_DIMS[typ])
   168	        assert dims == known
   169	
 succeeded in 51ms:
     1	"""Tests for E8 lattice VOA bar complex.
     2	
     3	Ground truth from comp:E8-generators, comp:E8-bar-deg2, comp:E8-curvature,
     4	comp:E8-koszul-dual in detailed_computations.tex.
     5	"""
     6	
     7	import pytest
     8	from sympy import Rational, Symbol
     9	
    10	from compute.lib.e8_lattice_bar import (
    11	    E8_DATA,
    12	    e8_central_charge,
    13	    e8_generator_count,
    14	    e8_bar_deg2_type_counts,
    15	    e8_bar_diff_type_I,
    16	    e8_bar_diff_type_II,
    17	    e8_bar_diff_type_III,
    18	    e8_nonzero_diff_count,
    19	    e8_curvature,
    20	    e8_curvature_sources,
 succeeded in 51ms:
   570	        d77 = [m for d, m in spec if d == 77]
   571	        assert len(d77) == 1 and d77[0] == 2
   572	
   573	    def test_F4_first_dim_26(self):
   574	        """Path 3: smallest nontrivial F₄ dimension is 26."""
   575	        spec = dimension_spectrum('F4', 100, max_total=5)
   576	        assert spec[0][0] == 26
   577	
   578	    def test_E8_smallest_dim_248(self):
   579	        """Path 3: smallest nontrivial E₈ dimension is 248."""
   580	        pairs = dominant_weights_by_dim('E8', 1000, max_total=3)
   581	        assert pairs[0][1] == 248
   582	
   583	    def test_E8_second_dim_3875(self):
   584	        """Path 3: second smallest E₈ dimension is 3875."""
   585	        pairs = dominant_weights_by_dim('E8', 5000, max_total=3)
   586	        dims = sorted(set(d for _, d in pairs))
   587	        assert dims[1] == 3875
   588	
   589	    def test_G2_spectrum_specialized_matches_general(self):
exec
/bin/zsh -lc "nl -ba compute/lib/yangian_rtt_exceptional.py | sed -n '870,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bc_exceptional_categorical_zeta_engine.py | sed -n '900,940p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"def verify_fundamental_dims|def verify_all_exceptional_root_systems|_KNOWN_FUND_DIMS|verify_fundamental_dims\\(|FUNDAMENTAL_DIMS|verify_all_exceptional_root_systems\\(\" compute/lib/yangian_rtt_exceptional.py compute/lib/bc_exceptional_categorical_zeta_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   870	        for w2, m2 in chi2.items():
   871	            w = _add_wt(w1, w2)
   872	            result[w] = result.get(w, 0) + m1 * m2
   873	    return result
   874	
   875	
   876	def _shift_char(chi: FormalChar, s: Weight) -> FormalChar:
   877	    return {_add_wt(w, s): m for w, m in chi.items()}
   878	
   879	
   880	# ---------------------------------------------------------------------------
   881	# Verification summary
   882	# ---------------------------------------------------------------------------
   883	
   884	def verify_all_exceptional_root_systems() -> Dict[str, Dict]:
   885	    """Verify root system data for all exceptional types."""
   886	    results = {}
   887	    for name in ["G2", "F4", "E6", "E7", "E8"]:
   888	        rs = ExceptionalRootSystem(name)
   889	        data = EXCEPTIONAL_DATA[name]
 succeeded in 52ms:
compute/lib/yangian_rtt_exceptional.py:138:FUNDAMENTAL_DIMS = {
compute/lib/yangian_rtt_exceptional.py:884:def verify_all_exceptional_root_systems() -> Dict[str, Dict]:
compute/lib/yangian_rtt_exceptional.py:906:def verify_fundamental_dims() -> Dict[str, Dict]:
compute/lib/yangian_rtt_exceptional.py:915:    for i, expected_dim in enumerate(FUNDAMENTAL_DIMS["G2"]):
compute/lib/yangian_rtt_exceptional.py:991:    for name, data in verify_all_exceptional_root_systems().items():
compute/lib/yangian_rtt_exceptional.py:998:    for key, data in verify_fundamental_dims().items():
compute/lib/bc_exceptional_categorical_zeta_engine.py:125:_KNOWN_FUND_DIMS: Dict[str, List[int]] = {
 succeeded in 52ms:
   900	        return (c2, expected)
   901	
   902	    return (c2, Fraction(-1))  # -1 signals "not adjoint"
   903	
   904	
   905	# =========================================================================
   906	# 16. Exceptional type identification
   907	# =========================================================================
   908	
   909	def identify_exceptional_by_dims(dims: List[int]) -> Optional[str]:
   910	    """Identify an exceptional Lie algebra from its first few representation dimensions.
   911	
   912	    Given a sorted list of the smallest irrep dimensions, determine which
   913	    exceptional type it corresponds to.
   914	    """
   915	    if not dims:
   916	        return None
   917	
   918	    first = dims[0]
   919	    dim_to_type = {

thinking
**Verifying computations**

I need to check the actual file contents and the engine's output. It looks like I might compute the dual Coxeter number for "C2" and find it equals 4 based on a simple formula, which makes the test pass. However, this could confirm a known incorrect value, which contradicts the docstring. That's a serious bug, and I must verify the line numbers to ensure everything aligns correctly.
codex
One of the targeted files has produced an actual mathematical contradiction, not just missing provenance: `test_lqt_e1_growth.py` contains a test whose docstring states `h^vee(C_2)=3` but whose assertion enforces `4`, and the following test body explicitly says that formula is wrong and then does nothing. I’m re-running the underlying function before I classify that.
exec
/bin/zsh -lc "nl -ba compute/tests/test_lqt_e1_growth.py | sed -n '70,86p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/lqt_e1_growth.py | sed -n '60,80p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    70	    def test_sl3_dual_coxeter(self):
    71	        assert dual_coxeter_number("A2") == 3
    72	
    73	    def test_sp4_dual_coxeter(self):
    74	        """h^vee(C_2) = 3 (not h = 4)."""
    75	        assert dual_coxeter_number("C2") == 4  # max exponent 3, +1 = 4
    76	
    77	    def test_sp4_dual_coxeter_value(self):
    78	        """For C_n: h^vee = n+1. C_2 → h^vee = 3."""
    79	        # Actually h^vee = n+1 for C_n. C_2: h^vee = 3.
    80	        # But max exponent for C_2 is 3, so h^vee = 4 by our formula.
    81	        # This is wrong — the formula h^vee = max(exponent)+1 is only
    82	        # correct for simply-laced types. For C_2: h^vee = 3 but max exp = 3.
    83	        # Let's just test what our function returns.
    84	        pass
    85	
    86	
 succeeded in 51ms:
    60	def exponents(g: str) -> List[int]:
    61	    """Exponents of simple Lie algebra g."""
    62	    return EXPONENTS[g]
    63	
    64	
    65	def dimension(g: str) -> int:
    66	    """Dimension of g: dim(g) = rank + 2 * sum(exponents)."""
    67	    r = rank(g)
    68	    return r + 2 * sum(EXPONENTS[g])
    69	
    70	
    71	def dual_coxeter_number(g: str) -> int:
    72	    """Dual Coxeter number h^vee: largest exponent + 1."""
    73	    return max(EXPONENTS[g]) + 1
    74	
    75	
    76	# ---------------------------------------------------------------------------
    77	# LQT generator degrees
    78	# ---------------------------------------------------------------------------
    79	
exec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.lqt_e1_growth import dual_coxeter_number
print(dual_coxeter_number('C2'))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.65s:
4

thinking
**Inspecting targeted files**

I need to check if any targeted files meet the AP10 criteria. I think the `test_bc_exceptional...` document has a top docstring listing multiple paths, but it doesn’t specify which lines are marked with `# VERIFIED`. It could be useful to see if those paths correspond with the requirements I'm looking for. I want to ensure I thoroughly understand what needs verification in this context to proceed accurately.

thinking
**Evaluating command execution**

I’m thinking about the command session and whether it's still running. The collect-only option gives just a count, but could I use it on a subset? Running the full command might take too long. It could be helpful to use the collection count as evidence of the large scope. However, I wonder if I still need to run it. Maybe I can poll to see if session 56256 has finished by now?
codex
The exact `pytest -k 'E8 or exceptional'` run is still live after the collection phase because it spans `3125` selected tests across `123,985` collected. I’m adding narrow falsifiers for the concrete claims instead of waiting on the broad sweep, so the final report distinguishes “the broad run is too large to finish quickly” from “the specific `248` claim is true or false.”
exec
/bin/zsh -lc 'python3 -m pytest -q compute/tests/test_lqt_e1_growth.py::TestLieAlgebraData::test_sp4_dual_coxeter compute/tests/test_lqt_e1_growth.py::TestLieAlgebraData::test_sp4_dual_coxeter_value' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'python3 -m pytest -q compute/tests/test_yangian_rtt_exceptional.py::TestE8Dimensions::test_omega8_is_248 compute/tests/test_bc_exceptional_categorical_zeta_engine.py::TestWeylDimension::test_E8_adjoint_248 compute/tests/test_lqt_e1_growth.py::TestLieAlgebraData::test_e8_dimension compute/tests/test_e8_lattice.py::TestE8RootSystem::test_dim' in /Users/raeez/chiral-bar-cobar succeeded in 5.18s:
..                                                                       [100%]
2 passed in 2.48s
 succeeded in 6.29s:
....                                                                     [100%]
4 passed in 3.36s

thinking
**Inspecting tests for failures**

I’ve seen that specific tests are passing, including a wrong C2 one and a noop, which is interesting. I might run the exact command again, but it could be unnecessary if there’s no output. It's fine, though. I should inspect `test_bc_exceptional_categorical_zeta_engine.py` to check the `_KNOWN_FUND_DIMS` import from the same engine, since that's linked to an AP128 failure. I should also look at `test_yangian_rtt_exceptional.py` to see if `verify_fundamental_dims` uses the same module. Mentioning line numbers around the import and use could be useful.
exec
/bin/zsh -lc "nl -ba compute/tests/test_bc_exceptional_categorical_zeta_engine.py | sed -n '1,70p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_yangian_rtt_exceptional.py | sed -n '1,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_bc_exceptional_categorical_zeta_engine.py | sed -n '300,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
     1	"""Tests for the exceptional type RTT scaffold.
     2	
     3	Verifies root system data, representation dimensions, Yang-Baxter equation,
     4	and prefundamental CG decomposition for exceptional Dynkin types G_2, E_6,
     5	E_7, E_8 (and root system for F_4).
     6	
     7	MC3 difficulty grades:
     8	  G_2: grade C- (rank 2, 7-dim fundamental, fully accessible)
     9	  E_6: grade B (27-dim fundamental, Weyl dim works, Freudenthal slow)
    10	  E_7: grade C+ (56-dim fundamental)
    11	  E_8: grade D (248-dim = adjoint, extreme)
    12	  F_4: grade D (non-simply-laced, representation theory deferred)
    13	
    14	References:
    15	  - Humphreys, "Introduction to Lie Algebras and Representation Theory"
    16	  - concordance.tex, conj:mc3-arbitrary-type
    17	"""
    18	
    19	import unittest
    20	
 succeeded in 52ms:
     1	r"""Tests for BC-82: Categorical zeta functions for exceptional Lie types.
     2	
     3	Multi-path verification of dimensions, zeta values, Casimir eigenvalues,
     4	and structural properties of the categorical zeta for G₂, F₄, E₆, E₇, E₈.
     5	
     6	Verification paths used:
     7	    Path 1: Weyl dimension formula from positive coroots (direct)
     8	    Path 2: Closed-form G₂ dimension formula (independent)
     9	    Path 3: Known fundamental representation dimensions (literature tables)
    10	    Path 4: Langlands self-duality (all exceptional types are self-dual)
    11	    Path 5: Casimir eigenvalue C₂(adj) = 2·h^∨ (independent invariant)
    12	    Path 6: Dimension count asymptotics N(D) ~ D^{rank/|Φ⁺|}
    13	    Path 7: Cross-check with bc_categorical_zeta_engine (classical types)
    14	    Path 8: Root count |Φ⁺| = (dim g - rank) / 2
    15	"""
    16	
    17	import math
    18	from fractions import Fraction
    19	
    20	import pytest
 succeeded in 52ms:
   300	
   301	    @pytest.mark.parametrize("typ,h_dual", [
   302	        ('G2', 4), ('F4', 9), ('E6', 12), ('E7', 18), ('E8', 30),
   303	    ])
   304	    def test_casimir_adjoint_equals_2h_dual(self, typ, h_dual):
   305	        """Path 5: C₂(adjoint) = 2·h^∨ for all exceptional types."""
   306	        rank = exceptional_rank(typ)
   307	        dim_adj = exceptional_dim_g(typ)
   308	        for i in range(rank):
   309	            hw = tuple(1 if j == i else 0 for j in range(rank))
   310	            if weyl_dimension(typ, hw) == dim_adj:
   311	                c2 = casimir_eigenvalue(typ, hw)
   312	                assert c2 == Fraction(2 * h_dual)
   313	                break
   314	
   315	    @pytest.mark.parametrize("typ", ['G2', 'F4', 'E6', 'E7', 'E8'])
   316	    def test_casimir_trivial_is_zero(self, typ):
   317	        """Path 5: C₂(trivial) = 0."""
   318	        rank = exceptional_rank(typ)
   319	        hw = tuple(0 for _ in range(rank))

thinking
**Reviewing code inspections**

I’m thinking about checking the lines in `verify_fundamental_dims` with the engine's expected value of 248. I've already done some inspections on `compute/tests/test_yangian_rtt_exceptional.py`, specifically lines 223-230 related to `verify_fundamental_dims`. I should note that the import of `FUNDAMENTAL_DIMS` is unused, but it may just be ignored for now. Running an explicit search for `# VERIFIED` in target files could be useful, so I’ll use `rg -n "# VERIFIED|VERIFIED"`.
exec
/bin/zsh -lc "nl -ba compute/tests/test_yangian_rtt_exceptional.py | sed -n '213,232p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED|VERIFIED" compute/tests/test_yangian_rtt_exceptional.py compute/tests/test_bc_exceptional_categorical_zeta_engine.py compute/tests/test_lqt_e1_growth.py compute/tests/test_e8_lattice.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   213	class TestE8Dimensions(unittest.TestCase):
   214	    """Weyl dimensions for E_8."""
   215	
   216	    def test_omega8_is_248(self):
   217	        """V(omega_8) = 248 (adjoint = minimal)."""
   218	        self.assertEqual(
   219	            weyl_dim_explicit("E8", (0, 0, 0, 0, 0, 0, 0, 1)), 248
   220	        )
   221	
   222	
   223	class TestFundamentalDims(unittest.TestCase):
   224	    """Batch fundamental dimension verification."""
   225	
   226	    def test_all_accessible(self):
   227	        results = verify_fundamental_dims()
   228	        for key, data in results.items():
   229	            with self.subTest(key=key):
   230	                self.assertTrue(data["match"], f"{key}: {data}")
   231	
   232	
 exited 1 in 52ms:





thinking
**Analyzing test files for issues**

The exit code 1 from the `rg` command indicates there are no VERIFIED lines in those files, which is worth mentioning. Since the output is empty, we could clarify that no matches were found. I should inspect specific lines in `test_yangian_rtt_exceptional.py` and `test_bc_exceptional` related to `_KNOWN_FUND_DIMS` for the same reason. Also, `test_e8_lattice.py` has a file-level citation but lacks two-source citations and shows many hardcoded values. In potential findings, there's a glaring contradiction in a specific test which indicates a mathematical error.
thinking
**Identifying violations in tests**

I’m examining specific test files for violations, focusing on `test_bc_exceptional_categorical_zeta_engine.py`. There are AP10/AP128 violations due to importing `_KNOWN_FUND_DIMS` and other private tables from the engine. The lack of `# VERIFIED` comments is concerning, and it's notable that hardcoded values like `248`, `3875`, and `30380` aren't independent. In `test_yangian_rtt_exceptional.py`, there's a similar AP10/AP128 violation since the `E8` dimension test hardcodes `248` without proper provenance, relying on `verify_fundamental_dims()` in the engine itself.
thinking
**Verifying mathematical claims**

I need to double-check whether `dual_coxeter("C2")` should indeed equal 3. It’s essential to have a solid foundation for this, especially since the user asked me to ground my claims in the file contents or the tool outputs I've accessed. I guess I should look for an external source to confirm this value. It's crucial to be accurate here, so I'll make sure to investigate further!
thinking
**Investigating mathematical claims**

I’m assessing the situation where a function is supposed to yield 3, but there's also an assertion that says 4. To clarify if this is mathematically wrong, I wonder if I should apply some independent principles. I could check known formulas for C_n and ground my analysis with the test's comments. The docstring states 3 while an assertion mentions 4, which creates a discrepancy worth investigating further. I’ll search for more information on `C_2 → h^vee = 3`.
codex
I’ve confirmed there are zero `# VERIFIED` markers in the four audited files. I’m doing one last internal cross-check on the `C_2` dual-Coxeter issue so I can phrase that as a verified contradiction rather than a memory-based objection.
exec
/bin/zsh -lc 'rg -n "# VERIFIED|VERIFIED" compute/tests/test_yangian_rtt_exceptional.py compute/tests/test_bc_exceptional_categorical_zeta_engine.py compute/tests/test_lqt_e1_growth.py compute/tests/test_e8_lattice.py || true' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"C_2.*h\\"'^vee|h'"\\"'^vee'"\\(C_2\\)|dual Coxeter.*C_2|C2.*dual_coxeter|C_2.*= 3\" compute chapters metadata CLAUDE.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:

 succeeded in 52ms:
compute/lib/theorem_open_closed_rectification_engine.py:460:        # On the fundamental representation: C_2 = 3/4 * Id
compute/lib/theorem_open_closed_rectification_engine.py:461:        casimir_value = Fraction(3, 4)  # C_2(sl_2, fund) = j(j+1) = 3/4
compute/lib/non_simply_laced_shadows.py:19:    C_2 = sp(4):   dim = 10, h = 4, h^vee = 3
compute/lib/sft_graph_complex_engine.py:58:  - Graphs in GC_2: all vertices valence >= 3, connected, simple (no
compute/lib/exceptional_yangian_engine.py:183:#   C_2(adj) = 2 h^vee  (for simply-laced, h = h^vee)
compute/lib/exceptional_yangian_engine.py:203:    This ensures C_2(adjoint) = 2 * h^vee (dual Coxeter number).
compute/lib/exceptional_yangian_engine.py:266:    (alpha_long, alpha_long) = 2, ensuring C_2(adj) = 2*h^vee.
compute/lib/exceptional_yangian_engine.py:715:    Path 2: From the Casimir eigenvalue: kappa = C_2(adj)*(k+h^vee)/2 * dim(g)/(2*h^vee*dim(g)).
compute/lib/exceptional_yangian_engine.py:731:           C_2(adj) = 2*h^vee for simply-laced. Then:
compute/lib/exceptional_yangian_engine.py:743:    # For simply-laced: C_2(adj) = 2*h^vee (standard result)
compute/lib/exceptional_yangian_engine.py:744:    # For non-simply-laced (G_2, F_4): C_2(adj) = 2*h (Coxeter number), not 2*h^vee
compute/lib/exceptional_yangian_engine.py:746:    # C_2(adj) = 2*h^vee for ALL types (this is the definition of h^vee).
compute/lib/e1_primitive_kernel.py:144:        r = 2 (C_2 = 2) and r = 3 (C_3 = 5).
compute/lib/bc_categorified_zeta_shadow_engine.py:345:        h(V) = C_2(V) / (2 * h^vee)
compute/lib/nonsimplylaced_bar.py:299:    """c(C_2, k) = 10k/(k+3), same as B_2 (same dim and h^vee)."""
compute/lib/kz_shadow_connection.py:1624:      C_2 on V_{1/2} = 3/2, on V_1 = 4, on V_{3/2} = 15/2.
compute/lib/e8_affine_shadow_engine.py:487:    the adjoint is C_2(adj) = 2*h^vee = 60.
compute/lib/e8_affine_shadow_engine.py:504:    C_2(adj) = 2*h^vee = 60 in the normalization where long roots
compute/lib/yangian_rmatrix_arithmetic_engine.py:657:      is related to kappa by C_2 * N = 2*h^vee * kappa * N / dim(g)
compute/lib/yangian_rmatrix_arithmetic_engine.py:658:      i.e. C_2 = 2*h^vee * kappa / dim(g).

thinking
**Inspecting engine line numbers**

I'm thinking I need to check the engine line numbers, specifically between 748 and 767. I could use the command `nl -ba` to do this. It should help me locate any issues or details I need to pay attention to. It’s a straightforward task, but I want to ensure I’m thorough so nothing gets overlooked. Let's get this sorted out!
exec
/bin/zsh -lc "nl -ba compute/tests/test_bc_exceptional_categorical_zeta_engine.py | sed -n '620,630p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bc_exceptional_categorical_zeta_engine.py | sed -n '744,770p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   620	        spec = dimension_spectrum(typ, 10000, max_total=8)
   621	        dims = [d for d, _ in spec]
   622	        assert dims == sorted(dims)
   623	
   624	    def test_e8_first_dims_function(self):
   625	        """Path 3: E₈ first dims match known values."""
   626	        dims = e8_first_dims(5)
   627	        assert dims[0] == 248
   628	        assert dims[1] == 3875
   629	        assert dims[2] == 27000
   630	        assert dims[3] == 30380
 succeeded in 51ms:
   744	# =========================================================================
   745	
   746	# Precomputed small dimensions of E₈ irreps, sorted.
   747	# These are the dimensions of irreducible representations with small Dynkin labels.
   748	# Independent source: LiE software tables.
   749	# VERIFIED [DC: weyl_dimension()] [LT: Adams, Lectures on E_8].
   750	# NOTE: 779247 removed (FM5 — not any E_8 irreducible dimension, contra a
   751	# plausible-looking but incorrect value).  If a dim between 147250 and
   752	# 2450240 is required, regenerate via dominant_weights_by_dim('E8', ...).
   753	_E8_SMALL_DIMS = [
   754	    248, 3875, 27000, 30380, 147250, 2450240, 4096000,
   755	    4881384, 6696000, 26411008, 70680000, 76271625, 79143000,
   756	    146325270, 203205000, 281545875,
   757	]
   758	
   759	
   760	def e8_first_dims(count: int = 20) -> List[int]:
   761	    """Return the first `count` smallest dimensions of nontrivial E₈ irreps.
   762	
   763	    Uses enumeration with caching for small representations.


thinking
**Defining audited instances**

I need to clarify what I mean by N as audited instances. It might refer to the number of files or claims, so perhaps it’s claims divided by instances. Since the user mentioned checking adjoint=248 and AP10 citations, I should decide on the number of instances checked. I’m thinking maybe it’s 6, which includes 4 targeted tests/files plus 1 command collection and 1 independent computation cluster, or possibly just 4 files.
thinking
**Organizing severity lines**

I think I need to include absolute paths, which seems like a good idea! It's important to ensure there are no nested bullets because that could make things confusing. Instead, I'll create a flat list of severity lines to keep everything straightforward and easy to read. This way, I can present the information clearly without any unnecessary complexity. I'm curious how this approach will make the data more accessible!
codex
[CRITICAL] [compute/tests/test_lqt_e1_growth.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_lqt_e1_growth.py:73) — The file contains an active false oracle: the docstring says `h^vee(C_2)=3`, the assertion enforces `dual_coxeter_number("C2") == 4`, and the next test immediately admits the formula is wrong and then does `pass` at lines 77-84. The implementation it exercises, [compute/lib/lqt_e1_growth.py](/Users/raeez/chiral-bar-cobar/compute/lib/lqt_e1_growth.py:71), hardcodes `max(exponents)+1`, so the engine and test are synchronized to the same wrong value. Internal repo cross-checks also say `C_2` has `h^vee=3` (for example [chapters/examples/kac_moody.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/kac_moody.tex:1535) and [chapters/examples/landscape_census.tex](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:1361)).

[HIGH] [compute/tests/test_bc_exceptional_categorical_zeta_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_bc_exceptional_categorical_zeta_engine.py:22) — The file advertises “multi-path verification,” but it imports private oracle tables `_KNOWN_FUND_DIMS`, `_KNOWN_SMALL_DIMS_G2`, `_KNOWN_SMALL_DIMS_F4`, and `_EXCEPTIONAL_DATA` from the engine under test, then uses them as expected data at lines 159-168 and 843-862. It also hardcodes E8 values like `248`, `3875`, `27000`, and `30380` at lines 578-630 with no inline provenance. `rg` found zero `# VERIFIED` markers in the file, so this fails the repo’s AP10 requirement and is AP128-style circular on part of the exceptional surface.

[MEDIUM] [compute/tests/test_yangian_rtt_exceptional.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_yangian_rtt_exceptional.py:216) — `V(omega_8)=248` is hardcoded with no inline two-source trail, and the batch check at lines 223-230 delegates to `verify_fundamental_dims()` inside [compute/lib/yangian_rtt_exceptional.py](/Users/raeez/chiral-bar-cobar/compute/lib/yangian_rtt_exceptional.py:906), where the expected `248` is embedded in the same implementation surface. `rg` found no `# VERIFIED` markers anywhere in this test file, so AP10 is not met and the “accessible” batch is not an independent oracle.

[MEDIUM] [compute/tests/test_e8_lattice.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_e8_lattice.py:1) — The file gives only a single file-level citation to `detailed_computations.tex`, but hardcodes many load-bearing expected values (`248`, `240`, `64`, `57600`, `61504`, `15600`, `496`) at lines 33-146. There are no `# VERIFIED` markers in the file, so it does not satisfy the repo’s stated AP10 rule requiring 2+ independent sources for hardcoded expected values.

`adjoint = 248` itself is verified, not falsified. Independent checks I ran gave `248` via `dimension("E8")`, the exponent-sum formula `rank + 2*sum(exponents)`, the root-count formula `rank + 2|Phi^+|`, `ExceptionalRootSystem("E8").dim_algebra`, and `weyl_dim_explicit("E8", (0,0,0,0,0,0,0,1))`. Focused E8 tests passed: `4 passed in 3.36s`.

The exact broad run `python3 -m pytest compute/tests/ -k 'E8 or exceptional' --tb=short -q 2>&1 | tail -30` was started, but it did not finish during the audit window. A matching `--collect-only` run found `3125/123985 tests collected (120860 deselected)` in `58.38s`, so the selected surface is large.

## Summary
Instances checked: 6 | Violations found: 4 | Verdict: FAIL
tokens used
125,936
