# Live Findings — Red-Team Audit

## Finding 1: Q_g Definition Ambiguity from Genus Filtration
**Status**: RESOLVED (not a real issue)
**Severity**: was TIER 2, downgraded to NON-ISSUE
**Location**: `higher_genus.tex:4757,4786` vs `higher_genus.tex:2387-2411,2447-2458`

**Analysis**: On careful re-examination, the direct sum at line 4757 IS correct. The bar complex decomposes as a genuine direct sum over genera (different moduli spaces). The differential respects genus (line 4786 is correct: collision residues on a genus-g curve stay at genus g). The apparent contradiction with the d^{(0)}, d^{(1)}, d^{(2)} decomposition in Theorem 2383 was caused by the notation collision (F2): those are Leray filtration components within a fixed genus, not cross-genus terms.

**Root cause**: F2 (notation collision) created the appearance of a problem.

---

## Finding 2: d^{(g)} Notation Collision
**Status**: FIXED
**Severity**: TIER 2
**Location**: `higher_genus.tex:2389` (Leray), `higher_genus.tex:4620` (total), `higher_genus.tex:6187,6432` (fiberwise)

**Problem**: Three distinct objects shared the notation d^{(g)}:
1. Leray filtration components d^{(0)}, d^{(1)}, d^{(2)} (Theorem 2383) — act within a fixed genus
2. Total differential d^{(g)}_total on B-bar^{(g)} — squares to zero
3. Fiberwise collision differential d_fib on a genus-g curve — does NOT square to zero

**Fix applied**:
- Line 2389: Changed misleading "encodes genus-g corrections" to "shifts Leray filtration by k base degrees"
- Added Remark rem:differential-notation (after line 2412) explicitly distinguishing the three notations: d^{(k)} for Leray components, d^{(g)}_total for the total differential, d_fib for the fiberwise collision differential
- Cross-referenced from algorithm (line 6497), explicit computation (line 6241), and MK4 proof (line 7781)
- Fixed broken ref sec:complementarity-explicit → ex:heisenberg-complementarity-explicit

---

## Finding 3: Algorithm Takes Cohomology of Curved Differential
**Status**: FIXED
**Severity**: TIER 3
**Location**: `higher_genus.tex:6476-6509` (algorithm and Heisenberg example)

**Problem**: Algorithm steps 3-5 computed d^{(g)} (fiberwise, d^2 != 0 at step 4) then took cohomology (step 5), which is undefined for non-square-zero differentials.

**Fix applied**:
- Algorithm rewritten with explicit notation: step 3 uses d^{(g)}_total (squares to zero), step 4 computes d_fib curvature (obstruction coefficient), step 5 takes cohomology of d^{(g)}_total
- Heisenberg example rewritten to distinguish d^{(1)}_total (Theorem thm:genus1-d-squared, squares to zero) from d_fib (has curvature kappa * omega_1)
- Explicit computation at line 6238 clarified: "fiberwise collision differential d_fib" with cross-ref to Remark rem:differential-notation

---

## Finding 4: Modular Koszulity — Open Question vs Verified Claim
**Status**: FIXED
**Severity**: TIER 2
**Location**: `higher_genus.tex:7514` vs `higher_genus.tex:7748-7754`

**Problem**: Line 7514 called higher-genus Koszul propagation "the key open question." Line 7754 claimed it verified for KM/Vir/W with a one-sentence physics argument.

**Fix applied**:
- Line 7514: Changed "the key open question" to "a key structural question" and added that the PBW argument of Prop gives affirmative answer at generic parameters; at special parameters remains open.
- Lines 7754: Expanded one-sentence argument to a structured paragraph: PBW filtration defined by conformal weight, propagator deformation affects only curvature (in center), associated graded E_1 page isomorphic to genus-0, E_2 collapse extends. Added explicit caveat that at special parameters (e.g., admissible levels) the property remains open.

---

## Finding 5: Eigenvalue Sign Argument Opacity
**Status**: FIXED
**Severity**: TIER 3
**Location**: `higher_genus.tex:5572-5591`

**Problem**: The V- identification claimed elements of Q_g(A!) "lie on the q = d row" of the E_2 page, contradicting the Koszul vanishing (fiber cohomology concentrated at q = 0 for ANY Koszul algebra, including A!). Three independent signs were invoked without clean justification.

**Fix applied**: Rewrote the V- identification paragraph. Removed the vacuous "q = d row" claim. New argument: (1) bar of A! uses j_!-extension, (2) Verdier involution sigma sends j_!-extended classes to j_*-extended classes, (3) the sign -1 arises from the j_! -> j_* natural transformation composed with Koszul identification, via anti-commutativity eq:verdier-ks-anticommute. Clean single-sign argument replaces opaque three-sign cascade.

---

## Finding 6: kappa + kappa' = 0 Claim for KM vs != 0 for W-algebras
**Status**: NOT A BUG (already documented in source)
**Severity**: TIER 3
**Location**: `higher_genus.tex:4033-4042`

**Analysis**: The text already contains an "Abelian case" paragraph (lines 4033-4042) documenting that the KM formula kappa = (k+h^v)d/(2h^v) has a removable singularity at h^v = 0 (Heisenberg), with kappa(H_kappa) = kappa defined directly from genus-1 curvature. Duality kappa + kappa' = 0 explicitly verified. c + c' documented as undefined because dual is curved. No fix needed.
