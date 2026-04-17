# Wave 3 — Chiral Chern–Weil & Level/r-Matrix Hygiene
## Adversarial referee report
Targets: `chiral_chern_weil.tex` (1960 ll.), `virasoro_r_matrix.tex` (395 ll.),
`three_parameter_hbar.tex` (459 ll.), `holographic_datum.tex` (1373 ll.),
`w3_holographic_datum.tex` (574 ll.), `garland_lepowsky.tex` (1401 ll.).
Anti-patterns under attack: AP126, AP141, AP136, AP39, AP151, AP-CY55, AP155.

------------------------------------------------------------------------

## Section 1 — r-matrix level audit table

Format: file:line — formula written — level prefix? — k=0 vanishing? — convention — verdict.

### chiral_chern_weil.tex
| line | formula | level? | k=0=>r=0? | conv | verdict |
|------|---------|--------|-----------|------|---------|
| 146 | `r(z)=k Ω/z` (intro, KM) | YES (k) | YES | trace | OK |
| 415 | `r^Heis(z)=k/z` boxed | YES (k) | YES | trace | OK |
| 429 | `r^Vir(z)=(c/2)/z^3 + 2T/z + ∂T` | n/a (Vir) | trivially (c=0) | — | OK but contains NON-VACUUM `∂T` term that is dropped from "vacuum leading" table on L1198 (silent inconsistency, see §3) |
| 449 | `r^KM(z)=k Ω/z` boxed (trace-form) | YES | YES | trace | OK |
| 455 | `r^KZ(z)=Ω/((k+h^v)z)` | implicit | NO at k=0 | KZ | OK *but* prose says "Lie bracket persists" — see §3.A |
| 458 | "bridge identity: `k Ω_tr = Ω/(k+h^v)` at generic k" | — | — | — | **WRONG IDENTITY** (see §3.A); fails dimensional check, fails k=0 limit |
| 762 | `r(z)=k Ω/z` (sl_2 expl) | YES | YES | trace | OK |
| 840 | `r(z)=k Ω/z` (sl_3 expl) | YES | YES | trace | OK |
| 1049 | `r(z)=k Ω/z` (KM derivation) | YES | YES | trace | OK |
| 1199 | summary table `V_k(g): k Ω/z` | YES | YES | trace | OK |

### virasoro_r_matrix.tex
| line | formula | level? | k=0=>r=0? | conv | verdict |
|------|---------|--------|-----------|------|---------|
| 116 | `r^coll(z)=(c/2)/z^3 + 2T/z` | c | c=0=>r=0 only on vacuum sector | — | OK (the `∂T` term is asserted absorbed; see §3.B for the absorption claim) |
| 310 | "Heisenberg: `r(z)=k/z`" | YES | YES | trace | OK |
| 318 | "KM: `r(z)=Ω/((k+h^v)z)` on adjoint sector" | implicit | NO | KZ | **AP151 CONVENTION CLASH** with `chiral_chern_weil.tex` whose KM box is `k Ω/z` (trace) |
| 320 | "R(z)=z^{Ω/(k+h^v)}" (Example 5.2, "class L") | KZ | NO at k=0 | KZ | At k=0 (still finite) the exponent is `Ω/h^v` — check OK (no k vanishing required because KZ-normalized r just needs to remain finite), but presentation as `R(z)=z^k` for Heisenberg vs `R(z)=z^{Ω/(k+h^v)}` for KM mixes conventions inside one comparison table (L342–346). |

### three_parameter_hbar.tex
| line | formula | level? | k=0=>r=0? | conv | verdict |
|------|---------|--------|-----------|------|---------|
| 107 | `r(z)=Ω/((k+h^v)z)` (KM master formula) | implicit | **NO** at k=0 (gives Ω/h^v) | KZ | OK *as KZ formula*, but **AP151** with the trace-form `k Ω/z` used in chiral_chern_weil.tex |
| 134 | `R(z;ℏ)=1+ℏ r(z)+O(ℏ^2)` | — | — | — | OK structural; relies on r |
| 164 | `r(z)=Ω/((k+h^v)z)` | implicit | NO | KZ | propagation of L107 |
| 172 | `κ_cl = av(r(z)) = k dim(g)/(2 h^v)` | yes | YES | hybrid | **NOT dimensionally consistent with L172's r**: averaging the KZ r-matrix `Ω/((k+h^v)z)` cannot produce `k dim(g)/(2 h^v)` because the trace gives `dim(g)/(k+h^v)`, NOT `k dim(g)/(2 h^v)`. The κ formula on L173 is the **trace-form averaging**; the displayed r on L107/164 is the **KZ form**. They are inconsistent. (See §4.A.) |
| 210 | `r_{KZ}(z)=(1/(k+h^v))·Ω/z` | implicit | NO | KZ | also contains a stray `}` (visible LaTeX bug `divided-power convention} = ...`, L210) |
| 241 | `r(z)=ℏ Ω/z` | by construction | YES | hybrid | OK |
| 286 | `r(z)=Ω/((k+h^v)z)` | implicit | NO | KZ | propagation |
| 302 | `r(z) = (k/(k+h^v))·Ω/z + (1/(k+h^v))·[structure constants]` | hybrid | k=0 piece kills first term | hybrid | **algebraically wrong on its face**: the structure-constant part should not carry the level-shift prefactor independently. The simple-pole `f^{ab}_c J^c/(z-w)` has NO `k` dependence; dividing it by `(k+h^v)` is a step that requires Sugawara renormalization, which is not derived here. (See §4.B.) |
| 345 | `R(z;ℏ)=1+ℏ Ω/z + O(ℏ^2)` | by construction | YES | hybrid | OK |

### holographic_datum.tex
| line | formula | level? | k=0=>r=0? | conv | verdict |
|------|---------|--------|-----------|------|---------|
| 194 | `r(z)=k/z` (Heis) | YES | YES | trace | OK |
| 202 | `r(z)=k Ω/z` (KM trace-form) | YES | YES | trace | OK; explicit "vanishing at k=0" is *correct* and good practice |
| 392 | `κ(V_k(g)) = av(r) + dim(g)/2 = dim(g)(k+h^v)/(2h^v)` | YES | k=0 ⇒ κ=dim(g)/2 (Sugawara) | trace | **algebraically valid** with `r=k Ω/z`: gives av(r)= k dim(g)/(2 h^v); then +dim(g)/2 reassembles to dim(g)(k+h^v)/(2h^v). Internally consistent within the trace convention. |
| 632 | `r(z)=k Ω/z` and "bridge identity" | YES | YES | trace | repeats the false bridge identity from chiral_chern_weil.tex L458 (see §3.A) |
| 670 | "spectral parameter z…residual after dlog" | — | — | — | OK narrative; consistent with three_parameter_hbar.tex L241 |
| 717 | `r_c(z) = (c/2)/z^3 + 2T/z` (Vir) | c | only at c=0 on vacuum | — | OK; same comment as `chiral_chern_weil.tex` L429 about `∂T` |
| 985 | obstruction `[R^mod_4]` "Vanishes for G,L,C; nonzero for M" | — | — | — | This is a *meta-claim* about the quartic obstruction; relies on multiple downstream theorems. Status not visible in scope of this audit. |

### w3_holographic_datum.tex
| line | formula | level? | conv | verdict |
|------|---------|--------|------|---------|
| 250 | `r_{TT}=(c/2)/z^3+2T/z` | c | — | OK (= Vir channel) |
| 252,254 | `r_{TW}=r_{WT}=3W/z` | n/a | — | OK pole-1 |
| 256 | `r_{WW}=(c/3)/z^5+2T/z^3+∂T/z^2+(3/10 ∂²T+α(c)Λ)/z` | c | — | **EVEN POLE z^{-2}** present — the bosonic-parity rule from `virasoro_r_matrix.tex` L121–124 ("only odd-order poles survive in the r-matrix" for single-generator bosonic algebras) is broken here, and the W3 paper carves out an exception in `rem:even-pole` (L289–297). Not a contradiction (W3 is multi-generator), but the global slogan "bosonic ⇒ odd poles" needs a scope tag. |

### garland_lepowsky.tex
| line | formula | level? | k=0=>r=0? | conv | verdict |
|------|---------|--------|-----------|------|---------|
| 965 | `r(z)=Ω/((k+h^v)z)` | implicit | NO | KZ | **AP151 clash** with KM trace-form `k Ω/z` used in `chiral_chern_weil.tex` |
| 1017 | `r(z)=Ω/((k+2)z)` (sl_2) | implicit | NO | KZ | propagation |
| 1081 | `r(z)=Ω_{sl_3}/((k+3)z)` | implicit | NO | KZ | propagation |
| 1317 | `r(z)=Ω/((k+h^v)z)` (concluding remark) | implicit | NO | KZ | propagation |
| 1324 | `av(r)+dim(g)/2 = κ(g_k)` | mixed | — | mixed | If r is KZ-normalized then av(r)=dim(g)/(k+h^v), and adding dim(g)/2 does NOT give the κ formula `dim(g)(k+h^v)/(2 h^v)`. The "+dim(g)/2 Sugawara" addendum **only works in the trace convention**. The Garland–Lepowsky note silently switches conventions between L965 and L1324. **AP151 + dimensional inconsistency.** |

### Headline AP126/AP141 verdict

The bare-Omega/z violation flagged in AP126/AP141 is **not** present in
`chiral_chern_weil.tex` (which is consistently trace-form throughout) or
`holographic_datum.tex` (which is also trace, with explicit "vanishing at
k=0" narrations — exemplary). It IS present, in modulated form, in:

  (a) **`three_parameter_hbar.tex`** at L107, L164, L210, L286 — these are
      *KZ-form* presentations `Ω/((k+h^v)z)`. Not literal AP126 (no missing
      level), but the document then writes `κ_cl = k dim(g)/(2 h^v)` (L173)
      which is the **trace-form averaging answer**. Internally inconsistent.
  (b) **`garland_lepowsky.tex`** at L965, L1017, L1081, L1317 — also
      KZ-form, but the proof on L1130–1147 uses `c(V_k(g))=k dim(g)/(k+h^v)`
      (a trace-convention central charge). Switching conventions is silent.
  (c) **`virasoro_r_matrix.tex`** at L318/L320 — declares "KM:
      `r(z)=Ω/((k+h^v)z)`, R(z)=z^{Ω/(k+h^v)}" while the abstract and main
      text use trace-form vocabulary throughout the rest of the file.

The "**bridge identity** `k Ω_tr = Ω/(k+h^v)`" at `chiral_chern_weil.tex`
L458 and `holographic_datum.tex` L635 is the **load-bearing FALSE
statement**. See §3.A.

------------------------------------------------------------------------

## Section 2 — Triage of major claims

### chiral_chern_weil.tex
**T1.** The averaging map `av: g^{E_1} → g^{mod}` is a surjective dg Lie
morphism (Thm 4.1, L547). **Triage: PROVED in spirit, but proof is
asserted and the kernel-description (item iii: "records R-matrix, braiding,
Yangian coherences") is *narration*, not theorem.**

**T2.** `κ(A) = ½ tr Res_{z=0} r(z)` with weight-dependent moment
(eq 4.18, L718). **Triage: holds for the four explicit families
(Heisenberg, Virasoro, KM, W_N) by direct computation. UNIVERSAL form
is not proved; the bc/βγ paragraph (L935–949) explicitly notes the
formula "applied naively" gives 0, and the actual κ comes from the
Sugawara stress-tensor sector. So the slogan-form "av of r computes
κ" is false in general — it has scope `(diagonal r-matrix nonzero)`
and the bc/βγ exception is acknowledged. Good practice.**

**T3.** `κ(W_N) = c(H_N − 1)` (eq 4.27, L1024). **Triage: PROVED
correctly; the AP136 trap is anticipated and called out in
`warn:harmonic` (L1038–1043).** This is a model AP136 fix.

**T4.** `κ(V_k(g)) = dim(g)(k+h^v)/(2 h^v)` (eq 4.50, L1129). **Triage:
PROVED via the "double-pole + Sugawara shift" decomposition. ATTACK:
the simple-pole channel computation (L1078–1098) uses
`Σ f^{ac}_d f^{bc}_d = 2 h^v (J^a, J^b)` (the Killing-form identity).
But the manuscript's own narrative inside the sl_2 proof at L780–810
admits this identity FAILS in the Chevalley basis ("sum is 5? No, 4.
Hmm, but C_2^{ad}=4"; L796–797). The hand-wave "with the correct index
placement the identity holds" (L807–809) is unsatisfactory.**

**T5.** `δ F_2(W_3) = (c+204)/(16 c)` (Section 7, multi-weight). Out of
audit scope here; depends on the W_3 channel decomposition in
`w3_holographic_datum.tex`.

### virasoro_r_matrix.tex
**T6.** `R(z) = z^{2h} exp(−c/(4z²))` on a primary of weight h
(Computation 2.1, L130). **Triage: PROVED on the primary line because
[L_0, **1**]=0; the path-ordered exponential reduces to ordinary
exponential. ATTACK: this is "R-matrix on the highest-weight vector",
NOT the full Virasoro R-matrix. Scope tag missing from abstract.**

**T7.** `S_3(Vir_c) = 2` independently of c (Theorem 3.1, L220).
**Triage: the proof (L228–243) is `S_3 := 2 κ / κ = 2`. This is a
*tautological identity*, not an independent theorem.** (See §3.D.)

**T8.** Class M membership via Δ = 8 κ S_4 = 40/(5c+22) ≠ 0 (Cor 3.2,
L245). **Triage: the discriminant formula is asserted, not derived.
The factor `5c+22` is the central charge of the W_3 W–W structure
function (denominator of α(c) in W_3, cf. `w3_holographic_datum.tex`
L261), not Vir-intrinsic. Scope error.**

**T9.** Class L for affine KM with `R(z) = z^{Ω/(k+h^v)}`
(Example 5.2, L316). **Triage: this is a *primary-line restriction*.
The full KM R-matrix is not a monomial; only its action on a fixed
weight space is.**

### three_parameter_hbar.tex
**T10.** `ℏ_KZ = ℏ_DNP = ℏ_bar = 1/(k+h^v)` (Theorem 3.1, L312).
**Triage: PROVED for KZ and DNP via citation. The bar-prefactor
proof (Prop 2.4, L290–306) is **circular**: it says
"r(z) = (k/(k+h^v)) Ω/z + (1/(k+h^v))[structure constants], which
combines to Ω/((k+h^v)z) by the definition of Ω relative to the
Killing form." This **silently uses Sugawara renormalization**
(rescaling the trace-form OPE coefficient by 1/(k+h^v)) and treats
the result as if it were derived from d-log absorption alone.
The honest derivation needs Sugawara as a hypothesis. (See §3.E.)**

**T11.** L210 contains a literal LaTeX bug: `divided-power
convention} = \lambda^n/n!`)`. The opening `\textit{` or similar is
missing; this is a typo not a math error, but it blocks compilation.
**Triage: BUILD-BREAKING typo.**

### holographic_datum.tex
**T12.** Six-component datum
`H(A) = (A, A^!, C, r(z), Θ, ∇^hol)` is *complete* (claimed
implicitly throughout, no formal completeness theorem). **Triage:
DEFINITION, not theorem. The "complete invariant" rhetoric in
Prop 6.6 (Recovery theorems, L967) lists FOUR reconstructions
(R1–R4), none of which proves completeness. Calling it "the
holographic datum" is a definitional claim; the *uniqueness up to
isomorphism* claim from §10 of the rectify task ("holographic datum
= unique up to iso for any Koszul chiral algebra") is **not**
proved here.**

**T13.** "BBL triangle commutativity" (L959, L223): cited as
"Theorem A (the Verdier intertwining at the algebra level)". **No
proof in this file.** Triage: deferred to monograph; out of
scope; flag for cross-volume consistency.

**T14.** Critical level `r(z)|_{k=-2} = -2 Ω/z (finite, trace-form)`
(L631). **Triage: in the trace convention this is just an
arithmetical fact. But the "Sugawara construction is undefined" at
critical level (L1192 of garland_lepowsky.tex) — so the *averaging
identity* `κ = av(r) + dim(g)/2` cannot be applied at k=-h^v; the
shifts disagree. The manuscript handles this correctly at k=-h^v ⇒
κ=0 by direct substitution into the closed formula, but the
*decomposition* (av(r) + dim(g)/2 = -dim(g)/2 + dim(g)/2 = 0) is
the right answer for the wrong reason: r is finite, av(r) is finite
(= -dim(g)/2 ≠ 0), and the Sugawara shift has to be
*re-interpreted* not just *added*.**

### w3_holographic_datum.tex
**T15.** `Λ_0 |h,w⟩ = (h² − 9h/5)|h,w⟩` (Prop 4.1, L309). **Triage:
PROVED by direct mode computation. Independent of c, w. Solid.**

**T16.** `δ F_2(W_3) = (c+204)/(16 c)` (claim from abstract).
**Triage: out of scope here; needs cross-channel computation;
flagged for separate audit.**

### garland_lepowsky.tex
**T17.** Critical-level structure (Prop 8.1, L1179). **Triage:
correct in items (i)–(iv) (κ=0, Feigin–Frenkel center, etc.);
item (v) `H^n(B(V_{-h^v}(g))) ≅ Ω^n(Op_{g^∨}(D))` cites Raskin and
the FLE — this is conditional on a deep theorem from outside the
manuscript. Flag for `\ClaimStatusProvedElsewhere` audit.**

------------------------------------------------------------------------

## Section 3 — Per-claim attack/defense/repair

### A. The "bridge identity" `k Ω_tr = Ω/(k+h^v)` (L458 chiral_chern_weil.tex; L635 holographic_datum.tex)

**Attack.** The identity as written is *type-wrong*: both sides are elements
of `g ⊗ g`, but the LHS scales linearly in k while the RHS is bounded as
k→∞. At k=0 the LHS is 0 while RHS is `Ω/h^v ≠ 0`; at k=−h^v the LHS is
`−h^v Ω` (finite) while RHS diverges. They cannot be equal at any value
of k, let alone "at generic k". The identity tries to express the
**relation between two different normalizations of Ω**, not between two
choices of k.

**Defense (steelman).** The author *means* "if you renormalize the OPE
coefficient by `(k+h^v)/k` (Sugawara renormalization), then a trace-form
r-matrix `k Ω/z` becomes a Sugawara-form r-matrix
`(k+h^v) Ω_{Sug}/z = Ω/z` after absorbing factors". In other words: r in
trace form *times* the Sugawara prefactor `1/(k+h^v)` *of the
ENERGY–MOMENTUM TENSOR* gives a different gauge of the *same r*. But the
identity then is between **r-matrices**, not between Casimir tensors
times scalars.

**Repair.** Replace the bridge identity by:

  "For r-matrices: `r^trace(z) = k Ω_tr/z` and
  `r^KZ(z) = Ω_KZ/((k+h^v)z)` are *the same r-matrix in two
  conventions*, related by `r^KZ = r^trace / (k+h^v)` together with
  `Ω_KZ = (k+h^v) Ω_tr`. The bare identity `k Ω_tr = Ω_KZ/(k+h^v)`
  is *false at every k* and should be removed."

### B. `r^Vir(z) = (c/2)/z^3 + 2T/z + ∂T` vs `(c/2)/z^3 + 2T/z`

`chiral_chern_weil.tex` L429 keeps the `+ ∂T` term. `virasoro_r_matrix.tex`
L116 drops it ("the simple OPE pole is absorbed entirely and contributes
nothing to the collision residue"). `holographic_datum.tex` L717 also
drops it. The summary table in `chiral_chern_weil.tex` L1198 silently
drops it.

**Attack.** The d-log absorption rule (`virasoro_r_matrix.tex` L121–123)
sends a pole of order n to a pole of order n−1, so the OPE simple pole
(order 1) becomes a "pole of order 0" — i.e., a regular term. A regular
term is NOT extracted by `Res_{z=0}`. So in fact `chiral_chern_weil.tex`
L429 is **wrong by the document's own absorption rule**: the `∂T` should
be dropped.

**Repair.** Drop the `∂T` from L429. Make the table at L1198 the canonical
form. Insert a 1-line sentence after eq. (3.20) on L432 explaining that
`∂T` is regular after d-log and contributes 0 to the residue.

### C. The Chevalley-basis Casimir computation (L780–810 chiral_chern_weil.tex)

The proof that the simple-pole Sugawara shift equals `dim(g)/2` is, for
sl_2, computed as: the contraction `Σ f^{ec}_d f^{ec}_d` should equal
`C_2^{ad} = 2h^v = 4`, but direct enumeration in Chevalley basis gives 5.
The text concludes "with the correct index placement the identity holds".

**Attack.** This is a hand-wave. The Killing form identity in **non-orthonormal** basis is
`κ_{ab} = Σ_{c,d} f^a_{cd} f^b^{cd}` with **lower–upper index pairing**.
In the Chevalley basis where `(e,f)=1, (h,h)=2, (e,e)=(f,f)=0`, the
metric is non-diagonal, and "f^{ec}_d" without raising/lowering by the
metric is not a Killing-form contraction.

**Repair.** Either (a) redo the computation in the orthonormal basis
`{e, f, h/√2}` where the identity manifestly works, or (b) write the
identity as `κ^{ae} κ^{bf} f^c_{ed} f^d_{fc} = 2h^v κ^{ab}` and verify the
Chevalley-basis numbers using the explicit metric `κ^{ef}=κ^{fe}=1,
κ^{hh}=2`. The current text neither does (a) nor (b); it asserts the
right answer and leaves a verification gap visible in the proof itself.

### D. `S_3(Vir_c) = 2` is tautological (L220 virasoro_r_matrix.tex)

The proof writes `S_3 := T_{(1)}T_lin / T_{(3)}T_const = 2T/(c/2) = ?`,
then re-writes the numerator/denominator as `2κ/κ = 2`.

**Attack.** The substitution `T_{(1)}T_lin = 2T → 2 κ` (a c-number) is
*using* the κ formula κ=c/2 to **replace a field-valued operator by a
scalar**. This is not a derivation of `S_3 = 2`; it's a definition of S_3
as the ratio that **a posteriori** equals 2 because the numerator was
chosen to be twice the central term. The identity is
`(2T_{(1)}T)_const / T_{(3)}T_const = 2`, which is a tautology.

**Defense (steelman).** What's actually true: the Vir OPE has **specific
modes** `T_{(3)}T = c/2 · 1` and `T_{(1)}T = 2 T`, and **on a primary
state** `2 T_0 |h⟩ = 2 h |h⟩`, while `c/2 · 1 |h⟩ = (c/2) |h⟩`. The ratio
on a primary is `2h/(c/2) = 4h/c`, which depends on **both** h and c.
There is no c-independent ratio `S_3 = 2` extractible this way.

**Repair.** Either (a) define S_3 as the ratio of *two specific structure
constants in the chiral homology* (and verify by explicit homological
computation, not by quotienting one field by another), or (b) downgrade
the theorem to `Lemma: the ratio of the (1)-mode coefficient to the
(3)-mode coefficient in T(z)T(w) is identically 2 in BPZ normalization`,
which is true and trivial. The current Theorem 3.1 conflates "structure
constant in the OPE" with "shadow tower coefficient".

### E. The bar-prefactor proof in `three_parameter_hbar.tex` is circular

L290–306: claims to **derive** `r(z) = Ω/((k+h^v)z)` from d-log
absorption of the OPE. But the OPE has `k(t^a,t^b)/(z-w)^2` (no
(k+h^v) factor), and d-log absorption alone gives `k Ω/z`. The
`(k+h^v)` factor appears only through Sugawara renormalization, which
is **not part of d-log absorption**.

**Attack.** "the normalization Ω = Σ t^a ⊗ t_a with (t^a, t_b) = δ^a_b
gives r(z) = (k/(k+h^v)) Ω/z + (1/(k+h^v))[structure constants], which
combines to Ω/((k+h^v)z) by the definition of Ω relative to the
Killing form" is **algebraically opaque**: how does a sum of `k Ω/z`
(a 2-tensor times a scalar) and `f^{ab}_c J^c/(z-w)` (a 2-tensor with a
*field* in one slot) "combine to" `Ω/((k+h^v)z)` (a 2-tensor times a
scalar)? It can't, unless the field-valued term is replaced by its
vacuum expectation, which is 0. So the `(1/(k+h^v))[structure
constants]` term should drop out, leaving `(k/(k+h^v)) Ω/z`, not
`Ω/((k+h^v)z)`. There is a missing factor of k.

**Repair.** State the result as: "**Hypothesis:** Sugawara
renormalization is performed, which rescales the OPE level k by
`k → k/(k+h^v)`. **Conclusion:** the bar-collision residue is
`Ω/((k+h^v)z)`." Or, equivalently, derive the collision residue
honestly as `k Ω/z` (without the Sugawara prefactor) and show that the
**identification** with `ℏ_KZ` and `ℏ_DNP` requires the additional
Sugawara step. Without this, T10 is **conditional on Sugawara
normalization**, not unconditional.

### F. AP155 (overclaiming novelty)

The "three-parameter identification" is itself a known relationship
(KZ coupling = level-shifted inverse, Drinfeld 1985 + Sklyanin 1983).
The remark `rem:classical` (L338) acknowledges this honestly. Good
practice. **No repair needed.**

### G. AP-CY55 ramification: "κ" without subscript

`virasoro_r_matrix.tex` uses bare `κ` throughout (L66, L221, L239 etc.).
This is Vol I, where `κ` was historically allowed; in Vol III scope it
would be `κ_ch`. **For Vol I-internal consistency**, OK, but the
abstract should clarify "modular characteristic κ in the sense of the
monograph (Vol I Theorem D)" once.

------------------------------------------------------------------------

## Section 4 — First-principles analyses

### F1. The two conventions for the affine KM r-matrix (cross-file convention clash, AP151)

**Wrong claim.** "The r-matrix of `V_k(g)` is `r(z) = Ω/((k+h^v)z)`."

OR equivalently: "The r-matrix of `V_k(g)` is `r(z) = k Ω/z`."

**Ghost theorem.** Both formulas are **correct**, in DIFFERENT
conventions, and they are related by **rescaling the Casimir tensor**:
`Ω_KZ = (k+h^v) Ω_trace`. The "trace convention" uses the bare
Killing form; the "KZ convention" uses the Sugawara-rescaled metric on
g, which absorbs the level shift into Ω itself.

**Precise error.** The chiral_chern_weil.tex / holographic_datum.tex
"bridge identity" `k Ω_tr = Ω/(k+h^v)` (L458/L635) tries to express
this rescaling as a *single* identity, but the equation is
dimensionally inconsistent: LHS scales as k, RHS as 1/(k+h^v). The
correct relation is between **r-matrices**:
`r_KZ(z) = (1/(k+h^v)) · r_trace(z)` IF you also rescale Ω.

**Correct relationship.** The KZ convention is the Sugawara-normalized
gauge: it's the r-matrix of the **completed** affine algebra at level k
in the basis where the energy-momentum tensor is `T = (1/2(k+h^v)) Σ
:J^a J_a:`. The trace convention is the **classical** r-matrix
extracted from the OPE before Sugawara. The two are gauge-equivalent
representations of the same operadic datum. **Type:** convention clash
+ label/content (the "bridge identity" labels the rescaling
incorrectly).

### F2. AP136 trap was successfully avoided in chiral_chern_weil.tex

`chiral_chern_weil.tex` L1024 writes `κ(W_N) = c (H_N − 1)` and L1038
explicitly warns `H_{N-1} ≠ H_N − 1`. **This is an AP136-prevention
template**: the formula is in the only non-confusable form, AND the
warning environment names the trap by its identity.

### F3. The "S_3 = 2" identity is the wrong invariant (AP-CY12 ramification at the Vol I level)

**Ghost theorem.** The cubic shadow coefficient *is* a class-M
invariant — it must be **nonzero** for class M, vanishing for class G,
and class-distinguishing in general.

**Precise error.** The current proof (L228–243) extracts S_3 by taking
two **specific OPE coefficients** and dividing them. This is not a
shadow computation; it's an algebraic identity in the structure
constants. The actual cubic shadow lives in the bar cohomology and is
**not** computable from a single ratio in the OPE.

**Correct relationship.** The shadow tower coefficients S_n are
invariants of the bar cohomology of A as a chirally Koszul algebra;
they are computed from the L_∞ structure on `H^*(B(A))`. For Vir_c, S_n
are nonzero for all n ≥ 3 (class M). The numerical *values* of
individual S_n require the full bar-cohomology computation; the
"S_3 = 2" identity, if proved correctly, would say "the cubic L_∞
operation `m_3` on `H^*(B(Vir_c))` is c-independent up to
normalization". This is a genuine and interesting theorem; the current
proof does not prove it.

### F4. The bc/βγ "κ from Sugawara, not from r" is the right theorem stated correctly

`chiral_chern_weil.tex` L890–948 (and `rem:bc-r-matrix` L934) handles
the `r=1` constant case correctly: "kappa extraction from the r-matrix
alone gives zero", "instead, κ arises from the Sugawara stress tensor
of the composite system". **This is the correct first-principles
analysis** of why the slogan "κ = av(r)" needs scoping: it holds when
the diagonal r-matrix is non-trivial; for cross-OPE-only systems, κ
comes from the Sugawara sector. The text gets this exactly right,
including the boundary checks for λ=1/2 and λ=2.

### F5. Holographic datum uniqueness (steelman §10.c)

**Claim under audit.** "Holographic datum = unique up to isomorphism
for ANY Koszul chiral algebra (not just W_3)."

**Ghost theorem.** For a chirally Koszul algebra A, the bar complex
`B(A)` and its Maurer–Cartan element `Θ_A` determine A up to chiral
quasi-isomorphism (this IS theorem 5 of the monograph). Therefore the
*pair* `(A, Θ_A)` is a complete invariant, AND every component of the
holographic datum is a projection of this pair.

**Precise error in the current text.** No completeness/uniqueness
theorem is **stated** in `holographic_datum.tex`. The recovery
proposition (L967, R1–R4) lists four reconstructions of *components*
from `Θ_A`, but doesn't prove the converse direction (that the datum
determines A) nor that the datum is well-defined modulo isomorphism.

**Correct relationship.** The honest statement is:

  "The map `A ↦ H(A) = (A, A^!, C, r(z), Θ_A, ∇^hol)` is functorial in
  chiral quasi-isomorphisms, and the assignment factors through the
  homotopy category of chirally Koszul algebras. The datum is a
  COMPLETE invariant of the homotopy class of A, in the sense that
  `H(A) ≃ H(A')` ⟹ `A ≃ A'` in the chirally Koszul homotopy category."

The current paper PROVES the existence and the four recoveries, but
not the completeness claim. **A genuine "uniqueness up to iso for any
Koszul chiral algebra" theorem requires a separate completeness lemma**,
which would say: "Two chirally Koszul algebras with quasi-isomorphic
holographic data are quasi-isomorphic."

### F6. The Virasoro `R(z) = z^{2h} exp(−c/(4z²))` is the **primary-line restriction**, not the full R-matrix

**Wrong claim (in slogan form).** "The Virasoro R-matrix is
`z^{2h} exp(−c/(4 z²))`."

**Ghost theorem.** On a fixed primary line of weight h, the Virasoro
modes act through `L_0` only (as L_m | h⟩ = 0 for m ≥ 1), so the
path-ordered exponential of `r(z) = (c/2)/z^3 + 2T/z` reduces to an
ordinary exponential, giving `z^{2h} exp(−c/(4 z²))`.

**Precise error.** Off-primary, `T(z) | h⟩` is no longer scalar; the
full R-matrix is operator-valued and does NOT have closed form. Calling
`z^{2h} exp(−c/(4z²))` "the spectral R-matrix of Vir" elides the
primary-line restriction.

**Correct relationship.** The primary-line restriction IS the
**simplest** non-trivial sector and has full closed form; the full R
on the Verma module is determined by the same r(z) but its action is
matrix-valued (in the modes L_{−1}, L_{−2}, …) and admits no
elementary closed form. The Vir paper should rename the result "The
spectral R-matrix on a primary line" and add one sentence about
extension off-primary.

------------------------------------------------------------------------

## Section 5 — Three upgrade paths

### Upgrade U1. Universal chiral Chern–Weil functor

**Statement.** Define
`CW^ch: Bun_G^ch(X) → H^*(M_{g,n}, χ)`
sending a chiral G-bundle to its chiral characteristic class with
explicit coefficient ring `χ = Q[k, h^v, k+h^v, (k+h^v)^{-1}]`.
The functor satisfies:

  (i) **Additivity in level**:
      `CW^ch(P_{k_1+k_2}) = CW^ch(P_{k_1}) + CW^ch(P_{k_2})` modulo
      Sugawara cross-terms.

  (ii) **Critical-level vanishing**:
       at k = −h^v, `CW^ch(P) = 0` (matches κ(V_{−h^v}(g)) = 0).

  (iii) **Naturality**: for a homomorphism φ: G → G' inducing a
        sub-VOA inclusion `V_k(g) → V_{k'}(g')`,
        `CW^ch_φ = (k'/(k'+h'^v)) (k+h^v)/k · CW^ch`
        (the rescaling tracks Sugawara normalization).

The current paper proves this for Heisenberg, Vir, KM, W_N family-by-family.
The upgrade is to assemble these into a **functor**, with a single coefficient
ring containing all the level-dependent denominators.

**Why this is achievable.** Each computation in Section 4 of
`chiral_chern_weil.tex` is already in functorial form (it depends only
on the OPE structure constants of the strong-generation set). Lifting
this to a functor requires only (a) declaring a category of "chiral
G-bundles with strong-generation set" and (b) verifying the morphisms
behave correctly under sub-VOA inclusions.

### Upgrade U2. Closed form for the Virasoro R-matrix at all c, off-primary

**Statement.** On the Verma module `M(c, h)`, the Virasoro R-matrix
admits an integral representation:

  `R(z; c, h) = T_{path-ord} exp ∮_{|w|=ε} r(z, w) dw`

where the path-ordering is over the modes L_{−1}, L_{−2}, …, and the
representation reduces to `z^{2h} exp(−c/(4 z²))` on the highest-weight
vector. The matrix elements satisfy a specific recursion:

  `⟨h, λ| R(z) | h, λ'⟩ = R^{(λ, λ')}(z; c, h)`

with `R^{(0,0)} = z^{2h} exp(−c/(4z²))` and higher matrix elements
computable by Wick contraction in the modes.

**Why this is achievable.** The Vir R-matrix is the Virasoro analog of
the universal Yangian R-matrix; the closed form on primaries is the
"trivial representation" piece. Off-primary, the full R is determined
by the Knizhnik–Zamolodchikov equation in the Vir setting (BPZ),
which is a system of differential equations with explicit solution by
contour integral.

### Upgrade U3. Holographic datum = complete invariant for any Koszul chiral algebra

**Statement.** For a chirally Koszul algebra A with bar complex B(A),
the holographic datum
`H(A) = (A, A^!, C, r(z), Θ_A, ∇^hol)` determines A up to chiral
quasi-isomorphism. Specifically:

  (a) `Θ_A ↦ A` is the cobar functor; this recovers A from Θ.

  (b) The pair `(B(A), Θ_A)` is a complete homotopy invariant of A.

  (c) Every other component of H is a projection of `(B(A), Θ_A)`:
      A^! = (H^* B(A))^∨; C ≃ A^!-mod; r(z) = bin/0-collision; ∇^hol
      = shadow connection.

  (d) Therefore: `H(A) ≃ H(A') ⟹ A ≃ A'` in the chirally Koszul
      homotopy category.

**Why this is achievable.** The hard part (`(B(A), Θ_A)` is a complete
invariant) is the bar-cobar adjunction, already proved in the
monograph. The upgrade is to **assemble the four R1–R4 recovery
clauses into a single completeness statement** and prove the converse.

------------------------------------------------------------------------

## Section 6 — Consolidated punch list

### Hard errors (must fix before publication)
| # | File | Line | Issue | Severity |
|---|------|------|-------|----------|
| 1 | three_parameter_hbar.tex | 210 | LaTeX bug `divided-power convention} = ...`; missing opening brace | BUILD-BREAK |
| 2 | chiral_chern_weil.tex | 458 | False "bridge identity" `k Ω_tr = Ω/(k+h^v)` | MATH-WRONG |
| 3 | holographic_datum.tex | 635 | Same false bridge identity, copy-pasted | MATH-WRONG |
| 4 | chiral_chern_weil.tex | 429 | `r^Vir(z) = (c/2)/z^3 + 2T/z + ∂T` keeps regular term | INTERNAL-INCONSISTENT (the doc's own dlog rule drops it) |
| 5 | virasoro_r_matrix.tex | 220 | `S_3(Vir_c) = 2` proof is tautological (uses 2κ/κ = 2) | PROOF-INVALID |
| 6 | virasoro_r_matrix.tex | 249 | `Δ_Vir = 8 κ S_4 = 40/(5c+22)` — 5c+22 is W_3 W–W denom, not Vir | SCOPE-CONFUSION |
| 7 | three_parameter_hbar.tex | 290–306 | Bar-prefactor "proof" silently uses Sugawara renormalization | PROOF-CONDITIONAL-NOT-LABELED |
| 8 | three_parameter_hbar.tex | 173 | `κ_cl = k dim(g)/(2h^v)` (trace) computed from r in KZ form (L107) | CONVENTION-CLASH |
| 9 | garland_lepowsky.tex | 1324 | `av(r) + dim(g)/2 = κ` doesn't hold in the KZ convention used at L965 | CONVENTION-CLASH |
| 10 | chiral_chern_weil.tex | 780–810 | sl_2 Chevalley-basis Casimir contraction concedes "5? No, 4. Hmm…" with hand-wave | PROOF-GAP |

### Medium issues (should fix; do not block publication)
| # | File | Line | Issue |
|---|------|------|-------|
| 11 | virasoro_r_matrix.tex | 130 | `R(z) = z^{2h} exp(−c/(4z²))` should be tagged "on a primary line" in abstract |
| 12 | virasoro_r_matrix.tex | 318 | KZ-form `Ω/((k+h^v)z)` for KM in document otherwise using trace-form vocabulary |
| 13 | holographic_datum.tex | 967 | "Recovery theorems" do not prove completeness/uniqueness despite slogan "complete invariant" |
| 14 | w3_holographic_datum.tex | 256 | Even pole `z^{-2}` in W–W channel contradicts the global "bosonic ⇒ odd poles" slogan in virasoro_r_matrix.tex L121–124; needs scope tag |
| 15 | chiral_chern_weil.tex | 547 | Theorem 4.1 item (iii) "kernel records R-matrix, braiding, Yangian coherences" is narration; should be a separate proposition with proof |
| 16 | garland_lepowsky.tex | 1217 | Critical-level item (v) `H^n ≅ Ω^n(Op)` cites Raskin/FLE; should carry `\ClaimStatusProvedElsewhere` tag |
| 17 | virasoro_r_matrix.tex | passim | bare `κ` (Vol I usage); harmless but flag for cross-volume migration to `κ_ch` |

### Convention-hygiene line
**Recommended global edit:** add a one-paragraph "Convention" note at
the top of `chiral_chern_weil.tex`, `holographic_datum.tex`,
`three_parameter_hbar.tex`, `garland_lepowsky.tex`, and
`virasoro_r_matrix.tex` reading:

  "**r-matrix conventions.** Throughout, we use the **trace
  convention**: the affine KM r-matrix is `r(z) = k Ω/z` with Ω the
  Casimir of the Killing form (long roots squared length 2). The KZ
  convention `r^KZ(z) = Ω/((k+h^v) z)` is related by Sugawara
  renormalization: `r^KZ(z) = (1/(k+h^v)) r^trace(z)` together with
  `Ω^KZ = (k+h^v) Ω^trace`. We **never** mix conventions in a single
  derivation; mixed-convention identities such as
  `k Ω_trace = Ω_KZ/(k+h^v)` are *false at every value of k* and must
  not appear."

### Cache write-back
The cross-file convention clash + the false "bridge identity" is a
NEW Vol I confusion pattern not in the cache (entries 1–56 are mostly
Vol III/Vol II). One entry has been appended to
`/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md`.

### Three positives (model practice to preserve)

  (a) `chiral_chern_weil.tex` L1038 `warn:harmonic` is the gold-standard
      AP136 trap-prevention; replicate this style elsewhere.

  (b) `chiral_chern_weil.tex` L890–948 + `rem:bc-r-matrix` correctly
      handles bc/βγ as a *case where the slogan κ = av(r) does not
      apply directly*; this is the correct first-principles analysis.

  (c) `holographic_datum.tex` PE-1 r-matrix audit comments (e.g.,
      L516–522, L621–631) are exemplary in-source AP126 verification
      logs. Every r-matrix declaration should carry such a comment
      block.

------------------------------------------------------------------------

## Summary tally

- AP126 violations (literal bare Ω/z): **0** in `chiral_chern_weil.tex`
  and `holographic_datum.tex` (these files use trace convention with
  level prefix). Modulated AP126 (KZ-form without scope tag) appears in
  4 files and produces convention clashes.
- AP141 follow-up: the systemic check "k=0 ⇒ r=0" is performed correctly
  for all trace-form r-matrices but **not** flagged for KZ-form (where
  the test is wrong: KZ r at k=0 is `Ω/h^v`, not 0).
- AP136: 1 trap successfully prevented (W_N harmonic), 0 violations.
- AP39: κ formulas for Heisenberg, Virasoro, KM are correct in all
  files; W_N formula consistent with H_N − 1 form. No violations.
- AP151 (convention clash): **5+ instances** across the 6 files; the
  load-bearing instance is the false "bridge identity" at
  `chiral_chern_weil.tex` L458 / `holographic_datum.tex` L635.
- AP-CY55 (kappa subscript): N/A (Vol I scope, bare κ permitted), but
  flagged for cross-volume migration.
- AP155 (overclaiming novelty): 0 violations; `rem:classical` is honest.

**Top-3 healings (in order of leverage):**

  1. Fix the false bridge identity (Hard #2, #3, #9) — single repair
     resolves 3 hard errors and the underlying convention clash.

  2. Add the global convention note to all 5 files — prevents future
     convention-clash regressions.

  3. Re-prove `S_3(Vir_c)` via genuine bar-cohomology computation
     (Hard #5) — converts a tautology into a real theorem.
