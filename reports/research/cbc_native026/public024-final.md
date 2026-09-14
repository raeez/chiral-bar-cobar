**Recommendation: reject the frozen native consumer union.** The operator proof and new conditional comparison arguments are sound within their stated scope. Several native theorems and summaries still turn those conditional inputs into unconditional conclusions. Root acceptance remains required.

All source anchors below refer to `research-candidates/cbc-virasoro021/candidate002/cbc/` in the assigned worktree.

The blocking findings are:

1. **The W-algebra theorem still asserts the missing comparison.** In [bv_brst.tex:1328](/Users/raeez/mathematics/worktrees/frontier-cbc-virasoro-021-20260914/research-candidates/cbc-virasoro021/candidate002/cbc/chapters/connections/bv_brst.tex:1328), `thm:bar-semi-infinite-w` asserts an unconditional quasi-isomorphism. Its proof imports the conditional Kac–Moody theorem at line 1356 without constructing its target, symbol map, or corrections. Lines 1389–1407 additionally assume DS intertwining and exactness on the collision complexes. The new summaries incorrectly describe this theorem as already possessing those hypotheses.

   The cited Arakawa result gives vanishing and exactness for objects of `KL_k`, not for unspecified collision complexes. The native proof establishes neither category membership nor DS equivariance. See Theorem 7.1(i), p. 588, with `KL_k` defined on p. 585, in [Arakawa’s primary paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n2-p04-p.pdf). The bibliography also gives the wrong page range: `565–694` should be `565–604`.

   **Required repair:** construct the stated W target, compatible differentials, DS-equivariant comparison and valid totalization, or retain the exact unresolved construction explicitly. Adding qualifications only to summaries does not repair this theorem.

2. **The Virasoro corollary retains an unsupported cohomology calculation.** `bv_brst.tex:1414–1435`, rendered as Corollary 30.4.9 on PDF p. 1380, imports the preceding W theorem and calls its dimensions Motzkin numbers. Its cited `thm:virasoro-chiral-koszul`, at `chiral_koszul_pairs.tex:567–584`, states conditional Koszulness and the vacuum PBW product; it contains no Motzkin-dimension theorem.

   The new critical-vacuum calculation instead gives absolute cohomology in degrees \(0,3\), and relative cohomology in degrees \(0,2\). A different semi-infinite target requires its actual definition and a proved comparison before any dimension transfer.

3. **An earlier amplitude theorem bypasses the repaired pairing hypotheses.** [bv_brst.tex:183](/Users/raeez/mathematics/worktrees/frontier-cbc-virasoro-021-20260914/research-candidates/cbc-virasoro021/candidate002/cbc/chapters/connections/bv_brst.tex:183), `thm:genus0-amplitude-bar`, still identifies arbitrary insertion amplitudes with a bar Euler characteristic. It supplies none of the insertion maps, pairing homotopy, or closed functional now required by Corollary 18.24.2.

   Its proof also asserts
   \[
   \overline C_n(\mathbb P^1)=\overline{\mathcal M}_{0,n+1},
   \]
   although their complex dimensions are \(n\) and \(n-2\). Arbitrary multilinear insertion integrals cannot be identified with an insertion-independent Euler characteristic by Gauss–Bonnet. This theorem appears on **affected PDF p. 1363**.

   **Required repair:** specify the actual geometric carrier and insertion maps, prove the relevant pairing statement, and independently justify any Euler-characteristic identity.

4. **Scalar anomaly claims contradict their cited result.** `free_fields.tex:3429–3433` and `concordance.tex:3065–3068` assert \(\kappa+\kappa'=0\), citing `cor:anomaly-duality-w`. That corollary, `bv_brst.tex:1451–1458`, gives **13** for the Virasoro same-family pair.

   The decisive exact example is
   \[
   k=-8/3,\quad k'=-4/3,\quad c=26,\quad c'=0,
   \qquad \kappa+\kappa'=(c+c')/2=13.
   \]
   The Kac–Moody discussion at `bv_brst.tex:1257–1317` also transports curvature/anomaly operators and genus-\(g\) semi-infinite identifications without supplying those operator or genuswise maps.

   **Required repair:** distinguish the scalar normalizations, the same-family partner, the string ghost contribution, and actual anomaly-operator transport. The filtered chain criterion establishes none of these additional identifications.

5. **The connected consumer union is larger than the seven edited files.** Unconditional claims remain at:

   | Source | Surviving claim |
   |---|---|
   | `main.tex:621–624`, PDF p. 1331 | Genus-zero bar/BRST comparison is proved. |
   | `introduction.tex:345,355` | Bar is BRST; the BRST resolution is complete. |
   | `concordance.tex:3156–3164`, PDF p. 1457 | Boundary KM/W BRST comparison is proved; only bulk comparison remains. |
   | `free_fields.tex:1629` | Semi-infinite Motzkin growth is imported through the W theorem. |
   | `free_fields.tex:3886–3917`, PDF p. 893 | Conditional comparison becomes a genus-one chain isomorphism. |
   | `holomorphic_topological.tex:314–371,737` | Open-string and W comparisons are asserted as proved. |
   | `koszul_pair_structure.tex:1288–1343,1400–1409` | The comparison transports MC equations and DS flatness without the required structure maps. |
   | `w_algebras_framework.tex:136–143` | All bar computations become semi-infinite computations; anomalies are said to cancel. |
   | `bv_brst.tex:224–227,1152–1158` | Matter–ghost bar constructions are instantiated despite the augmentation obstruction. |

   These occurrences require a new candidate and renewed review. The current seven-file delta does not close propagation.

6. **The affected prose still contains manuscript-firewall violations.** `concordance.tex:2124` retains “MC5 attack chain,” visible on PDF p. 1446. Lines 863 and 877 retain “the standard-tower MC5 packet closes.” These describe coordination and completion machinery rather than mathematical statements. Express the mathematical implication directly and move workflow language outside the manuscript.

The following bounded arguments passed independent examination:

| Coverage | Result |
|---|---|
| Full algebraic operator proof, native `bv_brst.tex:343–900` and complete standalone proof | Domain/local finiteness, ghost central term, commutant argument, \(Q^2\), residue normalization, intercept, polarization shifts, absolute/relative distinction and three-term relative complex are consistent. |
| Augmentation obstruction, `bv_brst.tex:924–963` | \(b_{(0)}c=\Omega_A\), \(T_{(3)}T=13\Omega_A\), residue normalization, and failures of vacuum projection/quotient are valid. |
| Relative/absolute and coordinate obstruction, `bv_brst.tex:965–1029` | Four-state calculation, contracting homotopies and \(g_sv=v-sc_0c_1\Omega\) are valid. |
| Filtered criterion, `bv_brst.tex:1033–1083` | Valid as a conditional theorem of complex vector-space complexes. I inspected the imported obstruction, Hom-primitive and cone-contraction proofs in `filtered_pbw_lifts.tex`; I did not rely on another reviewer’s verdict. |
| Binary and pairing requirements | The explicit binary-intertwining requirement, its counterexample, and the pairing-homotopy/closed-functional argument are valid. They do not construct the required application data. |
| Logarithmic sign correction | \(d\log(1-t)=dt/(t-1)\), with residue \(+1\) at \(t=1\), is correct. |

Independent exact Clifford calculations, implemented entirely in memory, reproduced
\[
R^2b_{-2}\Omega=-13c_{-2}\Omega,\quad
Qu=-2v,\quad Qe=Qv=Qw=0,\quad
\mathcal L_1v=-c_0c_1\Omega,\quad \mathcal L_1^2v=0.
\]
Cutoffs \(4,8,16\) agreed. I also checked the finite ghost-central sums for modes \(2,\ldots,10\). These support the finite calculations; the general operator conclusion rests on the inspected algebraic proof.

Byte and artifact bindings were verified:

| Binding | SHA-256 |
|---|---|
| Candidate manifest | `659d531edbe48ab58c1b716b58ba877ac71dd07c3400e312ef0595956ff43776` |
| Source freeze | `3743e17147ddda379b747a00392681411cf56259313604e71d21bd99002eb8e5` |
| Native diff | `8fe97a6617c3dd2f4804548984935f76ccff20c4170866b7dbef61cae59946f3` |
| Replacement records | `fc21bb2dd7edac46f79b565d3d39eaddcc2ead7ed50f3b4651fadbe766fcf006` |
| Archive001 binding | `faa0345f700a767685494b1097f720b8c62b1482a9d33de58b53a5d8d056207d` |
| Original archived manifest | `41e2346d90645d1d45f7deff0dd956f2ec368cfd293972734b7f038e053a0468` |
| Build-input closure | `846b8834975e95c365b36edd95ddeee5e3994988b5cdc90d89f9ef5ef61412dc` |
| Render binding | `2ac5ba058647416d5c114bed1ae4eeec712a19e5641ee2981a13e9c1a853fd1a` |
| Unchanged operator source | `017765248b4eccab1a14a20b014d95b5ddf277459945f9995ab7d90284c8efa0` |
| Unchanged operator PDF, 8 pages | `939dc34c716bf6a3e9690f449b22dcece8b0c27624c41bb2833d883b673ae88e` |
| Native PDF, 1,642 pages | `e8af4dd0a1fd6f9fb2ca2f4c3385ce145bce80e29ce596dd90685b2d5c4988a9` |

All **729 candidate rows**, **70 frozen source files**, **434 preserved build inputs**, and **1,314 archive rows** matched. Archived files and directories have no write bits. All 57 replacement records replayed in memory to the exact seven native files; records 21 and 34 each replace two occurrences. The unchanged inline operator region has SHA-256 `72786ba409a7264fa0b0095ad2c9dfbd731bb75ad83458bb0f46bc64e67128ad`; its differences from the standalone text are section depth, the native equation label, and the additional legacy theorem label.

I regenerated all **76 bound pages in memory** with Poppler 26.02.0; every raster hash matched. I visually inspected those pages, all eight operator pages, and additional omitted-consumer pages 1331 and 1380. Core pairing and coordinate-obstruction pages were also inspected at full size.

The native build retains the same **10 undefined citations and one undefined reference** as the archived baseline. `BerFres04` remains undefined on affected PDF p. 1388. No fatal LaTeX error or duplicate label was found. Consequently this is not a clean whole-book build/render acceptance.

Public execution metadata verified `gpt-6-astra` with `reasoning_effort: ultra`. No prior verdicts were read. **Changed paths: none.** No builds, disk renders, scratch files, cache writes, git mutations, or delegation were performed.

The bounded mathematical results above can be preserved. The actual chiral target, relative descent, symbol comparison and surviving consumer claims remain unresolved; this review does not certify the whole book.