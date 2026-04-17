# Wave 5 — Adversarial audit of the bar/cobar machinery (Vol I)

Scope: `chapters/theory/{bar_construction,cobar_construction,bar_cobar_adjunction,
bar_cobar_adjunction_curved,bar_cobar_adjunction_inversion,algebraic_foundations,
coderived_models,filtered_curved}.tex`. Read-only audit; no edits to the manuscript;
no commits. Goal: force the strongest correct version of every load-bearing claim
into view, with attack/defense/repair, line numbers, and upgrade paths.

Files audited (line counts):

| File | Lines |
|---|---:|
| `bar_construction.tex` | 2536 |
| `cobar_construction.tex` | 3491 |
| `bar_cobar_adjunction.tex` (dispatcher) | 5 |
| `bar_cobar_adjunction_curved.tex` | 7229 |
| `bar_cobar_adjunction_inversion.tex` | 6639 |
| `algebraic_foundations.tex` | 2505 |
| `coderived_models.tex` | 1044 |
| `filtered_curved.tex` | 216 |

These eight files carry the categorical engine that every later result (Theorems
A–H, Yangian, modular Koszul, higher genus) depends on. If anything below is
wrong, large parts of the manuscript fall.

---

## Section 1 — Triage of bar/cobar/adjunction/curved/inversion claims

### 1.1 The dispatcher and the architecture

`bar_cobar_adjunction.tex` (lines 1–5) is a 5-line `\input{}` dispatcher into two
logically distinct files: `bar_cobar_adjunction_curved.tex` (the adjunction
side) and `bar_cobar_adjunction_inversion.tex` (the inversion side). This is
clean. The chapter label `chap:bar-cobar-adjunction` lives in
`bar_cobar_adjunction_curved.tex` line 2.

### 1.2 The five primary theorems on this surface

| Label | Defined at | Status tag | Surface |
|---|---|---|---|
| `thm:bar-nilpotency-complete` | `bar_construction.tex` L872 | ProvedHere | `d^2_0 = 0` on genus-0 bar via Arnold |
| `thm:bar-cobar-adjunction` | `cobar_construction.tex` L1927 (= `thm:geom-unit`) | ProvedHere | Theorem A: geometric unit |
| `thm:bar-cobar-isomorphism-main` | `chiral_koszul_pairs.tex` L4194 | ProvedHere | Geometric bar–cobar duality (Verdier intertwining) |
| `thm:bar-cobar-inversion-qi` | `bar_cobar_adjunction_inversion.tex` L1613 | ProvedHere{} (placed at L1708) | Theorem B: 4-clause inversion theorem |
| `thm:off-koszul-ran-inversion` | `coderived_models.tex` L915 | ProvedHere | Coderived inversion off the Koszul locus |

Plus three structural propositions: `prop:curved-bar-acyclicity` (curved L368),
`prop:filtered-to-curved-fc` (`filtered_curved.tex` L16), and the
co-contra correspondence `thm:fact-co-contra-general` (`coderived_models.tex` L821).

### 1.3 First-order findings (one-line each, expanded in §2)

- **F1.** `thm:bar-cobar-adjunction` is labeled `[Geometric unit of adjunction]`,
  not `[Bar-cobar adjunction (Theorem A)]`. The dispatcher chapter and the
  intro of the curved file *call* this label "Theorem A" (cf. `curved` L9, L42),
  but the proved object is the *unit*, not the adjunction proper. **The
  adjunction itself is never proved as a theorem in these files.** It is
  asserted around the unit and counit constructions.
- **F2.** Three bar variants (B^FG, B^Sigma, B^ord) are *named* at
  `algebraic_foundations.tex` L2423–2469. But the chapters then use only
  `barB` (= B^Sigma) for theorems while `B^ord` accumulates 92 grep hits across
  theory chapters. **B^FG appears 5 times total**; **B^Sigma appears 4 times
  total** (after the dictionary remark). The "discipline" is named once and
  forgotten.
- **F3.** "Bar-cobar inversion" is stated in two utterly different surfaces:
  strict QI on the Koszul locus (clause 1) and coderived equivalence everywhere
  (clause 2). They are bound into a single theorem `thm:bar-cobar-inversion-qi`
  with one ProvedHere tag. Clause 4 is a conditional ("if collapse input
  holds"); shipping the whole package as one ProvedHere is, by AP4, a category
  error: clauses 1 and 2 are theorems, clause 4 is a *conjectural promotion
  rule* with explicit hypothesis.
- **F4.** The Bar-cobar Quillen equivalence (`curved` L6301) is labeled but its
  hypotheses (model structure on chiral CDG-coalgebras, properness, cofibrant
  generation) are not constructed in these files. The "Quillen equivalence"
  language is rhetoric over a Verdier-quotient/coderived statement that is
  *not* a Quillen equivalence in any standard sense.
- **F5.** `coderived_models.tex` ships *two* coderived categories:
  `D^co_prov(X)` (provisional, L243) and `D^co(C-CoFact)` (full, L631), with a
  fully faithful embedding `prop:provisional-embedding` (L745). The full one
  carries `thm:fact-co-contra-general` (L821) and `thm:off-koszul-ran-inversion`
  (L915). All this is a Stratum-I/Stratum-II distinction (cf. L194) marked
  ProvedHere. The "remaining gap" of L996–1019 is described as closed; it
  isn't — see §2.5.
- **F6.** The curvature relation `mu_1^2 = [mu_0,-]_{mu_2}` is stated correctly
  at `curved` L62, L226, L268. In the *very next sentence* (L270, also L105 in
  `filtered_curved.tex`) the manuscript writes "for chiral algebras (which are
  graded-commutative), this commutator vanishes". This is **not true for
  generic chiral algebras**. The chiral product `mu` on a non-commutative
  chiral algebra (any KM at non-zero level, any non-abelian Yangian, any
  E_1-chiral) is *not* graded-commutative on the augmentation ideal. The
  passage conflates BD-commutative chiral algebras (the strict subclass with
  no OPE poles, AP-V2-AP5/V2-AP11) with the general E_1-chiral case.
- **F7.** The "categorical logarithm/exponential" rhetoric at `cobar` L1961
  (Definition L1961–2003) and `bar_construction` L437–493 includes a claim of
  *additivity*: `barB(A ⊗ A') ≃ barB(A) ⊕ barB(A')`. This is **wrong as
  stated.** Bar is multiplicative on tensor products, not additive: for cofree
  cocommutative coalgebras, `barB(A ⊗ A') ≃ barB(A) ⊗ barB(A')`. The "log
  property" is not "log of a product is sum"; it is "log of an algebra is the
  primitive part of its bar". The slogan as written is a categorical-log
  caricature.
- **F8.** Theorem `thm:bar-cobar-inversion-qi` clause 1 says: if A is Koszul,
  the genus-0 counit is a QI; if in addition A is on the higher-genus Koszul
  locus then each `psi_g` and the completed `psi = sum_g hbar^{2g-2} psi_g`
  are QIs. In the proof of `thm:genus-graded-convergence` (L2470) the manuscript
  **simultaneously** says (a) "the formal genus series has zero radius of
  analytic convergence, consistent with non-Borel-summability" and (b) "the
  completed series psi is a quasi-isomorphism." A divergent formal series
  cannot be a QI in any chain complex over `C[hbar]`; it is a QI only after
  passing to `hbar`-adic completion (L2474–2478). The theorem statement omits
  this completion.
- **F9.** The strict-Koszul-lane proof in `inversion` L1715–1727 cites a
  cluster of theorems (`thm:bar-nilpotency-complete`, `thm:chiral-koszul-duality`,
  `thm:fundamental-twisting-morphisms`, `thm:higher-genus-inversion`). Five of
  the six citations chain through `thm:higher-genus-inversion`, which itself
  depends on `axiom MK:modular` (PBW concentration at genus g). The induction
  is on genus, but the base case (g=0) is BD §3.7.11 (`inversion` L2403). This
  base case **is** for BD-commutative chiral algebras; lifting to the full
  E_1-chiral case is exactly what the manuscript claims to do but does not
  prove uniformly. The dependency chain is conditional (V2-AP4: ordered-to-
  unordered descent is R-twisted), which is acknowledged at
  `bar_construction` L391–404 but elided in the theorem block.
- **F10.** `thm:off-koszul-ran-inversion` (`coderived_models` L915) is the
  strongest claim in the chapter: "for arbitrary complete augmented A with
  finite-dimensional graded bar pieces, the bar-cobar counit becomes an
  isomorphism in `D^co(barB-CoFact)`, without Koszulness." The proof is the
  three-step assembly Stratum-by-stratum + factorization compatibility +
  conservativity. This is genuinely strong, and it is the right statement, but
  the proof's Step 2 ("factorization compatibility of the bar-cobar counit",
  L972–983) asserts that `epsilon_{U_1 ⊔ U_2}` factors as
  `epsilon_{U_1} ⊗ epsilon_{U_2}` "since the cobar functor uses the
  factorization coproduct on C, and the bar functor uses the chiral product on
  A". This is true for the *factorization* bar `barB^fact`; it is **false** for
  the ordered bar `B^ord` (V2-AP4: descent is R-twisted), and the theorem does
  not specify which bar.

The remainder of the report unpacks these and cuts to the strongest defensible
upgrade.

---

## Section 2 — Per-claim attack/defense/repair

### 2.1 Theorem A as stated (`thm:geom-unit` = `thm:bar-cobar-adjunction`,
`cobar_construction.tex` L1926–1959)

**Statement (paraphrased).** The unit
`eta : A → Omega^ch(barB^ch(A))` is geometrically realized by the configuration-space
integral formula in L1931, and is a quasi-isomorphism, "with sum convergence by
nilpotency/completeness."

**Attack.**

(i) The double-labeling `thm:geom-unit = thm:bar-cobar-adjunction` (L1926–1927)
hides a substitution: a *unit being a QI* is **not** the same as the
*adjunction existing*. The adjunction `Omega^ch ⊣ barB^ch` requires (a) a
right adjoint that exists (factorization coalgebra construction via NAP duality),
(b) a left adjoint (free chiral algebra construction `thm:cobar-free` L1905), and
(c) a natural bijection on Hom-sets. The bijection is not proved; only the
unit map is exhibited.

(ii) The "sum convergence by nilpotency/completeness" clause (L1937) collapses
two distinct hypotheses (conilpotence of `barB`, completeness of `A`) into a
parenthetical. These are not interchangeable: conilpotent ⇒ no completion
needed (`thm:conilpotency-convergence`); merely complete ⇒ inverse-limit
formulation (`Step 4` of the same proof).

(iii) The geometric proof (L1941–1959) cites
`thm:completion-necessity` (L1952) for "completeness of the filtration", but
`thm:completion-necessity` is `ProvedElsewhere` (Positselski/GLZ). The proof
of Theorem A then turns on a Positselski input that is *not reproven* here.
This is acceptable as `ProvedElsewhere` for the input, but the conclusion
(`eta` is a QI) is asserted at the level of the spectral sequence collapse
(L1952) without a separate verification of the strict E_1-acyclicity in the
non-Koszul case.

**Defense.** On the Koszul locus and at genus 0 the unit-as-QI statement is
classical (LV12 Theorem 2.3.1 for operadic bar-cobar; chiral version is
Beilinson–Drinfeld §3.7). The proof's Step ("E_1-acyclic by Koszul") is
correct *for Koszul A*. The convergence is supplied by `thm:bar-NAP-homology`
(L328) plus the FM-compactification structure.

**Repair.** Split the theorem into:

- **Theorem A.1 (Adjunction).** `Omega^ch ⊣ barB^ch` between augmented chiral
  algebras and conilpotent factorization coalgebras on Ran(X). Proof: free /
  cofree adjoints + Hom bijection via universal property of T^c. ProvedHere.
- **Theorem A.2 (Unit is QI on Koszul locus).** Under
  `A ∈ Kosz(X)`, the unit is a QI; the proof is the spectral sequence at
  L1952. ProvedHere with explicit Koszul hypothesis.
- **Theorem A.3 (Unit is coderived equivalence universally).** For complete
  augmented A with finite-dim graded bar pieces, the unit becomes an
  isomorphism in `D^co(barB-CoFact)`. ProvedHere by Verdier-dualizing
  `thm:off-koszul-ran-inversion` (which is currently the counit version).

Currently A.1 is *implicit*; A.2 is conflated with A.1; A.3 has no Verdier-dual
counterpart on the unit side. The split makes the dependency tree honest.

### 2.2 Three-bar conflation in the inversion theorem
(`thm:bar-cobar-inversion-qi`, `inversion` L1613–1709)

**Statement (paraphrased).** Under conilpotence/completeness with finite-dim
graded bar pieces, the counit `psi : Omega(barB(A)) → A` is (1) a QI on the
strict Koszul lane at all genera, (2) a coderived isomorphism off the Koszul
lane, (3) computable via the coderived bar-degree spectral sequence, (4)
promotable back to QI under the collapse hypothesis.

**Attack.**

(i) The theorem **never specifies which `barB`**. The proof body uses
`barB_X(A)` (= B^Sigma, factorization, symmetric); the chapter intro at
`curved` L99–169 explicitly distinguishes B^ord vs barB and states that the
five main theorems are invariants of the *symmetric* bar. By V2-AP3 / V2-AP4,
this means the theorem is *only* about B^Sigma; the corresponding statement on
B^ord requires R-matrix twisted descent, which is acknowledged at L131–145 of
the curved file but never assembled into a theorem in this chapter.

(ii) Clause 1 ("strict Koszul lane") and clause 2 ("coderived off-Koszul")
*share* a hypothesis "complete augmented A with finite-dim graded bar pieces".
But clause 1 also requires Koszulness (L1634), while clause 2 explicitly drops
it (L1668). So the theorem statement carries **two distinct hypothesis sets**
under one ProvedHere tag.

(iii) Clause 4 (`promotion back to QI`) is *conditional*: "if kappa(A)=0, or
more generally if the coderived bar-degree spectral sequence degenerates to
ordinary cohomology on the relevant off-Koszul locus (the class G/L collapse
input), then the coderived equivalence upgrades to a chain-level QI." This is
**a conjecture stated as part of a theorem** (AP-V2-AP31). The "extra
collapse hypothesis" is not constructively verified for any non-Koszul family
(the manuscript itself states at L1996–1998: "No specific non-Koszul family is
presently proved by a separate family-level argument to satisfy that promotion
hypothesis").

(iv) Clause 1's higher-genus QI assertion `psi = sum_g hbar^{2g-2} psi_g`
(L1652) is asserted as a QI without specifying that QIs only make sense after
hbar-adic completion (L2474). The body of `thm:genus-graded-convergence`
(L2470) **explicitly notes** the formal series has zero analytic radius of
convergence; the theorem statement does not.

**Defense.** Each *clause individually* is proved (modulo hypotheses):

- (1) is the BD genus-0 + induction on genus (`thm:higher-genus-inversion`).
- (2) is `thm:off-koszul-ran-inversion` (proved cleanly via stratum
  Positselski, factorization compatibility, conservativity).
- (3) is `prop:coderived-bar-degree-spectral-sequence` (proved via Positselski
  Prop. 3.5).
- (4) is *honest as a conditional promotion rule* if read carefully (L1689–
  1690: "outside those collapse loci this theorem does not assert an ordinary
  QI").

**Repair.** Decompose:

- **Theorem B.1 (Strict Koszul-lane QI, all genera, completed series).** As
  current clause 1, with explicit hbar-adic completion in the conclusion and
  "Koszul + higher-genus Koszul locus" in the hypothesis. ProvedHere.
- **Theorem B.2 (Coderived inversion universal).** As current clause 2, no
  Koszul hypothesis. ProvedHere via `thm:off-koszul-ran-inversion`. State
  explicitly that this is for B^Sigma (factorization bar), with the
  R-twisted ordered analogue stated as
  Conjecture B.2′.
- **Proposition B.3 (Coderived bar-degree filtration).** As current clause 3.
  ProvedHere.
- **Conjecture B.4 (Promotion to ordinary QI).** Currently clause 4. The body
  of the manuscript already concedes that no non-Koszul family is proved to
  satisfy the collapse hypothesis. State as a conjecture, list the candidate
  classes (G, L) where collapse is *expected*, and isolate the missing input.

This is a **strict upgrade**: B.2 is the strongest claim and is honestly
proved; conditional clauses are no longer hidden inside a ProvedHere
theorem.

### 2.3 "Quillen equivalence" overclaim
(`curved` L6301 `thm:bar-cobar-quillen-equivalence`)

**Attack.** A Quillen equivalence requires two model structures and a Quillen
adjunction whose derived functors are equivalences. The chapter does not
construct a model structure on chiral CDG-coalgebras (no cofibrations,
fibrations, weak equivalences specified; no left-properness verified; no
combinatoriality). What is actually proved at `coderived_models.tex` is a
Verdier-quotient inversion in a coderived category, which is a *triangulated
equivalence*, not a Quillen equivalence.

**Defense.** "Quillen equivalence" is sometimes used loosely to mean "induces
an equivalence of homotopy categories." On that reading the statement is true
(modulo coderived ⇒ ordinary derived only on the flat lane).

**Repair.** Either:

(a) Prove Hinich / Vallette-style model structures on chiral CDG-coalgebras
    (this is a substantial undertaking, but it is the published mathematical
    framework, e.g., Positselski 2011 §8). Then the Quillen-equivalence claim
    becomes a real theorem.
(b) Downgrade language: replace "Quillen equivalence" with "triangulated
    equivalence" or "coderived equivalence."

Option (a) is the upgrade path and produces a publishable theorem of independent
interest.

### 2.4 Curvature commutator and the "graded-commutative" elision
(`curved` L270, `filtered_curved` L103–112)

**Statement.** `thm:curvature-central` (`curved` L263) gives `mu_1^2 = [mu_0,-]_{mu_2}`,
then immediately remarks "for chiral algebras (which are graded-commutative),
this commutator vanishes."

**Attack.** "Chiral algebras are graded-commutative" is **false in general**.
It is true for BD-commutative chiral algebras (= pole-free chiral algebras = the
strict subclass of E_inf-chiral on which `mu` extends across the diagonal,
`bar_construction.tex` L387–404 quoting BD §4). For E_1-chiral algebras
(Yangians, EK quantum vertex algebras, the `B^ord` lane), the chiral product
is associative but not commutative. Even for E_inf-chiral with poles
(Heisenberg, KM, Virasoro), the chiral *product* has poles and is not
graded-commutative on the diagonal until residues are extracted.

The elision is doubly bad because the very thing the chapter is *trying* to
introduce (curved structure for non-quadratic algebras like Virasoro, W_3) is
exactly the regime where `mu_2` does **not** trivialize the bracket: the
Virasoro `T(z)T(w)` OPE has a fourth-order pole that contributes to
`[mu_0, T]_{mu_2}`. Saying "this commutator vanishes" makes the curvature
correction structurally invisible.

**Defense.** In the *associated graded* with respect to the conformal-weight
filtration, leading-order chiral products are graded-commutative. On BD-
commutative algebras the statement is vacuously correct. So the elision is
true on the strict subclass that the example examines.

**Repair.** Split into three regimes:

- **BD-commutative subclass.** `[mu_0, -]_{mu_2} = 0` automatically; `mu_1^2 = 0`.
- **E_inf-chiral with poles (Heisenberg, KM, Vir, W).** `[mu_0, -]_{mu_2}` lives
  on the diagonal contraction; centrality of `mu_0` (when `mu_0 = kappa·1` is
  scalar) makes the commutator vanish *as a class* but not chain-level.
- **E_1-chiral (Yangian, etc.).** `mu_2` is genuinely non-commutative; the
  curvature commutator is the obstruction to `mu_1^2 = 0` and is not
  automatically vanishing. The framework here is the strict CDG-coalgebra
  with `d^2 = h*(-)`.

The current text uses Regime 1's calculation in the body of a theorem that is
nominally about Regime 2/3.

### 2.5 The "structural gap H1 closed" claim
(`coderived_models.tex` L996–1019, `rem:H1-closure`)

**Statement.** "Theorem `thm:off-koszul-ran-inversion` resolves structural gap
H1: the coderived Ran-space formalism is now established. Combined with the
strict Koszul-locus inversion, this gives the strongest proved package on the
present surface."

**Attack.**

(i) The proof of `thm:off-koszul-ran-inversion` (Step 1) requires
"finite-dimensional graded pieces on each stratum"; finite-dimensionality
"propagates from the 1-point stratum via the factorization tensor product:
near the generic point of Ran_n, C_n ≃ C_1^{⊗n}". This is correct *near the
generic point*. **Globally on Ran_n, the factorization isomorphism is not
trivial**: the chiral algebra extends across diagonals via NAP, and the
extension can introduce dimension jumps at the boundary strata. The proof
glosses over the global non-flatness.

(ii) Step 2 ("factorization compatibility of the bar-cobar counit", L972–983)
is asserted in one paragraph: "Both Omega_X and barB_X are defined via
factorization-compatible constructions ... so epsilon is a morphism in the
factorization CDG-comodule category." This is true but the chain-level
verification (that the unit/counit *commute* with the factorization
isomorphisms on disjoint opens) is a substantive computation deferred. The
counit at level n involves `n!` permutation orbits in B^Sigma; on B^ord it
involves the R-matrix; the counit's compatibility with factorization on
disjoint opens depends on which.

(iii) The "structural gap H1" is described as closed at L996; the very next
paragraph (L1008) admits "the remaining issue is exactly the flat-side
collapse input needed for that promotion." That is **not** closed; it is
restated as the residual obstruction.

**Defense.** The coderived statement *itself* is a real theorem: the cone is
coacyclic. This is genuinely strong and bypasses the collapse-input issue at
the level of the coderived category. The "gap closure" rhetoric is just
sloppy: H1 ≠ flat-side collapse.

**Repair.** Reword `rem:H1-closure` to:

"`thm:off-koszul-ran-inversion` closes the *coderived half* of structural gap
H1 (the existence of a Verdier-quotient inversion). The promotion half
(coderived equivalence ⇒ ordinary chain-level QI) remains open and is
isolated as the flat-side collapse input."

This is the minimal honest reading; nothing about the proof needs revisiting.

### 2.6 The "categorical logarithm: additivity" overclaim
(`cobar_construction.tex` L1969–1980, `def:categorical-logarithm`)

**Statement.** "Additivity (log sends products to sums):
`barB^ch(A ⊗ A') ≃ barB^ch(A) ⊕ barB^ch(A')`."

**Attack.** **This is wrong.** For cofree cocommutative coalgebras
(`barB^ch` = `Sym^c(s^{-1} bar A)`), the natural identity is
`barB(A ⊗ A') ≃ barB(A) ⊗ barB(A')` (multiplicative), not additive. The
"primitive part" of `barB(A ⊗ A')` is `s^{-1}(bar A ⊕ bar A')`, which is
additive — but the bar coalgebra itself, including all bar-degree-≥2 pieces,
is multiplicative. Confusing the primitive part with the whole bar gives a
formula that fails already at bar degree 2: `barB^2(A ⊗ A')` contains cross
terms `s^{-1} a ⊗ s^{-1} a'` that are absent from `barB^2(A) ⊕ barB^2(A')`.

The proof cited at L1976 ("logarithmic forms are additive under the product of
chiral brackets") is a separate (true) statement about *kernels*; it does not
imply additivity of the *coalgebra*.

**Defense.** None: the statement is straightforwardly wrong. "Categorical
logarithm" is a defensible heuristic but the property listed under "additivity"
is the wrong one.

**Repair.** Replace property (i) with:

"**Multiplicativity** (log of a tensor product = tensor product of logs):
`barB^ch(A ⊗ A') ≃ barB^ch(A) ⊗_{ext} barB^ch(A')` as factorization coalgebras."

The "log → +" intuition lives at the level of *primitives*: `Prim(barB(A)) =
s^{-1} bar A`; the primitives are additive. Phrase it that way.

### 2.7 Coderived spectral sequence dual identification
(`coderived_models` L314–363, `prop:coderived-bar-degree-spectral-sequence`)

**Attack.** The proposition claims that under bounded-below filtration with
strict associated graded, vanishing of `E_1` implies coacyclicity. The proof
cites Positselski Prop 3.5. That is correct *for the abstract Positselski
machine*. The proposition's hypothesis "the curvature term lies in F^1, so
`(gr^0 d_K)^2 = 0`" requires the curvature to be of strictly positive
filtration degree. For Heisenberg/KM with `mu_0 = kappa·1`, the curvature is
a *constant* (filtration degree 0 if the filtration starts at 0). The
filtration must therefore be the *augmentation-ideal* filtration, where
`mu_0 ∈ I^1` because `1 ∈ I^0`. This is implicit but not stated.

**Defense.** The proof is correct for the augmentation-ideal filtration; the
implicit choice can be read off the "PBW filtration" reference at L786.

**Repair.** Add explicit hypothesis: "with respect to the augmentation-ideal /
PBW filtration on the bar coalgebra, the curvature element `mu_0` lies in F^1
(positive filtration)." This is a one-line addition; without it the
proposition fails for the level-0 algebras.

### 2.8 "thm:bar-cobar-inversion-qi" missing Koszul hypothesis on higher-genus
clause

**Attack.** Clause 1 second half (L1642–1654) requires "A on the higher-genus
Koszul locus of `thm:higher-genus-inversion`, e.g., for the standard landscape
by `thm:pbw-allgenera-km` and `thm:pbw-allgenera-principal-w`." This is
Koszulness *plus* PBW-allgenera concentration. The current statement folds
both into "if A is Koszul + on the higher-genus locus" without flagging that
PBW-allgenera concentration is an *independent* hypothesis from genus-0
Koszulness.

**Defense.** The dependent theorems `thm:pbw-allgenera-km`,
`thm:pbw-allgenera-principal-w` exist and are ProvedHere for KM and principal
W. So the standard landscape is covered. The theorem just hides the
multi-hypothesis structure.

**Repair.** Hypothesis pull-out: list each input (Koszul, PBW, conilpotent or
complete, finite-dim graded bar pieces) as a separate bullet. Then list the
families satisfying each. This is hygiene.

### 2.9 Hierarchy V2-AP22 is invoked but never proved
(`algebraic_foundations` L2273–2275)

**Statement.** "The hierarchy `E_inf-chiral ⊂ P_inf-chiral ⊂ E_1-chiral`."

**Attack.** This is stated as a single line at L2273, with no proof, no theorem
label, no `\ClaimStatus` tag. The Vol II CLAUDE.md (V2-AP22) gives the full
hierarchy as `Comm assoc ⊂ PVA ⊂ E_inf-chiral ⊂ P_inf-chiral ⊂ E_1-chiral`,
each strict (V2-AP21). The Vol I version drops the first two levels (Comm and
PVA) and asserts the rest as a containment. **Neither containment nor
strictness is proved.**

The strict containment matters: `P_inf ⊊ E_1` is the entire reason E_1-chiral
algebras aren't degenerations of E_inf with extra brackets; it is what allows
Yangians to live outside E_inf.

**Defense.** As a *forward reference* to the dictionary section, listing the
hierarchy without proof is acceptable in a survey. The strictness is
addressed in `e1_modular_koszul.tex` and `ordered_associative_chiral_kd.tex`.

**Repair.** Add a one-paragraph remark giving (a) the inclusion morphisms
explicitly, (b) the witnesses to strict containment (e.g., "Heisenberg ∈
E_inf \ P_inf-shifted? No, Heisenberg is E_inf"; better: "the elliptic
Yangian witnesses E_1 \ E_inf"), (c) a forward reference to where strictness
is constructively shown.

### 2.10 The "ordered → symmetric averaging" is described, never theorematized
(`curved` L99–169, `rem:bar-ordered-primacy`)

**Attack.** The remark describes a surjective averaging map
`av : barB^ord(A) → barB(A)` (L113–122) and asserts it is "a quasi-isomorphism
of chain complexes in characteristic 0, but not an isomorphism of coalgebras."
This is a substantive mathematical claim and **it is given as a remark, not a
theorem.** No proof, no `ClaimStatus` tag.

The claim is true (averaging by `1/n!` is a section of the inclusion of
coinvariants in invariants in characteristic 0) but should be a Lemma with a
two-line proof.

**Defense.** It is genuinely standard. The remark gives the right answer.

**Repair.** Promote to `\begin{lemma}[Averaging map; \ClaimStatusProvedHere]
\label{lem:bar-ord-to-sym-av}` with a two-line proof: in characteristic 0,
the averaging idempotent `(1/n!) sum_sigma sigma` projects onto Sigma_n-
invariants; the QI follows from the flat resolution of the trivial
Sigma_n-module. Then every theorem that uses "barB" can cite this lemma to
specify which bar.

---

## Section 3 — Three-bar discipline audit

### 3.1 Census

| Symbol | Total grep hits across `chapters/theory/` |
|---|---:|
| `B^ord` (any rendering) | 92 |
| `B^FG` | 5 |
| `B^Sigma` | 4 |
| `barB` (= B^Sigma in current convention) | several hundred |

The convention `barB = B^Sigma` is set at `bar_construction.tex` L86
(`conv:bar-coalgebra-identity`) and reaffirmed at `cobar_construction.tex`
L102–132 (`rem:cobar-which-bar`). So the symbol `barB` is **always** B^Sigma.
B^ord is named throughout but never used inside a theorem of these chapters
(it lives in `ordered_associative_chiral_kd.tex` where it is the primary
object).

**Verdict.** The discipline is **superficially observed**: every chapter has a
remark naming all three. But the load-bearing theorems (`thm:bar-cobar-
adjunction`, `thm:bar-cobar-inversion-qi`, `thm:off-koszul-ran-inversion`,
`thm:fact-co-contra-general`) all use `barB` = B^Sigma without explicit tag.
This is operationally OK because the convention pins it down, but it makes the
chapter *blind to B^ord* — and the strongest claims (E_1-chiral inversion,
Yangian Koszul duality) live on B^ord.

### 3.2 Specific failures

- **F-Bar.1.** `thm:off-koszul-ran-inversion` says "A complete augmented chiral
  algebra ... barB_X^fact(A) ..." (L920–922). The hypothesis "complete
  augmented" allows E_1-chiral A; the conclusion is for the *symmetric*
  factorization bar. If A is E_1-chiral (Yangian), the symmetric bar
  *exists* (just take coinvariants) but loses the R-matrix — it is then a
  symmetric coalgebra to which the theorem applies, but the result is only
  about the symmetric quotient, not about A itself.
- **F-Bar.2.** The map `av : B^ord → B^Sigma` is NOT R-twisted in
  characteristic 0 (the naive averaging is a QI), but at the level of
  *coalgebra structure* the inverse map `B^Sigma → B^ord` (a section) **is**
  R-twisted (V2-AP4). The chapter says (`curved` L122) "this map is a QI of
  chain complexes ... but not an isomorphism of coalgebras"; it does not
  state that the section is R-twisted.
- **F-Bar.3.** `thm:bar-NAP-homology` (`bar_construction` L328) claims bar =
  factorization homology. This is for the symmetric bar (factorization is
  by definition symmetric). The "BD comparison" remark at L364–404 explicitly
  flags that the ordered bar is *not* the BD object. Correct, but then
  every downstream invocation of "bar = factorization homology" must mean
  B^Sigma, and the manuscript is consistent on this (modulo F-Bar.1).
- **F-Bar.4.** `B^FG` (Francis–Gaitsgory) appears in the dictionary
  (`algebraic_foundations` L2429) and twice elsewhere (L2462, L2462). The
  filtration `gr(B^Sigma) → B^FG` (retain only zeroth poles) is asserted
  at L2462. **No proof, no theorem label.** This is the standard FG
  comparison and it is correct; it should be `\begin{theorem}[FG comparison;
  \ClaimStatusProvedElsewhere{} \cite{FG12}]`.

**Verdict.** The discipline exists in name; in practice the chapter develops
B^Sigma exclusively. The other two bars are referenced for completeness but
their comparisons are *announced not proved*.

---

## Section 4 — Hierarchy (V2-AP22) audit

V2-AP22: `Comm assoc ⊊ PVA ⊊ E_inf-chiral ⊊ P_inf-chiral ⊊ E_1-chiral`. Each
inclusion strict.

### 4.1 Where the hierarchy is invoked

- `algebraic_foundations.tex` L2273–2275: 1-line statement of three-level
  hierarchy (Vol I version drops Comm and PVA).
- `algebraic_foundations.tex` L2425 (`def:einf-chiral`), L2213 (`def:e1-chiral`),
  L2256 (`def:pinf-chiral`): definitions of all three levels.
- `bar_construction.tex` L389–404: BD-commutative ⊂ E_inf-chiral, BD's
  Chapter 4 covers the strict pole-free subclass.
- `inversion.tex` L75–77: "The passage from quadratic to general is also the
  passage from E_inf to E_1: the Yangian Y(g), which is E_1-chiral but not
  E_inf, falls in the filtered class."

### 4.2 Strict containment witnesses

- `Comm assoc → PVA`: not addressed in Vol I.
- `PVA → E_inf-chiral`: V2-AP21 says PVA ≠ P_inf-chiral, which is a different
  containment. The Vol I dictionary remark `def:pinf-chiral` (L2256) defines
  P_inf-chiral as "an E_inf-chiral algebra with a compatible L_inf structure
  via Leibniz". This makes P_inf an *enrichment* of E_inf. The containment
  direction in Vol I is `E_inf-chiral ⊊ P_inf-chiral` (P_inf adds bracket
  data). **This contradicts V2-AP22**, which orders `E_inf-chiral ⊊ P_inf-chiral
  ⊊ E_1-chiral`.

  Reading V2-AP22 carefully: PVA = Poisson Vertex Algebra (classical shadow,
  cohomology level); P_inf = homotopy intermediate. So PVA ⊋ E_inf-chiral?
  No: PVA is a *Poisson* enhancement, and the V2-AP22 ordering makes
  Comm < PVA < E_inf < P_inf < E_1, which means PVA is *between Comm and
  E_inf*. Vol I's `def:pinf-chiral` puts P_inf above E_inf, in agreement
  with V2-AP22. Vol I is silent on PVA's place.

  **Verdict.** Vol I and Vol II are consistent on the containment *direction*
  (P_inf > E_inf), but Vol I never names PVA as a separate level. This is
  a missing rung, not a contradiction.

- `E_inf-chiral → P_inf-chiral`: the inclusion is explicit in
  `def:pinf-chiral` (P_inf is E_inf + L_inf).
- `P_inf-chiral → E_1-chiral`: this is the deep inclusion. Vol I asserts it
  in `algebraic_foundations` L2273 with no proof. The witness is "Yangian
  is E_1 but not E_inf" (`inversion` L76), which establishes
  `E_inf ⊊ E_1` but does not establish `P_inf ⊊ E_1`. The latter requires a
  P_inf algebra that is not E_1 — but every P_inf algebra has an E_inf
  product, hence is E_inf-chiral, hence is E_1-chiral. So `P_inf ⊆ E_1` is
  trivial; strict containment requires an E_1-chiral algebra without compatible
  L_inf. The Yangian is such a witness only if its `mu_2` does not lift to a
  shifted Lie bracket — which is exactly the chain-level Incompatibility
  Theorem in Vol III. So the witness lives outside Vol I.

### 4.3 Verdict on hierarchy discipline in Vol I

The hierarchy is *named correctly* but *never proved strict within Vol I*. The
strictness witnesses live in Vol III (Incompatibility Theorem). For Vol I to
be self-contained, either:

(a) Add a `\begin{remark}[Hierarchy strictness]` listing (i) E_inf-chiral
    witness without P_inf structure (probably none exist in Vol I; chiral
    PVAs are hard to realize), (ii) P_inf-chiral witness without E_1-chiral
    structure (vacuous since P_inf ⊆ E_1).
(b) Cite Vol III for the strictness witnesses and mark it as a
    cross-volume dependency.

Either is acceptable; (b) is the smaller intervention.

---

## Section 5 — First-principles analyses

### 5.1 Wrong claim: "barB is additive on tensor products" (cobar L1973)

- **Ghost theorem.** The *primitive part* of `barB(A ⊗ A')` is the desuspended
  augmentation ideal `s^{-1}(bar A ⊕ bar A') = s^{-1} bar A ⊕ s^{-1} bar A'`,
  which **is** additive.
- **Precise error.** Confusing `Prim(barB)` with `barB`. The full bar
  coalgebra is `T^c(s^{-1} bar A)`; for `A ⊗ A'`, this is `T^c(s^{-1} bar A
  ⊕ s^{-1} bar A')`, which is *multiplicative* on the cofree level: `T^c(V
  ⊕ W) = T^c(V) ⊗_{shuffle} T^c(W)`. So `barB(A ⊗ A') = barB(A) ⊗_{shuffle}
  barB(A')`, not `barB(A) ⊕ barB(A')`.
- **Correct relationship.** `Prim(barB)` is additive; `barB` is multiplicative
  with shuffle structure. The "log → +" slogan refers to primitives.

### 5.2 Wrong claim: "chiral algebras are graded-commutative, so [mu_0,-]_{mu_2}
vanishes" (curved L270, filtered_curved L103)

- **Ghost theorem.** *BD-commutative* chiral algebras (pole-free) are
  graded-commutative; on those, `[mu_0, -]_{mu_2} = 0`.
- **Precise error.** Generalizing "BD-commutative ⇒ graded-commutative" to
  "chiral ⇒ graded-commutative." The generalization is false: E_inf-chiral
  with poles (Heisenberg, KM, Vir, W) are not graded-commutative on the
  diagonal contraction; E_1-chiral (Yangian) is not graded-commutative
  anywhere.
- **Correct relationship.** On the *associated graded* with respect to the
  conformal-weight or augmentation-ideal filtration, leading-order chiral
  products are graded-commutative for E_inf-chiral. This is the precise
  statement that supports the elision; it is not "chiral ⇒ commutative."

### 5.3 Wrong claim (latent): "factorization compatibility makes the bar-cobar
counit factor as `eps_U1 ⊗ eps_U2`" (coderived_models L972–983, off-Koszul
inversion proof)

- **Ghost theorem.** True for the *symmetric* factorization bar: by
  factorization of the chiral algebra `A(U_1 ⊔ U_2) ≃ A(U_1) ⊗ A(U_2)` and
  the cofree property of the symmetric bar.
- **Precise error.** Stated without specifying the bar. For B^ord, the
  factorization isomorphism on disjoint opens carries an R-matrix twist;
  the counit does not factor cleanly without taking the R into account.
- **Correct relationship.** For B^Sigma: counit factors. For B^ord: counit
  factors *up to R-matrix conjugation*; the factorization is "twisted
  factorization" in the sense of V2-AP4.

### 5.4 Latent ghost theorem: "Promotion is automatic on G/L"
(`thm:bar-cobar-inversion-qi` clause 4)

- **Ghost theorem.** For class-G chiral algebras (semiclassical, polynomial
  shadow), the coderived bar-degree spectral sequence collapses, hence
  coderived equivalence promotes to ordinary QI.
- **Precise error.** Stated as conditional within a `ProvedHere` theorem.
  No specific G or L family is constructively verified to satisfy the
  collapse hypothesis. The body of the manuscript admits this at L1996.
- **Correct relationship.** Collapse on G/L is a *separately checkable*
  conjecture; the promotion rule is then a consequence.

---

## Section 6 — Three upgrade paths (strongest claims)

### 6.1 Upgrade Path A: Bar-cobar Quillen equivalence at all three bar levels

**Goal.** Establish a genuine Quillen equivalence
`(Omega^ch, barB^ch_*) : DGAlg^aug ⇄ DGCoalg^conil` for each of B^FG, B^Sigma,
B^ord, with explicit hypotheses.

**Why upgradeable.** The current "Quillen equivalence" claim (`curved` L6301)
is not backed by a model structure construction, but Hinich's model structure
on conilpotent dg-coalgebras is published (1997, with chiral lift in
Francis–Gaitsgory 2012) and the chiral lift is sketched in `coderived_models.tex`.

**Steps.**

1. Construct cofibration / fibration / weak equivalence triple on chiral
   CDG-coalgebras with conilpotent / complete inputs.
2. Verify proper / cofibrantly generated.
3. Show `Omega^ch` preserves cofibrations and acyclic cofibrations; `barB^ch`
   preserves fibrations and acyclic fibrations.
4. Quillen equivalence: derived functors are inverse on Ho.

For each bar variant:

- B^FG (Francis–Gaitsgory bar): already proved by FG12; cite.
- B^Sigma (symmetric factorization bar): the current chapter's surface;
  upgrade `thm:bar-cobar-quillen-equivalence` from rhetoric to theorem.
- B^ord (ordered bar): requires R-matrix twisted descent; this is where the
  upgrade is genuinely new.

**Output.** Three Quillen equivalences, parametrized by R-matrix data on the
ordered side.

### 6.2 Upgrade Path B: Curved bar-cobar without conilpotence (Positselski-style)

**Goal.** Drop conilpotence everywhere; replace by complete + finite-type
graded pieces. Establish a curved bar-cobar Quillen-style equivalence between
**curved** chiral A_inf algebras and **curved** chiral A_inf coalgebras, with
the equivalence implemented by the bar/cobar functors.

**Why upgradeable.** The current `thm:off-koszul-ran-inversion` is the
strongest proved statement. It uses Positselski's Theorem 7.2 stratum-by-
stratum and assembles via factorization. Promoting to a *curved bar-cobar
adjunction* (not just inversion of the counit) requires (a) defining curved
bar / curved cobar without conilpotence, (b) proving they are adjoint, (c)
showing the unit and counit are coderived equivalences.

**Steps.**

1. Define curved cobar `Omega^curved` of a curved CDG-coalgebra: the standard
   cobar with the curvature term added to the differential.
2. Define curved bar of a curved A_inf algebra: the standard bar with the
   curvature element added to the bar differential.
3. Hinich-Positselski adjoint pair: verify free / cofree + Hom bijection.
4. Use `thm:fact-co-contra-general` (`coderived_models` L821) for the unit
   side and `thm:off-koszul-ran-inversion` for the counit side.

**Output.** Bar-cobar adjunction in the curved/conilpotence-free regime,
covering Yangian, Virasoro, W, RTT.

### 6.3 Upgrade Path C: Universal coderived model

**Goal.** Replace the *provisional* coderived category
`D^co_prov(X)` with a universal one independent of the choice of filtration.

**Why upgradeable.** `coderived_models.tex` already proves the embedding
`D^co_prov(X) ↪ D^co(C-CoFact)` (`prop:provisional-embedding`, L745). The
provisional version is "filtered curved factorization models with bounded-below
filtration"; the full version is "factorization CDG-coalgebras" without the
filtration. The embedding is fully faithful; the gap is the *essential image*
(filtered vs all curved coalgebras).

**Steps.**

1. Show that every curved factorization CDG-coalgebra admits a *canonical*
   filtration (e.g., the bar-degree filtration on `barB^fact(A)`).
2. Conclude the embedding `D^co_prov(X) → D^co(C-CoFact)` is essentially
   surjective on the relevant subcategory.
3. Replace all theorems referring to `D^co_prov(X)` by theorems in
   `D^co(C-CoFact)`.

**Output.** A single coderived ambient, no Stratum-I/Stratum-II split. This
makes Vol I's "completed Yangian" and Vol II's "factorization coalgebra"
discussions live in the same category.

---

## Section 7 — Consolidated punch list

### 7.1 Required corrections

- **C-1.** `def:categorical-logarithm` (`cobar_construction.tex` L1969–1980),
  property (i): replace "Additivity" with "Multiplicativity"; the formula
  `barB(A ⊗ A') ≃ barB(A) ⊕ barB(A')` is wrong. Correct identity is
  `barB(A ⊗ A') ≃ barB(A) ⊗ barB(A')` with shuffle multiplication.
- **C-2.** `thm:curvature-central` (`curved` L263), surrounding text at L270
  and `filtered_curved` L103: remove the elision "for chiral algebras (which
  are graded-commutative)..." It is true only on the BD-commutative
  subclass. Replace with a three-regime split (BD-commutative;
  E_inf-chiral with central scalar `mu_0`; E_1-chiral with non-trivial
  commutator).
- **C-3.** `rem:H1-closure` (`coderived_models` L996–1019): the wording "gap
  H1 closed" is misleading; H1 has a *coderived half* (closed) and a
  *promotion half* (open). Reword to reflect this.
- **C-4.** `prop:coderived-bar-degree-spectral-sequence` (`coderived_models`
  L314): add explicit hypothesis "with respect to the augmentation-ideal /
  PBW filtration, `mu_0 ∈ F^1`."
- **C-5.** `thm:bar-cobar-adjunction` (`cobar_construction` L1926): split the
  double-label into A.1 (adjunction proper) and A.2 (unit is QI on Koszul);
  add A.3 (universal coderived equivalence on the unit side, dual to
  `thm:off-koszul-ran-inversion`).
- **C-6.** `thm:bar-cobar-inversion-qi` (`inversion` L1613): split the 4-clause
  ProvedHere into B.1, B.2, B.3 (theorems) and B.4 (conjecture). Add explicit
  `hbar`-adic completion to clause 1's higher-genus statement.

### 7.2 Required additions (one-line each)

- **A-1.** Promote `rem:bar-ordered-primacy` (`curved` L99) averaging map to
  `lem:bar-ord-to-sym-av` with two-line proof.
- **A-2.** Add `thm:fg-comparison` (`algebraic_foundations` L2462): the
  filtration `gr(B^Sigma) → B^FG`, `\ClaimStatusProvedElsewhere{} \cite{FG12}`.
- **A-3.** Add `thm:bar-cobar-quillen-properly-stated` (`curved` L6301):
  promote rhetoric to a real Quillen equivalence theorem, OR downgrade
  language to "triangulated equivalence."
- **A-4.** Add `rem:hierarchy-strictness` (`algebraic_foundations` L2275):
  list witnesses for each strict containment in V2-AP22, citing Vol III for
  P_inf ⊊ E_1.
- **A-5.** Add a hypothesis-pull-out box on `thm:bar-cobar-inversion-qi`:
  separate "Koszul," "PBW-allgenera," "complete," "finite-dim graded bar
  pieces," "conilpotent" — each with its family witnesses.

### 7.3 Watch list (correct as written, but fragile)

- **W-1.** `thm:off-koszul-ran-inversion` (`coderived_models` L915): the
  globalization Step 2 is one paragraph; consider expanding.
- **W-2.** `thm:fact-co-contra-general` (L821): Step 2 ("factorization
  compatibility of Phi and Psi") asserts an algebraic identity in one line;
  verify in detail.
- **W-3.** Three-bar census: 92 hits for B^ord, 5 for B^FG, 4 for B^Sigma in
  these chapters. The discipline is named in each chapter's intro but
  invisible in proofs. After C-5/C-6 split, every bar-using theorem should
  carry a `[bar = X]` regime tag analogous to `Convention conv:regime-tags`.

### 7.4 Cache write-back (AP-CY61 dictionary candidates)

Two patterns appeared 2+ times in this audit and should be added to
`appendices/first_principles_cache.md`:

| Wrong claim | Ghost theorem | Correct relationship | Type |
|---|---|---|---|
| "barB is additive: barB(A⊗A') ≃ barB(A) ⊕ barB(A')" | Prim(barB) is additive | Full bar is multiplicative (shuffle); only primitives add | part/whole |
| "Chiral algebras are graded-commutative, so [mu_0,-]_{mu_2}=0" | BD-commutative subclass is graded-commutative | E_inf-chiral with poles, E_1-chiral, Yangian: NOT graded-commutative | specific/general |

Both are scope-error / specific-vs-general patterns. Note: not committing
the cache update (read-only audit). Recommend adding via a separate session.

---

## Closing assessment

The bar-cobar machinery in Vol I is **structurally sound at the top level** and
**locally fragile** at the joins:

- **Sound.** `thm:off-koszul-ran-inversion`, `thm:fact-co-contra-general`,
  `prop:coderived-bar-degree-spectral-sequence` are real, well-proved
  theorems. The coderived framework is the strongest currently-published
  package in the chiral setting and gives the chapter genuine load-bearing
  content.

- **Fragile.** The 4-clause `thm:bar-cobar-inversion-qi` packs proved
  theorems, conditional theorems, and a conjecture under a single
  ProvedHere tag (AP4 / V2-AP31 violation). The "Quillen equivalence"
  rhetoric (`curved` L6301) is stronger than the proof supplies. The
  "graded-commutative ⇒ commutator vanishes" elision (`curved` L270)
  trivializes the very curvature it is meant to introduce. The three-bar
  discipline is named once and not enforced in theorem statements.

- **Genuine errors.** Two outright false statements:
  (a) "barB is additive on tensor products" (`cobar_construction` L1969).
  (b) "Chiral algebras are graded-commutative" (`curved` L270, `filtered_curved`
  L103).
  Both are local; neither propagates fatally because the manuscript uses the
  correct identities elsewhere. They should be corrected.

- **Upgrade paths.** Three: model structure for genuine Quillen equivalence
  (UP-A), conilpotence-free curved bar-cobar adjunction (UP-B), universal
  coderived model unifying provisional and full (UP-C). All three are
  publishable upgrades; UP-B is the most direct given the current state.

The chapter is at the **80% mark** of a publishable bar-cobar foundation. The
remaining 20% is concentrated in §7.1 (six required corrections, all small)
and §7.2 (five additions, mostly hygiene). The deeper upgrades in §6 are
genuine new theorems but do not block the current narrative.

---

*Wave 5 audit complete. Read-only; no manuscript edits; no cache write-back
performed. Cache candidates listed in §7.4 for separate session.*
