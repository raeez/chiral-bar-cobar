# CE08_stokes (492s, gpt-5.4)

[CRITICAL] [compute/lib/resurgence_frontier_engine.py:345](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:345) — The shadow series is classified here as Gevrey-0, so with the module’s own definition `B[G](xi)=sum S_r xi^r/r!` the Borel transform is entire. The same pipeline later treats class `M` as having finite Borel singularities and nontrivial Stokes data at `1/branch_\pm` ([compute/lib/resurgence_frontier_engine.py:1092](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1092), [compute/lib/resurgence_frontier_engine.py:1115](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1115), [compute/tests/test_resurgence_frontier_engine.py:359](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:359), [compute/tests/test_resurgence_frontier_engine.py:447](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:447), [compute/tests/test_resurgence_frontier_engine.py:739](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:739)). Direct checks on the module’s own coefficients gave `|S_20|/20! ≈ 2.11e-8` at `c=1` and `≈ 1.15e-27` at `c=13`, which supports Gevrey-0; the contradiction is the downstream Borel-singularity/Stokes interpretation, not the Gevrey label.

[HIGH] [compute/tests/test_resurgence_frontier_engine.py:447](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:447) — The singularity check is too weak to verify the claimed Borel singularities. It accepts any modulus ratio in `(0.01,100)`, and the actual module output is nowhere near the predicted locations: for `c=25`, `pade_pole_convergence(..., N=[20,30,40])` gave nearest moduli `70.82, 100.93, 28.13` while the predicted modulus is `1/rho = 4.1355`; for `c=13`, the nearest poles were around `37.35, 53.29, 63.65` while `1/rho = 2.1395`. The tests pass because the tolerance is permissive, not because the predicted singularity model is confirmed.

[HIGH] [compute/tests/test_resurgence_frontier_engine.py:1](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:1) — AP10/AP128 is not satisfied. This file contains many hardcoded expected values (`13/2`, `2.0`, `2*pi*i`, fixed `c`-grids, explicit pole/finite-value claims), but `rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_resurgence_frontier_engine.py` returned no matches. There are no per-value 2-source verification annotations.

[HIGH] [compute/tests/test_btz_arithmetic_frontier_engine.py:23](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:23) — The file promises “Every numerical result verified by at least 3 independent paths,” but the inspected asymptotic surface still hardcodes uncited constants such as `0.5651591039924851`, `196884`, `21493760`, `864299970`, and the exact asymptotic limit `2.0` ([compute/tests/test_btz_arithmetic_frontier_engine.py:509](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:509), [compute/tests/test_btz_arithmetic_frontier_engine.py:537](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:537), [compute/tests/test_btz_arithmetic_frontier_engine.py:807](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:807)). `rg` found only the mandate line, not the required `# VERIFIED` source trails.

[MEDIUM] [compute/lib/resurgence_frontier_engine.py:1145](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1145) — The self-dual `c=13` Stokes multiplier is internally inconsistent. This docstring says `S_1` is real at the self-dual point, but the implementation hardcodes `stokes_multiplier_from_monodromy(...) = 2*pi*i` for all `c` ([compute/lib/resurgence_frontier_engine.py:726](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:726)), and the tests explicitly assert it is purely imaginary ([compute/tests/test_resurgence_frontier_engine.py:544](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:544)).

## Summary
Gevrey type itself looks correct: the shadow coefficient growth is consistent with Gevrey-0/sub-factorial behavior. The failure is the downstream resurgence story built on top of that label: the same surface then treats the corresponding Borel transform as if it had finite singularities and Stokes jumps. The exact requested selector `python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --tb=short -q 2>&1 | tail -30` did not terminate during the audit window; a collect-only run found 890 selected tests, and targeted reruns passed (`compute/tests/test_resurgence_frontier_engine.py`: 97 passed; `compute/tests/test_btz_arithmetic_frontier_engine.py -k asymptotic`: 6 passed). Instances checked: 14 | Violations found: 5 | Verdict: FAIL


---
STDERR:
2026-04-12T22:08:36.005155Z ERROR codex_core::skills::manager: failed to install system skills: io error while remove existing system skills dir: Directory not empty (os error 66)
OpenAI Codex v0.104.0 (research preview)
--------
workdir: /Users/raeez/chiral-bar-cobar
model: gpt-5.4
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR]
reasoning effort: xhigh
reasoning summaries: auto
session id: 019d83bd-58e8-7e42-8243-ad6c15484d75
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


Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --tb=short -q 2>&1 | tail -30. Check: Gevrey type correct?

Also check: are hardcoded expected values in test files cited with 2+ independent sources (AP10/AP128)? Read the test file and verify.
mcp startup: no servers

thinking
**Considering test file analysis**

I might need to select multiple test files using the option `-k` along with 'stokes or asymptotic'. I should search within `compute/tests` and possibly count the instances checked and violations found. It sounds like sorting by severity with file:line references could be useful, and I’m also considering whether to include files with no findings, which seems likely. I should be careful not to modify any files while using tools like `rg`, `sed`, and `nl`.
codex
Using `deep-beilinson-audit` for the adversarial read and `build-surface` for the targeted pytest check. I’m starting with the requested test run, then I’ll read the matching test files and verify whether any hardcoded expectations are actually backed by 2+ independent sources as required by AP10/AP128.
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 301ms:
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
 succeeded in 357ms:
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
The requested pytest command is still running. While that finishes, I’m locating the exact `stokes`/`asymptotic` test surfaces and loading the repo’s audit baselines so the findings are grounded against the live manuscript constitution rather than memory.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' chapters/connections/concordance.tex" in /Users/raeez/chiral-bar-cobar succeeded in 54ms:
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

 succeeded in 54ms:
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

exec
/bin/zsh -lc 'rg -n "stokes|asymptotic|Gevrey|gevery|hardcoded|VERIFIED|DC|LT|LC|SY|CF|NE|DA" compute/tests' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then sed -n '1,220p' raeeznotes/raeeznotes100/red_team_summary.md; else sed -n '1,220p' archive/raeeznotes/raeeznotes100/red_team_summary.md; fi" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' metadata/theorem_registry.md" in /Users/raeez/chiral-bar-cobar succeeded in 130ms:
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
 succeeded in 406ms:
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
 succeeded in 450ms:
compute/tests/test_resurgence_frontier_engine.py:296:        """Borel transform should converge (algebraic GF is Gevrey-0)."""
compute/tests/test_resurgence_frontier_engine.py:497:    def test_stokes_jump_heisenberg_zero(self):
compute/tests/test_resurgence_frontier_engine.py:512:    def test_stokes_jump_affine_zero(self):
compute/tests/test_resurgence_frontier_engine.py:538:            virasoro_data, stokes_multiplier_from_monodromy,
compute/tests/test_resurgence_frontier_engine.py:541:        S_1 = stokes_multiplier_from_monodromy(d)
compute/tests/test_resurgence_frontier_engine.py:544:    def test_stokes_purely_imaginary(self):
compute/tests/test_resurgence_frontier_engine.py:547:            virasoro_data, stokes_multiplier_from_monodromy,
compute/tests/test_resurgence_frontier_engine.py:550:        S_1 = stokes_multiplier_from_monodromy(d)
compute/tests/test_resurgence_frontier_engine.py:554:    def test_stokes_independent_of_c(self):
compute/tests/test_resurgence_frontier_engine.py:557:            virasoro_data, stokes_multiplier_from_monodromy,
compute/tests/test_resurgence_frontier_engine.py:562:            S_values.append(stokes_multiplier_from_monodromy(d))
compute/tests/test_resurgence_frontier_engine.py:922:        """Borel coefficients match resurgence_stokes_engine.py."""
compute/tests/test_resurgence_frontier_engine.py:926:        from lib.resurgence_stokes_engine import (
compute/tests/test_btz_arithmetic_frontier_engine.py:19:  16. Large-n asymptotics
compute/tests/test_btz_arithmetic_frontier_engine.py:23:MULTI-PATH VERIFICATION MANDATE:
compute/tests/test_btz_arithmetic_frontier_engine.py:526:    def test_I1_large_x_asymptotic(self):
compute/tests/test_btz_arithmetic_frontier_engine.py:529:        asymptotic = math.exp(x) / math.sqrt(TWO_PI * x)
compute/tests/test_btz_arithmetic_frontier_engine.py:530:        ratio = bessel_I1(x) / asymptotic
compute/tests/test_btz_arithmetic_frontier_engine.py:807:    def test_asymptotic_ratio_is_2(self):
compute/tests/test_btz_arithmetic_frontier_engine.py:808:        """The theoretical asymptotic limit is 2."""
codex
I have the audit surface narrowed to the `stokes`/`asymptotic` test cluster. Next I’m reading the concrete test files that match that selector, checking whether the Gevrey claim is mathematically consistent with the implementation, and then I’ll reconcile that against the actual pytest result once the run completes.
Plan update
Audit is scoped to the targeted compute tests and AP10/AP128 hardcoded-value discipline, with no file modifications.
  → Run the requested pytest selector and capture the actual failing/passing surface
  • Read the selected stokes/asymptotic test files and isolate hardcoded expected values plus their stated verification sources
  • Check Gevrey-type assertions against the formulas/implementations used by the tests
  • Re-verify each candidate finding against exact file lines and assemble severity-ordered report
exec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '250,360p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   250	    def test_fraction_arithmetic_virasoro_c13(self):
   251	        """Fraction arithmetic at c=13."""
   252	        from lib.resurgence_frontier_engine import virasoro_coefficients_fraction
   253	        coeffs = virasoro_coefficients_fraction(13, 1, max_r=30)
   254	        assert abs(float(coeffs[2]) - 13.0 / 2.0) < 1e-14
   255	        # S_3 = 2
   256	        assert abs(float(coeffs[3]) - 2.0) < 1e-14
   257	
   258	    def test_fraction_high_order_r50(self):
   259	        """Fraction arithmetic to r=50 does not lose precision."""
   260	        from lib.resurgence_frontier_engine import virasoro_coefficients_fraction
   261	        coeffs = virasoro_coefficients_fraction(13, 1, max_r=50)
   262	        # Check that S_50 is a well-defined Fraction
   263	        assert isinstance(coeffs[50], Fraction)
   264	        # And nonzero
   265	        assert coeffs[50] != 0
   266	
   267	
   268	# =====================================================================
   269	# Section 3: Borel transform
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --collect-only -q" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/resurgence_stokes_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '480,590p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '900,950p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Resurgence and Stokes engine for the shadow obstruction tower.
     2	
     3	Connects the divergent shadow obstruction tower asymptotics to non-perturbative physics
     4	via Ecalle's resurgence theory. The shadow generating function
     5	
     6	    G(t) = sum_{r>=2} S_r t^r
     7	
     8	is generically divergent (class M with rho > 1 for c < c*). Borel
     9	resummation yields a well-defined analytic function, but the Borel
    10	transform has singularities that encode non-perturbative (instanton)
    11	contributions. The Stokes phenomenon -- discontinuous jumps in the
    12	lateral Borel sums as the direction of summation crosses a singular
    13	ray -- is governed by Stokes multipliers that are constrained by the
    14	MC equation (Ecalle's bridge equation).
    15	
    16	MATHEMATICAL FRAMEWORK:
    17	
    18	1. **Borel transform**: B[G](xi) = sum_{r>=2} S_r xi^r / Gamma(r+1).
    19	   For Virasoro at leading order, S_r ~ (2/r)(-3)^{r-4}(2/c)^{r-2},
    20	   so the Borel transform has singularities at xi = 1/rho * e^{+/- i*theta}
 succeeded in 51ms:
   480	        from lib.resurgence_frontier_engine import (
   481	            virasoro_data, shadow_coefficients_exact, lateral_borel_sum,
   482	        )
   483	        d = virasoro_data(2.0)
   484	        coeffs = shadow_coefficients_exact(d, max_r=40)
   485	        # Choose a point on the positive real axis
   486	        t_probe = 0.1 + 0.0j
   487	        S_plus = lateral_borel_sum(coeffs, t_probe, epsilon=0.05,
   488	                                    xi_max=30.0, n_quad=1000)
   489	        S_minus = lateral_borel_sum(coeffs, t_probe, epsilon=-0.05,
   490	                                     xi_max=30.0, n_quad=1000)
   491	        # The lateral sums may or may not differ significantly depending
   492	        # on whether t_probe is near a Stokes line. At least they should
   493	        # be finite.
   494	        assert math.isfinite(abs(S_plus))
   495	        assert math.isfinite(abs(S_minus))
   496	
   497	    def test_stokes_jump_heisenberg_zero(self):
   498	        """Heisenberg: Borel entire, so Stokes jump = 0."""
   499	        from lib.resurgence_frontier_engine import (
 succeeded in 51ms:
   900	    def test_coefficients_match_shadow_tower_recursive(self):
   901	        """Shadow coefficients match shadow_tower_recursive.py."""
   902	        from lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact
   903	        from lib.shadow_tower_recursive import shadow_coefficients_virasoro
   904	        for c in [1.0, 13.0, 25.0]:
   905	            d = virasoro_data(c)
   906	            frontier = shadow_coefficients_exact(d, max_r=20)
   907	            recursive = shadow_coefficients_virasoro(c, max_r=20)
   908	            for r in range(2, 21):
   909	                assert abs(frontier[r] - recursive[r]) < 1e-10, \
   910	                    f"S_{r} mismatch at c={c}"
   911	
   912	    def test_branch_points_match(self):
   913	        """Branch points match shadow_radius.py."""
   914	        from lib.resurgence_frontier_engine import virasoro_data
   915	        from lib.shadow_radius import virasoro_branch_points_numerical
   916	        d = virasoro_data(13.0)
   917	        bp = virasoro_branch_points_numerical(13)
   918	        assert abs(d.branch_plus - bp['t_plus']) < 1e-10
   919	        assert abs(d.branch_minus - bp['t_minus']) < 1e-10

thinking
**Inspecting code files**

I’m wondering if I should examine `compute/lib/resurgence_frontier_engine.py` instead of `resurgence_stokes`. It seems the tests import the new library, so I need to check the relevant segments related to the Gevrey claim, Stokes multiplier, and branch points. It feels like there’s a clear direction here, and I want to ensure I’m looking at the right parts of the code for a thorough understanding. Let's do a closer inspection!
exec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '760,980p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '260,520p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '520,760p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   760	    The bridge equation relates the alien derivative of each shadow
   761	    coefficient to the Stokes automorphism. At each arity, the MC
   762	    constraint provides an independent relation between S_1 and the
   763	    instanton corrections. Consistency (same S_1 at all arities) is
   764	    guaranteed by D^2 = 0.
   765	
   766	    At leading order in 1/c (for Virasoro):
   767	    - S_r ~ (-6/c)^r / r
   768	    - S_r^{(1)} ~ S_r * ratio^2 where ratio = -6/c
   769	    - The ratio is uniform across arities: this is the signature of
   770	      the leading-order log singularity.
   771	    """
   772	    coeffs = shadow_coefficients_exact(data, max_arity)
   773	    S_1 = stokes_multiplier_from_monodromy(data)
   774	
   775	    # For Virasoro: the leading-order one-instanton correction to S_r
   776	    # is proportional to S_r with a uniform ratio (from the log form).
   777	    # For a general algebra, the ratio depends on the specific branch
   778	    # cut structure. We use the leading-order log form here.
   779	    if data.depth_class == 'M' and abs(data.kappa) > 1e-30:
 succeeded in 51ms:
     1	r"""Resurgence frontier engine: Borel singularities, Stokes multipliers,
     2	and bridge equations from the MC equation for the shadow obstruction tower.
     3	
     4	This module implements the full resurgence analysis pipeline for chiral
     5	algebras, connecting the divergent shadow obstruction tower to non-perturbative physics
     6	via Ecalle's theory. The shadow generating function
     7	
     8	    G(t) = sum_{r>=2} S_r t^r
     9	
    10	is generically divergent for class M algebras. The Borel transform
    11	
    12	    B[G](xi) = sum_{r>=2} S_r xi^r / Gamma(r+1)
    13	
    14	has singularities whose locations are determined by the branch points of
    15	the shadow metric Q_L(t). These singularities encode non-perturbative
    16	(instanton) contributions to the shadow obstruction tower.
    17	
    18	PIPELINE:
    19	    1. Exact shadow coefficients (Fraction arithmetic) via convolution recursion
    20	    2. Borel transform to high order (r = 50+)
 succeeded in 51ms:
   260	    if x * x == n:
   261	        return x
   262	    return None
   263	
   264	
   265	def _shadow_coefficients_float_as_fraction(q0, q1, q2, max_r):
   266	    """Fallback: compute with floats, return as dict of floats."""
   267	    q0f = float(q0)
   268	    q1f = float(q1)
   269	    q2f = float(q2)
   270	    max_n = max_r - 2
   271	    a = [0.0] * (max_n + 1)
   272	    a[0] = math.sqrt(q0f)
   273	    if max_n >= 1:
   274	        a[1] = q1f / (2.0 * a[0])
   275	    if max_n >= 2:
   276	        a[2] = (q2f - a[1]**2) / (2.0 * a[0])
   277	    for n in range(3, max_n + 1):
   278	        conv = sum(a[j] * a[n - j] for j in range(1, n))
   279	        a[n] = -conv / (2.0 * a[0])
 succeeded in 51ms:
   520	    """
   521	    r_min = min(shadow_coeffs.keys())
   522	    r_max_full = max(shadow_coeffs.keys())
   523	
   524	    if N_values is None:
   525	        N_values = list(range(6, min(r_max_full - r_min + 1, 60), 2))
   526	
   527	    results = []
   528	    for N in N_values:
   529	        if N > r_max_full - r_min + 1:
   530	            break
   531	
   532	        # Truncate to first N coefficients
   533	        inner = []
   534	        for k in range(N):
   535	            r = r_min + k
   536	            sr = shadow_coeffs.get(r, 0.0)
   537	            inner.append(sr / math.gamma(r + 1))
   538	
   539	        m = N // 2



thinking
**Analyzing test files**

I'm seeing that the `collect-only` command is still running unexpectedly, which might be due to a heavy suite import. Maybe I could let it run longer or try a more targeted approach by using `rg -l "stokes|asymptotic" compute/tests` to locate specific files. I also want to run `pytest -k 'stokes or asymptotic' -q --co` to tackle potential import issues. Moreover, the user wants hardcoded expected values in test files backed by at least two independent sources. I should check `test_resurgence_frontier_engine.py` for these constants.
thinking
**Identifying hardcoded values**

I need to pinpoint hardcoded values that lack verified comments, which is likely a common issue. I'm thinking of counting instances, such as `2πi`, `0`, and specific values for `c`. AP10 requires that every hardcoded expected value in a test file has a `# VERIFIED` comment with at least two sources. I should be careful about whether this applies universally or only to values derived from mathematical claims.

Since the user wants a thorough audit, I'm considering highlighting violations by severity and providing file:line references, perhaps focusing on clusters of issues while also summarizing key findings.
thinking
**Inspecting test file header**

I need to make sure I don’t list too many lines when I report uncited hardcoded expected values. I could highlight a cluster starting at line 275, for example. I should also check the header of `test_resurgence_frontier_engine.py` for any AP10 comments—there might be none, which would be problematic. I’ll start by opening the file from the top to review its contents. This could help me gather the necessary information.
codex
The resurgence test surface is already showing a likely mathematical issue: the file states “algebraic GF is Gevrey-0,” while the implementation immediately performs a classical factorial Borel transform, which is the transform for Gevrey-1 growth. I’m now checking that against the exact coefficient asymptotics and the rest of the file before deciding whether it’s a genuine contradiction or just bad wording.
exec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_btz_arithmetic_frontier_engine.py | sed -n '500,860p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_miura_shadow_transfer.py | sed -n '520,570p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_shadow_period_integral_engine.py | sed -n '1030,1085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_verlinde_shadow_cohft_engine.py | sed -n '650,1090p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Tests for the resurgence frontier engine.
     2	
     3	Comprehensive verification of the Borel-Stokes-bridge equation pipeline
     4	for all supported chiral algebra families:
     5	
     6	1. Shadow data correctness for each family
     7	2. Exact shadow coefficients (Fraction and float)
     8	3. Borel transform: coefficients, evaluation, convergence
     9	4. Pade approximation: pole detection, convergence to true singularities
    10	5. Borel singularity locations vs shadow metric branch points
    11	6. Lateral Borel sums and Stokes discontinuity
    12	7. Stokes multiplier extraction and monodromy relation
    13	8. Bridge equation verification: MC constraint -> alien derivative
    14	9. Transseries: perturbative + instanton sectors, evaluation
    15	10. Heisenberg (class G): entire Borel, no singularities
    16	11. Affine sl_2 (class L): polynomial Borel, no singularities
    17	12. Virasoro at c=1,2,13,25: full pipeline
    18	13. W_3 multi-channel: T-line + W-line independent analysis
    19	14. Self-dual c=13: Z_2 symmetry, real Stokes multiplier
    20	15. Koszul duality: rho(c) vs rho(26-c)
 succeeded in 51ms:
Total output lines: 361

   500	        """I_1(0) = 0."""
   501	        assert bessel_I1(0) == 0.0
   502	
   503	    def test_I1_small_x(self):
   504	        """I_1(x) ~ x/2 for small x (next term is x^3/16)."""
   505	        x = 0.01
   506	        # I_1(x) = x/2 + x^3/16 + ... so error ~ x^3/16 ~ 6.25e-8
   507	        assert abs(bessel_I1(x) - x / 2) < 1e-7
   508	
   509	    def test_I1_known_value(self):
   510	        """I_1(1) ~ 0.5651591039924851."""
   511	        # From mathematical tables
   512	        expected = 0.5651591039924851
   513	        assert abs(bessel_I1(1.0) - expected) < 1e-8
   514	
   515	    def test_I1_positive_for_positive_x(self):
   516	        """I_1(x) > 0 for x > 0."""
   517	        for x in [0.1, 1.0, 5.0, 10.0, 50.0]:
 succeeded in 52ms:
   520	# ============================================================================
   521	# Section 12: Asymptotic growth rate (4 tests)
   522	# ============================================================================
   523	
   524	class TestAsymptoticGrowthRate:
   525	    """Test asymptotic properties of the Miura-transferred tower."""
   526	
   527	    def test_growth_rate_positive_c(self):
   528	        """Growth rate rho is real and positive for positive c."""
   529	        # k=10 for W_2 gives c = 1/2 > 0
   530	        result = miura_tower_asymptotics(2, Fraction(10), 20)
   531	        assert result['rho_exact'] is not None
   532	        assert result['rho_exact'] > 0
   533	
   534	    def test_growth_rate_negative_c(self):
   535	        """Growth rate rho is real for negative c."""
   536	        # k=1 for W_2 gives c = -1
   537	        result = miura_tower_asymptotics(2, Fraction(1), 20)
   538	        assert result['rho_exact'] is not None
   539	        assert result['rho_exact'] > 0
 succeeded in 52ms:
  1030	        """q_1 = 12c (= 12*kappa*alpha = 12*(c/2)*2)."""
  1031	        pf = shadow_curve_picard_fuchs(5)
  1032	        assert pf['q1'] == Rational(60)
  1033	
  1034	
  1035	# =========================================================================
  1036	# Section 24: Period growth analysis
  1037	# =========================================================================
  1038	
  1039	class TestPeriodGrowth:
  1040	    """Period growth and asymptotics."""
  1041	
  1042	    def test_lambda_fp_ratio_converges(self):
  1043	        """lambda_{g+1}^FP / lambda_g^FP -> 1/(2*pi)^2 ~ 0.0253."""
  1044	        target = 1 / (2 * math.pi)**2
  1045	        ratios = []
  1046	        for g in range(1, 15):
  1047	            r = float(lambda_fp(g + 1) / lambda_fp(g))
  1048	            ratios.append(r)
  1049	        # Last ratio should be close to target
 succeeded in 52ms:
Total output lines: 441

   650	            types_levels=[("A", 1, 2), ("A", 2, 1), ("A", 3, 1)],
   651	            max_genus=3,
   652	        )
   653	        for rec in results:
   654	            if rec.get("paths_12_agree") is not None:
   655	                assert rec["paths_12_agree"], \
   656	                    f"Paths 1-2 disagree at {rec['type']}_{rec['rank']} " \
   657	                    f"k={rec['level']} g={rec['genus']}"
   658	            if rec.get("paths_13_agree") is not None:
   659	                assert rec["paths_13_agree"], \
   660	                    f"Paths 1-3 disagree at {rec['type']}_{rec['rank']} " \
   661	                    f"k={rec['level']} g={rec['genus']}"
   662	
   663	
   664	# =========================================================================
   665	# Section 19: Asymptotic growth
   666	# =========================================================================
   667	
exec
/bin/zsh -lc 'rg -n "def test_.*(stokes|asymptotic)|class Test.*(Stokes|Asymptotic)|Gevrey" compute/tests' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_shadow_period_integral_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_resurgence_frontier_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_btz_arithmetic_frontier_engine.py' in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
17:Multi-path verification strategy (AP10-compliant):
79:    STANDARD_LANDSCAPE,
247:        for name, data in STANDARD_LANDSCAPE.items():
423:        for name, data in STANDARD_LANDSCAPE.items():
789:    """Multi-path verification of shadow periods (AP10-compliant)."""
exec
/bin/zsh -lc 'rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_miura_shadow_transfer.py' in /Users/raeez/chiral-bar-cobar exited 1 in 81ms:

 exited 1 in 50ms:

 succeeded in 125ms:
23:MULTI-PATH VERIFICATION MANDATE:
 succeeded in 168ms:
compute/tests/test_resurgence_frontier_engine.py:296:        """Borel transform should converge (algebraic GF is Gevrey-0)."""
compute/tests/test_resurgence_frontier_engine.py:475:class TestStokesDiscontinuity:
compute/tests/test_resurgence_frontier_engine.py:497:    def test_stokes_jump_heisenberg_zero(self):
compute/tests/test_resurgence_frontier_engine.py:512:    def test_stokes_jump_affine_zero(self):
compute/tests/test_resurgence_frontier_engine.py:532:class TestStokesMultiplier:
compute/tests/test_resurgence_frontier_engine.py:544:    def test_stokes_purely_imaginary(self):
compute/tests/test_resurgence_frontier_engine.py:554:    def test_stokes_independent_of_c(self):
compute/tests/test_bar_character_algebraic.py:511:class TestVirasoroAsymptotics:
compute/tests/test_bar_character_algebraic.py:514:    def test_leading_asymptotic_direction(self):
compute/tests/test_bar_character_algebraic.py:542:class TestW3Asymptotics:
compute/tests/test_bar_character_algebraic.py:553:    def test_w3_asymptotic_positive(self):
compute/tests/test_btz_arithmetic_frontier_engine.py:526:    def test_I1_large_x_asymptotic(self):
compute/tests/test_btz_arithmetic_frontier_engine.py:807:    def test_asymptotic_ratio_is_2(self):
compute/tests/test_btz_arithmetic_frontier_engine.py:971:class TestLargeNAsymptotics:
compute/tests/test_bc_zero_scheme_engine.py:505:    def test_asymptotic_formula_positive(self):
compute/tests/test_bc_zero_scheme_engine.py:511:    def test_asymptotic_monotone(self):
compute/tests/test_bc_zero_scheme_engine.py:518:    def test_asymptotic_at_zero(self):
compute/tests/test_bc_exceptional_categorical_zeta_engine.py:739:class TestAsymptotics:
compute/tests/test_bc_genus34_shadow_graph_engine.py:595:    def test_growth_ratio_asymptotic_g3(self):
compute/tests/test_miura_shadow_transfer.py:524:class TestAsymptoticGrowthRate:

thinking
**Investigating test results**

I found that my search on test_resurgence returned code 1, indicating no AP10/VERIFIED comments, which is solid evidence. Now, I need to inspect theorem_borel_summability since there's a Gevrey issue there. The user asked for specific tests, so I might also look into any conflicting Gevrey claims across tests and report on cross-test drift. It seems like the same issue might appear in `test_theorem_borel_summability_shadow_engine.py` and `test_theorem_stokes_mc_engine.py`, so I’ll inspect relevant lines for misclassification.
codex
There’s now a second-order pattern, not just a local wording slip. Multiple downstream test suites explicitly codify “Gevrey-0” for the same shadow/resurgence story, so I’m checking whether the repo has a consistent convention here or whether the same incorrect classification propagated into several independent engines.
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_shadow_s11_s15_engine.py | sed -n '350,380p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_borel_summability_shadow_engine.py | sed -n '180,240p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_borel_summability_shadow_engine.py | sed -n '610,630p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"Gevrey-0|Gevrey 0|Gevrey\" compute/lib compute/tests | sed -n '1,200p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_stokes_mc_engine.py | sed -n '300,380p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   350	        assert abs(last_ratio - rho) / rho < 0.5
   351	
   352	
   353	# =========================================================================
   354	# 14. GEVREY-0 (SUB-FACTORIAL)
   355	# =========================================================================
   356	
   357	class TestGevrey:
   358	    """The growth is Gevrey-0: |S_r|/r! -> 0."""
   359	
   360	    @pytest.mark.parametrize("c_val", [1, 13, 26])
   361	    def test_ratio_decreasing(self, c_val):
   362	        results = gevrey_test(c_val, max_r=15)
   363	        # |S_r|/r! should decrease for sufficiently large r
   364	        vals = [v for _, v in results if v > 0]
   365	        # Check that the last value is much smaller than the first
   366	        assert vals[-1] < vals[0], "Gevrey-0 test failed"
   367	
   368	    def test_c1_subfactorial(self):
   369	        """Even at c=1 (divergent series), growth is sub-factorial."""
 succeeded in 51ms:
   610	    def test_koszul_duality_kappa(self):
   611	        """kappa(Vir_c) + kappa(Vir_{26-c}) = 13 (complementarity sum).
   612	
   613	        This is AP24: kappa + kappa' = 13 for Virasoro, NOT zero.
   614	        """
   615	        for c_val in [1.0, 5.0, 13.0, 20.0]:
   616	            k = kappa_virasoro(c_val)
   617	            k_dual = kappa_virasoro(26.0 - c_val)
   618	            assert abs(k + k_dual - 13.0) < 1e-10
   619	
   620	    def test_shadow_vs_string_gevrey(self):
   621	        """Shadow is Gevrey-0, string is Gevrey-1."""
   622	        result = shadow_vs_string_comparison(13.0, g_max=10)
   623	        assert result['shadow_gevrey'] == 0
   624	        assert result['string_gevrey'] == 1
   625	        assert result['shadow_borel_summable'] is True
   626	        assert result['string_borel_summable_on_real_axis'] is False
   627	
   628	    def test_string_grows_faster(self):
   629	        """String coefficients grow much faster than shadow at large genus.
 succeeded in 53ms:
   300	
   301	class TestProof4BorelPade(unittest.TestCase):
   302	    """Proof 4: Borel-Pade numerical extraction."""
   303	
   304	    def test_borel_coefficients_u(self):
   305	        """Borel coefficients b_g = F_g / (g-1)!."""
   306	        kappa = 1.0
   307	        coeffs = _borel_coefficients_u(kappa, 10)
   308	        # b_1 = F_1 / 0! = F_1 = 1/24
   309	        self.assertAlmostEqual(coeffs[0], 1.0 / 24.0, places=14)
   310	        # b_2 = F_2 / 1! = 7/5760
   311	        self.assertAlmostEqual(coeffs[1], 7.0 / 5760.0, places=14)
   312	
   313	    def test_pade_finds_pole_near_4pi2(self):
   314	        """Direct Pade [15/15] on G(u) = sum F_g u^g has pole near (2pi)^2.
   315	
   316	        AP77: the shadow series is Gevrey-0 (convergent), so Borel-Pade
   317	        finds spurious poles. Direct Pade on the generating function
   318	        correctly locates the pole at u = (2pi)^2.
   319	        """
 succeeded in 64ms:
   180	        rho = math.sqrt(rho_sq)
   181	        assert abs(rho - growth_rate(1.0)) < 1e-10
   182	
   183	
   184	# ============================================================================
   185	# Block 3: Gevrey-0 growth verification
   186	# ============================================================================
   187	
   188	class TestGevrey0:
   189	    """Verify Gevrey-0 (sub-factorial) growth: |S_r|/r! -> 0."""
   190	
   191	    def test_gevrey0_at_c1(self):
   192	        """At c=1 (divergent region): |S_r|/r! still -> 0.
   193	
   194	        The oscillatory structure (complex conjugate branch points) causes
   195	        local non-monotonicity in |S_r|/r!, but the OVERALL trend is
   196	        super-exponential decay. We verify that the last third of the
   197	        ratios are much smaller than the first third.
   198	        """
   199	        result = gevrey_class_test(1.0, max_r=20)
 succeeded in 88ms:
compute/tests/test_resurgence_frontier_engine.py:296:        """Borel transform should converge (algebraic GF is Gevrey-0)."""
compute/tests/test_theorem_borel_summability_shadow_engine.py:7:Block 3: Gevrey-0 growth verification
compute/tests/test_theorem_borel_summability_shadow_engine.py:185:# Block 3: Gevrey-0 growth verification
compute/tests/test_theorem_borel_summability_shadow_engine.py:188:class TestGevrey0:
compute/tests/test_theorem_borel_summability_shadow_engine.py:189:    """Verify Gevrey-0 (sub-factorial) growth: |S_r|/r! -> 0."""
compute/tests/test_theorem_borel_summability_shadow_engine.py:207:            "Gevrey-0: |S_r|/r! not decaying overall"
compute/tests/test_theorem_borel_summability_shadow_engine.py:621:        """Shadow is Gevrey-0, string is Gevrey-1."""
compute/tests/test_theorem_shadow_s11_s15_engine.py:20:   14. Gevrey-0: |S_r|/r! -> 0
compute/tests/test_theorem_shadow_s11_s15_engine.py:357:class TestGevrey:
compute/tests/test_theorem_shadow_s11_s15_engine.py:358:    """The growth is Gevrey-0: |S_r|/r! -> 0."""
compute/tests/test_theorem_shadow_s11_s15_engine.py:366:        assert vals[-1] < vals[0], "Gevrey-0 test failed"
compute/tests/test_ising_shadow_complete.py:282:        """The shadow obstruction tower is Borel summable (algebraic GF => Gevrey-0)."""
compute/tests/test_resurgence_shadow_tower_engine.py:800:# Section 14: Gevrey analysis
compute/tests/test_resurgence_shadow_tower_engine.py:803:class TestGevreyAnalysis:
compute/tests/test_resurgence_shadow_tower_engine.py:804:    """Test the Gevrey order and optimal truncation."""
compute/tests/test_resurgence_shadow_tower_engine.py:807:        """The shadow series is Gevrey-0 (convergent)."""
compute/tests/test_chiral_zeta_virasoro_engine.py:250:    """Verify coefficient growth is Gevrey-0 (geometric decay)."""
compute/tests/test_chiral_zeta_virasoro_engine.py:258:        # [CF] AP119: Gevrey-0, NOT Gevrey-1 (no factorial divergence).
compute/tests/test_shadow_zeta_engine.py:8:  5. Convergence analysis (Gevrey-0, radius = (2*pi)^2)
compute/tests/test_shadow_zeta_engine.py:246:    """Gevrey-0 classification and convergence radius."""


thinking
**Evaluating Gevrey-0 classification**

I’m considering the Gevrey-0 classification and whether it’s actually correct. If the coefficients behave like S_r  rho^r r^{-5/2}, that fits within the standard Gevrey-0 definition. The statement regarding the Borel transform is tricky—it can converge, particularly when dealing with algebraic generating functions. I’m concerned about potential inconsistencies with Stokes jumps and singularities. Overall, though, it seems that Gevrey-0 might be appropriate based on geometric coefficients. I should confirm this further to avoid any misrepresentation.
thinking
**Inspecting Pade and Borel transforms**

I’m noticing that Pade is being used on the Borel transform to detect poles and approximate singularities. However, these might not correspond correctly. I need to carefully examine tests related to Pade and branch points. If the original series converges within radius R, the Borel transform should be entire. Still, some tests might mistakenly assert the existence of poles and correspondences with branch points, which could lack mathematical validity. It’s essential to investigate those tests further, especially in the Pade sections and their approach to Borel singularity detection.
exec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '980,1085p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '590,760p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '332,480p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/resurgence_frontier_engine.py | sed -n '1085,1180p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   980	    return result
   981	
   982	
   983	def shadow_weighted_exact(data: AlgebraShadowData, t: complex) -> complex:
   984	    r"""Evaluate the exact weighted shadow function H(t) = t^2 * sqrt(Q_L(t)).
   985	
   986	    This is the algebraic function whose Taylor expansion gives the
   987	    weighted shadow coefficients: H(t) = sum_{r>=2} r * S_r * t^r.
   988	    """
   989	    t = complex(t)
   990	    Q_val = data.q0 + data.q1 * t + data.q2 * t**2
   991	    return t**2 * cmath.sqrt(Q_val)
   992	
   993	
   994	# =====================================================================
   995	# Section 9: Borel sum vs exact (full verification)
   996	# =====================================================================
   997	
   998	def borel_sum_vs_algebraic(data: AlgebraShadowData, t_val: float,
   999	                            r_max: int = 60) -> Dict[str, Any]:
 succeeded in 52ms:
   590	            assert r.bridge_satisfied
   591	
   592	    def test_bridge_consistency_uniform_ratio(self):
   593	        """The instanton/perturbative ratio should be uniform (D^2=0)."""
   594	        from lib.resurgence_frontier_engine import (
   595	            virasoro_data, bridge_equation_ratio_consistency,
   596	        )
   597	        d = virasoro_data(13.0)
   598	        result = bridge_equation_ratio_consistency(d, max_arity=15)
   599	        assert result['consistent']
   600	
   601	    def test_bridge_arity2_kappa_exact(self):
   602	        """At arity 2, kappa is exact (one-loop), no instanton correction."""
   603	        from lib.resurgence_frontier_engine import (
   604	            virasoro_data, bridge_equation_verify,
   605	        )
   606	        d = virasoro_data(13.0)
   607	        results = bridge_equation_verify(d, max_arity=3)
   608	        # Arity 2 should have interpretation about being exact
   609	        assert results[0].arity == 2
 succeeded in 52ms:
   332	# =====================================================================
   333	# Section 4: Pade approximation
   334	# =====================================================================
   335	
   336	class TestPadeApproximation:
   337	    """Test Pade approximant computation and pole detection."""
   338	
   339	    def test_pade_of_geometric_series(self):
   340	        """[1/1] Pade of 1/(1-x) = 1 + x + x^2 + ... should be exact."""
   341	        from lib.resurgence_frontier_engine import pade_coefficients, pade_evaluate
   342	        coeffs = [1.0, 1.0, 1.0, 1.0]
   343	        P, Q = pade_coefficients(coeffs, 1, 1)
   344	        assert P is not None
   345	        # Evaluate at x = 0.5: should give 1/(1-0.5) = 2
   346	        val = pade_evaluate(P, Q, 0.5)
   347	        assert abs(val - 2.0) < 1e-10
   348	
   349	    def test_pade_poles_of_geometric(self):
   350	        """Pole of 1/(1-x) at x=1."""
   351	        from lib.resurgence_frontier_engine import pade_coefficients, pade_poles
 succeeded in 53ms:
  1085	    For classes G and L: the Borel transform is a polynomial (entire),
  1086	    so there are no singularities. The Pade poles should be absent or
  1087	    spurious. This is itself a verification.
  1088	    """
  1089	    coeffs = shadow_coefficients_exact(data, r_max)
  1090	    b_coeffs = borel_coefficients(coeffs)
  1091	
  1092	    # Pade poles in the Borel plane
  1093	    poles_diag = borel_pade_poles(coeffs, pade_type='diagonal')
  1094	    poles_subdiag = borel_pade_poles(coeffs, pade_type='subdiagonal')
  1095	
  1096	    # Predicted singularities: reciprocals of branch points
  1097	    if abs(data.branch_plus) > 1e-15:
  1098	        A_plus = 1.0 / data.branch_plus
  1099	        A_minus = 1.0 / data.branch_minus
  1100	    else:
  1101	        A_plus = complex('inf')
  1102	        A_minus = complex('inf')
  1103	
  1104	    # Pade convergence study
codex
The main contradiction is now clearer: the same module claims “algebraic GF is Gevrey-0” and therefore its Borel transform is entire, but elsewhere in the same pipeline it treats class `M` as having genuine Borel singularities and even asserts `analysis.is_entire_borel` is false. I’m checking whether this is only documentation drift or whether the tests materially rely on both incompatible stories.
exec
/bin/zsh -lc "rg -n \"self-dual|REAL|imaginary|2\\*pi\\*i|Stokes multiplier\" compute/tests/test_resurgence_frontier_engine.py compute/lib/resurgence_frontier_engine.py" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
compute/tests/test_resurgence_frontier_engine.py:12:7. Stokes multiplier extraction and monodromy relation
compute/tests/test_resurgence_frontier_engine.py:19:14. Self-dual c=13: Z_2 symmetry, real Stokes multiplier
compute/tests/test_resurgence_frontier_engine.py:418:        """At c=13 (self-dual), Pade poles exist and are finite.
compute/tests/test_resurgence_frontier_engine.py:421:        self-dual point because rho(13) ~ 0.467 is moderate. We only
compute/tests/test_resurgence_frontier_engine.py:431:        # At self-dual c=13, Pade poles should exist and be finite
compute/tests/test_resurgence_frontier_engine.py:451:        At c=13 (self-dual), rho ~ 0.467, and 50-term Pade is insufficient
compute/tests/test_resurgence_frontier_engine.py:529:# Section 7: Stokes multiplier
compute/tests/test_resurgence_frontier_engine.py:533:    """Test Stokes multiplier extraction."""
compute/tests/test_resurgence_frontier_engine.py:536:        """Leading-order Stokes multiplier = 2*pi*i from sqrt monodromy."""
compute/tests/test_resurgence_frontier_engine.py:544:    def test_stokes_purely_imaginary(self):
compute/tests/test_resurgence_frontier_engine.py:545:        """Leading-order S_1 is purely imaginary."""
compute/tests/test_resurgence_frontier_engine.py:829:    """Enhanced Z_2 symmetry at the self-dual point c = 13."""
compute/lib/resurgence_frontier_engine.py:1:r"""Resurgence frontier engine: Borel singularities, Stokes multipliers,
compute/lib/resurgence_frontier_engine.py:24:    6. Stokes discontinuity and leading Stokes multiplier S_1
compute/lib/resurgence_frontier_engine.py:36:    to the shadow obstruction tower. The Stokes multipliers control tunneling between
compute/lib/resurgence_frontier_engine.py:229:                # Negative q0 means imaginary kappa; should not happen for physical algebras
compute/lib/resurgence_frontier_engine.py:654:    S_1_extracted: complex  # extracted Stokes multiplier
compute/lib/resurgence_frontier_engine.py:709:    # Theoretical: monodromy of sqrt(Q_L) around simple zero gives S_1 = 2*pi*i
compute/lib/resurgence_frontier_engine.py:727:    r"""Leading-order Stokes multiplier from monodromy of sqrt(Q_L).
compute/lib/resurgence_frontier_engine.py:730:    (thm:shadow-connection), giving monodromy exp(2*pi*i * 1/2) = -1.
exec
/bin/zsh -lc "python3 - <<'PY'
import math, cmath
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact
for c in [1.0, 13.0, 25.0]:
    d = virasoro_data(c)
    coeffs = shadow_coefficients_exact(d, 20)
    vals=[abs(coeffs[r])/math.factorial(r) for r in range(2,21)]
    print('c',c,'last',vals[-1],'first',vals[0],'ratio last/first',vals[-1]/vals[0])
    ratios=[abs(coeffs[r+1]/coeffs[r]) for r in range(10,20) if abs(coeffs[r])>1e-50]
    print(' consecutive approx', ratios[-3:])
    print(' rho',d.rho,'1/rho',1/d.rho if d.rho else None)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.resurgence_frontier_engine import virasoro_data, full_resurgence_analysis
for c in [1.0,13.0,25.0]:
    d=virasoro_data(c)
    analysis=full_resurgence_analysis(d,r_max=20)
    print(c, analysis.is_entire_borel, len(analysis.pade_poles_diagonal), analysis.predicted_singularities)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import math
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact, borel_transform_from_shadow
for c in [13.0,25.0]:
    d=virasoro_data(c)
    coeffs=shadow_coefficients_exact(d,60)
    for xi in [1,5,10,20]:
        val=borel_transform_from_shadow(coeffs, xi)
        print('c',c,'xi',xi,'abs',abs(val))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 3.12s:
c 13.0 xi 1 abs 3.583676174248087
c 13.0 xi 5 abs 123.08295063101869
c 13.0 xi 10 abs 660.3911005279942
c 13.0 xi 20 abs 3989.0754386974277
c 25.0 xi 1 abs 6.583442498743275
c 25.0 xi 5 abs 197.97589072440047
c 25.0 xi 10 abs 959.1429971073441
c 25.0 xi 20 abs 5176.6211609025
 succeeded in 3.58s:
1.0 False 9 ((-5.999999999999999-1.7213259316477403j), (-5.999999999999999+1.7213259316477403j))
13.0 False 9 ((-0.46153846153846156-0.07376358484390531j), (-0.46153846153846156+0.07376358484390531j))
25.0 False 9 ((-0.24-0.029508444542532652j), (-0.24+0.029508444542532652j))

 succeeded in 3.86s:
c 1.0 last 2.1110560889070168e-08 first 0.25 ratio last/first 8.444224355628067e-08
 consecutive approx [11.820698243358239, 7.936572471938762, 6.768029939808041]
 rho 6.2420319578613945 1/rho 0.1602042422645035
c 13.0 last 1.1463832011140903e-27 first 3.25 ratio last/first 3.5273329265048933e-28
 consecutive approx [0.38799322054800967, 0.38245520352526097, 0.37544535831242637]
 rho 0.46739578295948925 1/rho 2.1395143825819956
c 25.0 last 1.61632835298578e-32 first 6.25 ratio last/first 2.586125364777248e-33
 consecutive approx [0.21375665189801277, 0.2130580625098971, 0.21217319059468728]
 rho 0.24180725443898432 1/rho 4.135525223674924
thinking
**Checking Python commands**

I'm wondering if the Python commands are still running, possibly because they might be importing heavy modules. It could be useful to check back later. I think it would be a good idea to inspect the lines around the self-dual section to ensure everything is functioning correctly. It’s all about making sure everything is working smoothly!
exec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '820,860p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   820	        result = w3_multi_channel_analysis(13.0, r_max=30)
   821	        assert result['W_line']['n_pade_poles'] > 0
   822	
   823	
   824	# =====================================================================
   825	# Section 14: Self-dual c = 13
   826	# =====================================================================
   827	
   828	class TestSelfDual:
   829	    """Enhanced Z_2 symmetry at the self-dual point c = 13."""
   830	
   831	    def test_is_self_dual(self):
   832	        from lib.resurgence_frontier_engine import self_dual_resurgence_analysis
   833	        result = self_dual_resurgence_analysis()
   834	        assert result['is_self_dual']
   835	
   836	    def test_branches_conjugate(self):
   837	        from lib.resurgence_frontier_engine import self_dual_resurgence_analysis
   838	        result = self_dual_resurgence_analysis()
   839	        assert result['branches_conjugate']

thinking
**Examining stokes multiplier**

I noticed there's no test for the real stokes multiplier, and the docstring might have a conflict, which I'd rate as medium to low importance. It seems like I need to review Python outputs for ratios and do a full analysis to clarify things. I should consider running some polling sessions as well to gather more data. Let's see how that all plays out!

thinking
**Inspecting source files**

I’m considering citing line 23, which only references local files, and line 47 for expected values. I also need to check if `test_btz_arithmetic_frontier_engine.py` includes the AP10 mandate but lacks source tags for the concrete expected constants. It looks like it might need further inspection, especially at the top. I want to make sure I’m thorough about how all these elements fit together and if they influence anything important.
exec
/bin/zsh -lc "nl -ba compute/tests/test_btz_arithmetic_frontier_engine.py | sed -n '1,80p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_shadow_period_integral_engine.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_miura_shadow_transfer.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_verlinde_shadow_cohft_engine.py | sed -n '1,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Tests for BTZ arithmetic frontier engine.
     2	
     3	Tests organised by section:
     4	  1.  J-function coefficients and BTZ degeneracies
     5	  2.  Prime factorisation and arithmetic invariants
     6	  3.  Divisor structure
     7	  4.  Shadow corrections to BTZ entropy
     8	  5.  Number field identification
     9	  6.  Rademacher expansion
    10	  7.  Shadow-modified Rademacher
    11	  8.  Kloosterman sums
    12	  9.  Farey tail and shadows
    13	  10. Bekenstein-Hawking from Koszul duality
    14	  11. Arithmetic height
    15	  12. Height growth analysis
    16	  13. Multi-path verification (Fourier, Rademacher, bootstrap)
    17	  14. Cross-family consistency
    18	  15. Special central charges (c = 13, 24, 26)
    19	  16. Large-n asymptotics
    20	  17. Planted-forest consistency
 succeeded in 51ms:
     1	r"""Tests for shadow_period_integral_engine.py.
     2	
     3	Multi-path verification of shadow period integrals, covering:
     4	  1. Genus-1 shadow periods for all standard families
     5	  2. Genus-2 shadow periods (scalar + higher-arity corrections)
     6	  3. Period polynomial (= lambda_g^FP, universal)
     7	  4. Siegel modular volumes
     8	  5. Shadow curve periods and branch points (Virasoro, class M)
     9	  6. Beilinson regulator
    10	  7. Deligne periods
    11	  8. Bernoulli structure and A-hat consistency
    12	  9. Additivity, complementarity, rationality cross-checks
    13	 10. CM criterion for shadow curves
    14	 11. Period decay ratios
    15	 12. Landscape-wide tests
    16	
    17	Multi-path verification strategy (AP10-compliant):
    18	  Path 1: Direct computation from kappa * lambda_g^FP * Vol(A_g)
    19	  Path 2: Tautological intersection numbers * moduli volumes
    20	  Path 3: Bernoulli number route
 succeeded in 51ms:
     1	r"""Tests for Miura shadow transfer engine.
     2	
     3	Systematic verification of DS-transferred shadow obstruction towers via the Miura
     4	transformation (Method C). The Miura map expresses W_N generators as
     5	nonlinear polynomials of N-1 free bosons. Free bosons have Gaussian
     6	shadow obstruction towers (depth 2). Composing through the Miura nonlinearity
     7	generates the infinite shadow obstruction tower of W_N.
     8	
     9	STRUCTURE:
    10	  Section 1: Central charge from Miura (8 tests)
    11	  Section 2: Kappa from Miura (8 tests)
    12	  Section 3: Miura vs direct shadow obstruction tower comparison — W_2 (6 tests)
    13	  Section 4: Miura vs direct shadow obstruction tower comparison — W_3 (6 tests)
    14	  Section 5: Miura vs direct shadow obstruction tower comparison — W_4 (4 tests)
    15	  Section 6: Shadow obstruction tower at high arity (r up to 20) (6 tests)
    16	  Section 7: S_4 quartic creation mechanism (6 tests)
    17	  Section 8: Depth increase G -> M via nonlinearity (4 tests)
    18	  Section 9: Ghost sector analysis (5 tests)
    19	  Section 10: W_3 W-line via Miura (4 tests)
    20	  Section 11: Miura monomial decomposition (4 tests)
 succeeded in 51ms:
     1	r"""Tests for the Verlinde-shadow CohFT engine.
     2	
     3	Verification paths:
     4	  Path 1: Verlinde formula via S-matrix (type A) / quantum Weyl dimensions (all types)
     5	  Path 2: Independent quantum Weyl dimension formula
     6	  Path 3: Known literature values (Di Francesco-Mathieu-Senechal, Beauville, Fuchs)
     7	  Path 4: Genus-1 = number of integrable representations
     8	  Path 5: Shadow F_g = kappa * lambda_g^FP
     9	  Path 6: Level-rank duality as consistency check
    10	
    11	The Verlinde formula is:
    12	    V_{g,k}(g) = sum_lambda S_{0,lambda}^{2-2g}
    13	using RAW S-matrix entries (NOT quantum dimensions d_lambda = S_{0,lambda}/S_{0,0}).
    14	
    15	Ground truth:
    16	  thm:shadow-cohft (higher_genus_modular_koszul.tex)
    17	  thm:modular-characteristic (higher_genus_modular_koszul.tex)
    18	  Verlinde (1988), Kac-Peterson (1984), Beauville (1996)
    19	"""
    20	

 succeeded in 2m 19s:
compute/tests/test_a2_polynomial_combinatorics_engine.py::test_asymptotic_ratio_converges_to_one_eighth
compute/tests/test_ahat_genus_comprehensive.py::TestAsymptotics::test_ratio_approaches_one_over_four_pi_squared
compute/tests/test_ahat_genus_comprehensive.py::TestAsymptotics::test_bernoulli_asymptotic_formula
compute/tests/test_ahat_genus_comprehensive.py::TestAsymptotics::test_lambda_fp_asymptotic_bound
compute/tests/test_ahat_genus_comprehensive.py::TestAsymptotics::test_factorial_growth_of_F_g
compute/tests/test_allgenus_chiral_homology.py::TestScalarGenusTower::test_bernoulli_asymptotics
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_resurgence_bridge_imaginary_check
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_data_structure
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_koszul_duality_relation
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_monodromy_koszul_sign
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_multiplier_imaginary
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_multiplier_proportional_to_kappa
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_stokes_multiplier_virasoro_c13
compute/tests/test_analytic_langlands_shadow_engine.py::TestStokesData::test_universal_instanton_action
compute/tests/test_analytic_shadow_partition_engine.py::TestLargeTauAsymptotics::test_leading_term
compute/tests/test_analytic_shadow_partition_engine.py::TestLargeTauAsymptotics::test_correction_exponentially_small
compute/tests/test_analytic_shadow_partition_engine.py::TestLargeTauAsymptotics::test_shadow_coefficient
compute/tests/test_arithmetic_resurgence.py::TestStokesMultipliers::test_genus_stokes_proportional_to_kappa
compute/tests/test_arithmetic_resurgence.py::TestStokesMultipliers::test_genus_stokes_linear_in_kappa
compute/tests/test_arithmetic_resurgence.py::TestStokesMultipliers::test_genus_stokes_alternating_sign




thinking
**Verifying test file values**

The test files usually claim to be AP10, but they don't all verify per line. I need to check if hardcoded expected values are cited with two or more independent sources, and many seem to lack this. It would help to provide a few concrete examples. The user asked to verify specific test files, not all 890, so I might focus on a subset and report the instances checked, as well as the pytest run results. This may take time to complete.
thinking
**Assessing test outcomes**

I think the actual run might show failures that highlight some issues. I might also consider running a shorter subset in another shell, but it’s probably better to wait. Inspecting specific modules for contradictions could help, as well as running individual tests to verify them. The user wants to check the Gevrey type, not necessarily failures, so I need to use my reasoning and focus on line 739 regarding `analysis.is_entire_borel`. It appears inconsistent with the library documentation, so I’ll confirm results and check the relevant documentation for logic.
thinking
**Analyzing Gevrey classification contradictions**

Given the comments at lines 345 and 1010, it seems class M is entirely critical, which is problematic because the module's logic contradicts its Gevrey classification. This could mean the tests are encoding the wrong Borel singularity picture. I wonder if it’s mathematically incorrect, but if the coefficients \( S_r \sim \rho^r r^{-5/2} \), the Borel transform divided by \( r! \) suggests it should be entire. So, the code’s `is_entire_borel` being false for class M seems incorrect. I'm curious why they’re using Pade poles since the Pade approximants of entire functions still have poles.
thinking
**Verifying mathematical concepts**

I'm diving into the idea that reciprocals of branch points aren't actual singularities of the Borel transform, which seems conceptually flawed. I need to verify this with actual code formulas. The `borel_transform_from_shadow` function sums up terms that appear entire if certain conditions are met. Their ratio test indicates a decay to zero for the coefficients, confirming that the class M Borel transform is indeed entire. However, there's a genuine discrepancy with expectations about singularities, and I may need to compute values to clarify this.
thinking
**Examining series convergence**

I'm considering how the value of `d.rho` affects the convergence of the original series, even if it remains in the Gevrey-0 class. For `c=1`, the series diverges when `rho>1` because the coefficients grow geometrically. However, the Borel transform remains entire since we divide by `r!`. This means there's no Stokes phenomenon from Borel singularities, yet tests suggest lateral sums might differ for class M on the Stokes line. I need to inspect the actual test for `test_lateral_sums_differ`.
exec
/bin/zsh -lc "nl -ba compute/tests/test_resurgence_frontier_engine.py | sed -n '475,540p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
   475	class TestStokesDiscontinuity:
   476	    """Test lateral Borel sums and Stokes jump."""
   477	
   478	    def test_lateral_sums_differ(self):
   479	        """S_+ and S_- should differ for class M on the Stokes line."""
   480	        from lib.resurgence_frontier_engine import (
   481	            virasoro_data, shadow_coefficients_exact, lateral_borel_sum,
   482	        )
   483	        d = virasoro_data(2.0)
   484	        coeffs = shadow_coefficients_exact(d, max_r=40)
   485	        # Choose a point on the positive real axis
   486	        t_probe = 0.1 + 0.0j
   487	        S_plus = lateral_borel_sum(coeffs, t_probe, epsilon=0.05,
   488	                                    xi_max=30.0, n_quad=1000)
   489	        S_minus = lateral_borel_sum(coeffs, t_probe, epsilon=-0.05,
   490	                                     xi_max=30.0, n_quad=1000)
   491	        # The lateral sums may or may not differ significantly depending
   492	        # on whether t_probe is near a Stokes line. At least they should
   493	        # be finite.
   494	        assert math.isfinite(abs(S_plus))

thinking
**Evaluating code checks**

I see the `test_lateral_sums_differ` documentation states that the results should differ, but the code checks seem limited to finite cases, so it's not a direct failure. However, the clustering around predicted singularities suggests there's something conceptually off. I might need to compute S_plus and S_minus for class M to see if they really differ or if numerical contour differences are at play. It seems testing this in Python could be useful!
exec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact, borel_pade_poles
for c in [1.0,13.0,25.0]:
    d=virasoro_data(c)
    coeffs=shadow_coefficients_exact(d, max_r=50)
    poles=borel_pade_poles(coeffs)
    near=sorted(poles,key=abs)[:5]
    print('c',c,'nearest',near,'pred',1/d.branch_plus)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact, lateral_borel_sum
for c in [2.0,13.0]:
    d=virasoro_data(c)
    coeffs=shadow_coefficients_exact(d, max_r=40)
    t=0.1+0j
    sp=lateral_borel_sum(coeffs,t,epsilon=0.05,xi_max=30.0,n_quad=1000)
    sm=lateral_borel_sum(coeffs,t,epsilon=-0.05,xi_max=30.0,n_quad=1000)
    print('c',c,'jump',abs(sp-sm),'sp',sp,'sm',sm)
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
import math
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact
for c in [2.0,13.0]:
    d=virasoro_data(c)
    coeffs=shadow_coefficients_exact(d, max_r=80)
    # root test approximate radius of ordinary generating function
    vals=[]
    for r in range(10,81):
        vals.append(abs(coeffs[r])**(1/r))
    print('c',c,'root test last',vals[-5:],'rho',d.rho)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.66s:
c 1.0 nearest [np.complex128(-0.34005337042064676+2.909619472641476j), np.complex128(-0.34005337042064676-2.909619472641476j), np.complex128(4.031242472393524+0j), np.complex128(-4.600796633305896+0j), np.complex128(-4.981455465454182+0.8254467397090595j)] pred (-5.999999999999999-1.7213259316477403j)
c 13.0 nearest [np.complex128(33.49802971823107+44.45160999920167j), np.complex128(33.49802971823107-44.45160999920167j), np.complex128(64.1466786383603+15.196624725169295j), np.complex128(64.1466786383603-15.196624725169295j), np.complex128(-66.88690361948831+0j)] pred (-0.46153846153846156-0.07376358484390531j)
c 25.0 nearest [np.complex128(110.26409605490099+68.73065503917088j), np.complex128(110.26409605490099-68.73065503917088j), np.complex128(52.64657034777174+125.31699743947222j), np.complex128(52.64657034777174-125.31699743947222j), np.complex128(148.81109263128812+0j)] pred (-0.24-0.029508444542532652j)
 succeeded in 2.74s:
c 2.0 root test last [2.5898542112327467, 2.5803574871439783, 2.5549031528797577, 2.542920007312747, 2.5897000535868866] rho 3.1024184114977142
c 13.0 root test last [0.42156610097089553, 0.4219674390116476, 0.4222249549760484, 0.42233771721753277, 0.42229674699250846] rho 0.46739578295948925
 succeeded in 2.76s:
c 2.0 jump 1.084169672739051e-07 sp (0.012012881540910835+5.420848363695255e-08j) sm (0.012012881540910835-5.420848363695255e-08j)
c 13.0 jump 7.462394243225657e-07 sp (0.06700270070910708+3.7311971216128286e-07j) sm (0.06700270070910708-3.7311971216128286e-07j)
codex
I’ve verified the Gevrey side enough to separate two different issues. The coefficient growth itself is consistent with Gevrey-0, but the same file then builds a class-`M` Borel-singularity/Stokes story that only makes sense for a non-entire Borel transform, so the problem is not the Gevrey label in isolation; it’s the downstream resurgence narrative built on top of it.
exec
/bin/zsh -lc "python3 -m pytest compute/tests/test_btz_arithmetic_frontier_engine.py -k 'asymptotic' -q" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_resurgence_frontier_engine.py -q' in /Users/raeez/chiral-bar-cobar succeeded in 2.31s:
......                                                                   [100%]
6 passed, 155 deselected in 0.89s
 succeeded in 6.84s:
........................................................................ [ 74%]
.........................                                                [100%]
97 passed in 4.33s

thinking
**Evaluating findings and progress**

I’m thinking I might have enough findings: one critical, two high-priority, and one medium. It could be worth mentioning that a big pytest run is still ongoing. I wonder if the final summary should indicate that the large requested command is still in progress. It seems likely to complete eventually, though. We can afford to wait a bit longer. I guess polling again might show whether the actual command 61156 will finish soon.
codex
The exact `pytest -k 'stokes or asymptotic'` run has not returned yet; collection alone was 890 selected tests in this environment, so I’m treating it as a long-running surface rather than a quick falsifier. I’ve already isolated the mathematical contradictions locally and I’m giving the full run a bit more time so I can report its status accurately rather than guessing.
exec
/bin/zsh -lc "python3 - <<'PY'
from compute.lib.resurgence_frontier_engine import virasoro_data, shadow_coefficients_exact, pade_pole_convergence
for c in [25.0,13.0]:
    d=virasoro_data(c)
    coeffs=shadow_coefficients_exact(d, max_r=50)
    conv=pade_pole_convergence(coeffs, N_values=[20,30,40])
    print('c',c)
    for e in conv:
        print(' N',e['N'],'nearest',e['nearest_pole'],'mod',e['nearest_modulus'])
    print('pred_mod',1.0/d.rho)
PY" in /Users/raeez/chiral-bar-cobar succeeded in 2.98s:
c 25.0
 N 20 nearest (-70.8188478176598+0j) mod 70.8188478176598
 N 30 nearest (-100.54127283880501+8.822884764799777j) mod 100.92765151146621
 N 40 nearest (28.131186810885534+0j) mod 28.131186810885534
pred_mod 4.135525223674924
c 13.0
 N 20 nearest (-37.351808984298344+0j) mod 37.351808984298344
 N 30 nearest (-51.24205221773414+14.644699907764885j) mod 53.2936689567671
 N 40 nearest (-63.03271525395208+8.873968432800734j) mod 63.65430470936075
pred_mod 2.1395143825819956

thinking
**Assessing process status**

I need to report that it's still running beyond a certain time, but I should provide more precise details. Currently, there are 890 selected tests found and no failures. Since it’s been running for quite a while now, I could mention that the exact command didn't finish within the observation window. It might be worth inspecting the current logs or running some commands to get more clarity on the process. Let's check on that!




thinking
**Considering summary clarity**

I’m thinking about whether I need to explicitly mention something in the summary or afterwards. It seems like the findings should only include genuine discrepancies. I wonder if being clear about that might help avoid confusion or any misunderstandings. So, I'll need to weigh how to frame this in a way that makes sense for the user while ensuring it’s both accurate and helpful.
thinking
**Evaluating Gevrey type findings**

In my final change-summary, I see that the Gevrey type itself shows no violation, and Gevrey-0 is consistent. However, I'll need the output contract to reflect findings ordered by severity. The user asked me to check the correctness of the Gevrey type, and it appears correct related to shadow coefficients. The false step lies in identifying Borel singularities for the same Gevrey-0 series, which is key but not a finding. Perhaps a brief note could clarify things before the summary.
thinking
**Organizing Gevrey findings**

I could include a [LOW] note about the Gevrey label, which appears consistent with the computed coefficient growth. However, the contract specifies findings only, so maybe I should focus on the summary, indicating that the Gevrey type is correct, but the downstream Borel/Stokes interpretation is not. I need to check if the exact run is complete and mention any partial status. The structured output requires a PASS/FAIL summary based on violations, which are 5 out of 11 instances checked.
thinking
**Planning final summary format**

The instruction to "End with: ## Summary..." makes it clear that I should place the summary at the end. I think it's best to structure my final answer with the findings followed by the summary paragraph, including the run status there instead of a separate line. For example, I’m considering: 

## Summary  
The requested selector processed 890 tests and was still running when I stopped. Targeted checks on specific tests passed, showing that the Gevrey type is consistent with Gevrey-0, but the downstream Borel/Stokes model is not. I checked 9 instances and found 5 violations, leading to a verdict of FAIL. 

I also need to make sure the findings are ordered by severity.
codex
[CRITICAL] [compute/lib/resurgence_frontier_engine.py:345](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:345) — The shadow series is classified here as Gevrey-0, so with the module’s own definition `B[G](xi)=sum S_r xi^r/r!` the Borel transform is entire. The same pipeline later treats class `M` as having finite Borel singularities and nontrivial Stokes data at `1/branch_\pm` ([compute/lib/resurgence_frontier_engine.py:1092](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1092), [compute/lib/resurgence_frontier_engine.py:1115](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1115), [compute/tests/test_resurgence_frontier_engine.py:359](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:359), [compute/tests/test_resurgence_frontier_engine.py:447](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:447), [compute/tests/test_resurgence_frontier_engine.py:739](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:739)). Direct checks on the module’s own coefficients gave `|S_20|/20! ≈ 2.11e-8` at `c=1` and `≈ 1.15e-27` at `c=13`, which supports Gevrey-0; the contradiction is the downstream Borel-singularity/Stokes interpretation, not the Gevrey label.

[HIGH] [compute/tests/test_resurgence_frontier_engine.py:447](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:447) — The singularity check is too weak to verify the claimed Borel singularities. It accepts any modulus ratio in `(0.01,100)`, and the actual module output is nowhere near the predicted locations: for `c=25`, `pade_pole_convergence(..., N=[20,30,40])` gave nearest moduli `70.82, 100.93, 28.13` while the predicted modulus is `1/rho = 4.1355`; for `c=13`, the nearest poles were around `37.35, 53.29, 63.65` while `1/rho = 2.1395`. The tests pass because the tolerance is permissive, not because the predicted singularity model is confirmed.

[HIGH] [compute/tests/test_resurgence_frontier_engine.py:1](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:1) — AP10/AP128 is not satisfied. This file contains many hardcoded expected values (`13/2`, `2.0`, `2*pi*i`, fixed `c`-grids, explicit pole/finite-value claims), but `rg -n "# VERIFIED|AP10|AP128|DC|LT|LC|SY|CF|NE|DA" compute/tests/test_resurgence_frontier_engine.py` returned no matches. There are no per-value 2-source verification annotations.

[HIGH] [compute/tests/test_btz_arithmetic_frontier_engine.py:23](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:23) — The file promises “Every numerical result verified by at least 3 independent paths,” but the inspected asymptotic surface still hardcodes uncited constants such as `0.5651591039924851`, `196884`, `21493760`, `864299970`, and the exact asymptotic limit `2.0` ([compute/tests/test_btz_arithmetic_frontier_engine.py:509](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:509), [compute/tests/test_btz_arithmetic_frontier_engine.py:537](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:537), [compute/tests/test_btz_arithmetic_frontier_engine.py:807](/Users/raeez/chiral-bar-cobar/compute/tests/test_btz_arithmetic_frontier_engine.py:807)). `rg` found only the mandate line, not the required `# VERIFIED` source trails.

[MEDIUM] [compute/lib/resurgence_frontier_engine.py:1145](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:1145) — The self-dual `c=13` Stokes multiplier is internally inconsistent. This docstring says `S_1` is real at the self-dual point, but the implementation hardcodes `stokes_multiplier_from_monodromy(...) = 2*pi*i` for all `c` ([compute/lib/resurgence_frontier_engine.py:726](/Users/raeez/chiral-bar-cobar/compute/lib/resurgence_frontier_engine.py:726)), and the tests explicitly assert it is purely imaginary ([compute/tests/test_resurgence_frontier_engine.py:544](/Users/raeez/chiral-bar-cobar/compute/tests/test_resurgence_frontier_engine.py:544)).

## Summary
Gevrey type itself looks correct: the shadow coefficient growth is consistent with Gevrey-0/sub-factorial behavior. The failure is the downstream resurgence story built on top of that label: the same surface then treats the corresponding Borel transform as if it had finite singularities and Stokes jumps. The exact requested selector `python3 -m pytest compute/tests/ -k 'stokes or asymptotic' --tb=short -q 2>&1 | tail -30` did not terminate during the audit window; a collect-only run found 890 selected tests, and targeted reruns passed (`compute/tests/test_resurgence_frontier_engine.py`: 97 passed; `compute/tests/test_btz_arithmetic_frontier_engine.py -k asymptotic`: 6 passed). Instances checked: 14 | Violations found: 5 | Verdict: FAIL
tokens used
114,569
