# CE04_rmatrix (598s, gpt-5.4)

- [HIGH] [compute/tests/test_theorem_pva_classical_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:8) — The header claims “3+ per claim” and “Cross-family consistency verified (AP10)”, but the hardcoded expected values later in the file, including `3(k+2)/4`, `c/2`, and `c/3` ([lines 475](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:475), [485](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:485), [699](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:699)), have no `# VERIFIED` comments at all. A grep over this file returned zero `# VERIFIED` hits, so AP10/AP128 is not actually enforced on this surface.
- [HIGH] [compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:736) — The file hardcodes manual oracle data such as `rpoles_manual = {3: F(13), 1: F(2)}`, `R2_path3 = -c/4`, and `kappa_5 = c/2` ([lines 750](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:750), [792](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:792), [822](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:822)) under “verified 3 ways / 5 ways”, but the file also has zero `# VERIFIED` annotations. The expected values are present; the required two-source audit trail is not.
- [MEDIUM] [compute/tests/test_theorem_three_way_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:134) — This selected `r_matrix` test file hardcodes the affine `sl_2` residue as `\Omega/((k+2)z)` and expects `1/(k+2)` at [line 175](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:175). Inference: the keyword slice therefore mixes KZ normalization here with the trace-form AP126 surface in `test_rmatrix_landscape.py`, so the user’s requested `k=0→0` check is not uniform across the selected tests. This file also has zero `# VERIFIED` tags.
- [MEDIUM] [compute/tests/test_rmatrix_landscape.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1013) — This file does enforce the trace-form AP126 boundary check: `r^{aff sl_2}(z)=k\Omega/z` and `k=0→0` are tested directly at [lines 1030](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1030) and [1050](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1050). But the same block hardcodes zero-level kappa expectations `0`, `3/2`, and `4` at [lines 1103](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1103)-[1105](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1105) with no `# VERIFIED` provenance, and grep found no `# VERIFIED` markers anywhere in the file.

Control/build note: [compute/tests/test_w_infinity_chiral_qg_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_w_infinity_chiral_qg_engine.py:447) contains a compliant `# VERIFIED: [DC] ... [SY] ...` annotation, so the missing-source findings above are real deviations, not a repo-wide absence of the pattern. A focused subset of four core files passed (`352 passed in 6.94s`); the exact full piped command was started, but it was still progressing after extended polling, so I do not have its final tail output.

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
session id: 019d83bd-58e8-7093-9d35-1bccc3398ab1
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


Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'r_matrix or rmatrix' --tb=short -q 2>&1 | tail -30. Check: level prefix present? k=0→0?

Also check: are hardcoded expected values in test files cited with 2+ independent sources (AP10/AP128)? Read the test file and verify.
mcp startup: no servers
codex
Using `deep-beilinson-audit` for adversarial verification and `build-surface` for the pytest evidence. I’m starting by reading the skill instructions, then I’ll run the requested `r_matrix` test slice and inspect the test files for level-prefix coverage and AP10/AP128 source-citation discipline.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
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
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'r_matrix or rmatrix' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 148ms:
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


thinking
**Updating testing process**

My Pytest session is still running, so I might need to poll it to get updates. I’m considering reading CLAUDE and other relevant skills. It seems like I could run a few commands in parallel to make things more efficient. I should think about updating my plan — it might not be strictly necessary, but could be useful. I also need to ensure that my commentary is up to date.
codex
The skill instructions confirm the audit path: load the canonical repo surfaces, then attack the compute/test claim cluster directly. The pytest slice is still running; in parallel I’m reading the constitutional files and locating the exact `r_matrix` test files to verify both mathematical coverage and source annotations.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "r_matrix|rmatrix|R-matrix|r-matrix|Omega/z|k=0" compute/tests' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 173ms:
compute/tests/test_shadow_trace_formula_engine.py:801:        These are NOT equal for any w unless k=0. This is expected.
compute/tests/test_agt_nekrasov_shadow_engine.py:227:        """SU(4) at k=0: Z_0 = 1."""
compute/tests/test_agt_nekrasov_shadow_engine.py:398:        """k=0: HS = 1 (trivial moduli space)."""
compute/tests/test_agt_nekrasov_shadow_engine.py:711:        """At k=0: one N-tuple (all empty) for all N."""
compute/tests/test_agt_nekrasov_shadow_engine.py:742:        # Manual count: sum_{k=0}^{3} p(k)*p(3-k)
compute/tests/test_agt_nekrasov_shadow_engine.py:1022:        """N-tuples at k=0: one tuple of empty partitions."""
compute/tests/test_cy_gepner_k3_engine.py:1389:        """k=0 gives c=0 (trivial model)."""
compute/tests/test_cy_gepner_k3_engine.py:1390:        model = N2MinimalModel(k=0)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:1:r"""Tests for sl_3 Yangian R-matrix from the ordered bar complex.
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:3:First rank-2 computation of the Yangian R-matrix from the monograph's
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:11:    5. r-matrix pole structure (AP19)
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:20:   14. Cross-checks with yangian_rmatrix_sl3.py
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:24:    - yangian_rmatrix_sl3.py: fundamental Casimir, YBE, spectral decomposition.
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:25:    - yangian_residue_extraction.py: Yang R-matrix for sl_N.
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:33:from compute.lib.theorem_sl3_yangian_r_matrix_engine import (
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:48:    # r-matrix
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:49:    r_matrix_fund, r_matrix_adj,
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:50:    # R-matrix
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:60:    dnp_r_matrix_genus0, dnp_comparison_report,
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:62:    sl2_yang_r_matrix, sl2_casimir_fund, verify_sl2_casimir_identity, verify_sl2_ybe,
 succeeded in 185ms:
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

 succeeded in 189ms:
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
 succeeded in 292ms:
# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

 succeeded in 319ms:
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
codex
I have the repo-wide AP126/AP128 policy text and the test-file search surface now. Next I’m isolating the actual `r_matrix` test modules and the pytest result, then I’ll re-read the hardcoded assertions against their comments instead of trusting the grep summaries.
exec
/bin/zsh -lc "rg -n \"VERIFIED|verified|AP10|AP128|Omega/z|k\\\\s*=\\\\s*0|k=0\" compute/tests/test_*r_matrix* compute/tests/*rmatrix* 2>/dev/null" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg --files compute/tests | rg 'r_matrix|rmatrix'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:277:    """The r-matrix r(z) = Omega/z has a single pole at z=0 (AP19)."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:280:        """r(z) = Omega/z has a single pole (AP19)."""
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py:503:        """r^{MK}(z) = r^{DNP}(z) = Omega/z at genus 0."""
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:17:AP44 divided-power convention verified at every step.
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:18:Cross-family consistency verified (AP10).
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:162:        """AP19 verified for all sl_2 channels."""
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:357:        """sl_2: CYBE verified numerically in fundamental representation.
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:359:        The CYBE for r(z) = Omega/z decomposes into two conditions:
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:373:        r(z) = k*Omega/z and the commutators scale as k^2 on both sides.
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:502:        assert result['ap19_verified'] is True
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:511:        assert result['ap19_verified'] is True
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:614:        """Heisenberg r-matrix verified via 3 independent paths.
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:635:        """Virasoro r-matrix verified via 3 independent paths.
compute/tests/test_theorem_pva_classical_r_matrix_engine.py:660:        """sl_2 r-matrix verified via 3 independent paths.
compute/tests/test_penner_matrix_model_delta_f2_engine.py:3:Multi-path verification (AP10, CLAUDE.md mandate):
compute/tests/test_penner_matrix_model_delta_f2_engine.py:57:    """Power sums S_k verified by 3 independent methods."""
compute/tests/test_penner_matrix_model_delta_f2_engine.py:102:    """A_2(N) verified by 4 independent representations."""
compute/tests/test_penner_matrix_model_delta_f2_engine.py:152:    """B_2(N) verified by 2 independent representations + cross-engine."""
compute/tests/test_penner_matrix_model_delta_f2_engine.py:398:# X. Cross-family consistency (AP10 multi-path)
compute/tests/test_yangian_rmatrix_sl3.py:227:        """r(z) = Omega/z has a SINGLE pole at z = 0 (AP19)."""
 succeeded in 50ms:
compute/tests/test_theorem_sl3_yangian_r_matrix_engine.py
compute/tests/test_cohft_givental_rmatrix.py
compute/tests/test_yangian_rmatrix_arithmetic_engine.py
compute/tests/test_yangian_rmatrix_sl3.py
compute/tests/test_elliptic_rmatrix_shadow.py
compute/tests/test_penner_matrix_model_delta_f2_engine.py
compute/tests/test_rmatrix_comparison_c3.py
compute/tests/test_shadow_cohft_rmatrix_engine.py
compute/tests/test_quantum_rmatrix_barcomplex.py
compute/tests/test_theorem_pva_classical_r_matrix_engine.py
compute/tests/test_rmatrix_poles_comprehensive.py
compute/tests/test_prefundamental_rmatrix.py
compute/tests/test_rmatrix_landscape.py
compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py
compute/tests/test_theorem_three_way_r_matrix_engine.py



thinking
**Analyzing test execution**

I see that the test is still running, and it might be taking longer than expected. Maybe I can extend the `yield_time_ms` or check active processes to better understand what's happening. The user specifically requested to run the command, though, so I want to focus on that. I could also consider using `pytest --maxfail=1` if it keeps hanging. I need to determine the exact test files selected with `-k 'r_matrix or rmatrix'`, which might be numerous but manageable.
thinking
**Verifying test files**

The user wants me to read and verify a specific test file, likely related to the requested slice, which might involve checking multiple files. I think I should focus on the main AP126 test file, like `test_rmatrix_landscape.py`, and others such as `test_rmatrix_poles_comprehensive.py` and `test_theorem_pva_classical_r_matrix_engine.py`. The `-k` expression selects by any match of "r_matrix" or "rmatrix," so that could include quite a few files. The user specifically asks about the presence of level prefixes and hardcoded expected values. I'll need to inspect the relevant files carefully for these details.
thinking
**Counting instances**

I need to keep track of instances, and it sounds like using an update plan with specific steps would be helpful. I’ll think through how to add those steps effectively to ensure I can accurately count what I need. It could involve breaking down the process into manageable parts, allowing me to focus on each instance as it comes up. This way, I'll maintain clarity and stay organized while I work on this task.
Plan update
Focused audit surface: r-matrix/rmatrix compute tests, especially AP126/AP141 level-prefix coverage and AP10/AP128 hardcoded expected-value sourcing.
  → Capture the requested pytest slice result and identify the exact r-matrix test surface exercised by `-k 'r_matrix or rmatrix'`
  • Read the core r-matrix test files to verify whether affine/classical formulas carry an explicit level prefix and whether tests enforce `k=0 -> 0` where required
  • Audit hardcoded expected values in those test files for `# VERIFIED` comments with at least two independent source categories, then re-check surviving findings
codex
I’ve narrowed the scope to the actual `r_matrix`/`rmatrix` test modules instead of the whole repo. I’m now collecting the pytest selection explicitly so I can distinguish “tests exist” from “the requested slice really exercises AP126/AP141 and AP10/AP128.”
exec
/bin/zsh -lc "sed -n '960,1125p' compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'r_matrix or rmatrix' --collect-only -q | tail -120" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        assert fam.kappa == Fraction(1)

    def test_betagamma_weight_half(self):
        """betagamma at lambda=1/2: c = 2*(3/2 - 3 + 1) = -1."""
        fam = betagamma_rmatrix(Fraction(1, 2))
        expected_c = Fraction(2) * (Fraction(3, 2) - 3 + 1)
        assert fam.kappa == expected_c / 2

    def test_empty_ope(self):
        """Empty OPE -> empty r-matrix."""
        assert ope_to_rmatrix_poles({}) == {}

    def test_max_pole_order_empty(self):
        assert max_pole_order({}) == 0

    def test_max_pole_order_single(self):
        assert max_pole_order({3: 1}) == 3

    def test_permutation_operator_identity_property(self):
        """P^2 = I for the permutation operator."""
exec
/bin/zsh -lc "sed -n '1,240p' compute/tests/test_theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' compute/tests/test_rmatrix_poles_comprehensive.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
r"""Tests for PVA classical r-matrix extraction and KZ25 bridge.

THEOREM (KZ25 classical-quantum bridge):
The classical r-matrix extracted from the PVA lambda-bracket is the
genus-0 binary seed of the shadow obstruction tower:
    r^{cl}(z) = Res^{coll}_{0,2}(\Theta_A)|_{\hbar=0}

VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):

    Path 1 (PVA extraction):    lambda-bracket -> OPE modes -> r-matrix poles
    Path 2 (AP19 cross-check):  OPE poles -> d-log shift -> collision poles
    Path 3 (rmatrix_landscape): compare with existing collision-residue engine
    Path 4 (CYBE):              classical Yang-Baxter from Jacobi identity
    Path 5 (kappa consistency): scalar trace of r-matrix matches kappa(A)

All formulas computed from first principles (AP1, AP3).
AP44 divided-power convention verified at every step.
Cross-family consistency verified (AP10).

References:
 succeeded in 51ms:
r"""Comprehensive r-matrix pole order verification tests.

AP19 (the bar kernel absorbs a pole): the collision residue r(z) has
pole orders ONE LESS than the OPE.  The d log(z_1 - z_2) kernel in the
bar construction absorbs one power of (z-w).  This is the single most
error-prone formula in the manuscript.

The pole-shift rule:
  OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}
  In particular:
    z^{-1} in OPE  --->  z^0 in r-matrix (regular, drops out)

Consequences:
  - Heisenberg: OPE z^{-2}  --->  r-matrix z^{-1}.  r(z) = kappa/z.
  - Affine sl_N: OPE z^{-2}, z^{-1}  --->  r-matrix z^{-1} only.
    r(z) = k*Omega/z.  The simple pole (bracket term) in the OPE
    becomes regular and drops.
  - Virasoro: OPE z^{-4}, z^{-2}, z^{-1}  --->  r-matrix z^{-3}, z^{-1}.
    r(z) = (c/2)/z^3 + 2T/z.  No z^{-2} pole for a bosonic algebra.
  - W_3: WW OPE has z^{-6}, z^{-4}, z^{-3}, z^{-2}, z^{-1}

thinking
**Considering session results**

I recognize that I need to eventually collect session results. It might be easier to run a direct command with a smaller timeout since the current execution is likely slowing down due to the large amount of data being processed. Maybe if I poll again after a short period, I can get a better outcome. It's all about finding the right balance, and I’ll keep that in mind!

thinking
**Evaluating findings in code**

I need to gather specific findings with file references and descriptions. I wonder if I should use the explorer agent for this task, but maybe that's unnecessary. Still, it might be okay to proceed without it. I'll inspect `test_rmatrix_landscape.py` and focus on key assertions. I’ll also search for any VERIFIED comments as those could provide valuable insights. This approach should help me pinpoint the information I need!
codex
I’ve confirmed one core module already: `test_rmatrix_landscape.py` does enforce the AP126/AP141 mechanical boundary check and distinguishes `r|_{k=0}=0` from `\kappa(k=0)\neq 0` for affine KM. I’m now checking whether those assertions are actually source-backed per AP10/AP128, because passing tests alone would not satisfy the repo’s own oracle discipline.
exec
/bin/zsh -lc 'rg -n "VERIFIED|assert .*==|assert .*!=|Fraction'"\\(|k=0|AP126|AP141\" compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "VERIFIED|assert .*==|assert .*!=|Fraction'"\\(|k=0|AP126|AP141\" compute/tests/test_theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "VERIFIED|assert .*==|assert .*!=|Fraction'"\\(|k=0|AP126|AP141\" compute/tests/test_rmatrix_poles_comprehensive.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,260p' compute/tests/test_rmatrix_landscape.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:
74:        pva = heisenberg_pva(k=Fraction(3))
77:        assert bracket[1] == Fraction(3)
79:        assert bracket.get(0, Fraction(0)) == Fraction(0)
83:        pva = heisenberg_pva(k=Fraction(1))
84:        assert pva.max_pole_order("J", "J") == 2
88:        k = Fraction(5)
93:        assert ope_poles[2] == k  # OPE mode J_{(1)}J = 1! * k = k
97:        k = Fraction(7)
101:        assert coll == {1: k}
105:        pva = heisenberg_pva(k=Fraction(1))
107:        assert rmat.ope_max_pole("J", "J") == 2
108:        assert rmat.coll_max_pole("J", "J") == 1
117:        k = Fraction(3)
121:        assert bracket[0] == (Fraction(1), "h")
123:        assert bracket[1] == k
127:        k = Fraction(4)
130:        assert bracket[1] == 2 * k
134:        pva = affine_sl2_pva(k=Fraction(1))
136:        assert bracket[0] == (Fraction(2), "e")
140:        pva = affine_sl2_pva(k=Fraction(1))
 succeeded in 52ms:
65:        assert fam.channels["JJ"]["ope_max_pole"] == 2
69:        assert fam.channels["JJ"]["rmatrix_max_pole"] == 1
72:        k = Fraction(3)
74:        assert fam.channels["JJ"]["rmatrix_poles"][1] == k
78:        assert len(fam.channels["JJ"]["rmatrix_poles"]) == 1
90:        for k in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(7, 3)]:
92:            assert fam.kappa == k
96:        for k in [Fraction(1), Fraction(5), Fraction(-3, 2)]:
98:            assert fam.channels["JJ"]["rmatrix_poles"][1] == k
107:            assert fam.channels[f"{gen}{gen}"]["ope_max_pole"] == 2
110:        k = Fraction(2)
113:            assert fam.channels[f"{gen}{gen}"]["rmatrix_max_pole"] == 1
114:            assert fam.channels[f"{gen}{gen}"]["rmatrix_poles"][1] == k
121:                assert ch["rmatrix_max_pole"] == 0
122:                assert len(ch["rmatrix_poles"]) == 0
130:        for k in [Fraction(1), Fraction(3), Fraction(-1)]:
132:            expected = Fraction(3) * (k + 2) / Fraction(4)
133:            assert fam.kappa == expected
138:            affine_sl2_rmatrix(Fraction(-2))
143:        k = Fraction(5)
 succeeded in 51ms:
84:def heisenberg_ope_poles(kappa=Fraction(1)):
89:def affine_sl2_ope_poles(k=Fraction(1)):
101:def virasoro_ope_poles(c=Fraction(1)):
106:def w3_TT_ope_poles(c=Fraction(1)):
121:def w3_WW_ope_poles(c=Fraction(1)):
127:    beta = Fraction(16, 1) / (22 + 5 * c) if c != Fraction(-22, 5) else None
151:def affine_slN_ope_poles(k=Fraction(1), N=2):
173:        assert max_pole_order(poles) == 2
178:        assert max_pole_order(r_poles) == 1
182:        kappa = Fraction(1)
184:        assert r_poles[1] == kappa
188:        for k in [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(7, 3)]:
190:            assert r_poles[1] == k
201:        assert len(r_poles) == 1
212:        assert max_pole_order(poles['diagonal']) == 2
217:        assert max_pole_order(r_poles) == 1
222:        assert max_pole_order(poles['off_diagonal']) == 1
227:        assert len(r_poles) == 0
236:        for k in [Fraction(1), Fraction(2), Fraction(5)]:
238:            assert r_poles == {1: k}
 succeeded in 52ms:
r"""Tests for rmatrix_landscape.py: explicit r-matrices for 8 standard families.

AP19 verification (the bar kernel absorbs a pole):
  OPE pole z^{-n}  --->  r-matrix pole z^{-(n-1)}
  z^{-1} in OPE  --->  z^0 = regular, DROPS

Three verification axes:
  (A) AP19 pole orders for all 8 families
  (B) CYBE / infinitesimal braid relations for affine families
  (C) Skew-symmetry r_{12}(z) + r_{21}(-z) = 0 for Casimir-based families

Ground truth:
  - eq:virasoro-r-collision: r^Vir(z) = (c/2)/z^3 + 2T/z
  - prop:affine-r-mode: r^aff(z) = k*Omega/z
  - AP19 in CLAUDE.md
  - collision_residue_identification.py
  - test_rmatrix_poles_comprehensive.py
"""

from __future__ import annotations

thinking
**Considering output collection**

I need to inspect the collect-only output, but it might be too slow. Maybe I could use a faster command like `python3 -m pytest compute/tests/test_rmatrix_landscape.py ...`? However, the user requested a full slice, so I’m just waiting for that to complete. I think I should note if the command doesn’t finish in a reasonable time. Polling every 30 seconds could work well to manage this.
codex
The direct pytest slice has been running long enough that I’m treating runtime as part of the audit surface, not just noise. I’m checking whether it is still making progress or effectively hanging, while continuing the source audit so the report doesn’t depend on an unfinished build artifact.
exec
/bin/zsh -lc "sed -n '220,420p' compute/tests/test_theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '420,760p' compute/tests/test_theorem_pva_classical_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
        assert 1 in coll
        assert coll[1] == (Fraction(2), "T")
        # Pole 0 (from OPE pole 1, dT) should be ABSENT (drops)
        assert 0 not in coll

    def test_virasoro_ap19(self):
        """AP19: collision max pole 3 = OPE max pole 4 - 1."""
        pva = virasoro_pva(c=Fraction(1))
        rmat = PVAClassicalRMatrix(pva)
        assert rmat.ope_max_pole("T", "T") == 4
        assert rmat.coll_max_pole("T", "T") == 3
        assert rmat.verify_ap19()[("T", "T")] is True

    def test_virasoro_bosonic_parity(self):
        """Virasoro collision poles are all odd: {3, 1}."""
        pva = virasoro_pva(c=Fraction(1))
        result = verify_bosonic_parity(pva, "T")
        assert result['all_odd'] is True
        assert set(result['odd_poles']) == {1, 3}
        assert result['even_poles'] == []
 succeeded in 52ms:

class TestQuantumCorrections:
    """Verify quantum correction structure by shadow class."""

    def test_heisenberg_class_g(self):
        """Heisenberg is class G: no quantum corrections."""
        pva = heisenberg_pva(k=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'G'
        assert qc['shadow_depth'] == 2
        assert qc['quantum_corrections'] is False

    def test_sl2_class_l(self):
        """Affine sl_2 is class L: no corrections at tree level."""
        pva = affine_sl2_pva(k=Fraction(1))
        qc = quantum_correction_class(pva)
        assert qc['class'] == 'L'
        assert qc['shadow_depth'] == 3
        assert qc['quantum_corrections_tree'] is False

exec
/bin/zsh -lc "rg -n \"VERIFIED|assert .*==|Fraction\\(|k=0|AP126|AP141\" compute/tests/test_theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"VERIFIED|assert .*==|Fraction\\(|k=0|AP126|AP141\" compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '520,565p' compute/tests/test_theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '720,815p' compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
84:        r = RMatrixFromBar.heisenberg(Fraction(1))
85:        assert r == {1: Fraction(1)}
89:        r = RMatrixFromPVA.heisenberg(Fraction(1))
90:        assert r == {1: Fraction(1)}
94:        r = RMatrixFromDNP.heisenberg(Fraction(1))
95:        assert r == {1: Fraction(1)}
99:        r = RMatrixFromGZ26.heisenberg(Fraction(1))
100:        assert r == {1: Fraction(1)}
119:        r = RMatrixFromBar.heisenberg(Fraction(3))
120:        assert set(r.keys()) == {1}
124:        for k in [1, 2, 3, -1, Fraction(1, 2)]:
125:            r = RMatrixFromBar.heisenberg(Fraction(k))
126:            assert r[1] == Fraction(k)
138:        r = RMatrixFromBar.affine_sl2(Fraction(1))
139:        assert r == {1: Fraction(1, 3)}
143:        r = RMatrixFromPVA.affine_sl2(Fraction(1))
144:        assert r == {1: Fraction(1, 3)}
148:        r = RMatrixFromDNP.affine_sl2(Fraction(1))
149:        assert r == {1: Fraction(1, 3)}
153:        r = RMatrixFromGZ26.affine_sl2(Fraction(1))
 succeeded in 50ms:
        )

    def test_leading_order_heisenberg(self):
        """Leading-order matching for Heisenberg: bar = PVA."""
        result = verify_leading_order_matching('heisenberg', {'k': 1})
        assert result['match']

    def test_leading_order_sl2(self):
        """Leading-order matching for sl_2: bar = PVA."""
        result = verify_leading_order_matching('sl2', {'k': 1})
        assert result['match']

    def test_leading_order_virasoro(self):
        """Leading-order matching for Virasoro: bar = PVA."""
        result = verify_leading_order_matching('virasoro', {'c': 1})
        assert result['match']

    def test_kappa_heisenberg_consistency(self):
        """kappa(H_k) = k: the r-matrix coefficient equals kappa for Heisenberg."""
        for k in [1, 2, 3]:
 succeeded in 51ms:
72:        assert set(ope.keys()) == {4, 2, 1}
73:        assert ope[4] == F(13)  # c/2 = 26/2 = 13
74:        assert ope[2] == F(2)
75:        assert ope[1] == F(1)
81:        assert set(rpoles.keys()) == {3, 1}
82:        assert rpoles[3] == F(13)  # c/2
83:        assert rpoles[1] == F(2)
89:        assert len(rmat) == 0  # All regular, nothing survives
113:        assert rpoles[3] == F(0)  # c/2 = 0
114:        assert rpoles[1] == F(2)  # 2T always present
130:                assert r0 == 2 * h1
136:        assert r2 == c_val / 2
140:        assert rmatrix_mode_r1_primary() == F(0)
148:        assert r0_c1 == r0_c26 == F(6)
156:        assert trace["r0_trace"] == 2 * h1
158:        assert trace["r2_trace"] == c_val / 2
160:        assert trace["r1_trace"] == F(0)
174:        assert coeffs[0] == F(1)
180:        assert coeffs[2] == -F(26, 4)
186:        assert coeffs[2] == -F(1, 4)
 succeeded in 52ms:


# =========================================================================
# 13. Pole-order cross-checks with rmatrix_landscape
# =========================================================================

class TestPoleOrderCrossCheck:
    """Cross-check r-matrix poles against rmatrix_landscape.py.

    Multi-path verification:
      Path 1: virasoro_rmatrix_poles (this engine)
      Path 2: ap19_pole_shift applied to ope_poles
      Path 3: manual computation from OPE
    """

    def test_three_path_pole_structure(self):
        """r-matrix poles verified 3 ways."""
        c = F(26)

        # Path 1: direct
exec
/bin/zsh -lc "sed -n '815,850p' compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        kappa_check = kappa_from_rmatrix(c)
        kappa_3 = kappa_check["kappa_shadow"]

        # Path 4: Sugawara
        kappa_4 = kappa_check["kappa_sugawara"]

        # Path 5: direct definition
        kappa_5 = c / 2

        assert kappa_1 == kappa_2 == kappa_3 == kappa_4 == kappa_5 == F(13)

    def test_exponential_convergence(self):
        """R-matrix series converges for |z| > 0.

        The series R(z) = z^{2h1} * sum_k (-c/4)^k/(k! z^{2k})
        converges absolutely for all z != 0 (entire function of 1/z^2).
        We use a running-product approach to avoid factorial overflow.
        """
        c_val = 26.0
        h1_val = 2.0
codex
The AP10/AP128 picture is getting clearer: several r-matrix test modules state “3 paths” in prose, but that is not the required `# VERIFIED` annotation with source-category tags. I’m checking whether there are any actual compliant examples in the same audit slice, so the report can distinguish missing discipline from mere stylistic variation.
exec
/bin/zsh -lc "sed -n '438,472p' compute/tests/test_w_infinity_chiral_qg_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '40,70p' compute/tests/test_entanglement_shadow_spectrum_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
        """AP19 d-log absorption: pole_r = pole_OPE - 1 at all spins."""
        for spin, method in [(1, self.mo.r_matrix_spin1),
                             (2, self.mo.r_matrix_spin2),
                             (3, self.mo.r_matrix_spin3)]:
            r = method()
            assert r["pole_order"] == r["ope_pole_order"] - 1, (
                f"AP19 fails at spin {spin}"
            )

    def test_spin1_k_zero_vanishes(self):
        r"""At k=0, r_1(z) = 0 (AP126 boundary check).

        # VERIFIED: [DC] k/z at k=0 = 0;
        #           [SY] abelian limit symmetry.
        """
        r = self.mo.r_matrix_spin1()
        assert r["k_zero_check"] == 0

    def test_spin1_k_zero_explicit(self):
        """Construct r-matrix at k=0 and verify vanishing."""
 succeeded in 52ms:
    (Fraction(0), Fraction(-2), Fraction(2)),
    # VERIFIED: [DC] direct substitution at lambda=0; [SY] c_bg=-c_bc by polynomial identity.
    (Fraction(1, 2), Fraction(1), Fraction(-1)),
    # VERIFIED: [DC] lambda=1/2 gives c_bc=1 and c_bg=-1; [LC] free fermion / symplectic boson normalization.
    (Fraction(1), Fraction(-2), Fraction(2)),
    # VERIFIED: [DC] lambda=1 gives c_bc=-2 and c_bg=2; [SY] ghost complementarity.
    (Fraction(3, 2), Fraction(-11), Fraction(11)),
    # VERIFIED: [DC] lambda=3/2 gives c_bc=-11 and c_bg=11; [SY] exact cancellation.
    (Fraction(2), Fraction(-26), Fraction(26)),
    # VERIFIED: [DC] lambda=2 gives reparametrization-ghost values; [LT] standard bc/betagamma cancellation.
]


AFFINE_ZERO_LEVEL_CASES = [
    ("sl_2", Fraction(3, 2)),
    # VERIFIED: [DC] dim(sl_2)/2=3/2 at k=0; [LT] CLAUDE C3 zero-level check.
    ("sl_3", Fraction(4, 1)),
    # VERIFIED: [DC] dim(sl_3)/2=8/2=4; [LT] affine KM census formula.
    ("e_8", Fraction(124, 1)),
    # VERIFIED: [DC] dim(E_8)/2=248/2=124; [LT] E_8 adjoint dimension 248.
exec
/bin/zsh -lc 'rg -n "# VERIFIED:|VERIFIED:" compute/tests/test_*r_matrix* compute/tests/*rmatrix* compute/tests/test_w_infinity_chiral_qg_engine.py 2>/dev/null' in /Users/raeez/chiral-bar-cobar succeeded in 59ms:
compute/tests/test_w_infinity_chiral_qg_engine.py:67:        # VERIFIED: [DC] direct from OPE J(z)J(w) ~ k/(z-w)^2;
compute/tests/test_w_infinity_chiral_qg_engine.py:88:        # VERIFIED: [DC] 6 * (25/12) = 25/2;
compute/tests/test_w_infinity_chiral_qg_engine.py:138:        # VERIFIED: [DC] Zamolodchikov 1985 OPE: W(z)W(w) ~ (c/3)/(z-w)^6;
compute/tests/test_w_infinity_chiral_qg_engine.py:157:        # VERIFIED: [DC] 32/(22+5*25) = 32/147;
compute/tests/test_w_infinity_chiral_qg_engine.py:235:        # VERIFIED: [DC] T_{(3)}T = c/2 from OPE;
compute/tests/test_w_infinity_chiral_qg_engine.py:266:        # VERIFIED: [DC] direct from OPE;
compute/tests/test_w_infinity_chiral_qg_engine.py:351:        # VERIFIED: [DC] 6 * 25/12 = 25/2;
compute/tests/test_w_infinity_chiral_qg_engine.py:450:        # VERIFIED: [DC] k/z at k=0 = 0;
compute/tests/test_w_infinity_chiral_qg_engine.py:540:        # VERIFIED: [DC] recursion p(n) = sum_{k=1}^{n} p(n-k);
compute/tests/test_w_infinity_chiral_qg_engine.py:584:        # VERIFIED: [DC] k=1 -> 1; [LT] C1 census.
compute/tests/test_w_infinity_chiral_qg_engine.py:602:        # VERIFIED: [DC] c/2 = 25/2; [LT] C2 census.
compute/tests/test_w_infinity_chiral_qg_engine.py:613:        # VERIFIED: [DC] 13/2; [SY] self-dual c=13.
compute/tests/test_w_infinity_chiral_qg_engine.py:624:        # VERIFIED: [DC] H_2 = 1 + 1/2 = 3/2, H_2 - 1 = 1/2;
compute/tests/test_w_infinity_chiral_qg_engine.py:636:        # VERIFIED: [DC] 25 * 5/6 = 125/6;
compute/tests/test_w_infinity_chiral_qg_engine.py:655:        # VERIFIED: [DC] H_2 - 1 = 1/2 vs H_1 = 1;
compute/tests/test_w_infinity_chiral_qg_engine.py:685:        # VERIFIED: [DC] direct summation H_N = sum 1/j;
compute/tests/test_w_infinity_chiral_qg_engine.py:861:        # VERIFIED: [DC] direct from OPE; [LT] C10; [LC] Psi=0 -> 0.
compute/tests/test_w_infinity_chiral_qg_engine.py:916:        # VERIFIED: [DC] Sugawara c=1 for rank-1; [LT] Kac VA book ch 3.
compute/tests/test_w_infinity_chiral_qg_engine.py:947:        # VERIFIED: [DC] expanding (1/(2*Psi)):Delta(J)^2:; [LC] Psi->inf -> 0.
compute/tests/test_w_infinity_chiral_qg_engine.py:975:        # VERIFIED: [DC] mode-3 = c/2 = 1/2; [CF] matches Virasoro at c=1.
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py -q --tb=short 2>&1 | tail -40' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '56,110p' compute/tests/test_w_infinity_chiral_qg_engine.py
sed -n '576,640p' compute/tests/test_w_infinity_chiral_qg_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 50ms:

    # --- Heisenberg JJ ---

    def test_jj_mode_0_vanishes(self):
        """J_{(0)}J = 0 (no simple pole in JJ OPE for abelian algebra)."""
        coeffs = self.ope.ope_JJ()
        assert coeffs[0] == 0

    def test_jj_mode_1_equals_k(self):
        r"""J_{(1)}J = k (double pole coefficient).

        # VERIFIED: [DC] direct from OPE J(z)J(w) ~ k/(z-w)^2;
        #           [LT] Kac, Vertex Algebras for Beginners, eq. 2.4.
        """
        coeffs = self.ope.ope_JJ()
        assert coeffs[1] == Rational(1)  # k=1

    def test_jj_k_zero_vanishes(self):
        """At k=0 all JJ OPE coefficients vanish (AP126 boundary check)."""
        ope_k0 = OPEData(c=Rational(25), k=Rational(0))
 succeeded in 9.97s:
........................................................................ [ 20%]
........................................................................ [ 40%]
........................................................................ [ 61%]
........................................................................ [ 81%]
................................................................         [100%]
352 passed in 6.94s
 succeeded in 2m 00s:
compute/tests/test_yangian_rmatrix_arithmetic_engine.py::TestStress::test_root_of_unity_eigenvalues[17]
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_bracket_consistency
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_killing_form_consistency
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_dimension
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_tracelessness
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_E3_is_bracket
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_F3_is_bracket
compute/tests/test_yangian_rmatrix_sl3.py::TestFundamentalRep::test_cartan_eigenvalues
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_casimir_identity_omega_eq_p_minus_i_over_n
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_casimir_scalar_fund
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_casimir_scalar_matrix
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_killing_form_symmetric
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_killing_form_nondegenerate
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_dual_basis_pairing
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_omega_eigenvalues
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_permutation_squared_is_identity
compute/tests/test_yangian_rmatrix_sl3.py::TestCasimir::test_permutation_eigenvalues
compute/tests/test_yangian_rmatrix_sl3.py::TestRMatrixPoleStructure::test_single_pole
compute/tests/test_yangian_rmatrix_sl3.py::TestRMatrixPoleStructure::test_residue_is_omega
compute/tests/test_yangian_rmatrix_sl3.py::TestRMatrixPoleStructure::test_ope_pole_orders_vs_rmatrix


thinking
**Evaluating test command options**

Alright, I've got a subset of core files that passed, but I still need to get the exact full slice. I could run it with a timeout, but the original broad slice might take a while due to multiple tests. I wonder if I should try running `pytest -q -k ...` again and just wait, as it might take minutes. The user requested the exact run, so I could mention it was still running by the audit cutoff. Alternatively, I could explore running the command again with a yield time setting to help?
thinking
**Deciding on command execution**

I've already executed the exact command, but it didn't return within the expected time, suggesting it might be too large or hanging. I wonder if I should run it in a new shell with a timeout of 120 seconds. However, the user didn't specifically request that. If it times out, we might only get a partial result. I could try running the command without `tail` to capture the final output and show progress without waiting for EOF, while also mentioning the original command is still running. Is that acceptable?
codex
The four core r-matrix modules pass cleanly in isolation, so I’ve ruled out an obvious local regression there. I’m now re-running the full requested keyword slice without the `tail` pipe so I can actually observe completion; the exact piped command is still not returning promptly.
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'r_matrix or rmatrix' --tb=short -q" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '130,185p' compute/tests/test_theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,120p' compute/tests/test_theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_pva_classical_r_matrix_engine.py | sed -n '456,706p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_rmatrix_landscape.py | sed -n '1010,1108p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
# Section 2: sl_2 KM family -- four-perspective agreement
# ============================================================

class TestSl2KMRMatrix:
    """Four-perspective cross-check for sl_2 r(z) = Omega/((k+2)z)."""

    def test_sl2_bar_k1(self):
        """Bar collision residue at level k=1: prefactor = 1/(1+2) = 1/3."""
        r = RMatrixFromBar.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_pva_k1(self):
        """PVA lambda-bracket at level k=1: prefactor = 1/3."""
        r = RMatrixFromPVA.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}

    def test_sl2_dnp_k1(self):
        """DNP MC element at level k=1: prefactor = 1/3."""
        r = RMatrixFromDNP.affine_sl2(Fraction(1))
        assert r == {1: Fraction(1, 3)}
 succeeded in 52ms:
r"""Tests for the three-way r-matrix cross-check engine.

Verifies that the collision residue r(z) = Res^{coll}_{0,2}(Theta_A) agrees
across four independent perspectives:

  (1) BAR collision residue (our framework)
  (2) PVA lambda-bracket (KZ25 / Gui-Li-Zeng)
  (3) DNP25 MC element (dg-shifted Yangian)
  (4) GZ26 commuting Hamiltonians

Test organization:
  Section 1: Heisenberg family (4 perspectives x 3 levels = 12 comparisons)
  Section 2: sl_2 KM family (4 perspectives x 3 levels)
  Section 3: Virasoro family (4 perspectives x 3 central charges)
  Section 4: Virasoro on primary states
  Section 5: W_3 multi-channel structure
  Section 6: Structural properties (antisymmetry, CYBE, pole structure)
  Section 7: AP19 verification (d log absorption, pole orders)
  Section 8: AP44 verification (PVA divided-power convention)
  Section 9: Numerical checks (IBR, KZ commutativity)
 succeeded in 51ms:
   456	# ========================================================================
   457	# Section 6: Kappa consistency
   458	# ========================================================================
   459	
   460	class TestKappaConsistency:
   461	    """Verify kappa(A) extracted from PVA matches known values."""
   462	
   463	    def test_kappa_heisenberg(self):
   464	        """kappa(H_k) = k."""
   465	        for k_val in [1, 3, 7, Fraction(1, 2)]:
   466	            pva = heisenberg_pva(k=Fraction(k_val))
   467	            assert kappa_from_pva(pva) == Fraction(k_val)
   468	
   469	    def test_kappa_virasoro(self):
   470	        """kappa(Vir_c) = c/2."""
   471	        for c_val in [1, 12, 26, Fraction(1, 2)]:
   472	            pva = virasoro_pva(c=Fraction(c_val))
   473	            assert kappa_from_pva(pva) == Fraction(c_val) / 2
   474	
   475	    def test_kappa_sl2(self):
 succeeded in 51ms:
  1010	# Pairs with: AP126 in CLAUDE.md, AP141 in CLAUDE.md, holographic_datum
  1011	# _master.tex Face 5, genus1_seven_faces.tex collision residues.
  1012	
  1013	class TestAP126AbelianLimit:
  1014	    """Every level-bearing classical r-matrix must vanish at k = 0."""
  1015	
  1016	    def test_heisenberg_k_zero(self):
  1017	        """r^Heis(z) = k/z must vanish at k=0 (AP141)."""
  1018	        fam = heisenberg_rmatrix(Fraction(0))
  1019	        # The single OPE pole has coefficient 0; after AP19 absorption
  1020	        # the resulting r-matrix has no nonzero poles.
  1021	        assert fam.channels["JJ"]["rmatrix_poles"] == {}, (
  1022	            "Heisenberg r(z) = k/z must vanish at k=0; AP126 violation"
  1023	        )
  1024	
  1025	    def test_heisenberg_k_zero_kappa(self):
  1026	        """kappa(H_0) = 0 (Heisenberg at level 0 has trivial kappa)."""
  1027	        fam = heisenberg_rmatrix(Fraction(0))
  1028	        assert fam.kappa == Fraction(0)
  1029	
exec
/bin/zsh -lc "rg -n \"KZ|k\\+2|Omega/\\(\\(k\\+2\\)z\\)|trace-form|convention\" compute/tests/test_theorem_three_way_r_matrix_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
7:  (2) PVA lambda-bracket (KZ25 / Gui-Li-Zeng)
19:  Section 8: AP44 verification (PVA divided-power convention)
20:  Section 9: Numerical checks (IBR, KZ commutativity)
29:  Path 4: Numerical verification (sl_2 Casimir, KZ Hamiltonians)
30:  Path 5: AP19/AP44 convention checks
36:  - AP19 (pole absorption), AP44 (divided-power convention)
134:    """Four-perspective cross-check for sl_2 r(z) = Omega/((k+2)z)."""
427:# Section 8: AP44 verification (PVA divided-power convention)
463:# Section 9: Numerical checks (IBR and KZ commutativity)
467:    """Numerical verification of CYBE and KZ commutativity."""
488:        """KZ Hamiltonians commute at 3 points, k=1."""
493:        """KZ Hamiltonians commute at 4 points, k=1."""
498:        """KZ Hamiltonians commute at 3 points, k=2."""
503:        """KZ Hamiltonians commute at 4 points, k=3."""
codex
I’ve reached the second-order issue the user asked for: not whether the tests have mathematics in them, but whether the expected values are independently sourced. The slice contains both patterns: one file with proper `# VERIFIED` tags and several others that hardcode values without the required source annotations, which means the oracle discipline is drifting inside the same audit surface.
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_three_way_r_matrix_engine.py | sed -n '132,180p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_w_infinity_chiral_qg_engine.py | sed -n '444,456p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py | sed -n '736,829p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED:|VERIFIED:" compute/tests/test_rmatrix_landscape.py compute/tests/test_theorem_pva_classical_r_matrix_engine.py compute/tests/test_theorem_three_way_r_matrix_engine.py compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   132	
   133	class TestSl2KMRMatrix:
   134	    """Four-perspective cross-check for sl_2 r(z) = Omega/((k+2)z)."""
   135	
   136	    def test_sl2_bar_k1(self):
   137	        """Bar collision residue at level k=1: prefactor = 1/(1+2) = 1/3."""
   138	        r = RMatrixFromBar.affine_sl2(Fraction(1))
   139	        assert r == {1: Fraction(1, 3)}
   140	
   141	    def test_sl2_pva_k1(self):
   142	        """PVA lambda-bracket at level k=1: prefactor = 1/3."""
   143	        r = RMatrixFromPVA.affine_sl2(Fraction(1))
   144	        assert r == {1: Fraction(1, 3)}
   145	
   146	    def test_sl2_dnp_k1(self):
   147	        """DNP MC element at level k=1: prefactor = 1/3."""
   148	        r = RMatrixFromDNP.affine_sl2(Fraction(1))
   149	        assert r == {1: Fraction(1, 3)}
   150	
   151	    def test_sl2_gz26_k1(self):
 succeeded in 52ms:
   444	                f"AP19 fails at spin {spin}"
   445	            )
   446	
   447	    def test_spin1_k_zero_vanishes(self):
   448	        r"""At k=0, r_1(z) = 0 (AP126 boundary check).
   449	
   450	        # VERIFIED: [DC] k/z at k=0 = 0;
   451	        #           [SY] abelian limit symmetry.
   452	        """
   453	        r = self.mo.r_matrix_spin1()
   454	        assert r["k_zero_check"] == 0
   455	
   456	    def test_spin1_k_zero_explicit(self):
 succeeded in 51ms:
   736	        """r-matrix poles verified 3 ways."""
   737	        c = F(26)
   738	
   739	        # Path 1: direct
   740	        rpoles = virasoro_rmatrix_poles(c)
   741	
   742	        # Path 2: AP19 applied
   743	        ope = virasoro_ope_poles(c)
   744	        rpoles_ap19 = ap19_pole_shift(ope)
   745	
   746	        # Path 3: manual
   747	        # OPE: z^{-4} -> z^{-3} (coeff c/2 = 13)
   748	        #       z^{-2} -> z^{-1} (coeff 2)
   749	        #       z^{-1} -> z^0 = drops
   750	        rpoles_manual = {3: F(13), 1: F(2)}
   751	
   752	        assert rpoles == rpoles_ap19
   753	        assert rpoles == rpoles_manual
   754	
   755	    def test_max_pole_orders(self):
 exited 1 in 52ms:


thinking
**Searching for comments**

I saw there are no verified comments in the four files, which is good! Now, I’m thinking about searching through more selected files, just in case there are some compliant ones. It seems like w_infinity already has what I need. I’m wondering if that search is necessary after all. I might need to poll the full slice for session 46269. That could clarify things!

thinking
**Evaluating output handling**

It looks like I'm outputting a dot, which is a good sign! I need to run some checks or processes, and I might have to poll more information. I'm thinking maybe the data set is big but still finite, which gives me a clear target to work with. I just need to keep things organized and make sure everything runs smoothly. Let's keep moving forward with this!

thinking
**Polling for results**

I’m considering how many tests we need to run and if we should keep polling later. It seems like we might need a final summary with an exact count, but maybe I can get away with just polling longer. Using 20 seconds between polls sounds reasonable for gathering better data. I'm curious if that'll be enough to get a clearer picture of the situation!
codex
The full keyword slice is not hanging outright; it is just much larger than the core subset. While that runs, I’ve confirmed the key structural split already: `test_rmatrix_landscape.py` enforces trace-form AP126 vanishing, but other selected files encode different normalizations and often do so without the mandated `# VERIFIED` source tags.





thinking
**Evaluating test inconsistencies**

I’m considering around 1200 tests that might take about 6-7 minutes. I need to inspect the early lines in `test_rmatrix_landscape`, especially concerning the kappa formulas. I wonder if using rg might help since there are no verified comments yet. I need to assess severity levels, like whether a wrong expectation due to inconsistent normalization could be critical. If there’s a convention difference between KZ and trace-form, it could indicate a slice inconsistency. The user wants to check for specific findings too.
thinking
**Examining file discrepancies**

I’m thinking about checking whether another file uses KZ without a boundary check at k=0, like in `theorem_three_way`. I didn't find anything there, but I noticed that lines 171-176 might expect 1/(k+2) without mentioning the AP126 trace-form or bridge. Since a selected slice includes `test_rmatrix_landscape.py`, this discrepancy could cause an engine test suite to pass despite a k-prefactor bug. While it might not be mathematically incorrect to use KZ, I need to clarify that the k=0→0 point applies only to trace-form files.
thinking
**Assessing normalization discrepancies**

I’m considering assigning a severity level of [MEDIUM] because the selected test surface mixes two normalizations without a clear convention bridge in the test file. Specifically, I'm looking at lines 134-176. Not having an explicit bridge could lead to confusion, and it's vital to note how this impacts the overall integrity of the tests. I need to ensure the user understands the implications of this situation!
thinking
**Evaluating documentation inconsistencies**

It looks like there's a really confusing boundary check due to the AP126 boundary being used elsewhere. This could lead to contradictory answers unless someone figures out the convention switches. I think the discrepancy is significant because convention drift can obscure bugs, so maybe it's a high severity issue. I'll need to inspect different tests related to `kappa_affine_sl2` and others to see if they intentionally use different conventions or if this is a more pressing problem.
thinking
**Summarizing violation instances**

I’m thinking that for my final summary or note, I might not need to go in-depth but should mention that the AP10 style appears elsewhere. I should gather counts of instances checked and violations found, possibly totaling around 6 or 7. I'll list the files inspected, including the requested pytest commands and any focused subsets. I could report, “Instances checked: 6 | Violations found: 4,” but I should ensure it meets the user’s expectations.





thinking
**Identifying discrepancies**

I see there's a discrepancy here, and it might be considered significant, particularly because within the same keyword slice, I'm noticing some contradictory convention surfaces. I'm trying to unpack this properly to understand what it means for my conclusions. I want to be careful and precise about how I interpret these conventions, as they could affect the overall clarity of the task. Let's explore this in more detail!
thinking
**Summarizing key elements**

I think I should mention that the level prefix and k=0→0 are checked, as they are important for the user's question. Maybe I could note this in the summary. I might say something like, "The level prefix and k=0→0 are discussed in `test_rmatrix_landscape.py` and `test_w_infinity_chiral_qg_engine.py`." However, I want to ensure the summary remains concise and to the point, so I’ll keep it brief while still providing necessary details.
thinking
**Considering summary and findings**

I'm thinking about how to present the findings, perhaps ordering them by severity. A brief note before the summary seems acceptable, but I want to minimize extraneous information. It might be useful to wait a bit longer for a complete overview, but I'm unsure about the worth of that wait. I could consider stopping the session since the user doesn’t see the command output, but it seems like I should mention that things are incomplete.
thinking
**Organizing severity levels**

I’m looking at severity ordering for some items. The first is a high severity for the theorem_three_way convention drift since it impacts the level-prefix / k=0 audit. Next, I see the theorem_pva classical file with missing `# VERIFIED` tags despite claiming multi-path, which I also flag as high severity. Then, I've got two medium severity issues: the virasoro_spectral with no `# VERIFIED` tags, and the rmatrix_landscape AP126 block, which has good boundary checks but lacks source tags. I need to check a specific test file too.
thinking
**Combining findings for strength**

I’m considering how to strengthen my findings by combining issues like convention drift with missing source tags. For example, lines 134 and 171 show a hardcoded KZ prefactor without a convention bridge or AP10 source tags, which is high severity. Line 460 of theorem_pva includes kappa formulas without `# VERIFIED` tags, even though the file header claims there are "VERIFICATION PATHS (3+ per claim)." I need to get those specific line numbers from the top to support this.
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_pva_classical_r_matrix_engine.py | sed -n '1,30p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	r"""Tests for PVA classical r-matrix extraction and KZ25 bridge.
     2	
     3	THEOREM (KZ25 classical-quantum bridge):
     4	The classical r-matrix extracted from the PVA lambda-bracket is the
     5	genus-0 binary seed of the shadow obstruction tower:
     6	    r^{cl}(z) = Res^{coll}_{0,2}(\Theta_A)|_{\hbar=0}
     7	
     8	VERIFICATION PATHS (3+ per claim, per CLAUDE.md multi-path mandate):
     9	
    10	    Path 1 (PVA extraction):    lambda-bracket -> OPE modes -> r-matrix poles
    11	    Path 2 (AP19 cross-check):  OPE poles -> d-log shift -> collision poles
    12	    Path 3 (rmatrix_landscape): compare with existing collision-residue engine
    13	    Path 4 (CYBE):              classical Yang-Baxter from Jacobi identity
    14	    Path 5 (kappa consistency): scalar trace of r-matrix matches kappa(A)
    15	
    16	All formulas computed from first principles (AP1, AP3).
    17	AP44 divided-power convention verified at every step.
    18	Cross-family consistency verified (AP10).
    19	
    20	References:





thinking
**Assessing file comments and structure**

I'm noticing a significant issue with the lack of `# VERIFIED` comments throughout, especially given how formulaic this file is. I should check if `test_rmatrix_landscape.py` line 1025 has one. Also, I might categorize `theorem_virasoro_spectral` as medium priority since it's more secondary and uses multi-path docstrings without source tags. Another candidate for medium could be `test_rmatrix_landscape`. I need to mention that the full command is lengthy but could omit it since it’s file-less. The user asked about the level prefix and boundary enforcement, so I'll summarize those findings.
thinking
**Evaluating findings and conventions**

I'm checking for non-uniform conditions and labeling this as inference, which feels good. It’s important to mention that there wasn’t an outright failure for AP126 in `test_rmatrix_landscape.py`, as that avoids false positives. Now, the user asked about checking the level prefix presence, so if k=0→0 is accurate, the absence of a convention could signify a drift. I’m also noting how the hardcoded expected values may yield 3-4 findings. I need to answer these points clearly!
thinking
**Summarizing findings and severity levels**

I could summarize that trace-form AP126 coverage is present in `test_rmatrix_landscape.py` and `test_w_infinity_chiral_qg_engine.py`. However, in `test_theorem_three_way_r_matrix_engine.py`, the KZ normalization affects the flow so that k=0 doesn’t lead to 0. This might not require a separate finding if there's no violation, but I could categorize it as a [MEDIUM] finding due to mixed normalization. The user’s audit concerns this discrepancy, which feels justifiable. I'll also highlight other findings about AP10 absence and source tag issues with appropriate severity levels. Overall, that gives four findings.
thinking
**Assessing finding severity levels**

I’m thinking about the theorem_virasoro finding, which claims three and five independent paths while hardcoding constants. I could rate this as [HIGH], but I’m also considering if it might align more with [MEDIUM]. There’s a risk that the engine and test could create a wrong mental model, which feels significant. In this case, maybe I should go with three findings rated as [HIGH] and one as [MEDIUM]. I don’t think any criticals are present.
thinking
**Updating the plan**

I'm considering whether I should finalize the plan after extended polling. It seems like marking it as completed might be an option, but I'm not totally sure if it's necessary. Maybe it's a good idea to update the plan before we wrap things up. I think since we've made enough progress, it could be worthwhile to take that step. Let's just make sure everything feels in order before we call it done!
Plan update
The relevant r-matrix test surface has been read directly, a focused subset was executed, and surviving findings were re-checked against file contents. The only incomplete artifact is the exact full-slice piped pytest command, which was still progressing after extended polling.
  ✓ Capture the requested pytest slice result and identify the exact r-matrix test surface exercised by `-k 'r_matrix or rmatrix'`
  ✓ Read the core r-matrix test files to verify whether affine/classical formulas carry an explicit level prefix and whether tests enforce `k=0 -> 0` where required
  ✓ Audit hardcoded expected values in those test files for `# VERIFIED` comments with at least two independent source categories, then re-check surviving findings
codex
- [HIGH] [compute/tests/test_theorem_pva_classical_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:8) — The header claims “3+ per claim” and “Cross-family consistency verified (AP10)”, but the hardcoded expected values later in the file, including `3(k+2)/4`, `c/2`, and `c/3` ([lines 475](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:475), [485](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:485), [699](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_pva_classical_r_matrix_engine.py:699)), have no `# VERIFIED` comments at all. A grep over this file returned zero `# VERIFIED` hits, so AP10/AP128 is not actually enforced on this surface.
- [HIGH] [compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:736) — The file hardcodes manual oracle data such as `rpoles_manual = {3: F(13), 1: F(2)}`, `R2_path3 = -c/4`, and `kappa_5 = c/2` ([lines 750](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:750), [792](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:792), [822](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_virasoro_spectral_r_matrix_engine.py:822)) under “verified 3 ways / 5 ways”, but the file also has zero `# VERIFIED` annotations. The expected values are present; the required two-source audit trail is not.
- [MEDIUM] [compute/tests/test_theorem_three_way_r_matrix_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:134) — This selected `r_matrix` test file hardcodes the affine `sl_2` residue as `\Omega/((k+2)z)` and expects `1/(k+2)` at [line 175](/Users/raeez/chiral-bar-cobar/compute/tests/test_theorem_three_way_r_matrix_engine.py:175). Inference: the keyword slice therefore mixes KZ normalization here with the trace-form AP126 surface in `test_rmatrix_landscape.py`, so the user’s requested `k=0→0` check is not uniform across the selected tests. This file also has zero `# VERIFIED` tags.
- [MEDIUM] [compute/tests/test_rmatrix_landscape.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1013) — This file does enforce the trace-form AP126 boundary check: `r^{aff sl_2}(z)=k\Omega/z` and `k=0→0` are tested directly at [lines 1030](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1030) and [1050](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1050). But the same block hardcodes zero-level kappa expectations `0`, `3/2`, and `4` at [lines 1103](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1103)-[1105](/Users/raeez/chiral-bar-cobar/compute/tests/test_rmatrix_landscape.py:1105) with no `# VERIFIED` provenance, and grep found no `# VERIFIED` markers anywhere in the file.

Control/build note: [compute/tests/test_w_infinity_chiral_qg_engine.py](/Users/raeez/chiral-bar-cobar/compute/tests/test_w_infinity_chiral_qg_engine.py:447) contains a compliant `# VERIFIED: [DC] ... [SY] ...` annotation, so the missing-source findings above are real deviations, not a repo-wide absence of the pattern. A focused subset of four core files passed (`352 passed in 6.94s`); the exact full piped command was started, but it was still progressing after extended polling, so I do not have its final tail output.

## Summary
Instances checked: 6 | Violations found: 4 | Verdict: FAIL
tokens used
95,570
