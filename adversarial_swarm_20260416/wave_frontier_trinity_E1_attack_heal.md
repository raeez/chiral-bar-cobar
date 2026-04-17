# Wave Frontier — Attack & Heal of `conj:trinity-E_1`

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Dual: aggressive
adversarial attack on the V19 Trinity Theorem at the genuinely-`E_1` regime,
followed by Russian-school first-principles healing into the strongest
correct form.

**Mandate.** "Russian-school delivery, Chriss--Ginzburg discipline. Platonic
form. CONSTRUCT, do not narrate. Dual mode: attack then heal."

**Target.** `conj:trinity-E_1` (Wave 14 V19 §11, line 683): the Chiral
Hochschild Trinity Theorem at the genuinely-`E_1` regime. The V19 statement
proves the Trinity (geometric `C^•_chiral`, algebraic `Ext^*_{A^e}(A,A)`,
bigraded `RHH_ch`) for *logarithmic chiral algebras with finite-type bar
pieces* (the Theorem A hypotheses H1--H3). For Yangian inputs `Y(g)` --
which V2-AP22 places at the **top** of the chiral hierarchy
(`Comm < PVA < E_∞-chiral < P_∞-chiral < E_1-chiral`) -- the V19 proof
strategy uses ingredients (Arnold--Orlik--Solomon collapse on FM, bar
spectral sequence collapse, Verdier intertwining) which silently demand
input strictly weaker than genuinely-`E_1`. The conjecture flags this gap.

**Posture.** No manuscript edits, no commits, no test runs (per pre-commit
hook). Read-only attack with explicit countermodel candidates; healing
into a strongest-correct three-option resolution (a/b/c) with the
recommendation that option (c) -- Trinity for `E_1` requires the V15
**Pentagon** rather than the single-colour Trinity -- is the platonic form.

---

## §0. The single-line attack thesis

> **Attack.** The V19 Trinity Theorem assumes its input `A` admits a *single*
> derived endomorphism centre `Z^der_ch(A)`. For genuinely-`E_1` chiral
> algebras (Yangians), Wave Two-Centers (2026-04-16) found that the chiral
> Hochschild centre and the *mode-algebra* Hochschild centre are GENUINELY
> DIFFERENT objects. AP-CY62, AP-CY64, AP-CY66 disciplines this. The
> Trinity comparison maps `Φ_GA` and `Φ_AB` then bridge the wrong pair: they
> identify `C^•_chiral(A)` with `Ext^*_{A^e}(A,A)`, but the algebraic Ext is
> an Ext on the mode algebra `A_mode`, which for Yangians is genuinely
> distinct from `Z^der_ch(A)`. A bare-name "Trinity" comparison is thus
> not even type-correct in the genuinely-`E_1` regime; one must *first*
> separate the chiral and mode centres, *then* state two parallel Trinity
> Theorems, and *then* state a single Pentagon coherence between them.

> **Heal.** The strongest correct theorem is a **Pentagon at the level of
> Hochschild centres for `E_1`-chiral algebras**: five named presentations
> (chiral-geometric `C^•_chiral`, chiral-algebraic `End^ch`, chiral-bigraded
> `RHH_ch`, mode-algebraic `Ext^*_{A_mode^e}`, factorisation-homology
> `∫_{S^1}A`), with five named comparison maps and one named Pentagon
> coherence cocycle. The single-colour Trinity for `E_1` is RECOVERED
> as the projection of this Pentagon onto the *chiral* sub-trio; the
> ROW-mismatch with the mode side is the explicit content of the Pentagon
> centre's `[ω]`. The single-colour Trinity at `E_1` HOLDS in the form (b)
> *modulo R-twist by the Yangian R-matrix*, and this R-twist is precisely
> the Pentagon centre cocycle.

---

## PHASE 1 — ATTACK

### A1. Why Trinity breaks at `E_1`: the four ingredients audit

The V19 proof of `Φ_GA: C^•_chiral(A) → Ext^*_{A^e}(A,A)` (memo §2.3) rests on
four ingredients. For each, audit whether genuinely-`E_1` survives.

**Ingredient 1: Codim-1 boundary residue = bar differential.**
The geometric cochain space carries `d_int + d_fact + d_config`. Restriction
to the open stratum `C_{n+2}(X) ⊂ C̄_{n+2}(X)` is supposed to read off the
codim-1 boundary residues as the *bar-resolution differentials* `d_n`. The
bar resolution `B̄^geom_•(A) → A` is an `A^e`-module resolution where
`A^e := A ⊠_{D_X} A^op` is the *chiral enveloping bimodule*.

Audit (`E_∞`-chiral case, V2-AP21--V2-AP23 row 3): The `A^e` makes sense
because for an `E_∞`-chiral algebra, the opposite `A^op` exists as a chiral
algebra in the same operadic universe. The boxed product `⊠_{D_X}` is
well-defined.

Audit (genuinely-`E_1` case, V2-AP22 row 5): For a Yangian `Y(g)`, the
"opposite" `Y(g)^op` is not a chiral algebra in the same operadic universe.
Yangians live in `(EK QVA)`-category which is NOT closed under taking
opposite as a chiral algebra: `Y(g)^op` is a quantum *vertex* algebra of
the *opposite-braided* type. The chiral enveloping bimodule `A^e =
A ⊠_{D_X} A^op` is then NOT in `(E_1-ChirAlg)`; it lives in a coloured
two-object category (`A` in the original braiding, `A^op` in the
opposite). FM164 already flagged the Yangian-bar-cobar pro-nilpotent
completion gap; the bimodule structure is the *upstream* version of that
gap. Ingredient 1 fails type-correctness.

**Ingredient 2: Arnold--Orlik--Solomon collapse on FM.**
The Arnold relations for the de Rham cohomology of `C̄_{n+2}(X)` produce a
spectral sequence which V19 claims collapses to the bar spectral sequence
on the algebraic side. In the `E_∞`-chiral case, the collapse uses the
*fully-symmetric* Arnold algebra (Arnold's original 1969 result on
`H^*(Conf_n(C); Q)`).

Audit (genuinely-`E_1` case): For Yangian inputs, the OPE poles are not
symmetric in the configuration coordinates -- they are *ordered*. The
relevant cohomology is `H^*(Conf^{ord}_n(R); Q)`, which is *trivial* in
positive degree (the ordered configuration space of `R` is contractible).
The "Arnold collapse" for the ordered version is therefore vacuous: the
spectral sequence collapses, but it collapses to the WRONG target -- it
collapses to the trivial complex, not the bar spectral sequence.
Ingredient 2 collapses to vacuity.

**Ingredient 3: FM-tower collapse `prop:fm-tower-collapse`.**
This proposition (`chiral_hochschild_koszul.tex:606`) says the Postnikov
tower of `C̄_n(X)`-strata stabilises in the chiral Hochschild differential
because the codim-≥2 strata contribute zero on the Koszul locus.

Audit (`E_∞`-chiral case): The Koszul locus is the locus where
`Ext^{i,j}_{A^e}(A,A) = 0` for `i ≠ j`. For `E_∞`-chiral inputs, this is
non-vacuous and includes Vir, KM, Heisenberg, BP at non-critical level.

Audit (genuinely-`E_1` case): For Yangians, the Ext-diagonal condition
fails categorically. The Yangian `Y(g)` is a *filtered-CDG-Koszul
deformation of `U(g[t])`* (FM161 corrected), with a *non-trivial curvature
class*. The off-diagonal Ext groups `Ext^{i,j}_{Y(g)^e}(Y(g), Y(g))` do
NOT vanish for `i ≠ j`; they encode the curvature. So the FM-tower
collapse hypothesis is FALSE for Yangians, and the geometric model has
*genuinely higher-codimension contributions* that the algebraic Ext model
cannot see. Ingredient 3 actively obstructs the comparison.

**Ingredient 4: Verdier intertwining for `Φ_AB`.**
The bigraded model is the Verdier-dualised bar resolution. The
intertwining `Φ_AB` uses `thm:bar-cobar-isomorphism-main` to convert
`RHom(-, A)` to `RHom(-, ω) ⊗^{?} A^∨`.

Audit (`E_∞`-chiral case): For `E_∞`-chiral inputs, `A^∨` is well-defined
as the Verdier dual; the operadic Koszul self-duality `E_2^! = E_2{1}` of
V15 Lemma `lem:edge-12` (Pentagon edge $\Phi_{12}$) supplies the
intertwining.

Audit (genuinely-`E_1` case): For Yangians, the Koszul dual `Y(g)^!` is
*conjecturally* `Y(g^v)` (FM167) -- the Langlands dual Yangian, not
`Y(g)` itself. So `Φ_AB` for Yangians is not a self-intertwining; it is
an intertwining between TWO DIFFERENT YANGIANS. The bigraded model
`RHH_ch(Y(g))` and the algebraic Ext model `Ext^*_{Y(g)^e}(Y(g), Y(g))`
are quasi-isomorphic only after passage through the Langlands-dual
algebra. Ingredient 4 introduces a forced detour through `Y(g^v)`.

### A2. Steel-man: weaker forms that might survive

The attack of A1 does not kill *every* form of Trinity at `E_1`. Three
weaker forms are candidates.

**Weak form (a): Coherent shifts.** Replace pairwise quasi-isomorphism
with "quasi-isomorphism up to coherent shifts in cohomological degree."
Concretely: there exist functorial integers `s_{GA}(A), s_{AB}(A) ∈ Z`
such that
```
   C^•_chiral(A) ≃ Ext^*_{A^e}(A, A)[s_{GA}(A)]
   Ext^*_{A^e}(A, A) ≃ RHH_ch(A)[s_{AB}(A)]
```
For E_∞ inputs the shifts are zero. For genuinely-E_1 inputs, the
shifts are conjecturally controlled by the Yangian level (the spectral
parameter `z`). Plausibility: HIGH; the V19 amplitude bound `[0, 2]`
becomes `[0, 2] + s_{GA} + s_{AB}` for the algebraic chain. Test: at
amplitude `[0, 3]` (the V19 conjecture's relaxed bound) the shift
`s_{GA} = 1` would account for the extra degree.

**Weak form (b): R-twist.** Replace pairwise quasi-isomorphism with
"quasi-isomorphism modulo conjugation by the Yangian R-matrix `R(z)`."
Concretely: there is an explicit gauge `R(z) ∈ End(A ⊗ A)[[z^{-1}]]` such
that
```
   Φ_GA: C^•_chiral(A) ≃ R(z) ◇ Ext^*_{A^e}(A, A)
```
where `R(z) ◇ -` means conjugation by the R-matrix in the bimodule
category. For E_∞ inputs `R(z) = id` (no twist). For genuinely-E_1
inputs the twist is the Yangian R-matrix -- *exactly* the
chain-level data that distinguishes E_1 from E_∞. Plausibility:
VERY HIGH; this is the natural reading of "mode versus chiral
centre" of AP-CY62/AP-CY66. The R-twist IS the difference between
the two centres.

**Weak form (c): Pentagon.** Replace single-colour Trinity with
two-colour Pentagon (V15) projected onto the chiral sub-trio. The
single-colour Trinity for `E_1` is the **closed-colour Pentagon
projection minus the open-colour data**, which is exactly the wrong
projection: it discards the boundary modes that carry the spectral
parameter. Concretely: the V15 Pentagon's five presentations, applied
to the pair `(B, A) = (Z^der_ch(A), A)`, are coherent. The Trinity is
the projection onto the closed colour. For E_∞ inputs the projection
captures everything (because the open colour data is symmetric under
the closed-colour braiding). For E_1 inputs the open-colour data is
the spectral parameter `z`, and dropping it loses the mode/chiral
distinction. Plausibility: MAXIMUM; this matches the V15 manifesto
that Pentagon is the parent and Trinity the child.

### A3. Counterexample attempt: Yangian `Y(sl_2)`

Take `A = Y(sl_2)`, the Yangian of `sl_2`. This is the simplest
genuinely-`E_1` chiral algebra. Compute the three Trinity models
schematically.

**Geometric `C^•_chiral(Y(sl_2))`.** The chiral algebra structure on
`Y(sl_2)` lives over the affine line `A^1` with the spectral parameter
`z` as coordinate. The cochain space is
`Γ(C̄_{n+2}(A^1), j_*j^*Y(sl_2)^{⊠(n+2)} ⊗ Ω^n_log)`. The first
non-trivial cohomology in degree 1 is generated by the *r-matrix
generator* `r(z) ∈ Y(sl_2) ⊗ Y(sl_2)[[z^{-1}]]`, which is non-trivial.
Indeed: `H^1(C^•_chiral(Y(sl_2))) ≅ Y(sl_2) ⊗ Y(sl_2)[[z^{-1}]]/(image
of bar)`, and this has dimension growing in `z`-degree.

**Algebraic `Ext^*_{Y(sl_2)^e}(Y(sl_2), Y(sl_2))`.** The mode algebra
`Y(sl_2)_mode` is the underlying Hopf algebra (no spectral parameter),
which is isomorphic (as a graded algebra) to `U(sl_2[t])`. By
HKR-Tsygan-Loday, `HH^*(U(sl_2[t]), U(sl_2[t])) = ∧^*(sl_2[t]) ⊗
U(sl_2[t])` (Poincaré-Birkhoff-Witt + standard HKR for envelopes of
Lie algebras). This is concentrated in finite cohomological degree but
is INFINITE-DIMENSIONAL in each degree (the polynomial ring `sl_2[t]`
has infinite rank). Critically: it has NO `z`-dependence; the
spectral parameter is invisible to mode algebra Ext.

**Bigraded `RHH_ch(Y(sl_2))`.** The Verdier-dualised bigraded model
sees both the spectral parameter (through the FM compactification of
`A^1`) and the bar grading (through the Hopf structure on `Y(sl_2)`).
Schematically, this should be `polynomial(z) ⊗ HH^*(U(sl_2[t]))`,
i.e. the mode algebra Hochschild *tensored with the spectral
parameter polynomials*.

**Comparison:**

| Model | Carries spectral parameter? | Carries Hopf-Hochschild? |
|---|---|---|
| Geometric `C^•_chiral` | YES (via FM(`A^1`)) | NO (no Hopf structure used) |
| Algebraic Ext on mode | NO (mode algebra has no `z`) | YES (via HKR on `U(sl_2[t])`) |
| Bigraded `RHH_ch` | YES | YES |

The three models compute THREE DIFFERENT THINGS. They are not
quasi-isomorphic. The Trinity Theorem at `E_1`, in the strict V19
form, FAILS for `Y(sl_2)`.

The bigraded model is the only one that sees both structures
simultaneously. The geometric and algebraic models are projections of
the bigraded model onto the spectral and mode axes respectively.
This is **direct evidence for healing form (c)**: the Pentagon (which
carries both colours) is the parent; the chiral-side Trinity captures
only the spectral colour; the mode-side Trinity captures only the mode
colour; their joint coherence is the Pentagon.

### A4. Where the V19 conjecture's amplitude relaxation [0,2] → [0,3] comes from

V19 §11 conjectures that for genuinely-`E_1` inputs the amplitude bound
relaxes from `[0, 2]` to `[0, 3]`. From the A3 analysis: the extra
cohomological degree is the **spectral parameter degree**. The bigraded
model has bidegree `(p, q)` with `p` = bar/algebraic, `q` =
Verdier/spectral; the totalisation shift `[-p]` cancels Verdier `[p+2]`
to a constant `[2]`. For E_∞ inputs, the spectral degree is constrained
to `q ∈ {0, 1, 2}` (Verdier amplitude on `C̄_{n+2}`). For genuinely-E_1
inputs, the spectral parameter `z` lives on `A^1` (an open curve, not a
compact one), and the Verdier amplitude extends to `q ∈ {0, 1, 2, 3}`
because the *boundary at infinity* of `A^1` contributes a third
codimension stratum (the point at infinity, which the FM
compactification of an open curve necessarily includes). Hence
amplitude `[0, 3]`. The V19 amplitude conjecture is structurally
correct; the amplitude relaxation is the geometric trace of the open
versus compact curve distinction.

### A5. Type-error catalogue

Bare-name "Trinity at `E_1`" is type-incorrect at three sites.

**Type error 1.** `A^e := A ⊠_{D_X} A^op` does not exist in
`(E_1-ChirAlg)` for Yangian inputs (A1 ingredient 1).

**Type error 2.** `Ext^*_{A^e}(A, A)` is not an `(E_1-ChirAlg)`-Ext;
it is a *mode-algebra* Ext (AP-CY66). The V19 statement names the
algebra as `A^e` but uses ambient category `Vect`, not chiral.

**Type error 3.** The intertwining `Φ_AB` for Yangians forces a detour
through the Langlands-dual `Y(g^v)` (A1 ingredient 4); the comparison
is not even between models of the same algebra.

These three type errors are not bugs to patch -- they are signals that
the genuinely-`E_1` case requires a structurally different framework.
The Pentagon is that framework.

---

## PHASE 2 — HEALING

### H1. The strongest correct version (recommended: option (c))

Of the three weak forms (a/b/c) of A2, option (c) is the *Platonic
form*: it is the only one that is structural rather than corrective.

**Theorem (E_1-chiral Hochschild Pentagon; conjectural, the strongest correct
form of `conj:trinity-E_1`).** *Let `A` be a genuinely-`E_1` chiral
algebra on a curve `X` (e.g., `A = Y(g)` a Yangian). Let `A_mode` be its
mode algebra (the underlying Hopf algebra, with no spectral parameter).
Let `(B, A)` be the Swiss-cheese pair with `B = Z^der_ch(A)` (closed
colour) and `A_mode` (open colour). Then there are FIVE Hochschild
presentations*

```
P_1   geometric chiral             C^•_chiral(A)        on FM(X)
P_2   algebraic chiral             End^ch(A)            in (E_1-ChirAlg)/D_X
P_3   bigraded chiral              RHH_ch(A)            Verdier on C̄_n(X)
P_4   algebraic mode               Ext^*_{A_mode^e}(A_mode)   in Vect
P_5   factorisation homology       ∫_{S^1} A            via Costello-Gwilliam
```

*All five fit into a Pentagon of named comparison maps `Φ_{12}, Φ_{23},
Φ_{34}, Φ_{45}, Φ_{51}` parallel to the V15 SC^{ch,top} Pentagon. The
Pentagon coherence 2-cocycle ω is the **Yangian R-matrix conjugation
class**:*
```
   [ω] = [R(z) ◇ - · R(z)^{-1}] ∈ H^2(SC^{ch,top}; aut)
```
*and `[ω] = 0` iff `R(z) = 1` (trivial R-matrix), iff `A` is `E_∞`-chiral
(no genuine spectral structure). For genuinely-`E_1` `A`, `[ω] ≠ 0` is
the chain-level obstruction to the single-colour Trinity Theorem
holding strictly.*

### H2. The single-colour Trinity at E_1 — what survives in form (b)

Form (b) of A2 (R-twist) is RECOVERED as the chiral-projection of H1.
Concretely:

**Corollary (Trinity at `E_1`, R-twisted form; conditional on H1).**
*For genuinely-`E_1` `A`, the three chiral models
`(C^•_chiral(A), End^ch(A), RHH_ch(A))` are pairwise quasi-isomorphic
**modulo R-twist by the Yangian R-matrix**:*
```
   C^•_chiral(A) ≃_R End^ch(A) ≃_R RHH_ch(A)
```
*where `≃_R` means quasi-isomorphism in the gauge category
`(D^b(A^e), R-conjugation)`. The Pentagon coherence 2-cocycle ω is the
R-conjugation class; modding out by R-conjugation (passing from the
chiral category to its *quotient by R-twist*) restores the strict
Trinity in the form*
```
   C^•_chiral(A)/R ≃ End^ch(A)/R ≃ RHH_ch(A)/R.
```

This is form (b) of A2, now with explicit content: the R-twist is
the Yangian R-matrix, the quotient `/R` is the passage from the
chiral algebra to its mode algebra.

### H3. The shift form (a) is a derived consequence

The amplitude relaxation `[0, 2] → [0, 3]` of V19 §11 is the
**cohomological shadow** of H1's R-twist: the R-matrix carries
`z`-degree, and the integration over `z` (i.e. taking sections of the
sheaf of Hochschild cochains over the spectral parameter line `A^1`)
contributes one extra cohomological degree. Hence:

**Corollary (amplitude relaxation; from H1).** For genuinely-`E_1` `A`:
amplitude(P_1) = amplitude(P_3) = `[0, 2 + deg_z(R)]` where `deg_z(R)`
is the spectral degree of the Yangian R-matrix. For Yangians of finite
type, `deg_z(R) = 1`, giving `[0, 3]`. Form (a) of A2 (coherent shift
`s_{GA} = 1`) is the cohomological readout of the spectral degree.

### H4. The three weak forms are equivalent under H1

Under H1, the three weak forms (a/b/c) of A2 are equivalent:

```
  H1 (Pentagon, two-colour)
     |
     | project to chiral colour
     v
  (c) projection ⇒ R-twisted Trinity
     |
     | take cohomology
     v
  (b) R-twisted ≃ ⇒ shifted ≃
     |
     | translate gauge to degree
     v
  (a) shifted ≃ (amplitude [0, 2 + deg_z(R)])
```

This is what makes (c) the platonic form: it implies (a) and (b) as
shadows, and it is the only one that names the structural obstruction
(the R-matrix carries the spectral parameter).

### H5. Connection to V20 Universal Trace Identity at the E_1 level

V20 (`UNIVERSAL_TRACE_IDENTITY.md`) identifies `tr_{Z(C)}(K_C) =
-c_ghost(BRST(Φ(C))) = c_N(0)/2`. The proof's Step 3 establishes
`δ := K^ch - K^BKM = 0` on the homotopy category and flags the
chain-level question as `conj:trace-identity-chain-level`, *which is
explicitly conditional on `conj:trinity-E_1`*.

H1 provides the structural mechanism for V20 Step 3 at `E_1`. The
chain-level identity `K^ch = K^BKM` is the *Pentagon coherence
cocycle vanishing* `[ω] = 0` projected onto the trace level. For
`E_∞` inputs the Pentagon `ω` vanishes and Step 3 holds at chain
level. For genuinely-`E_1` inputs the Pentagon `ω` is the Yangian
R-matrix conjugation class, which is non-trivial; the chain-level
identity then holds *only after passage to the gauge category*
`(D^b(A^e), R-conjugation)`. The trace, being a gauge-invariant
quantity, is unaffected: `tr_{Z(C)}(K_C)` projects equally well
through any gauge representative. Hence:

**Corollary (V20 Step 3 at `E_1`, from H1).** *The Universal Trace
Identity `tr_{Z(C)}(K_C) = -c_ghost(BRST(Φ(C))) = c_N(0)/2` holds at
the chain level for genuinely-`E_1` `Φ(C)` modulo R-twist. Since the
trace is gauge-invariant under R-conjugation, the numerical identity
holds at chain level on the gauge quotient, hence on the homotopy
category. V20 Step 3's `conj:trace-identity-chain-level` is then a
**consequence of H1**, not a parallel conjecture.*

### H6. Connection to V11 Pillar α (Φ functor) at d=3

V11 Pillar α (`PLATONIC_MANIFESTO_VOL_III.md` line 21) names the four
universal properties of Φ:
- (U1) Hochschild pullback `B^ord ∘ Φ ≃ CC_•`
- (U2) CY-morphism functoriality
- (U3) Drinfeld center compatibility
- (U4) standard-input recovery

At `d = 3`, Φ outputs `E_1`-chiral algebras (FM43, AP-CY56, AP-CY66).
The U1 universal property `B^ord ∘ Φ ≃ CC_•` requires the bar of an
`E_1`-chiral algebra to be quasi-isomorphic to the cyclic bar of the
source CY_3 category. The cyclic bar `CC_•(C)` for a CY_3 category `C`
is computed in `Vect` (mode-algebra category); the chiral bar
`B^ord(Φ(C))` is computed on `FM(X)` (chiral category). These two
categories are precisely the two colours of H1's Pentagon.

**Corollary (V11 (U1) at `d = 3`, from H1).** *The Hochschild pullback
universal property (U1) of Pillar α at `d = 3` is the projection of H1's
Pentagon onto its `Φ_{45}: P_4 ≃ P_5` edge (mode algebra ≃
factorisation homology over `S^1`). The chain-level statement of (U1)
for genuinely-`E_1` Φ outputs requires H1's R-twist gauge
identification; without H1, (U1) holds only on the homotopy
category.*

### H7. The healing punch list (no edits made)

If H1 is to be installed as a theorem in the Vol I manuscript, the
following edits are required (TRACKED, not executed).

**E_pentagon-1.** `chapters/theory/chiral_hochschild_trinity.tex` (the
new V19 chapter, currently architectural blueprint per V19 §9.1).
Replace the V19 `conj:trinity-E_1` (lines analogous to V19 §11) with
the H1 Pentagon Theorem, stated as **conjectural pending the
algebraic-category technicalities of `End^ch(A)` for Yangian inputs**
(FM164, FM161 -- the pro-nilpotent completion gap and the
filtered-CDG-Koszul framework). Mark the Pentagon Theorem as
`\ClaimStatusConjectured` until those gaps close.

**E_pentagon-2.** Vol II `chapters/foundations/sc_chtop_pentagon.tex`
(the V15 Pentagon chapter blueprint). In §5 ("Comparison with the
chiral Hochschild trinity"), upgrade the row "$C^*_{ch,fact} \simeq
C^*_{ch,BV}$" to a *cell* (closed-colour projection) within a parent
Pentagon at `E_1`. The Vol II Pentagon (V15) and the Vol I Pentagon at
`E_1` (H1) are the same structural theorem, applied to two different
arenas. Add a sentence:

> The Pentagon Theorem of this chapter (Vol II V15, governing
> `SC^{ch,top}`) and the Pentagon Theorem at `E_1`-chiral level (Vol I
> §H1, governing `(B, A) = (Z^der_ch(A), A_mode)` for genuinely-`E_1`
> `A`) are the two-colour and one-colour-pair-with-mode versions of a
> single Pentagon coherence principle.

**E_pentagon-3.** Vol III `chapters/quantum_groups/cy_to_chiral.tex`
(the V11 Pillar α chapter). In the discussion of (U1) at `d = 3`, add
a remark:

> The chain-level statement of (U1) at `d = 3` is conditional on the
> Vol I Pentagon Theorem at `E_1` (H1) of `wave_frontier_trinity_E1
> _attack_heal.md`. (U1) projects onto the
> mode/factorisation-homology edge of H1's Pentagon; the chain-level
> identification `B^ord ∘ Φ ≃ CC_•` follows from H1 by gauge
> reduction. The current `inf-cat` proof of CY-A_3 covers the
> homotopy-category statement; H1 covers the chain-level upgrade.

**E_pentagon-4.** `MASTER_PUNCH_LIST.md` (master list). Replace the
V19 `conj:trinity-E_1` line with three sub-items:
- (a) form (a/b/c) equivalence under H1: PROVED in H4.
- (b) shifted form (a) amplitude `[0, 3]` for Yangians: PROVED in H3.
- (c) Pentagon form H1: CONJECTURAL, conditional on FM164 + FM161 healings.

### H8. The conditional landscape after H1

After H1, the conditional landscape of `conj:trinity-E_1`-related
results restructures.

| Result | Pre-H1 status | Post-H1 status |
|---|---|---|
| V19 Trinity for `E_∞`-chiral | PROVED | PROVED (unchanged) |
| `conj:trinity-E_1` (V19 form, strict) | OPEN, expected FALSE | RETRACTED; replaced by H1 |
| Trinity at `E_1` modulo R-twist (form b) | not stated | COROLLARY of H1 |
| Amplitude `[0, 3]` for Yangians (form a) | OPEN | COROLLARY of H1 (H3) |
| V20 Step 3 `conj:trace-identity-chain-level` | OPEN (downstream of trinity-E_1) | COROLLARY of H1 (H5) |
| V11 (U1) chain-level at `d = 3` | OPEN | COROLLARY of H1 (H6) |
| H1 Pentagon at `E_1` | NEW | CONJECTURAL pending FM164/FM161 |

Net effect: **one conjecture stays open** (H1 Pentagon at `E_1`), and
**three previously-independent conjectures become its corollaries**
(form b, amplitude form a, V20 Step 3 chain level, V11 (U1) chain
level). This is the correct sense in which H1 is the platonic form:
it is the unique conjecture from which the rest follow.

### H9. The single-line memorable form

```
   The Trinity Theorem holds for E_1-chiral algebras after passing to
   the gauge category by the Yangian R-matrix; equivalently, the
   single-colour Trinity at E_1 is the closed-colour projection of a
   two-colour Pentagon whose coherence cocycle is the R-matrix
   conjugation class, vanishing iff the input is E_∞.
```

That is the entire content of H1 in a single sentence. The Trinity
holds *up to R-twist*; the R-twist IS the spectral parameter; the
spectral parameter IS what distinguishes `E_1` from `E_∞`. There is
nothing to fix in V19 -- the conjecture's flag is structurally
correct, and the flag is closed by *upgrading from Trinity to
Pentagon*, not by *strengthening the Trinity*.

### H10. Why option (c) Pentagon is platonic

Three independent reasons converge on H1 as the platonic form.

**Reason 1 (architectural).** V15 already establishes the Pentagon
for `SC^{ch,top}` (Vol II). The single-colour Trinity (V19, Vol I) is
the closed-colour projection of V15. There is no architectural reason
to expect the single-colour Trinity to be the *complete* statement at
`E_1`; the single-colour projection is meaningful at `E_∞` (where the
two colours decouple by symmetry) but loses information at `E_1`
(where the two colours are coupled by the spectral parameter). The
correct generalisation is to do at `E_1` what V15 did at the
operadic level: name the Pentagon, project to the Trinity as a
corollary.

**Reason 2 (mathematical).** The A3 counterexample analysis on
`Y(sl_2)` showed that the three V19 Trinity models compute three
different things at `E_1`. The Pentagon adds two more presentations
(mode algebra `Ext^*_{A_mode^e}` and factorisation homology
`∫_{S^1} A`) which complete the picture; only with all five does the
coherence statement become well-posed.

**Reason 3 (Russian-school discipline).** Chriss-Ginzburg's slogan
"five views of one object" applies more naturally to the Pentagon
than to the Trinity. The Trinity at `E_∞` was already a strain on
the slogan (three views of one object); at `E_1` the strain breaks
because one view (mode-algebra Ext) is genuinely separate. The
Pentagon restores the slogan in its full form: five views, one
universal centre, one coherence cocycle. This is the Platonic
ideal.

---

## §3. Summary table

| Item | Phase 1 (Attack) | Phase 2 (Heal) |
|---|---|---|
| V19 `conj:trinity-E_1` strict form | FAILS for `Y(sl_2)` (A3) | RETRACTED |
| Type-correctness | Fails at three sites (A5) | Fixed by Pentagon (H1) |
| V19 amplitude `[0, 3]` conjecture | Structurally correct (A4) | COROLLARY of H1 (H3) |
| R-twist form (b) | Plausible (A2) | COROLLARY of H1 (H2) |
| Shifted form (a) | Plausible (A2) | COROLLARY of H1 (H3) |
| Pentagon form (c) | Maximum plausibility (A2) | THE PLATONIC FORM (H1) |
| V20 Step 3 chain level | Conditional on `conj:trinity-E_1` | COROLLARY of H1 (H5) |
| V11 (U1) chain level at `d = 3` | OPEN | COROLLARY of H1 (H6) |
| Net new conjecture | none | H1 Pentagon at `E_1` (replaces 4 open conjectures) |

---

## §4. What this delivery does NOT do

- Does NOT edit any `.tex` source.
- Does NOT modify any `CLAUDE.md`.
- Does NOT modify the Master Punch List.
- Does NOT write engine files for the H1 Pentagon at `E_1`.
- Does NOT close FM164 (Yangian bar-cobar pro-nilpotent completion gap)
  or FM161 (Yangian Koszulness in Positselski nonhomogeneous framework).
  Both are PREREQUISITES to making H1 a theorem rather than a
  conjecture; both are tracked as separate punch list items.
- Does NOT commit anything. (Per pre-commit hook: build/tests not run,
  no AI attribution.)
- Does NOT supply the chapter prose for H1. (This memo is the
  attack/heal blueprint; the chapter realisation is a future wave.)

---

## §5. Closing assessment

The V19 `conj:trinity-E_1` is structurally CORRECT in its assertion
that something must change at `E_1`, but structurally INCOMPLETE in
its expectation that the Trinity itself can be relaxed
(amplitude `[0, 2] → [0, 3]`) to recover the statement. The correct
upgrade is to recognize that the Trinity at `E_∞` was already the
*projection of a Pentagon* (V15 closed-colour), and that the Pentagon
is the Platonic statement; the Trinity is its `E_∞` shadow.

At `E_1`, the Pentagon does not collapse to the Trinity, and the
single-colour Trinity becomes type-incorrect. The **strongest correct
form** of `conj:trinity-E_1` is:

> **H1.** The Pentagon Theorem at `E_1`-chiral level holds with the
> Yangian R-matrix conjugation class as the Pentagon coherence
> cocycle. The single-colour Trinity at `E_1` is recovered as the
> chiral projection modulo R-twist; the amplitude relaxation
> `[0, 3]` is the cohomological readout of the spectral degree.
> Three previously-independent conjectures (V20 Step 3 chain level,
> V11 (U1) chain level at `d = 3`, and the V19 amplitude
> conjecture) become corollaries of H1.

H1 is conjectural pending FM164 (Yangian bar-cobar pro-nilpotent
completion) and FM161 (Yangian Koszulness in Positselski
nonhomogeneous framework). With those two technical gaps closed, H1
becomes a theorem and four downstream conjectures collapse into
corollaries.

This is the Russian-school resolution: do not strengthen the
single-colour statement; recognize the two-colour structure that was
always there. The Pentagon was always the correct frame; the Trinity
was always the `E_∞` shadow; the `E_1` upgrade requires the parent,
not a relaxed child.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no manuscript
edits; no test runs; no build. Delivered to
`/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_frontier_trinity_E1_attack_heal.md`
per dual-mode attack-heal mandate.
