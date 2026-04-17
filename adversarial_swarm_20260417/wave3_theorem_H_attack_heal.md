# Wave 3 — Theorem H Adversarial Audit

Target: `thm:main-koszul-hoch`, `thm:hochschild-polynomial-growth`,
`thm:hochschild-concentration-E1`, `prop:fm-tower-collapse`,
`prop:chirhoch-sharp-hilbert`, `lem:chiral-homotopy-transport`,
`lem:chiral-quadratic-koszul`, `prop:chirhoch1-affine-km`.

Files in scope (Vol I):
- `chapters/theory/chiral_hochschild_koszul.tex` (7083 lines)
- `chapters/theory/chiral_center_theorem.tex` (ChirHoch^1 prop)
- `chapters/theory/chiral_koszul_pairs.tex` (PBW criterion body)
- `chapters/theory/theorem_h_off_koszul_platonic.tex` (off-Koszul)
- `compute/tests/test_theorem_H_hochschild_koszul.py` (HZ-IV decorator)

Skip list honoured: theorem_C_refinements_platonic, ftm_seven_fold_tfae,
theorem_A_infinity_2, ordered_associative_chiral_kd, preface.

## Phase 1 — Attack first-principles

### Attack 1. Shelton--Yuzvinsky transport to chiral Orlik--Solomon

**Claim attacked.** `prop:fm-tower-collapse` Step 3 + `lem:chiral-homotopy-transport`
invoke Shelton--Yuzvinsky (SY) Koszulity of the pure-braid
Orlik--Solomon algebra `OS(A_{m-1})` to furnish a contracting homotopy
`h_m` on `OS(A_{m-1})^{\geq 1}`. SY proves supersolvable hyperplane
arrangements have quadratic-Koszul OS algebras over a field. The
chiral bar lives on `FM_m(C)` as a `D_X`-module; the fibre cohomology
is the Arnold algebra `A_m` (the real-coefficient OS algebra of the
type-`A_{m-1}` arrangement).

**First-principles check.** SY is a statement about the
graded-commutative algebra `OS(A_{m-1})` over a field; Arnold 1969
and Orlik--Solomon 1980 identify this with `H^*(FM_m(C); R)` as a
graded ring. This identification is topological, not a `D_X`-module
statement: it extracts the constant `D_X`-module cohomology of the
fibre, which is exactly what the collision-depth spectral sequence
places on the `E_1` page fibrewise. The SY homotopy therefore
transports correctly provided the spectral-sequence coefficient
system on the fibre is the constant Arnold algebra. That is exactly
the `E_1`-page identification made in
`prop:fm-tower-collapse` Step~2 via Kontsevich formality
(`prop:en-formality`). No chiral re-proof of SY is needed; what is
needed is that the Arnold algebra structure on `H^*(FM_m(C))`
survives the chiral coefficient coupling. It does, because the
fibre cohomology is taken with constant coefficients (the coupling
to `A^{\otimes m}` is on the base, not the fibre).

**Verdict.** ACCEPT. The SY citation is used for its correct content
(Koszulity of a graded-commutative algebra over a field), and the
chiral coupling is fibre-constant. No hidden circular transport.

### Attack 2. Is `thm:pbw-koszulness-criterion` actually PBW → Koszul?

**Claim attacked.** If `thm:pbw-koszulness-criterion` derived PBW
collapse as a consequence of Koszulity, using it to prove
bar-concentration would re-introduce the Step~3 circularity the
programme claims to have healed.

**First-principles check.** Read `chapters/theory/chiral_koszul_pairs.tex:783-853`.
The theorem takes a chiral algebra `A` with PBW filtration
`F_0 \subset F_1 \subset \cdots` such that `gr_F A` is a commutative
chiral algebra (vertex Poisson), assumes (i) flatness of the
filtration, (ii) classical Koszulity of `gr_F A`, (iii) weight-finite
chain groups, and concludes chiral Koszulness of `A`. The proof
runs the filtration spectral sequence `E_0 = gr_F K`,
`E_1 = H^*(gr_F K)` collapses at `E_1` by Priddy applied to the
polynomial algebra `gr_F A`, converges by completeness. The
direction is PBW + classical Koszul ⇒ chiral Koszul, i.e.
PBW-filtration hypothesis + classical input PROVES chiral Koszulity.
The classical input is Priddy's theorem for polynomial algebras
(`chapters/theory/chiral_koszul_pairs.tex:895`), not SY.

**Verdict.** ACCEPT. The criterion runs in the healthy direction.
Using it to drive bar-concentration is not circular; bar-concentration
and FM-tower collapse are genuinely parallel consequences of PBW, as
`rem:pbw-parallel-consequences` asserts.

### Attack 3. Chain-level vs cohomology-level: is `σ^{-1}` strict?

**Claim attacked.** `lem:chiral-homotopy-transport` defines
`h_m^{ord} := σ ∘ h_m ∘ σ^{-1}` where `σ` is the Fresse chain map
of `lem:chiral-quadratic-koszul`. The latter states `σ` is a
chain map that `is an isomorphism on the degree-2 generator piece,
and its induced map on cohomology is a quasi-isomorphism whenever
P is chiral Koszul`. Cohomology qi does NOT furnish a strict
chain-level inverse `σ^{-1}`; only a homotopy inverse exists.
Yet the proof (lines 1189-1203) writes
`σ ∘ (d h_m + h_m d) ∘ σ^{-1} = σ ∘ (id - π_0) ∘ σ^{-1}
= id - π_0^{ord}`
as if `σ` admitted a two-sided strict inverse. If `σ` is only a qi,
`σ σ^{-1}` is `id` up to homotopy, and the derived identity
`d h_m^{ord} + h_m^{ord} d = id - π_0^{ord}` only holds up to a
homotopy, not strictly. This is a chain-level gap.

**First-principles assessment.** Three options.
(a) Strengthen `lem:chiral-quadratic-koszul` to produce a chain-level
isomorphism on the tensor-decomposed fibre
`B^{ord}(A)|_{FM_m(C)} ≃ OS(A_{m-1}) ⊗ A^{⊗ m}` on the Koszul locus.
The proof of `lem:chiral-homotopy-transport` (lines 1177-1181)
already asserts this identification; when it holds strictly, the
homotopy transports as written.
(b) Weaken the output to a homotopy-level contracting homotopy and
invoke the homotopy-transfer theorem (HTT, Kadeishvili) to transfer
it back to a strict homotopy on the bar side via the homotopy
inverse. HTT is a standard operadic tool (Loday--Vallette
Chapter 10) and does furnish the needed strict `h_m^{ord}` up to
a correction term supported in degree 0.
(c) Weaken the whole argument to the `E_1`-page of the collision-depth
spectral sequence, where cohomology-level statements suffice
(all we need is that higher Arnold classes die at `E_2`, which is a
cohomology-level statement).

**Verdict.** CHAIN-LEVEL GAP. The spectral-sequence formulation (c)
is what the proof actually needs, and it is cohomology-level clean;
the chain-level identity in `lem:chiral-homotopy-transport` is
stronger than needed and technically requires an HTT caveat.

**Heal.** Add a one-paragraph clarifying note to
`lem:chiral-homotopy-transport` that (i) on the Koszul locus the
tensor decomposition
`B^{ord}(A)|_{FM_m(C)} ≃ OS(A_{m-1}) ⊗ A^{⊗ m}` is chain-level
(as asserted at lines 1177-1181), so `σ` admits a strict inverse
on this decomposed model; (ii) the cohomology-level statement is
what Theorem H actually consumes via the `E_1 → E_2` vanishing in
`prop:fm-tower-collapse` Step 3. This is already implicit, but the
decorator paragraph makes the chain-level vs cohomology-level
boundary explicit.

### Attack 4. Sharp dim claim: `total dim = dim(g) + 2` or `rank(g) + 2`?

**Claim attacked.** Status table says
`ChirHoch^1(V_k(g)) = g; total dim = dim(g) + 2`. The variable `g`
overloaded (Lie algebra vs genus); `dim(g)` could be mis-read as
`rank(g)`. For `sl_2`, `dim(g) = 3`, total = `1 + 3 + 1 = 5`, not
`1 + 1 + 1 = 3`.

**First-principles check.** Read `prop:chirhoch1-affine-km` at
`chapters/theory/chiral_center_theorem.tex:2132-2197`. The statement
is `ChirHoch^1(V_k(g)) ≅ g` as `g`-modules, with
`dim ChirHoch^1(V_k(g)) = dim(g)`. At `sl_2` this gives 3, and
`rem:sl2-chirhoch-dim5` explicitly records the total `1 + 3 + 1 = 5`
for `ChirHoch^*(V_k(sl_2))`. For `sl_3`: `1 + 8 + 1 = 10`; for `E_8`:
`1 + 248 + 1 = 250`. The status-table `dim(g) + 2` is correct, with
`dim(g)` meaning the Lie algebra dimension (not rank), and the
programme explicitly distinguishes this from the older false bound
`dim ≤ 4`.

**Verdict.** ACCEPT. The formula is `dim(g) + 2` (Lie algebra
dimension, not rank). The reader-facing risk is the overloaded `g`;
the proposition uses `\fg` throughout.

### Attack 5. Critical-level exclusion

**Claim attacked.** At `k = -h^v` the theorem allegedly fails.
Does this mean `ChirHoch^2` explodes, the Koszul hypothesis fails,
or the concentration formula is merely ill-defined?

**First-principles check.** Read
`rem:critical-level-dimensional-divergence`
(lines 1709-1754) and `prop:chirhoch1-affine-km` proof paragraph
(lines 2181-2197). At `k = -h^v`:
(a) The Sugawara conformal vector is undefined (`(k+h^v)^{-1}`
divergence in the Segal--Sugawara formula).
(b) `ChirHoch^0 = Z(V_{-h^v}(g))` is the Feigin--Frenkel centre
`Fun(Op_{g^v}(D))`, a polynomial algebra on `rank(g)` generators
— genuinely infinite-dimensional.
(c) The Koszul hypothesis itself fails: `V_{-h^v}(g)` admits
singular vectors breaking flatness of the PBW filtration,
invalidating hypothesis (i) of `thm:pbw-koszulness-criterion`.
(d) Consequently `prop:fm-tower-collapse` no longer applies, and
the `{0, 1, 2}` concentration bound breaks via `ChirHoch^0` growing
without bound; the formula's failure is via infinite-dimensional
`ChirHoch^0`, not via excess `ChirHoch^{\geq 3}`.

**Verdict.** ACCEPT. The critical level is a genuine scope boundary
of Theorem H, driven by failure of Koszulness (flatness), manifesting
as infinite-dimensional `ChirHoch^0`. The programme statement "critical
level k = -h^v excluded" is correct.

### Attack 6. E_1-variant Yangian concentration

**Claim attacked.** `thm:hochschild-concentration-E1` asserts
concentration in `{0, 1, 2}` via ordered FM plus pure-braid OS
Koszulity, without going through the symmetric bar. For Yangian
`Y_ℏ(g)^{ch}` input (an E_1-chiral algebra, not E_inf), does the
concentration actually hold, or only the weaker statement that the
ordered bar is acyclic in positive degrees (which is different from
the chiral Hochschild `{0, 1, 2}` bound)?

**First-principles check.** `thm:hochschild-concentration-E1` takes
as hypothesis `A chiral Koszul algebra on X satisfying the PBW
criterion` — this is an E_inf-chiral hypothesis as stated (PBW
filtration with commutative associated graded). For the Yangian,
the E_1-chiral EK quantum VA lives on the formal disk, not on a
smooth projective curve `X`; the factorization-algebra-on-`Ran^{ord}(X)`
formulation is the one for which the pure-braid OS Koszulity
directly applies. The theorem statement elides this: it mixes
"chiral Koszul" (E_inf input) with "ordered FM + pure braid"
(E_1 apparatus). The conclusion
`ChirHoch^n(A) = 0 for n ∉ {0, 1, 2}`
is genuine for the E_inf hypothesis; for the E_1 (Yangian) input
the correct statement is that the ordered bar-cohomology is
concentrated in ordered degree 1 on the Koszul locus (which is the
definition of ordered chiral Koszulness), and this projects to the
symmetric Hochschild `{0, 1, 2}` bound via Σ-averaging only when the
Yangian has an E_inf completion.

**Verdict.** SCOPE-AMBIGUOUS. The theorem as stated is correct under
the E_inf hypothesis it asserts; the programme claim that this
covers the Yangian E_1-variant is a scope inflation. The correct
Yangian statement is the ordered bar Koszulity
(`thm:yangian-ordered-koszul` in `ordered_associative_chiral_kd.tex`),
not a symmetric Hochschild concentration.

**Heal.** Record a scope remark next to `thm:hochschild-concentration-E1`
clarifying that the "E_1" in the label refers to the E_1-page of the
spectral sequence (the `E_1` vs `E_2` distinction in
`prop:fm-tower-collapse`), not to E_1-chiral input algebras. For
E_1-chiral algebras (Yangian-type) a separate ordered bar Koszulity
statement applies, which implies the symmetric `{0, 1, 2}` bound
only after an averaging step that exists in the E_inf case.

### Attack 7. Independent-verification decorator disjointness

**Claim attacked.** The HZ-IV decorator at
`compute/tests/test_theorem_H_hochschild_koszul.py:46-75` declares
Feigin--Fuchs 1984 and Wang 1998 as verified-against sources.
Are they genuinely disjoint from the derivation path, or do they
secretly consume the same SY input?

**First-principles check.**
- Feigin--Fuchs 1984 (`hep-th/9303160`-family, and the 1984 Russian
  preprint): computes Virasoro cohomology via BRST of the Fock
  module with screening charges. The method is semi-infinite
  cohomology in the sense of Feigin, with no configuration-space
  input, no OS-algebra input, no Fulton--MacPherson compactification.
  Disjoint.
- Wang 1998 (`q-alg/9708008`): BRST cohomology for `W_N` via
  Feigin--Frenkel screenings in `U(\hat{g})` at generic level. Again
  semi-infinite cohomology, no FM, no OS. Disjoint.
- Whitehead + Kunneth for affine `sl_2`: Whitehead gives vanishing
  `H^1(sl_2; M) = H^2(sl_2; M) = 0` for finite-dim semisimple-module
  `M`; Kunneth climbs the chiral loop construction
  `\hat{sl_2}_k = sl_2 \otimes C[[t]] + C c`. This uses the
  Chevalley--Eilenberg complex, not the chiral bar. Disjoint.

**Verdict.** The three disjointness rationales stand. The decorator
is genuine.

**Residual.** The decorator is inscribed in one test file. The
decorator structure `@independent_verification` exists and is
imported from `compute.lib.independent_verification`. This is a
genuine HZ-IV decoration, not a draft.

## Phase 2 — Heal

### Heal 1. Chain-level vs cohomology-level clarifying remark

Add to `chapters/theory/chiral_hochschild_koszul.tex` after
`lem:chiral-homotopy-transport`: a remark making explicit that the
conjugation `σ ∘ h_m ∘ σ^{-1}` is well-defined strictly on the
tensor-decomposed local fibre model
`B^{ord}(A)|_{FM_m(C)} ≃ OS(A_{m-1}) ⊗ A^{⊗ m}` valid on the Koszul
locus, where `σ` restricts to a chain-level isomorphism, and that the
weaker cohomology-level statement (via `E_1 → E_2` vanishing in
`prop:fm-tower-collapse` Step 3) is what Theorem H actually consumes.

### Heal 2. E_1-scope clarification

Add to `thm:hochschild-concentration-E1` a scope remark that
"E_1" refers to the `E_1`-page of the collision-depth spectral
sequence (ordered Fulton--MacPherson), not to E_1-chiral input
algebras. E_1-chiral input (Yangian) obeys a separate ordered bar
Koszulity statement.

### Heal 3. Critical-level scope decorator

No heal needed; the scope is already stated correctly in
`rem:critical-level-dimensional-divergence`. Spot-check: preface
and intro should reflect the `k \neq -h^v` restriction when citing
Theorem H.

### Beilinson-rectified Theorem H (platonic statement, prose only)

On the Koszul locus (chiral quadratic with flat PBW filtration having
commutative associated graded), the chiral Hochschild cohomology of
a chiral algebra `A` on a smooth projective curve `X` is concentrated
in cohomological degrees `{0, 1, 2}` with the sharp bigraded
Hilbert series
  `P_A(t, q) = HS_{Z(A)}(q) + HS_{ChirHoch^1(A)}(q) · t
             + HS_{Z(A^!)}(q) · t^2`,
exhibiting on cohomology the Verdier duality
  `ChirHoch^n(A) ≅ ChirHoch^{2-n}(A^!)^∨ ⊗ ω_X`.
The amplitude `[0, 2]` is the reading of the complex dimension
`dim_C X = 1` through the collision-depth spectral sequence of the
chiral Fulton--MacPherson tower `{\bar{C}_{p+2}(X)}_{p \geq 0}`,
degenerating at `E_2` by bar-concentration (PBW collapse plus
pure-braid Orlik--Solomon Koszulity). The scope is sharp: critical
level `k = -h^v` is excluded because the Feigin--Frenkel centre
populates an infinite-dimensional `ChirHoch^0`.

Verification census:
(i) Heisenberg `H_k`: `P(t, q) = 1 + q · t + 1 · t^2`, total dim 3;
(ii) Virasoro `Vir_c`: `P(t, q) = 1 + 1 · t^2` for `c \neq 0`,
total dim 2 (degree-1 vanishes: the conformal vector is rigid);
(iii) affine `V_k(g)`: `P(t, q) = 1 + dim(g) · t + 1 · t^2`,
total dim `dim(g) + 2`; at `sl_2` this is 5, at `sl_3` it is 10,
at `E_8` it is 250.

Physically: degree 0 is the centre (local observables commuting
with everything); degree 1 is the space of first-order deformations
(outer derivations); degree 2 is the primary obstruction space
(central charges deforming the level). The `[2]` shift is the
curve dimension read through Verdier duality; the universality is
the reading of Koszul Reflection `K^2 ≃ id` on the derived centre.

Five-theorem placement: Theorem H is the reflection of Theorem A on
the tangent complex to the Maurer--Cartan moduli of chiral algebras
on `X`.

## References to attacks located in the proof

- `prop:fm-tower-collapse` Step 3 (3a-3c):
  `chapters/theory/chiral_hochschild_koszul.tex:886-951`.
- `lem:chiral-homotopy-transport`:
  `chapters/theory/chiral_hochschild_koszul.tex:1097-1224`.
- `lem:chiral-quadratic-koszul`:
  `chapters/theory/chiral_hochschild_koszul.tex:656-727`.
- `prop:chirhoch-sharp-hilbert`:
  `chapters/theory/chiral_hochschild_koszul.tex:1027-1084`.
- `thm:hochschild-concentration-E1`:
  `chapters/theory/chiral_hochschild_koszul.tex:1226-1277`.
- `thm:main-koszul-hoch`:
  `chapters/theory/chiral_hochschild_koszul.tex:1389-1504`.
- `prop:chirhoch1-affine-km`:
  `chapters/theory/chiral_center_theorem.tex:2132-2197`.
- `thm:pbw-koszulness-criterion`:
  `chapters/theory/chiral_koszul_pairs.tex:783-853`.
- HZ-IV decorator:
  `compute/tests/test_theorem_H_hochschild_koszul.py:46-93`.

## Confusion patterns flagged (CLAUDE.md eligible)

Pattern candidate: "cohomology-qi as strict inverse". When an
operadic chain map is only a quasi-isomorphism (cohomology-level
inverse), conjugation `σ ∘ h ∘ σ^{-1}` is meaningful only on a
chain-level-isomorphic decomposed model, not on the ambient
complex; the spectral-sequence formulation is the correct vehicle.

Pattern candidate: "E_1 overloading". `E_1` in Theorem H refers
to the spectral-sequence page (collision-depth filtration), not
to E_1-chiral input algebras. The identical symbol invites a
category error for Yangian-type inputs.
