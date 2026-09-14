# CBC native026 exact mathematical review

## Verdict

**Do not accept the frozen native consumer union.** The new bounded constructions have sound proofs on their stated carriers. Connected native claims still exceed those constructions or contradict their scalar formulas.

This verdict concerns manifest `60770b9aeb10d62de09c5793368d9483bf348d0ff9ef2897554acd27bfacc328` and aggregate diff `411331d13af5c34a49174a8c722989b3eac0190c9049c15c8098eb9e86b17c23`. All 76 source hashes match. The 16 change flags also match independent comparisons with the preserved native002 sources.

Source anchors below are relative to:

`/Users/raeez/mathematics/worktrees/frontier-cbc-native-026-20260914/research-candidates/cbc_native026/`

The original quantum chiral W comparison remains unresolved. The polynomial theorem neither constructs that comparison nor rules out every possible chiral target. This review does not certify the whole book.

## Blocking findings

### F1. The connected W theorem still imports the missing chiral reduction maps

**CRITICAL.** `cbc/chapters/examples/w_algebras_framework.tex:43–140`, especially lines 79–103 and 116–121. Native PDF pages 979–981.

Theorem `thm:w-algebra-koszul-main` still asserts a curved chiral equivalence at every noncritical principal level. Its proof replaces a bar construction by DS cohomology of bars of free fields. It supplies neither the full affine–ghost collision complex nor the required comparison maps. The displayed free-field object in lines 73–77 does not specify the ghost complex on which its reduction differential acts.

The new polynomial theorem proves a statement for augmented commutative differential graded algebras over C. Its associative bar is a direct sum of finite tensor words. The source expressly denies an automatic extension to chiral sheaves or completions. That proof cannot validate the retained chiral argument.

The proof also invokes Feigin–Frenkel duality to obtain `k'=-k-2h∨` at lines 95–97 and 112–114. Feigin–Frenkel parameters instead satisfy `t t∨=1/r∨`, with `t=k+h∨`. The new source states this distinction correctly at `ds_chain_comparisons.tex:259`. Arakawa records the reciprocal relation on page 566, footnote 1, of [Rationality of W-algebras: principal nilpotent cases](https://annals.math.princeton.edu/wp-content/uploads/annals-v182-n2-p04-p.pdf).

For sl2, take `t=-2/3`. Reflection gives `t'=2/3`, while the reciprocal partner is `t∨=-3/2`. The corresponding reflected central charges are 26 and 0. The reciprocal pair both have central charge 26. Thus the cited duality does not supply the asserted reflection map.

**Required repair:** construct the quantum chiral reduction comparison on its actual carrier, or preserve the explicit unresolved theorem obligation. Correcting the last paragraph of this proof does not validate its earlier steps. A change of theorem status alone does not close the original proof task.

### F2. The retained general central-charge sum fails for B2

**SERIOUS.** `cbc/chapters/examples/w_algebras_framework.tex:130–134`. Native PDF page 981.

The retained formula claims

`c(t)+c(-t)=2 rank(g)+4 h∨ dim(g)`

for every simple Lie algebra. The new formula at `ds_chain_comparisons.tex:233–256` instead gives

`c(t)+c(-t)=2r+48(ρ,ρ∨)`.

They agree for simply laced root systems. They do not agree in general.

For B2, take an orthonormal basis `e1,e2` and positive roots `e1-e2,e2,e1,e1+e2`. Long roots have squared length 2. Then

`ρ=(3/2,1/2)`, `ρ∨=(2,1)`, `(ρ,ρ∨)=7/2`.

The rank is 2, the dimension is `2+2·4=10`, and `h∨=1+(ρ,e1+e2)=3`. The correct reflected sum is `4+48·7/2=172`. The retained formula gives `4+4·3·10=124`.

The polynomial root calculation is reproduced in `check_exact.py`. This is an exact counterexample, independent of any conjectured bar comparison.

**Required repair:** retain the general `ρ,ρ∨` formula and state the simply laced specialization with its hypothesis.

### F3. The surviving modular-weight theorem is false on its own stated interpretation

**CRITICAL.** `cbc/chapters/examples/free_fields.tex:3817–3849`. Repeated at lines 3809–3810 and 3884–3888. Native PDF pages 892–894.

Theorem `thm:modular-invariance` asserts the scalar law

`Z(γτ)=(cγ τ+dγ)^(C/24) Z(τ)`.

Its proof defines `Z(τ)=Tr_V exp(2πiτ(L0-C/24))`. Here `C` denotes central charge and `cγ` the matrix entry.

For any nonzero integrally graded vacuum module with convergent character, translation gives

`Z(τ+1)=exp(-2πi C/24) Z(τ)`.

The asserted law gives `Z(τ+1)=Z(τ)`, since the translation matrix has bottom row `(0,1)`. The rank-one Heisenberg vacuum has `C=1` and character

`Z(τ)=q^(-1/24) product_(n≥1) (1-q^n)^(-1)`.

Its nontrivial translation multiplier already contradicts the claim. This calculation needs only the oscillator basis and the displayed trace definition. It does not use an assumed theorem about the bar construction.

A second contradiction occurs inside the proof at lines 3833–3837. The displayed propagator has Laurent expansion `Gτ(z)=1/z+O(z)`. With `a=cγτ+dγ`, the proposed transformation has residue `a` on its left side and `a²` on its right side. The added term is regular at zero. At `γ=S` and `τ=i`, these residues are `i` and `-1`.

The new proposition at lines 3852–3865 correctly requires transition data. It does not repair the false theorem immediately before it. The claim that the conformal vacuum fails to be L0-invariant is also inconsistent with `L0 1=0`.

**Required repair:** specify the character or conformal-block object and its actual multiplier or modular representation. Verify the propagator transformation by its Laurent coefficients. Then propagate the corrected law to the adjacent examples and anomaly assertions.

### F4. The concordance still asserts an unconditional BRST/bar identification

**SERIOUS.** `cbc/chapters/connections/concordance.tex:412–417`. Native PDF page 1430.

The Costello–Gwilliam comparison states that its BV formalism produces the same BRST complex as the native bar construction. It explicitly writes `B(A) ≃ C^BRST(A)` and cites the chapter.

The chapter now provides a filtered criterion, a polynomial reduction, and obstructions to the proposed augmentation and relative descent. These results do not supply the claimed field-theory complex or its comparison map. No specified model, collision target, coordinate descent, or chain map accompanies this statement.

This finding identifies an unsupported implication. It does not claim that no Costello–Gwilliam comparison can exist.

**Required repair:** name the actual complexes and prove their comparison. Until then, preserve the missing construction explicitly at this occurrence.

### F5. The adjacent genus-one scalar normalization remains contradictory

**SERIOUS.** `cbc/chapters/connections/bv_brst.tex:185–186`. Native PDF page 1364.

The same remark gives `F1=κ/24` and, for Virasoro, `F1=C/24`. With the retained normalization `κ=C/2`, the first equation instead gives `F1=C/48`.

The invoked source `cbc/chapters/theory/higher_genus.tex:4078–4081` gives the genus-one coefficient `1/24`: at `g=1`, its Bernoulli expression is `(1/2)(1/6)/2!=1/24`. The discrepancy is therefore present in the actual cited formula.

For `C=26`, the two claimed values are `13/24` and `13/12`. A separate trace convention could define a different quantity, but the remark identifies them without such a convention.

**Required repair:** distinguish the vacuum-energy exponent, the Hodge integral, and any separately normalized trace. State the normalization for each map.

### F6. The unchanged continuation still asserts unsupported MC-to-action identifications

**SERIOUS.** `cbc/chapters/theory/koszul_pair_structure.tex:1266–1295`. Native PDF page 629.

After the new MC transport theorem, the text again asserts a quartic RTT action, a Yangian MC/CS identification, a critical W free theory, and an orbifold action. It supplies no higher map to the de Rham carrier, no domain for the RTT operation, and no action of the purported orbifold group.

On the only connection carrier actually constructed here, `α∈Ω¹(M,g)` for a three-manifold, the literal wedge term `α⁴` is a four-form and vanishes. It cannot furnish the asserted nonzero quartic interaction. A contraction or a graded field space could change that conclusion, but either requires a new definition and proof.

**Required repair:** construct the operation and action on a specified carrier. The sound new transport theorem does not establish these examples.

### F7. Changed theorem content leaves stale hypothesis references

**MODERATE.** `cbc/chapters/connections/concordance.tex:698,776,830,860,2103,5451`. Native PDF pages 1435 and 1448 include examples.

These references still describe `thm:algebraic-string-dictionary` as the source of the full filtered comparison and pairing hypotheses. The label now denotes the state/scalar/insertion proposition at `free_fields.tex:3420–3437`. It no longer states that hypothesis package.

The appropriate references are the actual comparison theorem `thm:brst-bar-genus0` and pairing corollary `cor:string-amplitude-genus0`, together with the affine and double-complex hypotheses when applicable. This is a dependency-reference defect introduced by changing the label's mathematical content.

### F8. A reader-facing task reference remains in the connected continuation

**MODERATE, manuscript firewall.** `cbc/chapters/theory/koszul_pair_structure.tex:1309`. Native PDF page 629.

The remark describes bulk reconstruction as a “downstream MC5 task.” This is a task assignment or workflow description. State the unresolved mathematical comparison directly. The three specific public024 phrases targeted in `concordance.tex` have been removed, but that does not establish a clean firewall for the connected surface.

## Bounded mathematical results preserved

The target definitions were read before the prior public024 verdict. The following conclusions rest on the displayed proofs and independent calculations.

### Polynomial reduction and associative bar

`cbc/chapters/theory/ds_chain_comparisons.tex:10–121` is correct on its declared algebraic carrier over C.

Write `V=-2e∂h+h∂f`. The differential is `(e-1)∂b+cV`, with left odd differentiation. Its two summands anticommute because `V(e-1)=0` and the odd operations anticommute. The resulting square vanishes on every generator and therefore on the full algebra.

Filtering by c-degree gives a finite filtration. The first differential resolves the regular element `e-1`. The quotient complex is `C[h,f] → cC[h,f]`. In coordinates `u=f+h²/4`, its differential is `-2c∂h`. Polynomial integration proves surjectivity, while its kernel is `C[u]`. The inclusion sends `u` to the closed element `ef+h²/4`. The projection restricts to its inverse on cohomology and satisfies `pi=1`.

The bar shift is cohomological: `|sa|=|a|-1`. The formulas `b1(sa)=-sDa` and `b2(sa⊗sb)=(-1)^|a|s(ab)` have degree one. The Leibniz rule and associativity cancel their mixed and quadratic terms. Augmentation preservation makes the tensorwise maps well-defined.

The length filtration proof of the bar quasi-isomorphism is valid without a bounded cohomological degree assumption. Every element has finite tensor length. Each cone quotient is acyclic over C. Removing the highest component of a cycle therefore terminates. No assertion about a product completion follows from this argument.

The projection's Poisson failure `p{h,f}=-2u`, `{p(h),p(f)}=0` is exact. Characteristic zero is essential to the primitive calculation. The source does not claim the result in positive characteristic.

### Second differential and quantum reduction boundary

`ds_chain_comparisons.tex:125–168` gives a valid finite-column comparison theorem. The decreasing p-filtration of the total mapping cone has the column cones as its quotients. The filtration is finite in every total degree. Columnwise acyclicity therefore proves total acyclicity.

The example `x∧-` and `∂x` has anticommutator one. It correctly refutes the claim that separate odd nilpotence ensures a double complex.

Arakawa's category definition is on page 585. Theorem 7.1(i), page 588, gives higher-cohomology vanishing and exactness on `KL_k`. The new text correctly requires termwise category membership and equivariant collision maps. These statements were checked in the primary paper linked above. They do not construct the missing collision action or a W target.

### Virasoro nilpotence levels and scalar transport

`ds_chain_comparisons.tex:171–283` preserves the universal vacuum carrier. Substituting into the existing operator identity gives `6k²+37k+56=(3k+8)(2k+7)`. Thus the full charge is nilpotent precisely at `k=-8/3,-7/2`, with `k=-2` excluded.

The cohomology statement uses the existing four-state vacuum calculation and nonzero-weight contraction. It does not infer Motzkin dimensions from the vacuum PBW character. The unchanged full Virasoro operator proof was not repeated in this review.

The affine reflection sums and the principal root-vector formula are algebraic identities. The sl2 and sl3 values are 26 and 100. Multiplication by `1/2` and `5/6` gives 13 and `250/3`. String ghosts contribute `-26` to central charge and `-13` to half-central charge. These normalizations remain separate from the operator coefficient `(C-26)/12`.

The equation `dY F=F dX` implies `dY² F=F dX²`. Injectivity gives the stated obstruction. A quasi-isomorphism of square-zero complexes alone supplies no anomaly comparison on a different carrier.

### Horizontal maps and torus cohomology

`ds_chain_comparisons.tex:285–327` is correct for bounded complexes of finite-rank flat bundles. On zero-forms, the total chain identity separates into the internal chain equation and horizontality. The sign `(-1)^p` makes the connection and internal differential anticommute in the total complex.

Local flat frames identify stalk maps with fiber maps. The cone has zero cohomology sheaves. Derived global sections then preserve the asserted equivalence.

For the torus local system, the cellular differential is `(λ-1)e1∧-`. Its contraction is `ιe1*/(λ-1)` when `λ≠1`. The exterior anticommutator is one. For `λ=1`, the differential vanishes and dimensions are `(1,2,1)`. This establishes the claimed obstruction to inferring global cohomology from fibers.

### Insertion integrals and MC transport

`cbc/chapters/theory/insertion_integrals.tex:3–47` correctly distinguishes the configuration space and its PGL2 quotient. Their complex dimensions are n and n−3. The compact moduli space is smooth and oriented for ordered genus-zero markings with n≥3.

For closed inputs, the insertion chain map sends changes by a boundary to an exact top form. Stokes' theorem makes integration descend to cohomology. Multilinearity forces every insertion-independent value to vanish. The n=3 multiplication example distinguishes the amplitude from a fixed nonzero Euler characteristic.

`cbc/chapters/theory/mc_transport.tex:5–104` uses the correct de Rham differential graded Lie algebra. On a closed oriented three-manifold, integration by parts and invariance of the form give `δS=(k/2π)∫〈δA∧FA〉`. Nonzero k and nondegeneracy imply flatness.

For the L-infinity statement, nilpotence of the Artinian ideal makes the exponential expressions finite. The coalgebra equation sends `e^(sα)` to `e^(sβ)` and intertwines coderivations. Projection gives the target MC equation. The two explicit examples correctly show that neither a linear chain quasi-isomorphism nor the Jacobi identities alone guarantee MC transport.

The standalone `consumer_geometry.tex` body matches the concatenated native insertion and MC sources exactly. Duplicate text does not count as independent mathematical evidence.

## Public024 consumer disposition

The complete six-message public024 record was read. Its final verdict equals the preserved `public024-final.md` after trimming terminal whitespace.

| Prior finding or consumer | Exact native026 disposition |
|---|---|
| Unconditional W semi-infinite theorem | Replaced by the finite double-complex theorem. The original chiral target remains unresolved. Connected W proof F1 remains. |
| Virasoro Motzkin cohomology transfer | Replaced by the correct nilpotence levels and the absolute/relative vacuum result. |
| Arbitrary amplitude equals Euler characteristic | Replaced by the insertion-chain proposition and explicit n=3 counterexample. |
| KM/W scalar anomaly cancellation | The cited propositions now distinguish affine scalar, Sugawara charge, principal reflection, and ghosts. Retained conflicts F2 and F5 remain. |
| `main.tex:621–624` and introduction claims | The corresponding native026 passages state the target and comparison requirements. |
| `concordance.tex` boundary/bulk claim | Rewritten at lines 3122–3126. The separate occurrence F4 remains. |
| `free_fields.tex:1629` Motzkin claim | Rewritten at lines 1629–1632. |
| Genus-one chain-isomorphism consumer | Replaced at lines 3852–3865 by the torus obstruction. The preceding modular theorem F3 remains. |
| Open-string and AGT claims | Rewritten at `holomorphic_topological.tex:307–346,709–750` with actual operator/scalar results and explicit comparison requirements. |
| MC and CS theorem cluster | Replaced by the correct de Rham and L-infinity statements. The immediate continuation F6 remains. |
| W framework anomaly summary and twisting arrow | Rewritten at lines 136–149. The enclosing theorem and its general scalar sum remain defective. |
| Matter–ghost augmentation instantiations | Replaced at `bv_brst.tex:189–195,1117–1122` by the augmentation obstruction and construction requirements. |
| Three cited concordance firewall phrases | Removed. The independent connected firewall occurrence F8 remains. |

## Evidence and limits

`source-verification.json` records each of the 76 independently recomputed source hashes and each baseline change comparison. `calculation-results.json` records the exact finite checks. `check_exact.py` is the executable input.

The calculation command is:

```sh
python3 reports/research/cbc_union_review026/check_exact.py
```

It uses Python 3.9.6 and rational arithmetic. It checks D² and the projection chain equation on 140 monomials. It checks the bar square on all 781 words of lengths zero through four in `e-1,h,f,b,c`. It checks the inclusion and retraction through the tenth power, the nilpotence levels, the B2 counterexample, and all four torus basis vectors. These finite checks support their declared calculations. They do not replace the general proofs above.

The native PDF has 1,644 pages and SHA-256 `769073656753dc0138235ae25a20707b97992259c24cef3459bbef41e0d92701`. Its bytes match the recorded build. Twenty-six native pages were independently rasterized with Poppler and visually inspected. They are listed with raster hashes in `render-binding.json`.

The inspected pages are 627–629, 886–887, 892–894, 979–981, 1331, 1363–1364, 1378–1383, 1430, 1435–1436, 1448, and 1458–1459. The new proofs are legible. The old false claims and the firewall occurrence are visible in the same reader artifact. No standalone PDF was opened or rebuilt.

The recorded native build retains ten undefined citations, one undefined reference, and two overfull boxes. This lane checked the PDF binding and affected rendered pages. It did not independently rerun the complete native build or certify every page.

The programme requires `gpt-6-astra` and `ultra` for mathematical review. Independent runtime metadata was not exposed through the available tools, so observed controls remain unverified. No configuration mismatch was observed.

Only `reports/research/cbc_union_review026/` was written. Mathematical sources were read-only. No staging, commits, pushes, or child assignments occurred.

## Residual proof obligations

The quantum chiral comparison still needs a unital collision target, its coefficient actions, compatible relative descent, and a specified section functor. It then needs actual symbol maps and compatible corrections. Quantum reduction additionally needs the affine module category conditions, equivariance, and valid totalization. Higher structures require separate operation, pairing, connection, and clutching equations.

The true polynomial theorem is useful progress on a separate classical associative carrier. It does not discharge these residual obligations.
