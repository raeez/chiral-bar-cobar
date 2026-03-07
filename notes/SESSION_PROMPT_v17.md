# SESSION PROMPT v17 — FUTURES GAP CLOSURE

## Identity
You are the research collaborator specified in CLAUDE.md (triple-intersection: Serre/Grothendieck + Witten/Costello + Polyakov/Dirac). Read CLAUDE.md fully before proceeding.

## Mission
The proof architecture is sound (v15 resculpting complete, v16 dissemination complete). The four main theorems are proved. What remains is **expository honesty** (the manuscript must not overclaim) and **T2 theorem upgrades** (conjectures closable with existing machinery). This session executes Phase A (all 7 T1 items) and begins Phase B (prioritized T2 items).

The 9 advertised futures of the monograph (raeeznotes4.md) were analyzed against the actual proved core, yielding 46 specific gaps in three tiers:
- **T1 (7 items)**: Expository — text claims more than proofs deliver
- **T2 (8 items)**: Theorematic — closable with existing machinery + focused argument
- **T3 (31 items)**: Programme — correctly conjectural, require new mathematics or physics

## Pre-flight
```bash
# 1. Read CLAUDE.md, MEMORY.md
# 2. Fresh census
grep -rc 'ClaimStatusProvedHere\|ClaimStatusConjectured\|ClaimStatusProvedElsewhere\|ClaimStatusHeuristic' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "Total claims:",s}'
# 3. Verify v15 resculpting is stable
grep -n 'def:chiral-koszul-pair\|def:modular-koszul-chiral' chapters/ -r --include='*.tex' | head -4
# 4. Verify v16 dissemination complete (differential macros propagated)
grep -rc '\\dfib\|\\Dg\|\\dzero\|\\mcurv' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "Notation macro uses:",s}'
```

---

## PHASE A: EXPOSITORY HONESTY — 7 items, zero new mathematics

All items are independent grep-read-edit cycles. Execute as parallel batch.

### A1: Residual H^1(M_g) language [Future 1]

The manuscript was corrected (session ~145) to source genus parameters from H^1(Sigma_g), not H^1(M_g) (which vanishes for g>=2 by Harer). Verify no residual old language survives.

```bash
grep -rn 'H\^1.*M_g\|H\^{1}.*M_g\|H\^1(\\mathcal{M}\|H\^{1}(\\mathcal{M}\|H\^1(\\overline{\\mathcal\|parameters.*from.*H.*moduli' chapters/theory/introduction.tex chapters/connections/concordance.tex main.tex
```

**Decision rule**: If a hit says "H^1(M_g) controls/parameterizes genus corrections" → fix to reference H^1(Sigma_g) or the three-level diagram. If it correctly says "H^1(M_g) = 0 for g >= 2" as a negative fact → leave it.

### A2: Concordance status table vs actual theorem labels [Future 2]

The concordance chapter has a status table for A_mod through DK. After v15 resculpting, verify every entry matches the actual theorem's ClaimStatus tag.

```bash
grep -n 'A_.*mod\|B_.*mod\|C_.*mod\|\\mathrm{Index}\|\\mathrm{DK}' chapters/connections/concordance.tex | head -20
```

**Required matches**:
| Programme | Theorem label | Required status language |
|-----------|---------------|------------------------|
| A_mod | thm:bar-cobar-isomorphism-main | "proved" |
| B_mod | thm:higher-genus-inversion | "proved on the Koszul locus; coderived persistence off Koszul locus is conjectural" |
| C_mod | thm:quantum-complementarity-main + thm:shifted-symplectic-complementarity | "proved" |
| Index | thm:family-index | "proved" |
| DK | thm:factorization-dk-eval | "proved on the evaluation locus; full factorization-categorical equivalence is conjectural" |

Fix any entry that is missing the Koszul-locus or evaluation-locus qualifier.

### A3: Periodicity framing [Future 7]

The manuscript should not frame "unified periodicity" as established or imminent. The honest state is: partial, family-dependent periodicity profiles.

```bash
grep -rn 'unified periodicity\|periodicity.*classif\|periodicity.*doctrine\|periodicity.*universal\|complete.*periodicity' chapters/ appendices/ --include='*.tex'
```

For each hit: if the language implies a universal periodicity classification exists, add qualifier: "proved for minimal models and WZW; conjectural for general rational CFT." Check `deformation_theory.tex`, `concordance.tex`, `koszul_pair_structure.tex` in particular.

### A4: Theta_A framing [Future 4]

After v15 Strike 6, Theorem D is scalar-only. Verify introduction.tex and concordance.tex don't over-promise the non-scalar Theta_A.

```bash
grep -rn 'Theta_A\|\\Theta.*universal\|modular.*characteristic.*package\|non-scalar.*complet\|universal.*Maurer' chapters/theory/introduction.tex chapters/connections/concordance.tex
```

Every reference to Theta_A should say "programme target" or "conjectural." If any sentence implies Theta_A is established, add "conjectural."

### A5: A_mod functorial vs operadic [Future 3]

A_mod is proved functorially (families over M_{g,n}). Whether it lifts to a modular operad equivalence is unstated.

```bash
grep -n 'A_.*mod\|operadic.*equiv\|modular.*operad.*equiv' chapters/connections/concordance.tex
```

If the A_mod entry doesn't distinguish functorial (proved) from operadic (unstated), add one sentence: "The present proof establishes functorial compatibility of bar and cobar over $\overline{\mathcal{M}}_{g,n}$; whether this lifts to an equivalence of modular operads is a further question."

### A6: Index theorem as proved [Future 5]

thm:family-index and the A-hat-genus identity are proved. Introduction should use assertive language, not aspirational.

```bash
grep -n 'family.*index\|GRR\|Grothendieck.*Riemann.*Roch\|\\hat{A}\|A-hat\|genus.*series' chapters/theory/introduction.tex
```

Replace any "we expect," "should equal," "anticipated" with "equals," "is determined by," "we prove."

### A7: Stratum I/II in introduction [Future 3]

Verify introduction.tex correctly frames the proved core as the foundation of the modular homotopy theory, not the theory itself.

```bash
grep -n 'Stratum\|stratum\|proved.*core\|foundation.*modular\|modular.*homotopy.*theory' chapters/theory/introduction.tex
```

If introduction.tex conflates the proved theorems with the full modular homotopy theory, add a qualifying sentence.

### PHASE A GATE
```bash
pkill -9 -f pdflatex; sleep 16; make fast  # zero new errors
# Census should be UNCHANGED
grep -rc 'ClaimStatusProvedHere\|ClaimStatusConjectured' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "PH+CJ:",s}'
```

---

## PHASE B: THEOREM UPGRADES — ordered by feasibility and impact

Execute sequentially. Read all relevant proofs before writing. Only upgrade with COMPLETE proofs.

### B1: Modular periodicity for WZW [Priority: HIGHEST]

**Location**: `conj:modular-periodicity` in `koszul_pair_structure.tex`

**What exists**: `thm:modular-periodicity-minimal` proved for minimal models via theta/eta character structure.

**Why WZW should work**: WZW characters are also theta/eta ratios. For sl_2 at level k, chi_j(q) = (Theta_{2j+1,k+2}(q) - Theta_{-(2j+1),k+2}(q)) / eta(q). The theta functions Theta_{m,N} have periodicity N under the relevant modular transformation. The eta function has period 24. So bar-cohomology periodicity at WZW level should be lcm(N, 24) where N depends on level and rank.

**Action**:
1. Read `thm:modular-periodicity-minimal` and its complete proof
2. Read WZW character formulas in `kac_moody_framework.tex`
3. If the minimal-model proof technique (finite Fourier analysis on theta/eta) extends to WZW characters, write `thm:modular-periodicity-wzw`
4. If it extends, narrow `conj:modular-periodicity` to "non-WZW rational CFT only"

**CRITICAL**: Do NOT write a proof sketch. Either prove it completely or leave the conjecture as is.

### B2: Sharp geometric periodicity bound [Priority: HIGH]

**Location**: `conj:geometric-periodicity` in `koszul_pair_structure.tex`

**What exists**: `thm:geometric-periodicity-weak` with bound |(3g-2).

**Approach**: Mumford relation 12*lambda = kappa_1 + delta in Pic(M-bar_g) tensor Q. Since obs_g = kappa * lambda_g, if 12*lambda_g = kappa_1 + delta (tautological), then the obstruction class has a natural period dividing 12(2g-2) = deg(kappa_1).

**Action**:
1. Read `thm:geometric-periodicity-weak` and its proof
2. Read any appendix material on tautological classes of M-bar_g
3. If Mumford's relation directly yields the sharp bound, prove `thm:geometric-periodicity-sharp`
4. If additional intersection theory is needed beyond the manuscript's scope, add a scope remark to the conjecture

### B3: AGT scope narrowing [Priority: MEDIUM]

**Location**: `conj:agt-bar-cobar` in `holomorphic_topological.tex`

The 2D side (W-algebra bar = semi-infinite) is proved via `thm:bar-semi-infinite-w`. The 4D-2D bridge is AGT itself. Narrow the conjecture accordingly.

**Action**:
1. Read `conj:agt-bar-cobar` and full context
2. Split: (a) 2D side → reference thm:bar-semi-infinite-w (already PH), (b) 4D-2D bridge → remains CJ with scope remark citing Schiffmann-Vasserot
3. This is a T1-grade edit disguised as T2 — it narrows scope rather than proving new content

### B4: Higher-genus anomaly [Priority: MEDIUM]

**Location**: `conj:anomaly-physical` in `concordance.tex`

**What exists**: `thm:anomaly-physical-km-w` (genus-0 anomaly duality). Theorem D proves obs_g = kappa * lambda_g for all g.

**Key question**: Does `conj:anomaly-physical` at higher genus follow from Theorem D's universality clause? If obs_g = kappa * lambda_g and kappa + kappa' = 0, then obs_g(A) + obs_g(A!) = 0 for all g — which IS the anomaly cancellation at higher genus. Check if this is what the conjecture claims or if it requires something stronger (e.g., Costello-style renormalization).

**Action**:
1. Read `conj:anomaly-physical` — exact statement
2. If it's equivalent to "obs_g(A) + obs_g(A!) = 0 for all g," this is ALREADY PROVED by Theorem D clauses (iii) + (i). Upgrade to theorem, citing thm:modular-characteristic.
3. If it requires more (BV formalism, path integral), leave as CJ with scope remark noting the scalar anomaly cancellation is proved

### B5-B7: Deferred items

**B5** (KS operator on H^1_red), **B6** (sl_3 discriminant — BLOCKED by d^2 != 0), **B7** (Yangian cat O Koszulness): Only attempt if B1-B4 are complete and time remains. These require substantial new mathematics.

### PHASE B GATE
After each upgrade:
```bash
pkill -9 -f pdflatex; sleep 16; make fast
```

---

## PHASE C: T3 VERIFICATION — quick sweep

The 31 T3 gaps are correctly conjectural. Verify:

```bash
# Spot-check scope remarks on key T3 conjectures
for label in conj:coderived-ran conj:universal-MC conj:full-derived-dk conj:reflected-modular-periodicity conj:periodic-cdg conj:nc-cs conj:holographic-bar-cobar conj:bar-cobar-path-integral conj:CL-produces-chiral conj:factorization-dimension-tower; do
  echo "=== $label ==="
  grep -A3 "label{$label}" chapters/ appendices/ -r --include='*.tex' | head -6
done
```

For any T3 conjecture missing a scope remark, add 1-2 sentences: what it would take to upgrade (which missing piece of mathematics/physics).

Verify none are accidentally tagged ProvedHere:
```bash
grep -B5 'ClaimStatusProvedHere' chapters/ appendices/ -r --include='*.tex' | grep -i 'conjecture\|conjectural'
```

---

## Protocol

### Execution order
```
Pre-flight checks
  |
Phase A: A1-A7 (parallel batch, all independent)
  | compile gate
Phase B: B1 -> B2 -> B3 -> B4 -> (B5-B7 if time)
  | compile gate after each
Phase C: T3 verification sweep
  | final compile + full census
```

### Per-item discipline
1. **Grep before read.** Never guess line numbers.
2. **Read before write.** Always read +-30 lines of context.
3. **Minimum viable edit.** Change only what needs changing. No prose expansion.
4. **Phase A = text only.** No new theorems, no changed ClaimStatus tags.
5. **Phase B = complete proofs only.** A half-proof is worse than a conjecture.

### What you must NOT do
1. Do NOT change existing theorem statements (except narrowing conjecture scope).
2. Do NOT change proofs of existing theorems.
3. Do NOT change ClaimStatus tags in Phase A.
4. Do NOT create new .tex files.
5. Do NOT touch main.tex preamble or heisenberg_frame.tex.
6. Do NOT attempt sl_3 bar computation via direct matrix. d^2 != 0 is proved.
7. Do NOT add motivational paragraphs or expand prose.
8. Do NOT change bibliography unless a Phase B theorem needs a new citation.

### Session end
```bash
pkill -9 -f pdflatex; sleep 16; make   # full build
grep -rc 'ClaimStatusProvedHere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "PH:",s}'
grep -rc 'ClaimStatusConjectured' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "CJ:",s}'
grep -rc 'ClaimStatusProvedElsewhere' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "PE:",s}'
grep -rc 'ClaimStatusHeuristic' chapters/ appendices/ --include='*.tex' | awk -F: '{s+=$2}END{print "HE:",s}'
```
Update CLAUDE.md and MEMORY.md with any changes.

## Begin

Start with Phase A. Execute A1-A7 as parallel grep-read-edit cycles. Then compile gate. Then Phase B starting with B1.
