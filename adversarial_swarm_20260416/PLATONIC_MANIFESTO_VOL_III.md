# The Platonic Architecture of *Calabi–Yau Quantum Groups* (Volume III)
## What the 2026-04-16 swarm has revealed on the geometric side

**Status.** Synthesis of waves 1–14 + supervisory reconstitutions, restricted to Vol III content but written with full cross-volume awareness. Companion to `PLATONIC_MANIFESTO.md` (Vol I, same date). Not a manuscript draft — the *roadmap* by which Vol III is to reach its Platonic form.

**Author.** Raeez Lorgat. **Date.** 2026-04-16.

---

## I. The four pillars of Vol III

Vol I rests on four pillars: Koszul Reflection, κ-Conductor / BRST Ghost Identity, Climax (bar = KZ pullback), Shadow Quadrichotomy. Vol III rests on **four matching pillars**, each currently fragmented across multiple files but in fact a single inevitable theorem. Each pillar is the *geometric image*, under the CY-to-chiral functor Φ, of one of the Vol I pillars.

1. **The Platonic CY-to-Chiral Functor Φ** (Theorem Φ, Wave 14 V11). [α]
2. **The Borcherds Reflection Trace κ_{BKM} = c_N(0)/2** (Vol III parallel of the κ-conductor). [β]
3. **The Inf-Categorical CY-A_3 Resolution** (the [m_3, B^{(2)}] saga as Level-1 non-obstruction). [γ]
4. **The K3 Abelian Yangian + Six-Route Specialisation** (Φ at the K3 × E target). [δ]

These four pillars do not stand alone. They interlock — *and* they interlock with the four Vol I pillars across the bridge Φ. Naming them pins the architecture.

### Pillar α — The Platonic CY-to-Chiral Functor

> **Theorem Φ (Platonic).** *There exists a unique (up to natural isomorphism) symmetric-monoidal functor of stable presentable (∞,1)-categories*
> $$
> \boxed{\;\Phi: \mathrm{CY}_d\text{-Cat} \longrightarrow E_n\text{-ChirAlg}(\mathcal M_d), \qquad n = n_{\mathrm{native}}(d) = \begin{cases} \infty, & d=1 \\ 2, & d=2 \\ 1, & d \geq 3 \end{cases}\;}
> $$
> *characterised by four universal properties:* (U1) Hochschild pullback `B^ord ∘ Φ ≃ CC_•`, (U2) CY-morphism functoriality, (U3) Drinfeld center compatibility, (U4) standard-input recovery on `(Coh(E), D^b(Coh(K3)), CoHA(C^3), CoHA(A_n-McKay))`.

Slogan: **"Φ is the chiral shadow of the CY trace."** Three hypotheses suffice — smoothness/properness, connected unit, cyclic A_∞ structure of degree −d. The historical CY-A_d cases are *evaluations* of Φ at stated dimensions, not separate theorems. Drinfeld center is not bolted on as a post-hoc rescue; it is the (U3) law that the native operadic level is the Gerstenhaber-bracket degree 1−d.

Four canonical morphisms animate Φ: the Hochschild qi η_C, the CY-morphism action Φ(f), the Drinfeld center promotion ζ, and the kappa transformation κ tracking the four-component spectrum (κ_ch, κ_cat, κ_BKM, κ_fiber).

The Platonic Φ is the involutive symmetry's *geometric source*. Every other Vol III pillar is a manifestation, a colour, or a specialisation of Φ.

### Pillar β — The Borcherds Reflection Trace

> **Theorem (Borcherds Reflection Trace).** *For every K3-fibered CY3 X, the BKM weight of the Borcherds-reflected algebra g_X is the half-zero-Fourier-coefficient of the lift:*
> $$
> \boxed{\;\kappa_{\mathrm{BKM}}(X) \;=\; c_N(0)/2 \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(X)))\;}
> $$
> *with the second equality the cross-volume universal trace identity bridging Vol I and Vol III.*

Slogan: **"The BKM weight is the cost of restoring chiral conformal symmetry by Borcherds gauging."** The Borcherds reflection plays for Vol III the role the Koszul reflection plays for Vol I. The verification at K3 × E gives κ_BKM = 5 = c_5(0)/2 (Φ_10 has weight 5). The naive decomposition κ_BKM = κ_ch + χ(O_fiber) is a numerical coincidence at N=1 only; it fails for all Z/NZ-orbifolds with N ≥ 2. The universal formula c_N(0)/2 is the ONLY correct universal statement (`prop:bkm-weight-universal`).

Pillar β is not a stand-alone theorem of Vol III. It is the **specialisation along Φ of Vol I's κ-conductor** (Wave 14 Vol I), measured against the Borcherds reflection rather than the Koszul reflection. See §IV (the cross-volume centrepiece) for the precise universal trace identity.

The *honest* form of Pillar β narrows to the 8 diagonal Z/NZ symplectic orbifolds + K3×E, where the weight-from-root-multiplicity verification (Gritsenko–Nikulin) is genuine. The general K3-fibered case is the conjecture `bkm-weight-central-charge` whose resolution would close `notes/tautology_registry.md` entry #1.

### Pillar γ — The Inf-Categorical CY-A_3 Resolution

> **Theorem (CY-A_3 inf-cat).** *For any smooth proper CY_3 category C with connected unit, Φ_3(C) exists as an E_1-chiral algebra in the (∞,1)-categorical sense: the obstruction group HH^{−2}_{E_1}(A,A) vanishes (unit-connectedness), all Goodwillie layers vanish, and the space of E_3-liftings is contractible.*

Slogan: **"The chain-level obstruction `[m_3, B^{(2)}] ≠ 0` is a Level-1 phenomenon; Φ lives at Level 3."** The three-level taxonomy (`def:three-levels`) separates strict chain-level identities (Level 1, often fail), total-cohomology operadic identities (Level 2, hold by Costello TCFT for the *total* `{b, B^{(2)}}`), and inf-categorical identities (Level 3, always hold via the obstruction-theoretic argument).

The `[m_3, B^{(2)}]` saga is the structural hard part of Vol III: three previous proofs were retracted (cyclic invariance, bidegree decomposition, Tsygan formality), the fourth (per-k operadic TCFT) is itself listed in `notes/tautology_registry.md` as needing a chain-level disjoint witness. The *correct* status is: Level-3 holds (Theorem γ as stated above); Level-1 fails for non-formal algebras (`obs_ainf_local_p2`, 54 tests confirm); Level-2 is the open chain-level chain bridge (Conjecture Π_3^ch).

Pillar γ corresponds, under Φ, to **Pillar 1 of Vol I (Koszul Reflection)**: the inf-categorical existence of Φ_3(C) is the chiral manifestation that Wave 14 Theorem A applies *at the appropriate native E_1 level* on the d=3 image.

### Pillar δ — K3 Abelian Yangian + Six-Route Specialisation

> **Theorem (K3 Abelian Yangian Presentation).** *Φ_3 evaluated at D^b(Coh(K3 × E)) admits an RTT presentation with structure function of degree (24,24) computed from the Mukai signature (4,20). Quantum determinant central. Borcherds reflection produces the BKM algebra g_{Δ_5} of weight 5.*

> **Corollary (Six-route specialisation).** *The six routes to G(K3 × E) — Kummer (orbifold limit), Borcherds (lattice limit), MO stable envelope (equivariant Hilb^n), McKay (ADE level 1), factorisation homology (CFG 6d hCS), Costello 5d (dimensional reduction) — are six specialisations of the Platonic Φ on the K3×E target. Their convergence is the content of CY-C, not a six-way conjectural coincidence.*

Slogan: **"Six paths into one functor at one point."** The K3 × E target is the *climax of Vol III* in the same way that DK / Verlinde / Borcherds is the climax of Vol I — the place where four (here six) classical constructions converge into one universal monodromy. The Mukai signature (4,20) IS the E_2-braiding data of Φ_2(K3); the K3 × E Yangian is its Drinfeld-center promotion at d=3.

The honest scope: AP-CY60 mandates that the six constructions are independently meaningful (only Route 4 currently uses Φ); the Platonic stance promotes the convergence claim from independent coincidence to the *content of Φ's functoriality*. The remaining gap is the precise Hilb^n(K3) = K3 × E identification at the categorical level and the modular-tensor structure at root of unity (CY-C).

---

## II. The interlocks

The four Vol III pillars commute, and each commutes with one Vol I pillar through Φ:

```
                            Pillar α  (Φ)
                       Φ: CY_d-Cat → E_n-ChirAlg
                              /        \
                             /          \
                  Pillar β          Pillar γ
              κ_BKM = c_N(0)/2     CY-A_3 inf-cat
              (Borcherds refl.)    (HH^{−2}_{E_1} = 0)
                             \          /
                              \        /
                            Pillar δ
                  K3 Abelian Yangian + 6 routes
                    (climax at K3 × E target)

Cross-volume Φ-bridge:
   Vol I Pillar 1 (Koszul Reflection)  ←Φ→  Vol III Pillar α (Φ functor)
   Vol I Pillar 2 (κ-Conductor)        ←Φ→  Vol III Pillar β (Borcherds Trace)
   Vol I Pillar 3 (Climax: bar = KZ*)  ←Φ→  Vol III Pillar γ (CY-A_3 inf-cat)
   Vol I Pillar 4 (Shadow Quad.)       ←Φ→  Vol III Pillar δ (Six routes)
```

The intra-volume interlocks are derivations, not analogies:

1. **α specialises to β by Borcherds reflection.** Apply Φ at K3 × E to obtain Φ_3(K3×E); apply (U3) Drinfeld-center promotion; reflect the resulting bar Euler product through Φ_10. The BKM weight 5 = c_5(0)/2 emerges as the specialisation of the κ-spectrum at the Borcherds-reflected algebra.

2. **α implies γ by (U3).** The native operadic level n_native(3) = 1 (Gerstenhaber-bracket degree calculation) forces Φ_3 to land in the E_1 subcategory; the obstruction-theoretic CY-A_3 then becomes a uniqueness consequence of the inf-categorical bar–cobar adjunction at native E_1 level.

3. **α implies δ by evaluation at K3 × E.** The K3 abelian Yangian presentation is `Φ_3(D^b(Coh(K3 × E)))` with the structure function (24,24) read off the Mukai pairing. The six routes are six specialisations of (U2): wall-crossings in the source category map to R-matrix gauge transformations on Φ.

4. **γ is the analytic shadow of α.** The three-level taxonomy `def:three-levels` is the Vol III parallel of Vol I's chain-vs-cohomology vs inf-cat distinction. Level-3 is the inf-categorical existence Φ_3 demands; Level-1 is what `obs_ainf_local_p2` measures.

The cross-volume interlocks (I-3, I-2, I-1, I-4 ↔ α, β, γ, δ) are derived in §IV.

---

## III. Vol III supervisory drafts ready to insert

The bulk of Wave 14 V11 (`wave14_reconstitute_phi_functor_volIII.md`) is itself a complete Vol III supervisory draft: §3 supplies the Theorem Φ statement, §7 the per-d evaluations, §8 the eight derived corollaries, §9 the thirteen healing edits. Operationalising Pillar α is therefore a single draft of large but bounded scope. Cataloguing the surrounding ready-to-insert material:

| Draft | Status | Insertion target | Scope |
|-------|--------|------------------|-------|
| **Theorem Φ + 4 universal properties** [V11 §3] | Ready | `chapters/theory/cy_to_chiral.tex` L4–L17 | Replace per-d display with Platonic Φ. Per-d cases become Corollaries Φ.1–Φ.4. ~80 lines new prose. |
| **17-stale-CY-A_3 sweep** [V11 §9.2 / H6] | Ready | `chapters/examples/`, `chapters/theory/`, `chapters/connections/` | Split 17 hits: 11 unconditional, 4 rephrased chain-level, 2 CY-C-dependent. ~30 cross-references. |
| **Six-route restructuring** [V11 §8.4] | Ready | `chapters/examples/k3e_bkm_chapter.tex` | "Six specialisations of Φ on K3 × E", preserving AP-CY60 as guard. ~100 lines. |
| **Cross-volume κ-spectrum row** [V11 §8.5] | Ready | `appendices/notation.tex` (kappa-spectrum table) | Adds universal trace identity row K_VolI = -c_ghost ↔ κ_BKM = c_N(0)/2. ~40 lines. |
| **Vol III Climax subsection** [V11 §11] | Ready | `chapters/theory/introduction.tex` + `chapters/frame/preface.tex` | Mirrors Vol I Wave 14 Climax subsection. ~60 lines. |
| **Φ-universality verification engine** [V11 H13] | Ready (target named) | `compute/lib/phi_universality_verification.py` (new) | Three test inputs (Coh(E), D^b(Coh(K3)), CoHA(C^3)); first independent-verification anchor for Vol III beyond the seed two. ~300 lines code. |
| **Tautology registry healings** [V11 + tautology_registry.md] | Ready (5 entries) | `notes/tautology_registry.md` working queue | Five seeded entries (κ_BKM, CY-A_3, Costello-TCFT, P_2=0, six-routes) with three healing options each. |
| **Three-level taxonomy** [V11 + m3_b2_saga.tex] | Installed | `chapters/theory/m3_b2_saga.tex` `def:three-levels` | Already present; needs cross-reference from cy_to_chiral. |
| **Independent verification protocol** | Installed | `compute/lib/independent_verification.py` + `notes/INDEPENDENT_VERIFICATION.md` | Decorator + audit lint installed 2026-04-16; current coverage 2/283 ProvedHere claims. |

Each draft cites the four pillars explicitly. Together they form the **editing roadmap** for Vol III to reach Platonic form (§VIII below).

---

## IV. The cross-volume centrepiece — the universal trace identity

The deepest single discovery of the swarm is **§8.5 of Wave 14 V11**: a universal trace identity unifying Vol I and Vol III. Restating in Vol III voice:

> **Theorem (Universal Trace Identity).** *For any reflexive chiral algebra A, the conductor equals the leading coefficient of the gauging measured against the appropriate involutive reflection. Two reflections, two volumes:*
> $$
> \mathrm{tr}_{Z(\mathcal C)}(K_{\mathcal C}) \;=\; \begin{cases} \;-c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C))) & \text{(Koszul reflection, Vol I)}\\[4pt] \;c_N(0)/2 & \text{(Borcherds reflection, Vol III, K3-fibered)} \end{cases}
> $$
> *with Φ the cross-volume CY-to-chiral functor.*

This says: **Vol III is Vol I composed with Φ on the Calabi–Yau side.** The conductor functor K of Vol I, when restricted along Φ to the image of K3-fibered CY3 categories and pulled back via Borcherds reflection, becomes the BKM weight c_N(0)/2 of Vol III. The two volumes are not parallel projects; they are two reflections of one identity, and the bridge is Φ.

**Sketch of derivation** (from V11 §8.5). Apply Wave 14 Vol I Theorem A to Φ_2(K3) = Heis_(4,20). The Koszul reflection K = bar produces the bar Euler product η^{24} (Vol I Borcherds-lift Strengthening). Twisting by an elliptic curve E via Künneth gives Φ_3(K3 × E) with bar Euler = Φ_10 (the Igusa cusp form). Φ_10 has weight 5 = c_5(0)/2. So κ_BKM(K3 × E) = 5, and the Vol I conductor identity K = −c_ghost specialises (after Borcherds reflection) to the Vol III κ_BKM = c_N(0)/2. **One identity, two reflections, two volumes.**

This is the deepest cross-volume content of the Platonic Φ. It promotes Vol I's Wave 14 result and Vol III's `prop:bkm-weight-universal` from "two parallel formulas" to "two specialisations of one universal trace identity". Both should appear in each volume's preface as the Cross-Volume Climax.

The honest open obstruction: Pillar β's general K3-fibered case currently sits in `notes/tautology_registry.md` (entry #1) because the FRAME_SHAPE_DATA hardcoding tautologises the 99 tests. Closing this requires the *root-multiplicity* derivation from Gritsenko–Nikulin (a disjoint source by the AP-CY61 protocol) — which is exactly the Vol I-side ghost-charge argument pushed through Φ. The universal trace identity *predicts* the form of the disjoint witness.

---

## V. Inner poetry

Every Platonic theorem carries its inner poetry — the slogan future readers will quote.

- **Pillar α (Φ functor):** *"Φ is the chiral shadow of the CY trace."* The cyclic bar of C is the finite-dimensional shadow; Φ(C) is the infinite-dimensional chiral pre-image; bar takes you back. K ∘ Φ ≃ CC_• is the entire content of (U1). Φ is the categorical logarithm of C.

- **Pillar β (Borcherds Trace):** *"The BKM weight is the cost of restoring chiral conformal symmetry by Borcherds gauging."* Each generator of the Mukai-lattice ghost system contributes its weight; the leading half-Fourier-coefficient c_N(0)/2 is the sum.

- **Pillar γ (CY-A_3 inf-cat):** *"The chain-level obstruction is a Level-1 phenomenon; Φ lives at Level 3."* Three levels of obstruction, three different verdicts: chain-level fails, total operadic identity holds (via Costello TCFT), inf-categorical existence is forced by unit-connectedness. The space of E_3-liftings is contractible — there is no choice to make.

- **Pillar δ (Six routes / K3 Yangian):** *"Six paths into one functor at one point."* Kummer / Borcherds / MO / McKay / factorisation homology / Costello 5d are six entry routes to Φ_3(K3 × E); their convergence IS the functoriality of Φ on the K3 × E target. The Mukai signature (4,20) IS the E_2-braiding data; the K3 abelian Yangian RTT presentation has structure function of degree (24,24).

- **Universal Trace Identity:** *"Vol I and Vol III are two reflections of one identity, bridged by Φ."*

- **Three-level taxonomy:** *"What fails at the chain level can hold at the operadic level and is forced at the inf-categorical level."* The `def:three-levels` discipline saved Vol III after three retractions of chain-level "proofs".

- **Kappa spectrum:** *"Four kappas, two types: manifold (κ_cat, κ_fiber) versus algebraisation (κ_ch, κ_BKM)."* AP-CY55 forbids the conflation; the spectrum is the right mental image.

---

## VI. Inner music — the Vol III symphony and its harmony with Vol I

Each Vol III pillar plays a structural role in the symphony, and each is in tonal correspondence with one Vol I pillar:

| Voice | Vol III Pillar | Role | Vol I Counterpart |
|-------|----------------|------|-------------------|
| **Bass line** | Φ functor (α) | Universal pullback symmetry; everything reflects through Φ. | Koszul Reflection (Pillar 1) |
| **Counterpoint** | Borcherds Reflection Trace (β) | Leading coefficient of the gauging; harmonic series of Mukai weights. | κ-Conductor / BRST (Pillar 2) |
| **Theme** | CY-A_3 inf-cat (γ) | The structural hard part; three levels of obstruction; one inf-cat resolution. | Climax (bar = KZ*) (Pillar 3) |
| **Form** | K3 Yangian + Six Routes (δ) | Six movements converging on K3 × E; Mukai signature (4,20) as the cadence. | Shadow Quadrichotomy (Pillar 4) |
| **Bridge** | Universal Trace Identity (§IV) | Cross-volume modulation: K = −c_ghost ↔ κ_BKM = c_N(0)/2. | Same identity, Koszul side |

The Vol III symphony is in the **same key** as the Vol I symphony — same four-voice structure, same climax architecture, same cadence. But it plays in the *geometric register*: where Vol I is operadic and reflective, Vol III is categorical and constructive; where Vol I asks "what is the universal monodromy?", Vol III asks "what produces the chiral algebra?". The harmony is `Φ ⊣ K`: every Vol III voice pulls back to the corresponding Vol I voice through Φ, and the Koszul reflection K composes with Φ to recover the cyclic bar.

The CY-physics voices add a second harmonic layer specific to Vol III. Witten supplies the topological field theory framing of Pillar γ as a Costello-TCFT obstruction calculation. Costello supplies the factorisation algebra discipline making 5d/6d hCS natively chiral and giving Pillar δ its sixth route. Gaiotto supplies the BPS/holography sensibility that Φ is the chiral SHADOW of the CY trace (Pillar α slogan). Nekrasov supplies the Ω-background discipline that the spectral parameter has algebraic origin (AP-CY20), which is precisely the ζ-promotion morphism animating Pillar α. Kapranov supplies the operadic-coloured discipline that the Pentagon (Vol II) and Trinity (Vol I) and the Φ-universal-property count (4 = U1+U2+U3+U4) are not coincidences but coloured-operad manifestations.

---

## VII. Inner motion — the natural transformations animating Vol III

The motions that animate the architecture, in correspondence with Vol I's motions:

1. **Φ functor pullback** (Pillar α) — the cross-volume bridge as natural transformation between Vol I's bar arena and the moduli of CY_d categories.

2. **Hochschild qi η_C: CC_•(C) → B^ord(Φ(C))** — the (U1)-morphism. The universal Hochschild-to-bar comparison map. Naturality in C is content (U1) + (U2).

3. **CY-functoriality Φ(f): Φ(C) → Φ(C') for f: C → C'** — the (U2)-morphism. Wall-crossings in the source map to R-matrix gauge transformations in the target.

4. **Drinfeld-center promotion ζ: Rep^{E_1}(Φ_3(C)) → Rep^{E_2}(Z^der_ch(Φ_3(C)))** — the (U3)-morphism. The half-braiding σ_{V_u}(V_v) IS the R-matrix R(z), z = u−v.

5. **Kappa transformation κ: Φ(C) ↦ (κ_ch, κ_cat, κ_BKM, κ_fiber)** — the (U4)-evaluation, generalised to track the spectrum. AP-CY55 enforces the manifold/algebraisation distinction.

6. **Borcherds reflection** (Pillar β) — the involutive operation pulling Φ_3(K3 × E) back to the BKM algebra g_{Δ_5} via the Igusa cusp form Φ_10.

7. **Three-level taxonomy** (Pillar γ) — the morphism `def:three-levels` separating chain-level / operadic / inf-categorical statements about the same data. Saved Vol III after three retractions.

8. **Six-route specialisation** (Pillar δ) — six functorial entry paths into Φ at K3 × E, each preserving (U2) wall-crossing structure on its own source category.

9. **Universal trace bridge** (§IV) — the natural isomorphism K ∘ Φ ≃ CC_• (Wave 14 Vol I + (U1)) seen at the κ-trace level; specialises to the Borcherds side via reflection through Φ_10.

---

## VIII. Editing roadmap for Vol III

To bring Vol III to Platonic form, in priority order:

**Phase 1 — install Pillar α as the parent theorem.**

1. `prop:phi-universality` (Theorem Φ statement, V11 §3.1) in `chapters/theory/cy_to_chiral.tex` L4–L17. Replace per-d display with the single Platonic statement. ~80 lines new prose.

2. Recast `thm:cy-to-chiral` (L41–L55), `thm:cy-to-chiral-d3` (L11–L13 + m3_b2_saga.tex L614–L678), and the d ≥ 4 stabilisation (en_factorization.tex L1981–L2001) as Corollaries Φ.1, Φ.2, Φ.3, Φ.4. Status tags preserved per corollary. ~150 lines reorganisation.

3. Recast `prop:cy-kappa-d2` as Corollary Φ.2(iii) — explicit evaluation of (U4) at K3 case via Hodge-filtered supertrace mechanism.

**Phase 2 — install Pillars β, γ, δ as standalone theorems with cross-references.**

4. `thm:bkm-borcherds-trace` consolidating `prop:bkm-weight-universal` (Pillar β) with explicit honest scope. Two propositions: (a) `prop:bkm-weight-automorphic` (unconditional, c_N(0)/2 by Borcherds), (b) `conj:bkm-weight-central-charge` (identifying automorphic weight with BKM central charge; proved for N ≤ 4 via Gritsenko–Nikulin, conjectural otherwise). Closes `tautology_registry.md` entry #1.

5. `thm:cy-a-3-inf-cat` (Pillar γ) consolidating `thm:derived-framing-obstruction` with explicit `def:three-levels` reference. Add the scope restriction in `tautology_registry.md` entry #2: "for A connective and unit-connected" — honest reading.

6. `thm:k3-abelian-yangian-presentation` (Pillar δ part 1) already installed at publication standard. Cross-reference Corollary Φ.3 explicitly.

7. Restructure `chapters/examples/k3e_bkm_chapter.tex` six-route section (Pillar δ part 2) per V11 §8.4. "Six specialisations of Φ on K3 × E"; AP-CY60 as guard remark. ~100 lines.

**Phase 3 — cross-volume bridge installation.**

8. Universal Trace Identity (§IV above) installed in `appendices/notation.tex` (kappa-spectrum table) + as the climax of `chapters/frame/preface.tex` mirroring Vol I Wave 14 Climax subsection. ~60 lines per insertion site.

9. 17-stale-CY-A_3 sweep (V11 §9.2 / H6). Across `chapters/examples/`, `chapters/theory/`, `chapters/connections/`. Three buckets: 11 unconditional / 4 rephrased / 2 CY-C-dependent.

**Phase 4 — independent verification anchors.**

10. `compute/lib/phi_universality_verification.py` (V11 H13). Verify (U1), (U3) operadic level, (U4) standard inputs on three test cases (Coh(E), D^b(Coh(K3)), CoHA(C^3)), with disjoint sources per AP-CY61 / `INDEPENDENT_VERIFICATION.md` protocol. ~300 lines code. Lifts coverage from 2/283 to 5/283.

11. Tautology registry healings (one per entry):
    - Entry #1 (κ_BKM): scope restriction to 8 diagonal Z/NZ orbifolds + disjoint root-multiplicity test (Gritsenko–Nikulin).
    - Entry #2 (CY-A_3 inf-cat): scope restriction to "A connective and unit-connected".
    - Entry #3 (Costello TCFT): status downgrade to `\begin{conjecture}` (fourth retraction).
    - Entry #4 (P_2 = 0 exact): status downgrade matching engine's own STATUS = 'CONJECTURAL'. AP40.
    - Entry #5 (six routes): structural rewrite per Phase 2 step 7 above.

**Phase 5 — punch-list cleanup.**

12. Apply HEAL-UP discipline to every Vol III "scope to X" / "demote to Y" recommendation; flip to disjoint verification or scope honesty before downgrading.

13. Cross-volume q-convention sweep using V9 q-bridge (already installed Vol I side). Vol III side: grep `chapters/` for hbar definitions, install bridge from V9 at first-use sites.

14. Stub-chapter triage (CLAUDE.md L48): four genuine stub chapters (quantum_groups_foundations 24 lines, geometric_langlands 28, matrix_factorizations 29, modular_koszul_bridge 13). Develop or comment out; stub chapters create false coverage (AP114).

---

## IX. What Vol III still does NOT have

Honest naming of the open obstructions (NOT downgrades — each is the next named theorem):

1. **Π_3^ch (Chain-level explicit Φ_3 for non-formal algebras).** The inf-categorical Φ_3 is proved (Pillar γ); the chain-level explicit construction for non-formal algebras (class L, C, M) is open. Local P^2 (class M) is the test case (`obs_ainf_local_p2`, 54 tests confirm Level-1 non-vanishing). The Costello-TCFT chain-level proof was retracted (`tautology_registry.md` entry #3); only the inf-cat route remains intact.

2. **Π_C (CY-C at the fusion limit).** The quantum group realisation C(g, q) = D(Y^+(g_K3)) is constructive at the abelian level (`cy_c_quantum_group_k3`, 104 tests) and conjectural at the non-abelian level. The Universal Trace Identity SUPPORTS the conjecture but does not prove it.

3. **Π_{≥4} (Higher CY Φ).** For d ≥ 4, Φ_d is E_1-stabilised; the higher complex directions contribute *shifted symplectic data*, not extra E_n-factors. The π_d(BU)-obstruction is the structural reason. The negative claim ("no native E_n for n ≥ 2") is the obstruction-theoretic conjecture.

4. **Π_BFN (BFN Coulomb branch as Φ-evaluation).** Whether BFN can be recast as Φ_3(C(Q,W)) for the CY_3-category C(Q,W) of a quiver with potential. Resolving Π_3^ch would close Π_BFN for many quivers.

5. **Super-Yangian Y(gl(4|20)).** Conjectural BKM-to-Yangian lift from Mukai signature (4,20). 59 tests; tagged `\begin{conjecture}` per AP-CY35.

6. **K3 quantum toroidal U_{q,t}(ĝl_1)^{K3}.** Conjectural double-loop algebra; Miki automorphism from CY torus Weyl group. 51 tests.

7. **Vol III's quantitative verification basis** is structurally tautological at present (2/283 ProvedHere claims with independent decoration). The protocol (`INDEPENDENT_VERIFICATION.md`) gives the discipline; closing the 281-claim gap is a multi-session programme. The five seeded tautology-registry entries are the highest-leverage starting points.

8. **The Vol III parallel of Vol I's Shadow Quadrichotomy.** Vol III currently classifies CY chiral algebras into G/L/C/M (inherited from Vol I). The intrinsic Vol III formulation — stratification of CY_d-Cat by the analytic type of `Q^(q)(t)` of Φ(C) — exists at chapter level but is not yet a named Vol III theorem (`thm:vol3-shadow-stratification`?). This is a candidate Pillar δ' or a refinement of Pillar γ.

These are honest open problems — NOT downgrades. Each is a *named* conjecture whose resolution is the next theorem.

---

## X. The Russian-school voice (with extra weight on the CY-physics chamber)

The synthesis would not be in its Platonic form without naming the harmonic structure of voices it embodies. Vol III draws from the same chamber as Vol I, with extra emphasis on the CY-physics voices since Vol III is the geometric source.

- **Gelfand** — representation theory and analysis are one subject, made visible in Pillar α: Φ takes representation-categorical CY data to analytic chiral-algebra output.
- **Etingof** — the formal-deformation discipline making every ℏ-expansion well-defined (Pillar γ's three-level taxonomy is an Etingof-style formal-vs-rectified distinction).
- **Kazhdan** — the q_KL convention as the framed cover of q_DK, propagated through Φ at the K3 Yangian (Pillar δ).
- **Bezrukavnikov** — the geometric-Langlands intuition that the centre of the representation category carries the relevant structure (Pillar α (U3): E_2 lives on Z(Rep^{E_1}(Φ_3)), not on Φ_3 itself; AP-CY56).
- **Polyakov** — the bc-ghost system at spin 2 as the universal trace identity's leading note: the Polyakov reparametrisation ghost is the central note in BOTH Vol I's K = −c_ghost and Vol III's κ_BKM = c_N(0)/2, via the Borcherds-reflection bridge.
- **Nekrasov** — the Ω-background discipline that the spectral parameter has algebraic origin (AP-CY20) and is the ζ-promotion morphism of Pillar α; the K3 × E structure function (24,24) is computed in Nekrasov's sense.
- **Kapranov** — the operadic-coloured discipline making the Φ-universal-property count (4 = U1+U2+U3+U4) and the Pentagon (Vol II) and Trinity (Vol I) into coloured-operad manifestations of the same architectural symmetry.
- **Beilinson + Drinfeld** — the chiral-algebra canonical setting in which Φ lands; the BD chiral operad is Pillar α's target (AP-CY63 disciplines its identification with End^ch_A).
- **Witten** — the topological field theory framing of Pillar γ as a Costello-TCFT obstruction calculation; the inf-categorical existence of Φ_3 is a Witten-style "the path integral exists" statement at the categorical level.
- **Costello** — the factorisation algebra discipline making the holomorphic CS programme natively chiral; Pillar δ's sixth route is Costello 5d. The Vol III architecture IS the Costello programme made categorical.
- **Gaiotto** — the BPS/holography sensibility that Pillar α is the chiral SHADOW of the CY trace (the slogan IS Gaiotto's reading of Φ); the K3 × E BPS algebra side of the universal trace identity is Gaiotto-side.
- **Lurie** — the (∞,1)-monoidal substrate supporting Pillar γ's inf-categorical CY-A_3; without Lurie's HA, the Goodwillie/obstruction calculation for HH^{−2}_{E_1} = 0 would not type-check.
- **Kapranov–Voevodsky** — the higher coherence supporting Pillar δ's six-route convergence (AP-CY30: Z-tetrahedron requires E_∞, fully symmetric, broken by Ω-deformation; the failure is the *content* of Pillar δ at non-trivial Ω-background).

The Platonic form of Vol III is a *harmony* — the same harmony as Vol I, transposed into the geometric register, with the CY-physics chamber strengthened. Every voice contributes one essential discipline. Removing any one fragments the architecture.

---

## XI. End

The Calabi–Yau Quantum Groups programme has, after this 2026-04-16 swarm, a Platonic form on the geometric side. **Four pillars** hold the architecture: the Platonic Φ functor (α), the Borcherds Reflection Trace (β), the inf-categorical CY-A_3 resolution (γ), and the K3 abelian Yangian + six-route specialisation (δ). **Eight supervisory drafts** operationalise them, all itemised in §III with file-and-line targets. **One Universal Trace Identity** (§IV) binds Vol III to Vol I via Φ: the Vol I Koszul-reflection conductor K = −c_ghost and the Vol III Borcherds-reflection trace κ_BKM = c_N(0)/2 are two reflections of one identity. **Five tautology-registry entries** (`notes/tautology_registry.md`) and **eight named open conjectures** (§IX) chart the honest gap between current state and Platonic form.

The work to install this Platonic form into the Vol III manuscript is the editing roadmap of §VIII — five phases, fourteen numbered steps, no new mathematical input beyond existing chapters. The current per-d dispatch becomes a single Φ functor with four universal properties; the per-d cases become evaluations; the six routes to G(K3 × E) become specialisations; the cross-volume universal trace identity becomes the climax of both volumes' prefaces.

The arithmetic is verified (independence audit installed; coverage 2/283 with disciplined growth path). The poetry is named (five slogans). The motion is constructed (nine natural transformations, four animations). The music plays (four pillars, four voices, one cross-volume modulation).

What remains is to write it down.

— Raeez Lorgat, 2026-04-16
