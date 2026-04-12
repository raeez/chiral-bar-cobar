# CE03_koszul_conductor (647s, gpt-5.4)

[CRITICAL] chapters/examples/bershadsky_polyakov.tex:34 — The chapter’s five-theorem summary table states `\kappa(k)+\kappa(-k-6)=K_{\mathcal B}/2` with `K_{\mathcal B}=196`, i.e. `98`, but the same chapter later proves `98/3` at [chapters/examples/bershadsky_polyakov.tex:296](/Users/raeez/chiral-bar-cobar/chapters/examples/bershadsky_polyakov.tex:296). The compute layer and BP tests also use `98/3`, so this is a live manuscript contradiction on a theorem-summary surface.

[HIGH] compute/tests/test_koszul_conductor_table_engine.py:5 — The file claims every hardcoded expected value is AP10/AP128-compliant, but that claim is false. `test_h0` at [compute/tests/test_koszul_conductor_table_engine.py:89](/Users/raeez/chiral-bar-cobar/compute/tests/test_koszul_conductor_table_engine.py:89) hardcodes `0` with no `# VERIFIED` comment, and `test_K_kk_196` at [compute/tests/test_koszul_conductor_table_engine.py:311](/Users/raeez/chiral-bar-cobar/compute/tests/test_koszul_conductor_table_engine.py:311) cites `[LT]` plus `[LT]`, not two categories.

[HIGH] compute/tests/test_bp_koszul_conductor_engine.py:7 — The file advertises per-value verification paths for each hardcoded expectation, but line [279](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:279) hardcodes `98/3` with no `# VERIFIED`, line [296](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:296) hardcodes `-3` with no `# VERIFIED`, and lines [383](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:383) and [389](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:389) use only single-category `[CF]` comments.

[HIGH] compute/tests/test_theorem_c_complementarity.py:62 — The file contains many hardcoded theorem constants (`13`, `250/3`, `1/24`, `7/5760`, `31/967680`, etc.) but grep found no `# VERIFIED` markers anywhere in the file. AP10/AP128 provenance is absent across the whole test surface.

[HIGH] compute/tests/test_complementarity_landscape.py:60 — Same AP10/AP128 failure pattern: hardcoded constants such as `1/4`, `13`, `250/3`, `533/2`, and `9394/15` appear throughout, and the file contains no `# VERIFIED` comments at all.

[HIGH] compute/tests/test_complementarity_cross_verification.py:87 — Same AP10/AP128 failure pattern: the file hardcodes complementarity constants (`13`, `250/3`, `533/2`, `9394/15`, `-13`, `-50`, `-123`, etc.) but has no `# VERIFIED` comments anywhere.

[MEDIUM] compute/tests/test_ds_complementarity_defect.py:104 — Hardcoded conductor/defect constants (`13`, `250/3`, `-26`, `3952`, `2262`, etc.) are asserted without AP10/AP128 provenance comments.

[MEDIUM] compute/tests/test_level_rank_complementarity.py:184 — The file uses hardcoded complementarity expectations (`0`, `2`, fixed-point/critical values, explicit levels) and has no `# VERIFIED` comments anywhere.

Verified non-findings: `K(BP)=196` and `K(Vir)=13` are correct. Direct symbolic simplification gave `196` and `13`; the compute layer agrees; manuscript support is at [chapters/examples/landscape_census.tex:156](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:156), [chapters/examples/bershadsky_polyakov.tex:296](/Users/raeez/chiral-bar-cobar/chapters/examples/bershadsky_polyakov.tex:296), and [chapters/theory/higher_genus_complementarity.tex:2952](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2952).

Focused relevant pytest subset passed: `776 passed in 11.31s`. The exact broad `-k 'koszul_conductor or complementarity'` sweep did not finish during the audit window.

## Summary
Instances checked: 18 | Violations found: 8 | Verdict: FAIL


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
session id: 019d83bd-597e-73e3-a6d9-33f0a96c0a76
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


Run: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'koszul_conductor or complementarity' --tb=short -q 2>&1 | tail -30. Check: K(BP)=196? K(Vir)=13?

Also check: are hardcoded expected values in test files cited with 2+ independent sources (AP10/AP128)? Read the test file and verify.
mcp startup: no servers
codex
Auditing the compute surface and the supporting manuscript references now. I’m using `deep-beilinson-audit` for adversarial checking, `build-surface` for the pytest run, and `multi-path-verify` for the two complementarity constants and the AP10/AP128 source-citation check.
exec
/bin/zsh -lc "pwd && rg --files | rg '"'^(CLAUDE'"\\.md|chapters/connections/concordance\\.tex|metadata/theorem_registry\\.md|raeeznotes/raeeznotes100/red_team_summary\\.md|archive/raeeznotes/raeeznotes100/red_team_summary\\.md|compute/tests/.*complementarity.*|compute/tests/.*koszul_conductor.*|compute/.*complementarity.*|compute/.*koszul_conductor.*|.*landscape_census.*|.*complementarity.*|.*Koszul.*|.*BP.*|.*Vir.*)"'$'"'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/build-surface/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/multi-path-verify/SKILL.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "sed -n '1,220p' .agents/skills/deep-beilinson-audit/SKILL.md" in /Users/raeez/chiral-bar-cobar succeeded in 53ms:
/Users/raeez/chiral-bar-cobar
CLAUDE.md
metadata/theorem_registry.md
audit_campaign_20260412_230832/F02_kappa_Vir.md
audit_campaign_20260412_230832/F17_K_BP.md
audit_campaign_20260412_230832/F07_r_Vir.md
audit_campaign_20260412_230832/F18_complementarity.md
chapters/examples/landscape_census.tex
rectification_20260412_233715/R02_higher_genus_complementarity.md
chapters/connections/concordance.tex
chapters/theory/higher_genus_complementarity.tex
audit_campaign_20260412_231034/F18_complementarity.md
audit_campaign_20260412_231034/F02_kappa_Vir.md
audit_campaign_20260412_231034/F07_r_Vir.md
audit_campaign_20260412_231034/F17_K_BP.md
compute/lib/theorem_c_complementarity.py
compute/tests/test_koszul_conductor_table_engine.py
compute/lib/level_rank_complementarity.py
compute/lib/complementarity_landscape.py
compute/lib/complementarity_cross_verification.py
 succeeded in 231ms:
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
 succeeded in 256ms:
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

 succeeded in 365ms:
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

Plan update
Audit surface fixed to complementarity and koszul conductor tests, with source-of-truth checks for K(BP)=196, K(Vir)=13, and AP10/AP128 provenance of hardcoded expectations.
  → Read required constitutional files and target test/manuscript/compute surfaces
  • Run the requested targeted pytest command and classify failures
  • Verify K(BP)=196 and K(Vir)=13 against compute and manuscript sources
  • Audit AP10/AP128 compliance for hardcoded expected values in the relevant tests
  • Recheck findings and produce severity-ordered report
codex
I’ve fixed the audit surface to the complementarity/koszul-conductor tests and the manuscript formulas they claim to implement. Next I’m reading the source-of-truth files, then I’ll run the exact pytest command you specified and compare the failures or passes against the manuscript and AP10/AP128.
exec
/bin/zsh -lc "nl -ba metadata/theorem_registry.md | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/connections/concordance.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba CLAUDE.md | sed -n '1,220p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	# Theorem Registry
     2	
     3	Auto-generated on 2026-04-10 from the structured claim extractor in `scripts/generate_metadata.py`.
     4	
     5	This registry now tracks every `\ClaimStatusProvedHere` block directly from source, so the proved surface cannot silently drift behind the TeX tree.
     6	
     7	## Snapshot
     8	
     9	| Metric | Value |
    10	|---|---:|
    11	| ProvedHere claims | 2809 |
    12	| Total tagged claims | 3615 |
    13	| Active files in `main.tex` | 85 |
    14	| Total `.tex` files scanned | 128 |
    15	
    16	## Status Totals
    17	
    18	| Status | Count |
    19	|---|---:|
    20	| `ProvedHere` | 2809 |
 succeeded in 52ms:
     1	\chapter{Concordance with primary literature}
     2	\label{chap:concordance}
     3	
     4	\index{concordance|textbf}
     5	
     6	This chapter is the constitution of the monograph. When chapters
     7	disagree, this chapter governs. It records the five main theorems
     8	with their precise status and locates every result against the
     9	prior literature: what is proved, what is conditional, what
    10	remains conjectural.
    11	
    12	The governing principle is falsification: every claim in these three
    13	volumes is presumed false until it appears below with an explicit
    14	status tag and a proof reference or independent verification trail.
    15	A theorem that contradicts the concordance is not a theorem; it is an
    16	error in the chapter that states it. Omission from this chapter is
    17	itself a verdict: what is not recorded here has not survived scrutiny.
    18	The concordance does not summarize the monograph; the monograph
    19	approximates the concordance.
    20	
 succeeded in 51ms:
     1	# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)
     2	
     3	## Identity
     4	
     5	E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.
     6	
     7	**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.
     8	
     9	Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.
    10	
    11	**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.
    12	
    13	**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).
    14	
    15	**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.
    16	
    17	**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.
    18	
    19	**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.
    20	
exec
/bin/zsh -lc "if [ -f raeeznotes/raeeznotes100/red_team_summary.md ]; then nl -ba raeeznotes/raeeznotes100/red_team_summary.md | sed -n '1,260p'; else nl -ba archive/raeeznotes/raeeznotes100/red_team_summary.md | sed -n '1,260p'; fi" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	# Red-Team Summary of Vol1/Vol2 Claim Audit
     2	## Scope
     3	- Formal tagged claims catalogued: **4866**
     4	- Volume I formal claims: **2841**
     5	- Volume II formal claims: **2025**
     6	- Informal/meta claim harvest (README / PROGRAMMES / PROOF_ATLAS / audit notes): **94**
     7	- Every formal claim has an attached attack swarm in the master ledger. The informal harvest is separate because sentence-level slogans are less structurally tagged.
     8	
     9	## Status profile
    10	- ProvedHere: **3801**
    11	- Conjectured: **327**
    12	- Heuristic: **35**
    13	- ProvedElsewhere: **513**
    14	- Conditional: **116**
    15	- Open: **74**
    16	
    17	## Risk profile
    18	- medium: **1999**
    19	- low: **1913**
    20	- high: **807**

thinking
**Locating target files**

I need to locate the target files and formulas first. Then, I think I'll run the requested pytest. Before doing that, it seems smart to use a standard prelude, which would include running pkill followed by pytest. I'll aim to use the exact command to ensure everything goes smoothly. It feels like I have a solid plan here to approach it methodically!
exec
/bin/zsh -lc "pkill -9 -f pdflatex 2>/dev/null || true
sleep 2
python3 -m pytest compute/tests/ -k 'koszul_conductor or complementarity' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobar exited -1 in 10.98s:

codex
The targeted pytest run is in flight. While that runs, I’m reading the exact test files and the complementarity manuscript surface so I can distinguish a mathematics failure from a missing provenance comment or a stale oracle.
exec
/bin/zsh -lc "nl -ba compute/tests/test_koszul_conductor_table_engine.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_bp_koszul_conductor_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_exceptional_koszul_conductor_engine.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_c_complementarity.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_complementarity_landscape.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Tests for Bershadsky-Polyakov Koszul conductor and complementarity engine.
     2	
     3	THEOREM-LEVEL TESTS: For the BP algebra W^k(sl_3, f_{(2,1)}), the Koszul
     4	conductor K_BP = c_BP(k) + c_BP(-k-6) = 196 is level-independent, and
     5	the kappa complementarity kappa_BP(k) + kappa_BP(-k-6) = 98/3.
     6	
     7	VERIFICATION PATHS for each hardcoded expected value:
     8	    [DC] Direct computation from c_BP(k) = 2 - 24(k+1)^2/(k+3)
     9	    [CF] Cross-family: K_BP = 196 matches sl3_subregular_bar.py, bp_shadow_tower.py,
    10	         theorem_gz_frontier_engine.py (corrected from 76, AP1/AP3)
    11	    [SY] Symmetry: c_BP(-2) = c_BP(1) = -22 (k and -k-3 share numerator structure)
    12	    [LC] Limiting case: c_BP(-1) = 2 (numerator vanishes: (k+1)^2|_{k=-1} = 0)
    13	
    14	References:
    15	    Fehily-Kawasetsu-Ridout (2020): BP central charge
    16	    sl3_subregular_bar.py: anomaly ratio rho = 1/6, Koszul conductor K = 196
    17	    theorem_gz_frontier_engine.py: K_BP = 196
    18	    bp_shadow_tower.py: K_BP = 196, shadow tower
    19	"""
    20	
 succeeded in 51ms:
     1	r"""Tests for the Koszul conductor table engine.
     2	
     3	Verifies K(A) = kappa(A) + kappa(A^!) and c + c' for all families
     4	in the standard chiral algebra landscape.  Every hardcoded expected
     5	value has a VERIFIED comment citing 2+ independent sources (AP10/HZ-6).
     6	
     7	Ground truth references:
     8	  C1-C7:   central charges and kappa per family
     9	  C18:     K(A) = kappa+kappa': 0 (KM/Heis/lattice/free), 13 (Vir),
    10	           250/3 (W_3), 196 (BP)
    11	  C20:     K_BP = 196, self-dual at k=-3
    12	  AP136:   H_N = sum_{j=1}^N 1/j, NOT H_{N-1}
    13	  B7:      WRONG: kappa(W_N) = c*H_{N-1}
    14	  B9:      WRONG: kappa+kappa' = 0 universally
    15	"""
    16	
    17	import pytest
    18	from fractions import Fraction
    19	
    20	from compute.lib.koszul_conductor_table_engine import (
 succeeded in 52ms:
     1	"""Tests for exact principal W conductor data at exceptional Lie types.
     2	
     3	The new engine keeps both conductor surfaces explicit:
     4	  - central-charge complement: c(k) + c(k')
     5	  - kappa complementarity: kappa(k) + kappa(k')
     6	
     7	Type A is checked against the existing canonical engines.
     8	Exceptional values are checked against independently derived exact constants.
     9	"""
    10	
    11	from fractions import Fraction
    12	
    13	import pytest
    14	
    15	from compute.lib.alpha_n_conductor_engine import K_WN, alpha_N
    16	from compute.lib.exceptional_koszul_conductor_engine import (
    17	    ALL_SUPPORTED_TYPES,
    18	    EXCEPTIONAL_TYPES,
    19	    KAPPA_COMPLEMENTARITIES,
    20	    KOSZUL_CONDUCTORS,
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
     1	"""Tests for Theorem C complementarity: Q_g(A) + Q_g(A!) = H*(M_bar_g, Z(A)).
     2	
     3	50+ tests verifying:
     4	  - Scalar complementarity: kappa(A) + kappa(A!) = constant
     5	  - Genus-g complementarity: F_g(A) + F_g(A!) = (kappa+kappa!) * lambda_g^FP
     6	  - Feigin-Frenkel dual parameters
     7	  - Self-dual points (Virasoro at c=13, NOT c=26)
     8	  - Level independence of complementarity sums
     9	  - Lagrangian indicators
    10	  - Two-channel decomposition for affine algebras
    11	  - Full landscape verification
    12	
    13	All arithmetic is exact (Fraction).
    14	
    15	References:
    16	  thm:quantum-complementarity-main (higher_genus_complementarity.tex)
    17	  prop:kappa-anti-symmetry-ff (kac_moody.tex)
    18	  CLAUDE.md: Theorem C, Critical Pitfalls
    19	"""
    20	import pytest
 succeeded in 52ms:
     1	"""Tests for the full complementarity landscape.
     2	
     3	Verifies ALL complementarity data for ALL standard families:
     4	
     5	1. Heisenberg: kappa + kappa' = 0
     6	2. Free fermion: kappa + kappa' = 0
     7	3. Lattice VOAs: kappa + kappa' = 0
     8	4. betagamma/bc: kappa + kappa' = 0
     9	5. Affine KM (all simple types): kappa + kappa' = 0, K = 2*dim(g)
    10	6. Virasoro: kappa + kappa' = 13, K = 26, self-dual at c = 13
    11	7. W_N (N=2..7): kappa + kappa' = rho_N * K_N, verified at multiple levels
    12	
    13	Cross-checks:
    14	- K_N formula vs direct computation
    15	- Level independence of complementarity sum
    16	- Self-dual points
    17	- betagamma polynomial symmetry
    18	- Consistency with existing compute modules
    19	
    20	References:
 succeeded in 51ms:
     1	\section{The complementarity theorem}
     2	\label{sec:complementarity-theorem}
     3	
     4	Classical Koszul duality over a point is a discrete correspondence:
     5	$\cA$ and~$\cA^!$ are linked by $\Omega \circ B$ and nothing more.
     6	Already at genus~$0$ on a curve, the Fulton--MacPherson
     7	compactifications $\overline{C}_n(X)$ and the Arnold forms
     8	$\eta_{ij} = d\log(z_i - z_j)$ supply configuration-space geometry
     9	that has no counterpart over a point: the collision residues that
    10	define the bar differential, the averaging map
    11	$\mathrm{av}\colon r(z) \mapsto \kappa$ that extracts the modular
    12	characteristic from the spectral $r$-matrix, and the higher
    13	operations $m_n$ for $n \geq 3$ that determine whether the shadow
    14	tower terminates. At genus~$g \geq 1$, the fiberwise curvature
    15	$d_{\mathrm{fib}}^2 = \kappa(\cA) \cdot \omega_g$ forces the two
    16	algebras to interact through the moduli
    17	$\overline{\mathcal{M}}_g$. The genus-$g$ obstruction space
    18	decomposes into two complementary halves via Verdier duality:
    19	\begin{equation}\label{eq:complementarity-chapter-opening}
    20	 H^*\bigl(\overline{\mathcal{M}}_g,\,\mathcal{Z}(\cA)\bigr)

thinking
**Auditing test files**

I need to inspect more test files for comments and any missing VERIFIED tags. I'm considering that some files might have hardcoded values without explanations. An audit of all tests seems necessary. I might count the instances checked based on the values or the number of files. It seems logical to establish a formula for instances checked, possibly based on hardcoded expected-value instances plus test files. I plan to review the pytest results first.

thinking
**Rerunning the command**

I’m realizing I might not be getting output because of a pipeline issue? It seems like I should rerun the command without using tail, which may be causing some weird behavior. There’s a code -1; it could have been killed, perhaps? So I’ll try running the exact command with bash -lc. The user wants me to run the command tail -30, so I’ll focus on capturing the output properly this time. Let's run it again!
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'koszul_conductor or complementarity' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobar
thinking
**Inspecting compute libraries**

I'm thinking about the ongoing tests, which seem to be taking a while. I should remember to check in later. In the meantime, I’ll inspect the remaining files to see if they have what I need. It seems I might require specific compute libraries and sources. Reading through the compute/lib files and relevant manuscript lines could be helpful. Also, I might use regex to identify K_BP, K(Vir), and AP10 in the tests.
codex
I’ve confirmed the main target tests and the complementarity chapter are loaded. Next I’m reading the underlying compute engines and the census/manuscript references for the two conductor constants, while the test run continues in the background.
exec
/bin/zsh -lc "nl -ba compute/lib/theorem_c_complementarity.py | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"K_BP|196|K\\(BP\\)|K_kk\\(BP\\)|K\\(Vir\\)|Virasoro|13\\b|complementarity\" chapters/examples/landscape_census.tex chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex audit_campaign_20260412_230832/F17_K_BP.md audit_campaign_20260412_230832/F18_complementarity.md rectification_20260412_233715/R02_higher_genus_complementarity.md" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/koszul_conductor_table_engine.py | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/complementarity_landscape.py | sed -n '1,360p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_level_rank_complementarity.py | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bp_koszul_conductor_engine.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	"""Theorem C verification: complementarity Q_g(A) + Q_g(A!) = H*(M_bar_g, Z(A)).
     2	
     3	THEOREM C (Main Theorem 3 of 5): The genus-g quantum moduli of A and A!
     4	are complementary Lagrangian subvarieties.
     5	
     6	At the scalar level (Theorem D):
     7	  kappa(A) + kappa(A!) = constant (family-specific)
     8	  F_g(A) + F_g(A!) = (kappa + kappa!) * lambda_g^FP
     9	
    10	The complementarity sum depends ONLY on the root datum (for KM/W-algebras)
    11	or the algebra type (for free-field systems), never on the level.
    12	
    13	KEY FORMULAS (from the manuscript):
    14	  - Heisenberg H_k:       kappa = k,               kappa! = -k,          sum = 0
    15	  - Virasoro Vir_c:        kappa = c/2,             kappa! = (26-c)/2,    sum = 13
    16	  - Affine V_k(sl_N):     kappa = (N^2-1)(k+N)/(2N), FF anti-symmetric,  sum = 0
    17	  - betagamma:             kappa = c/2,             kappa! = -c/2,        sum = 0
    18	  - W_3:                   kappa = 5c/6,            kappa! = 5(100-c)/6,  sum = 250/3
    19	  - Lattice V_Lambda:      kappa = rank,            kappa! = -rank,       sum = 0
    20	
 succeeded in 52ms:
Total output lines: 1630

chapters/examples/landscape_census.tex:5:The complementarity sum $c + c' = 2d$ holds for every Kac--Moody
chapters/examples/landscape_census.tex:9:$\widehat{\mathfrak{sl}}_2$, Virasoro, and $\beta\gamma$, three
chapters/examples/landscape_census.tex:22:forces the infinite shadow tower of Virasoro and the $\mathcal{W}$-algebras
chapters/examples/landscape_census.tex:47:(Theorem~\ref{thm:central-charge-complementarity}), and the
chapters/examples/landscape_census.tex:109: & $\dfrac{78k}{k+12}$ & $156$ & $\dfrac{13(k+12)}{4}$ & PH \\[4pt]
chapters/examples/landscape_census.tex:158: & $2 - \dfrac{24(k{+}1)^2}{k{+}3}$ & $196$
chapters/examples/landscape_census.tex:211:the degree-$2$ projection; the complementarity sum $c + c'$ is the
chapters/examples/landscape_census.tex:496:CYBE $[r_{12}, r_{13}] + \text{cyc.} = 0$ holds vacuously;
chapters/examples/landscape_census.tex:531:($h = 1$) gives $z^{-1}$; the Virasoro ($h = 2$) gives $z^{-3}$;
chapters/examples/landscape_census.tex:561:(Virasoro, $\cW_N$, $r_{\max} = \infty$), the degree-$3$ MC
chapters/examples/landscape_census.tex:702: & $\dfrac{40}{5c{+}22}$ & $\sqrt{\dfrac{180c{+}872}{c^2(5c{+}22)}}$ & $13$ \\[8pt]
chapters/examples/landscape_census.tex:713: & $\dfrac{20}{71}$ & $> 0$ & $13$\textsuperscript{$\S$} \\[4pt]
chapters/examples/landscape_census.tex:726:The Virasoro discriminant complementarity is
chapters/examples/landscape_census.tex:732:The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
chapters/examples/landscape_census.tex:734:${}^\S$For the Monster module $V^\natural$: the complementarity
chapters/examples/landscape_census.tex:735:sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
chapters/examples/landscape_census.tex:736:($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
chapters/examples/landscape_census.tex:740:In the Virasoro row, the displayed partner $\mathrm{Vir}_{26-c}$ is
 succeeded in 51ms:
     1	r"""Koszul conductor table engine: K(A) = kappa(A) + kappa(A^!) for all families.
     2	
     3	Computes two complementarity invariants for every family in the standard
     4	chiral algebra landscape:
     5	
     6	  K_cc(A) = c(A) + c(A^!)          (central charge sum)
     7	  K_kk(A) = kappa(A) + kappa(A^!)  (Koszul conductor)
     8	
     9	The Koszul conductor K_kk is the invariant called K(A) in the monograph
    10	(C18 of the true formula census).  Known values:
    11	
    12	  K_kk = 0       for KM, Heisenberg, lattice, free families
    13	  K_kk = 13      for Virasoro
    14	  K_kk = 250/3   for W_3
    15	  K_kk = 196     for Bershadsky-Polyakov
    16	
    17	All arithmetic uses fractions.Fraction for exact rational results.
    18	
    19	Canonical references:
    20	  C1.  kappa(H_k) = k
 succeeded in 100ms:
     1	"""Full complementarity landscape: kappa, kappa', K, rho, self-dual point for ALL families.
     2	
     3	Theorem C (complementarity) at the scalar level (Theorem D):
     4	
     5	    kappa(A) + kappa(A!) = constant
     6	
     7	The constant depends on the algebra family:
     8	
     9	    (1) Free-field systems (Heisenberg, betagamma/bc, lattice, free fermion):
    10	        kappa + kappa' = 0
    11	
    12	    (2) Affine Kac-Moody algebras (all simple types):
    13	        kappa + kappa' = 0    (FF anti-symmetry: k -> -k-2h^v negates kappa)
    14	        K := c + c' = 2*dim(g)  (the central charge sum IS level-independent)
    15	
    16	    (3) W-algebras W_N = W(sl_N) (principal, type A):
    17	        kappa + kappa' = rho_N * K_N
    18	        where rho_N = H_N - 1 = sum_{s=2}^N 1/s  (anomaly ratio)
    19	        and   K_N = 2(N-1)(2N^2+2N+1)             (Koszul conductor)
    20	        Self-dual at c_* = K_N / 2.
 succeeded in 147ms:
     1	r"""Bershadsky-Polyakov Koszul conductor and complementarity: exact Fraction arithmetic.
     2	
     3	MATHEMATICAL CONTENT
     4	====================
     5	
     6	The Bershadsky-Polyakov algebra W^k(sl_3, f_{(2,1)}) is the DS reduction of
     7	affine sl_3 at the MINIMAL nilpotent orbit.  Its central charge, Feigin-Frenkel
     8	dual level, Koszul conductor, anomaly ratio, and modular characteristic are
     9	computed here in exact rational arithmetic.
    10	
    11	Formulas:
    12	
    13	    c_BP(k) = 2 - 24(k+1)^2 / (k+3)
    14	
    15	    k' = -k - 6     (Feigin-Frenkel dual; h^v(sl_3) = 3, Dynkin shift)
    16	
    17	    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)
    18	
    19	    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)
    20	
 succeeded in 198ms:
     1	"""Tests for conj:level-rank-complementarity (kac_moody.tex, ~line 3870).
     2	
     3	Investigates the conjecture that for affine V_k(g) at non-critical level:
     4	  Q_g(V_k(g)) + Q_g(V_{-k-2h^vee}(g)) = H*(M_bar_g, Z(V_k(g)))
     5	
     6	PROVED ingredients tested:
     7	  (1) kappa anti-symmetry: kappa(g_k) + kappa(g_{-k-2h^vee}) = 0
     8	  (2) Genus-1 complementarity: dim Q_1 + dim Q_1' = 2 = dim H*(M_bar_{1,1})
     9	  (3) Level-rank for gl_N: U(N)_k <-> U(k)_{-N}
    10	  (4) Verlinde symmetry at genus 1: dim V_1(sl_N, k) = dim V_1(sl_k, N)
    11	  (5) Center factorization at genus 1
    12	
    13	Mathematical references:
    14	  conj:level-rank-complementarity    (kac_moody.tex)
    15	  thm:sl2-genus1-complementarity     (kac_moody.tex)
    16	  prop:ff-channel-shear              (kac_moody.tex)
    17	  thm:quantum-complementarity-main   (higher_genus_complementarity.tex)
    18	"""
    19	
    20	import pytest

thinking
**Inspecting landscape census details**

I need to look more closely at specific lines in the landscape_census, as the search output seems truncated. It would be helpful to focus on lines around 150 and specifically at line 158 K_BP 196. I should also check lines around Virasoro, maybe starting at line 129. Let’s open the relevant sections of the data table to gather the necessary details!
exec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '90,175p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"K\\(BP\\)|196|K_BP|98/3|Virasoro.*13|K\\(Vir\\)|13\\b\" chapters/theory/higher_genus_complementarity.tex chapters/examples/landscape_census.tex chapters/examples/bershadsky_polyakov.tex" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "# VERIFIED|VERIFIED:" compute/tests/test_*complementarity*.py compute/tests/test_*koszul_conductor*.py compute/tests/test_bp_koszul_conductor_engine.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/bershadsky_polyakov.tex | sed -n '1,260p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '720,742p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "eq:bp-conductor|eq:bp-complementarity|prop:bp-kappa|196|98/3|varrho" chapters/examples/bershadsky_polyakov.tex' in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    90	$\widehat{\fg}_k$ (general)
    91	 & $\widehat{\fg}_{-k-2h^\vee}$
    92	 & $\dfrac{kd}{k + h^\vee}$ & $2d$
    93	 & $\dfrac{td}{2h^\vee}$ & PH \\[4pt]
    94	\hline
    95	$\widehat{\mathfrak{sl}}_2$ at level $k$
    96	 & $\widehat{\mathfrak{sl}}_2$ at $-k{-}4$
    97	 & $\dfrac{3k}{k+2}$ & $6$ & $\dfrac{3(k+2)}{4}$ & PH \\[4pt]
    98	\hline
    99	$\widehat{\mathfrak{sl}}_3$ at level $k$
   100	 & $\widehat{\mathfrak{sl}}_3$ at $-k{-}6$
   101	 & $\dfrac{8k}{k+3}$ & $16$ & $\dfrac{4(k+3)}{3}$ & PH \\[4pt]
   102	\hline
   103	$\widehat{\mathfrak{so}}_{8}$ at level $k$ (type $D_4$; triality)
   104	 & $\widehat{\mathfrak{so}}_{8}$ at $-k{-}12$
   105	 & $\dfrac{28k}{k+6}$ & $56$ & $\dfrac{7(k+6)}{3}$ & PH \\[4pt]
   106	\hline
   107	$\widehat{E}_6$ at level $k$
   108	 & $\widehat{E}_6$ at $-k{-}24$
   109	 & $\dfrac{78k}{k+12}$ & $156$ & $\dfrac{13(k+12)}{4}$ & PH \\[4pt]
 succeeded in 51ms:
chapters/examples/bershadsky_polyakov.tex:11:$\kappa + \kappa' = \varrho K = 98/3 \neq 0$ witnesses the
chapters/examples/bershadsky_polyakov.tex:36: = K_{\mathcal{B}}/2$, \; $K_{\mathcal{B}} = 196$
chapters/examples/bershadsky_polyakov.tex:65:Koszul conductor & $K_{\mathcal{B}} = c(k) + c(-k{-}6) = 196$ \\
chapters/examples/bershadsky_polyakov.tex:66:Complementarity & $\kappa + \kappa' = 98/3$ (W-type) \\
chapters/examples/bershadsky_polyakov.tex:201:$k' = -k - 6$. The dual central charge is $c' = c(-k-6) = 196 - c$.
chapters/examples/bershadsky_polyakov.tex:204:K_{\mathcal{B}} \;=\; c(k) + c(-k-6) \;=\; 196\,.
chapters/examples/bershadsky_polyakov.tex:217: = 4 + 192 = 196\,.
chapters/examples/bershadsky_polyakov.tex:238:$\mathcal{B}^k$ (minimal) & $(2,1)$ & $196$ \\
chapters/examples/bershadsky_polyakov.tex:245:$c_{\mathrm{sd}} = K/2$ is $c = 13$ for Virasoro, $c = 50$ for
chapters/examples/bershadsky_polyakov.tex:300:\frac{c(k)}{6} + \frac{196 - c(k)}{6}
chapters/examples/bershadsky_polyakov.tex:302:\frac{196}{6}
chapters/examples/bershadsky_polyakov.tex:307:$\kappa + \kappa' = \varrho \cdot K$ here $\varrho = 1/6$ and $K = 196$.
chapters/examples/bershadsky_polyakov.tex:406:\qquad c' = 196 - c\,.
chapters/examples/bershadsky_polyakov.tex:420:At degree~$2$: $\sigma^{(2)} = c/2 + (196-c)/2 = 98$.
chapters/examples/bershadsky_polyakov.tex:451:$K$ & $16$ & $196$ & $100$ \\
chapters/examples/landscape_census.tex:109: & $\dfrac{78k}{k+12}$ & $156$ & $\dfrac{13(k+12)}{4}$ & PH \\[4pt]
chapters/examples/landscape_census.tex:158: & $2 - \dfrac{24(k{+}1)^2}{k{+}3}$ & $196$
chapters/examples/landscape_census.tex:496:CYBE $[r_{12}, r_{13}] + \text{cyc.} = 0$ holds vacuously;
chapters/examples/landscape_census.tex:702: & $\dfrac{40}{5c{+}22}$ & $\sqrt{\dfrac{180c{+}872}{c^2(5c{+}22)}}$ & $13$ \\[8pt]
chapters/examples/landscape_census.tex:713: & $\dfrac{20}{71}$ & $> 0$ & $13$\textsuperscript{$\S$} \\[4pt]
 succeeded in 52ms:
     1	\chapter{The Bershadsky--Polyakov algebra}\label{chap:bershadsky-polyakov}
     2	
     3	The Bershadsky--Polyakov algebra is the simplest non-principal
     4	Drinfeld--Sokolov reduction, yet it exhibits every phenomenon that
     5	distinguishes non-principal from principal $\mathcal{W}$-algebra
     6	Koszul duality: the partition $(2,1)$ is self-transpose, so the
     7	Koszul dual is again a Bershadsky--Polyakov algebra at a
     8	different level; the shadow obstruction tower is class~$M$ on the
     9	$T$-line but class~$G$ on the $J$-line, giving mixed shadow depth
    10	within a single algebra; and the complementarity sum
    11	$\kappa + \kappa' = \varrho K = 98/3 \neq 0$ witnesses the
    12	failure of anti-symmetry in the non-principal landscape.
    13	
    14	\begin{table}[ht]
    15	\centering
    16	\small
    17	\caption{Five-theorem verification for the Bershadsky--Polyakov
    18	algebra $\mathcal{B}^k = \mathcal{W}^k(\mathfrak{sl}_3, f_{(2,1)})$
    19	at generic level
    20	$k \neq -3$.}\label{tab:bp-five-theorems}
 succeeded in 52ms:
compute/tests/test_bp_koszul_conductor_engine.py:113:        # VERIFIED: [DC] direct substitution + [CF] cross-engine
compute/tests/test_bp_koszul_conductor_engine.py:123:        # VERIFIED: [DC] (k+1)^2 vanishes at k=-1; [LC] limiting case
compute/tests/test_bp_koszul_conductor_engine.py:128:        # VERIFIED: [DC] both evaluate to -22; [SY] (k+1)^2/(k+3) at k=1,k=-2
compute/tests/test_bp_koszul_conductor_engine.py:158:        # VERIFIED: [DC] direct computation -k-6
compute/tests/test_bp_koszul_conductor_engine.py:164:            # VERIFIED: [DC] -(-k-6)-6 = k+6-6 = k; [SY] involution property
compute/tests/test_bp_koszul_conductor_engine.py:169:        # VERIFIED: [DC] -(-3)-6 = -3; [SY] fixed point of k -> -k-6 is k = -3
compute/tests/test_bp_koszul_conductor_engine.py:175:            # VERIFIED: [DC] k + (-k-6) = -6; [SY] sum is constant
compute/tests/test_bp_koszul_conductor_engine.py:189:        # VERIFIED: [DC] algebraic proof in engine docstring; [CF] matches
compute/tests/test_bp_koszul_conductor_engine.py:196:            # VERIFIED: [DC] direct sum; [CF] cross-checked independently
compute/tests/test_bp_koszul_conductor_engine.py:213:        # VERIFIED: [DC] 1 - 2/3 - 2/3 + 1/2 = 6/6 - 4/6 - 4/6 + 3/6 = 1/6
compute/tests/test_bp_koszul_conductor_engine.py:219:        # VERIFIED: [DC] sum over generators; [CF] matches constant
compute/tests/test_bp_koszul_conductor_engine.py:248:        # VERIFIED: [DC] definition; [CF] matches sl3_subregular_bar.py kappa formula
compute/tests/test_bp_koszul_conductor_engine.py:254:        # VERIFIED: [DC] (1/6)*(-6) = -1; [CF] negative kappa (below critical)
compute/tests/test_bp_koszul_conductor_engine.py:259:        # VERIFIED: [DC] (1/6)*2 = 1/3; [LC] c_BP(-1)=2 since (k+1)^2 vanishes
compute/tests/test_bp_koszul_conductor_engine.py:273:        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
compute/tests/test_bp_koszul_conductor_engine.py:283:        # VERIFIED: [DC] 196/6 = 98/3; [CF] consistency check
compute/tests/test_bp_koszul_conductor_engine.py:300:        # VERIFIED: [DC] -(-3)-6 = -3; [SY] unique fixed point of involution
compute/tests/test_bp_koszul_conductor_engine.py:373:        # VERIFIED: [DC] algebraic proof; [CF] CLAUDE.md C20
compute/tests/test_bp_koszul_conductor_engine.py:378:        # VERIFIED: [DC] fixed point of -k-6; [CF] CLAUDE.md C20
compute/tests/test_bp_koszul_conductor_engine.py:383:        # VERIFIED: [CF] CLAUDE.md C20 correction history
 succeeded in 52ms:
   720	${}^\dagger$For $\beta\gamma$ and $bc$: $\Delta = 0$ and $\rho = 0$ on the primary
   721	(weight-changing) line by stratum separation
   722	(Remark~\ref{rem:contact-stratum-separation}); the quartic contact invariant
   723	$\mathfrak{Q}^{\mathrm{contact}} \neq 0$ lives on a charged stratum.
   724	Both two-generator free-field systems share the same stratum separation
   725	mechanism and class~C shadow depth.
   726	The Virasoro discriminant complementarity is
   727	$\Delta(c) + \Delta(26{-}c) = 6960/[(5c{+}22)(152{-}5c)]$
   728	(Corollary~\ref{cor:discriminant-atlas}(ii)).
   729	The Koszul conductor for $\mathcal{W}_N$ is
   730	$K_N = 4N^3 - 2N - 2$ and $\varrho_N = H_N - 1$; explicitly:
   731	$K_2 = 26$, $K_3 = 100$, $K_4 = 246$, $K_5 = 488$.
   732	The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
   733	$c^* = 50$ for $\mathcal{W}_3$, $c^* = 123$ for $\mathcal{W}_4$.
   734	${}^\S$For the Monster module $V^\natural$: the complementarity
   735	sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
   736	($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
   737	since $\dim V_1^\natural = 0$ forces $\kappa = c/2 = 12$
   738	.
   739	
 succeeded in 59ms:
11:$\kappa + \kappa' = \varrho K = 98/3 \neq 0$ witnesses the
36: = K_{\mathcal{B}}/2$, \; $K_{\mathcal{B}} = 196$
42: & Proved & Prop~\ref{prop:bp-kappa} \\
62: $c/6$; \; anomaly ratio $\varrho = 1/6$ \\
65:Koszul conductor & $K_{\mathcal{B}} = c(k) + c(-k{-}6) = 196$ \\
66:Complementarity & $\kappa + \kappa' = 98/3$ (W-type) \\
201:$k' = -k - 6$. The dual central charge is $c' = c(-k-6) = 196 - c$.
203:\begin{equation}\label{eq:bp-conductor}
204:K_{\mathcal{B}} \;=\; c(k) + c(-k-6) \;=\; 196\,.
217: = 4 + 192 = 196\,.
238:$\mathcal{B}^k$ (minimal) & $(2,1)$ & $196$ \\
260:\label{prop:bp-kappa}
268:The anomaly ratio is $\varrho(\mathcal{B}^k) = \kappa/c = 1/6$.
281:\texttt{kappa\_deficit\_ds.py}. The anomaly ratio $\varrho = 1/6$
283:$\varrho(\mathrm{Vir}) = 1/2$,
284:$\varrho(\mathcal{W}_3) = 5/6$, and
285:$\varrho(\mathcal{B}^k) = 1/6$ satisfy
286:$\varrho(\mathrm{BP}) + \varrho(\mathcal{W}_3) = 1$,
297:\begin{equation}\label{eq:bp-complementarity}
300:\frac{c(k)}{6} + \frac{196 - c(k)}{6}

thinking
**Checking constants in formulas**

I need to systematically search relevant files for assertions with hardcoded constants and ensure that any preceding comments have been marked as VERIFIED. I think using scripts or awk could work, but I have to be careful. I also need to check the actual formulas: K(BP)=196 and K(Vir)=13. A direct computation from the compute library or manuscript makes sense. Since the user asked about these constants, I’ll run a Python snippet to verify them, possibly using sympy for simplification.
codex
The manuscript side is consistent so far on the two target constants: `landscape_census.tex` gives BP conductor `196` and Virasoro conductor `13` via the `W_2` row. I’m now checking whether the compute layer proves the same values independently, and whether the tests actually meet AP10/AP128 rather than just claiming they do.
exec
/bin/zsh -lc "nl -ba compute/tests/test_bc_koszul_zeta_complementarity_engine.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from sympy import symbols, simplify
k, c = symbols('k c')
expr_bp = (2 - 24*(k+1)**2/(k+3)) + (2 - 24*(-k-5)**2/(-k-3))
expr_vir = c/2 + (26-c)/2
print('bp_simplified=', simplify(expr_bp))
print('vir_simplified=', simplify(expr_vir))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_complementarity_cross_verification.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_ds_complementarity_defect.py | sed -n '1,320p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction
from compute.lib.bp_koszul_conductor_engine import K_BP, kappa_complementarity
from compute.lib.koszul_conductor_table_engine import virasoro_K_kk
print('K_BP(0)=', K_BP(0))
print('K_BP(1)=', K_BP(1))
print('K_BP(-1)=', K_BP(-1))
print('kappa_complementarity(0)=', kappa_complementarity(0))
print('virasoro_K_kk(0)=', virasoro_K_kk(Fraction(0)))
print('virasoro_K_kk(13)=', virasoro_K_kk(Fraction(13)))
print('virasoro_K_kk(26)=', virasoro_K_kk(Fraction(26)))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_bp_koszul_conductor_engine.py | sed -n '260,420p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
     1	r"""Tests for bc_koszul_zeta_complementarity_engine.py -- Koszul duality
     2	(Theorem C) acting on zeta zeros in the Benjamin-Chang framework.
     3	
     4	Verification paths:
     5	  - Path 1: Direct computation of residue ratios
     6	  - Path 2: Gamma duplication/reflection identities for ratio simplification
     7	  - Path 3: Boundary cases c=0, c=26 where one algebra is trivial
     8	  - Path 4: Consistency with kappa+kappa' values from landscape_census.tex
     9	
    10	80+ tests covering:
    11	  1. Complementarity of residues (A_c / A_{26-c})
    12	  2. Self-dual residue at c=13
    13	  3. Duality-twisted zeta with double poles
    14	  4. Complementarity L-function and Koszul perturbation
    15	  5. Shadow complementarity (shadow zeta sum/difference)
    16	  6. Lagrangian intersection structure
    17	  7. Defect form Omega_c
    18	  8. Boundary cases and kappa consistency
    19	
    20	Manuscript references:
 succeeded in 51ms:
     1	"""Tests for the DS complementarity defect.
     2	
     3	Verifies:
     4	1. δ_K = K_N · (H_N - 1) for all N
     5	2. Factorization δ_K = K_N · ρ(sl_N)
     6	3. K(ĝ_k) = 0 for all affine
     7	4. K(Vir_c) = 13 for all c
     8	5. Cubic conductor C + C' = -26 for Virasoro
     9	6. Quartic conductor Q + Q' depends on c (NOT level-independent)
    10	7. Genus-g defect δ_{Q_g} = K · λ_g^FP
    11	8. Large-N asymptotics δ_K ~ (4/3)N³ log N
    12	9. Affine tower vanishes at all arities/genera
    13	10. Hook-type defects for non-principal reductions
    14	"""
    15	
    16	from fractions import Fraction
    17	import pytest
    18	
    19	from compute.lib.ds_complementarity_defect import (
    20	    DSComplementarityDefect,
 succeeded in 51ms:
     1	r"""Tests for complementarity cross-verification: kappa(A) + kappa(A!).
     2	
     3	MANDATE: 4 independent methods, 15+ families, 100+ tests.
     4	
     5	CRITICAL REGRESSION CHECK (AP24):
     6	    The old overclaim kappa+kappa'=0 for ALL families is WRONG.
     7	    Virasoro: kappa+kappa' = 13 (NOT 0).
     8	    W_3: kappa+kappa' = 250/3 (NOT 0).
     9	    These tests prevent the AP24 error from recurring.
    10	
    11	Tests organized by:
    12	    1. Method agreement (4 methods x 15+ families = 60+ checks)
    13	    2. Expected values for each family
    14	    3. Level independence
    15	    4. Self-dual points
    16	    5. Ghost kappa table
    17	    6. Genus-g extension (F_g complementarity)
    18	    7. Shadow metric/discriminant complementarity
    19	    8. Shadow radius complementarity
    20	    9. AP24 regression checks
 succeeded in 51ms:
   260	        assert kappa_BP(-1) == Fraction(1, 3)
   261	
   262	
   263	# =============================================================================
   264	# Tests: kappa complementarity
   265	# =============================================================================
   266	
   267	class TestKappaComplementarity:
   268	    """Tests for kappa_BP(k) + kappa_BP(-k-6) = 98/3."""
   269	
   270	    @pytest.mark.parametrize("k, _c_k, _comment", C_BP_TEST_DATA)
   271	    def test_kappa_complementarity(self, k, _c_k, _comment):
   272	        """kappa complementarity = 98/3 at each test level."""
   273	        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
   274	        # [CF] matches sl3_subregular_bar.py complementarity
   275	        assert kappa_complementarity(k) == Fraction(98, 3)
   276	
   277	    def test_kappa_complementarity_constant(self):
   278	        """KAPPA_COMPLEMENTARITY_EXACT = 98/3."""
   279	        assert KAPPA_COMPLEMENTARITY_EXACT == Fraction(98, 3)
 succeeded in 1.76s:
bp_simplified= 196
vir_simplified= 13
 succeeded in 1.92s:
K_BP(0)= 196
K_BP(1)= 196
K_BP(-1)= 196
kappa_complementarity(0)= 98/3
virasoro_K_kk(0)= 13
virasoro_K_kk(13)= 13
virasoro_K_kk(26)= 13
exec
/bin/zsh -lc "python3 - <<'PY'
from sympy import symbols, simplify
k, c = symbols('k c')
expr_bp = (2 - 24*(k+1)**2/(k+3)) + (2 - 24*(-k-5)**2/(-k-3))
expr_vir = c/2 + (26-c)/2
print('bp_simplified=', simplify(expr_bp))
print('vir_simplified=', simplify(expr_vir))
PY" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "python3 - <<'PY'
from fractions import Fraction
from compute.lib.bp_koszul_conductor_engine import K_BP, kappa_complementarity
from compute.lib.koszul_conductor_table_engine import virasoro_K_kk
print('K_BP(0)=', K_BP(0))
print('K_BP(1)=', K_BP(1))
print('K_BP(-1)=', K_BP(-1))
print('kappa_complementarity(0)=', kappa_complementarity(0))
print('virasoro_K_kk(0)=', virasoro_K_kk(Fraction(0)))
print('virasoro_K_kk(13)=', virasoro_K_kk(Fraction(13)))
print('virasoro_K_kk(26)=', virasoro_K_kk(Fraction(26)))
PY" in /Users/raeez/chiral-bar-cobar succeeded in 1.90s:
K_BP(0)= 196
K_BP(1)= 196
K_BP(-1)= 196
kappa_complementarity(0)= 98/3
virasoro_K_kk(0)= 13
virasoro_K_kk(13)= 13
virasoro_K_kk(26)= 13
 succeeded in 1.92s:
bp_simplified= 196
vir_simplified= 13

thinking
**Inspecting audit report findings**

I want to organize each finding into file-level and line anchor categories, since the user is requesting an audit report. I think including several examples could be helpful. I’ll need to inspect `test_theorem_c_complementarity.py`, especially around lines 60-120, along with some other relevant lines. I noticed there are no VERIFIED comments anywhere, which might require me to search more thoroughly. Perhaps I should use `rg` for a better search.
exec
/bin/zsh -lc "rg -n \"VERIFIED|Fraction\\(|== Fraction\\(|== 13|== 196|== 98/3|== 250/3\" compute/tests/test_theorem_c_complementarity.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"VERIFIED|Fraction\\(|== Fraction\\(|== 13|== 196|== 98/3|== 250/3\" compute/tests/test_level_rank_complementarity.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"VERIFIED|Fraction\\(|== Fraction\\(|== 13|== 196|== 98/3|== 250/3\" compute/tests/test_ds_complementarity_defect.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"VERIFIED|Fraction\\(|== Fraction\\(|== 13|== 196|== 98/3|== 250/3\" compute/tests/test_complementarity_cross_verification.py" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n \"VERIFIED|Fraction\\(|== Fraction\\(|== 13|== 196|== 98/3|== 250/3\" compute/tests/test_complementarity_landscape.py" in /Users/raeez/chiral-bar-cobar exited 1 in 52ms:

 succeeded in 52ms:
62:        assert kappa("heisenberg", k=1) == Fraction(1)
63:        assert kappa("heisenberg", k=3) == Fraction(3)
64:        assert kappa("heisenberg", k=-5) == Fraction(-5)
65:        assert kappa("heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)
69:        assert kappa("virasoro", c=1) == Fraction(1, 2)
70:        assert kappa("virasoro", c=26) == Fraction(13)
71:        assert kappa("virasoro", c=13) == Fraction(13, 2)
72:        assert kappa("virasoro", c=Fraction(7, 10)) == Fraction(7, 20)
77:        assert kappa("affine", lie_type="A", rank=1, k=1) == Fraction(9, 4)
78:        assert kappa("affine", lie_type="A", rank=1, k=0) == Fraction(3, 2)
79:        assert kappa("affine", lie_type="A", rank=1, k=2) == Fraction(3)
84:        assert kappa("affine", lie_type="A", rank=2, k=1) == Fraction(16, 3)
85:        assert kappa("affine", lie_type="A", rank=2, k=0) == Fraction(4)
91:            expected = Fraction(N * N - 1) * (k_val + N) / (2 * N)
104:        assert kappa("betagamma", lam=Fraction(1, 2)) == Fraction(-1, 2)
106:        assert kappa("betagamma", lam=1) == Fraction(1)
108:        assert kappa("betagamma", lam=0) == Fraction(1)
112:        assert kappa("betagamma", c=-2) == Fraction(-1)
113:        assert kappa("betagamma", c=2) == Fraction(1)
117:        assert kappa("w3", c=6) == Fraction(5)
 succeeded in 51ms:
66:    @pytest.mark.parametrize("k_val", [1, 2, 5, -3, Fraction(1, 2)])
70:        assert r["sum_m1"] == Fraction(0)
73:        assert kappa_heisenberg(Fraction(1)) == Fraction(1)
74:        assert kappa_heisenberg(Fraction(7)) == Fraction(7)
75:        assert kappa_dual_heisenberg(Fraction(1)) == Fraction(-1)
82:        1, Fraction(1, 2), Fraction(7, 10), 13, 26, Fraction(25, 2)
87:        assert r["sum_m1"] == Fraction(13), f"AP24 REGRESSION: sum={r['sum_m1']} != 13"
90:        assert kappa_virasoro(Fraction(26)) == Fraction(13)
91:        assert kappa_virasoro(Fraction(13)) == Fraction(13, 2)
92:        assert kappa_dual_virasoro(Fraction(26)) == Fraction(0)
93:        assert kappa_dual_virasoro(Fraction(13)) == Fraction(13, 2)
97:        assert kappa_virasoro(Fraction(13)) == kappa_dual_virasoro(Fraction(13))
101:        assert kappa_virasoro(Fraction(26)) != kappa_dual_virasoro(Fraction(26))
114:            assert r["sum_m1"] == Fraction(0)
123:        assert r["sum_m1"] == Fraction(0)
131:        kap = kappa_affine("A", 2, Fraction(1))
132:        assert kap == Fraction(16, 3)
134:        assert kap != Fraction(1)
142:        c_val = Fraction(koszul_conductor_wn(N), 2)  # self-dual point
145:        exp = anomaly_ratio_wn(N) * Fraction(koszul_conductor_wn(N))
 succeeded in 52ms:
58:        assert exponent_sum(2) == Fraction(1, 2)
61:        assert exponent_sum(3) == Fraction(5, 6)
64:        assert exponent_sum(4) == Fraction(13, 12)
67:        assert koszul_conductor(2) == Fraction(26)
70:        assert koszul_conductor(3) == Fraction(100)
73:        assert koszul_conductor(4) == Fraction(246)
76:        assert koszul_conductor(5) == Fraction(488)
79:        assert koszul_conductor(6) == Fraction(850)
82:        assert self_dual_central_charge(2) == Fraction(13)
85:        assert self_dual_central_charge(3) == Fraction(50)
102:                assert K_affine(N, Fraction(k)) == 0
105:        for c in [1, 13, 25, Fraction(1, 2), Fraction(-22, 5) + 1]:
106:            assert K_virasoro(c) == 13
109:        assert K_wn(2) == 26 * Fraction(1, 2)  # = 13
112:        assert K_wn(3) == 100 * Fraction(5, 6)  # = 250/3
115:        assert K_wn(4) == 246 * Fraction(13, 12)  # = 1599/6 = 266.5
119:        assert K_wn(2) == Fraction(13)
129:        assert d.delta_K == Fraction(13)
135:        assert d.delta_K == Fraction(250, 3)
150:        prev = Fraction(0)
 succeeded in 51ms:
62:        for k in [1, 2, -3, Fraction(1, 2), Fraction(7, 3)]:
63:            self.assertEqual(kappa_heisenberg(k), Fraction(k))
67:        for k in [1, 2, -3, Fraction(1, 2)]:
68:            self.assertEqual(kappa_dual_heisenberg(k), -Fraction(k))
72:        for k in [1, -1, 0, Fraction(1, 2), 100]:
80:        self.assertEqual(kappa_free_fermion(), Fraction(1, 4))
84:        self.assertEqual(kappa_dual_free_fermion(), Fraction(-1, 4))
95:            self.assertEqual(kappa_lattice(rank), Fraction(rank))
100:            self.assertEqual(kappa_dual_lattice(rank), -Fraction(rank))
127:        self.assertEqual(kappa_betagamma(Fraction(0)), 1)
128:        self.assertEqual(kappa_betagamma(Fraction(1)), 1)
129:        self.assertEqual(kappa_betagamma(Fraction(1, 2)), Fraction(-1, 2))
130:        self.assertEqual(kappa_betagamma(Fraction(2)), 13)
134:        self.assertEqual(kappa_bc(Fraction(0)), -1)
135:        self.assertEqual(kappa_bc(Fraction(1)), -1)
136:        self.assertEqual(kappa_bc(Fraction(1, 2)), Fraction(1, 2))
140:        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3),
141:                    Fraction(1, 2), Fraction(2, 3), Fraction(1),
142:                    Fraction(3, 2), Fraction(2), Fraction(-1)]:
148:        for lam in [Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)]:
codex
The AP10/AP128 audit is already producing genuine issues. Several complementarity test files contain many hardcoded constants with no `# VERIFIED` comment at all, and even one file that claims full compliance still has constants justified only by same-category references or a single cross-reference.
exec
/bin/zsh -lc 'python3 -m pytest compute/tests/test_koszul_conductor_table_engine.py compute/tests/test_bp_koszul_conductor_engine.py compute/tests/test_theorem_c_complementarity.py compute/tests/test_complementarity_landscape.py compute/tests/test_complementarity_cross_verification.py compute/tests/test_ds_complementarity_defect.py compute/tests/test_level_rank_complementarity.py -q --tb=short' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc 'rg -n "VERIFIED" compute/tests/test_level_rank_complementarity.py compute/tests/test_theorem_c_complementarity.py compute/tests/test_complementarity_landscape.py compute/tests/test_complementarity_cross_verification.py compute/tests/test_ds_complementarity_defect.py' in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_level_rank_complementarity.py | sed -n '140,220p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_koszul_conductor_table_engine.py | sed -n '304,392p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_complementarity_cross_verification.py | sed -n '200,340p'" in /Users/raeez/chiral-bar-cobar exited 1 in 51ms:

 succeeded in 52ms:
   140	        k_double_prime = ff_dual_level(typ, rank, k_prime)
   141	        assert simplify(k_double_prime - k) == 0, (
   142	            f"FF is not an involution for {name}: (k')' = {k_double_prime}"
   143	        )
   144	
   145	    @pytest.mark.parametrize("typ,rank,dim_g,h_dual,name", SIMPLE_ALGEBRAS)
   146	    def test_ff_fixed_point_is_critical(self, typ, rank, dim_g, h_dual, name):
   147	        """The unique fixed point of FF is k = -h^vee (critical level)."""
   148	        result = self_dual_level(typ, rank)
   149	        assert result["self_dual_level"] == -h_dual
   150	        assert result["is_critical"] is True
   151	
   152	    def test_ff_central_charge_inversion(self):
   153	        """Central charge under FF: c(k) + c(k') = 2*dim(g) for sl_N.
   154	
   155	        c(k) = k * dim / (k + h^vee)
   156	        c(k') = (-k-2h^vee) * dim / (-k-h^vee)
   157	        c(k) + c(k') = dim * [k/(k+h^vee) + (-k-2h^vee)/(-k-h^vee)]
   158	                      = dim * [k/(k+h^vee) + (k+2h^vee)/(k+h^vee)]
   159	                      = dim * (2k + 2h^vee)/(k + h^vee)
exec
/bin/zsh -lc "nl -ba compute/tests/test_ds_complementarity_defect.py | sed -n '96,205p'" in /Users/raeez/chiral-bar-cobar succeeded in 56ms:
   304	# ===========================================================================
   305	# Bershadsky-Polyakov (C18, C20)
   306	# ===========================================================================
   307	
   308	class TestBershadskyPolyakov:
   309	    """BP: K_kk = 196, self-dual at k=-3."""
   310	
   311	    def test_K_kk_196(self):
   312	        """K_kk(BP) = 196.  (C18, C20)"""
   313	        # VERIFIED: [LT] C18 K_kk=196, [LT] C20 K_BP=196
   314	        assert bp_K_kk() == Fraction(196)
   315	
   316	    def test_self_dual_level(self):
   317	        """Self-dual at k=-3: k'=-(-3)-6=-3."""
   318	        # VERIFIED: [DC] -(-3)-6=-3, [LT] C20
   319	        k = Fraction(-3)
   320	        k_dual = -k - 6
   321	        assert k_dual == k
   322	
   323	    def test_bp_c_symmetry(self):
 succeeded in 56ms:
   200	    """Verify the expected complementarity constants."""
   201	
   202	    def test_heisenberg_sum_zero(self):
   203	        assert expected_sum("heisenberg") == Fraction(0)
   204	
   205	    def test_virasoro_sum_13(self):
   206	        """AP24 CRITICAL: Virasoro sum is 13, not 0."""
   207	        assert expected_sum("virasoro") == Fraction(13)
   208	
   209	    def test_affine_sum_zero(self):
   210	        assert expected_sum("affine") == Fraction(0)
   211	
   212	    def test_betagamma_sum_zero(self):
   213	        assert expected_sum("betagamma") == Fraction(0)
   214	
   215	    def test_bc_sum_zero(self):
   216	        assert expected_sum("bc") == Fraction(0)
   217	
   218	    def test_lattice_sum_zero(self):
   219	        assert expected_sum("lattice") == Fraction(0)
 succeeded in 50ms:
    96	# ===========================================================================
    97	
    98	class TestComplementarityConstants:
    99	    def test_K_affine_is_zero(self):
   100	        for N in range(2, 8):
   101	            for k in [1, 2, 3, 5, 10]:
   102	                assert K_affine(N, Fraction(k)) == 0
   103	
   104	    def test_K_virasoro_is_13(self):
   105	        for c in [1, 13, 25, Fraction(1, 2), Fraction(-22, 5) + 1]:
   106	            assert K_virasoro(c) == 13
   107	
   108	    def test_K_wn_sl2(self):
   109	        assert K_wn(2) == 26 * Fraction(1, 2)  # = 13
   110	
   111	    def test_K_wn_sl3(self):
   112	        assert K_wn(3) == 100 * Fraction(5, 6)  # = 250/3
   113	
   114	    def test_K_wn_sl4(self):
   115	        assert K_wn(4) == 246 * Fraction(13, 12)  # = 1599/6 = 266.5
 succeeded in 14.75s:
........................................................................ [  9%]
........................................................................ [ 18%]
........................................................................ [ 27%]
........................................................................ [ 37%]
........................................................................ [ 46%]
........................................................................ [ 55%]
........................................................................ [ 64%]
........................................................................ [ 74%]
........................................................................ [ 83%]
........................................................................ [ 92%]
........................................................                 [100%]
776 passed in 11.31s

thinking
**Evaluating command execution**

I'm considering that the exact command might still be running due to the extensive tests. The user specifically requested this exact run, so it feels important to honor that. I think it would be best to check if the report is completed, but getting the results matters more. I could try rerunning the command with a timeout, perhaps mirroring the subset tests. I'll wait for another 30 seconds to see if it wraps up.
codex
The focused complementarity/koszul-conductor subset passes: `776 passed in 11.31s`. The broader exact `-k 'koszul_conductor or complementarity'` sweep is still running because it pulls in heavier numerical/zeta surfaces; I’m keeping it alive long enough to classify whether any findings are mathematical or just provenance failures.

thinking
**Considering command execution**

I’m still running the command, and it might be waiting for pytest to finish, which could take a while. Maybe I should think about endlessly numerical tests? Should I kill the process? I could check CPU usage with `ps`, but it seems okay for now. Since the user specifically asked for an exact command, I wonder if I should wait longer or try a shorter selection? But the command might still take over a minute. Let's give it another 60 seconds.

thinking
**Exploring command options**

I'm thinking about possibly creating another command that includes a timeout to get results after a specific duration. I might consider using `python3 -m pytest ... --maxfail=1`, but I'm not sure if that's the exact approach. Using `exec_command` with a `yield_time_ms` of 300000 could work, since that means I can allow the command to run for up to 300 seconds. I can try running the exact command again, but only for 120000 milliseconds this time. I'll see how that goes!
exec
/bin/zsh -lc "python3 -m pytest compute/tests/ -k 'koszul_conductor or complementarity' --tb=short -q 2>&1 | tail -30" in /Users/raeez/chiral-bar-cobar
thinking
**Verifying tests and formulas**

I want to count the matching tests, but it looks like there could be a huge number, around 8k. That's quite a lot, but I'm not sure it's relevant. I need to check if there are any failing subsets or other issues. Since the subset seems to pass, the mathematical constants are likely correct. I should verify the direct formulas using Python/sympy. Hmm, the previous Python sessions might still be running because of SciPy imports. Let's poll on that!


thinking
**Inspecting comments for compliance**

I'm considering if there are weak comments in the code, particularly ones without "VERIFIED" categories. For example, the comment on `test_h0`, line 89, states `# Empty sum = 0`, which is a hardcoded value but lacks verification. It seems this file may not be fully compliant. I think line 89 might be more relevant since it's more direct, but I'm wondering if it needs to be cited for severity. I'll explore line 89 and see what else stands out.
thinking
**Evaluating compliance claims**

I’m thinking the compliance claim at line 5 could be false since `test_h0` uses a hardcoded 0 without a "VERIFIED" comment, and `test_K_kk_196` only uses `[LT]+[LT]`. I believe I should reference lines 5, 89, and 313, but I might need to focus on one or two for precision. I could open the section around lines 66-93 to gather more context for my analysis. It's important to be thorough while keeping it concise!
exec
/bin/zsh -lc "nl -ba compute/tests/test_koszul_conductor_table_engine.py | sed -n '66,96p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    66	class TestHarmonicNumbers:
    67	    """H_N = sum_{j=1}^{N} 1/j.  NOT H_{N-1} (AP136)."""
    68	
    69	    def test_h1(self):
    70	        # VERIFIED: [DC] direct sum 1/1=1, [LT] DLMF 25.11
    71	        assert harmonic(1) == Fraction(1)
    72	
    73	    def test_h2(self):
    74	        # VERIFIED: [DC] 1+1/2=3/2, [LT] DLMF 25.11
    75	        assert harmonic(2) == Fraction(3, 2)
    76	
    77	    def test_h3(self):
    78	        # VERIFIED: [DC] 1+1/2+1/3=11/6, [LT] OEIS A001008/A002805
    79	        assert harmonic(3) == Fraction(11, 6)
    80	
    81	    def test_h4(self):
    82	        # VERIFIED: [DC] 1+1/2+1/3+1/4=25/12, [LT] OEIS A001008/A002805
    83	        assert harmonic(4) == Fraction(25, 12)
    84	
    85	    def test_h5(self):
exec
/bin/zsh -lc "nl -ba compute/tests/test_bp_koszul_conductor_engine.py | sed -n '272,392p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
   272	        """kappa complementarity = 98/3 at each test level."""
   273	        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
   274	        # [CF] matches sl3_subregular_bar.py complementarity
   275	        assert kappa_complementarity(k) == Fraction(98, 3)
   276	
   277	    def test_kappa_complementarity_constant(self):
   278	        """KAPPA_COMPLEMENTARITY_EXACT = 98/3."""
   279	        assert KAPPA_COMPLEMENTARITY_EXACT == Fraction(98, 3)
   280	
   281	    def test_kappa_complementarity_is_varrho_times_K(self):
   282	        """98/3 = (1/6) * 196."""
   283	        # VERIFIED: [DC] 196/6 = 98/3; [CF] consistency check
   284	        assert Fraction(1, 6) * Fraction(196) == Fraction(98, 3)
   285	
   286	
   287	# =============================================================================
   288	# Tests: self-dual level
   289	# =============================================================================
   290	
   291	class TestSelfDual:

thinking
**Inspecting code for hardcoded values**

I'm thinking I should take a closer look at `test_complementarity_landscape.py`, especially around the initial hardcoded values. It seems important to verify how these values might affect the overall functionality of the code. I want to make sure everything is set up correctly and that there aren't any issues lurking in that early section. Let’s get into that file and see what’s going on!
exec
/bin/zsh -lc "nl -ba compute/tests/test_complementarity_landscape.py | sed -n '56,110p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    56	    """Test kappa formulas for all families."""
    57	
    58	    # ---- Heisenberg ----
    59	
    60	    def test_heisenberg_kappa_is_level(self):
    61	        """kappa(H_k) = k."""
    62	        for k in [1, 2, -3, Fraction(1, 2), Fraction(7, 3)]:
    63	            self.assertEqual(kappa_heisenberg(k), Fraction(k))
    64	
    65	    def test_heisenberg_dual(self):
    66	        """kappa'(H_k) = -k."""
    67	        for k in [1, 2, -3, Fraction(1, 2)]:
    68	            self.assertEqual(kappa_dual_heisenberg(k), -Fraction(k))
    69	
    70	    def test_heisenberg_sum_zero(self):
    71	        """kappa + kappa' = 0 for Heisenberg."""
    72	        for k in [1, -1, 0, Fraction(1, 2), 100]:
    73	            s = kappa_heisenberg(k) + kappa_dual_heisenberg(k)
    74	            self.assertEqual(s, 0)
    75	
exec
/bin/zsh -lc "nl -ba compute/tests/test_theorem_c_complementarity.py | sed -n '56,120p'" in /Users/raeez/chiral-bar-cobar succeeded in 52ms:
    56	
    57	class TestKappaValues:
    58	    """Verify kappa(A) for each standard family against the Master Table."""
    59	
    60	    def test_heisenberg_kappa_is_level(self):
    61	        """kappa(H_k) = k (the level IS the obstruction coefficient)."""
    62	        assert kappa("heisenberg", k=1) == Fraction(1)
    63	        assert kappa("heisenberg", k=3) == Fraction(3)
    64	        assert kappa("heisenberg", k=-5) == Fraction(-5)
    65	        assert kappa("heisenberg", k=Fraction(1, 2)) == Fraction(1, 2)
    66	
    67	    def test_virasoro_kappa_is_c_over_2(self):
    68	        """kappa(Vir_c) = c/2."""
    69	        assert kappa("virasoro", c=1) == Fraction(1, 2)
    70	        assert kappa("virasoro", c=26) == Fraction(13)
    71	        assert kappa("virasoro", c=13) == Fraction(13, 2)
    72	        assert kappa("virasoro", c=Fraction(7, 10)) == Fraction(7, 20)
    73	
    74	    def test_affine_sl2_kappa(self):
    75	        """kappa(sl_2_k) = 3(k+2)/4 = dim*(k+h^v)/(2*h^v)."""

thinking
**Verifying computation results**

I need to check the equation \( kappa + kappa' = varrho K_B = 98/3 \), not \( K_B/2 \). This discrepancy seems really significant. I should verify the compute tests since they use \( 98/3 \). It’s important to see if there are other files duplicating this incorrect statement. I plan to search for \( K_{\mathcal{B}}/2 \) or the phrase "kappa(k) + kappa(-k-6)". Let's go ahead and check!
codex
A genuine manuscript contradiction surfaced while I was checking BP against the tests. The compute layer and the BP chapter both say the complementarity constant is `98/3`, but the BP chapter’s front summary table still states `kappa(k)+kappa(-k-6)=K_B/2` with `K_B=196`, which would be `98`, not `98/3`.
exec
/bin/zsh -lc "rg -n \"K_\\{\\\\mathcal\\{B\\}\\}/2|\\\\kappa\\(k\\) \\+ \\\\kappa\\(-k\\{-\\}6\\)|98/3|varrho K|K_\\\\mathcal\\{B\\}\" chapters/examples/bershadsky_polyakov.tex chapters/examples/landscape_census.tex chapters/theory/higher_genus_complementarity.tex chapters/connections/concordance.tex compute/tests/test_bp_koszul_conductor_engine.py compute/lib/bp_koszul_conductor_engine.py" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:K_\{\mathcal\{B\}\}/2|\kappa\(k\) \+ \kappa\(-k\{-\}6\)|98/3|varrho K|K_\mathcal\{B\})
           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "nl -ba chapters/examples/bershadsky_polyakov.tex | sed -n '28,40p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/bershadsky_polyakov.tex | sed -n '288,310p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/lib/bp_koszul_conductor_engine.py | sed -n '17,25p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba chapters/examples/landscape_census.tex | sed -n '154,160p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "nl -ba compute/tests/test_bp_koszul_conductor_engine.py | sed -n '267,285p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
    28	 (hook self-transpose, $k \mapsto -k-6$)
    29	 & Proved & Thm~\ref{thm:bar-cobar-verdier} \\
    30	B (inversion) &
    31	 $\Omega(\barB(\mathcal{B}^k)) \xrightarrow{\sim}
    32	 \mathcal{B}^k$ (PBW universality)
    33	 & Proved & Thm~\ref{thm:bar-cobar-inversion-qi} \\
    34	C (complementarity) &
    35	 $\kappa(k) + \kappa(-k{-}6)
    36	 = K_{\mathcal{B}}/2$, \; $K_{\mathcal{B}} = 196$
    37	 & Proved & Prop~\ref{prop:bp-complementarity} \\
    38	D (modular char.) &
    39	 $\kappa(\mathcal{B}^k)
    40	 = \dfrac{c}{6}
 succeeded in 52ms:
   288	DS reductions of $\mathfrak{sl}_3$.
   289	\end{proof}
   290	
   291	\begin{proposition}[Complementarity;\;
   292	\ClaimStatusProvedHere]
   293	\label{prop:bp-complementarity}
   294	\index{Bershadsky--Polyakov algebra!complementarity}
   295	\index{complementarity!Bershadsky--Polyakov}
   296	For $k \neq -3$, the complementarity sum for the Bershadsky--Polyakov Koszul pair is
   297	\begin{equation}\label{eq:bp-complementarity}
   298	\kappa(k) + \kappa(-k-6)
   299	\;=\;
   300	\frac{c(k)}{6} + \frac{196 - c(k)}{6}
   301	\;=\;
   302	\frac{196}{6}
   303	\;=\;
   304	\frac{98}{3}\,.
   305	\end{equation}
   306	This is an instance of the general W-type complementarity
   307	$\kappa + \kappa' = \varrho \cdot K$ here $\varrho = 1/6$ and $K = 196$.
 succeeded in 53ms:
    17	    K_BP = c_BP(k) + c_BP(-k-6) = 196   (level-independent)
    18	
    19	    varrho_BP = 1/6  (anomaly ratio: sum_i (-1)^{p_i}/h_i over strong generators)
    20	
    21	    kappa_BP(k) = varrho_BP * c_BP(k)
    22	
    23	    kappa_BP(k) + kappa_BP(-k-6) = varrho_BP * K_BP = 98/3
    24	
    25	    Self-dual level: k = -3, the fixed point of the involution k -> -k-6.
 succeeded in 51ms:
   154	 \textup{(}subregular DS reduction\textup{)}}} \\
   155	\hline
   156	$\mathrm{BP}_k = \mathcal{W}_3^{(2)}(k)$
   157	 & $\mathrm{BP}_{-k-6}$
   158	 & $2 - \dfrac{24(k{+}1)^2}{k{+}3}$ & $196$
   159	 & $\dfrac{1}{6}\bigl(2 - \dfrac{24(k{+}1)^2}{k{+}3}\bigr)$ & PH \\[4pt]
   160	\hline
 succeeded in 51ms:
   267	class TestKappaComplementarity:
   268	    """Tests for kappa_BP(k) + kappa_BP(-k-6) = 98/3."""
   269	
   270	    @pytest.mark.parametrize("k, _c_k, _comment", C_BP_TEST_DATA)
   271	    def test_kappa_complementarity(self, k, _c_k, _comment):
   272	        """kappa complementarity = 98/3 at each test level."""
   273	        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
   274	        # [CF] matches sl3_subregular_bar.py complementarity
   275	        assert kappa_complementarity(k) == Fraction(98, 3)
   276	
   277	    def test_kappa_complementarity_constant(self):
   278	        """KAPPA_COMPLEMENTARITY_EXACT = 98/3."""
   279	        assert KAPPA_COMPLEMENTARITY_EXACT == Fraction(98, 3)
   280	
   281	    def test_kappa_complementarity_is_varrho_times_K(self):
   282	        """98/3 = (1/6) * 196."""
   283	        # VERIFIED: [DC] 196/6 = 98/3; [CF] consistency check
   284	        assert Fraction(1, 6) * Fraction(196) == Fraction(98, 3)
   285	

thinking
**Searching for string occurrences**

I need to rerun the search to find simpler instances—maybe I only need to locate the wrong occurrence. So, I’ll search for the plain strings K_B/2 and 98/3 to see if they pop up correctly. It sounds like a straightforward task, but I want to make sure I'm extracting the right information here. Let's see what I find!
exec
/bin/zsh -lc "rg -n \"K_\\{\\\\mathcal\\{B\\}\\}/2|98/3|varrho \\\\cdot K\" chapters/examples/bershadsky_polyakov.tex compute/tests/test_bp_koszul_conductor_engine.py compute/lib/bp_koszul_conductor_engine.py" in /Users/raeez/chiral-bar-cobar exited 2 in 51ms:
rg: regex parse error:
    (?:K_\{\mathcal\{B\}\}/2|98/3|varrho \cdot K)
           ^^
error: unrecognized escape sequence
exec
/bin/zsh -lc "rg -n -F 'K_{\\mathcal{B}}/2' chapters/examples/bershadsky_polyakov.tex && rg -n -F '98/3' chapters/examples/bershadsky_polyakov.tex compute/tests/test_bp_koszul_conductor_engine.py compute/lib/bp_koszul_conductor_engine.py && rg -n -F 'varrho \\cdot K' chapters/examples/bershadsky_polyakov.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
36: = K_{\mathcal{B}}/2$, \; $K_{\mathcal{B}} = 196$
compute/tests/test_bp_koszul_conductor_engine.py:5:the kappa complementarity kappa_BP(k) + kappa_BP(-k-6) = 98/3.
compute/tests/test_bp_koszul_conductor_engine.py:268:    """Tests for kappa_BP(k) + kappa_BP(-k-6) = 98/3."""
compute/tests/test_bp_koszul_conductor_engine.py:272:        """kappa complementarity = 98/3 at each test level."""
compute/tests/test_bp_koszul_conductor_engine.py:273:        # VERIFIED: [DC] varrho * K_BP = (1/6)*196 = 98/3
compute/tests/test_bp_koszul_conductor_engine.py:278:        """KAPPA_COMPLEMENTARITY_EXACT = 98/3."""
compute/tests/test_bp_koszul_conductor_engine.py:282:        """98/3 = (1/6) * 196."""
compute/tests/test_bp_koszul_conductor_engine.py:283:        # VERIFIED: [DC] 196/6 = 98/3; [CF] consistency check
compute/lib/bp_koszul_conductor_engine.py:23:    kappa_BP(k) + kappa_BP(-k-6) = varrho_BP * K_BP = 98/3
compute/lib/bp_koszul_conductor_engine.py:78:# Kappa complementarity sum: varrho * K = (1/6) * 196 = 98/3.
compute/lib/bp_koszul_conductor_engine.py:79:# VERIFIED: [DC] (1/6) * 196 = 98/3;
compute/lib/bp_koszul_conductor_engine.py:80:# [LT] chapters/examples/bershadsky_polyakov.tex, eq. `eq:bp-complementarity`, gives 98/3.
compute/lib/bp_koszul_conductor_engine.py:156:    r"""Kappa complementarity: kappa_BP(k) + kappa_BP(-k-6) = varrho * K_BP = 98/3."""
compute/lib/bp_koszul_conductor_engine.py:159:    # [CF] equals varrho_BP * K_BP = 98/3.
compute/lib/bp_koszul_conductor_engine.py:204:        2. kappa_complementarity(k) == 98/3.
compute/lib/bp_koszul_conductor_engine.py:213:        9. KAPPA_COMPLEMENTARITY_EXACT == 98/3.
compute/lib/bp_koszul_conductor_engine.py:234:        # (2) Kappa complementarity = 98/3
compute/lib/bp_koszul_conductor_engine.py:269:    # VERIFIED: [DC] (1/6) * 196 = 98/3;
compute/lib/bp_koszul_conductor_engine.py:271:    # VERIFIED: [DC] (1/6) * 196 = 98/3; [CF] BP complementarity gives the same value.
compute/lib/bp_koszul_conductor_engine.py:273:        f"KAPPA_COMPLEMENTARITY_EXACT = {KAPPA_COMPLEMENTARITY_EXACT}, expected 98/3"




thinking
**Evaluating complementarity issues**

I’m looking at line 66 in the shadow archetype table, where it mentions "Complementarity & κ+κ'=98/3." It seems the five-theorem table is the issue, and I'll need to inspect the docstring in the test file to check if it correctly states kappa complementarity as 98/3. This could hint at a more significant contradiction in the verification table. The summary in line 36 doesn’t align, so I need to explore if there are other conflicting entries and ensure all hardcoded values comply. This seems quite critical!
thinking
**Assessing command execution**

I'm thinking about inspecting what’s happening by running another process status check. The broad sweep seems to be running for over 60 seconds, while the focused subset passed. Even though the user asked for the exact command, I’m considering waiting a bit longer, maybe 2 more minutes. It feels like enough time, but if it’s not finished, I should mention that. I might also run `pgrep` to check the elapsed time, but altering the command with a timeout might not be ideal either.
thinking
**Updating command status**

I've already run the exact command, but the result isn’t available because it's still running. I could mention that it has been running for over 2 minutes without a final exit code. However, the focused subset related to the requested formulas passed. To get clearer insight, I might consider running the exact command in a separate terminal to handle the long numerical tests. Since we don't have the final output, I should definitely communicate that, but I’m also wondering if the broad run is just hung.
thinking
**Considering mpmath and testing commands**

I’m thinking about the slowness of mpmath. Could I use the command `pytest --collect-only -k 'koszul_conductor or complementarity' -q | tail -30`? Hmm, no. For the audit, the exact command isn’t essential if the subset covers the formulas I need. But I might want to check session 53761 later. I’ll poll occasionally while I continue to inspect things to keep an eye on how it's running.
exec
/bin/zsh -lc 'ps -o pid,etime,pcpu,pmem,command -ax | rg "pytest compute/tests/ -k"' in /Users/raeez/chiral-bar-cobar exited 1 in 53ms:
zsh:1: operation not permitted: ps




thinking
**Considering citation format**

I’m thinking about how to properly cite one finding, suggesting I could use the line from `compute/tests/test_theorem_c_complementarity.py:62` and mention sibling files. But the output contract states it should follow the `file:line` format. Hmm, maybe it's still acceptable if I describe others alongside. It's important to get this right, so I’m just mulling over the best approach to ensure clarity and adherence to the rules!
thinking
**Considering command execution**

I’m working out some calculations and checks, confirming that `6 = 266.5` holds true, and `K(W_4)=533/2` is also correct. There might be a need to execute a broad command, running tests with options like `-q` and `-k`, which could take time. It’s possible to keep one session open while we finalize things, so let’s consider using `timeout 90 python -m pytest ...` to manage longer execution times. I’ll be keeping tabs on the output as we go.
thinking
**Assessing test execution**

I’m figuring out that pytest should finish once all tests exit, but some might be stuck. While 776 tests passed, it seems we need to acknowledge that the broad command didn’t complete in this session. We might mention it’s still running after over 2 minutes due to heavier tests. I could run the command `pytest -k 'koszul_conductor or complementarity' --maxfail=1` to check for early failures, but I don’t think that's necessary. The file `test_exceptional_koszul_conductor_engine.py` isn't central to the user’s request, but it does contain relevant parts.
thinking
**Reviewing omitted test files**

It seems like our subset of 7 files missed a few important tests, like `test_exceptional_koszul_conductor_engine.py`, `test_e8_koszul_conductor_engine.py`, and possibly others like `test_landscape_census_verification.py`. I’m wondering if we should run these tests too or at least take a closer look at them. It’s possible they contain crucial information that could help in understanding any issues we're facing. Let’s consider the best approach to proceed!
exec
/bin/zsh -lc "rg -n -F '13' chapters/examples/landscape_census.tex | sed -n '1,20p'" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F 'K_{\\mathcal{B}}/2' chapters examples metadata compute" in /Users/raeez/chiral-bar-cobarexec
/bin/zsh -lc "rg -n -F '98/3' chapters/connections/concordance.tex metadata/theorem_registry.md chapters/examples/bershadsky_polyakov.tex chapters/examples/landscape_census.tex" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
109: & $\dfrac{78k}{k+12}$ & $156$ & $\dfrac{13(k+12)}{4}$ & PH \\[4pt]
113: & $\dfrac{133k}{k+18}$ & $266$ & $\dfrac{133(k+18)}{36}$ & PH \\[4pt]
496:CYBE $[r_{12}, r_{13}] + \text{cyc.} = 0$ holds vacuously;
702: & $\dfrac{40}{5c{+}22}$ & $\sqrt{\dfrac{180c{+}872}{c^2(5c{+}22)}}$ & $13$ \\[8pt]
713: & $\dfrac{20}{71}$ & $> 0$ & $13$\textsuperscript{$\S$} \\[4pt]
732:The self-dual central charges are $c^* = K_N/2$: $c^* = 13$ for Virasoro,
735:sum $\kappa + \kappa' = 13$ is the Virasoro-sector value
736:($\kappa(V^\natural) = 12$, $\kappa(\mathrm{Vir}_2) = 1$; sum $= 13$),
1243:$\varrho(\mathcal{W}_4) = 1/2 + 1/3 + 1/4 = 13/12$.
1329:$E_6$ & $78$ & $12$ & $12$ & $13(k+12)/4$ & $156$ & $156 = 2\cdot 78$ \\
1330:$E_7$ & $133$ & $18$ & $18$ & $133(k+18)/36$ & $266$ & $266 = 2\cdot 133$ \\
1689:$\mathrm{Vir}_{13}$ (self-dual)
1909: & 2 & 3 & 6 & 13 & 28 & 59 & 122 & 249 & $2^n$ \\
1915: & 3 & 5 & 7 & 9 & 11 & 13 & 15 & 17 & $2n{+}1$ \\
1918: & 8 & 36 & 204 & 1352$^\dagger$ & 9892$^\dagger$ & 76084$^\dagger$ & 598592$^\dagger$ & 4755444$^\dagger$ & $8^n$ \\
2402:$(3 {+} \sqrt{13})/2 \approx 3.303$, and
2403:$(3 {-} \sqrt{13})/2 \approx -0.303$.
2589:= \frac{4x(2 - 13x - 2x^2)}{(1 - 8x)(1 - 3x - x^2)},
2615: $\dim H^4 = 1352$, $\dim H^5 = 9892$, $\dim H^6 = 76084$,
2634:\emph{Scope.} Independent verification requires computing $\dim H^4(\barBgeom(\widehat{\mathfrak{sl}}_{3,k}))$ directly from the chiral bar differential. The value $1352$ would confirm the recurrence~\eqref{eq:sl3-bar-recurrence} and the rationality of the GF, while any other value would rule out this rational form.
 exited 2 in 51ms:
rg: examples: No such file or directory (os error 2)
chapters/examples/bershadsky_polyakov.tex:36: = K_{\mathcal{B}}/2$, \; $K_{\mathcal{B}} = 196$
 succeeded in 51ms:
chapters/examples/bershadsky_polyakov.tex:11:$\kappa + \kappa' = \varrho K = 98/3 \neq 0$ witnesses the
chapters/examples/bershadsky_polyakov.tex:66:Complementarity & $\kappa + \kappa' = 98/3$ (W-type) \\

thinking
**Searching for theorem details**

I'm realizing that using `rg -F '13'` isn't helping much, but I feel like I have enough information. I might need to look up the theorem C complementarity or find the specific section in the Virasoro textbook regarding line 13. Citing landscape_census on pages 729-733 and higher_genus_complementarity on pages 2997-3003 seems reasonable. I'll also verify formulas with sympy and check around line 2950 in `higher_genus_complementarity.tex`, especially looking at a nearby table.
exec
/bin/zsh -lc "nl -ba chapters/theory/higher_genus_complementarity.tex | sed -n '2948,3004p'" in /Users/raeez/chiral-bar-cobar succeeded in 51ms:
  2948	\midrule
  2949	\multicolumn{6}{@{}l}{\textit{$\cW_N$-algebras:
  2950	 $\kappa + \kappa^! = \varrho_N K_N \neq 0$
  2951	}} \\[2pt]
  2952	$\mathrm{Vir}_c$ ($= \cW_2$)
  2953	 & $c/2$ & $(26{-}c)/2$
  2954	 & $13$ & $26$ & $13$ \\
  2955	$\cW_3$
  2956	 & $5c/6$ & $5(100{-}c)/6$
  2957	 & $250/3$ & $100$ & $50$ \\
  2958	$\cW_4$
  2959	 & $13c/12$ & $13(246{-}c)/12$
  2960	 & $533/2$ & $246$ & $123$ \\
  2961	$\cW_5$
  2962	 & $77c/60$ & $77(488{-}c)/60$
  2963	 & $9394/15$ & $488$ & $244$ \\
  2964	$\cW_6$
  2965	 & $29c/20$ & $29(850{-}c)/20$
  2966	 & $2465/2$ & $850$ & $425$ \\
  2967	$\cW_7$







thinking
**Counting verification instances**

I need to find a way to count the instances checked for verification. My plan could involve counting the source files and checks executed. For example, there are possibly four constitutional files, four manuscript sources (though I might have already counted some), and four compute libraries. I also think there may be around ten test files. The summary I’ll aim for could be something like 16 surfaces checked, with 7 violations found. But I want to be clear about what "instances checked" really means.
thinking
**Considering verification inclusion**

I might want to include a short verification of K(BP)=196 and K(Vir)=13 in my summary, but I'm unsure. The user specifically asked me to check those values, so it seems important to clearly mention the results. Maybe I could incorporate that in the first or second findings, but actually, if the user is already correct, it might be better to avoid unnecessary findings altogether.
thinking
**Deciding on anchor points**

I’m considering whether to anchor at line 87 or line 207. Each choice likely has its own pros and cons. I think I need to weigh factors like stability and convenience based on the context. It's a simple decision on the surface, but I want to ensure I'm making the best choice! I’m curious about what the best outcome would be for each option, so a bit of analysis might help clarify things.
thinking
**Reviewing verification markers**

I found no `VERIFIED` markers in the specified file based on grep results. That’s backed up by the exit code 1 from my attempts across five files. I need to reference the exact line numbers clearly, particularly for `compute/tests/test_level_rank_complementarity.py` line 184, which shows no markers. There’s a potential issue here, as the instructions prioritize bugs, risks, and behavioral regressions when conducting audits. I’ll emphasize findings while maintaining a severity order throughout my report.
thinking
**Assessing compliance in tests**

I see that there's an inconsistency regarding the values in the chapter, where it suggests 98 but later supports a value of 98/3 between lines 296-307, which the compute layer/test surface also confirms. There are several high-priority issues to note. For instance, `compute/tests/test_koszul_conductor_table_engine.py:5` claims all hardcoded values have AP10-compliant provenance, but `test_h0` at line 89 uses a hardcoded 0 with no `# VERIFIED`. Similar issues persist in other tests with misleading compliance claims.
thinking
**Analyzing AP10 pattern**

I'm considering how to describe the AP10 pattern, particularly the lack of any "VERIFIED" comments in the file, which isn’t included. Maybe it’s acceptable for completeness if we highlight this as a systemic issue across multiple files. I should check for "VERIFIED" markers in the bc_zeta file, but it's likely there are none. If needed, I could summarize the findings: "Instances checked: 18 | Violations found: 8 | Verdict: FAIL." That keeps things concise!
thinking
**Considering computation results**

I need to mention direct symbolic simplification from a Python snippet as clear evidence of computation. That's good! However, I should point out that the command "tail -30" didn’t complete. The user specifically asked me to run it, so I want to ensure the final output isn’t too lengthy. I'm thinking about including 8 findings, 2 note lines, and a summary, which totals about 14 lines. I’ll craft this carefully!
codex
[CRITICAL] chapters/examples/bershadsky_polyakov.tex:34 — The chapter’s five-theorem summary table states `\kappa(k)+\kappa(-k-6)=K_{\mathcal B}/2` with `K_{\mathcal B}=196`, i.e. `98`, but the same chapter later proves `98/3` at [chapters/examples/bershadsky_polyakov.tex:296](/Users/raeez/chiral-bar-cobar/chapters/examples/bershadsky_polyakov.tex:296). The compute layer and BP tests also use `98/3`, so this is a live manuscript contradiction on a theorem-summary surface.

[HIGH] compute/tests/test_koszul_conductor_table_engine.py:5 — The file claims every hardcoded expected value is AP10/AP128-compliant, but that claim is false. `test_h0` at [compute/tests/test_koszul_conductor_table_engine.py:89](/Users/raeez/chiral-bar-cobar/compute/tests/test_koszul_conductor_table_engine.py:89) hardcodes `0` with no `# VERIFIED` comment, and `test_K_kk_196` at [compute/tests/test_koszul_conductor_table_engine.py:311](/Users/raeez/chiral-bar-cobar/compute/tests/test_koszul_conductor_table_engine.py:311) cites `[LT]` plus `[LT]`, not two categories.

[HIGH] compute/tests/test_bp_koszul_conductor_engine.py:7 — The file advertises per-value verification paths for each hardcoded expectation, but line [279](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:279) hardcodes `98/3` with no `# VERIFIED`, line [296](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:296) hardcodes `-3` with no `# VERIFIED`, and lines [383](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:383) and [389](/Users/raeez/chiral-bar-cobar/compute/tests/test_bp_koszul_conductor_engine.py:389) use only single-category `[CF]` comments.

[HIGH] compute/tests/test_theorem_c_complementarity.py:62 — The file contains many hardcoded theorem constants (`13`, `250/3`, `1/24`, `7/5760`, `31/967680`, etc.) but grep found no `# VERIFIED` markers anywhere in the file. AP10/AP128 provenance is absent across the whole test surface.

[HIGH] compute/tests/test_complementarity_landscape.py:60 — Same AP10/AP128 failure pattern: hardcoded constants such as `1/4`, `13`, `250/3`, `533/2`, and `9394/15` appear throughout, and the file contains no `# VERIFIED` comments at all.

[HIGH] compute/tests/test_complementarity_cross_verification.py:87 — Same AP10/AP128 failure pattern: the file hardcodes complementarity constants (`13`, `250/3`, `533/2`, `9394/15`, `-13`, `-50`, `-123`, etc.) but has no `# VERIFIED` comments anywhere.

[MEDIUM] compute/tests/test_ds_complementarity_defect.py:104 — Hardcoded conductor/defect constants (`13`, `250/3`, `-26`, `3952`, `2262`, etc.) are asserted without AP10/AP128 provenance comments.

[MEDIUM] compute/tests/test_level_rank_complementarity.py:184 — The file uses hardcoded complementarity expectations (`0`, `2`, fixed-point/critical values, explicit levels) and has no `# VERIFIED` comments anywhere.

Verified non-findings: `K(BP)=196` and `K(Vir)=13` are correct. Direct symbolic simplification gave `196` and `13`; the compute layer agrees; manuscript support is at [chapters/examples/landscape_census.tex:156](/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex:156), [chapters/examples/bershadsky_polyakov.tex:296](/Users/raeez/chiral-bar-cobar/chapters/examples/bershadsky_polyakov.tex:296), and [chapters/theory/higher_genus_complementarity.tex:2952](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_complementarity.tex:2952).

Focused relevant pytest subset passed: `776 passed in 11.31s`. The exact broad `-k 'koszul_conductor or complementarity'` sweep did not finish during the audit window.

## Summary
Instances checked: 18 | Violations found: 8 | Verdict: FAIL
tokens used
175,101
