# First-Principles Audit of the Mathematics and Physics — Vol I

**Date:** 2026-07-10 (07:00–08:00 JST)
**State audited:** commit `e011027` ("release pdf") plus the live working
tree, which was under concurrent modification by another session during
the audit. Working-tree line numbers drift; committed-state references
are stable against `e011027` / `df6a9be`. Where a finding was re-checked
against the moving tree, the snapshot time is noted.
**Method:** five independent adversarial deep reads (Theorem A; Theorem
H; Theorems B and D; the five-archetype landscape and κ-matrix; the
physics chapters), each instructed to ignore claim-status macros,
FRONTIER.md, and concordance files and to referee the actual statements
and proof bodies against primary knowledge. Every load-bearing finding
below was then independently confirmed at the main line by direct
reading, grep, or symbolic recomputation before inscription here.
Repo validation gates (`make test`, `make integrity`, etc.) were
reserved for session-end integration.

**Post-audit state:** [Part III](#part-iii--post-repair-ledger) records
the theorem repairs, exact computations, propagation, and remaining
construction problems completed after the two referee passes below.
Its status table is the current working-tree account.

---

## 1. Executive verdict

**Overall grade: C+. The skeleton is healthy; several headline organs
are not.**

- **The standard Virasoro, modular, and intersection-theoretic constants
  listed below survive direct recomputation.** Later reconstruction found
  two separate numerical surfaces requiring correction: the mirror-quintic
  HKR vector has middle entry $204$ and total dimension $208$, and the
  symbols $S_r$ require a residue projection beyond the raw Ward
  correlator. The two weight-six formulas belong to distinct null-state
  and weighted-Riccati extractions.
- **The claim-status labelling discipline substantively holds.** Census
  across the physics chapters: ProvedHere 67, ProvedElsewhere 23,
  Conditional 144, Conjectured 58, Heuristic 17 (~72% openly deferred).
  The Master Reconstruction Theorem is an honestly Conditional assembly
  theorem with its open piece quarantined as a Conjecture.
- **But three of the five headline theorems have their novel content
  resting on definitional circularity or an unproved bridge** (A, B's
  falsity clause, D at g ≥ 2); **one verified type error** sits at the
  centre of the Verdier lane; **one phantom-citation cluster** props up
  the M-theory frame of `bv_brst.tex`; and Theorem H's healing left a
  named open hole that a concurrent rewrite was re-stamping ProvedHere
  during the audit by moving the open conjecture into the hypotheses.

The systemic failure mode is the manuscript's own MA-1 discipline
(shadow ≠ object) violated one level up: definitions, conventions, and
finite enumerations promoted to theorem-status slogans, and "3+
independent verification paths" degrading under inspection into one
derivation implemented three times.

---

## 2. Independently verified spine (direct computation at the main line)

1. Level-4 vacuum Virasoro Gram matrix in basis {L₋₄|0⟩, L₋₂²|0⟩}:
   G₁₁ = 5c, G₁₂ = 3c, G₂₂ = c(c+8)/2; det = c²(5c+22)/2. Quasi-primary
   Λ = L₋₂²|0⟩ − (3/5)L₋₄|0⟩ (coefficient forced by L₁Λ = 0, i.e.
   3 + 5x = 0), consistent with Λ = :TT: − (3/10)∂²T since
   ∂²T(0)|0⟩ = 2L₋₄|0⟩. Norm ⟨Λ|Λ⟩ = c(5c+22)/10 **exactly**.
2. Poles of h_M = h_LV/𝒩(M): c = 0 and c = −22/5 = c(M(2,5)) Yang–Lee
   (1 − 6·9/10 = −22/5). ✓
3. 𝒩(M) at the Stokes pole c = −218/45 evaluates to 436/405. ✓
4. S₄ = 10/[c(5c+22)] = 1/⟨Λ|Λ⟩. ✓
5. κ is **not** preserved under Sugawara: κ_affine/κ_Sugawara-image
   = (k+h∨)²/(kh∨). The manuscript pre-empts this correctly
   (anomaly-ratio bridge ϱ = κ/c in `kac_moody.tex:855–861`;
   two-channel collapse discussion at
   `chapters/examples/genus_expansions.tex:1447`); κ(sl₂, k=1) = 9/4
   appears correctly at `topologization_chain_level_platonic.tex:610`.
6. κ(W₂) = c(H₂−1) = c/2 = κ(Vir). ✓
7. Presentation-dependence of κ is conceded in the canonical source:
   `chapters/examples/landscape_census.tex:905` ("The degree-two
   coefficient depends on a chosen one-dimensional subspace of
   fields").

Referee-verified (spot-confirmed where quoted): the weighted-Riccati
recurrence through $S_6$; K3×E row Künneth zeros;
Δ₅ weight 5 with Δ₅² = χ₁₀ (Igusa); κ_fiber = 24 = rk H̃(K3);
FF-duality sign κ(V_{−k−2h∨}) = −κ; W₃ conductor K^c = 100 and
K^κ(W₃) = 250/3; FP integrals 1/24, 7/5760, 31/967680; genus-1
M̄₁,₁ facts (∫λ₁ = 1/24, λ₁ = δ_irr/12); Cardy, Brown–Henneaux,
Carlip −(3/2)log S; F₁ = κ/24, F₂ = 7κ/5760; φ_{−2,1} coefficients
8, 12, 39, 56.

---

## 3. Pillar-by-pillar findings

### 3.1 Theorem A — grade **C−**

Statement/proof: `chapters/theory/theorem_A_infinity_2.tex:331–438`
(`thm:koszul-reflection`, KR-i…KR-v; hypothesis packages at :71–126);
properadic form `thm:A-infinity-2` at :1286–1380; Verdier lane
`chapters/theory/cobar_construction.tex:1576–1808`
(`thm:bar-cobar-verdier`); Koszul locus
`chapters/theory/algebraic_foundations.tex:274–302`.

- **Sound:** the Francis–Gaitsgory import (KR-i/ii, pro-nilpotent
  enhanced equivalence for the reduced associative operad, divided
  powers retained) is correctly scoped. Sign conventions verified by
  hand: the cobar differential squares to zero; the mixed b₁/b₂ check
  on [a|b] cancels exactly; H•(ΩB(A)) ≅ A on the toy.
- **F-A1 (TYPE ERROR, verified at main line).**
  `cobar_construction.tex:1598–1608` defines
  A^{!,co}_∞ := 𝔻_Ran(B̄(A)) and then A^!_∞ := Ω^{ch,cont}(A^{!,co}_∞);
  lines 1633–1655 of the same file prove 𝔻_Ran(B̄(A)) is an **algebra**
  (deconcatenation coproduct Verdier-transposes to μ_Verdier; "Thus the
  Verdier dual of the bar coalgebra is an algebra object"). Cobar
  consumes coalgebras; no coproduct on 𝔻_Ran B̄(A) is ever constructed.
  `def:chiral-koszul-pair` (`chiral_koszul_pairs.tex:1013–1014`)
  declares the compatibility datum has "already performed that
  completed cobar step," yet `thm:bar-cobar-isomorphism-main`(2)
  (`chiral_koszul_pairs.tex:5483–5486, 5531–5538`) applies Ω^cont on
  top of it — cobars twice. Finite-window shadow computes id, not
  (−)^!. The type-correct intertwining 𝔻_Ran∘B̄_X ≃ B̄_X∘(−)^! exists
  only as an unproven display in a remark
  (`bar_cobar_adjunction_inversion.tex:4432–4434`), with (−)^!
  circularly defined as Ω𝔻B̄. **Repair:** delete one cobar —
  𝔻_Ran B̄(A) *is* the dual algebra (its own μ_Verdier shows this) —
  and prove the remark-level slogan as the actual intertwining theorem.
  (As of 08:00 JST the CLAUDE.md summary has been retyped in exactly
  this direction — "Verdier algebra K_X(A_b) = 𝔻_Ran B_X(A_b)" — but
  the manuscript body at `cobar_construction.tex:1608` still carries
  the double-cobar definition.)
- **F-A2 (intertwining is a definition, not a theorem).** The proof of
  `thm:bar-cobar-verdier` says so verbatim
  (`cobar_construction.tex:1750–1756`): the identification "is an
  identification of the constructed Verdier-dual bar component, not an
  additional comparison theorem."
- **F-A3 (dualizability assumed).** The theorem's hypotheses "make"
  the Ran object Verdier-dualizable (`cobar_construction.tex:1588–1591`);
  `lem:bar-holonomicity` (:366–425) covers only D_X-finite-type with
  regular singularities — satisfied by **no archetype vertex algebra
  as a whole object**; all five archetypes have open H_VD input lists
  (`theorem_A_infinity_2.tex:693–732`). Theorem A currently applies to
  square-zero toys, finite windows, and one claimed Heisenberg
  instance.
- **F-A4 (K² ≃ id is definitional).** Kosz(X) is defined as the locus
  where the counit is a quasi-isomorphism
  (`algebraic_foundations.tex:274–302`); the slogan restricted to the
  counit half is true by definition of the locus. Two distinct functors
  are both called K (`theorem_A_infinity_2.tex:52–56` vs
  `chiral_koszul_pairs.tex:2668`); under the 𝔻∘B̄ reading, K² ≃ id is
  proved nowhere (KR-v proves Verdier biduality B ≃ 𝔻𝔻B, a different
  statement). The chapter head `algebraic_foundations.tex:31–34`
  advertises a K² clause that `thm:koszul-reflection` does not contain.
- **F-A5 (downstream promotion).** `chiral_koszul_pairs.tex:2668–2677`
  and `cobar_construction.tex:2934–2937` promote the Conjectured
  factorization clause KR-iii to a "symmetric-monoidal adjoint
  equivalence" — symmetric-monoidality appears in no statement or
  proof (bar is at best lax monoidal), and the Conjectured status of
  H_fact is dropped in the restatements. The "proof" of KR-iii
  (:423–426) restates H_fact verbatim.
- **F-A6 (proof-by-narrative inside ProvedHere).** The
  "non-degeneracy by induction" paragraph
  (`cobar_construction.tex:1787–1798`) misstates the FM boundary
  (ignores screen bundles and the X-fibering) to prove by "Künneth
  induction" something either tautological or unproven.

### 3.2 Theorem H — grade **C committed / D+ live trajectory**

Committed state (`df6a9be`, in `chapters/theory/chiral_hochschild_koszul.tex`
as committed): `thm:hochschild-concentration-E1` at 1521
(**Conjectured**); open obligation `conj:ordered-twisted-tensor-acyclicity`
at 1479; healed `lem:chiral-homotopy-transport` at 1429; FM-collapse
engine `prop:fm-tower-collapse` at 996; symmetric `thm:main-koszul-hoch`
at 2099 (Conditional).

- **The excision was correct.** The old step claimed a contracting
  homotopy on OS(A_{m−1})^{≥1} with dh + hd = id − π₀ — impossible (OS
  carries zero differential and nonzero positive-degree cohomology,
  Poincaré polynomial ∏(1+jt)); Shelton–Yuzvinsky contracts the Koszul
  complex OS ⊗ (OS^!)∨, never OS itself. The replacement lemma is
  correct.
- **F-H1 (open hole, exactly named).** Degrees ≥ 3 die at precisely
  one step: positive-fibre acyclicity of the residue-twisted tensor
  complex at every collision stratum — which is
  `conj:ordered-twisted-tensor-acyclicity`, unproved. "Part 2" of the
  healing was never committed.
- **F-H2 (conjecture as stated admits a counterexample).** It assumes
  only chiral-Koszul + PBW; any commutative chiral algebra (regular
  OPEs) passes those trivially, the residue twist d₁ vanishes, and the
  positive Arnold classes survive — non-acyclic. A
  nondegenerate-curvature/genericity hypothesis is needed and not
  stated. All proved Heisenberg contractions divide by k (k ≠ 0);
  `lem:curved-dual-centre-heisenberg` itself concedes the k = 0 shadow
  degenerates.
- **F-H3 (no non-vacuous verified example).** No chiral algebra is
  verified to satisfy the full H_H package; no ChirHoch^{≥3} vanishing
  is verified for any example. The sole ProvedHere computation
  (`comp:fermion-hochschild`) checks only degrees 0–2 and its degree-2
  witness is internally inconsistent: the claimed generator ψψ* is
  exact under the rescaling 1-cochain N(ψ) = ψ, N(ψ*) = 0 — the very
  mechanism used two paragraphs earlier to kill the boson level
  cocycle at k ≠ 0. `thm:virasoro-hochschild`
  (`hochschild_cohomology.tex:208`) argues ChirHoch¹ = 0 from generic
  Verma irreducibility (non sequitur as written) and obtains
  ChirHoch² = ℂ circularly through the conditional duality.
  `compute/lib/chiral_hochschild_engine.py:5` self-declares it is "not
  a chain model for the full derived center."
- **Genuinely proved and worth keeping:** depth-one two-point
  Heisenberg residue contractions (verified: α_{(n)}α_{−n}^q 1 =
  qnk·α_{−n}^{q−1}1), the curved Clifford dual-centre lemma
  (finite-window contraction + ML surjectivity), the correct
  critical-level exclusion (`hochschild_cohomology.tex:~280`, unbounded
  Feigin–Frenkel centre recorded and excluded), and the FM-collapse
  endpoint (full-collision stratum contributes holonomic D_X-Ext on a
  curve, amplitude [0,2] — standard and fine).
- **F-H4 (URGENT — live status-laundering).** During the audit, a
  concurrent session rewrote the file (+1979/−1531 at 07:31 JST,
  still growing): `thm:hochschild-concentration-E1` re-titled "Ordered
  chiral Hochschild support" and re-stamped **ProvedHere** (verified
  live at line 2101, later 2021) with hypothesis package
  "incidence-compatible finite-window retracts and Mittag–Leffler
  completion" — i.e. the open conjecture relocated into an assumed
  Definition, after which "Supp ⊆ S given a retract onto an
  S-supported complex" is trivially true and mathematically empty.
  ~20 downstream citations (e.g.
  `theorem_h_off_koszul_platonic.tex:278`,
  `mc3_five_family_platonic.tex:177`,
  `infinite_fingerprint_classification.tex:1202`) still read the label
  as the {0,1,2} concentration theorem. Recommendation: keep the
  committed Conjectured status; the single gating obligation before
  any ProvedHere stamp returns is constructing the finite-window
  collision realization for one algebra (rank-one Heisenberg, all
  strata, graded mixed-mode).

### 3.3 Theorem B — grade **B−**

Canonical pointer `chapters/theory/chiral_climax_platonic.tex:1096–1141`;
main inversion `bar_cobar_adjunction_inversion.tex:2041–2378`;
off-Koszul coderived `coderived_models.tex:1111–1254`; weight-completed
Positselski `theorem_B_scope_platonic.tex:738–875`; class-M failure
`theorem_B_scope_platonic.tex:270–352, 897–978`.

- **Sound architecture:** D^co consistently on the comodule side,
  D^ctr on the contramodule side, coacyclic-cone semantics never
  silently promoted to quasi-isomorphism; completed/pro ambients and
  ML towers honestly bookkept; the recollement skeleton of the
  higher-genus induction is valid; `mc5_class_m_chain_level_platonic.tex:161–202`
  contains the correct self-diagnosis of the falsity claim's scope.
- **F-B1 (headline circularity, self-documented).**
  `bar_cobar_adjunction_inversion.tex:2367`: "(i)⇔(ii) is definitional"
  — the counit-equivalence-on-Kosz(X) headline is a tautology; the
  real content (FTM equivalence package, chiral Loday–Vallette 2.3–2.4)
  is Conditional at `chiral_koszul_pairs.tex:745`. What "Koszul locus"
  genuinely adds over classical LV is convergence (unbounded conformal
  weight breaks the bar-length filtration), honestly replaced by
  finite-window/ML hypotheses.
- **F-B2 (falsity overclaim).** The boxed "False theorem"
  (`theorem_B_scope_platonic.tex:965–978`) and the proof sentence at
  :954–956 drop the load-bearing qualifier "compatible with the
  finite-window contractions" (:919). What is proved: (i) the trivial
  ∏-vs-⊕ lemma (:270–300, verified); (ii) the *specific* comparison
  series has no raw limit. Non-existence of the limit of the *chosen*
  homotopies does not exclude a different raw homotopy; no
  non-quasi-isomorphism is exhibited. Unqualified raw falsity sits in
  tension with Positselski's co/contra correspondence over a field
  (no finite-type or conilpotency hypotheses needed), and the
  manuscript's own finite-window model reduces to Ch(Vect)
  (:363–408).
- **F-B3 (witness typing, verified at :275).** The witness
  e_k = s⁻¹L₋ₖ ⊗ s⁻¹Lₖ does not typecheck against the manuscript's own
  bar model: in the state-space reading Lₖ|0⟩ = 0 for k ≥ −1, so every
  e_k vanishes; in the mode reading all e_k have total weight 0, so
  infinitely many independent elements pile into one weight-graded
  piece, contradicting the finite-type-per-weight lemma (:220–227) on
  which the completed tower theorem relies (a mode cutoff is not the
  weight filtration).
- **F-B4 (misattributed delegation).**
  `theorem_B_scope_platonic.tex:980–999` delegates the class-G/L
  chain-level input to "Vol II … thm:bv-bar-coderived-vol1"; that label
  lives in **Vol I** at `chapters/connections/bv_brst.tex:2500`
  (Conditional); Vol II cites it back to Vol I. The chiral Positselski
  packages (CP1–CP3; `coderived_models.tex:1123–1133`) are never
  discharged for a single worked example.

### 3.4 Theorem D — grade **C+** (genus 1 sound; g ≥ 2 definitional)

Canonical pointer `chiral_climax_platonic.tex:1333–1367`; genus
universality `higher_genus_foundations.tex:7669–7867`; obstruction
theory :5786–6024; the crux :6640–7168; clutching
`clutching_uniqueness_platonic.tex:100–330`.

- **Genus 1 is the theorem's real content and it is sound.**
  obs₁ = κλ₁ verified: Virasoro (c/2)λ₁ against the
  Beilinson–Schechtman/TUY Atiyah-algebra anchor; Heisenberg kλ₁
  (fixed-normalization caveat acknowledged at
  `higher_genus_modular_koszul.tex:3169–3181`); sl₂ at k = 1:
  obs₁ = (9/4)λ₁, ∫ = 3/32 ✓; δF₁^cross = 0 combinatorially forced ✓;
  m₁² = [m₀,−] carries the correct CDG signs and does not silently
  assume m₀ central.
- **F-D1 (two objects named obs_g, unreconciled).** The
  deformation-theoretic obstruction lives in **H²**(M̄_g, Z(A))
  (transgression d₂: E₂^{0,1} → E₂^{2,0},
  `higher_genus_foundations.tex:5808–5812`); λ_g lives in **H^{2g}**.
  The bridge is the scalar-diagonal hypothesis, and
  `rem:scalar-diagonal-honest` (:6673–6700, verified verbatim)
  concedes: the K-theoretic construction *defines* obs_g as the ch_g
  projection of κ·λ₋₁(𝔼), after which obs_g = κλ_g reduces to the
  unconditional identity ch_g(λ₋₁(𝔼)) = (−1)^g c_g(𝔼); "the
  substantive content … is precisely the scalar-diagonal hypothesis."
  The theorem at g ≥ 2 is true by construction of a redefined obs_g.
- **F-D2 (sign).** The genus-dependent (−1)^g is "absorbed by the bar
  suspension convention" (:6800–6801, 7052–7055) — a fixed convention
  cannot absorb a g-dependent sign; at odd g the computed class is
  −κλ_g.
- **F-D3 (single-path).** The Chern–Weil/BGS section is explicitly
  "corroborative, not a second derivation" (:7033). Clutching
  conditions (b), (c) are automatic for the K-theoretically *defined*
  obs_g — clutching pins the definition, not an independently
  constructed class (the Mumford facts ξ_irr*λ_g = 0,
  ξ_h*λ_g = λ_h ⊠ λ_{g−h} are themselves correct).
- **F-D4 (proof-body sloppiness).** `thm:heisenberg-obs` Step 2
  integrates the 1-form dlog θ₁ over Σ_g (ill-typed); Step 4's
  divergent Σₖ k is "evaluated geometrically" with no regularization
  shown. KM centrality of obs_g at g ≥ 2 rests on a heuristic locality
  argument (:6016) whose cycle does meet the collision locus after
  configuration-space integration; `rem:kac-moody-obs-scope`
  (:6234–6245) honestly admits the hypothesis is unverified for
  non-abelian 𝔤.

### 3.5 Five-archetype landscape and κ-matrix — grade **B−**

κ's actual definition: `higher_genus_modular_koszul.tex:2846–2860`
(genus-1 fiberwise curvature scalar, d_fib² = κ·ω₁·id), normalized per
`landscape_census.tex:879–905` by the genus-1 obstruction coefficient
**and the trace-form collision residue**.

- **All constants verify** under stated conventions (see §2). The
  Sugawara discrepancy is pre-empted; FF-duality sign passes; W_N
  values and conductors check.
- **F-K1 (κ is line-dependent, "canonical" overstated).** κ is an
  invariant of (algebra + designated primary line + level/trace
  datum), not of the VOA alone: 𝓗_k ≅ 𝓗_1 as VOAs yet κ = k vs 1;
  Niemeier κ = 24 (Heisenberg line) vs Monster κ = 12 (T-line) at the
  same c = 24. Conceded at `landscape_census.tex:905`; overstated as
  "a canonical invariant of 𝒜" at `concordance.tex:7035–7037`.
- **F-K2 (classification is enumerative, dressed as structural).**
  Genuine theorem: the line-wise trichotomy r_max ∈ {2, 3, ∞} forced
  by Riccati algebraicity H = t²√Q, Q quadratic, case-split on the
  discriminant Δ = 8κS₄
  (`shadow_tower_quadrichotomy_platonic.tex:536–556`) — depth 4 on such
  a line is impossible. Class C is adjoined by declaration
  (:519–523, "declare class(βγ_λ) := C"); the universality theorem
  (`universal_conductor_K_platonic.tex:791–830`) is scoped to the 21
  hand-selected census rows with proof "the comparison is finite
  because the census table is finite"; class B's r_max = 5 arises in a
  *different* depth notion via a heuristic +2 CoHA shift
  (`ordered_associative_chiral_kd.tex:8955–8962`). The headline
  "every standard chiral algebra collapses into one of five
  archetypes" silently mixes two depth notions and defines "standard"
  by census membership (conceded at `landscape_census.tex:1477` and
  `introduction.tex:425–441`).
- **F-K3 (S₆ ambiguity).** Two coexisting inequivalent weight-6
  normalizations: the weighted-Riccati 80(45c+193)/[3c³(5c+22)²]
  (CLAUDE.md value; √Q_T-consistent) vs the null-state
  4(240c+1031)/[c³(5c+22)²]
  (`shadow_tower_higher_coefficients.tex:86–110`), not proportional; no
  direct weight-6 OPE/Wick computation adjudicates (only S₅ has one);
  a third wrong value once lived in CLAUDE.md
  (`compute/tests/test_kappa_stratification_M.py:30–48`). The
  45c+193-vs-45c+218 tension is **not** an error: 193 is the t⁴ Taylor
  coefficient, 218 the root-norm of the same quadratic
  Q_T = c² + 12ct + [4(45c+218)/(5c+22)]t² (verified symbolically;
  radius formula = root-modulus-squared).
- **F-K4 ("Borel" is a misnomer).** |S_r| ~ ρ^r r^{−5/2} is geometric
  growth from a square-root branch point — a finite ordinary radius of
  convergence, not factorial divergence; the quadrichotomy chapter
  itself notes no Γ(r) growth (`…quadrichotomy_platonic.tex:1046–1075`)
  while the introduction and CLAUDE.md brand it "Borel-Riccati".
- **F-K5 (verification theater).** The S₆ test's "three paths" are one
  algorithm implemented three times; the archetype table's V2/V3 are
  in-theory consequences of V1; row B (K3×E) is single-path
  ("pinned separately", `landscape_census.tex:3093–3120`), its
  κ^Heis = 3 is a declared additive normalization conditional on the
  unconstructed realization morphism η_{K3,E}
  (`landscape_census.tex:556–608`, ClaimStatusConditional), and its
  scalar κ = c₊ = 4 rests on a heuristic ordered-bar reading
  (:3040–3070). The advertised "3+ independent paths" standard is not
  met for row B.

### 3.6 Physics chapters — grade **B−**

Read closely: `bv_brst.tex`, `thqg_open_closed_realization.tex`,
`entanglement_modular_koszul.tex`, `thqg_entanglement_theory.tex`,
`holographic_codes_koszul.tex`; targeted: `holographic_datum_master.tex`,
`frontier_modular_holography_platonic.tex`; skimmed:
`grand_unification_platonic.tex`, Feynman chapters.

- **Honest and correct:** the OCA firewall (derived centre = universal
  closed sector, physical bulk requires β_T) is enforced in the body
  (`thqg_open_closed_realization.tex:78–121, 725–780`;
  seven-slot scope gate
  `frontier_modular_holography_platonic.tex:1367–1416`). The genuine
  theorem content is the chiral Swiss-cheese terminality of Hochschild
  cochains (`thqg_open_closed_realization.tex:633–723`) — correct in
  kind. Entanglement: Calabrese–Cardy reproduced correctly with
  (EH1)–(EH3); `lem:ent-replica-genus-anomaly-separation`
  (`entanglement_modular_koszul.tex:295–340`) explicitly proves κ ≠ c
  and pre-empts the numerological conflation; RT labelled "scalar
  approximation", QES/Page Conjectured. BV: CME/QME/BV-algebra
  conventions all correct; the PVA gate refuses all-loop QME without
  the analytic SDR package — exactly right. Holographic codes: code
  subspace precisely defined, Knill–Laflamme stated correctly, and the
  chapter *proves the negative* (symplectic projection is not KL
  recovery, explicit 4-dimensional countermodel,
  `holographic_codes_koszul.tex:358–413`).
- **F-P1 (PHANTOM CITATION CLUSTER — integrity breach, verified by
  grep).** `CostelloGaiottoPaquette2018` is cited **12 times** in
  `chapters/connections/bv_brst.tex` with pinpoint section/equation
  numbers ("section 4, eq. (4.12)", "section 4.3", "section 7") to
  support the identification of the twisted-11D-SUGRA bulk partition
  function on ℝ³×K3×ℂ² with Φ₁₀ (:3813–3818, :4357–4414, :5387,
  :5431–5432) — **no bibliography entry for this key exists anywhere
  in the repository**, no such 2018 paper is known, and no result of
  that shape is an established theorem of the twisted-holography
  literature. Three further load-bearing keys are also absent from the
  bibliography: `Costello2017M5`, `CostelloLi2016`, `Costello2015omega`
  (5 uses). Everything downstream (the Heegner obstruction tower, the
  four-loop pair cancellations, the bulk-boundary product identity at
  :5397–5415) inherits the defect. The automorphic target for
  $\Delta_5$ is the Borcherds lift of the weight-zero index-one Jacobi
  form $\phi_{0,1}$; the coefficients of $\phi_{-2,1}$ belong to a
  separate Fourier lane. The BV-to-Heegner identification is the
  conjectural comparison map.
- **F-P2 (bibliography mismatch, verified).**
  `bibliography/references.tex:362–363` pairs the 2016 title "M-theory
  in the Omega-background and 5-dimensional non-commutative gauge
  theory" (arXiv:1610.04144) with arXiv:2111.08879 — at least one
  identifier is wrong.
- **F-P3 (misattribution).**
  `frontier_modular_holography_platonic.tex:5772–5776` (also
  :5661–5664) attributes the M5-boundary-VOA = W_{1+∞}[λ=N]
  identification to CostelloP2201, which is the *celestial* holography
  paper, not an M5/twisted-M-theory result.
- **F-P4 (cosmetic inflation).** Index entry "Ryu–Takayanagi
  formula!algebraic derivation" (`entanglement_modular_koszul.tex:4`)
  and the cross-chapter sentence at `holographic_codes_koszul.tex:63–64`
  promise more than the bodies deliver; reproduced standard results
  (CC entropy) are tagged ProvedHere rather than ProvedElsewhere.

### 3.7 Master Reconstruction Theorem — healthy as an assembly

`chapters/connections/master_reconstruction.tex:781–881`
(`thm:mr-master`, ClaimStatusConditional): the proof is pure
cross-reference to named components (Morita, Theorem A,
Eilenberg–Watts, Koszul reflection, Drinfeld double, modular functor),
each with its own status tag; the open chiral–Drinfeld comparison is
quarantined as `conj:mr-chiral-drinfeld-comparison`. Its truth reduces
entirely to the component pillars above — in particular it inherits
F-A1…F-A5 through clauses M1/M3.

---

## 4. Systemic diagnosis

The deep machinery is repeatedly correct — the FG import, Positselski
usage, moduli geometry, sign conventions, the standard-CFT and
modular-forms spine. The advertising layer above it is not. Recurring
mechanism, in the manuscript's own vocabulary: **shadow ≠ object,
applied one level up** —

1. loci defined by a property, then the property headlined as a
   theorem on that locus (Kosz(X) / counit; K² ≃ id);
2. objects redefined so the headline identity holds by construction
   (obs_g at g ≥ 2; κ_BKM = c(0)/2);
3. finite enumerations and declarations presented as structural
   classifications (five archetypes; class C by fiat; class B in a
   different depth notion);
4. "3+ independent paths" implemented as one derivation restated
   (S₆ test; row B; the "corroborative, not a second derivation"
   Chern–Weil section);
5. literature support manufactured where the algebra is asked to touch
   physics (the Costello phantom cluster).

---

## 5. Urgent operational items

1. **Live status-laundering on Theorem H** (F-H4): a concurrent
   session was, during this audit, re-stamping
   `thm:hochschild-concentration-E1` ProvedHere by relocating the open
   conjecture into an assumed-retract Definition, while ~20 downstream
   citations still read the label as the concentration theorem.
   Recommendation: halt/review that loop; keep the committed
   Conjectured status.
2. **Git object store is damaged**: `git rev-list --all --count` fails
   ("Failed to traverse parents of commit ec48c72…"); an auditing
   agent independently hit a corrupt object (reported as 66d05e3)
   during `git log --all`. For a repo whose discipline leans on its
   audit trail, run `git fsck --full`, identify the unreachable/broken
   refs, and repair before damage reaches reachable history.

---

## 6. Triage ledger (ordered)

| # | Repair | Targets |
|---|--------|---------|
| 1 | Halt/review the live Theorem H rewrite; restore Conjectured until the finite-window collision realization is constructed for rank-one Heisenberg (all strata, graded mixed-mode) | `chiral_hochschild_koszul.tex` + ~20 citing files |
| 2 | Excise or re-source `CostelloGaiottoPaquette2018` (12 uses), `Costello2017M5`, `CostelloLi2016`, `Costello2015omega`; fix `Costello2111` title/arXiv pair; re-scope the M5/W_{1+∞} attribution | `bv_brst.tex`, `references.tex:362–363`, `frontier_modular_holography_platonic.tex:5772–5776` |
| 3 | Delete the second cobar: 𝔻_Ran B̄(A) is the dual algebra directly; state and prove 𝔻_Ran∘B̄_X ≃ B̄_X∘(−)^! as the intertwining theorem (currently a remark at `bar_cobar_adjunction_inversion.tex:4432–4434`); purge the double-cobar composite from `thm:bar-cobar-isomorphism-main`(2) | `cobar_construction.tex:1598–1608`, `chiral_koszul_pairs.tex:1013–1014, 5483–5538`, six theory files; CLAUDE.md already retyped |
| 4 | Restore the "compatible with the finite-window contractions" qualifier on the class-M falsity box everywhere; re-type the witness e_k (state vs mode ambient) or replace it | `theorem_B_scope_platonic.tex:270–300, 897–978`; `bar_cobar_adjunction_curved.tex:946–965` |
| 5 | Add the nondegenerate-curvature hypothesis to `conj:ordered-twisted-tensor-acyclicity`; fix the fermion degree-2 witness (ψψ* is exact under the rescaling cochain); repair the Virasoro ChirHoch¹ non sequitur | `chiral_hochschild_koszul.tex`, `hochschild_cohomology.tex:208–330` |
| 6 | Reconcile the two objects named obs_g (H² transgression vs H^{2g} Chern projection); own the (−1)^g sign instead of absorbing it into a convention; state g ≥ 2 as conditional-by-construction in the headline, as `rem:scalar-diagonal-honest` already does in the body | `higher_genus_foundations.tex:5786–7168`, `chiral_climax_platonic.tex:1333–1367` |
| 7 | Adjudicate S₆ by a direct weight-6 OPE/Wick computation (the S₅ engine extends); retire the losing normalization; rename "Borel-Riccati" to reflect geometric growth | `shadow_tower_higher_coefficients.tex:86–137`, `compute/`, CLAUDE.md, `introduction.tex:3079` |
| 8 | Rewording pass: "canonical invariant of 𝒜" → line-dependent datum (`concordance.tex:7035`); five-archetype exhaustiveness → census-scoped with the two depth notions distinguished; delete the symmetric-monoidal promotion (`chiral_koszul_pairs.tex:2668–2677`, `cobar_construction.tex:2934–2937`); fix the Vol II/Vol I misattribution (`theorem_B_scope_platonic.tex:980–999`); fix the false chapter-head advertisement (`algebraic_foundations.tex:31–34`); retag reproduced standard results ProvedElsewhere | as cited |
| 9 | `git fsck --full`; repair the object store | repo root |

---

## 7. Repairs already in flight (observed post-audit)

As of 08:00 JST 2026-07-10, the working-tree CLAUDE.md has been
rewritten consistently with findings F-A1/F-A4 and F-B1: Theorem A's
row now names the "Verdier algebra K_X(A_b) = 𝔻_Ran B_X(A_b)" (no
cobar application; no K² ≃ id slogan), Theorem B's row is restated as
quadratic Koszul recognition q_{A_b}: A_b^i → B_X(A_b), and the
five-object list types A^!_{b,∞} = 𝔻_Ran B_X(A_b) as the Verdier
algebra. The manuscript body has **not** yet followed: the double-cobar
definition is still live at `cobar_construction.tex:1608`, the Theorem
H ProvedHere stamp is still live at `chiral_hochschild_koszul.tex:2021`,
and the 12 phantom citations are still present in `bv_brst.tex`.
Summary-file repairs without body repairs invert the epistemic
hierarchy (the .tex source outranks CLAUDE.md); the body edits of
triage items 1–3 are the real work.

---

# Part II — Mathematical yield (fresh-eyes pass, same date)

A second, stricter pass: one referee forbidden from reading CLAUDE.md,
FRONTIER.md, notes/, status appendices, or Part I above, instructed to
verify the four flagship proof chains line-by-line and grade only
**true + proved + new**. A theorem whose hypothesis package contains
its conclusion counts as zero regardless of labelling.

**Yield grade: D (bordering C−).** Every flagship theorem either
encodes its conclusion in a named hypothesis package or is elementary
algebra downstream of a postulated recursion; what is genuinely proved
is genuinely known; the one claimed independent numerical verification
is fabricated.

The four chains, as actually proved:

1. **obs₁ = κλ₁ — zero yield.** The proof of the Heisenberg clause is
   "The package H_D¹ identifies the self-contraction trace … with the
   curvature of the Hodge line; its coefficient is κ"
   (`higher_genus_foundations.tex:5848–5850`); the affine clause "is
   the package H_D¹ in this normalization" (:5903–5905). The true
   underlying statement is classical: Quillen 1985 /
   Beilinson–Schechtman 1988 / TUY determinant-line anomaly —
   κ(βγ_λ) = 6λ²−6λ+1 is Mumford's exponent. Worse, :6499–6502
   asserts the identity "remains unconditional for all families",
   contradicted by every proof site in the file.
2. **The r_max ∈ {2,3,∞} trichotomy — conditional on an underived
   recursion.** Given the quadratic convolution recursion, H = t²√Q
   and the discriminant split are correct elementary power-series
   algebra. But the recursion is never derived from any chiral/bar
   computation: `shadow_tower_higher_coefficients.tex:328–366` lists
   the residue complex, contraction, and transferred brackets as
   open, and "Every proposed value of S_r begins after this input";
   the quadrichotomy chapter's provenance lemma cites *itself*
   (`shadow_tower_quadrichotomy_platonic.tex:204–217`). Statement
   error: class M is characterized by "Q irreducible" (:496–499) —
   the correct criterion (used by the proof) is Q not a perfect
   square; reducible non-square Q also gives r_max = ∞.
3. **S₅ — the "independent Wick verification" is fabricated.**
   `compute/lib/s5_virasoro_wick.py:291–337`: the decisive function
   returns the hard-coded `Fraction(-48, 10)` beneath a narrative
   comment; the set-partition and perfect-matching enumerators
   (:257–288) are dead code, never called; the docstring claims the
   two chains "share NO intermediate derivation symbol". The
   provenance proposition attributes S₅ to "Belavin–Polyakov–
   Zamolodchikov 1984" (`landscape_census.tex:1435`) — BPZ contains
   no such invariant — and cites
   "Appendix~\ref{appendix:virasoro-shadow-tower-computation}", a
   label that exists nowhere in the repository (:1454). The genuinely
   proved fragment — level-4 Gram matrix, ⟨Λ|Λ⟩ = c(5c+22)/10 — is
   correct and classical (re-verified twice in this audit).
   Side note (main-line): the level-5 vacuum Gram matrix is
   [[10c, 4c], [4c, c(c+6)]] with det = 2c²(5c+22), so the *shape*
   S₅ ∝ 1/[c²(5c+22)] is the right inverse-Gram form — but no
   level-5 computation exists in the repo.
4. **Weight-completed bar–cobar inversion — correct assembly, absent
   core.** The complete filtered comparison lemma
   (`bar_cobar_adjunction_inversion.tex:2050–2091`; Milnor/lim¹) and
   the completed-tower MC convergence
   (`bar_cobar_adjunction_curved.tex:1028–1248`) are line-by-line
   sound — and standard (Eilenberg–Moore/Boardman; Positselski's
   routine lemma). The finite-stage chiral input is never proved:
   H_CL items (iii)–(iv) (`chiral_koszul_pairs.tex:350–377`) assume
   stratumwise identifications with ordinary dg bar/cobar models
   compatible with collision residues — precisely the geometric
   theorem a chiral bar–cobar inversion would consist of. A
   translation of FG12 + Positselski, not a new convergence argument.

**Complete list of true + proved mathematics found on the flagship
chains** (all classical or trivial): the level-4 Virasoro Gram data;
degree-r extraction of a Hamiltonian master equation
(`appendices/nonlinear_modular_shadows.tex:2212–2246`); the
conditional √Q trichotomy; the filtered comparison and MC-convergence
lemmas; ch(λ₋₁𝔼) = (−1)^gλ_g + …, λ_g² = 0, the FP generating
function (Mumford/Faber–Pandharipande, correctly cited); the elliptic
propagator Arnold-defect computation.

**Consequences for Part I:** Part I §3.5's statement that "S₅ has a
genuinely independent Wick verification" is **overturned** — the
verification is circular at the code level. Part I's grades measured
correctness-as-scoped and process; measured as mathematical yield
(true + proved + new), Vol I currently contains no publishable-weight
new theorem on its flagship chains. Triage addition (top priority):
delete or actually implement `s5_virasoro_wick.py`; remove the BPZ
misattribution and the phantom appendix citation; fix the class-M
irreducibility wording.

---

# Part III — Post-repair ledger

**Snapshot:** 2026-07-10, live working tree above commit
\(e011027\). **Verdict:** the manuscript has moved substantially toward
a canonical conditional theorem architecture.  The active Vol~I
surfaces now distinguish the primitive algebra, its full bar coalgebra,
its quadratic coalgebra, its Verdier algebra, the chosen strict Koszul
partner, the derived centre, the ordinary centre local system, the
native deformation class, its virtual \(K\)-class, its Hodge character,
and its numerical graph trace.  Each passage among these objects now
has a named map and a stated hypothesis package.  Canonical closure is
therefore concentrated in the explicit constructions listed in
§III.8, with each obligation localized to a named comparison problem.

## III.1. Canonical objects and comparison maps

Let \(A=T_X(V)/(R)\) be a connected positive quadratic presentation
in the Open quadrant.  The current object ledger is:

| Level | Object or map | Canonical meaning and type |
|---|---|---|
| \(1\) | \(A=T_X(V)/(R)\) | The chosen augmented \(E_1\)-chiral algebra presentation. |
| \(2\), quadratic | \(A^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)\) | The quadratic coalgebra determined by the presentation. |
| \(2\), full | \(B_X(A)=T^c(s^{-1}\bar A)\) | The full completed bar coalgebra with its chiral collision differential. |
| \(2\), recognition | \(q_A:A^{\mathrm i}\to B_X(A)\) | The quadratic comparison; Theorem~B asks precisely for this map to be a quasi-isomorphism. |
| \(1\leftrightarrow2\) | \(\Omega_XB_X(A)\xrightarrow{\sim}A\) | Universal associative reconstruction in the pro-nilpotent Francis--Gaitsgory Ran ambient; \(H_{\mathrm{fact}}\) carries factorization closure and \(H_{\mathrm{conv}}\) carries the completed chain realization. |
| \(2\), Verdier | \(K_X(A)=\mathbb D_{\mathrm{Ran}}B_X(A)\) | The Verdier algebra obtained by dualizing the full bar coalgebra. |
| \(2\), dual comparison | \(\mathbb D(q_A):K_X(A)\to\mathbb D_{\mathrm{Ran}}(A^{\mathrm i})\) | The Verdier dual of quadratic recognition. |
| \(2\), chosen pair | \(\nu_A^{\mathrm{pair}}:K_X(A)\to A^!\) | The selected comparison with a strict or completed Koszul partner.  The manuscript currently writes this map as \(\nu_A\). |
| \(2\), residue-dual | \(C_A^{\mathrm{res}}=C_X(s^{-1}\mathbb D_XV,s^{-2}R^\perp)=(A^!_{\mathrm{quad}})^{\mathrm i}\) | The coalgebra attached to the residue-dual quadratic presentation. |
| \(2\), polarization | \(\chi_{A,\beta}:A^{\mathrm i}\to C_A^{\mathrm{res}}\) | The filtered coalgebra comparison supplied by \(H_{\mathrm{res}}(A;\beta,\chi)\). |
| \(3\) | \(Z_{\mathrm{ch}}^{\mathrm{der}}(A)=C^\bullet_{\mathrm{ch}}(A,A)\simeq R\!\operatorname{Hom}_{A^e}(A,A)\) | The chiral derived centre and brace algebra; this is the object of Theorem~H. |
| \(3\to5\), Theorem C | \(\mathcal Z(A)\), \(\mathbf C_{g,n}(A)=R\Gamma(\overline{\mathcal M}_{g,n},\mathcal Z(A))\) | The ordinary fibre-centre local system and its derived global sections on a stable pair \(2g-2+n>0\), with \(d_{g,n}=3g-3+n\). |

Theorem~C uses a chosen brace quasi-isomorphism
\[
 \iota_Z^{\mathrm{der}}\colon
 Z_{\mathrm{ch}}^{\mathrm{der}}(A)
 \xrightarrow{\ \sim\ }
 Z_{\mathrm{ch}}^{\mathrm{der}}(A^!).
\]
Taking \(H^0\), followed by the strict-flat fibre-centre comparison
\(C0\), gives
\[
 \iota_Z\colon\mathcal Z(A)\xrightarrow{\ \sim\ }\mathcal Z(A^!).
\]
For each stable pair \((g,n)\), its derived global-sections map is
\[
 j_Z:=R\Gamma(\iota_Z)\colon
 \mathbf C_{g,n}(A)\xrightarrow{\ \sim\ }\mathbf C_{g,n}(A^!).
\]
The \(C1\) datum represents involutions
\(\sigma_A,\sigma_{A^!}\) and the anti-equivariance
\(\sigma_{A^!}j_Z=-j_Z\sigma_A\).  Hence
\[
 \chi^-_{A;g,n}:=
 j_Z\big|_{\operatorname{im}p_A^-}\colon
 \operatorname{im}p_A^-
 \xrightarrow{\ \sim\ }\operatorname{im}p_{A^!}^+.
\]
Thus the second summand is the genuine positive eigensummand of the
\(A^!\)-centre, transported into the \(A\)-ambient complex.
Perfectness and the anti-invariant pairing give the degree
\(-d_{g,n}\) Lagrangian complementarity assertion.  In particular,
genus one uses \((g,n)=(1,1)\) and shift \(-1\), while stable genus
zero uses \((0,3)\) and shift \(0\).  The unit-line formula at
\((0,3)\) additionally uses the represented coefficient involution.
The shifted-symplectic enhancement belongs to its separate package
\(C2\).  Under trace--eigenclass compatibility, the normalized
Theorem~D trace sends the represented \(C1\) eigensummands to the
scalar \(K^\kappa(A)\).
This construction is canonical relative to the two strict-flat
representatives, the supplied map \(\iota_Z^{\mathrm{der}}\), the two
represented involutions, and the chosen strictification of
anti-equivariance.  Absolute canonicity is the contractibility theorem
for their joint choice space; its current status is **Open**, with
source obligations at
'higher_genus_complementarity.tex:1138--1140,2447--2449'.

Two uses of the letter \(\nu\) now have distinct types.  Besides
\(\nu_A^{\mathrm{pair}}\) above, the scaled-retract convention uses a
scalar \(\nu_A^{\mathrm{sc}}\in k^\times\):
\[
 d_Ah_A+h_Ad_A
 =\nu_A^{\mathrm{sc}}
   \bigl(\operatorname{id}_{C_A}-\iota_Ap_A\bigr),
 \qquad
 \widetilde h_A=(\nu_A^{\mathrm{sc}})^{-1}h_A.
\]
An explicit chain map from this retract to the scalar trace complex is
the datum which can identify
\(\nu_A^{\mathrm{sc}}=K^\kappa(A)\).  The superscripts in this ledger
make the type distinction visible; a subsequent notation pass can
adopt them throughout the manuscript.

The residue-dual comparison is Conditional on its three named
packages.  The packages \(H_{\mathrm{CL}}\) and
\(H_{\mathrm{res}}\) give the coalgebra roof
\[
 B_X(A)\xleftarrow[\sim]{q_A}A^{\mathrm i}
 \xrightarrow[\sim]{\chi_{A,\beta}}C_A^{\mathrm{res}}.
\]
Continuous Verdier duality under
\(H_{\mathbb D}^{\mathrm{bar}}\) gives the algebra cospan
\[
 K_X(A)\xrightarrow{\mathbb D(q_A)}A^!_{\mathrm{quad}}
 \xleftarrow{\mathbb D(\chi_{A,\beta})}
 \mathbb D_{\mathrm{Ran}}C_A^{\mathrm{res}}.
\]
A chosen map \(c_A:A^!_{\mathrm{quad}}\to A^!\) satisfying
\(\nu_A^{\mathrm{pair}}=c_A\circ\mathbb D(q_A)\) selects the partner.
This roof and cospan are the Conditional theorem surface carried by
`chiral_koszul_pairs.tex`.

## III.2. Four further type firewalls

### Collision kernel, coinvariant, and scalar

The binary collision datum is the operator-valued kernel
\[
 K_A^{\mathrm{coll}}(z)
 =\operatorname{Res}^{\mathrm{coll}}_{0,2}
   (\Theta_A^{E_1}).
\]
Its successive shadows form the typed chain
\[
 K_A^{\mathrm{coll}}(z)
 \longmapsto q_2\!\left(K_A^{\mathrm{coll}}\right)
 \longmapsto
 \tau_{A,2}^{\mathrm{res}}\,
 q_2\!\left(K_A^{\mathrm{coll}}\right)
 =\kappa(A).
\]
Here \(q_2\) passes to the diagonal/translation coinvariant, while
\(\tau_{A,2}^{\mathrm{res}}\) is the separately chosen normalized
scalar functional.  A matrix-valued classical kernel is the
represented image
\[
 r_{A,W}(z)=\rho_W\!\left(K_A^{\mathrm{coll}}(z)\right).
\]
Its CYBE assertion is Conditional on the representation/intertwining,
completion, and Arnold-boundary package
\(H_{\mathrm{CYBE}}^{\mathrm{rep}}(A;W)\).  The abstract kernel itself
carries the ordered Maurer--Cartan and Arnold relation.

### Open--closed comparison

The algebraic closed sector is
\(Z_{\mathrm{ch}}^{\mathrm{der}}(A)\).  For a
holomorphic--topological theory \(T\) with boundary chart \(A\), an
OCA datum supplies the brace-compatible map
\[
 \beta_T\colon
 \operatorname{Loc}_{\partial}
 \operatorname{Obs}^{\mathrm{bulk}}(T)
 \longrightarrow Z_{\mathrm{ch}}^{\mathrm{der}}(A).
\]
The quasi-isomorphism condition on \(\beta_T\) in the chosen
completion identifies the boundary \(E_2\) local-operator shadow of
the physical bulk with the algebraic derived centre.  Thus the
physical interpretation is carried by a specific comparison theorem,
while the derived centre retains its universal algebraic definition.

### Based comparison of bar models

For two bar models equipped with maps
\[
 u_i:B_i\xrightarrow{\sim}\mathcal B_X(A),
\]
the comparison space is taken in the slice over the fixed bar object
\(\mathcal B_X(A)\).  Its relevant mapping space is contractible.
After the base maps are forgotten, the equivalence component is an
\(\operatorname{Aut}(\mathcal B_X(A))\)-torsor.  Maurer--Cartan
transport therefore uses a chosen \(L_\infty\) quasi-isomorphism.
This is the precise model-independence statement used by the active
introduction and higher-genus surfaces.

### Lattice Hochschild grading

Let \(\Lambda\) be a positive-definite even integral lattice.  In
cochain degree \(n\), projection of every input and the output to the
conformal-weight window \((V_\Lambda)_{\leq N}\) gives the finite set
\[
 \Gamma_{n,N}:=
 \left\{\beta-\sum_{i=1}^n\alpha_i\;\middle|\;
 (V_\Lambda^{\alpha_i})_{\leq N}\neq0,
 (V_\Lambda^\beta)_{\leq N}\neq0\right\}.
\]
The finite-window cochain model decomposes as
\[
 C^n_{\mathrm{ch}}(V_\Lambda,V_\Lambda)_{\leq N}
 \cong
 \bigoplus_{\gamma\in\Gamma_{n,N}}
 C^n_{\mathrm{ch}}(V_\Lambda,V_\Lambda)^{[\gamma]}_{\leq N}.
\]
The complete chart model is the derived inverse limit of these finite
sums, equivalently the degreewise conformal-weight-completed product
of the charge-shift complexes.

The package \(H_\Lambda^{\mathrm{HH}}\) consists of a filtered
\(\Lambda\)-action \(\rho\) on the oscillator space \(\mathcal H\),
Mittag--Leffler comparison data, and the filtered quasi-isomorphism
\[
 \Xi_\Lambda\colon
 \widehat C^\bullet_{\mathrm{ch}}
 (V_\Lambda,V_\Lambda)^{[0]}
 \xrightarrow{\sim}
 \widehat C^\bullet(\Lambda;\mathcal H_\rho),
 \qquad
 \widehat C^\bullet(\Lambda;\mathcal H_\rho)
 :=R\!\varprojlim_N
 C^\bullet(\Lambda;(\mathcal H_\rho)_{\leq N}).
\]
Unimodularity makes the discriminant module
\(D(\Lambda)=\Lambda^\vee/\Lambda\) trivial.  The internal
charge-shift grading \(\gamma\in\Lambda\) remains as a second datum.

The ordered \(E_1\) complex carries the cochain map
\[
 \operatorname{res}_{\mathcal H}\colon
 CC^\bullet_{E_1,\mathrm{ch}}(V_\Lambda^{N,q})^{[0]}
 \longrightarrow
 CC^\bullet_{E_1,\mathrm{ch}}(\mathcal H,\mathcal H)
\]
obtained by evaluation on charge-zero inputs.  A collision merging
charges \(\alpha_i,\alpha_j\) has coefficient
\(\varepsilon_{N,q}(\alpha_i,\alpha_j)\); its reversed-order ratio is
the commutator bicharacter
\[
 c_{N,q}(\alpha_i,\alpha_j)
 =\frac{\varepsilon_{N,q}(\alpha_i,\alpha_j)}
        {\varepsilon_{N,q}(\alpha_j,\alpha_i)}.
\]
For \(\beta\in\Lambda\), a periodicity datum
\(H_{\mathrm{per}}(N,q;\beta)\) is the continuous chain isomorphism
\[
 T_{N\beta}\colon
 CC^\bullet_{E_1,\mathrm{ch}}
 (V_\Lambda^{N,q})^{[\gamma]}
 \xrightarrow{\sim}
 CC^\bullet_{E_1,\mathrm{ch}}
 (V_\Lambda^{N,q})^{[\gamma+N\beta]}
\]
together with the charge-dependent filtration reindexing
\[
 \Delta_{N\beta}(\lambda)
 =N(\lambda,\beta)+\frac{N^2(\beta,\beta)}2.
\]
A compatible family of these data for generators of \(N\Lambda\)
reduces charge labels to \(\Lambda/N\Lambda\), while the functions
\(\Delta_{N\beta}\) restore the conformal filtration.

## III.3. Exact status of Theorems A, B, C, D, and H

| Theorem | Current status | Exact mathematical content |
|---|---|---|
| A | **Conditional overall.** Enhanced Ran equivalence and universal reconstruction: ProvedElsewhere. Factorization closure: Conjectured. Completed-chain and Verdier realizations: Conditional. | Francis--Gaitsgory give the enhanced associative bar--cobar equivalence in the pro-nilpotent Ran ambient and the universal counit \(\Omega_XB_X(A)\simeq A\).  The package \(H_{\mathrm{conv}}\) carries this equivalence to the selected completed chain models, \(H_{\mathrm{fact}}\) carries the factorization restriction, and \(H_{\mathrm{VD}}\) constructs \(K_X(A)\) on the dualizable locus.  Quadratic recognition enters in row~B at the A/B interface. |
| B | **Conditional.** | Under \(H_{\mathrm{CL}}(A,A^{\mathrm i},\tau_{\mathrm i})\), the five conditions—Koszul twisting, \(q_A\) a quasi-isomorphism, \(\Omega_X(A^{\mathrm i})\simeq A\), acyclicity of both twisted tensor products, and strong PBW convergence on the Koszul diagonal—are equivalent.  The Conditional residue-self-dual refinement adds \(H_{\mathrm{res}}\) and \(H_{\mathbb D}^{\mathrm{bar}}\), producing the roof \(B_X(A)\xleftarrow{q_A}A^{\mathrm i}\xrightarrow{\chi_{A,\beta}}C_A^{\mathrm{res}}\) and its Verdier cospan. |
| C | **Conditional, split into \(C0,C1,C2\).** | \(C0\) constructs strict-flat fibre-centre models for both partners.  For every stable \((g,n)\), \(C1\) supplies \(\sigma_A,\sigma_{A^!}\), an anti-equivariant genuine-partner quasi-isomorphism \(j_Z\), the restriction \(\chi^-_{A;g,n}\), and the degree-\(-d_{g,n}\) perfect pairing.  \(C2\) supplies the shifted-symplectic enhancement.  Trace--eigenclass compatibility and Theorem~D produce the scalar trace shadow. |
| D | **Conditional under \(H_D=(H_D^1,H_D^K,H_D^{\mathrm{tr}},H_D^{\mathrm{graph}})\).** | The native class \(\operatorname{Obs}^{\mathrm{def}}_g\in H^2(\operatorname{Def}_g)\) has genus \(g\geq2\).  The pointed genus-one class \(\operatorname{Obs}^{\mathrm{def}}_{1,1}\) has normalized trace \(\kappa\lambda_1\) under \(H_D^1\).  The virtual, Hodge, and graph projections use their named packages. |
| H | **Conditional.** | A family datum \(H_H(A;S)\) gives a strong deformation retract of the complete chiral cochain model onto \(K_{A,S}\), hence \(\operatorname{Supp}\operatorname{ChirHoch}^\bullet(A)\subseteq S\).  The Bakalov--De Sole--Kac bounded computations are ProvedElsewhere; each curve chart also carries its bounded-to-chart quasi-isomorphism.  Koszul-dual support reflection uses an additional perfect degree-\(d\) chain pairing. |

The main Theorem-C spine, the higher-genus complementarity chapter,
and the refinements chapter now have the stable genuine-partner form
above.  Their one-index \(Q_g\)-shorthand scan is empty.  Stable
\((g,n)\), \(d_{g,n}\), genuine-partner transport, conditional
genus-zero vanishing, quotient/duality separation, protected-cofiber
transport, and PTVV typing are synchronized on these canonical
surfaces.  Secondary Vol~I consumers form the remaining local
propagation lane.

The consumer 'higher_genus_modular_koszul.tex' now carries stable
partner transport, the \(C0,C1,C2\) packages, the realization
\(\rho\), and the Theorem-D trace lane through all eight residual
groups.  Its legacy one-index scan is empty; all six type signatures
agree.  The structural scan records \(1{,}961\) balanced environment
pairs and \(1{,}289\) unique labels.  The root-focused suite records
\(162\) passing checks, followed by \(12\) passing syntax guards.

The recomputed active include graph contains \(135\) classified
occurrences across \(24\) secondary files: \(53\) same-\(A\)-ambient
partner sites, \(78\) related one-index uses, two ambient-collapse
sites, and two unrelated polynomial uses.  The recursive include
union contains \(169=68+97+2+2\) occurrences across \(26\) files in
the same four classes.  The ambient-collapse sites occur at
'yangians_drinfeld_kohno.tex:7845,7886'; the polynomial \(Q_g(x)\)
occurs at 'koszul_pair_structure.tex:3180,3183'.  The next propagation
frontier begins with
'frontier_modular_holography_platonic.tex:112--178,203--300', whose
ProvedHere cofiber and cotangent claims require the genuine-partner
ambient, followed by 'thqg_introduction_supplement_body.tex' and its
wrapper, 'holographic_codes_koszul.tex', 'thqg_entanglement.tex', and
'chiral_hochschild.tex'.

The Creutzig landscape compute lane now preserves epistemic type from
producer to consumer.  Source-backed values, Conditional
comparisons, and Open construction problems are carried by
\(\mathrm{ClaimPacket}\); symbolic arithmetic begins after the packet
contains a represented value.  The upstream/source-backed suite
records \(302\) passing checks, and the aggregate typed suite records
\(454\) passing checks.

The first minimal orthogonal case is now computed from its actual
even-orbifold generator ledger.  For \(N=7\), with \(r=N-4=3\),
\[
 n_1=3+\binom r2=6,\qquad
 n_{3/2}=2r=6,\qquad
 n_2=1,
\]
so there are \(13\) even generators and
\[
 \sum_i\frac1{\Delta_i}
 =6+6\!\left(\frac23\right)+\frac12
 =\frac{21}{2},
 \qquad
 c\!\left(\mathcal W^{-1}(\mathfrak{so}_7,f_{\min})\right)
 =\frac74.
\]
The reciprocal-weight sum is a diagnostic; the genus-one anomaly
ratio remains Open and the modular characteristic remains
Conditional.  By
Creutzig--Fasquel--Kovalchuk--Linshaw--Nakatsuka
\textup{(}2025, Theorem~1.1\textup{)}, the orbifold realization is
ProvedElsewhere for every integer \(N\geq7\).  Their Corollary~1.2
proves strong rationality at level \(-1\) for even \(N\geq8\), while
the odd family retains its Open source-visible obligation.

For types \(B,C,D\), generator arithmetic is exact, while the central
charge, dual-level relation, and reflected central-charge sum retain
Open fixed-convention packets.  The \(D_3=A_3\) oracle gives
\[
 c_{\mathrm{rank-pole}}-c_{A_3}=60k+120,
\]
which localizes the missing terms in the rank-minus-pole ansatz.
For hook partitions, the displayed partition corridor is
combinatorial data.  Creutzig--Fasquel--Linshaw--Nakatsuka
\textup{(}2025, Conjecture~A\textup{)} formulate general reduction by
stages; their Theorem~A
\textup{(}Theorems~4.1, 4.6, 4.8\textup{)} supplies the three stated
low-rank reductions.  The DS/bar and Koszul-transport packets
therefore retain their named comparison hypotheses.

Every public arithmetic constructor enforces an exact input domain:
Python and SymPy floating values raise a type error, and dimension,
rank, and partition parameters carry exact-integer gates.  The
landscape catalog is the configured \(27\)-row truncation:
\(5\) principal type-\(A\) rows, \(10\) hook rows, \(3\) minimal
\(\mathfrak{so}_{7,9,11}\) rows, \(6\) type-\(B/C\) rows, and \(3\)
type-\(D\) rows.  Its summary records this finite domain and preserves
the status of every scalar, shadow, DS/bar, duality, and KSDual field.

The \(W_3\) PBW consumer now separates represented grading data from
the nonlinear quotient construction.  The \(L_0\)-weight and target
grade bookkeeping are Computed.  Each composite \(W_{(1)}\)
coefficient carries an Open \(\mathrm{ClaimPacket}\) with hypothesis
\(H_{W_3}^{\mathrm{nl}}\), whose realization is the corresponding
nonlinear quotient calculation.  The combined source and consumer
suite records \(48\) passing checks; every emitted composite
nth-product is supported by represented quotient data.

Theorem~H now states a family-indexed implication.  For the rank-one
even superboson the bounded dimension vector is \((2,1)\), supported
in \(\{0,1\}\); for Virasoro the bounded groups are one-dimensional in
degrees \(0,2,3\).  These computations enter a curve chart through the
explicit map \(\chi_V^{\mathrm{bd}}\).

## III.4. The four objects of Theorem D

The current Theorem~D ledger is:
\[
 \operatorname{Obs}^{\mathrm{def}}_g(A)
 \in H^2(\operatorname{Def}_g(A)),
 \qquad g\geq2,
\]
\[
 \mathfrak O_g^K(A)
 =\kappa(A)\lambda_{-1}(\mathbb E_g)
 \in K^0(\overline{\mathcal M}_g),
\]
\[
 \operatorname{ch}_g\!\left(\mathfrak O_g^K(A)\right)
 =(-1)^g\kappa(A)\lambda_g,
\]
and
\[
 F_g(A)
 =F_g^{\mathrm{sc}}(A)+\delta F_g^{\mathrm{cross}}(A),
 \qquad
 F_g^{\mathrm{sc}}(A)
 =\kappa(A)\lambda_g^{\mathrm{FP}}.
\]
The package \(H_D^1\) gives the pointed genus-one identity
\[
 \operatorname{tr}_1
 \operatorname{Obs}^{\mathrm{def}}_{1,1}(A)
 =+\kappa(A)\lambda_1.
\]
The package \(H_D^K\) constructs the virtual object and its signed
Hodge character.  The package \(H_D^{\mathrm{tr}}\) supplies the
deformation-to-\(K\) comparison before the Hodge and numerical
projections.  The package \(H_D^{\mathrm{graph}}\) supplies the stable
graph functional and \(\delta F_g^{\mathrm{cross}}\).  On the
scalar-diagonal, uniform-weight locus this cross-channel term equals
zero.

The pointed-genus propagation now contains \(105\) occurrences of
\(\operatorname{Obs}^{\mathrm{def}}_{1,1}\) across \(37\) files in
the \(212\)-file active TeX surface.  Every order-one Maurer--Cartan
passage uses the pointed deformation complex \(\operatorname{Def}_{1,1}\),
while the native class \(\operatorname{Obs}^{\mathrm{def}}_g\) carries
the explicit range \(g\geq2\).

## III.5. Numerical ledger

Each entry below is either a direct exact computation or an explicitly
typed conditional interpretation.

1. **Ward recursion and free-boson Wick expansion; Computed.**  At
   \(c=1\) and consecutive integral insertion points \(z_j=j\), the
   connected stress-tensor correlators are
   \[
    G_5^{\mathrm{conn}}=\frac{775}{5184},
    \qquad
    G_6^{\mathrm{conn}}=\frac{49705}{373248}.
   \]
   Ward recursion and the free-boson perfect-matching expansion agree
   exactly.  The construction of the residue package
   \(H_{\mathrm{res}}\) carries these raw correlators to any scalar
   \(S_5\) or \(S_6\) used by the shadow tower.

2. **Two weight-six extractions; Computed.**
   \[
    R_6^{\mathrm{Ricc}}
    =\frac{80(45c+193)}
            {3c^3(5c+22)^2},
    \qquad
    C_6^{\mathrm{rel}}
    =\frac{4(240c+1031)}
            {c^3(5c+22)^2},
   \]
   and
   \[
    C_6^{\mathrm{rel}}-R_6^{\mathrm{Ricc}}
    =-\frac{4(180c+767)}
             {3c^3(5c+22)^2}.
   \]
   The first is the weighted Riccati-metric coefficient; the second is
   the order-six relation coefficient.  A level-six radical map and
   \(H_{\mathrm{res}}\) supply the corresponding representation- and
   residue-level interpretations.

3. **Weight-twelve multiple zeta value; Computed.**
   \[
    d_{11}=9,\qquad d_{12}=12,
   \]
   and Newton's identity gives
   \[
   \zeta(3,3,3,3)=\frac{
      \zeta(3)^4
      -6\zeta(3)^2\zeta(6)
      +3\zeta(6)^2
      +8\zeta(3)\zeta(9)
      -6\zeta(12)}
      {24}.
   \]
   Its motivic indecomposable projection is zero.  A primitive
   weight-twelve correction is therefore carried by a separately
   constructed graph class \(\gamma_{12}\) and its comparison maps.

4. **Calabi--Yau threefold HKR dimensions; Computed.**  For the
   quintic with \((h^{1,1},h^{2,1})=(1,101)\), the anti-diagonal HKR
   vector is
   \[
      (1,0,101,4,101,0,1).
   \]
   For its mirror it is
   \[
      (1,0,1,204,1,0,1).
   \]
   Both have total dimension \(208\).  For \(K3\times E\),
   Künneth gives
   \[
      \bigl(\dim HH^j(K3\times E)\bigr)_{j=0}^{6}
      =(1,2,23,44,23,2,1),
      \qquad
      \sum_{j=0}^{6}\dim HH^j(K3\times E)
      =\dim PV^\bullet(K3\times E)
      =\dim PV^\bullet(K3)\,
       \dim PV^\bullet(E)
      =24\cdot4=96.
   \]
   The Gauss--Manin local system on \(H^3(K3\times E)\) has rank
   \(2+2h^{2,1}=44\); the Hochschild total has dimension \(96\).
   These are distinct invariants.
   The framing engine separates the primary classifying-space input,
   the Euler scalar shadow, the represented Batalin--Vilkovisky class,
   its null-homotopy, and the framing-anomaly comparison.  The
   non-rigid quintic, mirror quintic, and \(K3\times E\) occupy the
   open represented-data state.  The local \(\mathbb C^3\) and
   resolved-conifold models occupy the same open state.  The finite
   oracle checks the incoming and outgoing differentials,
   \(d^2=0\), the cocycle equation, the identity \(d(h)=c\), and the
   cohomological scalar condition \(\ell\circ d=0\).  Consequently,
   \[
    c=d(h)\quad\Longrightarrow\quad\ell(c)=0.
   \]
   Its represented quintic cocycle has scalar projection
   \(-25/3\) and survives in cohomology.  Its \(K3\times E\) oracle
   realizes the exact zero-scalar transition \(c=d(h)\).  The anomaly
   lane uses a named framing-anomaly comparison with unit
   normalization.  The three-dimensional architecture is the
   two-stage composite
   \[
    \Phi_3^{(\Sigma_2,C)}
    =\operatorname{Sp}^{\mathrm{ch}}_{\Sigma_2,C}
     \circ\Phi_3^{\mathrm{FA}}.
   \]
   Both stages have status **Conditional construction problem**.
   The BCOV bar module now separates four fields: the cofree
   symmetric carrier, a represented differential, the resulting
   cohomology dimensions, and the independent scalar-shadow
   amplitudes.  On the constant-polyvector \(\mathbb C^3\) lane, the
   vanishing brackets give the exact zero coderivation and identify
   carrier with cohomology.  On the conifold, quintic, and
   \(K3\times E\) open coderivation profiles, the carrier is computed
   while the interaction-dependent coderivation and its cohomology retain status
   **Open**.  A supplied finite differential checks state transition,
   its grading against the computed carrier degree multiplicities,
   cohomological degree \(+1\), and \(d^2=0\); the coproduct co-Leibniz
   identity completes its coderivation verification.  The conifold
   is a support-sensitive three-vector effective carrier whose
   geometric comparison remains open.
   The scalar comparison routine now accepts an independently
   supplied BCOV series and distinguishes open, different,
   incomplete, differing, and agreeing outcomes.  The
   \(K3\times E\) value \(5\) occupies the BKM lane, while its compact
   Euler scalar is \(0\); the engine records the two distinct lanes
   and leaves the BCOV comparison open.  For the quintic, the
   Euler-half shadow is \(-100\), while the canonical BCOV one-loop
   scalar is
   \[
      \frac{\chi(X)}{24}=-\frac{25}{3}.
   \]
   An independent quintic BCOV oracle gives
   \[
      F_1^{\mathrm{BCOV}}=-\frac{25}{72},
      \qquad
      F_2^{\mathrm{BCOV}}=\frac{5}{144}.
   \]
   Its recorded source is
   'landscape_census.tex:prop:canonical-bcov-quintic'; every supplied
   BCOV series carries a provenance string.
   The Euler-half shadow gives \(-25/6\) and \(-35/288\) in the same
   genera, so the engine records explicit different-lane
   discrepancies.  The \(K3\times E\), conifold, and \(\mathbb C^3\)
   BCOV-series comparisons retain open status until independent
   inputs supply their comparison data.

5. **Rank-\(24\) even superboson; ProvedElsewhere at the bounded
   level.**  With \(\dim\mathfrak h=24\),
   \[
    H^n_{\mathrm{ch},b}(B_{\mathfrak h},B_{\mathfrak h})
    \cong
    (\Lambda^n\mathfrak h)^*
    \oplus(\Lambda^{n+1}\mathfrak h)^*,
   \]
   hence
   \[
    \dim H^n_{\mathrm{ch},b}
    =\binom{24}{n}+\binom{24}{n+1},
    \qquad
    \sum_n\dim H^n_{\mathrm{ch},b}=2^{25}-1.
   \]
   The bounded-to-chart quasi-isomorphism transports this vector to a
   chosen Mukai--Heisenberg curve chart.

6. **Affine critical separation; Computed.**  The polynomial
   trace-form scalar
   \[
    \kappa_{\mathrm{aff}}(V_k(\mathfrak g))
    =\frac{\dim\mathfrak g}{2h^\vee}(k+h^\vee)
   \]
   extends to the critical level with
   \(\kappa_{\mathrm{aff}}(V_{-h^\vee}(\mathfrak g))=0\).  The
   Sugawara central charge
   \(c_{\mathrm{Sug}}=k\dim\mathfrak g/(k+h^\vee)\) and the KZ/DS
   comparison packages carry their critical poles.  Five focused
   modules verify this separation in \(719\) tests.

## III.6. Focused verification runs

The following focused runs completed successfully during the repair
session:

| Surface | Observed result |
|---|---:|
| Theorem~A ambient and transition packages | 36 passed |
| Full bar--Verdier typed chain | 76 passed |
| Quadratic and residue-dual roof/cospan | 199 passed |
| Chiral Koszul claim-surface synchronization | 200 passed |
| Collision kernel, coinvariant, operator, and scalar | 336 passed; 4 expected xfails |
| Theorem~C/H centre-local-system lane | 407 passed |
| Holographic scalar-family guards | 98 passed |
| Theorem~D pointed-genus structural gate | 4 passed |
| Theorem~D focused four-object suite | 28 passed |
| Theorem~H computation engines | 193 passed |
| Theorem~H source and cross-volume guards | 33 passed |
| Public theorem spine | 6 passed |
| Level-\(4\) F5 descent | 6 passed |
| Based comparison of bar models | 2 passed |
| Ward, Wick, and weight-six focused suite | 101 passed |
| Weight-twelve MZV, Vol~I | 72 passed |
| Calabi--Yau threefold framing and BCOV engines | 186 passed |
| Affine critical trace/Sugawara separation | 719 passed |
| Lattice Hochschild charge and periodicity structure | 17 passed |
| Disjoint A/D/lattice/CY3-framing/BCOV integration suite | 253 passed |
| Frozen claim registry and dependency validation | 158 passed |
| Higher-genus modular Theorem~C root-focused suite | 162 passed |
| Higher-genus modular Theorem~C syntax guard | 12 passed |
| Creutzig landscape upstream/source-backed suite | 302 passed |
| Creutzig landscape aggregate typed suite | 454 passed |
| \(W_3\) PBW grading and nonlinear-quotient status suite | 48 passed |
| Final typed-theorem and compute integration invocation | 922 passed |
| Initial disjoint transitive frontier audit | 1,464 passed; 75 typed obligations |
| Blue/green typed frontier closure | 107 passed |
| Blue/green closure with upstream compute lanes | 561 passed |
| BCOV graded-carrier and independent-series suite | 94 passed |

Several rows share test modules.  Each row records an individual
observed run; the ledger consequently treats the table as an
overlapping family of checks, with each count attached to its row.
The \(922\)-check row is one command-level invocation with a
pairwise-disjoint module selection spanning the typed \(W\)-landscape
and nonprincipal \(B/C/D\) lanes, the \(W_3\) quotient lane, canonical
Theorem~C, the A/D/lattice integration lane, Calabi--Yau
threefold/BCOV, and the registry parser with its Open dependency
boundaries.
The initial read-only transitive invocation exercised \(1{,}539\)
pairwise-disjoint downstream checks.  It recorded \(1{,}464\) passing
checks and isolated \(75\) interface obligations beyond the repaired
lane.  Typed blue/green repair closes \(34=27+7\) of these obligations:
the focused blue/green suite records \(107\) passing checks, and its
integration with the upstream compute lanes records \(561\) passing
checks.  A fresh run of the five frontier modules records \(171\)
passing checks and \(41=26+14+1\) active interface failures:

| Priority | Downstream surface | Historical obligations | Current status and canonical repair |
|---:|---|---:|---|
| 1 | 'test_ds_kd_blue_team.py' | 27 | **Closed here.** Packet arithmetic and scalar-to-Boolean promotions now lift through the epistemic type. |
| 2 | 'test_theorem_ds_koszul_hook_engine.py' | 26 | **Active.** Lift packet equalities, sums, and differences; derive structural compatibility from represented comparison data. |
| 3 | 'test_ds_kd_green_team.py' | 7 | **Closed here.** Open \(\rho\)-packets now remain Open through the \(\kappa=\rho c\) product until \(\rho\) acquires a represented value. |
| 4 | 'test_theorem_nonprincipal_sl5_32_engine.py' | 14 | **Active.** Repair seven packet coercions and synchronize seven generator-spectrum, KRW, and conductor assertions with the canonical oracle. |
| 5 | 'test_brst_sl5_subregular_engine.py' | 1 | **Active.** Replace the prior \(c(1)=-236\) assertion by the canonical value \(c(1)=-78\). |

The Calabi--Yau row decomposes as \(92+94=186\) across the framing and
BCOV modules.  The affine row decomposes as
\(115+125+253+104+122=719\) across the complementarity, Polyakov,
Chern--Simons, effective-action, and remaining-comparison modules.
Scoped source invocations of 'git diff --check' completed cleanly.
The repository-wide invocation reaches pre-existing generated
whitespace in 'out/main.log'.  The targeted TeX environment counts
remained balanced.

## III.7. Represented F5 class and cross-volume divergences

The level-\(4\) vertical carries the seven-part package
\(H_4^{\mathrm{vert}}=(\mathrm{H1})\text{--}(\mathrm{H7})\).  Its
seventh clause is the represented boundary-action comparison
\[
 \Xi_4\colon
 \mathcal H_{\mathcal C}^{\mathrm{line}}
 \longrightarrow
 \operatorname{LineMod}\!\left(D(Y^+(X))\right),
\]
an \(E_2\) quasi-isomorphism in the completed factorization ambient.

Under \(H_{\mathrm{F5}}^{\mathrm{desc}}(A)\), the coefficient map is
\[
 \gamma_A\colon
 C^\bullet\!\left(
   \mathfrak{grt}^{\mathrm{ell}},
   \mathfrak{sp}(A)\otimes\mathfrak{sp}(A^!)
 \right)
 \longrightarrow
 \operatorname{Def}_{\mathrm{KZB}}^\bullet(\rho_A).
\]
The descent map
\[
 \Theta_{\mathrm{F5},A}\colon
 \operatorname{Def}_{\mathrm{KZB}}^\bullet(\rho_A)
 \longrightarrow
 \operatorname{Def}_{\mathrm{double}}^\bullet(A)
\]
represents
\[
 \operatorname{Obs}^{(1)}_{\mathrm{double}}(A)
 =H^2(\Theta_{\mathrm{F5},A})
   [\omega_{\mathrm{KZB}}(\rho_A)]
 \in H^2(\operatorname{Def}_{\mathrm{double}}^\bullet(A)).
\]
The map \(H^2(\gamma_A)\) compares the represented KZB source class
with elliptic Grothendieck--Teichm\"uller cohomology.  The map
\(H^2(\Theta_{\mathrm{F5},A})\) places that class in the deformation
complex of the represented Hall--Drinfeld double.
The equivalence
\[
 \operatorname{Obs}^{(1)}_{\mathrm{double}}(A)=0
 \quad\Longleftrightarrow\quad
 r_{\max}(A)=2
\]
is Conjecture
'conj:level-4-F5-shadow-depth'.  Thus the represented deformation
class and the shadow-depth criterion have distinct epistemic status.

The current cross-volume propagation ledger contains the following
precise divergences.

- **Theorem C.**  Vol~II
  'chapters/theory/curved_dunn_higher_genus.tex:1560–1573' presents
  Theorem~C as a derived-centre/determinant-curvature coefficient
  theorem.  Vol~II
  'chapters/theory/sc_chtop_heptagon.tex:925–965' identifies the
  chain-homotopy norm with the Theorem-C scalar sum and places the
  pairing directly on \(\operatorname{ChirHoch}\).  Vol~III
  'chapters/examples/cy_d_kappa_stratification.tex:2072–2088,
  3229–3247' promotes the Mukai arithmetic value \(8\) to a
  Theorem-C \(\mathsf B\)-row value.  Vol~III
  'chapters/theory/cy_to_chiral.tex:1927–1933,3905–3917' describes a
  factor \(2\) as a derived-centre complementarity contribution and a
  new Theorem-C entry.  Canonical Vol~I assigns Theorem~C to the
  ordinary centre local system after the chosen derived-centre bridge,
  assigns the scalar to the normalized Theorem~D trace, and records
  Mukai \(8\) as exact lattice arithmetic with a conjectural chiral
  interpretation.  The computed Vol~I scalar-trace family is
  \(\{0,13,250/3\}\), with the Bershadsky--Polyakov value \(25/3\)
  conditional on its chosen-pair package.

- **Theorem D.**  Vol~II 'FRONTIER.md:18' writes the untyped formula
  \(\operatorname{obs}_g=\kappa_{\mathrm{ch}}^{\mathrm{Hodge}}\lambda_g\)
  as Theorem~D.  Vol~III
  'chapters/connections/bar_cobar_bridge.tex:572' and
  'chapters/theory/modular_trace.tex:24' use
  \(\operatorname{obs}_g=\kappa_{\mathrm{ch}}\lambda_g\) for the
  genus-\(g\) obstruction; 'modular_trace.tex:85' refines the symbol
  to \(\operatorname{obs}^{\mathrm{sc}}_g\) while retaining only the
  scalar lane.  The same scalar presentation occurs in
  'chapters/connections/modular_koszul_bridge.tex:27,181,1153,1186',
  'chapters/connections/geometric_langlands.tex:1330', and
  'chapters/examples/cy_c_beyond_k3e_existence_obstruction.tex:
  3697,3766--3806'.  Canonical Vol~I uses the four-object chain of §III.4
  and the packages \(H_D^1,H_D^K,H_D^{\mathrm{tr}},
  H_D^{\mathrm{graph}}\).  Vol~II's tensor-Arakelov form in
  'chapters/theory/theorems_C_D_native_vol2_platonic.tex:385–606'
  is an additional conditional construction whose comparison with
  the four Vol~I objects is itself a typed theorem.

- **Calabi--Yau threefold framing.**  Vol~III
  'chapters/theory/cy_to_chiral.tex:4967--5004' states that
  holomorphic Chern--Simons supplies a Batalin--Vilkovisky contracting
  homotopy on its verified loci.  The constructions at
  'cy_to_chiral.tex:5270--5364' add a Connes hierarchy and Hopf
  decomposition, and use
  \[
   \delta_{\mathrm{BV}}(\operatorname{CS})
   =\int_X\Omega\wedge F_A
  \]
  as the toric and compact trivialization.  Canonical Vol~I assigns
  \(\chi_{\mathrm{top}}(X)/24\) to the scalar-shadow field.  A
  chain-level framing begins with a represented cocycle \(c\) in a
  named finite deformation complex and a cohomological scalar
  functional \(\ell\).  For \(\ell(c)=0\), a represented cochain
  \(h\) with \(d(h)=c\) gives the exact transition.  For
  \(\ell(c)\in k^\times\), the scalar functional witnesses survival
  of the represented class in cohomology.  A named framing-anomaly
  comparison completes the target data.

These divergences are now localized to named files and formulas.
Cross-volume propagation can therefore replace each untyped scalar
formula with the four-object chain, each derived-centre formulation of
Theorem~C with the \(C0\)-bridge to \(\mathcal Z(A)\), and each CY3
scalar-to-BV promotion with the represented cocycle and homotopy data.

## III.8. Remaining constructions and repository integrity

The frontier summary at 'FRONTIER.md:67--72' now assigns the
Borcherds coefficient identity, the chiral conductor, and the fibre
Euler characteristic to three distinct type signatures.

The remaining mathematical work has the following finite form.

1. Construct \(H_{\mathrm{fact}}\) for closure of the enhanced Ran
   bar--cobar equivalence on the factorization subcategories, and
   construct \(H_{\mathrm{conv}}\) for its completed chain
   realization.
2. Construct \(H_{\mathrm{CL}}\) for each claimed quadratic family:
   stratumwise chiral comparison, collision compatibility, strict
   inverse limit, and the quasi-isomorphism \(q_A\).  Construct
   \(H_{\mathrm{res}}\) and \(H_{\mathbb D}^{\mathrm{bar}}\) for the
   residue-dual roof and Verdier cospan.
3. Construct \(H_H(A;S)\) and the bounded-to-chart map for every
   family whose Theorem-H support is used.
4. Construct the \(C0,C1,C2\) maps, including the brace
   quasi-isomorphism, flat fibre-centre comparison, represented
   involution, perfect pairing, and shifted-symplectic enhancement.
5. Construct the chain map from the scaled retract to the normalized
   scalar trace complex, thereby comparing
   \(\nu_A^{\mathrm{sc}}\) with \(K^\kappa(A)\).
6. Construct \(H_D^1,H_D^K,H_D^{\mathrm{tr}},
   H_D^{\mathrm{graph}}\) on each advertised family and evaluate the
   cross-channel stable-graph terms.
7. Construct the OCA quasi-isomorphism \(\beta_T\) for each physical
   bulk interpretation and the represented package
   \(H_{\mathrm{CYBE}}^{\mathrm{rep}}\) for each matrix \(r\)-kernel.
8. Construct the level-six radical comparison, the coefficient map
   \(\gamma_A\), the descent map \(\Theta_{\mathrm{F5},A}\), and the
   archetype calculations entering the shadow-depth conjecture.
   Construct the boundary-action comparison \(\Xi_4\) of clause
   \((\mathrm{H7})\) for the level-\(4\) vertical.
9. Construct \(H_\Lambda^{\mathrm{HH}}\), \(\Xi_\Lambda\), and the
   compatible family of periodicity data
   \(H_{\mathrm{per}}(N,q;\beta)\) on each lattice family whose
   Hochschild or \(E_1\)-periodicity statement is used.
10. Construct the nonlinear quotient package
   \(H_{W_3}^{\mathrm{nl}}\) and its represented coefficient table for
   composite \(W_{(1)}\)-products.  This package promotes the Computed
   \(L_0\)-weight and target-grade data to exact nth-product
   coefficients.
11. Construct the represented CY3 cocycle \(c\) and cohomological
   scalar projection \(\ell\).  On the zero-scalar locus construct a
   cochain \(h\) with \(d(h)=c\); on the nonzero-scalar locus use
   \(\ell(c)\in k^\times\) as the cohomological witness.  Construct the
   named framing-anomaly comparison and the two Conditional stages
   \(\operatorname{Sp}^{\mathrm{ch}}_{\Sigma_2,C}
   \circ\Phi_3^{\mathrm{FA}}\).  Construct the finite
   interaction-dependent bar coderivation with its degree-\(+1\) table,
   square-zero identity, and coproduct co-Leibniz identity.  Compute
   BCOV amplitudes by an independent recursion and construct their
   comparison with the scalar-shadow field and the BKM input.
12. Propagate the stable genuine-partner Theorem-C notation through
   secondary Vol~I consumers, and propagate the Theorem-C and
   Theorem-D object ledgers through Volumes~II and~III.
13. Complete the \(41=26+14+1\)-assertion transitive frontier: lift
   packet equality, sums, differences, and structural compatibility
   in the hook consumer; repair the seven packet coercions and seven
   nonprincipal generator/KRW/conductor assertions; and replace the
   BRST value at level one by \(c(1)=-78\).

A fresh 'git fsck --full' on this snapshot identifies an unresolved
historical parent relation from commit
'ec48c72e6f0524b047569dd940e9bb952943902e' to commit
'66d05e35a863408e23bbd1888e48c7c49de6d228', together with historical
tree and blob obligations.  The live working tree is readable and
carries the integrated repair set.  A fresh-object-store migration has
the following form:

1. preserve the live tracked delta as a binary patch and record the
   untracked-file list;
2. clone 'git@github.com:raeez/chiral-bar-cobar.git' into a sibling
   directory with a fresh object store;
3. run 'git fsck --full' in that clone and verify the canonical base
   commit;
4. apply the tracked patch, copy the listed untracked files,
   and compare file hashes against the live tree;
5. rerun the focused suites, 'git diff --check', and the session-end
   build in the fresh clone;
6. promote the verified fresh clone to the canonical workspace after
   the comparison closes.

The frozen registry reads \(156\) TeX sources and \(142\) active
surfaces.  It contains \(4{,}683\) tagged claims:
\(1{,}666\) ProvedHere, \(439\) ProvedElsewhere, \(1{,}785\)
Conditional, \(363\) Conjectured, \(324\) Definitional, \(77\) Open,
and \(29\) Heuristic.  Its proved subregistry contains \(2{,}105\)
claims, and its dependency graph contains \(4{,}683\) vertices and
\(6{,}511\) edges.  The refreshed label index contains \(14{,}898\)
labels in \(15{,}240\) occurrences, with \(341\) repeated occurrences
or aliases pending classification.  The active-theory phase contains
\(66\) files, \(1{,}980\) vertices, and eleven Open labels.  The
formula ledger contains \(34\) entries.  Source extraction agrees
exactly with the claim stream.

The SHA-256 anchors are
claims '2982f0e75c162222f967942982117c89c952449c254b41dd419d32918da1cb80',
census '11d645c8c401bd0feb61828e45eb0b6ac80d35327b9cc71027256b546ff159c6',
graph '625e003541df0e681a01f8f9f8ca48a39d26dd3c6afec93887687d390471429f',
labels '82cc6d57ed8ecf8ebef410e355951ffa7d28ade55daac7bf1aee6f651cb6aa31',
registry '67353f308b05ed2326f61554fbd41122f29ac9f8914492bf925a84bc2ad169ea',
theorem index
'cda938023bae9e22f1fcfa34d103682d2ae59fb30c04d4c84267b62e62d0b7a1',
and active theory
'82d18a432ddb75fc8e1c7c7bca36ab770775f029f2fa13eb41a5e9429c956c76'.
All generated surfaces use the canonical vocabulary.

The dependency audit aligned five consuming claim surfaces with their
source obligations.  The \(H_1,H_3,H_4\) climax consequences now
invoke, respectively, nearby-cycle, deformation-class, and descent
data.  The arithmetic \(\varprojlim^1\)-to-Fourier consequence now
invokes the filtered automorphic-to-bar comparison.  The
wall-of-walls consequence retains the abstract \v Cech class until the
monodromy-to-derived-endomorphism comparison is supplied.  All eleven
dependency-boundary labels retain Open status.  The final
claim-registry and Theorem-A scope validation records \(158\) passing
checks.  The full LaTeX build
is the session-end validation reserved for explicit user opt-in.  This
ledger records the focused mathematical and type-surface verification
completed here.

---

# Part IV — Healing ledger (this session)

**Date:** 2026-07-10 (second healing session). **Note:** Part III now
records the integrated post-repair state.  This Part IV preserves the
chronological healing record, organized by triage item: (i) repairs
verified in the live tree from the concurrent session and (ii) repairs
executed in this session, with file:line and mathematical content. The
PostToolUse Beilinson gate raised no flags on any edit this session.

## Item 1 — Phantom citations (bv_brst / references / frontier)

- VERIFIED already repaired in tree: zero occurrences of
  `CostelloGaiottoPaquette2018`, `Costello2017M5`, `CostelloLi2016`,
  `Costello2015omega` anywhere in `chapters/`, `appendices/`,
  `bibliography/`. `bv_brst.tex` now cites real sources only
  (`Costello2111` = arXiv:1610.04144 with its actual Theorems
  9.0.2–9.0.3, `CL20`, `GN96Igusa`, Bruinier); the Φ₁₀/BV
  identification is `rem:bvbrst-paramodular-anomaly`
  (ClaimStatusConjectured, `bv_brst.tex:3190–3205`) and the
  cross-dimensional comparison is stated as the open morphism
  ρ_Ω^obs (`bv_brst.tex:3174–3187`). `references.tex:362–363` now
  pairs the 1610.04144 title with arXiv:1610.04144 (2016).
  `frontier_modular_holography_platonic.tex` M5 section
  (`thm:frontier-m5`, ~:5659–5771) attributes W_{1+∞} to
  `Costello2111` with "expected"-scoped finite-N statement and
  Conditional stamp; no `CostelloP2201` misattribution and no
  "central result of" phrasing remain.
- THIS SESSION: nothing further needed (verification only).

## Item 2 — Verdier-lane type error (Theorem A)

- VERIFIED already repaired in tree: `cobar_construction.tex`
  `thm:bar-cobar-verdier` (:1568–1712) defines
  K_X(𝒜) := 𝔻_Ran^cont B_X^cont(𝒜) directly as an augmented algebra
  with μ_K = 𝔻(Δ_B)∘χ⁻¹ (no second cobar); the typed intertwining
  Ω_X^{geom,cont}∘𝔻_X ⇒ 𝔻_Ran^cont∘B_X^cont is stated inside the
  theorem (Conditional, (V1)–(V5)) and proved by biduality; the
  chapter head (:80–126) and `rem:verdier-engine`
  (`bar_cobar_adjunction_inversion.tex:3020–3069`) carry the correct
  typing; A^!_∞ := 𝔻_Ran B_X(A) with 𝔻(q_A): A^!_∞ → A^! Conditional
  (`bar_cobar_adjunction_inversion.tex:1242–1330`);
  `def:chiral-koszul-pair` (`chiral_koszul_pairs.tex:733–805`) has
  compatibility datum θ₁₂: 𝔻_Ran^cont(𝒞₁) ≃ 𝒜₂ (algebra, no cobar);
  `thm:bar-cobar-isomorphism-main`(2) (:5176–5256) uses
  ν₁₂ = θ₁₂∘𝔻_Ran(η₁); the superscript notation `A^{!,co}` is purged
  repo-wide (grep: zero); `algebraic_foundations.tex:31–34` chapter
  head no longer advertises a K² clause; the "symmetric-monoidal
  adjoint equivalence" promotions are gone (grep "adjoint
  equivalence": zero).
- THIS SESSION (new proof): inscribed the missing toy verification as
  `lem:verdier-bar-square-zero-toy` + proof +
  `rem:square-zero-toy-typing` at `cobar_construction.tex:1714–1795`
  (after the proof of `thm:bar-cobar-verdier`): for
  A = k[ε]/(ε²), B̄(A) has zero differential; the transposed product
  is y^m·y^n = (−1)^{mn}y^{m+n} with the sign cocycle trivialized by
  b(n) = (−1)^{n(n−1)/2} (coboundary verified in-proof); full dual
  = k[[y]] (completed quadratic dual), window colimit = k[y] = A^!
  (R^⊥ = 0); cohomology = completion of Ext_A(k,k) = k[y]; and the
  typing remark records that a second cobar applied to 𝔻B̄(A) is
  type-incorrect and would compute the identity on finite windows.

## Item 3 — Theorem B falsity overclaim + witness typing

- VERIFIED already repaired in tree: the boxed "False theorem" is
  replaced by `prop:chiral-positselski-raw-direct-sum-class-M-false`
  ("State-family separation", ProvedHere,
  `theorem_B_scope_platonic.tex:804–831`) which scopes the conclusion
  to "a specified compatible finite-window homotopy" and defers the
  raw counit to the open cone problem
  `rem:class-m-raw-comparison-open` (:358–376, ClaimStatusOpen). The
  witness is re-typed as the state family v_k = L_{−k}𝟙,
  e_k = s⁻¹v_k ⊗ s⁻¹v_k with total bar weight 2k+2 (:291–334) —
  distinct weights, so the family lies in Π∖⊕ exactly by weight
  completion, reconciled with the finite-type-per-weight lemma
  (`lem:weight-filtration-basics`, :222–258); this supersedes the
  audit's mode-model suggestion with a cleaner state-space heal.
  The Vol II/Vol I misattribution is fixed at
  `rem:theorem-B-chain-level-G-L-attribution` (:833–852):
  `thm:bv-bar-coderived-vol1` correctly located in Vol I
  `chapters/connections/bv_brst.tex`, Conditional, with Vol II citing
  Vol I.
- THIS SESSION (re-scope): `concordance.tex:2392–2400` — the last
  surviving unqualified echo ("...fails already in class M through
  S₄ ≠ 0, so the unqualified sentence 'class-M chain-level false' is
  true only for that naive ambient") reworded to carry the
  compatible-homotopy qualifier and to name the open cone problem
  (`rem:class-m-raw-comparison-open`). Grep confirms no other
  "chain-level false"/"inversion is false"/"raw falsity" echo remains
  outside the properly scoped ghost–error–correct triple of
  `mc5_class_m_chain_level_platonic.tex`.

## Item 4 — Theorem D restratification (g ≥ 2)

- VERIFIED already repaired in tree: `higher_genus_foundations.tex`
  now carries the two-object split — Obs^def_g ∈ H²(Def_g(𝒜))
  (deformation class) vs 𝔒_g^K = κλ₋₁(𝔼_g) and its Hodge shadow
  obs^Hdg_g = (−1)^g κλ_g ∈ H^{2g} (K-theoretic), with the (−1)^g
  owned in every display (:219–222, :321–326, :5803–5819, :6058–6077,
  eq:lambda-recurrence :6010–6017) and the sign's origin isolated in
  `rem:chern-character-mumford` (:6020–6025) and
  `rem:heisenberg-anomaly` (:5837–5843). The Chern-character identity
  ch(λ₋₁𝔼) = ∏(1−e^{x_i}) is `cor:mumford-multiplicative`
  (ProvedElsewhere, :5999–6018); the bridge between the two objects is
  the named package clause H_D^tr inside
  `thm:genus-universality` (Theorem D, Conditional, four-package split
  H_D = (H_D^1, H_D^K, H_D^tr, H_D^graph), :6338–6406);
  `rem:scalar-diagonal-honest` survives (:6079–6087). The false
  unconditionality sentence (old :6499–6502) is replaced by "holds
  under H_D^1" (:6477–6478). The old sloppy `thm:heisenberg-obs` proof
  (dlog θ₁ integrated over Σ_g; divergent Σk) is excised — the current
  proof (:5822–5835) is the package identification plus the
  splitting-principle computation; no surviving ill-typed integral or
  unregularized divergent sum (grep verified).
- THIS SESSION (re-scope, five edits in
  `clutching_uniqueness_platonic.tex`): (1) ChapterIntro (:27–50)
  rewritten — installs the chapter convention
  obs_g(𝒜) := (−1)^g obs^Hdg_g(𝒜), re-scopes the identity to
  "under H_D^K on the nose", and adds the honesty sentence: clutching
  conditions are automatic for the K-theoretic class (a multiple of
  λ_g by construction), so clutching pins the representative within
  its numerical-equivalence class; a second derivation begins with an
  independently constructed deformation class. (2)
  `rem:socle-scope-explanation`
  final paragraph — same honesty statement, plus: elevating the
  corroboration to a second derivation requires an independent
  deformation-theoretic construction (= clause H_D^tr).
  (3) The four-part itemize (:759–765): "Unconditional scalar identity
  ... direct Arakelov–Faltings+BGS+GRR path" → "K-theoretic scalar
  identity ... under H_D^K; given β_g the Chern-character step is
  unconditional". (4) `rem:clutching-upstream-impact`: "the direct
  path supplies the identification independently" → "the K-theoretic
  path supplies the identification under H_D^K".
  (5) `prop:obs-g-lower-degree-components` statement and proof:
  "direct Arakelov–Faltings–BGS proof" → "K-theoretic identification
  under H_D^K" (two sites).

## Item 5 — S₅ fabrication

- VERIFIED already repaired in tree:
  `compute/lib/s5_virasoro_wick.py` was rewritten honestly — the
  hard-coded Fraction(−48,10) and dead enumerators are gone;
  `s5_virasoro_wick()` and the residue extractions raise
  `ResidueProjectionRequired`; the −48/[c²(5c+22)] value is exposed
  only as `s5_weighted_riccati_candidate` (recurrence output), with
  `s5_virasoro_recursion` computing it from the recursion engine; the
  false "share NO intermediate derivation symbol" claim is deleted;
  `compute/lib/virasoro_ward_correlators.py` implements the genuine
  Ward recursion + cycle-expansion oracle with the residue projection
  named as the open requirement. `landscape_census.tex` (~:1400–1441)
  no longer attributes S₅ to BPZ and no longer cites the phantom
  appendix label (`appendix:virasoro-shadow-tower-computation` — grep:
  zero); provenance is now "output of the weighted-Riccati recurrence;
  agreement with an ordered residue scalar is the comparison theorem"
  (Conditional). `shadow_tower_quadrichotomy_platonic.tex`
  `lem:mc-recursion-line` no longer self-cites; the classification
  criterion in `quad:ii` (:499–515) is stated correctly as "two simple
  roots over the algebraic closure, Δ ≠ 0".
- THIS SESSION (new computation + new tests + provenance pointer):
  (1) `compute/lib/s5_virasoro_wick.py` — added
  `virasoro_vacuum_expectation(modes, c)`, a from-scratch VEV engine
  using only [L_m,L_n] = (m−n)L_{m+n} + (c/12)(m³−m)δ and
  L_n|0⟩ = 0 (n ≥ −1); `virasoro_level4_gram_matrix_from_commutators`
  (engine recomputation of [[5c,3c],[3c,c(c+8)/2]]);
  `virasoro_level5_gram_matrix` — the level-5 vacuum Gram matrix in
  basis (L₋₅|0⟩, L₋₃L₋₂|0⟩), computed by the engine: entries
  10c, 4c, c(c+6), det = 2c²(5c+22) (the audit noted no level-5
  computation existed in the repo; all entries hand-verified against
  the commutators before inscription); and
  `s5_times_level5_gram_determinant` — the inverse-Gram shape identity
  S₅^Ricc · det G₅ = −96, documented explicitly as a shape consistency
  check, NOT a derivation. Docstring extended: the two consistency
  checks (recursion match, inverse-Gram shape) are named and both
  disclaimed as non-derivations; residue-complex construction of S_r
  remains open. (2) `compute/tests/test_s5_virasoro_wick.py` — five
  new tests (engine elementary values incl. bra/ket annihilation;
  level-4 engine-vs-closed-form; level-5 Gram entries + determinant;
  inverse-Gram shape at six central charges incl. c = −218/45).
  All 31 tests pass. (3)
  `shadow_tower_quadrichotomy_platonic.tex` `lem:mc-recursion-line` —
  added the provenance pointer to
  `thm:nms-all-degree-master-equation`
  (`appendices/nonlinear_modular_shadows.tex`), the actual degree-r
  extraction lemma. (4) Fixed the three surviving loose "irreducible"
  wordings to the proof's criterion "not a perfect square":
  `shadow_tower_quadrichotomy_platonic.tex` :1609 (Virasoro witness),
  :1997–2000 (K3 witness — with the explicit note that Q₋₂₁₄ is a
  difference of squares, hence reducible over ℝ, so non-squareness is
  the criterion), :2018 ("non-square Q_c").

## Item 6 — S₆ + Borel wording

- VERIFIED already repaired in tree:
  `shadow_tower_higher_coefficients.tex`
  `prop:sth-formal-sixth-order-extractions` (:384–465) presents
  R₆^Ricc = 80(45c+193)/[3c³(5c+22)²] and
  C₆^rel = 4(240c+1031)/[c³(5c+22)²] as outputs of two DIFFERENT
  extractions with their exact difference computed; the comparison
  with any residue scalar S₆(Vir_c; H_res) is deferred to the open
  residue package (`rem:s5-bpz-wick-verification`, and the Problem
  block :490–504 is ClaimStatusOpen). All manuscript sites now use the
  superscripted names R₆^Ricc / C₆^rel (grep: no bare adjudicated S₆
  outside recursion-internal derivations that define their own
  symbol). "Borel-Riccati" / "Borel radius" / "Stokes pole" are gone
  from prose repo-wide (grep: zero); the radius is presented as a
  branch-root product with r^{−3/2} transfer asymptotics for √Q
  coefficients (hence r^{−5/2} for S_r), and
  `thm:borel-summability-classM` (:1050–1102) states explicitly that
  the series is NOT Gevrey-1 and that Borel–Écalle structures do not
  follow from the quadratic identity; c_S = −218/45 is the "caesura"
  where a branch root exits the affine chart (:823–848), distinguished
  from the double-root locus.
- THIS SESSION: verification only (internal labels
  `eq:borel-radius-closed`, `sec:borel-geometric` left intact — label
  renames are bookkeeping and would touch many \ref sites for zero
  mathematical gain).

## Item 7 — Wording pass

- VERIFIED already repaired in tree: "canonical invariant of 𝒜" is
  gone from `concordance.tex` (the ~:7035 site drifted; grep of the
  exact phrase across the repo found one remaining site, fixed below).
  `thm:uc-landscape-universality`
  (`universal_conductor_K_platonic.tex:843–904`) is retitled
  "Constructed universality map on G/L/C/M census rows", scoped
  explicitly to the 21 census rows with the Yangian/quantum-lattice/
  wild-Kronecker rows separated by type signature. The introduction's
  archetype passage (`introduction.tex:455–498`) is scoped to "the
  displayed finite atlas", states the line-wise trichotomy
  r ∈ {2,3,∞} as the proved statement, presents class C via stratum
  separation, and presents class B as the conjectural
  CY-specialisation row with "proposed coordinates" r_max = 5 under
  five named hypotheses — the two depth notions are no longer mixed
  in a single headline.
- THIS SESSION (re-scope):
  `holographic_datum_master.tex:400–408` — the one surviving
  "canonical invariant of 𝒜" (for the collision residue) re-scoped:
  invariant on the cyclic-rigid generic locus, with the explicit
  sentence that its scalar projections are invariants of the triple
  (algebra, primary line, trace datum), not of the algebra alone
  (per `landscape_census.tex:905`).

## Item 8 — Theorem H guard

- VERIFIED state of the live file
  (`chiral_hochschild_koszul.tex`, 8539 lines): the concurrent rewrite
  settled on the audit's route (a) implemented honestly —
  `thm:hochschild-concentration-E1` (:2070–2103) is titled "Ordered
  chiral Hochschild support", stamped ProvedHere AS a support-transport
  statement whose hypothesis is the finite-window collision
  realization (`def:theorem-h-pbw-finite-window-lane`, :404–443, which
  ends "The deformation-retract identities and their incidence
  compatibility are the hypotheses consumed by Theorem H"); the
  retract existence is quarantined as
  `conj:ordered-twisted-tensor-acyclicity` (:1631–1672,
  ClaimStatusConjectured) — and the audit's demanded
  nondegenerate-curvature hypothesis has been ADDED via
  `def:nondegenerate-collision-symbol` (:1604–1629), which explicitly
  identifies the regular-OPE commutative case as the degenerate locus
  (blocking the audit's counterexample); the conjecture now assumes
  nondegeneracy. The fermion degree-2 witness is excised:
  `comp:fermion-hochschild` (:3457–3471) is ClaimStatusConditional
  with no ψψ* claim, deferring to a family support datum, and
  `ex:HH-fermion-complete` (:7051–7079) likewise. The Virasoro
  ChirHoch¹ non sequitur is repaired: `thm:virasoro-hochschild`
  (`hochschild_cohomology.tex:200–232`) now states the
  Bakalov–De Sole–Kac bounded computation (support {0,2,3}, real
  citation) plus a Conditional bounded-to-chart comparison — no
  Verma-irreducibility argument, no circular duality.
- Downstream citations: `theorem_h_off_koszul_platonic.tex:103` and
  :270–290 read the label as filtration/support-transport
  (conditional wording already present);
  `mc3_five_family_platonic.tex:171–183` reads it via "independent
  family support datum ... A full datum also requires ..." (already
  conditional); `infinite_fingerprint_classification.tex:~1190–1205`
  reads it via "The assumed filtered comparison ..." (already
  conditional).
- THIS SESSION (two repairs): (1) `e1_modular_koszul.tex:3354–3362` —
  the one downstream site that misread the theorem as supplying "the
  ordered twisted-tensor acyclicity" reworded: "the ordered support
  transport of Theorem ... whose finite-window-retract hypothesis is,
  in the family-generic case, the open Conjecture
  conj:ordered-twisted-tensor-acyclicity". (2)
  `appendices/first_principles_cache.md` row 302 — the stale directive
  "Cite thm:hochschild-concentration-E1 for the proof of Theorem H"
  rewritten: cite it as the conditional support-transport statement
  with the retract hypothesis named, cite the conjecture for the open
  retract existence.

## Item 9 — git fsck diagnosis (no repair attempted)

`git fsck --full` output: 808 problem lines total, of which 47 are
`missing` objects; the load-bearing damage is
- broken commit link: `ec48c72` → missing parent commit `66d05e3`
  (`ec48c72` IS in reachable history — `main`, two agent branches, and
  remote `develop` all contain it, ~790 commits behind HEAD), so any
  full-history walk (`git rev-list HEAD --count`, `git log --all`,
  clone, gc) fails with "Failed to traverse parents of ec48c72";
- missing trees `106e8db` (referenced by many broken tree links),
  `71fb17d`; missing blob `37f5a4a` and ~44 further missing objects;
  plus a large population of harmless dangling blobs.
Recent operations (log/status/commit/diff near HEAD) are unaffected.
Sole remote: `origin = git@github.com:raeez/chiral-bar-cobar.git`.
RECOMMENDED (not executed, per no-destructive-git and diagnose-only
instruction): `git fetch origin` — if origin's history is complete it
restores the missing objects non-destructively; verify afterwards with
`git fsck --full` and `git rev-list --all --count`. Do NOT run
`git gc`/`git prune` before the missing objects are restored (gc on a
corrupt store can convert recoverable damage into permanent loss).

## Open construction and propagation obligations

- The comparison
  \(\mathbb D_{\mathrm{Ran}}B_X(A)\simeq\widehat A^!\) carries the
  Conditional package
  \((H_{\mathrm{CL}},H_{\mathrm{quad}},
  H_{\mathbb D}^{\mathrm{bar}})\) together with locally finite
  quadratic pieces.  The finite-window square-zero calculation is
  ProvedHere in `lem:verdier-bar-square-zero-toy`.
- The pointed genus-one trace
  \(\operatorname{tr}_1\operatorname{Obs}^{\mathrm{def}}_{1,1}
  =\kappa\lambda_1\) is Conditional under \(H_D^1\).  A direct proof
  from the Beilinson--Schechtman/Tsuchiya--Ueno--Yamada
  Atiyah-algebra construction is the next theorem-level obligation.
- The normalized residue construction
  \(H_{\mathrm{res}}(\mathrm{Vir}_c;X)\) and its level-six radical map
  govern the comparison between the two weight-six coefficients and
  the shadow-tower scalar.
- The nonlinear quotient package \(H_{W_3}^{\mathrm{nl}}\) supplies
  the represented composite \(W_{(1)}\)-coefficient table.  The
  \(L_0\)-weight and target-grade data are Computed; each composite
  nth-product retains Open status at this construction boundary.
- The finite-window collision realization for rank-one Heisenberg at
  every stratum, including graded mixed modes, supplies the first
  complete family datum \(H_H(\mathcal H_k;S)\).
- A represented Batalin--Vilkovisky cocycle and cohomological scalar
  projection advance each Calabi--Yau threefold example from its scalar
  shadow to the deformation complex.  The zero-scalar locus carries
  the exact transition \(d(h)=c\); the invertible-scalar locus carries
  the surviving cohomology class.  A named anomaly comparison and the
  two-stage functor
  \(\operatorname{Sp}^{\mathrm{ch}}_{\Sigma_2,C}
  \circ\Phi_3^{\mathrm{FA}}\) complete the construction problem.
  The BCOV bar lane additionally requires the finite
  interaction-dependent coderivation, its degree and co-Leibniz
  checks, an independently computed amplitude field, and the
  comparison map from that field to the scalar shadow.
- The main Theorem-C spine now uses stable \((g,n)\), the genuine
  \(A^!\)-centre, the anti-equivariant map \(j_Z\), and the shift
  \(-d_{g,n}\).  The higher-genus complementarity and refinements
  chapters carry this form with an empty one-index shorthand scan.
  The \(135=53+78+2+2\) active secondary Vol~I occurrences and the
  four Theorem-D objects receive the typed propagation through
  Volumes~II and~III listed in §III.7.
- The initial transitive frontier audit isolated \(75\) downstream
  assertions across five modules.  Typed blue/green repair closes
  \(34\) with \(107\) focused and \(561\) upstream-integrated passing
  checks.  The current \(41=26+14+1\)-assertion repair frontier lies in
  the hook, nonprincipal \(\mathfrak{sl}_5\), and BRST consumers; its
  ranked obligations appear in §III.6.
- The theorem registry and dependency index have their
  post-convergence regeneration: \(4{,}683\) typed claims and a
  \(4{,}683\)-vertex, \(6{,}511\)-edge dependency graph.  The
  dependency audit aligns the five consuming claim surfaces with
  their open hypotheses.  The full LaTeX build is the session-end
  validation under explicit user opt-in.
- Repository-history recovery is a separate authorized operation.  A
  fresh authoritative object store, binary-patch transfer, hash
  comparison, and a final `git fsck --full` form its verification
  sequence.
