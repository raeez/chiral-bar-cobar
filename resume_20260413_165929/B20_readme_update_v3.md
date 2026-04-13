# B20_readme_update_v3 (126s)

Edited [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md) only.

- `FIXED` theorem status: changed `CY_3 functor (d=3)` from `Open` to `Conjectural`, with the conditional `S^3`-framing/quantization caveat, to match the manuscript’s `Theorem CY-A_2 / Conjecture CY-A_3` boundary.
- `FIXED` page count: changed `371` to `367`, verified from both `calabi_yau_quantum_groups.pdf` and `out/calabi_yau_quantum_groups.pdf`.
- `FIXED` test count: changed `19,785 collected` to `19,838 collected`, verified with `pytest compute/tests --collect-only -q`.

Verification: re-read the modified status/metrics block for coherence, then grepped `README.md` for the stale patterns (`CY_3 functor ... **Open**`, `Pages | 371`, `19,785 collected`) and found none. `\ref`/`\label` checks were not applicable because the assigned surface is Markdown, not LaTeX.


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
session id: 019d87dd-ad6e-7d61-b378-1e2488f6c0ab
--------
user
<task>
You are a SURGICAL FIX agent. Read the audit findings, read the source, make the MINIMUM
truthful edit that resolves each finding. Do NOT rewrite sections that are correct.
For each edit: verify it doesn't break surrounding context.
</task>
<action_safety>
Only edit files explicitly assigned. Keep changes tightly scoped.
After editing, re-read to verify coherence. Check \ref and \label validity.
</action_safety>
<completeness_contract>
Address EVERY finding listed. For each: state FIXED (how) or BLOCKED (why).
</completeness_contract>
<verification_loop>
After all edits, grep for forbidden patterns in the modified files.
</verification_loop>


TARGET: README.md (Vol III)
Same: update page count, test count, theorem status. No scope inflation.
mcp startup: no servers


thinking
**Planning inspection tasks**

I need to look at the README and potentially gather build/test counts from the repo. Checking the current page and test count, along with theorem status from live sources, seems important. I might want to inspect any changes in the README using git diff, and I should confirm the page count from the built PDF using pdfinfo. I'll find the test count references, which seems to be around 1,800+ tests. This audit seems necessary, and I should ensure regular updates.
thinking
**Starting commentary tasks**

I’m planning to begin commentary by using the vol3-beilinson-loop along with pre-edit verification. My first step will be to read the README to get a clear understanding. Then, I’ll check the differences with the git diff to see what has changed. Finally, I need to verify the surfaces to ensure everything is in order. This approach should help me organize my thoughts and ensure a thorough review!
codex
Using `vol3-beilinson-loop` and `vol3-pre-edit-verification` here because the assigned surface is a scoped rectification that touches advertised theorem status. I’m reading the live `README.md`, its current diff state, and the nearest verification surfaces for page count, test count, and status before editing.
exec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-beilinson-loop/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,260p' README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/vol3-pre-edit-verification/SKILL.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
---
name: vol3-beilinson-loop
description: Use when auditing, rectifying, falsifying, converging, or pressure-testing theorem, proof, formula, status, or scope material in the Calabi-Yau Quantum Groups repository. Trigger on audit, rectify, red-team, Beilinson, theorem status, proof gap, convergence, or "is this actually proved?" tasks.
---

# Vol III Beilinson Loop

Read `AGENTS.md` first. This skill is the triggered deep workflow for hostile mathematical review.

## Surface

Work on the live manuscript surface:

- `main.tex`
- currently `\input`-ed files
- the dirty git diff
- relevant build logs
- the narrowest relevant `compute/tests/` slice

## Passes
 succeeded in 51ms:
---
name: vol3-pre-edit-verification
description: Use before editing any high-risk Vol III formula, theorem status, d=3 existence claim, compute oracle, or cross-volume convention bridge. This is the Codex-native analogue of the Claude-side pre-edit verification templates.
---

# Vol III Pre-Edit Verification

Before editing a high-risk surface, fill in a fenced `PRE-EDIT` block in commentary and end with `verdict: ACCEPT` or `verdict: REJECT`.

If a required source is blank or any boundary check fails, do not edit yet.

## Triggers

- `r`-matrix or OPE/lambda-bracket edit
- `kappa` or modular-characteristic edit
- bar/cobar/desuspension formula
- theorem environment or claim-status edit touching d=3 objects
- shadow-class or SC-formality edit
- `MF(W)` CY-dimension edit
- cross-volume Part reference or copied formula
 succeeded in 52ms:
# Calabi-Yau Quantum Groups

**Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
by Raeez Lorgat.

The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.

## The Three Volumes

| Volume | Title | Role |
|:------:|-------|------|
| **I** | *Modular Koszul Duality* | The algebraic engine: bar-cobar duality for chiral algebras on curves |
| **II** | *A-infinity Chiral Algebras and 3D HT QFT* | The 3D interpretation: Swiss-cheese, PVA descent, gravity |
| **III** | *Calabi-Yau Quantum Groups* (this volume) | The categorical completion |

## The CY-to-Chiral Functor

The programme flow:

```
 succeeded in 51ms:
diff --git a/README.md b/README.md
index ccbf866..39ca020 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |


thinking
**Determining page and test counts**

I need to figure out the actual current page count and the status of tests, possibly by inspecting build artifacts. It might help to read through the README and related sources. I wonder if I could use grep for the page count or maybe pdfinfo on the built PDF. I should also look into the test counts from pytest or build logs. It looks like the README could have different counts, so verifying everything is essential.
thinking
**Investigating README changes**

I’m wondering if the user has already changed the README since the worktree has a diff. I don’t want to override anything unless it's necessary. I need to inspect the repository state and see if the current file already reflects changes from the audit. I should confirm if more edits are needed. The user mentioned they want a detailed fix regarding page count, test count, and theorem status. Let’s check for the latest counts in the PDF or README and explore the source or build logs for verification.
codex
The current `README.md` already has a live diff, so I’m treating it as a dirty surface rather than assuming it is correct. Next I’m verifying the advertised counts and status claims against the local build/test surface before deciding whether a further edit is needed.
exec
/bin/zsh -lc "rg --files -g '*.pdf'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"CY_3 functor|Open|Conjectural|chain-level S\\"'^3-framing|A_X does not yet exist|CoHA as E_1 sector|Drinfeld center" README.md chapters main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "find . -maxdepth 3 \\( -name '*.log' -o -name '*pytest*' -o -name '*test*summary*' \\) | sed -n '1,200p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"19,785|Compute tests|Tagged claims|Pages \\|\" README.md main.tex chapters compute tests -g '"'!build'"'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
working_notes.pdf
notes/physics_sduality_langlands.pdf
notes/physics_bv_brst_cy.pdf
notes/physics_wall_crossing_mc.pdf
notes/physics_4d_n2_hitchin.pdf
notes/theory_qvcg_koszul.pdf
notes/physics_mtheory_branes.pdf
notes/physics_anomaly_cancellation.pdf
notes/physics_celestial_cy.pdf
notes/physics_topological_strings.pdf
notes/theory_6d_hcs_chiral_qg.pdf
calabi_yau_quantum_groups.pdf
main.pdf
out/calabi_yau_quantum_groups.pdf
out/working_notes.pdf
 succeeded in 51ms:
README.md:34:For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfaces). For d=3: conditional on chain-level S^3-framing; the chiral algebra A_X does not yet exist.
README.md:40:| Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
README.md:43:| R-matrix braiding | Vol II, Part III | Abstract E_1 -> E_2 lift via Drinfeld center; d=3 applications require the E_1 input |
README.md:48:- **II. The CY Characteristic Datum**: CY-to-chiral functor Phi, quantum chiral algebras, modular trace, quantum group foundations, braided factorization (U_q(g), R-matrix, YBE from bar coassociativity, braided bar-cobar adjunction CY-B, braided shadow tower), Drinfeld center and bulk algebras (BZF theorem, center vs derived center, Kazhdan-Lusztig at roots of unity)
README.md:59:| CoHA as E_1 sector (toric CY3) | **Proved** |
README.md:60:| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
README.md:61:| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
README.md:62:| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
README.md:63:| Langlands = Koszul | **Conjectural** |
chapters/examples/fukaya_categories.tex:523: is recovered via the Drinfeld center
chapters/examples/fukaya_categories.tex:555:afterwards through the Drinfeld center.
chapters/examples/fukaya_categories.tex:649:\section{Open-string sector and the Swiss-cheese structure}
chapters/examples/fukaya_categories.tex:658:\begin{proposition}[Open-closed map from Fukaya categories]
chapters/examples/k3_times_e.tex:173: \item \textbf{(Conjectural.)} The $E_2$-structure should come from the $\mathrm{Sp}_4(\mathbb{Z})$-action on $\mathbb{H}_2$, connecting genus-2 modular structure to braided monoidal structure via the modular functor. Spelling this out requires the full machinery of Section~3 and the $d = 3$ extension.
chapters/examples/k3_times_e.tex:1951:For the $K3 \times E$ chiral algebra (class~$M$, infinite shadow depth), the decomposition of the $\cN = 4$ superconformal character into massless and massive sectors produces a mock modular form $h(\tau) = 2q^{-1/8}(-1 + 45q + 231q^2 + \cdots)$ with shadow $S(\tau) = 24\,\eta(\tau)^3$. The polar coefficient $h|_{q^{-1/8}} = -2 = -\kappa_{\mathrm{ch}}(A_{K3})$: the chiral modular characteristic is the leading mock modular coefficient. The pattern across shadow classes: class~$G$ produces genuine modular forms (semisimple Drinfeld center); class~$M$ produces mock modular forms (logarithmic, non-semisimple center). The mock shadow is $\kappa_{\mathrm{ch}} \cdot \chi(K3) \cdot \eta^3 = 48\,\eta^3$. The connection class~$M \Longrightarrow$ logarithmic center is a strong conjecture supported by all computed examples but requiring resolution of the pointwise convergence obstruction in the Drinfeld center computation (Remark~\ref{rem:three-centers-sharp}).
chapters/examples/derived_categories_cy.tex:174:Across all three examples the pattern is the same: Beilinson quiver $\to$ superpotential $\to$ critical CoHA $\to$ positive half of an affine (super) Yangian $\to$ $\Eone$-sector of the Vol~III chiral algebra, via the CY-to-chiral functor for toric CY$_3$ without compact $4$-cycles (Theorem~\ref{thm:rsyz}). The passage from $\Eone$ to $\Etwo$ requires the Drinfeld center, and is developed in Chapter~\ref{ch:drinfeld-center}. In every case the modular characteristic is of type $\kappa_{\mathrm{cat}}$ (holomorphic Euler characteristic of the base Fano) and must be distinguished from $\kappa_{\mathrm{ch}}$ (computed intrinsically from the resulting chiral algebra); agreement between the two is a prediction of the functor, verified at $d = 2$ and conjectural at $d = 3$.
chapters/examples/toric_cy3_coha.tex:415:with the Drinfeld center identification conditional on Conjecture~CY-C
chapters/examples/toric_cy3_coha.tex:600:$\Rep^{\Etwo}(\mathcal{G}(X))$ is recovered by the Drinfeld center:
chapters/examples/toric_cy3_coha.tex:605:the Drinfeld center of the CoHA representation category
chapters/examples/toric_cy3_coha.tex:609:The difficulty is that the Drinfeld center does not commute with
 succeeded in 51ms:
./.pytest_cache
./.build_logs/working-notes.log
./.build_logs/tex-build.stdout.log
./working_notes.log
./main.log
 exited 2 in 51ms:
rg: tests: No such file or directory (os error 2)
README.md:68:| Pages | 371 |
README.md:73:| Tagged claims | 451 |
README.md:74:| Compute tests | 19,785 collected |

thinking
**Inspecting files and counts**

I need to get the actual page count using pdfinfo. For test counts, I might check pytest collection or the logs. There’s a possibility I could use `rg` in `.pytest_cache`, but using `pytest --collect-only` might be expensive. I wonder if there’s even a tests directory because of naming issues. I’ll have to inspect the repo structure and the README says there are 19,785 collected tests; I should verify that. Additionally, I need to check the current page count, which might be 371. I’ll use pdfinfo to figure out which PDF is Volume III.
codex
I have the README surface and the manuscript status language. I still need the hard numbers from executable artifacts, because the count lines are the part most likely to drift silently.
exec
/bin/zsh -lc "find compute -maxdepth 3 \\( -type d -name 'tests' -o -type f -name 'test_*.py' \\) | sed -n '1,200p'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "pdfinfo out/calabi_yau_quantum_groups.pdf | rg 'Pages|Title'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "pdfinfo calabi_yau_quantum_groups.pdf | rg 'Pages|Title'" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "rg -n \"collected|passed|failed|errors\" .pytest_cache .build_logs compute README.md -g '"'!*.pdf'"'" in /Users/raeez/calabi-yau-quantum-groups succeeded in 52ms:
compute/tests
compute/tests/test_tilting_chart_cy3.py
compute/tests/test_categorified_e1_shadow_engine.py
compute/tests/test_quintic.py
compute/tests/test_celestial_e1_chart_bridge.py
compute/tests/test_kw_twisted_n4_chiral.py
compute/tests/test_kl_sl2.py
compute/tests/test_higgs_bundle_chiral.py
compute/tests/test_chiral_coproduct_general_engine.py
compute/tests/test_e1_chiral_bialgebra.py
compute/tests/test_cech_descent_e1.py
compute/tests/test_ks_hocolim_equivalence.py
compute/tests/test_hms_e1_chart_compatibility.py
compute/tests/test_borcherds_lift.py
compute/tests/test_coha_chart_explicit.py
compute/tests/test_modular_cy_characteristic.py
compute/tests/test_nontoric_chart_atlas.py
compute/tests/test_hcs_codim2_defect_ope.py
compute/tests/test_psi34_fock_matrices.py
compute/tests/test_local_p2_shadow.py
 succeeded in 51ms:
Title:           
Pages:           367
 succeeded in 51ms:
Title:           
Pages:           367
 succeeded in 52ms:
Total output lines: 482

README.md:74:| Compute tests | 19,785 collected |
compute/tests/test_bar_hocolim_commutation.py:786:        assert "all_passed" in results
compute/tests/test_bar_hocolim_commutation.py:788:    def test_grand_verification_all_passed(self):
compute/tests/test_bar_hocolim_commutation.py:791:        assert results["all_passed"] is True
compute/lib/k3_yangian.py:546:                'failed_at_n': n_test,
compute/tests/test_toric_cy3_e1_landscape.py:235:            assert ok, f"Pick's theorem failed for {name}"
compute/tests/test_toric_cy3_e1_landscape.py:839:            assert ok, f"kappa cross-verification failed for {name}"
compute/tests/test_toric_cy3_e1_landscape.py:962:                assert val, f"Finite genus failed for {key}"
compute/tests/test_toric_cy3_e1_landscape.py:1291:            assert ok, f"Pick's theorem failed for {name}"
compute/tests/test_coha_gluing_morphisms.py:647:            assert result == expected, f"Roundtrip failed at beta={beta}"
compute/tests/test_coha_gluing_morphisms.py:658:            assert result == expected, f"K^-1 o K failed at beta={beta}"
compute/tests/test_coha_gluing_morphisms.py:680:            assert result == expected, f"A3 roundtrip failed at {beta}"
compute/tests/test_coha_gluing_morphisms.py:1047:            assert result_a == expected, f"Method 1 failed at {beta}"
compute/tests/test_coha_gluing_morphisms.py:1048:            assert result_b == expected, f"Method 2 failed at {beta}"
compute/tests/test_coha_gluing_morphisms.py:1155:            assert result == expected, f"Composed inverse failed at {beta}"
compute/tests/test_hocolim_costello_li_comparison.py:546:        assert result['passed']
compute/tests/test_hocolim_costello_li_comparison.py:552:        assert result['passed']
compute/tests/test_hocolim_costello_li_comparison.py:557:        assert result['passed']


thinking
**Verifying test and page counts**

I need to figure out the count of collected tests, so I'll try running the pytest command with the `--collect-only` option on the compute/tests. Although it might be expensive, it should be fine. I could narrow it down with `pytest compute/tests --collect-only -q` to count lines or get a summary. It's possible there are around 19,785 collected tests. I'll also verify the page count from pdfinfo, which shows 367, not 371, so there’s a discrepancy to check.
thinking
**Deciding on test count update**

I need to determine whether the claimed count of 19,785 should be updated. To do this, I’ll run a collection count. If the number of tests is large, running them could be expensive, but using the `--collect-only -q` option should prevent actual test execution, just importing modules, which may take some time. A more efficient way could be to use `pytest compute/tests --collect-only -q 2>/dev/null | tail -n 20` to retrieve the last lines or a summary. Let’s go ahead and run that.
codex
The build artifact check already falsified one README number: the volume PDF on disk is `367` pages, not `371`. I’m now checking the test collection count directly so the metrics line is grounded the same way.
exec
/bin/zsh -lc "python - <<'PY'
from pathlib import Path
root = Path('compute/tests')
print(sum(1 for _ in root.rglob('test_*.py')))
PY" in /Users/raeez/calabi-yau-quantum-groups exited 127 in 52ms:
zsh:1: command not found: python
exec
/bin/zsh -lc 'pytest compute/tests --collect-only -q' in /Users/raeez/calabi-yau-quantum-groups succeeded in 3.39s:
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_standard_generators_exist
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_spins
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_degrees_zero
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_derivative_generators
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_repr
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_frozen
compute/tests/test_a_infinity_bar_w1inf.py::TestWGenerator::test_hashable
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_arity
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_total_spin
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_cohomological_degree
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_repr_unit_coeff
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_repr_neg_coeff
compute/tests/test_a_infinity_bar_w1inf.py::TestAInfBarElement::test_repr_general_coeff
compute/tests/test_a_infinity_bar_w1inf.py::TestLinearCombination::test_zero
compute/tests/test_a_infinity_bar_w1inf.py::TestLinearCombination::test_simplify_cancellation
compute/tests/test_a_infinity_bar_w1inf.py::TestLinearCombination::test_simplify_collection
compute/tests/test_a_infinity_bar_w1inf.py::TestLinearCombination::test_add
compute/tests/test_a_infinity_bar_w1inf.py::TestW1InfOPE::test_jj_ope
compute/tests/test_a_infinity_bar_w1inf.py::TestW1InfOPE::test_tt_ope_poles
compute/tests/test_a_infinity_bar_w1inf.py::TestW1InfOPE::test_tt_central_charge

thinking
**Evaluating Python commands**

I need to check the poll pytest thing. It seems like my Python command failed because it couldn't find a python alias. So, I should use python3 instead. It's a small detail, but it's essential to get the right command to avoid errors. I guess it's just one of those things I have to remember when working with Python, especially on systems where the alias might not be set up. Let's keep moving forward!
codex
Collection is still running. The quick side check failed because this environment has `python3`, not `python`; I’ll use `python3` only if I need a non-editing count helper.
exec
/bin/zsh -lc "python3 - <<'PY'
from pathlib import Path
root = Path('compute/tests')
print(sum(1 for _ in root.rglob('test_*.py')))
PY" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
229
codex
The quantitative lines are now pinned: `367` pages from the built PDF and `19,838 tests collected` from `pytest --collect-only`. I’m doing one last status check against the manuscript so the README doesn’t advertise a stronger d=3 theorem state than the source text supports.
exec
/bin/zsh -lc "rg -n \"CY-A\\"'$_3|Conjecture~CY-A|Theorem~CY-A|ClaimStatus(ProvedHere|Conditional|Conjectured|Open)|d = 3.*conditional|d = 3.*conjectur|open programme" chapters/theory/introduction.tex chapters/theory/cy_to_chiral.tex chapters/frame/preface.tex main.tex' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '1898,1925p' chapters/theory/cy_to_chiral.tex" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '270,315p' chapters/theory/introduction.tex" in /Users/raeez/calabi-yau-quantum-groups succeeded in 51ms:
main.tex:139:\newcommand{\ClaimStatusProvedHere}{\textsuperscript{\textsc{[ph]}}}
main.tex:141:\newcommand{\ClaimStatusConjectured}{\textsuperscript{\textsc{[cj]}}}
main.tex:143:\newcommand{\ClaimStatusOpen}{\textsuperscript{\textsc{[op]}}}
main.tex:144:\newcommand{\ClaimStatusConditional}{\textsuperscript{\textsc{[cd]}}}
main.tex:349:steps are proved (Theorem~CY-A). For $d = 3$, holomorphic
chapters/frame/preface.tex:54:are proved (Theorem~CY-A$_2$). For $d = 3$, holomorphic
chapters/frame/preface.tex:678:(Theorem~CY-A$_2$) and is a programme for $d = 3$, conditional on
chapters/frame/preface.tex:815:algebras and proves Theorem~CY-A$_2$ for $d = 2$, with the
chapters/theory/introduction.tex:26:For $d = 2$, the functor $\Phi$ sends a CY category $\cC$ (Fukaya, derived, matrix factorization, or more general) to a chiral algebra $A_\cC$ whose bar complex $B(A_\cC)$ encodes the CY cyclic homology, with the CY trace realized as the modular characteristic $\kappa_{\mathrm{ch}}(A_\cC)$. For $d = 3$, the analogous output is conditional on the chain-level $\mathbb{S}^3$-framing programme and is not yet available in general.
chapters/theory/introduction.tex:244:The combinatorics of a Calabi--Yau threefold $X$ (lattice, intersection form, BPS spectrum) constitute the \emph{generalized root datum} of a \emph{quantum vertex chiral group} $G(X)$. For toric CY3 (via the CoHA and Drinfeld double) and for CY$_2$ categories (via Theorem~CY-A$_2$), this object is constructed. For general CY$_3$, including the prototype $K3 \times E$, $G(X)$ is the target of a programme (Conjecture~CY-A$_3$), not a constructed object.
chapters/theory/introduction.tex:286: \item \textbf{CY-A} (Theorem~CY-A$_2$ / Conjecture~CY-A$_3$): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
chapters/theory/introduction.tex:289: \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
chapters/theory/introduction.tex:520:\emph{Fukaya categories} (Chapter~\ref{ch:fukaya}). The symplectic input. For an elliptic curve $E_\tau$, the Fukaya category $\Fuk(E_\tau)$ is CY of dimension~$1$ and $\Phi$ produces the Heisenberg vertex algebra $H_k$ at level $k = \mathrm{vol}(E_\tau)$. For a K3 surface~$S$, $\Fuk(S)$ is CY of dimension~$2$ and $\Phi$ produces an $E_2$-chiral algebra with $\kappa_{\mathrm{ch}} = \chi(\mathcal{O}_S) = 2$. For compact CY threefolds, the Fukaya-side functor is conditional on the chain-level $\mathbb{S}^3$-framing (Conjecture~CY-A$_3$); the open-string sector ($\Fuk(X)$ with Lagrangian boundary conditions) connects to the Volume~II Swiss-cheese structure. Wrapped Fukaya categories $\mathcal{W}(X)$ of Liouville manifolds provide the non-compact analogue: for cotangent bundles $T^*M$, Abouzaid's equivalence $\mathcal{W}(T^*M) \simeq \mathrm{Mod}(C_*(\Omega M))$ reduces the CY-to-chiral functor to the based loop space.
chapters/theory/introduction.tex:524:\emph{Matrix factorizations}. The Landau--Ginzburg input. A polynomial $W \colon \mathbb{C}^n \to \mathbb{C}$ gives a CY category $\mathrm{MF}(W)$ of dimension $n - 2$. For ADE singularities $W = x^N + y^2 + z^2 + w^2$ in four variables, $\mathrm{MF}(W)$ is CY of dimension~$2$ and $\Phi$ (Theorem~CY-A$_2$) produces chiral algebras related to $\mathcal{W}_N$-algebras. The LG/CY correspondence $\mathrm{MF}(W) \simeq D^b(\mathrm{Coh}(X_W))$ provides a further consistency check against the derived-category side. For non-ADE singularities (unimodal, bimodal), the resulting chiral algebras are expected to be new objects not realized by the standard Lie-theoretic landscape of Volume~I.
chapters/theory/cy_to_chiral.tex:34:\ClaimStatusProvedHere{}
chapters/theory/cy_to_chiral.tex:49:\ClaimStatusProvedHere{}
chapters/theory/cy_to_chiral.tex:67:\ClaimStatusConjectured{}
chapters/theory/cy_to_chiral.tex:76:At $d = 2$, the identification is proved (Proposition~\textup{\ref{prop:cy-kappa-d2}}). At $d = 3$, the conjecture is verified for $\C^3$ where both sides are independently computable ($\kappa_{\mathrm{ch}} = \kappa_{\mathrm{cat}} = 1$; see Theorem~\textup{\ref{thm:kappa-c3}}). The obstruction to extending the $d = 2$ proof is that the $d = 3$ quantization step may introduce corrections: Serre duality $\mathbb{S}_\cC \simeq [3]$ no longer kills the one-loop anomaly by parity. The $d = 3$ functor itself is conjectural beyond $\C^3$.
chapters/theory/cy_to_chiral.tex:100:\ClaimStatusConjectured{}
chapters/theory/cy_to_chiral.tex:131:\ClaimStatusConjectured{}
 succeeded in 52ms:
 \midrule
 $\kappa_{\mathrm{ch}}$ (degree 2) & Weyl vector $\rho$ contribution & Leading DT invariant \\
 $C$ (degree 3, cubic) & First imaginary root corrections & Genus-0 3-point function \\
 $Q$ (degree 4, quartic) & Higher imaginary roots & Genus-0 4-point function \\
 Full $\Theta_A$ & Complete automorphic correction & Full BPS generating function \\
 \bottomrule
\end{tabular}
\end{center}
The denominator identity of $\mathfrak{g}_X$ ($\Delta_5$ for $K3 \times E$, the DT partition function for toric CY3) should be the bar-complex Euler product of the quantum vertex chiral group, when that group exists. For toric CY3 this identification is part of Conjecture~CY-C. For $K3 \times E$, since $A_{K3 \times E}$ is not yet constructed, the product formula for $\Delta_5$ is an \emph{observation} about the Borcherds lift, not a theorem derived from the bar complex.

The bar Euler product of lattice VOAs recovers the Borcherds denominator identity (verified for $E_8$ and Leech lattice; conditional on CY-A$_3$ for $K3 \times E$).

\section{Main results}
\label{sec:main-results}

\begin{itemize}
 \item \textbf{CY-A} (Theorem~CY-A$_2$ / Conjecture~CY-A$_3$): Construction of $\Phi \colon \CY_d\text{-}\Cat \to E_2\text{-}\mathrm{ChirAlg}$ via the factorization envelope and $\mathbb{S}^d$-framing. \emph{Proved for $d = 2$} (CY surfaces, where the $\mathbb{S}^2$-framing gives $E_2$ via Kontsevich--Vlassopoulos). \emph{For $d = 3$}: a programme conditional on (a)~constructing the chain-level $\mathbb{S}^3$-framing compatible with BV structure and (b)~the quantization step. The $\mathbb{S}^3$-framing gives an $E_3$-structure, from which $E_2$ is obtained by restriction; however, $\pi_1(\mathrm{Conf}_2(\mathbb{R}^3))$ is trivial, so the restriction gives a symmetric braiding at the topological level. The quantum group braiding for $d = 3$ is expected to arise through the Drinfeld center of $E_1$-monoidal categories.
 \item \textbf{Theorem CY-B} ($E_2$-chiral Koszul duality; \emph{conditional}): Bar-cobar adjunction in the $E_2$-chiral setting. Items (i)--(ii) follow from the Volume~I machine applied to each $E_1$-direction via Dunn additivity; the full $E_2$-equivariant refinement (coherent intertwining by the $R$-matrix) is established as a rigorous proof sketch, with detailed verification of higher coherences deferred. In the CY$_3$ applications, the further identification of automorphic correction with the shadow obstruction tower and of the denominator identity with the bar-complex Euler product remains a conjectural target rather than a proved consequence.
 \item \textbf{Conjecture CY-C} (Quantum group realization): For toric CY3, $\Rep^{E_2}(G(X))$ should be braided monoidal equivalent to $\Rep(Y(\widehat{\mathfrak{g}}_{Q_X}))$; for $K3 \times E$, the $\Sp_4(\mathbb{Z})$-module structure on the denominator identity should recover the braided structure. The critical CoHA is the $E_1$-sector (positive half). The CY category $\cC(\frakg, q)$ is not yet constructed in general.
 \item \textbf{Theorem CY-D} (Modular CY characteristic): For $d = 2$, $\kappa_{\mathrm{ch}}(\Phi(\cC))$ equals the CY Euler characteristic $\chi^{\CY}(\cC)$. For $K3 \times E$ ($d = 3$), the Borcherds weight gives the distinct automorphic invariant $\kappa_{\mathrm{BKM}} = 5$; without $A_{K3 \times E}$ (which is not constructed), this is an observation matching the Borcherds lift weight formula, not a computation from the Volume~I definition of $\kappa_{\mathrm{ch}}$. The general $d = 3$ formula is conjectural.
 succeeded in 52ms:
\renewcommand{\arraystretch}{1.3}
\small
\begin{tabular}{llp{7cm}}
 \toprule
 \textbf{Component} & \textbf{Status} & \textbf{Evidence} \\
 \midrule
 Functor chain for $\C^3$ & \textbf{Verified} & End-to-end: PV$^*$ $\to$ $\Omega$-deformation $\to$ $Y^+(\widehat{\fgl}_1)$ $\to$ Drinfeld center $\to$ $\cW_{1+\infty}$ (\S\ref{sec:d3-functor-chain}) \\
 $\bS^3$-framing obstruction & \textbf{Topol.\ trivial} & $\pi_3(B\Sp) = \pi_3(BU) = 0$ (Thm.~\ref{thm:s3-framing-vanishes}) \\
 $\Eone \to \Etwo$ enhancement & \textbf{Trivial, all tested} & CY condition $g(z)g(-z) = 1$ (Cor.~\ref{cor:e1-e2-trivial}) \\
 Bar complex identification & \textbf{Verified} & Euler product $= 1/M(q)$ (Prop.~\ref{prop:c3-bar-euler}) \\
 $\kappa_{\mathrm{ch}}(\C^3)$ & \textbf{5-path verified} & $\kappa_{\mathrm{ch}} = 1$ (Thm.~\ref{thm:kappa-c3}) \\
 Toric CY$_3$ chart gluing & \textbf{Proved} & Hocolim of McKay chart CoHAs $=$ CL boundary algebra (Thm.~\ref{thm:toric-chart-gluing}); 133 tests \\
 \midrule
 Compact CY$_3$ chain-level & Open & Holomorphic CS provides trivialization, but $\Ainf$-compatibility not checked \\
 $\kappa_{\mathrm{ch}}$ formula for K3-fibered & Partial & Verified for $K3 \times E$ and Enriques $\times E$; conjectural beyond \\
 Motivic DT identification & Open & Correct at motivic level, not at naive BCH level \\
 \bottomrule
\end{tabular}
\end{center}


thinking
**Adjusting audit details**

I need to think about adjusting the top paragraph because the audit suggests updating the page count, test count, and theorem status. There shouldn't be any scope inflation. It seems like I might only need to make minimal changes to lines 61, 68, and 74, and possibly the row as well. I'm also considering if the phrase "open programme" should be part of the theorem status and whether we should leave it as is.
codex
```text
## PRE-EDIT: d=3 status
statement: README status row for the d=3 CY-to-chiral functor
depends on unconstructed object?: yes; general d=3 output and A_X are not constructed in general
environment: README status table (advertised theorem/programme status, not theorem environment)
claim status: Conjectured for CY-A_3; conditional dependencies include chain-level S^3-framing and quantization
dependency chain: chapters/theory/introduction.tex (Theorem CY-A_2 / Conjecture CY-A_3) + chapters/theory/cy_to_chiral.tex ("the d=3 functor itself is conjectural beyond C^3")
verdict: ACCEPT
```

```text
## PRE-EDIT: compute oracle
claim: README metric lines for page count and collected test count
path 1: pdfinfo calabi_yau_quantum_groups.pdf -> Pages: 367
path 2: pdfinfo out/calabi_yau_quantum_groups.pdf -> Pages: 367
path 3: pytest compute/tests --collect-only -q -> 19838 tests collected in 1.84s
source and normalization: live built PDFs on disk; live pytest collection over compute/tests
engine/test independence: page count comes from PDF metadata; test count comes from pytest collection rather than README or file-count heuristics
verdict: ACCEPT
```

I’m making a three-line README patch only: d=3 status wording, page count, and collected test count. After that I’ll re-read the modified block and grep the modified file for the superseded values.
file update
M /Users/raeez/calabi-yau-quantum-groups/README.md
@@ -60,3 +60,3 @@
 | Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
-| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
+| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
@@ -67,3 +67,3 @@
 |--------|------:|
-| Pages | 371 |
+| Pages | 367 |
 | Theory chapters | 13 |
@@ -73,3 +73,3 @@
 | Tagged claims | 451 |
-| Compute tests | 19,785 collected |
+| Compute tests | 19,838 collected |
 | Compute modules | 196 lib + 204 test |
apply_patch(auto_approved=true) exited 0 in 21ms:
Success. Updated the following files:
M README.md
file update:
diff --git a/README.md b/README.md
index 39ca020262234213a343201cb0b8c9c08ba80c70..ecf56af57769e469360e7879dd3516c3f5e6b98d
--- a/README.md
+++ b/README.md
@@ -58,20 +58,20 @@
 | Lattice VOA bridge | **Proved** |
 | CoHA as E_1 sector (toric CY3) | **Proved** |
 | Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
-| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
+| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | 371 |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
 | Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
 | Working notes | Separate PDF in build |
 | Tagged claims | 451 |
-| Compute tests | 19,785 collected |
+| Compute tests | 19,838 collected |
 | Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

file update:
diff --git a/README.md b/README.md
index 39ca020262234213a343201cb0b8c9c08ba80c70..ecf56af57769e469360e7879dd3516c3f5e6b98d
--- a/README.md
+++ b/README.md
@@ -58,20 +58,20 @@
 | Lattice VOA bridge | **Proved** |
 | CoHA as E_1 sector (toric CY3) | **Proved** |
 | Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
-| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
+| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | 371 |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
 | Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
 | Working notes | Separate PDF in build |
 | Tagged claims | 451 |
-| Compute tests | 19,785 collected |
+| Compute tests | 19,838 collected |
 | Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

codex
The patch is in. I’m re-reading the touched block now and then running an explicit stale-pattern grep against `README.md` so the old counts/status do not survive anywhere in the modified file.
exec
/bin/zsh -lc "rg -n \"\\| CY_3 functor \\(d=3\\) \\| \\*\\*Open\\*\\*|\\| Pages \\| 371 \\||19,785 collected\" README.md" in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc 'git diff -- README.md' in /Users/raeez/calabi-yau-quantum-groupsexec
/bin/zsh -lc "sed -n '54,78p' README.md" in /Users/raeez/calabi-yau-quantum-groups succeeded in 50ms:

| Component | Status |
|-----------|--------|
| CY_2 functor (d=2) | **Proved** |
| Lattice VOA bridge | **Proved** |
| CoHA as E_1 sector (toric CY3) | **Proved** |
| Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
| BKM = shadow tower | **Conjectural** (requires d=3 functor) |
| Langlands = Koszul | **Conjectural** |
| BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |

| Metric | Value |
|--------|------:|
| Pages | 367 |
| Theory chapters | 13 |
| Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
| Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
| Working notes | Separate PDF in build |
| Tagged claims | 451 |
 exited 1 in 52ms:

 succeeded in 50ms:
diff --git a/README.md b/README.md
index ccbf866..ecf56af 100644
--- a/README.md
+++ b/README.md
@@ -3,7 +3,7 @@
 **Volume III** of *Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves*
 by Raeez Lorgat.
 
-The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is the root datum of a quantum vertex chiral group G(X). The bar-complex Euler product recovers the BKM denominator identity, and the shadow obstruction tower of Vol I organizes the BPS root multiplicities. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification is a precisely scoped conjecture whose central obstruction is the construction of the CY-to-chiral functor.
+The combinatorial skeleton of a Calabi-Yau category (its lattice, BPS spectrum, and symmetries) is expected to determine the root datum of a quantum vertex chiral group G(X). When that chiral object exists, its bar-complex Euler product recovers the BKM denominator identity, and Vol I's shadow obstruction tower organizes the corresponding root-multiplicity data. Proved for d=2 (Yangians, elliptic Hall algebras); for d=3 the identification remains a precisely scoped open programme whose central obstruction is the construction of the CY-to-chiral functor.
 
 ## The Three Volumes
 
@@ -38,9 +38,9 @@ For d=2: the functor exists (Yangians from quivers, elliptic Hall from K3 surfac
 | Input | Source | Role in Vol III |
 |-------|--------|-----------------|
 | Shadow obstruction tower Theta_A | Vol I, Theorem D + MC2 | Conjecturally = automorphic correction of BKM |
-| E_1 ordered bar B^{ord}(A) | Vol II, Part II | CoHA = E_1-sector of quantum vertex chiral group |
+| E_1 ordered bar B^{ord}(A) | Vol II, Part II | Toric CY3: proved E_1 sector; general d=3 use remains conditional |
 | Modular characteristic kappa(A) | Vol I, Theorem D | Real roots + Weyl vector of BKM algebra |
file update:
diff --git a/README.md b/README.md
index 39ca020262234213a343201cb0b8c9c08ba80c70..ecf56af57769e469360e7879dd3516c3f5e6b98d
--- a/README.md
+++ b/README.md
@@ -58,20 +58,20 @@
 | Lattice VOA bridge | **Proved** |
 | CoHA as E_1 sector (toric CY3) | **Proved** |
 | Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
-| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
+| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | 371 |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
 | Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
 | Working notes | Separate PDF in build |
 | Tagged claims | 451 |
-| Compute tests | 19,785 collected |
+| Compute tests | 19,838 collected |
 | Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

codex
Edited [README.md](/Users/raeez/calabi-yau-quantum-groups/README.md) only.

- `FIXED` theorem status: changed `CY_3 functor (d=3)` from `Open` to `Conjectural`, with the conditional `S^3`-framing/quantization caveat, to match the manuscript’s `Theorem CY-A_2 / Conjecture CY-A_3` boundary.
- `FIXED` page count: changed `371` to `367`, verified from both `calabi_yau_quantum_groups.pdf` and `out/calabi_yau_quantum_groups.pdf`.
- `FIXED` test count: changed `19,785 collected` to `19,838 collected`, verified with `pytest compute/tests --collect-only -q`.

Verification: re-read the modified status/metrics block for coherence, then grepped `README.md` for the stale patterns (`CY_3 functor ... **Open**`, `Pages | 371`, `19,785 collected`) and found none. `\ref`/`\label` checks were not applicable because the assigned surface is Markdown, not LaTeX.
file update:
diff --git a/README.md b/README.md
index 39ca020262234213a343201cb0b8c9c08ba80c70..ecf56af57769e469360e7879dd3516c3f5e6b98d
--- a/README.md
+++ b/README.md
@@ -58,20 +58,20 @@
 | Lattice VOA bridge | **Proved** |
 | CoHA as E_1 sector (toric CY3) | **Proved** |
 | Drinfeld center lift E_1 -> E_2 | **Proved elsewhere** (d=3 applications remain conditional) |
-| CY_3 functor (d=3) | **Open** (the programme is conditional on chain-level S^3-framing) |
+| CY_3 functor (d=3) | **Conjectural** (the programme is conditional on chain-level S^3-framing and quantization) |
 | BKM = shadow tower | **Conjectural** (requires d=3 functor) |
 | Langlands = Koszul | **Conjectural** |
 | BKM side verification | K3 x E: 271 tests (Borcherds product, root multiplicities) |
 
 | Metric | Value |
 |--------|------:|
-| Pages | 371 |
+| Pages | 367 |
 | Theory chapters | 13 |
 | Example chapters | 6 (with `K3 x E` merged into `toroidal_elliptic`) |
 | Connection chapters | 4 (including restored `modular_koszul_bridge` + `geometric_langlands`) |
 | Working notes | Separate PDF in build |
 | Tagged claims | 451 |
-| Compute tests | 19,785 collected |
+| Compute tests | 19,838 collected |
 | Compute modules | 196 lib + 204 test |
 | Anti-patterns | AP-CY1 through AP-CY19 + AP150-AP157 + FM24 |
 | HOT ZONE entries | HZ3-1 through HZ3-10 (Vol III-specific operational templates) |

tokens used
75,466
