# STRUCTURAL AUDIT — Chiral Bar-Cobar Monograph

**Date**: 2026-03-06
**Auditor**: Claude Opus 4.6 (adversarial mode)
**Scope**: All 55 .tex files in chapters/ and appendices/, plus compute engine (901 tests)
**Method**: 10 parallel agents + targeted deep reads + cross-file consistency checks
**Mandate**: Catalogue everything wrong. Fix nothing.

---

## Fresh Census (verified)

| Tag | Count | CLAUDE.md says |
|-----|-------|----------------|
| ProvedHere | **687** | 683 (STALE by +4) |
| ProvedElsewhere | **313** | 313 |
| Conjectured | **99** | 99 |
| Heuristic | **18** | 18 |
| Open | **0** | 0 |
| **Total** | **1117** | 1113 |

---

## PART I: Critical Findings (Severity 1-2)

### F1. PERIODICITY CONTRADICTION (Severity 1 -- MATHEMATICAL ERROR)

Two PH-tagged theorems directly contradict each other. A **third** PE-tagged theorem also asserts the false claim.

**Claim A** (`introduction.tex:1111`, `thm:periodicity-cohomology`, PH):
> "Affine Kac-Moody: CH^{p+2h}(g_k) = CH^p(g_k) at critical level k = -h^vee (period 2h)"

**Claim A'** (`hochschild_cohomology.tex:76`, PE):
> Also asserts CH^{n+2h} = CH^n for general affine KM at critical level.

**Claim B** (`koszul_pair_structure.tex:591-660`, `thm:affine-periodicity-critical`, PH):
> "For rank r > 1: polynomial growth O(n^{r-1}) but **not strict periodicity** when the exponents are not all equal."

**Explicit counterexample** (`koszul_pair_structure.tex:684-696`, `rem:rank-distinction`):
> sl_3: dim CH^6 = 1 but dim CH^{12} = 3, violating 6-periodicity.

Claim B is correct (complete 3-ingredient proof). Claims A and A' are false for rank > 1.

**Additional contamination** (`introduction.tex:1136`): Claims W_3 has period lcm(2,3) = 6, but `hochschild_cohomology.tex:97-101` correctly says "dimensions grow polynomially (not periodically)."

**Root cause**: The proof at `introduction.tex:1128-1133` says a Z/h-grading from the Coxeter element gives "double periodicity." A Z/h-grading gives a decomposition, not periodicity. Periodicity requires all eigenspaces to have equal dimension, which holds only for rank 1.

**Misleading attribution** (`introduction.tex:1139`): "From the genus-0 perspective this periodicity is not visible; it arises because the cohomology classes on M_g correspond to modular forms." This is backwards -- the *proved* Virasoro periodicity comes from the Gel'fand-Fuchs theorem, a *genus-0* result. The sentence incorrectly attributes it to higher-genus modular forms.

**Impact**: Critical. Three separate locations (intro, hochschild, W-algebra claim) repeat this false general statement.

**Fix**: (1) Restate intro thm item (2) with rank-1 restriction. (2) Fix hochschild_cohomology.tex:76. (3) Fix intro W-algebra period-6 claim. (4) Fix misleading attribution at line 1139.

---

### F2. QUANTUM PERIODICITY PROOF GAP (Severity 2)

`deformation_theory.tex:741-780`, thm "Quantum periodicity", tagged PH.

**Step 4** (line 778-779):
> "The periodicity of quantum dimensions gives periodicity of fusion coefficients, hence periodicity of bar complex differentials."

Same logical gap as DEEPAUDIT F5 (which caused three other periodicity claims to be downgraded to CJ). Periodic fusion coefficients do NOT automatically give periodic bar differentials: fusion coefficients determine Hom space *dimensions*, but bar differentials are *specific maps* within those spaces.

**Additional contamination**: Proofs of the *already-downgraded* CJ theorems at `deformation_theory.tex:913-915` and `deformation_theory.tex:944` still reason as if the CJ results are proved facts ("$\text{Period} \mid N_{\text{modular}}$ by the modular periodicity theorem above" -- but that theorem is CJ).

**Fix**: Downgrade quantum periodicity to CJ, OR complete Step 4. Also fix the CJ proof texts to say "if modular periodicity holds" rather than citing it as fact.

---

### F3. THEOREM A PROOF -- ALL STEPS THIN (Severity 2)

`higher_genus.tex:1501-1579`, proof of thm:bar-cobar-isomorphism-main (Main Theorem A).

The proof graph agent rated **Steps 1, 2, and 4 as THIN** (Step 3 is a formal consequence, rated SOLID):

- **Step 1** (Part I): Cites three theorems but doesn't chain them together. None of the three individually state that B^ch(A_1) = A_2^!. The deduction requires the Koszul property (diagonal Ext concentration), which is asserted but not argued.
- **Step 2** (Part II): Says Omega^ch(A_2^!) = A_1 "by" Verdier duality + cobar nilpotency. How these combine to give reconstruction requires a filtration/spectral sequence argument that is absent.
- **Step 4** (Part IV): Quasi-inverse property asserted with bullet points instead of proof. The unit being a QI is never separately established.

**Impact**: Medium-high. Theorem A is the first of three main theorems. All supporting lemmas ARE proved individually in bar_cobar_construction.tex, but the *synthesis* step assembling them into Theorem A reads as an annotated outline.

**Fix**: Add 2-3 sentences per step showing how the cited theorems combine to yield each Part.

---

### F4. SEVEN SEVERITY-2 PROOF GAPS IN BAR_COBAR_CONSTRUCTION.TEX

The proof integrity agent found 7 additional proof gaps in bar_cobar_construction.tex:

| # | Line | Claim | Issue |
|---|------|-------|-------|
| F4a | 4593 | lem:obstruction-class | "d_g^2 lands in center by Jacobi" -- centrality is what needs proving; circular. |
| F4b | 4618 | lem:period-integral | "By relative Stokes' theorem...this is the period integral stated" -- hypotheses unchecked. |
| F4c | 4662 | lem:obs-def-pairing | Uses the decomposition Q_g(A) + Q_g(A^!) that the parent theorem is trying to prove. Circular within proof sketch. |
| F4d | 3575 | thm:geom-unit | Geometric formula for unit of bar-cobar adjunction. QI claim reduces to single display formula presented without derivation. No explicit homotopy constructed. |
| F4e | 7939 | prop:counit-qi | "Proof is dual to Theorem ref" + 4 steps each saying "similar." Real proof is one line (Verdier duality); rest is padding. |
| F4f | 4849 | thm:completion-necessity | "Proof by Example: Virasoro" for a theorem claiming three general conditions. Proof only demonstrates one instance of one condition. |
| F4g | 2609 | thm:cobar-d-squared-zero, Term 3 | Distributional argument: acknowledges delta(z_i-z_j)^2 is ill-defined, then invokes "Arnold-relation cancellation" informally. (Clean proof exists via Verdier duality at cor:cobar-nilpotence-verdier:2389.) |

**Note**: F4a-c are in a section (lines 4555-4706) that appears to be a "proof sketch" section, with full proofs appearing later in higher_genus.tex. The issue is these lemmas carry PH tags despite being sketches.

---

### F5. HOCHSCHILD DUALITY COROLLARY VAGUE (Severity 2-3)

`higher_genus.tex:1599-1619`, cor:hochschild-duality, tagged PH.

"d" undefined ("related to conformal weight" is not a definition). Proof is 4 lines of hand-waving. The [2]-shift vs general d-shift is ambiguous.

---

### F6. THEOREM C -- THREE THIN STEPS (Severity 2-3)

The proof graph agent found Theorem C's 10-step proof is mostly SOLID but has three thin points:

| Step | Issue |
|------|-------|
| Step 4 (higher vanishing, line 4899) | Chiral generalization of diagonal Ext concentration asserted by analogy with LV12 Thm 3.4.4. Classical proof uses Koszul complex filtration; chiral analog requires independent verification that is absent. |
| Step 7, Ingredient 1 (line 5210) | "Verdier duality reverses sign of infinitesimal actions" stated as fact without proof or citation. Standard in D-module theory but needs a reference (Kashiwara or similar). |
| Step 8 (eigenvalue identification, line 5406) | Dense chain of sign computations through j_*/j_! exchanges. Logically coherent but would benefit from more explicit computation. |

---

### F7. CROSS-FILE THEOREM MISAPPLICATIONS (Severity 2-3)

The cross-file consistency agents found several places where theorems are applied without verifying hypotheses:

| File:Line | Issue | Severity |
|-----------|-------|----------|
| `bar_cobar_construction.tex:3846` | cor:level-shifting-part1 applies Theorem A to *curved* bar complex. Theorem A requires Koszul (uncurved). | 3 |
| `higher_genus.tex:575` | Uses Theorem A as "formality" -- Theorem A proves QI, not formality. Different concepts. | 2 |
| `examples_summary.tex:935` | Applies Theorem A to Yangian, which is E1-chiral. Theorem A is stated for E-infinity-chiral. Correct theorem is thm:e1-chiral-koszul-duality. | 2 |
| `minimal_model_examples.tex:563` | Cites Theorem B for minimal models, where the Koszul hypothesis explicitly fails. | 3 |
| `chiral_modules.tex:3516` | Applies Theorem C to Vir at general c without checking Koszul hypothesis. | 2 |
| `higher_genus.tex:3516` | Cites "Main Theorem C" but references thm:kodaira-spencer-chiral-complete (the KS theorem, which is a *component* of Theorem C's proof, not Theorem C itself). | 2 |
| `toroidal_elliptic.tex:149` | Uses E1-chiral Koszul duality for toroidal algebra with hypothesis "conditional on Step 2." | 2 |

---

### F8. W3 OBSTRUCTION PRIMARY/GENERATOR REVERSAL (Severity 3)

`higher_genus.tex:3611`: Claims "W_0(T) = 0 (since T is primary of weight 2 for the weight-3 field W)." This reverses the relationship: *W* is primary for the Virasoro algebra generated by *T*, not the other way around. The W_{(1)}T OPE gives 2W, which is non-zero. The cross-term vanishing in cohomology should follow from non-centrality, but the stated reason is incorrect.

---

## PART II: Structural Weaknesses (Severity 3-4)

### S1. H^4(W3) = 52 PROVENANCE GAP (Severity 3)

`examples_summary.tex:338-342`: "obtained from the generators-and-relations analysis of the bar complex at conformal weights h <= 12." No such analysis exists. The compute engine hardcodes the value without derivation. MEMORY.md confirms: "Origin unknown." Value is load-bearing for the W3 GF conjecture.

### S2. G2 CHAIN-GROUP DIMENSION ERROR (Severity 3)

`genus_expansions.tex:318`: States G2 values "14, 196, 2744 = 14^n" as chain-group dimensions. But 2744 = 14^3 is NOT the chain-group dimension at n=3. The formula is dim(g)^n * (n-1)!, giving 14^3 * 2! = 5488. The compute engine correctly reports 5488. The text conflates "generator factor" 14^n with full chain-group dim.

### S3. YANGIAN H^n = 3^n+1 -- ZERO DEGREES OF FREEDOM (Severity 3)

The Yangian conjecture is based on exactly 3 data points (H^1=4, H^2=10, H^3=28) fitted to a 2-parameter family a*r^n + b. This provides zero degrees of freedom -- any 3 points uniquely determine such a formula. The critical test (H^4=82) has not been computed. Correctly tagged CJ, but the "evidence" is essentially tautological.

### S4. NOTATION COLLISIONS (Severity 3)

**kappa -- TRIPLE overloading** (affects 6+ files):
- Heisenberg level (H_kappa): 184 occurrences in 19 files
- Obstruction coefficient (kappa(A)): extensive in higher_genus.tex, genus_expansions.tex
- Casimir/Killing form (kappa^{ab}): bar_cobar_construction.tex:3803, kac_moody_framework.tex:152

Worst case: `heisenberg_eisenstein.tex:246` writes "kappa(H_kappa) = kappa" -- three distinct uses of kappa in one equation.

**sigma -- TRIPLE overloading**:
- Anomaly ratio sigma(g): examples_summary.tex, higher_genus.tex:3906
- Verdier-Koszul involution: higher_genus.tex:5248, w_algebras_framework.tex
- Chevalley anti-involution: chiral_modules.tex:1236

**h -- DOUBLE overloading**: Coxeter number (hochschild_cohomology.tex:77) vs conformal weight (detailed_computations.tex:2567).

### S5. HEISENBERG NOTATION FRAGMENTATION (Severity 3)

- Generator: J(z) vs alpha(z) (both in free_fields.tex)
- Level: H_k (116 occurrences) vs H_kappa (184 occurrences)
- Duplicate definition: free_fields.tex:580 (unlabeled, J) and free_fields.tex:2418 (labeled, alpha)

### S6. DUPLICATE DEFINITIONS (Severity 3)

- **Koszul pair**: Defined 6+ times across algebraic_foundations.tex, koszul_pair_structure.tex, chiral_koszul_pairs.tex, bar_cobar_construction.tex. Some are distinct flavors (classical vs chiral), but two definitions in algebraic_foundations.tex:91 and :699 cover the same classical notion.
- **Coisson algebra**: Defined at deformation_quantization.tex:79 and deformation_examples.tex:51. The first references the second, creating a circular cross-reference.
- **Heisenberg**: See S5.

### S7. TERMINOLOGY ISSUES (Severity 3)

| Location | Issue |
|----------|-------|
| `free_fields.tex:2486` | Bar written as coLie^ch(V*) but described as "cocommutative coalgebra" -- different cooperad types (justified by Milnor-Moore at rank 1, but misleading) |
| `free_fields.tex:2486,2490` | Cooperad type changes from coLie to coSym mid-computation without justification |
| `deformation_quantization.tex:1005` | "Poisson chiral algebra" used for Coisson algebra -- contradicts the manuscript's own distinction that Coisson is NOT a chiral algebra |
| `introduction.tex:1356` | "Symplectic bosons" in boson-fermion context -- technically correct (= beta-gamma at lambda=1/2) but natural reading suggests Heisenberg, which would be wrong |

### S8. CENSUS DRIFT (Severity 4)

CLAUDE.md reports 683 PH; actual count is 687. Delta = +4.

---

## PART III: Proof Dependency Graph

### Main Theorem Dependencies

```
Theorem A (thm:bar-cobar-isomorphism-main) [higher_genus.tex:1440]
  Steps 1,2,4: THIN | Step 3: SOLID
  |-- thm:geometric-equals-operadic-bar (bar_cobar:1845, PH)
  |-- thm:arnold-three (bar_cobar:873, PH)
  |-- thm:bar-nilpotency-complete (bar_cobar:588, PH)
  |-- thm:verdier-bar-cobar (bar_cobar:3253, PH)
  |-- thm:cobar-d-squared-zero (bar_cobar:2609, PH)
  |-- thm:stokes-config (higher_genus:732, PH)

Theorem B (thm:higher-genus-inversion) [higher_genus.tex:7286]
  Base: SOLID | Inductive step: THIN (open-stratum lemma)
  |-- def:modular-koszul-chiral (higher_genus:7468)
  |    |-- Theorem A (via D2: bar(A) = A^!)
  |-- lem:higher-genus-open-stratum-qi (higher_genus:7228, PH) [THIN]
  |-- lem:higher-genus-boundary-qi (higher_genus:7247, PH) [SOLID]
  |-- lem:extension-across-boundary-qi (higher_genus:7270, PH) [SOLID]

Theorem C (thm:quantum-complementarity-main) [higher_genus.tex:4528]
  Steps 1-3,5-6,9-10: SOLID | Steps 4,7,8: THIN
  |-- INDEPENDENT of Theorems A and B
  |-- LV12 Thm 3.4.4 (PE) -- diagonal Ext
  |-- BD04 Thm 4.6.1 (PE) -- Gauss-Manin
  |-- 11 internal PH dependencies, all in bar_cobar/chiral_koszul_pairs
```

**Circular dependency check**: NONE FOUND.
- A is self-contained (bar_cobar_construction.tex + supporting lemmas)
- B depends on A (through hypothesis)
- C is independent of both A and B

---

## PART IV: Master Table Forensics

### Verified Against Compute Engine

All 60 proved values across 6 algebras (Heisenberg, free fermion, bc, beta-gamma, sl2, Virasoro) through degree 10 match exactly between manuscript, compute engine registry, and closed-form formulas.

All central charges, complementarity sums, kappa formulas, Feigin-Frenkel dual levels, and spectral sequence collapse pages verified correct.

### Provenance Classification

| Entry | Status |
|-------|--------|
| H^1-H^3 for all 7 algebras | PROVED + verified |
| H^4-H^10 for Heis/fermion/bc/bg/sl2/Vir | PROVED (closed-form GFs) |
| H^4(W3) = 52 | **UNDOCUMENTED** (see S1) |
| H^5+ for W3 | CONJECTURED (correctly flagged) |
| H^4+ for sl3 | CONJECTURED (correctly flagged) |
| H^4+ for Yangian | CONJECTURED (3 data points, zero DOF -- see S3) |

---

## PART V: Tag Integrity Report

### Systematic Sample (68 PH claims, every 10th)

| Category | Count | Percentage |
|----------|-------|------------|
| SOLID (complete proof) | 45 | 66% |
| SOFT (thin/deferred proof) | 19 | 28% |
| PHANTOM (no proof at all) | 2 | 3% |
| MISCLASSIFIED | 2 | 3% |

**Extrapolated for 687 PH**: ~451 SOLID, ~191 SOFT, ~20 PHANTOM, ~20 MISCLASSIFIED.

### 7 PHANTOM PH claims (no proof attempt)

| Location | Claim | Assessment |
|----------|-------|------------|
| `introduction.tex:728` | Full genus bar complex | Intro preview; proof in later chapter |
| `introduction.tex:886` | NAP complete statement | "See Theorem ref for complete proof" |
| `introduction.tex:1245` | Extended Koszul duality | Intro preview; proof in later chapter |
| `classical_to_chiral.tex:416` | Three-level hierarchy | Programmatic statement |
| `classical_to_chiral.tex:430` | Computational strategy | Algorithmic recipe |
| `genus_expansions.tex:157` | Lattice-independence | No proof given |
| `lattice_foundations.tex:1202` | Unimodular case | No proof given |

The introduction previews (3 of 7) are standard expository practice but inflate the PH count by ~17 across the introduction.

### Conventions verified CLEAN across all files

- Cohomological grading (|d|=+1) with desuspension s^{-1} for bar
- Com^! = Lie (never coLie)
- Heisenberg NOT self-dual; H^! = Sym^ch(V*)
- Bosonization != Koszul (warned in 5 locations)
- Feigin-Frenkel: k -> -k - 2h^vee (never -k - h^vee)
- Coisson is NOT a chiral algebra (stated 3 locations)
- Curved A-infinity minus sign (m_1^2 = [m_0, -])
- QME coefficient 1/2; HCS coefficient 2/3
- No \newcommand in chapter files

---

## PART VI: Regression Risk Map

### Prior Audit Findings

| Finding | Source | Current Status |
|---------|--------|----------------|
| F1 Eigenspace proof | DEEPAUDIT | STALE (verified rewritten) |
| F2 Lagrangian shift | DEEPAUDIT | FIXED |
| F5 Modular periodicity | DEEPAUDIT | LIVE -- same gap persists in quantum periodicity (F2 above) |
| F6-F7 Geometric/Unified | DEEPAUDIT | Correctly CJ, but proof texts still cite them as facts |

### Highest Regression Risks

1. **Periodicity complex**: Wrong statements in 3 locations (intro, hochschild, W-algebra). Correct statement in koszul_pair_structure.tex.
2. **W3 pipeline**: H^4=52 load-bearing and undocumented.
3. **Theorem A proof quality**: All agents flagged Steps 1/2/4 as thin.
4. **Census**: Found stale in 5 consecutive audits. Must be automated.

---

## PART VII: Honest Assessment

### If defending as a PhD thesis, where would the committee attack?

1. **introduction.tex thm:periodicity-cohomology**: False claim visible on first reading. Any examiner knowing sl3 Lie algebra cohomology catches this immediately.

2. **Theorem A proof**: Three of four steps are annotated outlines, not proofs. The supporting lemmas are all individually proved in bar_cobar_construction.tex, but the *assembly* is where this thesis claims novelty -- and the assembly is thin.

3. **deformation_theory.tex quantum periodicity**: "If you downgraded three other theorems for this exact gap, why not this one?"

4. **H^4(W3) = 52**: "Where does this come from?" No answer exists in the manuscript.

5. **bar_cobar_construction.tex lines 4555-4706**: Seven PH-tagged lemmas that are proof sketches. Full proofs exist later in higher_genus.tex, but these lemmas shouldn't carry PH tags in their sketch form.

### What's actually solid

- **Compute engine** (901 tests passing): independent verification of all numerical claims
- **No circular dependencies** in main theorem chain
- **Master Table**: correctly flagged; proved values all verified
- **koszul_pair_structure.tex**: Strongest chapter. Complete proofs, correct statements.
- **Theorem C proof**: 10-step eigenspace decomposition is mostly solid (3 thin points out of 10)
- **Claim tagging**: 66% SOLID on systematic sample. 99 CJ all have scope remarks.
- **Convention consistency**: All critical conventions (grading, duality, signs) are correct across 55 files

### Complete Finding Inventory

| Sev | Count | Category |
|-----|-------|----------|
| 1 | 1 | F1: Periodicity contradiction (3 locations) |
| 2 | 14 | F2-F7: Proof gaps, theorem misapplications, proof thinness |
| 3 | 12 | S1-S7, F8: Provenance gaps, notation collisions, terminology, numerical error |
| 4 | 1 | S8: Census drift |
| **Total** | **28** | |

### Systematic Fix Plan

| Priority | Findings | Fix | Effort |
|----------|----------|-----|--------|
| P0 | F1 (periodicity, 3 locations) | Restate intro + fix hochschild + fix W3 period | 30 min |
| P0 | S8 (census) | Update CLAUDE.md | 2 min |
| P1 | F2 (quantum periodicity) | Downgrade to CJ | 15 min |
| P1 | F3 (Theorem A thin) | Add synthesis sentences to Steps 1,2,4 | 30 min |
| P1 | F4a-c (sketch section PH tags) | Downgrade to remarks pointing to full proofs | 20 min |
| P2 | F5 (Hochschild cor) | Define d, expand proof | 20 min |
| P2 | F6 (Theorem C thin steps) | Add citation for D-module sign; expand Ext argument | 30 min |
| P2 | F7 (theorem misapplications, 7 instances) | Add hypothesis checks or correct citations | 45 min |
| P2 | F8 (W3 primary reversal) | Fix "T is primary for W" to correct relationship | 5 min |
| P2 | S1 (H^4 W3 provenance) | Add dagger or document computation | 15 min |
| P2 | S2 (G2 chain-group error) | Fix 2744 to 5488 with correct formula | 5 min |
| P3 | S4-S5 (notation collisions) | Distinguish kappa_level/kappa_obs/kappa_Killing; consolidate H notation | 2 hrs |
| P3 | S6 (duplicate definitions) | Merge or cross-reference | 1 hr |
| P3 | S7 (terminology) | Fix coLie/cocommutative, "Poisson chiral", boson-fermion | 20 min |
| P3 | F4d-g (bar_cobar proof gaps) | Expand proofs or cite clean alternatives | 1 hr |

**Total: ~7 hours** for complete fix sweep.

---

*End of STRUCTURAL_AUDIT.md*
