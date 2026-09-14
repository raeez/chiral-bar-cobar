# Exact review of CBC successor002 and elliptic propagator003

Date: 2026-09-14. The two verdicts below concern distinct frozen source closures.

**Successor002: the new bounded proofs pass mathematical review. The whole native consumer closure remains unaccepted.** The surviving W, modular-amplitude, and higher-action claims listed below prevent whole-candidate acceptance. Replacing a failed theorem with an explicit missing-map statement does not complete the original chiral theorem obligation.

**Elliptic propagator003: pass for the scalar smooth Dolbeault theorem on a compact complex torus.** No blocking mathematical or rendering defect was found in its two-source closure. This verdict does not certify a chiral bar, BRST, conformal-character, or field-theory comparison. One minor notation defect is recorded below.

## Frozen boundaries

The source worktree is `/Users/raeez/mathematics/worktrees/frontier-cbc-native-026-20260914`. Its base is `cb6e88263f4bb75ef5c1d9db911f61ca5d3d4d9c`.

| Boundary | SHA-256 |
|---|---|
| Successor002 source manifest, 80 sources | `91231055c6aa861d1facd38e37e740f5e6fdb7b87ce52cdf67ab781c2222ce96` |
| Successor002 exact delta, 17 changed or added sources | `e796e8d29f378b011515e2aa8240817ccdd991f89c681b8d73f30e188724c391` |
| Successor002 final evidence manifest, 631 files | `e08e4c39dac58be71d51ecc403476c9d6134c937a5d9af5d47dcf19afcefd341` |
| Propagator003 source manifest, two sources | `ec88713d11a841d221352e828ac1cf9750b1796c4fa13d4eb34af0d13bb876b1` |
| Propagator003 `proof/elliptic_propagator.tex` | `c990f9adeb01ebb53108d8ff59a14c7bba14c0c6ca136b0d51598ad662905b05` |
| Propagator003 `proof/main.tex` | `bfff287cf0182f9f13be64412e3d7c40e09d974e7307f7aef94c2af5bf48eb39` |

All 82 source hashes match. All 631 entries in the successor final manifest match. The 76 predecessor source hashes also match. An independent `difflib.unified_diff` reconstruction reproduces the supplied successor diff byte for byte. The 754 recorded TeX input objects match their hashes.

`source-verification.json`, `delta-verification.json`, and `native-input-verification.json` retain these checks. Exact source copies are under `frozen-sources/`. They are review evidence, not edited manuscript candidates.

The prior eight-group review was read at `frontier-cbc-union-review-026-20260914/reports/research/cbc_union_review026/REVIEW.md`. Its verdicts were treated as claims to check. The sources, calculations, and PDFs below supply this review's evidence.

## Blocking native findings

### R1. A proposed W comparison still appears as a proved theorem

**CRITICAL.** All source paths in this section are relative to `research-candidates/cbc_native026/candidate002/cbc/`.

`chapters/examples/w_algebras_framework.tex:588–618` retains `thm:w-koszul-precise` with a proved-here status. Part B asserts a curved chiral equivalence at every noncritical principal level. Its proof now says that Part B is the proposed comparison in Remark `thm:w-algebra-koszul-main`. Part A then takes an unspecified critical-level limit, and Part C invokes Part B.

The actual remark at lines 45–58 explicitly requires an affine–ghost collision complex, reduced target, compatible comparison, and a family over the level parameter. Those constructions do not appear in the displayed proof. A proposed comparison cannot prove Part B. A limiting scalar curvature cannot construct the required critical-level family or its specialization.

Theorem `thm:w3-koszul-dual` at lines 1156–1188 repeats the problem. Its proof claims critical self-duality from the proposed comparison. It also calls reflection `k -> -k-6` Feigin–Frenkel duality. The primary reciprocal relation is `t t^vee=1/r^vee`, with `t=k+h^vee`. See Arakawa, page 566, footnote 1, in [Rationality of W-algebras: principal nilpotent cases](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n2-p04-p.pdf).

The deciding Virasoro example is `t=-2/3`. Reflection gives charges 26 and 0. Reciprocation gives charges 26 and 26. A conformal map preserves `T_(3)T=(c/2)1`, so reflection cannot be supplied by that conformal duality. This counterexample refutes that route. It does not refute every possible curved equivalence.

Actual rendered evidence: native PDF pages 987–988 and 995. Additional consumers remain at `chapters/frame/heisenberg_frame.tex:2242–2269` and `chapters/examples/deformation_examples.tex:562`, visible on pages 72 and 1083. The W chapter opening at lines 15–26 also asserts the unconstructed functorial conclusion, visible on page 977.

Required proof: construct the quantum chiral objects, collision actions, and compatible maps. Specify the equivalence and preserved structures. Critical specialization requires its own construction. The explicit polynomial theorem does not bridge these carriers.

### R2. The adjacent one-loop integral does not descend to the stated torus

**SERIOUS.** `chapters/examples/free_fields.tex:3785–3792`, native PDF page 892.

Immediately before the corrected character section, the example still displays

`integral_(M_1) d tau wedge d bar(tau)/Y^2 integral_(T_tau) dz_1 wedge dz_2/(z_1-z_2)^2 V_1(z_1)V_2(z_2)`

and claims a modular one-loop correction. No insertion transformation law or appropriate two-point integration domain is given. The scalar kernel is not periodic: at difference `z=1/2`, its value is 4, while the representative `z+1=3/2` gives 4/9. Thus it does not define the displayed scalar coefficient on the torus. Two independent insertion coordinates also require an explicit configuration-space domain or a gauge-fixing construction. Neither is specified here.

The corrected `G_tau` proposition proves a covering-plane transformation law. Propagator003 proves a separate periodic scalar kernel. Neither frozen candidate identifies this amplitude with an integral formed from that kernel and actual insertion maps.

Required proof: give the insertion objects, periodic kernel, integration cycle or domain, collision regularization, and modular descent. Then prove the claimed invariance.

### R3. The later action continuation repeats the unresolved MC interpretation

**SERIOUS.** `chapters/theory/koszul_pair_structure.tex:1345–1354`, native PDF page 631.

The later continuation still asserts an action with terms `m_(n-1)(alpha^n)` and says that critical level abelianizes the theory. It does not give a cyclic contraction, a map into three-forms, or the higher morphism to the de Rham carrier. In standard A-infinity notation, `m_(n-1)` has `n-1` inputs. Applying it directly to `n` copies requires additional pairing or contraction notation.

On the constructed carrier `Omega^bullet(M) tensor sl_2`, take `A=e dx+f dy`. Then `dA=0` and `[A,A]/2=h dx wedge dy`, independently of any level. Thus critical level alone does not abelianize this carrier. Four or more uncontracted one-form factors also vanish on a three-manifold.

The sound new contraction proposition at `form_degree.tex:3–24` states exactly which extra tensor and vector field can give a nonzero three-form. It does not construct this retained action. Replacing the earlier RTT paragraph did not resolve this later occurrence.

The immediately preceding BV theorem, `koszul_pair_structure.tex:1299–1331`, also retains an unresolved native interface, visible on page 630. It identifies an unspecified residue operator with a BV Laplacian and a bar pairing with a QME candidate. The theorem says the full QME is established, while its proof still requires the interaction calculation. The polynomial Koszul projection supplies neither this operator on collision sheaves nor that interaction identity.

Required proof: define the native operator and cyclic pairing, prove the higher equations, and specify the map to the field space. The finite BV theorem cannot supply these data by itself.

## Eight-group disposition

| Prior group | Exact successor disposition | Remaining obligation |
|---|---|---|
| F1: full W/DS theorem and reflection | `w_algebras_framework.tex:45–58` now states the missing construction. `reduction_parameters.tex:3–18` proves the conformal obstruction. | Original quantum chiral theorem remains unresolved. R1 identifies retained theorem consumers. |
| F2: B2 normalization | `reduction_parameters.tex:20–33` gives 172. The former all-simple formula at the original occurrence was removed. | A scalar identity does not prove the W comparison. The later simply-laced W3 check has value 100, but its phrase “general formula” needs the simply-laced qualification if read universally. |
| F3: modular weight and kernel residue | `elliptic_normalizations.tex:3–114` proves translation, inverse-eta weight, invariant pairings, and the corrected covering-plane kernel law. | The native character/chain realization remains conjectural. R2 identifies the surviving amplitude. Propagator003 is a separate scalar construction. |
| F4: unconditional CG/BRST identification | `concordance.tex:412–416` now gives the finite Koszul theorem and lists the missing field-theory data. | Original CG/chiral comparison remains unresolved. The continuation in R3 still lacks native BV data. |
| F5: genus-one coefficient | `bv_brst.tex:185–189` consistently gives `F1=kappa/24=C/48`. `reduction_parameters.tex:35–53` distinguishes vacuum energy. | A Hodge or trace interpretation needs its own normalized map. |
| F6: RTT quartic, critical theory, quotient | `form_degree.tex:3–43` proves the degree obstruction, explicit contraction, persistent sl2 curvature, and one quotient factor. | These bounded results do not construct RTT or cyclic higher operations. R3 remains in the next continuation. |
| F7: stale comparison references | The six cited concordance references now point to `thm:brst-bar-genus0` and `cor:string-amplitude-genus0`. The modular index describes the translation proposition. | Replacement of the W theorem leaves the stronger consumers in R1. |
| F8: manuscript firewall | The cited downstream-task sentence and the W/AGT task sentence are absent. The replacement sentences state mathematical missing maps. | No all-book firewall certificate is claimed. The new proof bodies and all four propagator pages contain mathematics only. |

## Proof checks for successor002

### Characters and covering-plane kernel

The Heisenberg PBW basis has one oscillator of each positive integral weight. Its generating function is `product_(n>=1)(1-q^n)^(-1)`. Vacuum energy gives the factor `q^(-1/24)`. This proves `Z_H=eta^(-1)` and the translation phase directly.

The S transformation follows from the eta identity with the branch positive on the positive imaginary axis. This is [DLMF 23.18.5](https://dlmf.nist.gov/23.18#E5). Its inverse weight is `-1/2`. For general integral characters, each summand has the same translation phase. A nonzero product with its conjugate is translation invariant exactly when the real central-charge difference lies in `24 Z`.

For `j=c tau+d`, lattice rescaling gives `zeta_(gamma tau)(z/j)=j zeta_tau(z)`. Differentiating the eta law gives `E2(gamma tau)=j^2 E2(tau)+6cj/(pi i)`. Hence the declared `G=zeta+(pi^2/3)E2 z` satisfies `G_(gamma tau)(z/j)=jG_tau(z)-2 pi i c z`. Its coefficient residue is `j`, and its pulled-back one-form residue is one. No periodicity is asserted for this G.

The source defines the full grouped zeta summand. It decays as the inverse cube of the lattice norm. Therefore the reindexing uses an absolutely normally convergent series, not a conditionally ordered weight-two Eisenstein sum.

### Reflection, B2, and F1

The conformal-isomorphism obstruction follows from the vacuum and third product of the conformal vector. Equality of `c(t)` and `c(-t)` gives `t^2+1=0`. At those two values, both universal presentations have charge 13, proving sufficiency.

The B2 positive roots independently give `rho=(3/2,1/2)` and `rho^vee=(2,1)`. Their squared norms are `5/2` and 5. Their pairing is `7/2`. Substitution into the principal charge formula gives `86-60t-30/t` and reflected sum 172. Arakawa's page 566 formula uses the same root/coroot normalization. The proposed value 124 fails in this exact deciding case.

The Bernoulli coefficient is `(1/2)(1/6)(1/2)=1/24`. Thus `F1(26/2)=13/24`, while the conformal vacuum exponent is `-26/24=-13/12`. These arithmetic identities have distinct declared meanings.

### Polynomial BV and its Jacobian projection

On `K=C[x_1,...,x_n] tensor Lambda(eta_1,...,eta_n)`, with degrees 0 and -1, the bracket has degree one. The Hamiltonian S contains no eta variable. Thus `Qx_i=0`, `Qeta_i=partial_i S`, and `Q^2=0` on all generators. The square is an even derivation, so it vanishes everywhere.

The quotient map kills every gradient component and every eta variable. It is a chain algebra map. A regular first gradient gives a two-term resolution. Tensoring with the next free two-term complex produces a finite two-column calculation. The next gradient acts injectively on the preceding quotient. Induction gives only degree-zero cohomology, exactly the Jacobian algebra. This proves the stated quasi-isomorphism.

For `S=x^3/3+y^4/4`, the gradient is `(x^2,y^3)` and the Jacobian basis is `1,x,y,xy,y^2,xy^2`. Direct odd differentiation gives `Q(eta_1 eta_2)=x^2 eta_2-y^3 eta_1`. The square cancels. For `S=0`, Q is zero and negative cohomology survives. This verifies why the regular-sequence hypothesis is needed. The theorem does not assert a BV bracket on the quotient or preservation of such a bracket.

### Form degree and quotient integration

The fourfold wedge vanishes because `Lambda^4 T^*M=0`. With the stated tensor entry and vector field, only `T(e_1,e_1,e_2,e_3)` contributes. The result is exactly `dx wedge dy wedge dz`. It is a defined local three-form, with no gauge-invariance claim.

The quotient map for a free finite orientation-preserving action is an oriented covering of degree `|Gamma|`. A partition of unity on evenly covered sets gives one contribution per sheet. This proves the single factor `1/|Gamma|`. On the three-torus, translation by `1/N` in the first coordinate gives quotient volume `1/N`. A second division would give the wrong value.

### Preserved predecessor results

The polynomial DS and associative bar proof was reread at `ds_chain_comparisons.tex:10–121`. Its finite c-filtration first resolves the regular element `e-1`. The coordinate `u=f+h^2/4` turns the remaining differential into `-2c partial_h`. Polynomial primitives give cohomology `C[u]`. The displayed inclusion and projection are inverse on cohomology.

For the direct-sum bar, every cycle has finite maximal tensor length. Acyclicity of each cone quotient removes that largest component, and induction terminates. This argument does not prove the product-completed statement. The projection's Poisson defect remains `p{h,f}=-2u`, while `{p(h),p(f)}=0`.

The finite-column comparison at lines 130–156 uses a finite decreasing filtration with acyclic column cones. Its total quasi-isomorphism follows without an infinite-convergence claim. The flat-bundle comparison at lines 285–322 requires both horizontality and the internal chain identity. The torus local-system example still separates equal fibers from different global cohomology.

The insertion proof uses an actual chain map to smooth top forms on compact `Mbar_(0,n)`. Stokes' theorem makes its integral a cohomology function. Multilinearity excludes an arbitrary nonzero insertion-independent value. The MC proof requires all coalgebra identities over a nilpotent Artinian ideal. Its exponential sums are finite. The Chern–Simons variational identity uses the closed oriented three-manifold, nonzero k, and nondegenerate invariant form.

These arguments remain valid on their stated carriers. The unchanged full Virasoro operator calculation was not repeated here. Preservation of its bytes is recorded separately from fresh proof certification.

## Proof checks for propagator003

All anchors below refer to `proof/elliptic_propagator.tex` inside its own two-source closure.

### Periods and current equation

Lines 20–54 define the lattice zeta series and prove its periods. Absolute normal convergence permits differentiation and reindexing. The derivative of wp is periodic. Evenness of wp makes its period differences vanish at primitive half-periods. Thus the zeta differences are constants. An oriented fundamental parallelogram gives `a_tau tau-b_tau=2 pi i`.

Lines 56–105 define

`P_tau(z)=zeta_tau(z)-a_tau z+(2 pi i/Y) Im z`.

The period-one increment is zero. The period-tau increment is `b_tau-a_tau tau+2 pi i=0`. Each summand is odd. The singularity `1/z` is locally integrable in two real dimensions.

With `dbar=(1/2)(partial_x+i partial_y)dbar z`, its scalar derivative is `pi delta_area-pi/Y`. Since `dbar z wedge dz=2i dx wedge dy`, the pole contributes `2 pi i delta_0`. The smooth term contributes `-2 pi i nu_tau`. The current equation and its sign are correct.

The difference of two permitted solutions is a smooth holomorphic function on the compact torus. It is constant, and oddness kills that constant. Pairing a hypothetical primitive of `2 pi i delta_0` with the constant test function excludes that primitive. Thus subtraction of the constant mode is necessary, not an optional regularization.

### Modular weight and the E2 constant

Lines 117–141 use uniqueness to prove the modular law. The scaled function `j^(-1)P_(tau')(z/j)` has the same periods, singularity, oddness, and scalar dbar derivative. It therefore equals P. This gives coefficient weight one and an invariant pulled-back one-form. The normalized area also pulls back correctly because `Y'=Y/|j|^2`.

Lines 143–166 use [DLMF 23.8.2](https://dlmf.nist.gov/23.8#E2). Its half-periods are `1/2,tau/2`. The DLMF nome is `exp(pi i tau)`, so its `q^(2n)` becomes the source's `exp(2 pi i n tau)`. The sine coefficient becomes `4 pi`.

The cotangent linear coefficient is `-pi^2/3`. The sine series contributes `8 pi^2 sum n q^n/(1-q^n)`. The zeta series has zero linear coefficient. Thus `a_tau=(pi^2/3)E2(tau)`, with the stated sign and factor. The strip `|Im z|<=Y-epsilon` gives geometric decay, including every fixed derivative order. The lattice definition agrees with [DLMF 23.2.5](https://dlmf.nist.gov/23.2#E5).

### Smooth Dolbeault deformation retraction

Lines 168–238 fix a smooth scalar Dolbeault complex on one compact torus. Its topology is the usual Frechet topology. The operator is convolution by the L1 kernel P with area measure and factor `1/pi`.

Changing variables places every derivative on the smooth input. Bounded derivatives and an L1 kernel justify differentiation under the integral. The displayed seminorm estimate proves continuity. Convolution of the current equation gives `dbar H=1-ip` on one-forms. Moving the derivative to the input gives `H dbar=1-ip` on functions. This also establishes that p is a chain map.

Inversion preserves area and reverses the odd kernel. Its mean is therefore zero. Fubini gives `pH=0`, constant inputs give `Hi=0`, and the two-term grading gives `H^2=0`. The ordinary coefficient averages give `pi=1`.

For naturality, the one-form coefficient pulls back with `bar(j)^(-1)`. Changing integration variable contributes `|j|^2`, and the kernel contributes `j^(-1)`. Their product is one. The claimed identity `phi^* H_(tau')=H_tau phi^*` therefore holds. This proof fixes the coefficient type and avoids confusing a scalar with a one-form.

An independent Fourier calculation gives a deciding normalization check. Write `z=s+t tau`, with both coordinates periodic modulo one. Then

`partial_bar(z) exp(2 pi i(ms+nt)) = [pi(m tau-n)/Y] exp(2 pi i(ms+nt))`.

For `(m,n) != (0,0)`, the inverse coefficient is `Y/[pi(m tau-n)]`. The zero mode is removed. At `tau=i,m=1,n=0`, this is `-i/pi`, exactly the source's example. Rapid Fourier decay also gives an independent smooth inverse description. The convolution proof already proves the general theorem.

**Minor notation:** lines 180, 200, 209, and 231 use `f,dbar z` where the input one-form is `f dbar z`. Equation (5) and the final paragraph visibly contain this comma. The domain and subsequent one-form calculation make the intended multiplication unambiguous. It is a typographical issue, not a different operator or a mathematical blocker. Any correction would create new bytes and need a new manifest.

## Calculations, builds, and renders

Run the retained independent diagnostic with:

```sh
python3 reports/research/cbc_successor_review026/check_calculations.py
```

It uses Python 3.9.6 and only the standard library. Exact checks cover B2, the Virasoro reflection witness, F1, 196 BV monomials, all 81 fourfold wedges, and 160 nonzero Fourier modes. The BV calculation tests a regular nonquadratic gradient. The S=0 case records failure without regularity.

Twelve numerical kernel checks use three tori and the matrices S, T, -I, and `(1 0;1 1)`. They test both the periodic P law and the separate meromorphic G law. Maximum observed errors are below `2.3e-15`. The output records an analytic Fourier-tail bound for each P evaluation. Floating-point roundoff is not certified, so these calculations are diagnostics, not proof certificates.

One diagnostic initially used the wrong sign in an extra square-torus test. The modular law gives `P(iz)=-iP(z)`, so the correct identity is `P(z)-iP(iz)=0`. The corrected test passes. This was a test-equation defect and did not change either source candidate.

The independent propagator build used its copied, owned source directory as cwd and a separate owned output directory. Three pdflatex passes exited zero with no warnings. `build003.json` records the command and toolchain. `elliptic-build-input-closure.json` freezes 107 actual inputs. The source bytes were not edited.

| PDF | Pages | SHA-256 |
|---|---:|---|
| Supplied native002 | 1642 | `270673722a7de743dc8a425a2302527d50f879379941785e189b0b9cfec4de61` |
| Supplied bounded proof002 | 22 | `c304d2cf0ab6deed23c3b653c8b064cb8559c6e6ed6a38ca25d09a04e20200c6` |
| Supplied propagator003 | 4 | `a4551df9526b233bd462b648b9fc59713e09fc6146351c5c3bba7da1e85bff8b` |
| Independently rebuilt propagator003 | 4 | `4bacb88ed43c977852a3d5acab5960f00a625b89e789b2f334c2cc6e2b034949` |

The two propagator PDFs have different file hashes. All four independently rasterized page hashes agree between them. Thus the rendered output matches exactly at the recorded Poppler resolution. No claim of PDF byte identity is made.

Twenty-one native pages were rasterized and visually inspected: 72, 628–631, 891–894, 977–979, 987–988, 995, 1008, 1083, 1362, 1428, 1433, and 1485. The corrected proofs are legible. The blocking continuations remain visible in that same artifact. Proof002 pages 17–22 and every propagator page were also inspected. `render-binding.json` records 35 raster outputs, including the four rebuilt duplicates.

The native build was not rerun. Its frozen log records ten undefined citations, one undefined reference, and two overfull boxes. Its exact PDF and recorded input objects were checked. The supplied proof002 build has no recorded warnings. Neither log status certifies the unreviewed portions of the book.

No project-management narration was found in the new mathematical proof bodies or propagator PDF. The specific F8 task phrases are absent. This review does not certify all inherited native prose or every inherited metadata field.

## Residual obligations and custody

The first quantum chiral obligation remains the construction of the affine–ghost collision complex and its reduced unital target. A valid comparison needs actual chain maps, affine category hypotheses, collision equivariance, and a justified totalization. Operations, pairings, anomaly squares, connections, clutching, and critical specialization require their separate equations.

Propagator003 supplies scalar periodicity, its current equation, modular naturality, and a smooth Dolbeault contraction. It does not supply coefficient objects on a chiral collision complex or a conformal trace. Integrating it into native002 would form a new candidate. The two frozen verdicts cannot be combined into a certificate for changed native bytes.

The programme requires gpt-6-astra with ultra effort for mathematical review. Independently observed runtime metadata was unavailable. Observed controls remain unverified, and no mismatch was observed. Instruction text is not runtime evidence.

Only `reports/research/cbc_successor_review026/` in the assigned review worktree was written. No source edit, staging, commit, push, or child assignment occurred. The review closes this bounded investigation. It does not close the original W/CG/MC repair or authorize integration, publication, or reader delivery.
