# Subregular reduction, quotient bars, and connected consumers

Candidate007 constructs actual associative algebra and induced-module bar comparisons after the full four-generator subregular C2 quotient. It also proves the exact first obstruction to an ordinary normal-product bar on the unreduced vertex carrier. This is a new candidate for independent mathematical review. The inherited native book remains unaccepted.

The parent candidate006 is immutable: its final manifest SHA-256 is `59f34c00e17d9e0044d8769290ce7d5dfd55f524f2010a23f5f172c477b83e7d`, and all 755 recorded files are checked at entry and exit. The complete candidate006 review is retained in `prior-reviews/`; the complete earlier F1–F8/R1–R3 and candidate004 integration findings are retained in `prior-rejections/`. They are evidence to reconcile, not mathematical premises.

## Exact mathematical boundary

The polynomial universal vertex inclusion W_R → C_R from candidate006 is retained with its full proof. It holds over R=C[k] and every complex fiber, including k=−3. The only change to that proof is the Kac–Wakimoto good-grading locator from pp.3–5 to pp.3–6. The conformal vector T and its central charge still require inversion of k+3. No new argument assigns T to the critical fiber.

The new source `cbc/chapters/theory/subregular_bar.tex` proves:

1. No unital W_0 → V^0(sl3) exists: the affine augmentation would compose to a W_0 augmentation, contradicting J_(1)J=1. A universal W_k vertex augmentation exists exactly at k=−3/2. The two reflected current coefficients sum to −2, so both reflected factors cannot augment.
2. At every level, the normal-product associator on J,J,U is exactly 2:(∂J)U:, nonzero by the polynomial PBW theorem. Hence the ordinary normal-product tensor-bar differential fails to square to zero at length three, including at the uniquely augmentable level. This is an obstruction to that specified operation, not a disproof of every curved chiral construction.
3. The C2 quotient of the complete affine–ghost carrier has an explicit polynomial/exterior coordinate change to A_R⊗Q_R, where A_R=R[J,U,p,v0] and Q_R consists of four contractible even/odd pairs. The differential and Euler contraction prove a Poisson quasi-isomorphism A_R→K_R and identify R_W with A_R without assuming that C2 preserves arbitrary quasi-isomorphisms. The reverse projection is associative but is not Poisson.
4. The specified associative augmentations produce strict direct-sum bar coalgebra quasi-isomorphisms B(A_R) ↔ B(K_R). Their cohomology is the exterior algebra on four degree −1 generators, with ranks 1,4,6,4,1. All maps, signs, representatives, and the free-resolution proof are given.
5. For every differential A_R-module M, there are explicit compatible module-bar quasi-isomorphisms B(A_R;M) ↔ B(K_R;K_R⊗_A M). The A_R-linear contraction and finite tensor length prove this without boundedness or completion. This does not identify arbitrary affine vertex modules with those induced modules.
6. The quotient loses first products: q(∂J)=0 while q((∂J)_(1)U)=−U. Thus the bar result cannot be transferred back to the unreduced vertex carrier merely by citing C2.
7. The central-charge base is the finite rank-two algebra C[c,t]/(6t²+(c−25)t+24), isomorphic to C[t,t⁻¹], with discriminant (c−1)(c−49). Neither sqrt(c) nor adic completion is forced.
8. Exact sl4 centralizer calculations give the correct five even subregular generators of weights 1,2,2,2,3 and all five orbit rows. The principal/affine weight-one obstruction and a W3 vacuum obstruction exclude the specified naive tower maps.

The connected native module section now states the actual induced-module theorem. Its direct callers distinguish this quotient carrier from a global or reflected chiral comparison. Companion proofs show why exactness alone does not preserve indecomposables, projectives, or Ext, why an Euler relation does not construct an exact triangle, and why affine Sugawara→principal DS projection fails at k=0 (third products 0 and −15). A local Virasoro residue is recomputed with its correct factorial. The hierarchy proposition now contains the actual associative comparison and the full-carrier obstruction.

These results do not prove arbitrary-nilpotent reflected Koszul duality, completed principal towers, arbitrary vertex-module compatibility, conformal-block descent, or genus-two Hodge normalization. Their exact missing constructions remain stated in mathematical language. Independent pre-existing claims elsewhere in the native book remain unaccepted; `rejection-disposition.md` gives the complete boundary.

## Evidence and reproduction

Run from the owned worktree:

```
/opt/homebrew/bin/python3 reports/research/cbc_native026/candidate007/check_modes.py
/opt/homebrew/bin/python3 reports/research/cbc_native026/candidate007/check_bar.py
python3 reports/research/cbc_native026/candidate007/build.py subregular
python3 reports/research/cbc_native026/candidate007/build.py proof
python3 reports/research/cbc_native026/candidate007/build.py native
```

The mode engine passes 347 exact identities (300 basic generator/vacuum identities and 47 composite identities). The new computation passes 1,744 identities, including the associator, all C2 brackets, contraction monomials through factor degree four, polynomial bar identities, exterior cycles, differential module-bar signs, and independent sl4 centralizer matrices. These finite checks do not replace the general written contraction and resolution proofs. Python is 3.14.6 and SymPy is 1.14.0.

Primary sources are pinned in `primary/provenance.json`: Kac–Wakimoto math-ph/0304011v2; Arakawa 1005.0185v4; Arakawa 1605.00138v2. The latter gives the C2 functor, affine quotient, and charged-ghost quotient with exact page and proposition locators. No novelty claim is made.

`source-manifest.json` and `source.diff` bind every source byte and its parent. `build-input-closure.json` binds the recorded TeX inputs, fonts, build records, and PDFs. `render-binding.json` and `render-inspection.json` specify the inspected pages. `final-manifest.json` binds the complete closure. No changed byte carries a prior whole-candidate verdict.

A preliminary native build detected an unclosed inherited remark boundary after a region replacement. The exact old surrounding paragraph was restored, and the full native build was rerun to convergence. Preliminary logs are retained separately. Both inherited overfull paragraphs were given line-break changes; they no longer produce overfull diagnostics. Ten inherited missing citations and one missing reference remain explicit native blockers. No missing citation was filled merely to make an unsupported claim appear verified.

The old affine sl2, relative P1, unital P1, Virasoro, elliptic propagator, finite BV, and global proof bodies are preserved. The preservation manifest records their hashes. No old candidate was changed, no stage/commit/push was performed, and no central PDF or external viewer was used. No child was spawned. The requested mathematical controls are gpt-6-astra and ultra; matching exposed metadata was reported by the coordinator. This local tool context supplies no independent backend attestation.
