# Deep Audit: W-infinity Factorization Koszul Dual -- Session 8
# Date: 2026-03-14
# Scope: Chriss-Ginzburg concretization audit of the MC4 W-infinity construction

## I. Cartography

### Proved Claims (ProvedHere)

| Label | File:Line | Depends On | Compute Verification |
|---|---|---|---|
| `thm:winfty-factorization-kd` | w_algebras_deep.tex:795 | thm:master-pbw, thm:ds-koszul-intertwine, cor:level-shifting-part1, thm:h-level-factorization-kd | Indirect (W3/W4 OPE tests) |
| `thm:ds-koszul-intertwine` | chiral_modules.tex:4187 | DS vanishing theorem, double complex/spectral sequence argument | None |
| `cor:ds-bar-level-shift` | chiral_modules.tex:4311 | thm:ds-koszul-intertwine, cor:level-shifting-part1 | None |
| `prop:winfty-mc4-criterion` | bar_cobar_construction.tex:5622 | prop:mc4-reduction-principle, cor:mc4-degreewise-stabilization, prop:inverse-limit-differential-continuity | None |
| `cor:winfty-weight-cutoff` | bar_cobar_construction.tex:5673 | prop:mc4-weight-cutoff (conformal weight stabilization) | None |
| `cor:winfty-standard-mc4-package` | bar_cobar_construction.tex:5770 | prop:winfty-mc4-criterion, cor:winfty-weight-cutoff, prop:inverse-limit-differential-continuity | None |
| `cor:winfty-hlevel-comparison-criterion` | bar_cobar_construction.tex:5882 | prop:completed-target-comparison, Milnor exact sequence | None |
| `prop:winfty-ds-stage3-explicit-packet` | bar_cobar_construction.tex:6856 | Explicit W3 OPE | test_w3_bar.py (passes) |
| `prop:winfty-ds-stage4-residual-packet` | bar_cobar_construction.tex:6952 | Stage-3 packet, Virasoro action | test_w4_* (passes) |
| `prop:winfty-mc4-frontier-package` | bar_cobar_construction.tex:7793 | cor:winfty-hlevel-comparison-criterion, stage3/4 packets, DS-side extraction | test_w_infinity_dual_candidate.py (passes) |
| `prop:paired-standard-mc4-frontier` | examples_summary.tex:236 | cor:winfty-standard-mc4-package, cor:yangian-standard-mc4-package | None |
| `prop:w-algebra-scalar-saturation` | higher_genus.tex:14761 | BRST pullback, H^2_cyc = C, Fateev-Lukyanov rigidity | None |

70+ additional propositions and corollaries at stages 4-5 in bar_cobar_construction.tex:6129-11050 (all PH), decomposing the stage-4 and stage-5 packets into increasingly refined subpackets.

### Conjectured Claims (27 total in bar_cobar_construction.tex)

| Label | File:Line | Nature |
|---|---|---|
| `conj:master-infinite-generator` | concordance.tex:610 | H-level comparison for both towers |
| `conj:w-infty-bar` | w_algebras_deep.tex:502 | Large-N coupling identification |
| `def:winfty-principal-stage-compatible` | bar_cobar_construction.tex:5931 | Desideratum for H-level target |
| `def:winfty-quotient-system` | bar_cobar_construction.tex:5953 | Desideratum for quotient system |
| `def:winfty-stage4-ward-normalized` | bar_cobar_construction.tex:8078 | Ward normalization hypothesis |
| `conj:winfty-stage4-ward-inheritance` | bar_cobar_construction.tex:8281 | Key missing lemma for 6-to-4 contraction |
| `conj:winfty-stage4-visible-diagonal-normalization` | bar_cobar_construction.tex:8253 | Visible diagonal |
| `conj:winfty-stage4-visible-borcherds-transport` | bar_cobar_construction.tex:8591 | Borcherds transport |
| `conj:winfty-stage5-*` (18 conjectures) | bar_cobar_construction.tex:10329-10932 | Stage-5 principal structural input |

---

## II. Gaps

### Gap 1: The H-level filtered target W^{ht} does not exist

The entire MC4 programme rests on constructing a separated complete filtered H-level target whose finite quotients recover the principal stages W_N. No such object is constructed anywhere in the monograph. The definitions at bar_cobar_construction.tex:5931 and :5953 are conjectured desiderata, not constructions. The concordance (concordance.tex:609-692) states this explicitly as the content of conj:master-infinite-generator.

### Gap 2: dim H^2_cyc(W_infinity) is not computed

The text proves dim H^2_cyc(W_N, W_N) = 1 for each finite W_N (higher_genus.tex:14773). But the non-scalar Theta_A programme (raeeznotes34.md) requires dim H^2_cyc >= 2. The text does not prove, state, or even conjecture what dim H^2_cyc(W_infinity) is. The BRST pullback argument that gives dim <= 1 for finite W_N does not obviously extend to the inverse limit. The stability of H^3(sl_N) = C strongly suggests dim H^2_cyc(W_infinity) = 1, which would mean W_infinity cannot provide a non-scalar Theta_A.

### Gap 3: No bar-side residue extraction exists in compute/

The compute infrastructure extracts only DS-side coefficients C^DS. No code computes bar complex entries from the configuration-space residue calculus and extracts C^res independently. The variable "C_res" in w4_ds_ope.py is misleadingly named.

### Gap 4: c334^2 and c444^2 are imported, not derived

These square-class expressions are imported from external literature (Hornfeck 1993, Blumenhagen et al. 1996). The monograph does not derive them from the explicit DS BRST complex.

### Gap 5: Factorization descent for the completed object is terse

The proof of Part (iii) of thm:winfty-factorization-kd compresses the factorization-level lim^1 vanishing argument.

### Gap 6: No geometric home for higher-spin bar complex channels

For W-algebras, no analogue of the affine Grassmannian / KL conjecture geometric realization is developed.

### Gap 7: Yangian-W_infinity connection is parallel but not functorial

No theorem, functor, or construction connects the two MC4 towers.

---

## III. Critical Path

### Three highest-impact missing constructions

1. Explicit W^{ht} via Miura realization
2. Compute dim H^2_cyc(W_infinity) in the large-N limit
3. Build bar-side residue extraction at stage 4

### Three highest-impact missing computations

1. Independent bar-side C^res for the stage-3 packet
2. DS-derived c334^2 from the explicit sl_4 BRST complex
3. Explicit cyclic cocycle basis for W_infinity

### One missing perspective

The convolution-algebraic realization of the W-algebra bar complex via perverse sheaves on the Slodowy slice inside the affine Grassmannian.

---

## IV. Computational Evidence

### Test suite: 610/610 pass (all W-infinity related)

All tests genuine (not tautological). But all tests are DS-side. None independently compute bar-side residues.

### Independent verification: stage-3 packet

- Seed set I_3 has 15 elements
- Three nonzero entries: C^DS_{2,2;2;0,2} = 2, C^DS_{2,3;3;0,2} = 3, C^DS_{3,3;2;0,4} = 2
- Twelve zero entries verified
- c334^2 and c444^2 formulas match Hornfeck symbolically

---

## V. Verdict

The W_infinity construction is solidly proved at the M-level and extensively analyzed at the conjectural H-level frontier. Two critical obstructions prevent it from fulfilling its non-scalar Theta_A aspiration: (1) W^{ht} is a desideratum, not a construction; (2) dim H^2_cyc(W_N) = 1 for every finite N, strongly suggesting dim H^2_cyc(W_infinity) = 1, which would kill the non-scalar programme.

The single most important next step is to compute dim H^2_cyc(W_infinity) honestly.
