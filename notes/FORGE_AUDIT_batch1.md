# FORGE AUDIT — Batch 1: Theory Core
# Date: 2026-03-14
# Files: introduction.tex, algebraic_foundations.tex, bar_cobar_construction.tex, configuration_spaces.tex
# Total lines audited: ~20,773

---

## CRITICAL FINDINGS (fix immediately)

### C1: Partition lattice suspension exponent inconsistency
**Files**: algebraic_foundations.tex:541,553 vs poincare_duality_quantum.tex:1083
**Issue**: algebraic_foundations.tex claims B(Com)(n) ~ s^{n-1} with homology in degree n-3.
poincare_duality_quantum.tex claims B(Com)(n) ~ s^{n-2} with homology in degree n-2.
These are mutually contradictory. The order complex of Pi_n has dimension n-3 (chains of length n-3), so the algebraic_foundations version (degree n-3) is consistent with Bjorner-Wachs.
**Action**: Verify against LV12 Theorem 7.4.6. Fix whichever file is wrong.

### C2: [1] shift notation wrong for arity-dependent operadic suspension
**File**: algebraic_foundations.tex:557,562
**Issue**: B(Com) ~ coLie[1] uses uniform [1] shift, but the actual shift is s^{n-1} in arity n (operadic suspension, not uniform). Standard: B(Com) ~ s*coLie (LV12 7.2.4).
**Action**: Replace [1] with correct operadic suspension notation.

### C3: Wrong notation in Poincare polynomial (open vs compactified)
**File**: configuration_spaces.tex:1280
**Issue**: Uses \barC_n(C) (= FM compactification) but the Poincare polynomial prod(1+it) is for the OPEN config space C_n(C). The compactification has different cohomology.
**Action**: Change \barC to C (or equivalent macro for open config space).

### C4: dfib^2=0 claim contradicts core convention
**File**: bar_cobar_construction.tex:11385-11389
**Issue**: Claims "dfib^2 = 0 strictly iff mu_0 in Z(A)" and "all standard chiral algebras have dfib^2=0 strictly." This contradicts CLAUDE.md: dfib^2 = kappa * omega_g != 0 for kappa != 0. The intended meaning is likely that m_1^2 = [mu_0, -] acts as a scalar (central curvature), not that dfib^2 vanishes.
**Action**: Rewrite to distinguish "curvature is central" from "curvature vanishes."

---

## MODERATE FINDINGS (fix in batch)

### M1: d^2=0 without genus-0 qualifier
**File**: introduction.tex:168-169
**Issue**: "Arnold relation makes d^2=0" but d_bracket^2 != 0 in general (proved, CLAUDE.md). Should use d_0 or add "at genus 0."

### M2: Bar-cohomology = Koszul-dual without Koszulness qualifier
**File**: introduction.tex:176-177
**Issue**: "H*(B(A)) = A^!" stated unconditionally. Only true when A is Koszul.

### M3: Genus-g propagator formula is schematic
**File**: introduction.tex:194-197
**Issue**: A-cycle integral form differs from the precise Im(Omega)^{-1} formula in higher_genus.tex.

### M4: Two \chapter commands in one file
**File**: algebraic_foundations.tex:265
**Issue**: Second \chapter has no label. Consider splitting file or merging chapters.

### M5: Empty section
**File**: algebraic_foundations.tex:507
**Issue**: "Com-Lie Koszul duality from first principles" has no content.

### M6: Factorization "verification" proves nothing
**File**: algebraic_foundations.tex:649-667
**Issue**: C^inf fails the axiom it claims to verify.

### M7: Conflicting normal bundle formulas
**File**: configuration_spaces.tex:3059 vs 3106
**Issue**: O(-1) tensor L_S vs O(-1). The proof at 3106 shows O(-1) is correct.

### M8: Confused fibration direction in proof sketch
**File**: configuration_spaces.tex:1555-1581
**Issue**: Arrow between C_n(Sigma_g) and M_{g,n} is reversed.

### M9: Bar complex defined 3-5 times
**File**: bar_cobar_construction.tex:257/337/1443/1468/1504
**Issue**: Same object with varying notation (d_residue / d_fact / d_res). ~300 lines of near-duplicate.

### M10: Session amalgamation — duplicate MC/nilpotence material
**File**: bar_cobar_construction.tex:11316-12800
**Issue**: 3 MC definitions, 3 classification tables, 3 completion-criteria discussions. ~800-1000 lines compressible.

### M11: Orphaned label conv:proof-architecture
**File**: introduction.tex:1031
**Issue**: Referenced 4 times in other files but label is between environments, not inside one.

---

## MINOR FINDINGS (defer or skip)

- introduction.tex: Dead labels (437-438, 1078-1082), label placements, P-infinity title ambiguity
- algebraic_foundations.tex: Dead labels (122-123), label misprefixes (16), duplicate Weiss remarks (690/887), duplicate Koszul pair definitions (68/367), missing KS citation (460)
- configuration_spaces.tex: NBC basis defined twice (1299/1793), Ran space defined three times (927/1359/3496), ~700 lines compressible coordinate examples, elliptic Arnold attribution
- bar_cobar_construction.tex: Forward/backward ref error (2568), double/triple labels (3086/3576/5218/5333), Unicode char (5280), PATCH markers (11377/12214), orientation bundle defined twice (391/1056), functoriality proved twice (688/1092), cobar d^2=0 proved twice (2269/2460)

---

## CROSS-FILE PATTERNS

1. **Session amalgamation**: bar_cobar_construction.tex (lines 11316-12800) and algebraic_foundations.tex (two \chapter commands) show clear signs of incremental session appending without consolidation.
2. **Dead labels**: Across all files, unreferenced labels from prior rewrite sessions accumulate.
3. **Multiple definitions of same object**: Bar complex (3-5x), Ran space (3x in config_spaces), NBC basis (2x), orientation bundle (2x), MC elements (3x), cobar (2x).
4. **Factorization verification**: Both algebraic_foundations and bar_cobar have C^inf "verifications" that fail.

---

## POSITIVE HIGHLIGHTS

- bar_cobar_construction.tex:1-93 (nilpotence-periodicity): EXEMPLARY
- bar_cobar_construction.tex:622-686 (prop:pole-decomposition): EXEMPLARY — d_bracket^2 != 0 mechanism
- bar_cobar_construction.tex:5385-5655 (MC4 reduction): Clean logical architecture
- bar_cobar_construction.tex:9000-10700 (stage-5 visible-pairing): Correct, well-proved
- bar_cobar_construction.tex:14579-15078 (categorical logarithm): Cohesive, well-written
- introduction.tex:415-620 (logarithmic seed + four theorems): EXEMPLARY
- All CLAUDE.md conventions verified correct in:
  - Feigin-Frenkel shift k<->-k-2h^vee
  - Curved A-infinity sign m_1^2 = [m_0, a]
  - Lambda = :TT: - (3/10)d^2T (MINUS)
  - FM = blowup
  - Normal bundle = tangent
  - Prime form K^{-1/2}

---

## LINE COUNT BEFORE FIXES
- introduction.tex: 1098
- algebraic_foundations.tex: 940
- bar_cobar_construction.tex: 15078
- configuration_spaces.tex: 3657
- **TOTAL: 20,773**
