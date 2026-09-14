# CBC subregular reduction: exact review

## Verdict

**MATHEMATICAL PASS, bounded to the new subregular construction and its corrected formulas.**
The inclusion in `thm:cbc27-subregular-map` is a strict unital vertex quasi-isomorphism over C[k].
Its proof supports every complex specialization, including k=-3.
The localized Bershadsky–Polyakov products and binary collision comparison also pass.

**NATIVE UNION REJECTED.**
The frozen book contains contradictory copies of the subregular claims, unsupported downstream equivalences, and inherited build failures.
The new theorem does not certify the whole book or any previously reviewed module.
No publication, integration, or release is authorized by this review.

## Frozen candidate

Repository worktree: `/Users/raeez/mathematics/worktrees/frontier-cbc-native-026-20260914`.
Base commit: `cb6e88263f4bb75ef5c1d9db911f61ca5d3d4d9c`.
Source prefix below: `research-candidates/cbc_native026/candidate006/`.

- Final source manifest: `reports/research/cbc_native026/candidate006/source-manifest.json`.
- Source-manifest SHA-256: `d116f3c5208ac9e1b7437b391b8cbc011b33e2ff02a1a3a4e72ef1798a990f00`.
- Main theorem source: `cbc/chapters/theory/subregular_ds.tex`.
- Main theorem source SHA-256: `e7ba05abec42d37ed47cae9346bc09b0289ff1837ed68756bb3019315cbe8da0`.
- Final artifact manifest: `reports/research/cbc_native026/candidate006/final-manifest.json`.
- Artifact-manifest SHA-256: `59f34c00e17d9e0044d8769290ce7d5dfd55f524f2010a23f5f172c477b83e7d`.

All 87 source hashes and all 755 artifact-manifest hashes were checked directly.
Seven source paths differ from candidate004.
The parent manifest has SHA-256 `ebf6a58cbe681cae5189bf11b776d689af9a061b31bc77ff3c2071f7b96b2d37`.
Its 85 source files were also verified before reproducing the baseline.

The initial source manifest was `3f182388ee1a2cf49c0c9a2652b9cad8f35d2b6c5b27daf1d836f1d5655012bc`.
The successor changes only the layout of the differential display in `subregular_ds.tex:85–93`.
`formatting-successor.diff` preserves that exact comparison.
The earlier source copy remains in `frozen/` and the successor in `frozen002/`.

Required runtime controls are gpt-6-astra with ultra effort.
Observed model and effort metadata are unavailable and remain unverified.
No configuration mismatch was observed.
No descendants, target writes, staging, commits, pushes, central PDF writes, or standalone PDF application launches occurred.

## Blocking native findings

### F1. False inclusion into the universal affine algebra

**SERIOUS / VERIFIED_DEFECT.**
`cbc/chapters/examples/w_algebras_framework.tex:111`, `rem:ds-hierarchy-summary`, displays

```
V^k(sl3) ⊃ W^k(sl3,f_min) ⊃ W3.
```

The first asserted inclusion is impossible at k=0 as a unital vertex map.
The universal affine algebra V^0(sl3) has a unital augmentation to C: send every affine current to zero.
The defining affine brackets permit this map because their level term vanishes.
Any unital vertex map W^0(sl3,f_min) → V^0(sl3) would therefore give an augmentation of W^0 to C.
However, the independently checked identity J_(1)J=1 holds in W^0.
Every positive vertex product in C vanishes, which gives the contradiction 0=1.

This is an exact counterexample at a noncritical level.
It does not attack the new map into V^k(sl3) tensor the charged ghosts.
That target has no augmentation, since b_(0)c=1.
The new theorem therefore uses the necessary carrier correctly.

Smallest remedy: replace the displayed inclusions by the actual reduction operations and the proved inclusion into the affine–ghost complex.
A stronger inclusion statement needs a separate map and a domain that survives the k=0 obstruction.
Acceptance requires propagation to every claimed affine/subregular hierarchy and a fresh review of the changed bytes.
Native PDF page 998 displays this inherited defect.

### F2. A direct BP duplicate has the wrong parity and coefficient construction

**SERIOUS / VERIFIED_DEFECT.**
`cbc/chapters/theory/chiral_koszul_pairs.tex:1820–1840`, `ex:bp-algebra`, calls G± fermionic.
It then requires square-root coefficients and an adic completion for this algebra.
Its summary table at line 1867 repeats the square-root completion claim.

In the explicit model, U and V are even: each term contains an even affine state or an even ghost product.
Their PBW symbols are nonzero, so parity cannot be changed by treating them as zero states.
All four generators and the reduction map exist over C[k].
After inverting k+3, every displayed BP structure coefficient is rational in k.
No completion enters the construction or its cohomology proof.

Changing from k to the central charge is a separate coefficient problem.
For t=k+3, c=25-6t-24/t gives

```
6t^2+(c-25)t+24=0,
Discriminant=(c-1)(c-49).
```

This does not establish the claimed necessity of C[c^(1/2)] or of an adic completion.
The cited example must name its actual coefficient construction before asserting one.

Smallest remedy: use the four even generators, the polynomial family, and the localized conformal presentation with their stated domains.
Treat any further coefficient change or completion as a separate construction.
The false parity is visible in the native PDF on page 594.
This file is unchanged by candidate006 but belongs to its active source closure.

### F3. The stronger reflected equivalence survives downstream as a proved proposition

**CRITICAL / VERIFIED_DEPENDENCY_GAP.**
`cbc/chapters/examples/w_algebras_deep.tex:1445–1502`, `prop:ds-koszul-hierarchy`, claims the reflected Koszul equivalence for all nilpotents.
Taking sl3 and the self-transpose orbit (2,1) recovers the stronger BP equivalence that the new remark leaves unconstructed.

The proposed proof invokes `thm:ds-koszul-intertwine` at lines 1468–1482.
Its actual declaration in `cbc/chapters/theory/chiral_modules.tex:4228–4263` is a module/coalgebra square at noncritical level.
It supplies neither the asserted arbitrary-nilpotent orbit transformation nor a map between the two reflected BP vertex carriers.
Its proof at lines 4286–4308 also requires a comparison between taking cohomology and the completed or configuration-dependent bar construction.
Commuting differentials alone do not supply that comparison.

The new strict inclusion is at one level and has the full BRST complex as target.
It cannot fill this missing reflected-level arrow.
The central-charge obstruction concerns conformal vertex isomorphisms only.
It does not refute an independently defined curved Koszul equivalence.

Smallest remedy: preserve the reflected theorem target in the research record and construct its actual coalgebra/vertex comparison with all hypotheses.
No whole-book acceptance can treat the new same-level reduction map as that construction.
Native PDF page 1073 still displays the stronger proved proposition.

### F4. Inherited build and manuscript-boundary defects remain

**MODERATE / VERIFIED_DEFECT.**
The native build has ten undefined citation keys, one undefined reference, and two overfull boxes after convergence.
The keys are WW27, Ahlfors79, Mum70, Pont66, Rudin62, Muk81, Olsson16, Tohoku, TUY89, and BerFres04.
The undefined reference is `def:bar-construction`.
The overfull widths are 3.84515pt and 12.93716pt.
Every remaining native diagnostic is present in the reproduced candidate004 baseline after page-number normalization.
The candidate removes the earlier 10.30968pt overfull field display.

The unchanged paragraph `w_algebras_deep.tex:163–175`, headed “Frontier discipline,” narrates the section's work organization.
It appears beside the corrected BP computation on native PDF page 1059.
That surrounding prose does not satisfy the manuscript boundary.
The added mathematical section and changed formula paragraphs introduce no such material.

These findings preserve the existing unaccepted status of the native book.
They are not evidence against the new subregular theorem.

## Independent derivation and its limits

`independent-first-stage.md` was recorded before reading the candidate proof.
It derives an integral sl3 BRST model with two commuting constraints and no neutral ghosts.
The classical constraint quotient has four polynomial invariants and two translation coordinates.
Its jet complex contracts by the polynomial Euler homotopy.
The predicted integral PBW dimensions through weight three are 1,2,7,16.

The first stage uses f=E31 and the minus-character constraint convention.
The candidate uses f=-E21 and the plus-character convention of Kac–Wakimoto.
Permuting matrix indices 2 and 3 and exchanging the ghost pairs identifies the displayed constraint complexes.
The sign convention for the nilpotent character changes at this comparison.

The actual quantum low-weight calculation was performed after reading the candidate's representatives.
It is an independent implementation, not a blind first-stage derivation of those representatives.
This distinction limits the independence claim and is retained here explicitly.
No candidate computation code was imported.

`independent_modes.py` derives affine brackets from 3-by-3 matrices and charged-fermion brackets from the Clifford relations.
It stores vacuum states as ordered negative-mode words over Q[k].
Normal-product modes use the iterate formula with finite energy bounds.
It checks 101 exact identities, all passing:

- affine and fermion mode calibration and translation;
- every displayed BRST differential and D squared on every generator;
- J,U,P,V closure, both contractible pairs, and all three ghost normal-order identities;
- JJ, JU, JV, JP and UV products;
- the exact stress homotopy;
- denominator-cleared TJ, TG±, TT and equal-charge products.

The program uses Python 3.14.6 and SymPy 1.14.0.
Its SHA-256 is `a0b5a994a29774606e8a7b2d2a485c37b032bf18c5d7fd7bc98076fdaea8091e`.
The retained candidate computation has 347 entries marked passed, but those entries are not the acceptance argument.

`low_weight_cohomology.py` constructs the actual C-minus modes in weights zero through three.
It verifies independence of the chosen basis, D squared, and the differential ranks.
At generic k and at k=-3,-3/2,-1,-1/2,0,2, its cohomology has dimensions 1,2,7,16 in degree zero.
Every tested positive cohomological degree vanishes.
These are exact finite checks, not a proof of the all-weight or all-level statement.

## Proof of the general bridge

The deciding general argument is the explicit filtered contraction, not the finite calculations.

For the first filtration, the degrees are 0 on a,e,b_i, 1 on h,j,u,v,c_i, and 2 on A,B.
Derivatives preserve filtration degree.
Every generating singular bracket lowers total degree.
The associated graded is therefore the free polynomial/exterior jet algebra over C[k].
The modified-current substitutions and the translation a↦a-1 are invertible polynomial substitutions in that algebra.
Thus normally ordered multiplication C-minus tensor C-plus → C is a filtered linear isomorphism.
Its associated graded inverse lifts by induction because every state has finite nonnegative degree.
D is an odd derivation, so this linear isomorphism respects the tensor differential.
No claim that it is a vertex tensor decomposition is needed.

C-plus is the polynomial Koszul complex with Db1=a-1 and Db2=e, including all jets.
The homotopy b1∂_(a-1)+b2∂_e, summed over jets, has anticommutator equal to factor count.
Every sum is finite on an algebraic state.
Division by a positive integer is valid over C[k] and every complex specialization.
This contracts C-plus onto its unit.

For C-minus, assign degree 1 to H,J,U,X,c_i and degree 2 to A,B, including all jets.
The top differential preserves these degrees and sends H to -2c1 and X to c2.
The triangular substitutions

```
p=A+H^2/4+UX,
v0=B-HX/2-3JX/2
```

make p and v0 closed and retain an invertible polynomial coordinate system.
The remaining complex is the polynomial de Rham complex in H,X and their jets.
Its homotopy is -H∂_c1/2+X∂_c2, divided by positive factor count.
It contracts onto the polynomial jets of J,U,p,v0.

The explicit cycles J,U,P,V lift these four generators.
Their leading symbols prove linear independence of ordered monomials.
A degree-zero cycle has an invariant leading symbol, since C-minus has no negative cohomological degree.
Subtracting its unique polynomial lift lowers filtration degree and terminates.
For a positive-degree cycle, the graded homotopy gives a preimage of the leading symbol.
Subtracting its differential also lowers degree and terminates.
This proves cohomology concentration and the asserted PBW basis without a convergence assumption on infinite products.

All operations use only integer inverses and 1/2.
They work directly over C[k] and in every fiber, so no specialization argument can hide torsion.
The proof uses algebraic direct sums throughout.
A completion or inverse limit would require a new argument and is not asserted here.

## Products, stress tensor, and boundary cases

The mode calculation verifies the k+3 terms in DA and DB and the k+2 terms in P and V.
It verifies the cubic coefficient with G-minus=-V and both G fields even.
The stress identity holds as an exact state equation before passing to cohomology:

```
(k+3)(L_full-T-(1/2)∂J)=D(:b1 A:+:b2 B:).
```

T itself is defined only after inverting k+3.
The denominator-cleared equation remains a polynomial identity, but does not define T at k=-3.
Its numerator has coefficient one on the PBW generator P and remains nonzero in that fiber.
Thus the displayed denominator has no removable polynomial cancellation.
The conformal charges and current anomaly agree with the independently derived integral grading.
The conformal identities become strict in W because it has no degree-zero boundaries inside C-minus.
The PBW charge/weight bound excludes the remaining positive equal-charge products.

The scalar products are κ_J=(2k+3)/3, (k+1)(2k+3), and c/2.
They vanish simultaneously only at k=-3/2.
At k=-1/2 their values are 2/3,1,1/5.
At k=-3/2, the universal generators still have independent PBW symbols.
No claim concerning their survival in the simple quotient is made.

Writing t=k+3 gives c=25-6t-24/t.
Reflection sends t to -t, hence the charge sum is 50.
Equality occurs exactly when t squared is -4.
The text correctly states only a necessary condition for a conformal isomorphism at those exceptional parameters.

## Binary chiral comparison

The source localization, target principal parts, both connections, right-module conversion, orientation, and residue normalization are stated explicitly.
For the z connection, differentiation of gY(a,ξ)b equals the sum of the base derivative and Y(∂a,ξ)b.
For the w connection, the derivative of g(w+ξ,w), the term -∂ξ, and the translation commutator cancel the first-state derivative.
The remaining expression is the stated derivative on the second state.
Thus the principal-part map respects both connections.

Every Laurent coefficient uses the same vertex mode before and after the inclusion.
This proves the collision square, including the regular products selected by meromorphic coefficients and the vacuum terms.
Vertex truncation makes each principal part finite.
Tensoring over C, localization, and the stated algebraic direct sum preserve quasi-isomorphisms.
The standard mapping-cone exact sequence proves the cone comparison.
No completed bar, second differential, coordinate descent, nodal-curve gluing, or reflected duality is inferred.

## Primary sources

Both PDFs were downloaded directly from arXiv with pinned versions.
Their hashes and extraction commands are retained in `primary/provenance.json`.

1. Kac–Wakimoto, *Quantum reduction and representation theory of superconformal algebras*, arXiv:math-ph/0304011v2.
   Section 1, pp. 4–6, supplies the affine/Clifford modes, the plus-character BRST field, and the good-pair convention.
   Theorem 4.1 and its proof, pp. 10–12, supply the vacuum PBW and cohomology theorem.
   Remark 4.1 on p. 12 identifies the closed degree-zero subalgebra realization.
   The present polynomial proof supplies the integral-base and critical-level assertions directly.
   URL: https://arxiv.org/pdf/math-ph/0304011v2
2. Arakawa, *Rationality of Bershadsky–Polyakov vertex algebras*, arXiv:1005.0185v4.
   Section 2, p. 2, gives the universal BP products and the improvement L=T+∂J/2.
   Its separate notation for the universal algebra and simple quotient matters at exceptional levels.
   The candidate uses the universal carrier consistently.
   URL: https://arxiv.org/pdf/1005.0185v4

The candidate's p. 3–5 locator for the good-grading convention is slightly short: the explicit definition of “good” appears on p. 6.
The displayed centralizer criterion already appears on p. 5.
This is a minor navigation issue, not a missing mathematical hypothesis.

## Build, render, and changed consumers

Commands, environment, input closures, pass logs, versions, and hashes are retained in the build JSON files.
The fixed environment is SOURCE_DATE_EPOCH=1789344000 and FORCE_SOURCE_DATE=1.
The toolchain is pdfTeX 3.141592653-2.6-1.40.27, TeX Live 2025.
The builds disable shell escape and use the recorder.

| Target | Pages | Convergence | Result |
|---|---:|---|---|
| Candidate004 comparison baseline | 47 | 4 passes | One inherited overfull display |
| Candidate004 native baseline | 1666 | 5 passes | Inherited citations/reference and three overfull boxes |
| Candidate006 subregular | 8 | 4 passes | No warnings |
| Candidate006 comparison | 53 | 5 passes | No warnings |
| Candidate006 native | 1672 | 5 passes | Inherited citations/reference and two overfull boxes |

The three builds read 86 of the 87 manifested source files.
The extra manifested source is the unused `proof/main.tex` entrypoint.
No unmanifested non-TeX-Live source input was observed.

The exact candidate PDFs have these SHA-256 values:

- Subregular: `bd00b563fbf3aacec55d9f004e16282a264106a0a0771bc431909793409d41f3`.
- Comparison: `513f21035368926c1232c78ffffb5dfd4ee7e9608e300254c7a7f813ce0ccfff`.
- Native: `93e3574591c2f32831c9060d488c6cff2eeb01c82c415213b4850ff00bb1eb30`.

Their extracted text is identical to the independent builds.
All 46 inspected page PNGs also match the exact candidate renders byte for byte at 100 dpi.
`rendered-pages.json` lists all pages.
The review covers all eight subregular pages, comparison pages 32–34 and 45–53, and 26 native pages containing changes or their transitions.
It includes the formerly colliding native equation on page 992.
No clipping, equation-number collision, missing glyph, or overlap survives on the changed displays.

The seven changed paths were inspected against their exact parent hashes:

- `cbc/chapters/theory/subregular_ds.tex`: complete new construction, reviewed above.
- `cbc/chapters/examples/w_algebras_framework.tex`: inserted construction, corrected parity, same-level map, critical domain, reflection obstruction, and orbit table.
- `cbc/chapters/examples/w_algebras_deep.tex`: corrected generators, PBW character, scalar products, and exceptional levels.
- `cbc/chapters/theory/unital_p1_chains.tex`: layout only, preserving every field convention.
- `cbc/bibliography/references.tex`: two verified primary citations.
- `proof/comparison_main.tex`: includes the new source and those two citations.
- `proof/subregular_main.tex`: a standalone entrypoint for the exact source.

The changed formulas are mutually consistent.
The newly added prose and PDF metadata contain no project-management or private-repository references.
The inherited native findings above prevent a whole-file or whole-book pass for the surrounding consumer material.

## Residual obligations and handoff

The new theorem has no surviving mathematical proof obligation within its declared universal, algebraic, same-level scope.
The native union still requires F1–F4 repairs and independent review of the resulting source and artifacts.
A curved reflected Koszul comparison remains a separate theorem target.
Coordinate descent for this subregular model, completed chiral bars, nodal gluing, and any second differential remain outside this result.
The review does not recertify the prior Virasoro, affine, relative, or global modules.

All changes made by this review are under its assigned directory.
`review-evidence-manifest.json` inventories their hashes.
The two checking programs, their exact outputs, both source freezes, both baseline builds, three successor builds, primary sources, and rendered pages remain available there.
