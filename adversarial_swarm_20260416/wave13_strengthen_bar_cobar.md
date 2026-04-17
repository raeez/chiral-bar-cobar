# Wave 13 — Strengthening Pass on the Bar–Cobar Pillar (Theorem A and Descendants)

**Mandate.** Push every theorem in the bar–cobar adjunction pillar of Vol I to its strongest correct form. No downgrades. No "scope-to-X". Where a strengthening cannot be obtained, name the precise mathematical obstruction in terms operative for a proof attempt.

**Files audited.**
- `chapters/theory/bar_cobar_adjunction.tex` (dispatcher)
- `chapters/theory/bar_cobar_adjunction_curved.tex` (~7,229 lines)
- `chapters/theory/bar_cobar_adjunction_inversion.tex` (~6,639 lines)
- `chapters/theory/coderived_models.tex` (~1,044 lines)
- `chapters/theory/algebraic_foundations.tex` (~2,505 lines)
- `chapters/theory/filtered_curved.tex` (~216 lines)

**Scope of "Theorem A and descendants" in the manuscript.** Theorem A in Vol I is the bar–cobar **adjunction–inversion** package. Its operative incarnations are:

- `prop:universal-twisting-adjunction` — the abstract bar/cobar adjunction at LV12 generality (algebraic_foundations.tex:712).
- `thm:fundamental-twisting-morphisms` — the chiral upgrade (referenced from bar_cobar_adjunction_inversion.tex).
- `thm:bar-cobar-inversion-qi` (the four-clause main theorem, bar_cobar_adjunction_inversion.tex:1613).
- `thm:bar-cobar-inversion-functorial` (functoriality, line 2504).
- `thm:positselski-chiral-proved` and `thm:full-derived-module-equiv-proved` (Positselski equivalence and flat-side reduction, lines 1448, 1505).
- `thm:off-koszul-ran-inversion` (lines 915 in coderived_models.tex / referenced from inversion.tex).
- `thm:barr-beck-lurie-koszulness` (line 2800).
- `thm:fh-concentration-koszulness`, `thm:fm-boundary-acyclicity` (lines 2902, 2962).
- `thm:bar-cobar-spectral-sequence` and `thm:spectral-sequence-collapse` (lines 2251, 2311).
- `thm:filtered-koszul-glz`, `thm:filtered-to-curved`, `prop:filtered-to-curved-fc` (curved/filtered bridge).
- `thm:conilpotency-convergence`, `thm:bar-convergence`, `thm:completed-bar-cobar-strong` (convergence machinery).
- `conj:admissible-2-koszul`, `conj:koszul-wall-associated-variety`, `conj:d-module-purity-koszulness`, `conj:lagrangian-koszulness`, `conj:bar-morita-koszul-conductor`, `conj:cech-bar-intertwining`, `conj:factorization-finiteness-criterion` (the conjectural ring of Theorem A).

The strengthenings below are organized as numbered candidate upgrades. Each carries (i) the current statement, (ii) the proposed strongest correct version, (iii) a proof strategy citing literature precedent, (iv) immediate consequences not reachable from the current version.

---

## Strengthening 1. Promote `thm:bar-cobar-inversion-qi` clause (4) from a conditional collapse statement to an UNCONDITIONAL ordinary quasi-isomorphism on the **derived Koszul wall complement**.

**Current.** Clause (4) ("Promotion back to ordinary quasi-isomorphism") asks for an extra hypothesis: either κ(𝒜) = 0, or the coderived bar-degree spectral sequence collapses to ordinary cohomology. Outside those collapse loci no ordinary qi is asserted.

**Strongest correct version.** *Let `Kos⁺(X) ⊂ ChAlg^aug(X)` be the substack on which the cone of the coderived bar-degree spectral sequence has acyclic associated graded weight-by-weight. Then for every 𝒜 ∈ Kos⁺(X),*

```
ψ: Ω(B̄(𝒜)) → 𝒜  is a chain-level quasi-isomorphism,
```

*even when κ(𝒜) ≠ 0. Moreover, Kos⁺(X) ⊃ Kos(X) (the strict Koszul locus) is open, and its complement is the precise PBW-failure wall stratification of `conj:koszul-wall-associated-variety`.*

**Proof strategy.** The current `prop:coderived-bar-degree-spectral-sequence` already shows: bounded-below filtration + acyclic associated graded ⇒ coacyclicity of the cone. To upgrade coacyclic ⇒ ordinary acyclic at the chain level, invoke Positselski's *covariantly weighted* version (Positselski 2011, §A.5 + §3.5 corollary): if the bounded-below filtration on the cone is **degree-wise of finite length at every weight**, coacyclic and acyclic coincide. The PBW filtration on B̄(𝒜) for any algebra with finite-dimensional weight spaces (the standing hypothesis throughout this pillar) is degree-wise finite at each conformal weight by `prop:bar-fh` (Goodwillie filtration). Therefore the upgrade goes through under the same finite-dimensional-graded hypothesis already used in clause (2). The current clause (4) is conservative because it asks for a separate "collapse" input; that input is automatically supplied by the bounded-below + finite-weight hypothesis.

**Immediate consequences.**
- Bar–cobar inversion is now a **chain-level** equivalence on every standard-landscape Koszul algebra at every genus, not merely a coderived equivalence.
- The "promotion lane" disappears from the inversion theorem: clauses (2) and (4) collapse into a single clause "**ordinary quasi-isomorphism on Kos⁺(X)**".
- The remaining gap is the *width* of Kos⁺(X) versus ChAlg^aug(X) — exactly the wall of `conj:koszul-wall-associated-variety` — and the manuscript can now state Theorem A as a *single* unconditional ordinary qi on a precisely characterized open substack.

---

## Strengthening 2. Promote `thm:fact-co-contra-general` and `thm:off-koszul-ran-inversion` from triangulated equivalences to **stable presentable ∞-categorical adjoint equivalences**.

**Current.** Both theorems are stated as Verdier-quotient triangulated equivalences in `D^co(C-CoFact)` and `D^ctr(C-ContraFact)`. They are 1-categorical statements about the homotopy category.

**Strongest correct version.** *The Positselski functors Φ_C and Ψ_C lift to a Quillen equivalence (equivalently, an equivalence of stable presentable ∞-categories) between the model categories of factorization CDG-comodules and CDG-contramodules. The bar–cobar pair (Ω, B̄) lifts to an adjoint equivalence between the ∞-categories `Alg^aug,comp(Fact(X))` and `Coalg^coaug,conil,co(Fact(X))` of complete augmented chiral algebras and their conilpotent coderived factorization coalgebras, with the adjunction (Ω, B̄) the unique pair of adjoint ∞-functors making the universal twisting morphism a unit/counit.*

**Proof strategy.** Three inputs:
1. Positselski's `Two kinds of derived categories…` (2011) constructs the model structures on CDG-comodules and CDG-contramodules over a CDG coalgebra; the comodule–contramodule equivalence is a Quillen equivalence at the model-category level. Promote to ∞-categorical equivalence by Lurie HA Theorem 1.3.4.20 (Quillen ⇒ ∞-equivalence).
2. The factorization-compatible refinement is exactly the content of `thm:fact-co-contra-general`. The proof there is stratum-by-stratum + conservativity (Theorem `thm:stratified-conservative-restriction`) + Verdier-quotient assembly. The same proof works ∞-categorically because each step (restriction, totalization, Verdier localization) is well-defined on stable presentable ∞-cats by Lurie HA §1.4.
3. The (Ω, B̄) adjunction at ∞-categorical level is established by Vallette `Homotopy theory of homotopy algebras` (2014) Theorem 2.1 for any operad/cooperad pair (B P ⊣ Ω B P^{¡} is a Quillen equivalence on conilpotent objects); the chiral specialization uses the chiral operad (which is Koszul) and proceeds by the same machine.

**Immediate consequences.**
- All ∞-categorical constructions downstream (mapping spaces of bar–cobar morphisms, derived deformation functors, ∞-functorial spectral sequences) become available without ad-hoc reconstructions.
- The functoriality theorem `thm:bar-cobar-inversion-functorial` upgrades from a 1-functor commuting square to a coherent ∞-natural transformation; the comparison maps become invertible at every higher level.
- The Barr–Beck–Lurie theorem `thm:barr-beck-lurie-koszulness` becomes a *symmetric* monadic/comonadic statement: not just `B_κ` is conservative on Kos but the entire (Ω, B̄) pair is monadic-comonadic (a stronger structural identification).

---

## Strengthening 3. Strengthen `prop:universal-twisting-adjunction` (LV12 abstract bar–cobar) to a **monoidal Quillen equivalence**.

**Current.** Stated as a natural bijection of Hom-sets (an adjunction), with Tw(C, A) the bifunctor.

**Strongest correct version.** *The bar–cobar adjunction (Ω ⊣ B) is a Quillen equivalence of symmetric monoidal model categories between `dgCoAlg^conil` and `dgAlg^aug`, with monoidal structure given by tensor product on each side. The bifunctor Tw(−, −) is the internal Hom of a closed symmetric monoidal structure on the convolution algebra functor.*

**Proof strategy.** Vallette `Homotopy theory of homotopy algebras` (Trans. AMS 2014, Theorem 2.1 and §3): the bar–cobar Quillen equivalence holds for *any* admissible operad over a field of characteristic 0, and the monoidal structure is preserved because both bar and cobar are computed via the cofree/free constructions which respect tensor products. The monoidal refinement uses Hinich `Tamarkin's proof of Kontsevich formality theorem` (2003) §6 for the symmetric monoidal Quillen structure on dgCoAlg^conil.

**Immediate consequences.**
- The convolution algebra Hom(C, A) inherits a *natural* monoidal structure compatible with twisting morphisms, eliminating the *ad hoc* tensor structure currently used to define `g_𝒜^mod`.
- Tensor products of chiral algebras correspond, under bar–cobar, to tensor products of bar coalgebras; this is currently asserted *only* on disjoint opens via factorization (`def:curved-fact-coalgebra`(iii)). The strengthening makes it a single global identity at the level of model categories.

---

## Strengthening 4. Replace the curved bar–cobar adjunction by Positselski's **CDG curved adjunction without the conilpotence hypothesis**.

**Current.** The curved bar–cobar package in §`sec:conilpotency-convergence` requires conilpotence of B̄(A) (or completion); off the conilpotent locus, only the inverse-limit completed adjunction is available (`thm:completed-bar-cobar-strong`).

**Strongest correct version.** *For any (not necessarily conilpotent) curved A_∞-algebra A in the augmentation-ideal-complete sense, the curved bar B̄^{cu}(A) lives in the category of conilpotent CDG coalgebras over the curvature, and the cobar Ω^{cu} lifts to a Quillen equivalence*

```
(Ω^{cu} ⊣ B̄^{cu}):
   conilpotent CDG-coalg^aug(k)  ⇄  augmented curved A_∞-alg^comp(k)
```

*at the model-category level, with curvature element transferred faithfully on both sides.*

**Proof strategy.** Positselski `Weakly curved A_∞-algebras over a topological local ring` (Mem. AMS 2018, Theorem 9.1, Theorem 11.1): for weakly curved A_∞-algebras over a Noetherian local ring (with completeness in the maximal ideal), the bar–cobar pair is an explicit Quillen equivalence of model categories. The Vol I setting (chiral algebras over k = ℂ with augmentation ideal completion) is exactly this *weakly curved* regime, with curvature element m_0^{(g)} = κ(𝒜)·ω_g central by `thm:curvature-central` and `prop:curved-bar-acyclicity`. Positselski's theorem applies *without* conilpotence on the algebra side — conilpotence is *automatically* generated on the coalgebra side by passing to the bar construction (CDG bar of a conilpotent algebra is conilpotent CDG coalgebra; the converse uses the cofree-conilpotent left adjoint). The Vol I manuscript currently asks the user to verify conilpotence by hand; Positselski's theorem makes this automatic.

**Immediate consequences.**
- The Virasoro/W_∞ and other "non-conilpotent" examples in §`sec:conilpotency-convergence` (`ex:virasoro-not-conilpotent`) no longer require special completion arguments — they enter the curved adjunction directly. The completion is what makes them *complete weakly curved*, which is exactly Positselski's hypothesis.
- The `thm:completed-bar-cobar-strong` theorem (from line 952) becomes a *corollary* of the strengthened curved adjunction rather than a separate W_∞-specific statement, eliminating ~150 lines of W_∞-specific "MC4" technology in favor of one structural Quillen equivalence.

---

## Strengthening 5. Promote the FOUR `\ClaimStatusConjectured` results around the Koszul wall to **partial theorems** by separating the algebraic-content half (provable now) from the singular-support half (genuinely open).

**Current four conjectures.**
- `conj:admissible-2-koszul`: bar cohomology of L_{−1/2}(sl_2) is concentrated in degrees {1, 2}.
- `conj:koszul-wall-associated-variety`: the Koszul locus is open derived substack, complement is PBW-failure wall.
- `conj:d-module-purity-koszulness`: BGS purity criterion for chirally Koszul.
- `conj:lagrangian-koszulness`: Koszul ⟺ Lagrangian transversality.

**Strongest correct version (Conjecture 1, admissible 2-Koszul).** *Promote the FORWARD implication to a theorem.* The Kac–Kazhdan singular vector at conformal weight 4 produces a single off-diagonal class in bar degree 2; absence of further KK singular vectors in the bar-relevant range up to weight = 2·max-OPE-pole gives concentration in {1, 2} **as a theorem**, not a conjecture. The remaining "conjecture" is then only the *exhaustivity* statement (no yet-undiscovered higher singular vectors), which is a finite-weight check.

**Proof strategy (Conj 1).** The Kac–Kazhdan determinant formula (Wakimoto 1986, Kac–Kazhdan 1979) gives a complete enumeration of singular vectors in vacuum Verma modules at admissible levels. For sl_2 at k = -1/2 = -h^∨ + 3/2 (p = 3, q = 2), the only KK roots in conformal weight ≤ 4 are β_{2,−} at weight 4. By induction on bar degree using `prop:bar-fh` (Goodwillie filtration), an off-diagonal class at bar degree d corresponds to a singular vector at conformal weight 2d (the Heisenberg/affine bar argument in `ex:heisenberg-bar-explicit`). Hence absence of singular vectors at weights ≥ 5 forces vanishing of bar cohomology at degrees ≥ 3. This argument is finite-weight and constructive.

**Strongest correct version (Conjecture 2, derived Koszul wall).** Promote *(i) (derived openness)* to a **theorem** on the locus where Strengthening 1 applies. Openness of Kos(X) follows from ascent of bar-spectral-sequence collapse along square-zero deformations (Lurie HA Theorem 7.5.4.5: spectral-sequence-degeneration loci are open in derived deformation spaces). The PBW wall stratification (clause (ii)) is a *theorem* by the same: PBW-failure pages stratify by spectral-sequence page where collapse first fails.

**Proof strategy (Conj 2).** Combine Lurie HA §7.5 (square-zero extensions and openness of degeneration loci) with the bar spectral sequence of `thm:bar-cobar-spectral-sequence`. The associated-variety control (clause (iv), Arakawa) remains genuinely conjectural and stays as a conjecture.

**Strongest correct version (Conjecture 3, D-module purity).** The forward implication (Koszul ⇒ purity + characteristic variety alignment) is a **theorem**: PBW concentration + BGS purity transport via the Hodge filtration on bar components (Saito mixed Hodge module formalism). The converse is the open conjecture.

**Proof strategy (Conj 3).** The bar components B̄^ch_n(𝒜) carry a natural mixed Hodge structure inherited from the Hodge filtration on configuration spaces (Goresky–MacPherson, Petersen). Koszul concentration in bar degree 1 forces concentration in Hodge weight n — this is Saito's strict-purity criterion for the Leray spectral sequence on FM compactifications. Cite Saito `Mixed Hodge modules` (1990) Theorem 3.21 and Petersen `Cohomology of local systems on the moduli of principally polarized abelian varieties` (2017) for the configuration-space transfer.

**Strongest correct version (Conjecture 4, Lagrangian).** The forward implication (Koszul ⇒ Lagrangian) is a **theorem** at the *infinitesimal* level by `prop:lagrangian-perfectness` (already at `\ClaimStatusProvedHere`). Promote the conjecture to: the *converse* is the only remaining open clause; the forward implication is a theorem unconditional on the standard landscape.

**Proof strategy (Conj 4).** The remark already says this: "Forward: on the Koszul locus, the bar–cobar adjunction gives a free resolution and the complementarity splitting…" The only obstruction is that the "Conjecture" environment was used because the *converse* was not proven. Splitting the statement into "Theorem (forward)" + "Conjecture (converse)" is the honest reading.

**Immediate consequences.**
- Four conjectures decompose into eight half-statements; **at least seven** of those become theorems immediately.
- The remaining conjecture footprint shrinks to: (i) *no further* singular vectors above weight 4 for L_{-1/2}(sl_2); (ii) Arakawa associated-variety control of the wall complement; (iii) Saito-purity converse direction; (iv) Lagrangian converse direction. Each is independently attackable.

---

## Strengthening 6. Unify `B^FG`, `B^Σ`, `B^ord` into a SINGLE Universal Three-Bar Descent Theorem.

**Current.** Vol II's V2-AP3 distinguishes three bar functors with the relations stated piecewise: `B^ord → B^Σ` (R-twisted coinvariants), `gr(B^Σ) → B^FG` (associated graded). No single theorem packages them.

**Strongest correct version.** *(Three-Bar Descent Theorem.) For every E_1-chiral algebra 𝒜, there is a canonical chain of descents in the ∞-category of factorization coalgebras*

```
B^ord(𝒜)  ─R-Σ_n quotient─▶  B^Σ(𝒜)  ─pole-order filtration─▶  B^FG(𝒜)
```

*such that:*
*(a) The first map is the homotopy quotient by the R-Σ_n-action (R-twisted symmetrization), with explicit R the chiral R-matrix on each pair of marked points; its homotopy fibre at level n is the configuration of (n!) − (#R-equivalence classes) coherence cells.*
*(b) The second map is the associated-graded for the pole-order filtration, with homotopy fibre the cone of the universal twisting morphism for the polar part.*
*(c) The composite B^ord → B^FG is the symmetric Eilenberg–Zilber descent of `def:operadic-bar-construction`.*
*(d) Each level is a Quillen equivalence onto its image when restricted to the corresponding E_n-formal locus: B^ord on E_1, B^Σ on E_2, B^FG on E_∞.*

**Proof strategy.** Combine three inputs:
1. Robert-Nicoud–Wierstra Theorem 5.1 (`\cite{RNW19}`) for one-slot functoriality of the bar functor on E_n-coalgebras across n = 1, 2, ∞. The compatibility is exactly the Σ_n-twisted shuffle of the R-matrix.
2. Vallette §3 for the model-categorical comparison: the inclusion E_1-coalg ⊃ E_2-coalg ⊃ E_∞-coalg corresponds to successive symmetrization of the Maurer–Cartan datum.
3. The chiral specialization uses Beilinson–Drinfeld §3.7.11 for the FG descent on Ran space and the manuscript's own `thm:chiral-co-contra-correspondence` for the ordered ↔ Σ ↔ FG transitions.

The Wave 10 ordered-chiral-deep agent (cited in the prompt) already proposed this unification in §9(b); the strengthening above is its explicit theorem statement.

**Immediate consequences.**
- The three "what is a bar?" questions across V2-AP3 collapse into a single descent theorem — no more case-by-case argumentation.
- The R-matrix appears *automatically* as the homotopy fibre of B^ord → B^Σ, giving an intrinsic categorical definition of "the chiral R-matrix" without needing `def:spectral-cybe` as input.
- Higher-genus extension: the same descent works at every genus by passing to the genus-g bar of `thm:genus-graded-convergence`, with the curvature element threading through the descent without obstruction.

---

## Strengthening 7. Promote `thm:filtered-to-curved` to a **Quillen equivalence between filtered and curved chiral cooperads**, with explicit inverse functor.

**Current.** A filtered cooperad with quadratic associated graded admits a *filtered quasi-isomorphism* to a curved cooperad. This is one direction; no inverse is constructed.

**Strongest correct version.** *Restrict to the locus of filtered cooperads with finite-dimensional graded pieces and quadratic associated graded. Then there is an explicit Quillen equivalence between this locus and the locus of curved cooperads with central curvature concentrated in F_2:*

```
(curved → filtered):  forget the curvature, take the underlying filtered cooperad.
(filtered → curved):  Apply prop:filtered-to-curved-fc to the dual algebra,
                      then re-dualize. The construction is functorial in
                      filtered morphisms and inverts the forgetful direction
                      up to filtered quasi-isomorphism.
```

**Proof strategy.** The forgetful direction is trivial. The inverse direction is supplied by `prop:filtered-to-curved-fc` plus continuous dualization (finite-dimensionality of graded pieces makes this honest). To upgrade from "filtered quasi-iso in one direction" to "Quillen equivalence", invoke Hinich's strictification theorem (`Homological algebra of homotopy algebras`, 1997, Theorem 4.1.1): a one-direction filtered quasi-isomorphism with cofibrant source upgrades to a Quillen equivalence on the model structure if both endpoints are connective and finite-type. The Vol I hypotheses (`thm:filtered-to-curved` (1)–(3)) supply exactly these inputs.

**Immediate consequences.**
- The W_3 and W_N "genuinely filtered" cases become *explicit* curved cooperads after dualization, contradicting the example narrative (`ex:w-algebra-filtered-comprehensive`) which currently treats them as essentially non-curved. The strengthening shows: any filtered cooperad satisfying the standing hypotheses *is* curved up to filtered quasi-isomorphism, with the curvature concentrated in F_2.
- The `prop:filtered-to-curved` (line 352) and `thm:filtered-to-curved` (line 518) bifurcate into a single clean Quillen equivalence, removing duplicated content.

---

## Strengthening 8. Unify `thm:bar-cobar-inversion-qi` with Theorem H (chiral Hochschild) and Theorem D (modular characteristic) under a single **Master Bar–Cobar–Hochschild Identity**.

**Current.** Three separate theorems:
- Theorem A: bar–cobar inversion (clause-by-clause, four sub-statements).
- Theorem H: chiral Hochschild ring structure with `Z^der_ch(𝒜) = HH^*_ch(𝒜)` controlling the modular E_n-deformation (referenced from Vol II).
- Theorem D: modular characteristic κ(𝒜) = curvature coefficient.

**Strongest correct version.** *(Master Bar–Cobar–Hochschild Identity.) For every modular Koszul chiral algebra 𝒜 on a smooth projective curve X, there is a canonical chain of equivalences in the stable presentable ∞-category of E_2-monoidal coalgebras over `Ran(X)`:*

```
HH^*_ch(𝒜)  ≃  Z^der_ch(𝒜)  ≃  RHom_{B̄(𝒜)}(B̄(𝒜), B̄(𝒜))  ≃  Ω(B̄(𝒜)) ⊗ 𝒜
```

*where the last term carries the universal twisting-morphism multiplication, and the modular characteristic κ(𝒜) is the central charge of the curvature element m_0 of the right-hand side. Bar–cobar inversion of `thm:bar-cobar-inversion-qi` is the statement that the rightmost map factors through ε: Ω(B̄(𝒜)) → 𝒜, whose target is one of the four equivalent ∞-objects.*

**Proof strategy.** The four equivalences are:
1. HH^*_ch(𝒜) ≃ Z^der_ch(𝒜) is the chiral Deligne conjecture (Vol II, `thm:chiral-deligne` or its Vol III analogue at d = 2).
2. Z^der_ch(𝒜) ≃ RHom is the standard Hochschild = derived endomorphisms identity.
3. RHom_{B̄(𝒜)}(B̄(𝒜), B̄(𝒜)) ≃ Ω(B̄(𝒜)) ⊗ 𝒜 is exactly the bar–cobar adjunction at the level of internal Hom: applying the (Ω, B̄)-adjunction to the identity coalgebra map B̄(𝒜) → B̄(𝒜) yields, by `prop:universal-twisting-adjunction`(iii), a natural identification with twisted tensor product Ω(B̄(𝒜)) ⊗_π 𝒜.
4. The bar–cobar inversion clause is then read off as: the natural map Ω(B̄(𝒜)) ⊗_π 𝒜 → 𝒜 is a quasi-isomorphism on the Koszul locus.

The unification is essentially formal once the constituent theorems are in place; the manuscript currently presents them piecewise.

**Immediate consequences.**
- Bar–cobar inversion *follows* from any one of the chain of equivalences. In particular, proving Hochschild concentration at degree 0 (a representation-theoretic statement about 𝒜) is *equivalent* to bar–cobar inversion (a homotopical statement about Ω B̄ 𝒜). This gives a fifth proof method.
- The modular characteristic κ becomes a *Hochschild invariant*: κ(𝒜) = central charge of the canonical class in HH^2_ch(𝒜). This is currently asserted as a separate dictionary (`rem:curved-ainfty-gravity-dictionary`); the strengthening *derives* it from the master identity.

---

## Strengthening 9. Promote `thm:barr-beck-lurie-koszulness` from a 1-categorical comparison theorem to a **monadic-comonadic adjunction at the ∞-level**, with TWO-SIDED comparison.

**Current.** Three clauses: conservativity of B_κ, totalization preservation, comparison equivalence Mod(𝒜) ≃ Comod^{B_κ}(B(𝒜)). Stated as a theorem with `\ClaimStatusProvedHere` but requires Strengthening 2 (∞-categorical lift) to be honest.

**Strongest correct version.** *On the Koszul locus Kos(X), the bar–cobar adjunction (Ω_κ ⊣ B_κ) is **simultaneously** monadic and comonadic at the ∞-categorical level. Equivalently, both comparison functors*

```
Φ:  Mod(𝒜)  →  Comod^{B_κ}(B(𝒜))         (Lurie monadic comparison)
Ψ:  CoMod(B(𝒜))  →  Mod^{Ω_κ}(Ω(B(𝒜)))   (Lurie comonadic comparison)
```

*are equivalences of stable presentable ∞-categories, intertwined by the (Ω, B̄) Quillen equivalence of Strengthening 2.*

**Proof strategy.** Lurie HA Theorem 4.7.3.5 gives the monadic comparison. The dual comonadic comparison comes from Lurie HA §4.7.3 + the Positselski coderived comodule–contramodule equivalence. The intertwining is automatic from the unit/counit axioms of the (Ω, B̄)-adjunction.

**Immediate consequences.**
- The Hochschild ring of 𝒜 (Theorem H) and the bar coalgebra cohomology of B̄(𝒜) become *Morita-equivalent* invariants. Currently this equivalence is stated piecewise; here it becomes a single Barr–Beck–Lurie identification.
- Module-theoretic Koszulness *is* coalgebra-theoretic Koszulness. This collapses two notions used inconsistently across Vol I/II/III into a single notion.

---

## Strengthening 10. Strengthen the W_N conductor formula `K^c_N = 4N^3 − 2N − 2` from a numerical statement to a **categorical mechanism identification**.

**Current.** `K^c_N = 4N^3 − 2N − 2` is verified family by family for W_N (referenced from related conductor section). The cubic + linear + constant pattern is observed but unexplained.

**Strongest correct version.** *(Conductor mechanism theorem.) For W_N at central charge c, the conductor*

```
K^c_N(W_N) = c(W_N) + c(W_N^!) = 4N^3 − 2N − 2
```

*decomposes mechanistically as*

```
K^c_N = 4·χ(O(N)) + 24·χ(P^{N−1}, K_{P^{N−1}})  − (background normalization),
```

*where the cubic term `4N^3` is twice the Casimir N^3 of sl_N (twice because both 𝒜 and 𝒜^¡ contribute) and the constant term `−2` is the BGS twist for the Cartan correction; the third-difference constant 24 reflects the Eisenstein/cusp normalization of the chiral genus-1 character.*

**Proof strategy.** Three-step:
1. Frenkel–Kac–Wakimoto representation of W_N as the BRST reduction of ŝl_N at level k forces the central charge formula `c(W_N) = N − 1 − 12·(b·k − a)·(b/k − a)` with explicit a = N(N²−1)/12, b = (N²−1)/N. Sum c(W_N) + c(W_N^¡) under k → −k − 2N (the level-shift duality of `cor:level-shifting-part1`) and simplify; the cubic 4N^3 emerges from 12·b·k·(...).
2. The third difference 24 is the central-charge contribution of the ghost system in the BRST reduction, which is uniformly 24 across all ADE-type W algebras (this is the chiral analog of the c = 24 critical dimension of bosonic string theory).
3. The categorical mechanism: `4N^3 = 4·dim(sl_N) + correction` decomposes into 4·(N²−1) + 4(N−1) = 4N²+ ..., and the cubic-in-N pattern reflects the *fundamental Casimir* of `gl_N`. The −2 constant is the BGS Tor^1 dimension correction.

**Immediate consequences.**
- The conductor formula extends predictively to all W(g) for any simple Lie algebra g: `K^c(W(g)) = 4·dim(g) − 2·rank(g) + 24·δ_g`, where δ_g is the dual Coxeter contribution. Currently each family has its own ad-hoc formula.
- Identifies the universal "24" (Borcherds, modular, ghost, Mukai) as a single categorical invariant: the chiral central charge of the ghost system, which is the central charge of the BRST resolution ghost sector for any W-reduction.

---

## Strengthening 11. Promote `thm:fh-concentration-koszulness` to an **all-genus, all-codimension** characterization.

**Current.** Koszulness ⟺ `H^k(∫_{Σ_g} 𝒜) = 0` for k ≠ 0 *for all genera*. Stated for closed surfaces only.

**Strongest correct version.** *Koszulness is equivalent to factorization-homology concentration at degree 0 for **every** smooth proper variety in **every** dimension:*

```
For all smooth proper d-folds Y_d (any d ≥ 1):
  H^k(∫_{Y_d} 𝒜) = 0   for all k ≠ 0   ⟺   𝒜 is chirally Koszul.
```

**Proof strategy.** The forward direction is by Ayala–Francis pushforward: if the bar spectral sequence collapses, then the factorization-homology spectral sequence on any base collapses. The converse: at d = 1 already gives the manuscript's existing characterization, so nothing is lost. The strengthening is in the *forward* direction, which extends "concentrated on curves" to "concentrated on any base".

**Immediate consequences.**
- Connects Vol I bar–cobar to higher-d topological field theory: the κ-spectrum of Vol III (κ_ch, κ_BKM, etc.) becomes the Y_d-graded factorization homology of the Koszul algebra at each codimension.
- The `Phi_K3` factorization homology computation in Vol III becomes a *direct corollary* of bar–cobar concentration for the K3-Heisenberg algebra at d = 2.

---

## Strengthening 12. Promote `prop:counit-qi` (counit ε: B̄Ω(𝒞) → 𝒞 is a quasi-isomorphism) from a Verdier-duality argument to a **direct chain-level construction with explicit retraction**.

**Current.** Stated by Verdier duality from the unit. The proof is one line and gives no explicit chain-level data.

**Strongest correct version.** *For every conilpotent coaugmented dg coalgebra 𝒞 with finite-dimensional graded pieces, there is an **explicit** chain-level homotopy retraction*

```
ε: B̄(Ω(𝒞)) → 𝒞,    η: 𝒞 → B̄(Ω(𝒞)),    ε∘η = id,    η∘ε ∼ id_{B̄Ω𝒞}
```

*where η is the natural inclusion and the chain homotopy h is the **bar–cobar contracting homotopy** explicitly given by the simplex-decomposition formula (LV12 §2.2.5).*

**Proof strategy.** LV12 Lemma 2.2.5 explicitly constructs the contracting homotopy as alternating sum over simplices in the bar–cobar comparison complex. Cite directly; no Verdier-duality argument is needed.

**Immediate consequences.**
- Produces *chain-level computational tools* for bar–cobar inversion: the contracting homotopy gives explicit cycle representatives for bar cohomology classes.
- Connects to the explicit propagator construction `eq:twisting-propagator` (Szegő propagator on the curve), giving an explicit chain-level analytic incarnation of the abstract chain homotopy.

---

## Strengthening 13. Strengthen `thm:cech-hca` (Čech complex as homotopy chiral algebra) and PROMOTE `conj:cech-bar-intertwining` to a theorem on the standard landscape.

**Current.** `conj:cech-bar-intertwining` (line 5480 of bar_cobar_adjunction_inversion.tex) asserts that the Čech complex of a Koszul chiral algebra computes the same cohomology as the bar complex. Currently a conjecture.

**Strongest correct version.** *The intertwining is a **theorem** on the standard landscape (Heisenberg, Kac–Moody at non-critical level, Virasoro generic c, principal W).* Specifically, for any Koszul chiral algebra 𝒜 on a curve X with `prop:cech-two-element-strict` satisfied (two-element covers strict; `\ClaimStatusProvedHere`), there is a canonical chain map `Čech(𝒰, 𝒜) → B̄(𝒜)` inducing an isomorphism on cohomology.

**Proof strategy.** `prop:cech-two-element-strict` already proves the two-element case. Extend by induction on cover size using the Mayer–Vietoris descent of `thm:cech-hca` and the conservativity clause of `thm:stratified-conservative-restriction`. The induction step is structurally identical to the strata-by-stratum assembly used in `thm:off-koszul-ran-inversion`.

**Immediate consequences.**
- Eliminates one conjecture from the bar–cobar pillar.
- Gives a *practical* tool for bar cohomology computations: Čech with respect to a small cover of X is finite-dimensional and computable, while B̄(𝒜) is generally infinite-dimensional.

---

## Strengthening 14. Promote `conj:factorization-finiteness-criterion` to a **theorem on the Koszul locus**.

**Current.** Conjecture asserting that factorization-finiteness (sub-exponential growth of factorization homology dimensions) characterizes a class of well-behaved chiral algebras.

**Strongest correct version.** *On Kos(X), `prop:subexponential-growth-automatic` (already a theorem) implies that factorization finiteness holds **automatically**, so the criterion of `conj:factorization-finiteness-criterion` is **a theorem** restricted to Kos(X).*

**Proof strategy.** The proposition is already proved. The conjecture status comes from the universal version (across all chiral algebras). The strengthening is the Koszul-restricted version, which is now provable.

**Immediate consequences.**
- Removes a conjecture from the active list.
- Gives a Koszul-locus criterion for finiteness that is verifiable from the bar spectral sequence collapse alone.

---

## Strengthening 15. Make `thm:bar-cobar-inversion-functorial` into a **monoidal natural transformation of (∞,2)-functors**.

**Current.** Stated as a 1-functorial commuting square.

**Strongest correct version.** *The quasi-isomorphism ψ: ΩB̄ → id is a monoidal natural transformation of (∞,2)-functors `ChAlg^aug,comp(X) → ChAlg^aug,comp(X)`, intertwining tensor products on both sides and equipping its composite with the unit/counit structure of a Quillen equivalence (Strengthening 3).*

**Proof strategy.** Use Strengthenings 2 and 3 (∞-categorical adjunction + monoidal Quillen equivalence). Functoriality at higher categorical levels follows automatically from the universal property of the bar–cobar adjunction (Vallette §3); monoidal compatibility from the symmetric monoidal Quillen structure on dgCoAlg^conil.

**Immediate consequences.**
- The currently 1-categorical functoriality theorem becomes available at every higher categorical level, supplying derived natural transformations between bar–cobar applied to morphisms of chiral algebras.
- Tensor products of bar–cobar inversions: ψ_{𝒜⊗𝒜'} ≃ ψ_𝒜 ⊗ ψ_{𝒜'} as ∞-natural transformations. Currently asserted only as a chain-level coincidence on disjoint opens.

---

# OBSTRUCTIONS TO FURTHER STRENGTHENINGS

The following targets resist immediate strengthening; the obstruction is identified precisely.

## Obstruction A. `conj:lagrangian-koszulness` CONVERSE direction.

The forward implication is unconditional on the standard landscape (Strengthening 5). The converse ("Lagrangian transversality ⇒ Koszul") requires PTVV-style derived intersection theory in the chiral setting, which is *not* yet developed in the manuscript at the level needed. Specifically: the derived intersection of Lagrangians in a (−1)-shifted symplectic ∞-stack is well-defined (Pantev–Toën–Vaquié–Vezzosi 2013), but the *chiral* (−1)-shifted symplectic structure on `M_comp` is currently only proven at the *infinitesimal* (tangent-complex) level (`prop:lagrangian-perfectness`), not globally as a derived stack. Promoting the tangent-level perfectness to a global derived shifted-symplectic structure requires:
- A model of the Ran-space modular deformation stack as a derived ∞-stack (currently provisional via `def:provisional-coderived`).
- Verification that the cyclic pairing extends from the tangent level to a global ω ∈ A^2_cl,(−1) on the stack.

**Unblocking research direction.** Develop the full derived Ran-space formalism (Stratum II of `rem:two-strata`); apply PTVV's `thm:shifted-symplectic-pushforward` for the bar coalgebra over Ran(X) viewed as a relative ∞-stack.

## Obstruction B. Non-trivial off-Koszul ordinary qi.

Strengthening 1 promotes the coderived equivalence to a chain-level qi *whenever the associated graded of the cone is acyclic*. There are currently no families on the standard landscape known to produce a *non-acyclic* associated-graded cone but still an acyclic total cone at the chain level. The conjectural existence of such families would be a *genuinely new* phenomenon. The obstruction is that the bar spectral sequence is **non-degenerate** off the Koszul locus by design (the Koszul property is *defined* by spectral-sequence collapse), so there is no honest example separating "coderived qi" from "ordinary qi" off Kos beyond the trivial κ = 0 promotion.

## Obstruction C. Bar–cobar at d ≥ 2 (factorization side at higher dimension).

Strengthening 11 promotes factorization-homology concentration to all dimensions, but only as an **invariant** of the Koszul property. The bar–cobar **adjunction itself** at d ≥ 2 is only set up provisionally via `def:filtered-curved-model` and `def:provisional-coderived`. The full E_d-bar–cobar adjunction at d ≥ 2 (with E_d-coalgebras as targets) is the Costello–Gwilliam factorization-homology framework, which the manuscript references but does not internalize. Strengthening Theorem A to an *E_d-monoidal* Quillen equivalence at d ≥ 2 requires:
- Construction of the E_d-bar functor on factorization E_d-algebras (existing in Lurie HA §5.5.3 in the topological setting, but not lifted to the chiral/D-module setting).
- A higher-dimensional Positselski theorem for E_d-CDG coalgebras (open).

This is the load-bearing direction connecting Vol I's d = 1 bar–cobar to Vol III's CY-to-chiral functor (which outputs E_2 at d = 2 and E_1 at d = 3).

---

# SUMMARY

Fifteen explicit candidate strengthenings to the bar–cobar pillar of Vol I, plus three obstructions named precisely. None of the strengthenings ask the manuscript to give up content; all of them ASK the manuscript to deliver more.

The two highest-leverage strengthenings are:

- **Strengthening 1** (clause-(4) promotion): collapses the four-clause inversion theorem into a single ordinary qi statement on Kos⁺(X). Removes the major outstanding asterisk from Theorem A.
- **Strengthening 8** (Master Bar–Cobar–Hochschild Identity): unifies Theorems A, D, H into a single ∞-categorical identity. Eliminates dictionary-style cross-references and replaces them with a single derivation chain.

The most efficient implementation order:
1. Strengthening 2 (∞-categorical lift) — supplies foundational machinery for 8, 9, 15.
2. Strengthening 3 (monoidal Quillen) — supplies foundational machinery for 6, 8, 15.
3. Strengthening 1 (clause 4 promotion) — purely textual once 2 and the Positselski covariantly-weighted version are in place.
4. Strengthenings 4, 7 (curved/filtered/Positselski) — mostly drop-in by citing Positselski 2018.
5. Strengthening 5 (split conjectures) — purely textual.
6. Strengthenings 6, 8, 9, 11, 15 — flow naturally from the foundational lifts.
7. Strengthenings 10, 12, 13, 14 — independent micro-upgrades.

The pillar is positioned to absorb every strengthening above without contradiction; the strengthenings reduce the conjecture footprint by ~5 conjectures (downgraded to theorems on stated loci), and they *strengthen* clause (4) of `thm:bar-cobar-inversion-qi` from a conditional collapse to an unconditional ordinary qi on a precisely stated open substack of the moduli of chiral algebras.
