# Arithmetic Chapter Rewrite Plan

**Target**: `chapters/connections/arithmetic_shadows.tex` (10,020 lines)
**Date**: 2026-04-04
**Standard**: Chriss-Ginzburg. Every object earns its place. Every paragraph forces the next.

---

## 0. Executive Summary

The chapter is the strongest "connections" chapter in Vol I: it contains genuine mathematics (shadow-spectral correspondence, depth decomposition, Hecke-Newton closure for lattice VOAs, non-lattice Ramanujan bound via Franc-Mason), extensive honest assessments of what is proved vs open vs structurally impossible, and a well-organized programme with four named gaps. The 44-agent swarm found no load-bearing mathematical errors. The primary problems are:

1. **Niemeier discrimination blindness** (major omission): the scalar shadow obstruction tower gives kappa=24 for ALL 24 Niemeier lattices. The chapter never addresses this. The charged-sector resolution and multi-channel bar complex are absent.
2. **AP42 overclaims** (5 sites): "completing the reduction," "implements Serre's programme," "universal invariant" applied to a projection, unflagged circularity at g>=6, SK-lift conflation for Leech.
3. **Scope inflation** (3 sites): "completing the reduction" for a narrowing, CPS hypotheses presented as unconditional when caveat is in the proof, introductory claim about shadow obstruction tower as "universal invariant."
4. **Missing swarm findings**: the depth decomposition universality, Ising d_arith paradox resolution, non-perturbative Borel-arithmetic falsification, p-adic convergence, V-natural as class M, and the arithmetic comparison conjecture sharpening are all absent.
5. **Section ordering**: the chapter front-loads lattice results (correct) but then mixes the quartic residue programme, structural diagnosis, geometric positivity, modular rigidity, operadic transfer, and Hecke-Newton closure in a non-monotone dependency order.

The rewrite should be surgical: the mathematical content is sound. The work is reordering, adding missing findings, correcting overclaims, and adding the Niemeier charged-sector story.

---

## 1. Section-by-Section Assessment

### Introduction (lines 1-97)

**Correct**: Depth decomposition statement, epistemic scope paragraph, structural obstruction.
**Overclaimed (AP42)**: Line 33-36: "the shadow obstruction tower is the universal invariant that encodes both the Langlands programme (arithmetic) and the Sullivan programme (homotopy theory) in the single Maurer-Cartan element Theta_A." This conflates the PROJECTION of Theta_A onto each arity with the FULL MC element. The shadow obstruction tower is a sequence of projections; it does not encode the Langlands programme. The Langlands programme enters only through the Hecke decomposition of theta functions for LATTICE VOAs, not through Theta_A directly.
**Fix**: Replace "the shadow obstruction tower is the universal invariant that encodes both" with "the shadow obstruction tower organizes the algebraic data that, for lattice vertex algebras, connects to both."
**Missing**: No mention of the Niemeier discrimination problem (ALL 24 lattices have kappa=24, completely blind).

### Section: The sewing-Rankin-Selberg bridge (lines 162-327)

**Correct**: Eight-step chain, sewing operator, divisor-sum decomposition, sewing-Selberg formula, structural obstruction remark.
**Sound**: The sewing-Selberg formula (Thm 277) is proved. The structural obstruction (Rem 300) is honest.
**No changes needed** except minor: the eight-step chain at lines 166-196 could note that Steps 5-8 apply ONLY to lattice VOAs.

### Section: Four identities (lines 329-463)

**Correct**: Narain, E8, Z^2, Leech. All proved.
**Minor**: The Leech proposition (line 430) says "Assuming GRH, the zeros lie on three critical lines." This is honest. No fix needed.
**Missing**: No discussion of what happens for the OTHER 23 Niemeier lattices beyond Leech. The five lattice verifications table (line 466) includes V_Z, V_{Z^2}, V_{A_2}, V_{E_8}, V_Leech but not D_16^+ + D_16^+ or E_8^3 (which appear later at line 830). The Niemeier atlas should be referenced.

### Section: Five lattice verifications (lines 466-491)

**Correct**: Table matches the theorems.
**Enhancement**: Add a remark noting that the table covers only 5 of 24 Niemeier lattices, and ALL 24 have depth 4 (same kappa=24, same dim S_12 = 1). The SCALAR shadow obstruction tower is completely blind to root system. Reference the charged-sector resolution (new section).

### Section: Proof of the shadow-spectral correspondence (lines 493-601)

**Correct**: The proof is sound. The arithmetic sieve table (lines 537-551) correctly identifies arity-r with the r-3'th cusp eigenform.
**No changes needed**.

### Section: The period-shadow dictionary (lines 643-944)

**Correct**: Period-shadow dictionary, five worked examples, spectral decomposition principle, depth formula.
**Enhancement**: The D_16^+ + D_16^+ vs E_8^3 computation (line 830) should be expanded to explain WHY they have the same depth but different coefficients. This is the first hint of the Niemeier discrimination problem: different root systems produce different cuspidal weights c_Delta, but the scalar shadow (kappa=24) cannot see this.

### Section: The cusp-singularity theorem (lines 947-1154)

**Correct**: Growth rates, self-referentiality criterion, shadow obstruction tower asymptotics, effective coupling.
**Minor issue**: The general finiteness conjecture (line 1055) statement is fine. The "controlled, Tier 2" in prop 1005 line 1013 states finiteness for "lattice-VOA and rank-one betagamma families" which is correct and appropriately scoped.
**No changes needed**.

### Section: Non-lattice theories (lines 1156-1235)

**Correct**: betagamma primary-counting, refined shadow-spectral correspondence, Virasoro alpha values, Ising d_arith = 0.
**Enhancement**: The Ising d_arith = 0 proposition (line 1208) should add a remark about the ISING PARADOX from the swarm: d_arith=0, d_alg=infinity, yet the Ising model has deep arithmetic structure in its fusion ring and VVMF. The depth decomposition captures only the Roelcke-Selberg spectral content; the fusion ring arithmetic is invisible to it.

### Section: Higher depths via higher-rank lattices (lines 1237-1318)

**Correct**: Depth formula, table, arithmetic depth filtration.
**Enhancement**: Add the swarm finding that the first d_arith > 3 occurs at rank 48, and that M(7,8) has d_arith = 7. Add the genus-dependent arithmetic depth d_arith^{(g)} as a new definition (from swarm).

### Section: The depth decomposition (lines 1321-1473)

**Correct**: The theorem and proof are sound. d_alg in {0,1,2,infinity} from single-line dichotomy.
**Enhancement**: Add the swarm finding that the depth decomposition is UNIVERSAL (applies to all modular Koszul algebras, not just lattices). This should be stated as a remark.
**Enhancement**: Add the complete table from the swarm: G(d_alg=0), L(d_alg=1), C(d_alg=2), M(d_alg=infinity). Currently implicit but not tabulated.

### Section: Interacting Gram positivity (lines 1476-1562)

**Correct**: Interacting sewing weight, negative/positive atom cases, Virasoro corollary.
**No changes needed**.

### Section: Stieltjes representation (lines 1565-1676)

**Correct**: Shadow spectral measure, Carleman rigidity, two spectral measures.
**RECTIFICATION-FLAG at line 1593**: Already present and honest. Keep.
**No changes needed**.

### Section: The period filtration (lines 1679-1817)

**Correct**: Shadow periods, motivic decomposition, Kummer motive, transcendence asymmetry, MC motivic identity, Euler-Koszul motivic weight.
**No changes needed**.

### Section: The spectral curve and sewing-shadow intertwining (lines 1820-2279)

**Correct**: Algebraic shadow generating function, Eisenstein moment minor, shadow Epstein zeta, shadow Higgs field, general shadow triple, shadow BPS spectrum.
**RECTIFICATION-FLAG at line 2171**: Already present and honest. Keep.
**Minor**: The BPS central charge formula (line 2194) Z^2 = 80c^2/(45c+218) -- verify independently. The denominator 45c+218 should be checked against the spectral curve data alpha = (180c+872)/(5c+22). We have 45c+218 = 45c+218, while (180c+872)/4 = 45c+218. Consistent.

### Section: Sewing-shadow intertwining (lines 2281-2596)

**Correct**: The intertwining theorem, shadow Fredholm determinant, Heisenberg verification, spectral measure identification, shadow-moduli resolution, universality of G.
**Sound**: All proved claims are correctly scoped.

### Section: MC recursion in spectral coordinates (lines 2598-2697)

**Correct**: Newton from MC is correct (tautological for 2 variables as swarm confirms).
**Enhancement**: Add the swarm's clarification that this is EXACTLY Newton (a tautology for 2 variables), not a new result. The four-station table (line 2667) correctly identifies the open step.

### Section: Shadow metric to Dirichlet L-functions (lines 2700-2906)

**Correct**: Shadow L-function construction, shadow principal class conjecture, Koszul-Epstein function, three structural constraints.
**No changes needed**.

### Section: The Hecke module structure (lines 3063-3138)

**Correct**: Hecke-equivariant MC element for lattice VOAs.
**No changes needed**.

### Section: The quartic residue programme (lines 3141-4619)

**Correct**: Mixed (s,u)-transform, 3x3 moment determinant, Virasoro calculation, genuine residue kernel, compatibility ratios, four structural gaps, W_N multi-channel, Miura defect, residue clutching defect, Beilinson functional, honest laboratories, synthesis.
**Four gaps table (line 3471)**: Correct and honest.
**AP42 violation (line 3683-3694)**: The phrase "completing the reduction" in Rem 3610 about genus-2 Beurling kernel. The swarm flagged this. The correct wording should be "narrowing the gap" since the escalation principle is CONJECTURAL at g>=3.
**Fix**: Line 3694 change "completing the reduction" to "narrowing the gap" and add "(conjectural at g >= 3)."
**Enhancement**: The escalation principle (Rem 3684-3695) has an UNFLAGGED CIRCULARITY at g>=6: genus-g MC contributes L(1/2, Sym^{g-1} f x chi_D), but for g>=6 this requires Langlands functoriality GL(2)->GL(g), which is open. The Newton-Thorne break of this circularity for holomorphic forms should be noted.

### Section: The structural diagnosis (lines 4623-4795)

**Correct**: Modularity constraint, bracket positivity, Hodge index, modular spectral rigidity conjecture, Weil analogy.
**Enhancement**: Rem 5033 (positivity does not force Ramanujan) is exemplary honesty. Keep.
**AP42 violation**: The non-commutative Weil conjecture (line 4744) states "D_A^2 = 0 is the analogue of Frob^2 = q." This is acknowledged as structural analogy in Rem 4786: "D_A^2 = 0 is a tautological property of any differential, while Frob^2 = q encodes arithmetic not visible to D_A." The analogy table is honest. No fix needed -- the disclaimer at 4786-4791 is adequate.

### Section: The geometric positivity programme (lines 4958-5062)

**Correct**: Shadow bracket form, Petersson identification, positivity limitation.
**Exemplary**: Rem 5033 is a model of honest scope reporting.
**No changes needed**.

### Section: The modular rigidity programme (lines 5065-5301)

**Correct**: Modularity constraint on atoms, rigidity defect, rigidity threshold, algebraic-analytic divide.
**Enhancement**: The Route C finite-atoms restriction (Rem 5147) is correctly stated. No fix needed.

### Section: The operadic functorial transfer programme (lines 5304-5755)

**Correct**: CPS hypotheses from MC+HS-sewing, conditional status remark, automorphy corollary, prime-locality conjecture, signed Stieltjes measure, multiplicativity failure for rational CFT, shadow arithmetic trichotomy, operadic RS main form, complete chain.
**Conditional status (line 5361)**: Correctly marked ClaimStatusConditional.
**AP42 violation (line 9412)**: The swarm flagged line 9412 "implements Serre's programme" -- I cannot find this exact phrase but will search for it. If present, should be "encodes algebraic data for."
**Enhancement**: Add the swarm finding that the operadic RS is correctly a CONJECTURE, not a theorem. The gap = Langlands GL(2)->GL(r+1) for r>=5.

### Section: The Hecke-Newton closure (lines 5759-6448)

**Correct**: Chiral graph integrals, Hecke-Newton closure for lattice VOAs (proved), non-lattice extension (proved for rational VOAs), irrational extension (conjectural), complete status table, prime-locality frontier, Route C.
**Enhancement**: The non-lattice Ramanujan bound (Thm 5947) is marked ProvedHere. Verify: the proof uses Observation A (holomorphy), B (character-level RS), C (VVMF Hecke decomposition), D (completion). All four observations are sound for rational VOAs. The scope restriction (Rem 6031) is honest.
**Enhancement**: Route C gap analysis (Rem 9823) is EXCELLENT and should be preserved in full in the rewrite. This is a model of honest mathematical self-assessment.

### Section: The Koszul self-duality principle (lines 6683-6957)

**Correct**: Verdier-Hecke commutation, self-dual factorisation, theta decomposition bridge.
**No changes needed**.

### Section: The complexified modular integral (lines 6958-7665)

**Not read in full above -- need to verify**.
**Assessment**: This section extends the sewing-Hecke framework to complexified spectral parameters. Contains the spectral determinant bridge, complexified RS integral, arithmetic-geometric decomposition, Liouville complexification, and assessment. The assessment subsection should be checked for scope honesty.

### Section: The analytic continuation programme (lines 7667-9084)

**Not read in full above -- need to verify**.
**Assessment**: Contains the scattering coupling factorization, refined structural obstruction, Hecke defect as obstruction class, rigidity inheritance theorem, assessment and open problems, arithmetic packet connection, Miura defect in packet connection. This is the technical heart of the programme.

### Section: The genus-2 arithmetic frontier (lines 9085-9619)

**Correct**: Genus-2 sewing non-diagonality (proved), genus-2 non-collapse (proved), Saito-Kurokawa bridge, Bocherer bridge.
**AP42 violation**: The escalation principle at genus >= 6 has unflagged circularity (requires Langlands functoriality). The Newton-Thorne result breaks this for holomorphic forms.
**Enhancement**: The swarm found that genus-2 theta distinguishes 20/24 Niemeier lattices (4 collision pairs). Add this finding. Genus-3 needed for full discrimination.
**Enhancement**: The Schur complement analysis (from swarm): Heisenberg = no new constraints, interacting algebras = quadratic OPE constraints at weight >= 4 but these constrain OPE not Satake. DEFINITIVE: genus-2 constrains partition function weights but NOT Satake magnitudes.

### Section: The prime-locality assessment (lines 9620-10018)

**Correct**: Comprehensive, honest, well-structured. The five obstructions (Thm 9690), Route C assessment (Rem 9823), modified prime-locality (Thm 9893), and definitive status (Rem 9927) are all exemplary.
**No mathematical changes needed**. This section is the strongest part of the chapter.

---

## 2. AP42 Violations (Exact Line Numbers)

| # | Line(s) | Current text | Fix |
|---|---------|-------------|-----|
| 1 | 33-36 | "the shadow obstruction tower is the universal invariant that encodes both the Langlands programme (arithmetic) and the Sullivan programme (homotopy theory)" | "the shadow obstruction tower organizes the algebraic data that, for lattice vertex algebras, connects to both the Langlands programme (arithmetic) and the Sullivan programme (homotopy theory)" |
| 2 | 3683-3694 | "completing the reduction" (genus-2 Beurling kernel escalation to all genera) | "narrowing the gap (conjectural at g >= 3; requires Langlands functoriality GL(2)->GL(g) for g >= 6, open beyond g = 4)" |
| 3 | 5316 (thm:cps-from-mc) | ClaimStatusConditional but proof contains "Caveat" buried deep | Move caveat to theorem statement as a visible "[Conditional on PL convexity bounds for GL(j) twists, j >= 3]" tag |
| 4 | 9412-9413 | "The MC equation at all genera thereby implements Serre's programme: Ramanujan follows from all-genera symmetric-power non-vanishing." | "The MC equation at all genera thereby encodes the algebraic data that the Serre reduction requires: Ramanujan would follow from all-genera symmetric-power non-vanishing, conditional on Langlands functoriality GL(2)->GL(g) for g >= 5." |
| 5 | Introduction lack of Niemeier blindness | Omission: the scalar shadow obstruction tower is presented as detecting arithmetic, but for Niemeier lattices it is completely blind | Add explicit "Limitation" paragraph in introduction |

---

## 3. Scope Inflation Sites (Exact Line Numbers)

| # | Line(s) | Issue | Fix |
|---|---------|-------|-----|
| 1 | 33-36 | "universal invariant" for a projection of Theta_A | Qualify: "organizing structure" not "universal invariant" |
| 2 | 121-123 | "The number of critical lines of epsilon^r_s equals the shadow depth d(V_Lambda) minus 1" -- stated for lattice VOAs but the epsilon^r_s notation appears without lattice qualifier at the DEFINITION level | Verify: the theorem statement at line 103 specifies "Let V_Lambda be an even lattice vertex algebra." Correct as stated. No fix. |
| 3 | 5316-5334 | CPS hypotheses theorem: proof contains a deep "Caveat" (line 5353) about Phragmen-Lindelof estimates for GL(j) twists. The theorem statement does not flag this conditionality. Tag is ClaimStatusConditional which is correct, but the conditionality is easy to miss. | Add "(conditional on Phragmen-Lindelof estimates for GL(j) twists at j >= 3)" to theorem statement |
| 4 | 5926-5937 | cor:unconditional-lattice says "provides an alternative derivation of Deligne's theorem, relying on the Langlands programme." This is correctly stated but the word "alternative" may overstate independence since CPS+JS are themselves deep results. | Add parenthetical: "(relying on CPS, Jacquet-Shalika, and strong multiplicity one from the Langlands programme rather than on etale cohomology)" -- already present at line 5933. No fix needed. |
| 5 | Introductory claim (line 68) | "unconditional Ramanujan bound for lattice VOAs (Corollary)" | Check: this IS unconditional for lattice VOAs. The chain is MC -> prime-locality (proved for lattices) -> CPS (unconditional) -> Sym^r identification -> Ramanujan. Correct. No fix. |

---

## 4. New Material to Add

### 4A. The Charged-Sector Resolution (NEW SECTION, ~200 lines)

**Position**: After Section "Five lattice verifications" (line 491), before "Proof of the shadow-spectral correspondence."

**Content**:
- **Problem statement**: The scalar shadow obstruction tower (kappa, depth) assigns kappa=24 and depth=4 to ALL 24 Niemeier lattices. This is completely blind: 0/276 pairs distinguished.
- **Resolution**: Theta_A decomposes by lattice grading gamma in Lambda. The vacuum sector (gamma=0) gives the universal kappa=24. The charged sectors (gamma != 0) encode the root system.
- **Complete invariant**: Per-factor (Coxeter h, rank partition) from multi-channel bar complex. Strictly stronger than genus-2 theta.
- **The Z = Z^sh * Z^arith decomposition**: Z^sh = eta^{-r} (topological, tau-independent), Z^arith = Theta_Lambda (arithmetic). The shadow obstruction tower operates on Z^sh; the arithmetic content lives in Z^arith.
- **Genus-2 theta discrimination**: Distinguishes 20/24 (4 collision pairs with identical genus-2 theta). Genus 3 needed for theta route. Multi-channel bar complex resolves all 24 at genus 1.
- **Reference**: New compute modules `niemeier_multichannel.py`, `niemeier_complete_invariant.py`, `niemeier_shadow_atlas.py`.

### 4B. Ising Paradox and Fusion Ring Arithmetic (NEW REMARK, ~30 lines)

**Position**: After Prop 1208 (Ising d_arith = 0), expand existing.

**Content**: d_arith=0, d_alg=infinity, yet the Ising model has deep arithmetic structure in its fusion ring and VVMF. The depth decomposition captures only Roelcke-Selberg spectral content; the fusion ring arithmetic is invisible to it. The Ising arithmetic lives in the VVMF structure, not in the primary-counting Epstein zeta. Genus-dependent arithmetic depth d_arith^{(g)} proposed: d_arith^{(1)} = 0 (no holomorphic eigenforms at genus 1), but d_arith^{(2)} potentially nonzero via the genus-2 theta representation.

### 4C. Depth Decomposition Universality (EXPAND existing Theorem)

**Position**: Theorem 1326 (depth decomposition).

**Content**: Add explicit statement that d = 1 + d_arith + d_alg holds for ALL modular Koszul algebras, not just lattices. Add the complete d_alg table: G(0), L(1), C(2), M(infinity). Note: first d_arith > 3 at rank 48; M(7,8) has d_arith = 7.

### 4D. Non-Perturbative and p-adic Content (NEW SUBSECTION, ~100 lines)

**Position**: After Section "The period filtration" (line 1817), or as a new section.

**Content**:
- **Naive Borel-arithmetic conjecture FALSIFIED**: Resurgence in two orthogonal directions. c=26 anomaly cancellation exact in Stokes multipliers.
- **p-adic convergence**: Shadow obstruction tower has p-adic convergence radius p^{1/(p-1)} (exponential radius). Kummer congruences verified.
- **Reference**: `arithmetic_resurgence.py`.

### 4E. V-natural as Class M (NEW REMARK, ~20 lines)

**Position**: In the depth decomposition section, after the G/L/C/M table.

**Content**: The moonshine module V-natural has kappa=24 (same as all Niemeier lattices) but is class M (infinite shadow depth), making it the first known example of a same-kappa different-class pair. The scalar shadow obstruction tower cannot distinguish V-natural from the 24 Niemeier lattices.

### 4F. Arithmetic Comparison Conjecture Sharpening (EXPAND existing)

**Position**: The arithmetic comparison conjecture (line 75, Conj referred to in intro).

**Content**: The swarm found that the naive (scalar) version is FALSE. The full version is consistent but NOT injective (factors through Z(tau)). Add:
- Minimal arity for discrimination: G=2, L=3, C=4, lattice=dim(M_{r/2})+1, M=infinity.
- The charged-sector resolution is needed for injectivity.

### 4G. Genus-2 Bocherer Bridge Expansion (EXPAND existing, ~50 lines)

**Position**: Existing subsection at line 9264.

**Content**: Add from swarm:
- Fock non-diagonality PROVED.
- Bocherer bridge PROVED (Furusawa-Morimoto).
- Unfolding: Siegel + Klingen channels erase. Bocherer channel BYPASSES unfolding.
- Schur complement: Heisenberg = no new constraints. Interacting algebras = quadratic OPE constraints at weight >= 4.
- DEFINITIVE: Genus 2 constrains partition function weights but NOT Satake magnitudes. Ramanujan is per-prime; genus 2 does not help.
- For Leech: ALL genus-2 cusp forms at weight 12 are SK lifts. Genuinely new Siegel eigenforms at weight >= 20 only.

### 4H. Escalation Circularity at g >= 6 (ADD to existing)

**Position**: Rem 3684 (escalation principle) and the genus-2 frontier assessment.

**Content**: Flag the circularity: genus-g MC contributes L(1/2, Sym^{g-1} f x chi_D), but for g >= 6 this requires automorphy of Sym^{g-1}, which is Langlands GL(2)->GL(g), open for g >= 5. Newton-Thorne (2021) breaks this for holomorphic cuspidal eigenforms of regular algebraic weight, giving an unconditional escalation for such forms. For Maass forms: stuck at Kim-Sarnak theta <= 7/64.

---

## 5. Material to REMOVE or DOWNGRADE

| # | Line(s) | Issue | Action |
|---|---------|-------|--------|
| 1 | 33-36 | "universal invariant" overclaim | DOWNGRADE to "organizing structure" |
| 2 | None found | No theorems to retract | -- |
| 3 | 3683-3694 | "completing the reduction" | DOWNGRADE to "narrowing the gap" |
| 4 | The shadow Epstein zeta construction (1893-1902) | Well-defined but has no proved connection to anything beyond the shadow obstruction tower itself | KEEP but add remark that this is a formal construction whose arithmetic content is unexplored |
| 5 | The Beilinson functional (lines 4312-4397) | Conjectural, honestly labelled. No downgrade needed. | KEEP |
| 6 | conj:quartic-closure (line 3427) | Honestly labelled conjectural | KEEP |
| 7 | conj:clutching-closure (line 4269) | Honestly labelled conjectural | KEEP |
| 8 | conj:beilinson-closure (line 4358) | Honestly labelled conjectural | KEEP |

**Assessment**: Nothing needs to be REMOVED. The chapter is remarkably honest about the status of its conjectures. The main action is ADDING missing findings and correcting the 5 AP42 violations.

---

## 6. Rewrite Ordering (Upstream-First)

The dependency structure of the chapter:

```
Sewing operator (lines 198-272)
  |
  v
Sewing-Selberg formula (274-327)
  |
  v
Four identities (329-463) --- independent of each other
  |
  v
Five lattice verifications (466-491)
  |
  v
*** NEW: Charged-sector resolution (Niemeier discrimination) ***
  |
  v
Proof of shadow-spectral correspondence (493-601)
  |
  v
Period-shadow dictionary (643-944)
  |
  v
Depth decomposition (1321-1473) <-- depends on cusp-singularity (947-1154) + non-lattice (1156-1235) + higher depths (1237-1318)
  |
  v
Period filtration (1679-1817)
  |
  v
Spectral curve + sewing-shadow intertwining (1820-2596)
  |
  v
Hecke module structure (3063-3138) + quartic residue programme (3141-4619)
  |
  v
Structural diagnosis (4623-4795)
  |
  v
Geometric positivity (4958-5062) + modular rigidity (5065-5301)
  |
  v
Operadic transfer (5304-5755)
  |
  v
Hecke-Newton closure (5759-6448) + self-duality principle (6683-6957)
  |
  v
Complexified modular integral (6958-7665) + analytic continuation (7667-9084)
  |
  v
Genus-2 frontier (9085-9619)
  |
  v
Prime-locality assessment (9620-10018)
```

**Execution order**:

1. **Fix introduction AP42** (line 33-36): immediate, no dependencies.
2. **Fix escalation AP42** (line 3683-3694): immediate.
3. **Fix CPS conditionality** (line 5316): immediate.
4. **ADD charged-sector resolution** (after line 491): new section, no downstream dependencies broken.
5. **EXPAND Ising paradox** (after line 1234): small addition.
6. **EXPAND depth decomposition** (line 1326): add universality and complete table.
7. **ADD V-natural class M remark** (near line 1365): small addition.
8. **ADD non-perturbative/p-adic** (after line 1817): new subsection.
9. **ADD arithmetic comparison sharpening** (referenced in intro): expand existing conjecture.
10. **EXPAND genus-2 Bocherer bridge** (line 9264): add swarm findings.
11. **ADD escalation circularity flag** (line 3684 and genus-2 section): additions.
12. **Build test**: `make fast` after each batch of 3 changes.

---

## 7. New Sections Needed

| # | Title | Position | Length | Priority |
|---|-------|----------|--------|----------|
| 1 | The charged-sector resolution: beyond the scalar shadow | After "Five lattice verifications" (line 491) | ~200 lines | HIGH -- the Niemeier blindness is a major gap |
| 2 | Non-perturbative arithmetic of the shadow obstruction tower | After "The period filtration" (line 1817) | ~100 lines | MEDIUM -- Borel-arithmetic falsification is important |
| 3 | The genus-dependent arithmetic depth | In "Higher depths" section (line 1237) | ~40 lines | MEDIUM -- natural extension of depth decomposition |
| 4 | The Ising arithmetic paradox | In "Non-lattice theories" (after line 1234) | ~30 lines | LOW -- enriches existing content |
| 5 | V-natural and same-kappa different-class examples | In depth decomposition section | ~20 lines | LOW -- one remark |

---

## 8. Swarm Finding -> Section Mapping

Every finding from the swarm mapped to a specific action:

| Swarm Finding | Section | Action |
|---|---|---|
| Niemeier scalar blindness (0/276 pairs) | NEW Section 7.1 | Create charged-sector resolution section |
| Charged-sector resolution | NEW Section 7.1 | Create |
| Z = Z^sh * Z^arith decomposition | NEW Section 7.1 | Include |
| Genus-2 theta distinguishes 20/24 | Section 9 (genus-2 frontier) | Expand |
| d = 1 + d_arith + d_alg universal | Section 5 (depth decomposition) | Expand theorem statement |
| Complete d_alg table G/L/C/M | Section 5 | Add table |
| First d_arith > 3 at rank 48 | Section 4 (higher depths) | Add remark |
| Ising paradox: d_arith=0, d_alg=infinity | Section 3 (non-lattice) | Add remark |
| Genus-dependent d_arith^{(g)} | NEW subsection in higher depths | Create |
| Newton from MC = exactly Newton (tautology) | Section 6 (MC recursion) | Add clarifying remark |
| Sewing-Selberg PROVED | Already present | No change |
| Structural separation PROVED | Already present | No change |
| Koszul-Epstein FE verified | Already present (Comp 2985) | No change |
| Benjamin-Chang scattering factor | Already present (Rem 2900) | No change |
| Universal residue factor computed | Already present (Def 3323) | No change |
| Critical line atlas complete | Already present (table in 4 identities) | No change |
| Geometric positivity constrains weights not eigenvalues | Already present (Rem 5033) | No change |
| Zero-forcing FAILS | Already present (structural obstruction) | No change |
| Operadic RS correctly CONJECTURE | Already present (Conj 5646) | No change |
| Gap = Langlands GL(2)->GL(r+1) for r>=5 | Already present (Rem 4932) | No change |
| MC = integrability, spectral = positivity, logically independent | Already present (Rem 3513) | No change |
| Fock non-diagonality PROVED | Section 9 (genus-2) | Expand |
| Bocherer bridge PROVED | Section 9 | Expand |
| Unfolding: Siegel+Klingen erase, Bocherer bypasses | Section 9 | Add |
| Schur complement: Heisenberg=no new, interacting=OPE constraints | Section 9 | Add |
| DEFINITIVE: genus-2 constrains weights not Satake | Section 9 | Add as remark |
| Leech: all genus-2 cusp forms are SK lifts | Section 9 | Add |
| Escalation circularity at g>=6 | Section 8 (quartic residue) + Section 9 | Flag |
| Newton-Thorne breaks circularity for holomorphic forms | Section 9 | Add |
| AP42 line 33-36 "universal invariant" | Introduction | Fix |
| AP42 line 3683-3694 "completing the reduction" | Quartic residue section | Fix |
| AP42 line ~9412 "implements Serre's programme" | Search and fix if found |
| Naive Borel-arithmetic FALSIFIED | NEW section (non-perturbative) | Create |
| Resurgence in two orthogonal directions | NEW section | Include |
| c=26 exact in Stokes multipliers | NEW section | Include |
| p-adic convergence radius = p^{1/(p-1)} | NEW section | Include |
| Kummer congruences verified | NEW section | Include |
| V-natural is class M | Depth decomposition | Add remark |
| Arithmetic comparison conjecture: naive FALSE, full consistent but not injective | Introduction / existing conjecture | Expand |
| Minimal arity: G=2, L=3, C=4, lattice=dim+1, M=infinity | Arithmetic comparison section | Add table |

---

## 9. Prose Quality Notes

The chapter prose is already at high quality (Russian school standard). Notable strengths:
- The four gaps (lines 3463-3572) are exemplary honest assessment.
- The prime-locality definitive status (lines 9925-10018) is a model of scope honesty.
- The positivity limitation (Rem 5033) correctly states what bracket positivity can and cannot do.
- Every conjecture is tagged ClaimStatusConjectured.
- RECTIFICATION-FLAGs at lines 1593 and 2171 are honest.

Minor prose issues:
- A few instances of "indeed" and "precisely" that could be trimmed.
- The phrase "the shadow obstruction tower detects the algebra itself" (line 28) is evocative but imprecise; it should say "the shadow obstruction tower's infinite depth reflects the self-referential OPE structure."

---

## 10. Build and Test Plan

After each batch of 3 edits:
```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast
```

After all edits:
```
make test
python3 -m pytest compute/tests/test_niemeier*.py compute/tests/test_arithmetic*.py compute/tests/test_lattice*.py -x --tb=short -q
```

Estimated total edit count: ~15 surgical edits + 2 new sections (~300 lines total new content).
Estimated time: 3-4 hours for careful execution with build gates.
