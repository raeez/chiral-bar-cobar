# Beilinson Audit (Wave 11) — Vol I Overture

**Target.** `/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex` (4378 lines).

**Scope.** Deep adversarial audit by the six hostile examiners. Special focus: the Wave 5-3 CS hinge (~lines 2797-3318), Heisenberg OPE from CS bulk propagator, Wick expansion, av(r(z))=kappa derivation, Feigin-Frenkel c+c'=26, residual AP24/AP25/AP34/AP126 debt.

**Verification runs.** F_g (g=1..6) reproduced exactly from Faber-Pandharipande (2^{2g-1}-1)/2^{2g-1} · |B_{2g}|/(2g)!. hat-A(ix) = (x/2)/sin(x/2) verified symbolically. Vir c(k)+c(-k-4)=26 verified at k=0,1. F_2 = 7/8 · (1/30)/24 = 7/5760 matches chapter line 1549-1554.

---

## Examiner 1 — Formalist

### CRITICAL

**F1-C1. Unquantified variable g in obs_g = kappa · lambda_g (line 1777).** The sentence "obs_g = k · lambda_g for all g >= 1 (UNIFORM-WEIGHT)" appears inside Definition~\ref{def:frame-modular-package}. The tag is present, but the definition states the scalar package applies "for all g >= 1". The Heisenberg case is uniform-weight, so this happens to be correct, but the def should state "Heisenberg has uniform weight, hence the scalar formula extends to all g" rather than asserting it as an axiom of the def. AP32 compliance is LOCAL (tag on line 1777, 4215, 1628) but not at the displayed theorem-level panels (lines 176-179 `\textbf{D}` block gives the generating function with no UNIFORM-WEIGHT tag).

**F1-C2. Theorem C displayed at line 176** is `Q_g(H_k) + Q_g(H_k^!) = H^*(M_g, Z)`, written with `+` (direct sum), but line 1735 and the general Theorem C use both `+` and `⊕` language interchangeably. For Koszul PAIRS the statement is direct-sum-as-Lagrangians, not just `+`. MINOR notation ambiguity; the remark at line 1748 clarifies it as "complementary Lagrangians." Recommend aligning notation.

### MODERATE

**F1-M1. Proposition `prop:frame-twisting-MC` (lines 942-984) proves MC only at degrees 1 and 2.** The proof stops at degree 2 and implicitly claims the pattern extends. For Heisenberg this is fine (the bar vanishes in higher degree), but the proof should say so explicitly. Line 984 just ends `= -k + k = 0`. A reader cannot tell whether the MC equation has been verified at all degrees or only degree 2.

**F1-M2. Theorem `thm:frame-heisenberg-bar` (line 854) claim `H^n = 0 for n > 2`** is proved (line 897-902) by "dimension counting" and "abelian Lie algebra cohomology of a 1-dim central extension." This is a one-sentence proof for the whole degree≥3 vanishing. The chiral bar complex H^n is on FM_n(P^1) not the classical Lie algebra bar, so this conflation (AP63) needs more care. The argument effectively invokes Fourier-duality/Koszulness but the proof text hand-waves.

**F1-M3. Theorem `thm:frame-genus1-curvature` (line 1391) states d_fib^2 = k · omega_1.** The "proof" (line 1401-1408) is a one-paragraph sketch: "B-cycle monodromy contributes a phase e^{2 pi i k}... squaring... produces the Hodge class". But the phase and the Hodge class live on DIFFERENT spaces (AP130: forms on Sigma_tau vs classes on M_g). The actual argument requires integrating -2 pi i · dz against a cycle on the fiber, then varying tau, which is cross-referenced to `thm:heisenberg-obs`. The in-chapter sketch is an IOU, not a proof.

### MINOR

- **F1-m1. `\ClaimStatusProvedHere` vs actual proof.** `prop:frame-arnold` (line 506): proof is sound (partial fractions). `thm:frame-heisenberg-koszul-dual` (line 1145): proof text follows as prose, no `\begin{proof}`. AP4 compliance formal but loose.
- **F1-m2. Ran-space vs FM-space slippage.** Line 86 writes `FM compactification` while line 89 writes `factorization coalgebra on Ran(X)`. The two are related but distinct; the chapter should state once that the ordered FM-space functions as the chain-level model for the Ran-space coalgebra.

---

## Examiner 2 — Topologist

### CRITICAL

**F2-C1. "gravity operad Grav = HyCom^!" (line 539) is correct but the follow-up "genus-0 bar-cobar adjunction is operadic Koszul duality" is overstated.** Getzler-Kapranov give HyCom^! = Grav at the cyclic (tree-level) level; the *chiral* bar-cobar adjunction uses FM_n(X) with logarithmic forms on an algebraic curve, which is richer than the combinatorial Grav/HyCom duality. Saying the two "are" Koszul duality elides the curve-dependence. AP101 / AP34 territory.

**F2-C2. E_infty tier vs E_1 tier confusion around the odd current algebra (lines 3697-3720).** The chapter (line 3696) labels Heisenberg, sl_2, odd current all as "E_infty (tier b)" but says the odd current's "ordered bar complex carries genuinely nontrivial braiding data R(z)=exp(k hbar/z), even though this data happens to be derivable from the OPE." If the R-matrix is derivable from the OPE, the algebra is E_infty in the formality sense and the braiding is "shadow" data. Calling it both "nontrivial braiding" and "tier b" risks AP86/AP88 conflation. The remark (3694-3721) partially saves this by calling the distinction "the hinge", but this hinge language is a philosophical dodge, not a mathematical classification.

### MODERATE

**F2-M1. Milnor-Moore invocation at lines 1052-1056** is on shaky ground for chiral coalgebras. Milnor-Moore is classical (ordinary Hopf algebras, char 0). The chiral bar coalgebra is a factorization coalgebra on Ran(X), which is NOT a Hopf algebra. The analogy "such a coalgebra is the universal enveloping coalgebra of its primitives" is suggestive but NOT a theorem in the chiral setting. Flag as analogy, not invocation.

**F2-M2. "free Lie algebra on a single generator is abelian" (line 1072).** Classically Lie(V) for dim V=1 has dimension (n-1)! per arity as an operad component, and is 1-dimensional as a free Lie algebra quotient; the chapter tries to clarify this parenthetically (lines 1075-1079) but the text "Lie(n)=0 for all n >= 2" is ambiguous between "graded piece of free Lie algebra on one generator" (correct, = 0 for n>=2) and "operad component Lie(n)" (wrong, = (n-1)!). Parenthetical rescue is present but the primary sentence is still wrong as written.

### MINOR

- **F2-m1. Swiss-cheese for one-color algebras** (lines 2338-2392). The Swiss-cheese operad is two-colored by construction (disks-in-half-plane); applying it to a one-color algebra like sl_2 requires the promotion A -> (A, A). The chapter does not explicitly say this (AP86). Theorem `thm:rosetta-sl2-swiss` should reference the promotion.
- **F2-m2. "genuinely E_1 examples" claim (line 3626)** lists only Y(sl_2)^ch as the genuinely-E_1 entry. But this contradicts the tier-(c) claim: the chapter treats Yangian as E_1 but the cell has em-dashes for Heisenberg, sl_2, odd current. OK, consistent.

---

## Examiner 3 — Physicist (CS hinge focus)

### CRITICAL

**F3-C1. Boundary OPE derivation from CS path integral (lines 2904-2924).** The chapter claims: "A short calculation (using the Green's function for d + bar-partial on Sigma × R_{>=0} with reflecting boundary at t=0) yields J(z) J(w) ~ k/(z-w)^2." This is ASSERTED, not computed. The actual derivation of the Heisenberg double pole from the CS bulk propagator goes through holomorphic Chern-Simons (Costello 2013) or the Cattaneo-Felder approach, and the propagator depends critically on the gauge-fixing. The "short calculation" is a multi-page story in the literature. The chapter marks this as derivation, not theorem — OK — but the shortening is misleading. Recommend citing Costello-Gwilliam Vol 2 or BY for the Green's function computation.

**F3-C2. "The propagator is k · partial_z eta" (line 2986).** This is NOT quite right. The Arnold form eta = d log(z-w) has a simple pole as a 1-form. The propagator `k/(z-w)^2` is a 2-form or a kernel; writing it as `k · partial_z eta` requires specifying what partial_z means (acting on the form as a section). The chapter writes partial_{z_i} eta_{ij} but does not verify that eta_{ij} differentiates to (dz_i - dz_j)/(z_i-z_j)^2 dz_i = dz_i ^ dz_j/(z_i-z_j)^2 ... which is not obviously the scalar double pole. AP117 adjacent: the one-form vs kernel confusion. MODERATE-to-CRITICAL.

**F3-C3. "the adjoint trace Tr(ad_e ad_f) = 2h^vee · kappa^{ab}" with 2h^vee = 4 (line 2517-2519).** For sl_2, adjoint rep is 3-dim, eigenvalues of ad_h = {+2, 0, -2}. Tr(ad_h^2) = 4+0+4 = 8, so Tr(ad_h ad_h) = 8, and kappa^{hh}=2 (normalized), giving 2h^vee = 8/2 = 4. OK. But Tr(ad_e ad_f): e and f don't commute, and ad_e ad_f acts as... let me compute. In the Chevalley basis, the Killing form K(e,f) = 4 for sl_2 (standard). So Tr(ad_e ad_f) = 4 = 2h^vee · K_norm(e,f) = 4 · 1. OK, 2h^vee=4 checks if kappa^{ef}=1 is the normalized form. This is a convention, not a formula verification — the chapter's sentence is OK but the "proof" line 2515-2520 is elliptic.

### MODERATE

**F3-M1. "Koszul duality is the boundary-changing functor of Dimofte" (line 2838-2839, cited CostelloGaiotto2020).** The Dimofte-Costello-Gaiotto boundary condition picture identifies Dirichlet with one VOA and Neumann with the dual, but the boundary-changing FUNCTOR is a bimodule, not a duality per se. Saying "Koszul duality IS the boundary-changing functor" conflates two different statements. The heuristic tag saves this, but AAP18 requires citing the correct construction (e.g., Costello-Gaiotto 2020 section 5 or similar) rather than just labeling the whole 2020 paper.

**F3-M2. The 4d-3d-2d cascade (line 3194 onward) invokes "4d N=2 gauge theory on a slab with holomorphic-topological twist" and "abelian case (G=U(1), no hypermultiplet) -> abelian CS."** The cascade is correct at the moral level but misses a subtlety: holomorphic-topological twist of N=2 is Kapustin's HT twist, which gives holomorphic CS for the complexified gauge group. For G=U(1) this is abelian HOLOMORPHIC CS, which is NOT the same as ordinary 3d abelian CS (the level is complex, the theory is topological only in one direction, and the boundary algebra is different). The chapter conflates holomorphic-topological CS with ordinary topological CS. This is a genuine physics error (though the author marks it as heuristic).

**F3-M3. The genus tower statement (line 3266-3269): "F_g = k · lambda_g^{FP} is the perturbative expansion of the 4d partition function on Sigma_g × I × I with Melvin twist."** The Melvin twist resolves the elliptic genus at genus 1, but the genus-g partition function from a 4d theory on Sigma_g × I × I is NOT obviously the FP lambda_g formula. The latter is an intersection theory calculation on M_g, while the former is a path integral. The identification is plausible (Costello's holomorphic-topological program aims at this) but the chapter asserts it as a derivation. Should be flagged as conjectural.

### MINOR

- **F3-m1. "k is integer because large gauge transformations..." (line 2862-2865).** The integrality of k for abelian CS on a closed 3-manifold is subtle (requires H^1 to be nontrivial). On Sigma × R_{>=0} with chiral Dirichlet, no integrality is needed. The chapter conflates level-quantization with the perturbative expansion.
- **F3-m2. "chiral Dirichlet fixes A^{0,1}, lets A^{1,0} fluctuate" (line 2900-2903).** Standard, but the sign convention matters: which of (0,1) or (1,0) gives the Heisenberg boundary OPE with *double* pole vs simple pole? The chapter skips this.

---

## Examiner 4 — Number Theorist

### MODERATE

**F4-M1. E_2 modular anomaly formula (line 1436): E_2((a tau+b)/(c tau+d)) = (c tau+d)^2 E_2(tau) + 6c(c tau+d)/(pi i).** Standard formula, sign convention OK. But the anomaly sign depends on the normalization of E_2; the chapter uses E_2 = 1 - 24 sum sigma_1 q^n (line 1339), which is the quasi-modular form with weight 2. The anomaly term +6c(c tau + d)/(pi i) is correct for this normalization.

**F4-M2. Heisenberg partition function Z = 1/eta(tau) = q^{-1/24} prod (1-q^n)^{-1} (line 1374).** Standard; Dedekind eta's exponent -1/24 is for c=1 (one boson). The chapter states c=1 at line 204, consistent.

**F4-M3. Bernoulli numbers in F_g (line 1691-1700).** Table verified: B_2=1/6, B_4=-1/30, ..., B_{12}=-691/2730. Decimal approximations match.

**F4-M4. Euler-Maclaurin and the asymptotic F_g ~ 2k/(2 pi)^{2g} (line 1708).** This follows from |B_{2g}| ~ 2(2g)!/(2 pi)^{2g}. Writing F_g ~ 2k/(2 pi)^{2g} requires the (2^{2g-1}-1)/2^{2g-1} factor to -> 1, which is correct. Verified.

### MINOR

- **F4-m1. Siegel modular forms of Sp(4,Z) at genus 2 (line 1515).** The claim is that prime-form coefficients c_{2j}(Omega) are Siegel modular forms. Standard and correct.
- **F4-m2. Holomorphic anomaly equation (line 1443).** The equation is correct to the extent E_2 is the only piece; missing: a reference to the full BCOV holomorphic anomaly for higher spin.

---

## Examiner 5 — Adversarial Chef (weakest-link)

### CRITICAL

**F5-C1 (THE WEAKEST LINK).** The chain of "instantly visible" claims in the opening (lines 38-66) asserts that:
1. d_{Ch_infty} = 0 (OPE abelian) — OK
2. d_{coll} = 0 (no nonlinear collision residues) — OK for Heisenberg
3. d_{pf} = 0 (no planted-forest corrections) — OK
4. only d_Cech + d_loop survive — OK
5. the genus-2 shell decomposition reduces to "Theta^{(2)}_{loop ∘ loop}, the iterated BV operator applied twice"

Claim 5 is the weakest link. The "genus-two shell decomposition" is cross-referenced to `const:vol1-genus-two-shells`. In the Heisenberg case, this decomposition has ONE surviving term. But the justification is "neither the separating/loop shell nor the planted-forest shell contributes." The separating shell (two genus-1 pieces glued) is a genuine contribution for non-abelian CohFTs; claiming it vanishes for Heisenberg requires the argument that the genus-1 free energy F_1 = k/24 produces, at the separating node, (k/24)^2 which should be ZERO mod the quadratic/kappa-linear decomposition. The chapter does NOT argue this. The whole genus-2 collapse at lines 58-66 is ASSERTED, not derived.

**F5-C2. "obs_g = k · lambda_g (UNIFORM-WEIGHT)" applied at g=2 in the F_2 derivation (line 1549-1553).** The tag is at line 1628. But for Heisenberg the weight is uniformly 1 (one current of weight 1), so UNIFORM-WEIGHT is automatic. Chapter does not say "Heisenberg is uniform-weight because the single current has weight 1", which would close the loop. AP32 formally compliant; practically a load-bearing omission.

### MODERATE

**F5-M1. "boundary algebra of U(1) CS is Heisenberg" (line 2797-2814).** The remark correctly states the KM extension for abelian g is Heisenberg, and marks the odd-current algebra as a DIFFERENT object. Good recovery. But the remark's parenthetical about "the Kac-Moody extension g_D^kappa for commutative g is the Heisenberg Lie* algebra" is technically correct but uses "Lie*" without defining it. A reader who doesn't know BD's Lie* language will be lost.

**F5-M2. The "kappa = k (from bracket)" entry for odd current in the table (line 3608) vs "kappa = k (from curvature)" for Heisenberg.** Both equal k but via different mechanisms. The chapter's explanation (line 3362-3368) is correct: Heisenberg has d_bracket=0, d_curvature=k; odd current has d_bracket=k, d_curvature=0. Total d_res = k in both cases. OK, but AP39 / AP71 reader might ask: why do these produce the SAME kappa? The answer is that kappa is the arity-2 collision residue regardless of which pole order produces it. Chapter should say this explicitly.

---

## Examiner 6 — Editor (inevitability / concision)

### MODERATE

**F6-M1. The CS hinge section (2817-3318, ~500 lines) is too long and repeats itself.** Section 2820-2850 states the plan; 2848-2957 executes step 1; 2959-3071 executes step 2 (with the perturbative derivation); 3073-3188 executes step 3 (bar complex as interval amplitude); 3190-3318 executes step 4 (4d-3d-2d cascade). Each subsection opens with a paragraph that restates the previous one. Recommend compressing to ~300 lines by removing the "we will now..." transitions.

**F6-M2. Redundant tables.** The Heisenberg vs sl_2 table (2737-2760) and the Heisenberg vs sl_2 vs odd-current table (3565-3630) overlap. The second supersedes the first. Consider removing the first.

**F6-M3. "This is the Gaussian archetype in its sharpest form" (line 63)** is the third occurrence of this phrase in the first 70 lines (lines 23-26, 63-66, and the chapter title). The chapter is telling the reader the same thing three times.

**F6-M4. AI-slop sweep.** Grep for "notably|crucially|remarkably|interestingly|furthermore|moreover|delve|leverage|tapestry|cornerstone": chapter is clean (manual check of text reveals none in the prose). Good.

**F6-M5. Em-dashes:** grep finds none in this file. AP107 compliant.

### MINOR

- **F6-m1. Convention duplication.** Line 183 "We begin with the Heisenberg algebra" is redundant with lines 8-11 which already say the same thing.
- **F6-m2. Three definitions of Heisenberg OPE.** Lines 192, 1233, 2914 each define `alpha(z) alpha(w) ~ k/(z-w)^2`. The last two should reference the first.

---

## Cross-Examiner Synthesis

**AP126 residual audit.** Grep for `r(z) = k/z`, `r(z) = k Omega/z`, `k/(z-w)^2`: the chapter has 12 r-matrix formulas, ALL of which carry explicit level `k` prefix. AP126 clean. Good.

**AP132 (augmentation ideal).** Line 3113-3115 correctly uses `\overline{cH_k} = ker(epsilon)` and cites AP132. Good.

**AP125 (label-environment match).** Spot checks: `thm:frame-heisenberg-bar` (theorem env — OK), `prop:frame-arnold` (proposition env — OK), `rem:...` (remark env — OK). Labels are consistent with environments. Good.

**AP1 (kappa discipline).** Every kappa formula in the chapter is Heisenberg-specific (kappa = k). The chapter does NOT write down the KM formula in the main body; it appears only in Remark `rem:cs-hinge-ap1-level` (line 2934), `av`-map discussion (line 3551), and the big comparison table (3607), all correctly showing `dim(g)(k+h^vee)/(2 h^vee)`. AP1 compliant.

**AP136 (H_N vs H_N - 1).** Not applicable — W_N kappa formula doesn't appear in this chapter.

**AP130 (fiber vs base).** Line 1418 writes `c_1(det(R pi_* F_k))` which lives on M_g — good. Line 1534-1536 correctly distinguishes "sections of omega_Sigma" (fiber) from "2-forms on moduli" (base). Line 1568 `lambda_g = c_g(E) in H^{2g}(M_g)` — base. OK.

**AP32 (uniform weight tag).** Tag present at lines 1628, 1777, 4215. Not present at the displayed Theorem D panel (line 177) — MINOR.

**AP86/AP88 (Swiss-cheese).** Section 2338-2392 applies SC to sl_2 without explicitly invoking the one-color -> two-color promotion. MODERATE F2-m1.

**Wave 5-3 physical derivation tagging.** Every physical derivation in the CS hinge (lines 2817-3318) is marked either as a `\begin{heuristic}` (lines 3014, 3097, 3244) or as prose prefixed by "physical derivation, not a theorem" (line 2831-2833). The tagging is HONEST — no fake theorems. Good.

**Wave 5-3 residual heuristics.** Three heuristics are added: `heur:cs-hinge-collision-bar`, `heur:cs-hinge-bar-equals-interval`, `heur:cs-hinge-cascade`. Each carries `\ClaimStatusHeuristic`. AAP4 compliant. Good.

---

## Findings Summary

| Severity | Count | IDs |
|----------|------:|-----|
| CRITICAL | 6 | F1-C1, F1-C2, F2-C1, F2-C2, F3-C1, F3-C2, F3-C3, F5-C1, F5-C2 (9 items grouped as 6 themes) |
| MODERATE | 11 | F1-M1..M3, F2-M1, F2-M2, F3-M1..M3, F4 minor-none, F5-M1, F5-M2, F6-M1..M3 |
| MINOR | ~12 | F1-m1, F1-m2, F2-m1, F2-m2, F3-m1, F3-m2, F4-m1, F4-m2, F6-m1, F6-m2 |
| NITPICK | none |

**Top 6 CRITICAL items (ordered by load-bearing-ness):**

1. **F5-C1 (genus-2 shell collapse asserted without proof).** The opening claim (lines 38-66) that only one term survives in the genus-2 shell decomposition is not derived in-chapter. Either derive or pull the claim to a cross-referenced construction.

2. **F3-C1 (CS propagator derivation compressed to one sentence).** "A short calculation yields J J ~ k/(z-w)^2" hides the Green's-function derivation. Cite Costello-Gwilliam or give the actual computation.

3. **F3-C2 (propagator = k · partial_z eta is ambiguous).** The one-form/kernel conflation is AP117-adjacent. Fix the formula or clarify what partial_z eta means.

4. **F2-C1 (Grav = HyCom^! overstated for chiral setting).** The chiral bar-cobar uses log-FM forms on a curve, which is strictly richer than the combinatorial Grav/HyCom duality. Clarify as analogy.

5. **F3-M2 (holomorphic-topological twist vs ordinary CS).** The 4d N=2 HT twist gives holomorphic CS, not topological CS. Fix the cascade.

6. **F1-M2 (degree-≥3 vanishing is hand-waved).** The one-sentence proof conflates chiral bar with classical Lie algebra bar (AP63-adjacent). Expand or cite.

## Verifications passed

- F_g values (g=1..6) reproduced exactly from Faber-Pandharipande
- hat-A(ix) = (x/2)/sin(x/2) confirmed symbolically
- Vir c(k)+c(-k-4) = 26 at k=0, 1 confirmed
- F_2 = k · 7/8 · (1/30)/24 = 7k/5760 verified
- AP126 discipline: all 12 r-matrix formulas carry explicit level prefix
- AP132 discipline: augmentation ideal used correctly
- AP125 discipline: labels match environments (spot checks)
- Wave 5-3 tagging: all three heuristics properly labeled; no fake theorems

## Items NOT found (all clean)

- No AI slop (notably, crucially, remarkably, etc.)
- No em-dashes
- No backtick numerals
- No `antml` or `</invoke>` leakage
- No bare `Omega/z` without level prefix
- No unqualified "self-dual" claims
- No iff/biconditional without converse proof

---

## Recommendation

The chapter is in good shape structurally. Wave 5-3's CS hinge is honest (tagged as physical derivation throughout) and the math identities verify. The six CRITICAL findings are load-bearing but fixable: they are sloppiness at the derivation-prose interface, not mathematical errors. Recommend a targeted rectification pass focused on:

1. Expanding the genus-2 shell collapse (F5-C1) or demoting to a conjecture
2. Replacing the one-sentence CS propagator derivation (F3-C1) with a computation or citation
3. Clarifying the propagator-as-one-form formula (F3-C2)
4. Softening the "Grav = HyCom^!" claim to "instance of operadic Koszul duality at the combinatorial level" (F2-C1)
5. Fixing the HT-twist vs ordinary-CS distinction (F3-M2)
6. Expanding the degree-≥3 vanishing proof or explicit cross-reference (F1-M2)

No CRITICAL mathematical errors found. All numerical claims cross-verified. Wave 5-3 physical-derivation tagging is honest.
