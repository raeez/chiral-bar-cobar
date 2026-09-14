# Virasoro operator and comparison-consumer construction, candidate002

The full Virasoro operator construction is unchanged from candidate001. This candidate repairs the direct comparison-consumer union identified by the exact review and supplies proofs of the augmentation, relative-cohomology, and coordinate-transition obstructions. It does not construct an alternative chiral target, a geometric symbol map, or a string amplitude. Root acceptance is pending.

## Exact boundaries and preservation

The source is `research-candidates/cbc-virasoro021/candidate002/`; evidence is this `candidate002/` report directory. The worktree is `/Users/raeez/mathematics/worktrees/frontier-cbc-virasoro-021-20260914`, branch `intake/cbc-virasoro-021-20260914`, principal base `18966d676a86720fc4b2919c82a9fb12892a0a0d`. Nothing has been staged, committed, or pushed.

Candidate001's complete 1,313-file manifest scope plus its manifest is preserved under the sibling `archive001/`, with exact bytes, no live symlinks, files mode 0444 and directories mode 0555. `archive001.json` records all 1,314 archived rows. Its original manifest SHA-256 is `41e2346d90645d1d45f7deff0dd956f2ec368cfd293972734b7f038e053a0468`. Original live001 files also remain unchanged. The original PBW020 preservation, complete build closures, failed routes, and review evidence remain inside that exact archive.

The unchanged standalone source `proof/virasoro_square.tex` has SHA-256 `017765248b4eccab1a14a20b014d95b5ddf277459945f9995ab7d90284c8efa0`. Its eight-page PDF is `virasoro-operator.pdf`, SHA-256 `939dc34c716bf6a3e9690f449b22dcece8b0c27624c41bb2833d883b673ae88e`. Its complete original proof input closure and all eight inspected rasters are preserved in archive001. The native insertion agrees exactly after heading/label translation.

## Mathematical result

For a nonzero restricted even Virasoro module with central charge C, conformal ghost vacuum, and algebraic finite-state carrier, the unchanged proof gives

`Q_t^2 = sum_(n>0) [(C-26)(n^3-n)/12 - 2tn] c_-n c_n`.

Absolute nilpotence is equivalent to C=26 and t=0. For nonnegative matter weights the actual zero-intercept relative carrier is the three-term complex `M0 -> M1 -> M0` with maps `L_-1,L1`; it is square-zero for every central charge. This is an operator identity with its full domain, not a scalar anomaly diagnostic.

The new native proofs establish:

1. For every nonzero unital V, the vertex algebra `V tensor bc` has no unital augmentation to the trivial vertex algebra: `b_(0)c=unit`. For Vir26 the separate matter equality is `T_(3)T=13 unit`. Residues against `dt` and `t^3 dt` detect these products on a disk, including among regular coefficients times logarithmic forms. The linear vacuum projection and quotient by the vacuum do not repair the original collision operations.
2. For universal Vir26, the zero-weight absolute basis is `e=Omega,u=c0 Omega,v=c_-1 c1 Omega,w=c_-1 c0 c1 Omega`, with `Qu=-2v` and the other images zero. Nonzero weights contract by `b0/H`. Absolute cohomology is in degrees 0 and 3; relative cohomology is in degrees 0 and 2. The relative inclusion kills the degree-two class and is not a quasi-isomorphism.
3. Under the specified coordinate convention `g_s=exp(s L1tot)`, `g_s v=v-s c0 c1 Omega` and `b0 g_s v=-s c1 Omega`. The fixed relative fiber is not preserved by the standard state-bundle transition. A different relative sheaf requires actual compatible descent or transported constraints.
4. A filtered comparison criterion on separately supplied complexes remains true with the complete split-filtration, actual graded quasi-isomorphism, and compatible Hom-correction hypotheses. The impossible augmentation-kernel target has been removed as an assignment, with its nonexistence proved explicitly. A different target is not silently declared constructed.
5. Binary compatibility is the additional typed equation `mu_bar(Phi tensor Phi)=Phi mu_pert` on actual common collision carriers. A chain isomorphism alone does not imply it.
6. Pairing transfer requires actual n-point complexes, insertion chain maps to a specified form complex, a degree-minus-one homotopy `alpha_bar Phi-alpha_BRST=d h+h d`, and a linear integration functional vanishing on exact top forms. The corrected amplitude corollary proves precisely that conditional transfer. Regularized logarithmic integration must satisfy those same existence and closedness hypotheses.

The logarithmic-basis proof also now uses `dt/(t-1)=dlog(1-t)`, so its second coefficient is B=b, consistent with its statement and residues.

## Complete direct-consumer coverage

There are 57 recorded replacement operations across seven native files. `replacements.json` preserves exact before/after strings and multiplicities; replay from archive001 reproduces all seven final files. `source001-to002.diff` is the aggregate source diff. No operator-proof byte was changed.

| Native consumer | Exact correction and final PDF pages |
| --- | --- |
| `bv_brst.tex`, comparison theorem and its immediate claims | New obstruction propositions; explicit fixed-coordinate relative state source; separate target, collision maps, normalization, descent, section functor, filtration, actual symbol, and compatible corrections. Pages 1364–1377; new propositions on 1373–1375. |
| `concordance.tex`, `rem:anomaly-scope` | Central charge proves the algebraic operator statement. All genus-zero target, descent, symbol, and correction constructions remain required. Pages 1455–1456. |
| `free_fields.tex`, algebraic string dictionary | Clause (i) explicitly imposes actual comparison data; central charge does not supply it. The remaining construction is not characterized as exclusively analytic. Pages 886–887. |
| `free_fields.tex`, amplitude corollary and its downstream integrand claims | Actual n-point insertion maps, pairing homotopy, closed integration functional, declared degree and domain. Pages 887–890. |
| `feynman_diagrams.tex`, ghost-bilinear/log assignment | Actual relative input and total-degree target required; `c0c1 Omega` is excluded. Binary comparison is an additional equation, with a counterexample to inference from a chain isomorphism. Pages 1343–1344. |
| `feynman_diagrams.tex`, compactified ternary corollaries | All four downstream reductions retain constructed-carrier, filtered-comparison, and binary-intertwining hypotheses. Logarithmic-basis sign corrected. Pages 1344–1346. |
| `concordance.tex`, Comparison 9, table row 9, V6 | Complete genus-zero carrier/map/pairing conditions and exact augmentation/coordinate obstructions; higher genus is an additional extension. Pages 1480–1484. |
| Other direct summaries in `concordance.tex` | Master-conjecture clause, both standard-tower assumptions, MC5 synopsis, local binary reduction, H7, and chiral-comparison-data remark carry the same conditions. Pages 1432–1434, 1446, 1450–1451, 1457. |
| `bar_cobar_construction.tex`, `higher_genus.tex`, `genus_complete.tex` | BV/anomaly dictionary introductions and genus-zero/genus-one summaries do not infer chain, operation, or pairing maps from the operator theorem. Pages 179–180, 377, 1411, 1421. |
| `bv_brst.tex`, final BV scope | Separate coefficient/filtered comparisons and BV operations/pairings remain required. Page 1388. |

This union does not certify surrounding KM/W Drinfeld–Sokolov claims, generic BV functor statements, all-genus claims, or the whole book. The exact review explicitly excludes those surrounding theorems from this bounded repair. In particular, inherited W/DS equivariance and exactness assertions still need a separate candidate; the conditions imposed in the amended direct summaries do not prove their existence.

## Evidence, rendering, and reproduction

The full fresh exact-review return is preserved in `inputs/exact-review001.md`. The symbol021 README, manifest, and four source files are preserved under `inputs/symbol021/`; their source hashes were checked against its manifest. `inputs/provenance.json` records the source identities. The new augmentation and coordinate calculations are informed synthesis after reading that proof, not a falsely claimed independent first stage. Their mathematical derivations appear in full in the manuscript.

`checks/finite_comparisons.py` uses Python 3.9.6 with exact exterior signs and Fraction arithmetic. It checks the finite residue and four-state calculations, coordinate failure, binary/pairing counterexamples, an actual homotopy-transfer example, and the logarithmic sign. These checks establish only their declared finite models; they do not compute a geometric target or an amplitude. Run:

```
python3 reports/research/CONSTRUCTION-2026-09-14/cbc-virasoro021/candidate002/checks/finite_comparisons.py
python3 reports/research/CONSTRUCTION-2026-09-14/cbc-virasoro021/candidate002/build.py native002-final
```

The final native PDF has 1,642 pages and SHA-256 `e8af4dd0a1fd6f9fb2ca2f4c3385ce145bce80e29ce596dd90685b2d5c4988a9`. Its last three build passes converge, with no new unresolved citation/reference identities or overfull boxes: the inherited eleven identities and two boxes remain. `native002-final-build.json` records commands, environment and toolchain. `native002-final-input-closure.json` preserves all 434 recorder inputs in content-addressed copies. `source-freeze.json` records all 70 source files.

All 76 targeted pages in `render-binding.json` were visually inspected via 39 contact sheets; final page 180 was inspected separately after its adjoining sentence was repaired. All 76 were regenerated from the final PDF. Exactly page 180 changed after the prior inspected render; the remaining 75 raster hashes are identical. No clipping, overlap, missing glyph, or project-management prose was found in the new passages. This is a bounded visual inspection, not approval of 1,642 pages of mathematics. `render-binding-intermediate.json` is historical metadata, not the final binding. `comparison_obstructions.tex` is an early drafting snippet; the actual native source and replay record are authoritative.

`runtime-controls.json` records this task's public session contexts, including resumption: `gpt-6-astra` and `ultra` were observed. This is task-control evidence, not backend attestation. No delegation occurred.

## Exact remaining construction

The original augmentation-kernel target is refuted. The first absent replacement is an actual unital chiral chain carrier with its coefficient complexes, vacuum insertions, collision maps, differential, and section functor. For the relative source, compatible coordinate descent is also absent. A candidate comparison then needs its actual graded map and compatible corrections, and a target cohomology calculation consistent with the relative classes. Binary and pairing comparisons require their additional displayed equations. The present operator theorem supplies none of those maps. Root alone may accept or integrate the frozen candidate.
