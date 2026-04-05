# BEILINSON PASS — FALSIFICATION VERDICTS

Principle: every item is false until independently verified. A smaller true
theory beats a larger false one. "What holds back forward progress is not
the lack of genius but the inability to dismiss false ideas."

---

## DISCARD (13 items)

### RL-13. Derived self-intersection formula
**DISCARD AS THEOREM.** The formula O(L x^h_M L) ~ Bar(A) requires derived
algebraic geometry machinery (smooth, affine, char 0) not developed in the
manuscript. The manuscript does not build derived stacks. Promoting this to
a theorem would create an unfounded dependency.
**Action:** Keep as a motivating remark in a single location (the open-sector
chapter, as a "geometric origin" aside). Never cite as a theorem.

### RL-20. Khan-Zeng dimensional constraint
**DISCARD AS GENERAL PRINCIPLE.** The (d,k) = (1,1) formula applies to freely
generated PVA gauge theories of a specific form. It does not explain why ALL
chiral algebras produce 3d data. The general mechanism is the center theorem.
**Action:** Cite in the PVA descent chapter as a consistency check; remove
from any "why 2d+1" discussion.

### V1-18. Arithmetic packet connection
**DISCARD FROM MAIN DEVELOPMENT.** The arithmetic packet connection nabla^{arith}_A
and the frontier defect form Omega_A conflate L-function theory with shadow
tower data in ways not yet independently verified. The "arithmetic comparison
conjecture" (Theta_A determines nabla^{arith}) is speculative.
**Action:** Move to a clearly labeled "Frontier/Speculative" appendix. Do not
present alongside proved results.

### V1-15. Factorization envelope adjunction
**DISCARD AS THEOREM.** The modular factorization adjunction U^{mod}_X -| Prim^{mod} is
conjectural at the modular level. The existence of U^{mod}_X is not proved.
**Action:** Mark clearly as Conjecture. Do not tag ProvedHere.

### V1-25 (partial). THQG G4, G8
**REFINE → DOWNGRADE.** G4 (S-duality) and G8 (reconstruction) rest on
physical axioms (H1)-(H4) that are not mathematical theorems. They should
be tagged Conditional, not ProvedHere.
**Action:** Change ClaimStatus tags to Conditional with explicit hypothesis lists.

### V2-13. Anomaly-completed structures
**REFINE.** Physics-motivated framework conditional on (H1)-(H4). Keep but
tag as Conditional throughout.

### V2-15. Celestial boundary transfer
**REFINE.** Ring 3 frontier material. Mark as Conditional/Frontier.

### V2-20 (bulk). 37 THQG extension files
**REFINE.** Do not let Ring 3 extensions inflate the proved core. Audit each
file for unconditional vs conditional claims. Many are tagged ProvedHere
but assume physical axioms.

---

## REFINE (27 items — need qualification, scope narrowing, or repositioning)

### RL-12. The 2d->3d mechanism
**REFINE.** The original research log stated this as "center theorem, NOT bar
ordering" with a false dichotomy. After Beilinson pass: BOTH perspectives
coexist. Bar coalgebra IS the open-sector model (deconcatenation = factorization
along R). But bar does not explain the BULK — the center does. These are
compatible, not competing. The corrected statement:
  - Bar/cobar: represents twisting morphisms and open-sector coalgebra
  - Center/Hochschild cochains: IS the acting bulk
  - The extra dimension comes from the center theorem, not from bar ordering
**Action:** Write both perspectives clearly; never set up a false dichotomy.

### RL-15. Modular twisting morphism
**REFINE.** The cooperad C^{oc,log}_{mod} is not yet constructed. This item
contains a definition-to-make, not a theorem-to-cite.
**Action:** Mark as "Construction (to be developed)" in the plan. The
construction requires RL-3 (mixed config spaces) and their compactifications.

### RL-21. Propagator factorization
**REFINE.** P(t,z) ~ Theta(t)/(2pi i z) is the abelian/free case. Nonabelian
theories have structure-constant corrections.
**Action:** Present as the Heisenberg/abelian computation, not as general.

### RL-22. Spectral Laplace transform
**REFINE.** Holds for polynomial lambda-brackets. General distributional case
needs completion theory.
**Action:** State polynomial case as theorem; flag general case as requiring
sewing envelope completion (V1-13).

### V1-2. Introduction scope narrowing
**REFINE.** Propagation incomplete. Must verify all downstream uses of
"standard examples" vs "free-field examples".
**Action:** Grep both volumes for "standard examples"; replace where needed.

### V1-5. Koszulness K-numbering
**REFINE.** K1-K12 in preface vs (i)-(xii) in meta-theorem have a known
mismatch (prior audit found 6/12 differed). Must be aligned.
**Action:** Align in the preface; add explicit cross-reference table.

### V1-8. Three-pillar Mok25 dependency
**REFINE.** Ambient D^2=0 (thm:ambient-d-squared-zero) and log clutching
depend on a single 2025 preprint. Must be isolable.
**Action:** Add explicit "If Mok25 revised:" fallback clause at each use site.

### V1-9. Arithmetic shadows
**REFINE.** Sound framework but needs Laplace-transform connection (RL-22) to
ground spectral data. Kummer motive / motivic decomposition claims need
independent verification.
**Action:** Separate proved depth decomposition from speculative motivic claims.

### V1-11. Yangians: CoHA conjectures
**REFINE.** CoHA E_1-chiral structure is conjectured, not proved.
**Action:** Tag as Conjectured; do not present alongside proved results.

### V1-14. Modular Koszul datum
**REFINE.** Reframe: Pi_X(L) encodes initial data for C_op construction.
Not a standalone six-fold datum.

### V1-25 (remaining). THQG chapters
**REFINE.** Audit each G-result for unconditional vs conditional.

### V1-32. Strict vs homotopy convolution
**REFINE.** Systematic check needed. Grep for "convolution" in both volumes;
verify each use specifies strict or homotopy.

### V2-6. Bulk-boundary-line triangle
**REFINE → PROMOTE.** Currently framed as specific to HT theories. Must be
promoted to universal consequence of the center theorem.

### V2-9. Spectral braiding
**REFINE.** Connect to Laplace transform dictionary.

### V2-11. Line operators
**REFINE.** Frame as: line operators are objects of C_op; A^!-module structure
is a presentation via a chosen generator.

### V2-22. Vol II preface/introduction
**REFINE → REWRITE.** Must present open-sector-primary perspective.

### V2-24. Ribbon/'t Hooft bridge
**REFINE.** Connect to RL-17 (modularity = trace + clutching). The 't Hooft
expansion IS the open-sector trace on the ribbon modular operad.

### V2-25. Cross-volume bridges
**REFINE.** The Hochschild bridge should be upgraded from conjectural to
consequence of the center theorem.

---

## KEEP (48 items — survived the pass)

### Tier 0: Already proved, editorial reframing only

V2-1 (A_infty-chiral axioms), V2-2 (SC operad), V2-3 (F4/F5), V2-4 (PVA descent),
V1-7 (shadow obstruction tower), V1-31 (PBW propagation), V1-6 (MC frontier), V1-8 (three
pillars — after Mok25 isolation), V2-5 (raviolo), V2-7 (brace algebra),
V2-19 (FM calculus), V2-8 (bar-cobar review), V1-28 (bar tables), V1-29
(config spaces — before expansion), V1-30 (Hochschild — before expansion).

### Tier 1: New constructions that survive

RL-1 (open sector primary), RL-2 (tangential log curves), RL-3 (mixed config),
RL-4 (mixed Ran), RL-5 (open/closed fact cat), RL-6 (boundary algebra from
generator), RL-7 (Morita invariance), RL-8 (chiral Hochschild cochains),
RL-9 (brace theorem), RL-10 (chiral Deligne-Tamarkin), RL-11 (bulk = center),
RL-14 (bar vs center), RL-16 (modular MC with clutching), RL-17 (modularity =
trace + clutching), RL-18 (cyclic = CY), RL-19 (annulus = HH), RL-23 (Jacobi
coalgebra), RL-24 (boundary-linear LG), RL-25 (complementarity as witness),
RL-26 (chiral Cartan), RL-27 (W_3 composite necessity), RL-28 (staircase).

### Tier 2: Vol I items needing integration

V1-1 through V1-4 (editorial), V1-10 (shadow growth), V1-16 (cubic gauge),
V1-17 (shadow metric), V1-19 (new claims), V1-20/21/22 (compute), V1-23
(E_1 chapter), V1-26 (CG tautological), V1-33 (depth filtration), V1-34
(genus SS), V1-35 (modular tangent complex).

---

## SUMMARY STATISTICS

| Category | Count |
|----------|-------|
| Total items | 88 |
| DISCARD | 5 |
| REFINE | 27 |
| KEEP as-is | 15 |
| KEEP with integration | 41 |
| Surviving items | 83 |
| Items requiring new writing | 22 |
| Items requiring only editorial | 34 |
| Items requiring moderate rewrite | 27 |
