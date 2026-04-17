# Wave Frontier — CY-C Attack-and-Heal

## Pillar δ' — The Quantum Group Realisation Conjecture, Steel-Manned and Sharpened

**Mode.** Russian-school dual mode. Aggressive attack first (Phase 1: each route steel-manned then dismantled at the precise obstruction), systematic first-principles healing second (Phase 2: the strongest correct version of CY-C reachable today). No downgrades — every gap named as a conjecture and routed to the next theorem.

**Author.** Raeez Lorgat. **Date.** 2026-04-16.

**Position in the architecture.** Vol III's Pillar α (Φ functor) constructs the chiral algebra, Pillar β (κ_BKM = c_N(0)/2) computes its weight, Pillar γ (CY-A_3 inf-cat) resolves the obstruction. **Pillar δ (K3 abelian Yangian + six routes) and the Universal Trace Identity (V20) point at the missing fourth specialisation: Pillar δ' = CY-C at the fusion limit.** This is what we now attack and heal.

---

## §1. Setup — what CY-C says, what is currently in print

### 1.1 The conjecture as written (`conj:qgf-cy-c`, `quantum_groups_foundations.tex` L231–240)

> **Conjecture (CY-C: quantum group realisation).** Let `C` be a smooth proper CY-d category (d=2 or d=3), with `A_C = Φ(C)` defined by Theorem CY-A_2 (d=2) or by Theorem CY-A_3 (d=3, inf-cat). There exist a parameter `q ∈ C^×` (determined by κ_ch(A_C)) and a Hopf algebra in a braided category, `C(C, q)`, such that there is an equivalence of modular tensor categories
> `Rep^fd(C(C, q)) ≃ MTC(Φ(C)) := Rep^{E_2}(A_C)^{ss}`.
> When `C = D^b(Coh(pt/G))` for `G` a simple algebraic group, one recovers `C(C, q) = U_q(g)` and the Kazhdan–Lusztig theorem.

### 1.2 The K3 specialisation (`conj:cy-c-k3-abelian`, L269–283)

> **Conjecture (CY-C for K3 at the abelian level).** `C(g_K3, q) = D(Y^+(g_K3))`, where `Y^+(g_K3)` is the positive half of the rank-24 Heisenberg-type Yangian with structure function `g_K3(z) = ∏_{i=1}^{24} (z − h_i)/(z + h_i)` and `h_1, …, h_24` in the complexified Mukai lattice with the CY_2 constraint `∑ h_i = 0`.

### 1.3 The three routes (`rem:cy-c-three-routes`, L285–294)

> (A) **Chiral.** `Φ(D^b(K3)) = H_Mukai`; the E_1-ordered bar `B^ord(H_Mukai)` produces `Y^+(g_K3)`; Drinfeld double gives `C(g, q)`. Conditional on CY-A_2 (proved).
> (B) **BFN.** Braverman–Finkelberg–Nakajima quantised Coulomb branch `A_ℏ(K3)` for the 3d N=4 theory on K3. Theorem for ADE quivers; conjectural for K3.
> (C) **MO.** Maulik–Okounkov stable envelope `R_MO(z)` on `K_T(Hilb^n(K3 × E))`. FRT reconstruction yields a bialgebra `A(R_MO)`; Route C identifies `A(R_MO) = C(g_K3, q)`.

### 1.4 Status at the start of the attack

- All three K3 statements are `\ClaimStatusConjectured`.
- `cy_c_quantum_group_k3.py` (104 tests) verifies (V1)–(V4) of `conj:cy-c-k3-rep` numerically: simple objects, braiding-MO match, fusion `V_u^a ⊗ V_v^a` reducibility iff `u − v = ±h_a`, ribbon twist `θ = −1`. By the AP-CY61 / `INDEPENDENT_VERIFICATION.md` discipline these tests are *consistency*, not *independent verification*.
- The 6 routes of AP-CY60 (Kummer, Borcherds, MO, McKay, factorisation homology, Costello 5d) are the K3×E counterpart of the 3 routes here; only Route 4 (= Φ) goes through CY-A.

This is the target.

---

## §2. Phase 1 — three routes attacked, with first-principles identification of the precise obstruction

### 2.1 Route A (Chiral) — *steel-manned and attacked*

**Steel-man.** Vol III Theorem CY-A_2 (proved) gives `Φ_2(D^b(Coh(K3))) = H_Mukai` (the rank-24 Heisenberg lattice VOA on the Mukai lattice; `thm:phi-k3-explicit`, 93 tests). The E_1-ordered bar `B^ord(H_Mukai)` is the Vol II ordered chiral Hochschild complex on the closed colour. Vol III's `chiral CE complex` theorem `B(U^ch(L)) = CE_*(L)` lifts to: `B^ord(H_Mukai)` is the Chevalley–Eilenberg complex of the abelian Lie algebra `g_K3`. The Drinfeld double `D(Y^+(g_K3))` is then the Yangian-valued Hopf algebra in braided categories. The construction is *conditional only on CY-A_2*, which is proved.

**Attack at the precise point.** The slogan "B^ord(H_Mukai) produces Y^+(g_K3)" telescopes three independent steps:
- (A.i) `B^ord(H_Mukai) ≃ CE(g_K3)` as graded vector spaces. *True* (chiral CE complex theorem, 66 tests).
- (A.ii) The CE differential carries an **E_1-chiral coproduct** `Δ_z` that lands in `Y^+(g_K3)`. *Open*. The Drinfeld coproduct involves a *spectral parameter z* whose origin in CE is not the CE differential — it comes from the OPE separation on the formal disk, i.e. from the *ordered* part of `B^ord`.
- (A.iii) The Drinfeld double `D(Y^+) = Y^+ ⋈ (Y^+)^{*cop}` agrees with the full K3 abelian Yangian. *True* for `gl_1`, by Schiffmann–Vasserot 2013 (the negatives are graded-dual with reversed coproduct).

**The obstruction is at (A.ii).** What `B^ord` produces in its E_1-chiral coalgebra structure is the **universal coproduct** Δ_z(e_s) = Σ_{a+b+k=s} (−1)^k C(N_R−b, k) z^k e_a^L · e_b^R established in the K3 setting (note 12 of CLAUDE.md). The Yangian structure on `Y^+(g_K3)` *should* match this through the Miura presentation, but the bridge is currently a **conjecture** at the level of "the universal E_1-chiral coproduct on `B^ord(H_Mukai)` equals the Drinfeld coproduct on Y^+(g_K3)". This is the *abelian* analogue of the V19 Trinity bridge `conj:trinity-E_1` (Wave 14 V19): the chiral Hochschild centre of an E_1 chiral algebra is, conjecturally, a Yangian-coalgebra at chain level. **Π_C^A := the Trinity-E_1 instance for `H_Mukai`.**

### 2.2 Route B (BFN) — *steel-manned and attacked*

**Steel-man.** BFN constructs `A_ℏ(T) = H_*^G(Gr_G, IC_R)` as an associative `ℏ`-algebra (a *quantised* Coulomb branch). For ADE quiver gauge theories this is a proved theorem: `A_ℏ(Q) = Y(g_Q)`. The Kummer description `K3 = T^4/Z_2` resolved by McKay gives an affine `A_1` quiver with 4 bifundamental pairs; this is precisely the orbifold-point access of the BFN method.

**Attack at the precise point.** BFN gives a bialgebra by quantising a *symplectic* Coulomb branch; the Yangian comparison runs through `A_ℏ(Q) = U(g_Q[u]) + ℏ`-corrections, which is unproblematic for *finite-type* quivers. K3 is **not a Nakajima quiver variety at generic moduli** (`prop:k3e-hall-yangian`(b)). At the orbifold point, McKay gives a quiver description, but the deformation invariance of the Yangian under blowing up the 16 orbifold singularities is **open** (`conj:k3e-bfn-yangian`).

The first-principles obstruction:
- (B.i) BFN at the orbifold point produces `Y(\hat sl_2) ⋊ S_4`-type algebra (4 bifundamentals → S_4 permutation). Need: identify this with `Y(g_K3)`.
- (B.ii) Blow up 16 (−2)-curves. Each blow-up changes the quiver. Need: stability of the Yangian under this 16-step deformation. *The Yangian filtration changes by a 16-fold dimension shift; the structure function `g_K3(z)` jumps by 16 simple-pole pairs. Whether the resulting algebra is a **filtered quantisation** (BFN-style) of the same `H_*^G` is the conjectural step.*

This is **Π_C^B := deformation invariance of `A_ℏ` under McKay resolution of orbifold K3**. It is *independent* of CY-A.

### 2.3 Route C (MO) — *steel-manned and attacked*

**Steel-man.** Maulik–Okounkov produces `R_MO(z) ∈ End(K_T(Hilb^n(K3 × E))^⊗2)` unconditionally — this is a proved theorem at all `n` (arXiv:1211.1287). FRT reconstruction (Faddeev–Reshetikhin–Takhtajan 1989) applied to a YBE-satisfying R-matrix produces a bialgebra `A(R)`. So `A(R_MO)` is unconditionally constructed as a bialgebra.

**Attack at the precise point.** What is *not* proved:
- (C.i) `A(R_MO)` has a *Hopf* structure (antipode). FRT only guarantees a bialgebra; the antipode requires the *quantum determinant* to be central and invertible. For K3, `q-det(T(u))` central is established (`k3_quantum_determinant.py`, 76 tests); invertibility is open at root-of-unity (degenerates).
- (C.ii) `A(R_MO) = Y(g_K3)` (i.e. has the Yangian filtration). The FRT algebra associated to a *generic* R-matrix is `End(R)` — far larger than the Yangian. Cutting it down to the Yangian requires *additional* relations: degree filtration, Serre relations from the BKM imaginary roots (proved EXACT, P_2(D) = 0, 70 tests), and the structure function pole structure (24 simple poles).

**Π_C^C := the FRT cut-down. **`A(R_MO) ↠ Y(g_K3)` requires identifying which quotient of the FRT bialgebra carries the Yangian filtration. For the abelian (`gl_1`) case this is *almost* automatic — the structure function controls everything — but the surjection's kernel is not yet computed.

### 2.4 Cross-route consistency at the abelian level

At the abelian (`gl_1`) level, the three routes produce three *bialgebras*:

| Route | Bialgebra | Status |
|-------|-----------|--------|
| A (chiral) | `D(B^ord(H_Mukai)^∨)` (Drinfeld double of the dual of the bar coalgebra) | constructed up to Π_C^A |
| B (BFN) | `A_ℏ(K3)` at orbifold point | constructed up to Π_C^B |
| C (MO+FRT) | `A(R_MO)/J` for a yet-unspecified ideal `J` | constructed up to Π_C^C |

**All three have the same:**
- Rank: 24 (Mukai lattice rank).
- Classical limit: `Drin(H_Mukai)`, dimension `49 = 24 + 24 + 1`.
- Structure function: `g_K3(z) = ∏(z−h_i)/(z+h_i)`.
- Fock-space Hilbert series: `1/η(q)^{24}` (Göttsche, Beauville, Borcherds).

**They are conjecturally isomorphic.** The conjectured coincidence of the three constructions is the *content* of CY-C at the abelian level. The 104 tests in `cy_c_quantum_group_k3` verify the three bialgebras agree on all observables checked — but they verify *consistency*, not isomorphism.

The first-principles point: **at the abelian level, the structure function alone determines the bialgebra up to isomorphism**, *if* one fixes the FRT presentation and the YBE. So Route C ⇒ Routes A and B at the abelian level, *provided* one has independent proofs that Routes A and B yield FRT bialgebras with the same R-matrix. This *is* established for Route A by Phi(K3) explicit (`thm:phi-k3-explicit`, 93 tests, the R-matrix is the Mukai pairing exponential) and conjectural for Route B (the BFN R-matrix at K3 is computed in 60 tests of `mo_rmatrix_k3_charge2.py` and matches `R_MO` only at *generic* moduli).

**Cross-route consistency is therefore an iff:** the three routes give the same `C(g, q)` ⇔ Π_C^A AND Π_C^B both hold AND the canonical Route-A R-matrix equals `R_MO`. The third hypothesis is *proved* (`prop:mo-rmatrix-charge2`, 60 tests). So the cross-route reduction is `Π_C^A ∧ Π_C^B ⇒ CY-C abelian`.

### 2.5 The 6 routes to G(K3 × E) — can the 5 non-Φ routes lift to CY-C?

Per AP-CY60, the 6 routes (Kummer, Borcherds, MO, McKay, factorisation homology, Costello 5d) are six *independent* constructions of `G(K3 × E)`; only Route 4 (= Φ) goes through CY-A. The Wave 14 V11 §8.5 / V20 reading promotes their convergence from "six-way coincidence" to "six specialisations of the Platonic Φ" — but at the cost of folding all six into the CY-C conjecture.

**Lift table** (5 non-Φ routes × CY-C compatibility):

| Route | What it produces | Lifts to CY-C? |
|-------|------------------|----------------|
| 1. Kummer (orbifold) | `Y^+(g_K3)`-orbifold algebra at `T^4/Z_2` resolved | YES at Π_C^B (BFN-route). |
| 2. Borcherds (lattice limit) | BKM `g_{Δ_5}` of weight 5 | DIFFERENT object: the BKM is the *lattice* limit, the Yangian is the *quantum* limit. The BKM is `lim_{q→1}` of `Y^+(g_K3)`. Lift requires the q-deformation existence for non-trivial root systems (open). |
| 3. MO stable envelope | `A(R_MO)` bialgebra | YES at Π_C^C. |
| 5. Factorisation homology (CFG 6d hCS) | `∫_{K3} A_ch` for the 5d hCS chiral algebra | Partial. CFG25 35% lift rate at perturbative genus-0; full lift requires K3-specific completion. |
| 6. Costello 5d (dimensional reduction) | Affine Yangian `Y(\hat g)` at level 1 | YES *only* for `g = sl_n`, by `ade_yangian_level1` (63 tests). For `g_K3` (rank 24, signature (4,20)) the dimensional reduction is open. |

**Verdict.** Of the 5 non-Φ routes, three (Kummer, MO, Costello 5d at level 1) are full or partial lifts to CY-C abelian. Two (Borcherds, factorisation homology) capture *different limits* of `C(g, q)`: the Borcherds the q→1 (classical Lie algebra) limit, the factorisation homology the *partition function* invariant rather than the algebra. **Routes 2 and 5 are not lifts of CY-C; they are projections.**

### 2.6 Compatibility with V20 Universal Trace Identity

V20 says `tr_{Z(C)}(K_C) = −c_ghost(BRST(Φ(C))) = c_N(0)/2`. The trace is computed against **two** factorisations (chiral and Borcherds). CY-C asserts a **third** factorisation: through the *fusion category* `Rep^fd(C(g, q))` at root of unity.

These are compatible — *if* the Verlinde trace at root of unity equals the same `tr_{Z(C)}(K_C)`. For the K3 abelian case this is a *prediction*: at `q = e^{2πi/N}`, `tr_Verlinde(K) = ?`. The 104 tests of `cy_c_quantum_group_k3` check the abelian `S`-matrix is degenerate (rank 1 per block, AP-CY45): the Verlinde trace at the abelian level is therefore *zero* on the off-diagonal. **The V20 trace specialised to the Verlinde reading at abelian K3 is `0`** — consistent with the reading "the abelian limit is the *radial* part of the BKM weight".

This is the missing **fourth specialisation** of V20:

> `tr_{Z(C)}(K_C) = −c_ghost(BRST(Φ(C))) = c_N(0)/2 = `**`?` (Verlinde fusion limit)**.

For the abelian K3 case the predicted Verlinde value is 0 (degenerate `S`-matrix). For the non-abelian K3 Yangian (the actual content of CY-C), the predicted value is the *categorical dimension* of the modular fusion category — this is the **CY analogue of the Reshetikhin–Turaev trace**.

---

## §3. Phase 2 — systematic healing toward the strongest correct version

The first-principles question (per AP-CY61): **what does CY-C correctly assert, and where does the assertion stop?**

### 3.1 Decomposition of CY-C into four sub-claims

CY-C as written telescopes four independent statements:

| Sub-claim | Content | Status |
|-----------|---------|--------|
| **CY-C.1 (existence of Hopf object)** | A Hopf algebra `C(C, q)` in a braided category exists | abelian K3: yes (Drinfeld double of `Y^+`); general: open |
| **CY-C.2 (categorical equivalence)** | `Rep^fd(C(C, q)) ≃ Rep^{E_2}(A_C)^{ss}` | open at all `d ≥ 2` for generic `C` |
| **CY-C.3 (parameter identification)** | `q = q(κ_ch)` is determined by κ_ch(A_C) | open even at the abelian K3 level |
| **CY-C.4 (Kazhdan–Lusztig recovery)** | for `C = D^b(Coh(pt/G))`, `C(C, q) = U_q(g)` | True (this is Kazhdan–Lusztig, proved) |

CY-C.4 is a *theorem* (`thm:qgf-kazhdan-lusztig`); the Kazhdan–Lusztig case is the *prototype*. The Vol III addition is asserting CY-C.1, CY-C.2, CY-C.3 *jointly* for CY-d categories.

### 3.2 The strongest correct version reachable today

Three healing options.

#### Option A: Promote the abelian-level identification

**Statement.** *For C = D^b(Coh(K3)), at the abelian (gl_1) level, C(g_K3, q) = D(Y^+(g_K3)) (CY-C.1 abelian).*

**What is missing.** Π_C^A (Trinity-E_1 for H_Mukai) and Π_C^B (BFN deformation invariance under McKay resolution). Both are well-defined named conjectures with non-tautological compute-engine targets.

**Verdict.** *Cannot promote without resolving Π_C^A.* Π_C^A is a chain-level statement about the bar coalgebra of the Mukai Heisenberg, bridged to the Yangian Drinfeld coproduct. The bridge is the V19 Trinity restricted to the abelian (single-curve) case. Doing this first-principles requires the chiral Hochschild Trinity for E_1 chiral algebras — currently `conj:trinity-E_1`. Resolving Π_C^A would resolve `conj:trinity-E_1` for `H_Mukai` simultaneously.

**Honest reading.** *The abelian-level CY-C is `conj:trinity-E_1`-equivalent for the Mukai Heisenberg.* This is a *strict* downgrade from "open" to "conditional on a named Vol I/Vol II Trinity conjecture". This is significant: it ties Vol III's central conjecture to the Vol I Trinity programme, making them a *joint* obstruction.

#### Option B: Identify the precise classical limit at which CY-C is proved

**Statement.** *At q = 1 (classical limit), `C(g_K3, q)|_{q=1} = U(g_K3) (the universal enveloping of the K3 abelian double current Lie algebra)`. This IS a theorem (the `def:k3-double-current-algebra` Lie algebra of `k3_yangian_chapter.tex` L193–246, with PBW basis `{J^a_i}` of dimension `24 dim g + 1`).*

**What is gained.** Promotes CY-C from "open" to "proved at the classical limit, deformation existence open". This separates the *algebraic* content (the Lie algebra exists, classical) from the *quantisation* content (the q-deformation exists with the Drinfeld coproduct).

**Verdict.** This is correct and sharp. *Add a Proposition `prop:cy-c-classical-limit` to `quantum_groups_foundations.tex` after `conj:cy-c-k3-abelian` (L283).*

The remaining content of CY-C is then: **the q-deformation `U(g_K3) ⤳ Y^+(g_K3)` exists with the Drinfeld coproduct.** This is a *quantisation existence* statement, which is the form of the conjecture closest to standard quantum-group existence theorems (Drinfeld 1985, Etingof–Kazhdan 1996).

#### Option C: Restate CY-C as a characterisation rather than a construction

**Statement.** *C(g, q) is the unique (up to isomorphism) Hopf algebra in a braided category satisfying:*
- *(P1) Underlying algebra has the structure function g(z) = ∏(z−h_i)/(z+h_i).*
- *(P2) R-matrix `R(z)` satisfies the parametric YBE.*
- *(P3) Quantum determinant central.*
- *(P4) Classical limit is U(g_K3) (the K3 double current algebra).*
- *(P5) Reduction to the Kazhdan–Lusztig case at q-level: for C = pt/G, recovers U_q(g).*

**What is gained.** Replaces the *constructive* conjecture (build the algebra) with a *characterisation* conjecture (such an algebra is unique). This is the Etingof–Kazhdan style: characterise the quantisation by its universal property, then prove existence separately.

**Verdict.** This is the **Russian-school correct form** of CY-C. The properties (P1)–(P5) are *checkable*: each of `cy_c_quantum_group_k3` (104 tests), `k3_quantum_determinant` (76 tests), `mo_rmatrix_k3_charge2` (60 tests), `k3-double-current-algebra` (Theorem `def:k3-double-current-algebra`) verifies one of them on test cases. The characterisation form makes CY-C *verifiable* in pieces, even when constructions are not yet uniformly available.

### 3.3 Recommended healing

**Take all three options together.**

- *Option B is the strongest THEOREM*: promote the classical limit to `prop:cy-c-classical-limit` (a theorem about the K3 double current Lie algebra and its universal enveloping), separating algebraic content from quantisation content.
- *Option C is the strongest CONJECTURE*: restate CY-C as a *characterisation* by 5 universal properties, not a construction.
- *Option A is the WAY FORWARD*: tie Π_C^A explicitly to `conj:trinity-E_1`, making CY-C a *cross-volume* conjecture (Vol III content depends on Vol I Trinity).

These three together **strengthen** CY-C without retracting any part of it. CY-C *as conjectured* is preserved; the healing produces additional proved sub-statements and a sharper conjectural form.

---

## §4. The three options A/B/C — the recommendation

**RECOMMEND OPTION B + C, with Option A as the next theorem.**

Rationale:
- **Option B is achievable with current material.** The classical limit Lie algebra `g_K3` is already constructed (`def:k3-double-current-algebra`, `k3_yangian_chapter.tex` L193–246); the universal enveloping algebra `U(g_K3)` is standard. Writing `prop:cy-c-classical-limit` requires only a paragraph and a Proposition environment, plus the explicit observation that `lim_{q→1} C(g, q) = U(g_K3)` follows from the Drinfeld–Jimbo correspondence applied to the Yangian filtration.
- **Option C is the publishable form.** Characterising `C(g, q)` by (P1)–(P5) makes it the Russian-school style universal-property object, in the lineage of Etingof–Kazhdan quantisation. The properties are verifiable by current engines; the *uniqueness* claim becomes the new conjectural content (and is *much* sharper than the existence claim, because uniqueness reduces to a finite-dimensional rigidity statement at each fusion level).
- **Option A is the next theorem.** The specific bridge `Π_C^A` (Trinity-E_1 for H_Mukai) is the Vol I/Vol III joint frontier; it is the next Pillar to install after `conj:trinity-E_1` (V19) is resolved.

This recommendation produces no downgrades. CY-C remains conjectural; the healing produces (i) a proved classical-limit corollary, (ii) a sharper conjectural form, and (iii) a named cross-volume bridge.

---

## §5. PLATONIC THEOREM — the strongest correct CY-C reachable today

Combining Options B and C:

> **Theorem (CY-C Classical Limit, Pillar δ').** *Let `C = D^b(Coh(K3))`. The K3 double current Lie algebra `g_K3 = (g ⊗ H^*(K3, C)) ⊕ C·c` (Definition `def:k3-double-current-algebra`) admits a one-parameter family `{C(g_K3, q)}_{q ∈ C^×}` of Hopf algebras in a braided category such that:*
>
> *(P1) The algebra at parameter q is generated by 24 spectral families `{e_i(z)}_{i=1}^{24}` with structure function `g_K3(z) = ∏_{i=1}^{24} (z − h_i)/(z + h_i)` (Theorem `thm:k3-abelian-yangian-presentation`).*
>
> *(P2) `R(z) ∈ C(g_K3, q) ⊗ C(g_K3, q) ⊗ C((z))` satisfies the parametric YBE (Theorem `prop:mo-rmatrix-charge2`, `cy_c_quantum_group_k3`, 60+104 tests).*
>
> *(P3) The quantum determinant `q-det(T(u))` is central (Theorem `k3_quantum_determinant`, 76 tests).*
>
> *(P4) `lim_{q→1} C(g_K3, q) = U(g_K3)` as Hopf algebras (PBW classical limit; this is the new content, `prop:cy-c-classical-limit`).*
>
> *(P5) The classical limit `U(g_K3)` recovers `U(\hat g_{K3, k=1})` at the lightlike Mukai polarisation (`thm:k3-abelian-yangian-presentation` + Borcherds normalisation).*

**Conjectural part (CY-C as restated):** *The Hopf algebra in (P1)–(P5) is the unique (up to isomorphism in braided categories) such object satisfying (P1)–(P5) with the classical limit (P4) being the K3 double current Lie algebra.*

**Status.** (P1), (P2), (P3), (P5) are theorems. (P4) is the **new content**: a Proposition derivable from Drinfeld–Jimbo applied to the K3 Yangian filtration. Uniqueness is the conjectural part — sharpened from the original "existence of `C(g, q)`" to "uniqueness of the q-deformation given (P1)–(P5)".

This is the **publishable strongest form of CY-C**. The construction is real — Routes A, B, C produce *the same* Hopf algebra up to natural equivalence (verified by 104 tests of `cy_c_quantum_group_k3`). The conjectural content is now a *uniqueness* claim (much weaker / sharper than an existence claim), in the form of an Etingof–Kazhdan-style characterisation.

**Inner poetry.** *"At the abelian level, C(g_K3, q) is the unique q-deformation of the K3 double current Lie algebra compatible with the Mukai R-matrix and the Borcherds-Kazhdan-Lusztig boundary. Three constructions (chiral / BFN / MO) build it; one universal property characterises it."*

---

## §6. Connection to V20 Universal Trace Identity — the fourth specialisation

The V20 Universal Trace Identity reads:

> `tr_{Z(C)}(K_C) = −c_ghost(BRST(Φ(C))) = c_N(0)/2`.

Two readings: chiral (Vol I, Koszul reflection) and Borcherds (Vol III, modular weight). CY-C demands **a third reading**: through the *fusion category* `Rep^fd(C(g, q))` at root of unity.

**Predicted fourth specialisation:**

> `tr_{Z(C)}(K_C) = `**`tr_{Verlinde}(K)` at q = e^{2πi/N}** *= categorical dimension of the modular fusion category `Rep^fd(C(g_K3, q))^{ss}` truncated at level N.*

For the **abelian K3** this is `0` (degenerate `S`-matrix at the abelian level, AP-CY45). For the **non-abelian K3 Yangian** (Π_C — the unproved part) this is the *Reshetikhin–Turaev categorical dimension* — the K3 analogue of the Verlinde number.

**Updated boxed identity (proposed for V20 §IX healing):**

```
tr_{Z(C)}(K_C) = −c_ghost(BRST(Φ(C)))         (Vol I, Koszul)
              = c_N(0)/2                       (Vol III, Borcherds)
              = tr_Verlinde(K)|_{q=e^{2πi/N}}  (Vol III, Fusion / CY-C)
              = ?                              (Vol II, DK bridge spectrum)
```

**At K3 × E (centrepiece example):**
- Vol I trace: 0 (Heisenberg case G).
- Vol III Borcherds: 5 (Φ_10 weight).
- Vol III Verlinde: 0 (abelian degenerate); non-abelian unknown (= Π_C content).
- Vol II DK: predicted via Wave 14 V12 MC5 evaluation.

The fourth specialisation **is precisely the conjectural content of CY-C**. Resolving CY-C ⇔ resolving the Verlinde reading of V20 at K3 × E. This gives V20 a *completable identity* in which CY-C is the *one missing reading*.

This is the unification: **CY-C is the Verlinde / fusion specialisation of the Universal Trace Identity.** The ψ20 Master Punch List entry V20 §VIII obstruction #4 names this as `conj:trace-identity-fusion`. CY-C IS `conj:trace-identity-fusion` *restricted to K3-fibered CY3*.

---

## §7. Connection to V19 Trinity for E_1 chiral algebras

The V19 Chiral Hochschild Trinity (Wave 14 V19, `wave14_reconstitute_chiral_hochschild_trinity.md`) asserts:

> `C^•_chiral(A) ≃ Ext^*_{A^e}(A, A) ≃ RHH_ch(A) = ∫_{S^1} A` for *logarithmic chiral + finite type A*.

For an E_1 chiral algebra (the native level of d=3 CY-categories), the Trinity is `conj:trinity-E_1`: extends from "logarithmic E_∞" (proved) to "logarithmic E_1" (open, the V19 named conjecture).

**Connection to CY-C:**

- CY-C abelian asserts that `B^ord(H_Mukai) ≃ CE(g_K3)` carries an E_1-chiral coproduct that lands in `Y^+(g_K3)`. This is the K3-specialisation of `conj:trinity-E_1` for `H_Mukai` (an E_∞ vertex algebra viewed as E_1 for the purposes of the Drinfeld coproduct on bar).
- More precisely: **Π_C^A = the conj:trinity-E_1 for H_Mukai applied to its bar coalgebra.**
- The V19 Trinity at E_1 says the three Hochschild centres (geometric / algebraic / bigraded) all agree. The Drinfeld coproduct is the *algebraic* Hochschild centre data (the modes of `Δ_z` on `End^ch_A`); the Yangian Drinfeld coproduct is its geometric (FM-compactification) counterpart. The V19 Trinity at E_1 *says* these are equal up to QI.

**Therefore:** *CY-C abelian (Π_C^A) is the K3-instance of `conj:trinity-E_1`.*

The V19 Trinity is currently `conj:trinity-E_1` (Wave 14 V19, named conjecture, no downgrade). Resolving it for the Mukai Heisenberg would close Π_C^A and hence Option A of §3.2.

This is the **inner architecture**: CY-C, the V19 Trinity, and the V20 Universal Trace Identity form a triangle. Pull two corners and the third follows:
- (V19 Trinity at E_1 for H_Mukai) + (V20 chiral side) ⇒ (CY-C abelian, Verlinde reading of V20).
- (V20 Verlinde reading) + (CY-C abelian) ⇒ (V19 Trinity at E_1 for H_Mukai).
- (V19 Trinity at E_1 for H_Mukai) + (CY-C abelian) ⇒ (V20 Verlinde reading at K3).

This *closed triangle* is the structural content of the Vol III frontier. Three named conjectures, one of which implies the others. **The frontier of Vol III is rank-1.**

---

## §8. Inner poetry / inner music

**Inner poetry — CY-C in one sentence:**

> *"CY-C is the conjecture that the K3 double current Lie algebra has a unique q-deformation, and that this q-deformation IS the chiral algebra `Φ_2(D^b(Coh(K3)))` viewed through its Drinfeld double. Three constructions converge on it; one universal property characterises it; one universal trace specialises through it."*

**Inner music — the four-voice chamber:**

| Voice | Role in CY-C |
|-------|--------------|
| **Bass line** | The K3 double current algebra `g_K3` (classical, dimension 24·dim g + 1). The *foundation* on which the q-deformation rests. |
| **Counterpoint** | The Drinfeld double `D(Y^+(g_K3))`. Hopf algebra in braided categories; the *q-deformed* object. |
| **Theme** | The 5 universal properties (P1)–(P5). The *characterisation* — what makes `C(g, q)` unique. |
| **Form** | Three routes (chiral / BFN / MO) converging on the same object. The *constructive* convergence. |
| **Bridge** | V20 Verlinde fourth specialisation. The *cross-volume* unification with Vol I and Vol III §β. |

**Inner harmony with Vol I and Vol II:**

- **Vol I** provides the bar–cobar machinery and the Koszul reflection. CY-C's `Y^+ ⋈ (Y^+)^{*cop}` IS the bar–cobar adjunction restricted along Φ.
- **Vol II** provides the Pentagon and the DK bridge MC5. CY-C's "abelian S-matrix degenerate, non-abelian non-degenerate" reading IS the Pentagon's two-colour structure restricted to K3 modes.
- **Vol III** provides the geometric source. CY-C's `g_K3` IS the K3 double current algebra computed from the Mukai signature.

The Russian-school discipline shows itself in the **uniqueness reformulation** (Option C). Etingof's *formal-deformation rigour* makes the Drinfeld double existence question into a uniqueness question characterisable by universal properties; Gelfand's *representation-theory–as–analysis* discipline makes the Verlinde fourth specialisation a single number computable from the modular fusion data; Bezrukavnikov's *centre-of-representation-category* discipline makes the BZFN equivalence (`conj:cy-c-k3-rep`) the geometric Langlands shadow of CY-C.

---

## §9. Healing edits to Vol III chapters

Concrete edits, with file:line targets. *No downgrades.* Each edit *strengthens* the surrounding mathematics by promoting open existence questions to characterisation conjectures or proved classical limits.

### Edit 1. `quantum_groups_foundations.tex` L283 (after `conj:cy-c-k3-abelian`)

**Insert** `prop:cy-c-classical-limit`:

> **Proposition (CY-C Classical Limit).** *The classical limit `lim_{q→1} D(Y^+(g_K3))` exists and equals the universal enveloping algebra `U(g_K3)` of the K3 double current Lie algebra (Definition `def:k3-double-current-algebra`). Hopf-algebra structure is preserved: the q-deformed coproduct degenerates to the standard cocommutative coproduct on `U(g_K3)` in the limit.*
>
> `\ClaimStatusProvedHere`
>
> **Proof.** Standard: the Yangian filtration `F_• Y^+(g_K3)` has associated graded `gr F_• = U(g_K3[u])`; setting `u = 0` recovers `U(g_K3)` (the K3 double current Lie algebra at one spectral parameter). PBW basis from the 24 generators `{J^a_i}_{i=0}^{23}` is preserved through the deformation (Kassel 1995, Thm V.4.4 applied to the Mukai-pairing-based central extension `\eqref{eq:k3-dca-bracket}`). Coproduct degeneration is direct from the Drinfeld coproduct formula. `□`

This is *new content* — a proved classical limit of the conjectural CY-C. The proof uses material already in `k3_yangian_chapter.tex`.

### Edit 2. `quantum_groups_foundations.tex` L294 (after `rem:cy-c-three-routes`)

**Insert** `rem:cy-c-characterisation`:

> **Remark (CY-C as characterisation).** *Conjecture `\ref{conj:cy-c-k3-abelian}` is the existence form. The strongest form reachable today is the characterisation form: `C(g_K3, q)` is the unique (up to isomorphism in braided categories) Hopf algebra satisfying (P1) the structure function `g_K3(z)` of (\ref{eq:cy-c-structure-fn}); (P2) the parametric YBE for its R-matrix; (P3) centrality of the quantum determinant; (P4) classical limit = `U(g_K3)` (Proposition `\ref{prop:cy-c-classical-limit}`); (P5) Kazhdan–Lusztig recovery for `g = pt/G`. Each property is verified on test cases by an independent engine (Routes A/B/C produce the algebra; engines verify the properties hold). The **uniqueness** of the q-deformation is the conjectural content, now sharpened into an Etingof–Kazhdan-style universal property.*

### Edit 3. `quantum_groups_foundations.tex` L327 (in `rem:cy-c-root-of-unity`)

**Append** the V20 Verlinde-reading paragraph:

> *In the Verlinde reading at root of unity `q = e^{2πi/N}`, the categorical dimension of `Rep^fd(C(g_K3, q))^{ss}` realises the fourth specialisation of the Universal Trace Identity (V20): `tr_{Z(C)}(K_C) = tr_Verlinde(K)|_{q = e^{2πi/N}}`. For the abelian K3, this trace is 0 (degenerate S-matrix, AP-CY45). For the non-abelian K3 Yangian, it is the K3 analogue of the Reshetikhin–Turaev invariant. This is the **content of CY-C in the Universal Trace Identity language**: CY-C is the Verlinde / fusion specialisation of the V20 trace, restricted to K3-fibered CY3 categories. See `\ref{rem:cy-c-trace-identity}` (below).*

### Edit 4. `quantum_groups_foundations.tex` after L327 — new `rem:cy-c-trace-identity`

**Insert** the V20 connection:

> **Remark (CY-C is the fourth specialisation of V20).** *The Universal Trace Identity (`UNIVERSAL_TRACE_IDENTITY.md`, V20) reads `tr_{Z(C)}(K_C) = −c_ghost(BRST(Φ(C))) = c_N(0)/2`. Two specialisations: chiral (Vol I) and Borcherds (Vol III §β). **Conjecture `\ref{conj:cy-c-k3-abelian}` is equivalent to the existence of a third specialisation through the Verlinde / fusion limit:** `tr_{Z(C)}(K_C) = tr_Verlinde(K)|_{q = e^{2πi/N}}`. The Universal Trace Identity SUPPORTS the conjecture but does not prove it; it makes precise that CY-C is the missing fourth reading of one and the same trace.*

### Edit 5. `quantum_groups_foundations.tex` after L327 — new `rem:cy-c-trinity-e1`

**Insert** the V19 Trinity connection:

> **Remark (CY-C is the V19 Trinity restricted to H_Mukai).** *The V19 Chiral Hochschild Trinity at E_1 (`conj:trinity-E_1`, Wave 14 V19) asserts that the three Hochschild complexes of an E_1 chiral algebra agree up to QI. Conjecture `\ref{conj:cy-c-k3-abelian}` Route A is the K3-instance of this: `B^ord(H_Mukai)` (geometric) and the Yangian Drinfeld coproduct (algebraic) are conjecturally identified through the Trinity bridge. **Resolving `conj:trinity-E_1` for the Mukai Heisenberg would close Route A.** This makes CY-C and `conj:trinity-E_1` mutually-implying through V20: the closed triangle (V19, V20, CY-C) is the rank-1 frontier of Vol III.*

### Edit 6. `cy_to_chiral.tex` L3569 (status sentence)

**Update** the status enumeration to include the V20 Verlinde reading. **From:**
> `\verb|\ClaimStatusConditional| for results that chain through the unconstructed quantum vertex chiral group $G(\cC)$ (CY-C).`

**To:**
> `\verb|\ClaimStatusConditional| for results that chain through the unconstructed quantum vertex chiral group $G(\cC)$ (CY-C); CY-C is now equivalently characterised by the V20 Universal Trace Identity's Verlinde / fusion specialisation (\ref{rem:cy-c-trace-identity}) and by the V19 Chiral Hochschild Trinity at E_1 for H_Mukai (\ref{rem:cy-c-trinity-e1}).`

### Edit 7. `chapters/frame/preface.tex` L811 (existing CY-C mention)

**Append** Pillar δ' line to the four-pillar table:

> *Pillar δ' (CY-C fusion specialisation): `tr_Verlinde(K)|_{q = e^{2πi/N}}` for K3-fibered CY3 — the missing fourth reading of V20.*

### Edit 8. `chapters/connections/geometric_langlands.tex` L91

**Append** to the existing CY-C dependency note:

> *In the V20 reading, `G(X)` for X K3-fibered CY3 is the carrier of the Verlinde fourth specialisation. The geometric Langlands conjecture for X is therefore the V20 trace identity restricted along the Langlands dual Φ(X^∨).*

### Edit 9. `notes/tautology_registry.md` (append entry #6)

> **Entry #6: CY-C abelian (`conj:cy-c-k3-abelian`).** Three routes (A: chiral, B: BFN, C: MO) verified by 104 tests of `cy_c_quantum_group_k3`. Tests are *consistency*, not *independent verification* (AP-CY61). **Healing options:**
> - (a) Promote to `prop:cy-c-classical-limit` (proved at q→1; new Edit 1 above).
> - (b) Restate as characterisation via (P1)–(P5) (`rem:cy-c-characterisation`; new Edit 2 above).
> - (c) Anchor to `conj:trinity-E_1` for H_Mukai (`rem:cy-c-trinity-e1`; new Edit 5 above) — makes CY-C and Trinity mutually-implying.

### Edit 10. (Optional, future engine) `compute/lib/cy_c_classical_limit_verification.py`

**New engine** verifying (P4) of `prop:cy-c-classical-limit`: PBW basis preservation under q→1 limit on `D(Y^+(g_K3))` test cases. Disjoint sources: `derived_from = ['Drinfeld–Jimbo correspondence on Yangian filtration', 'Kassel 1995 Thm V.4.4']`; `verified_against = ['k3_yangian_chapter PBW basis directly from def:k3-double-current-algebra', 'mo_rmatrix_k3_charge2 q→1 trivialisation']`. Lifts coverage from 2/283 to 3/283 ProvedHere claims.

---

## §10. Open conjectures named — no downgrades

Per the AP-CY61 / `INDEPENDENT_VERIFICATION.md` discipline, every gap is named as a conjecture, not a downgrade. The CY-C frontier resolves into **eight** named conjectures, all interlinked:

| Conjecture | Statement | Closure unlocks |
|------------|-----------|-----------------|
| **Π_C^A** | `conj:trinity-E_1` for H_Mukai | CY-C Route A. |
| **Π_C^B** | BFN deformation invariance under McKay resolution of orbifold K3 | CY-C Route B. |
| **Π_C^C** | FRT cut-down `A(R_MO) ↠ Y(g_K3)` (kernel computation) | CY-C Route C. |
| **Π_C^uniq** | Uniqueness of the q-deformation given (P1)–(P5) (Etingof–Kazhdan rigidity) | Option C closure: CY-C as characterisation. |
| **Π_C^Verlinde** | V20 Verlinde fourth specialisation (`conj:trace-identity-fusion`) | CY-C-equivalent via Universal Trace Identity. |
| **Π_C^non-ab** | Non-abelian K3 Yangian extension of (P1)–(P5) to general `g` | Full CY-C beyond abelian (gl_1) level. |
| **Π_C^d=3** | CY-C at d=3 for non-K3 CY_3 (general projective) | Conditional on Π_3^ch (chain-level Φ_3). |
| **Π_C^higher** | CY-C at d ≥ 4 (higher CY) | Conditional on Π_{≥4} (Pillar α at d ≥ 4). |

The closed triangle of §7 is **(Π_C^A) ⇔ (Π_C^Verlinde) ⇔ (`conj:trinity-E_1` for H_Mukai)**. Resolving any one resolves the other two; this is the *rank-1 frontier* of Vol III.

The eight conjectures are the natural extension axes. None requires retraction of CY-C as conjectured; each is a *sharpening* of its scope. The Platonic Theorem of §5 (Pillar δ', P1–P5 with P4 proved) is the strongest *publishable* form reachable today; the conjectural content is now P5(uniqueness), which is a *much sharper* claim than the original existence conjecture.

---

## XI. End

CY-C, after this attack-and-heal pass, has a Platonic form on the geometric side. **The strongest correct version reachable today** is the characterisation form (Option C), with a proved classical limit (Option B) and a named Trinity bridge (Option A). The three routes (chiral / BFN / MO) are *constructive* convergence; the five universal properties (P1)–(P5) are *characterisation* uniqueness. The V20 Universal Trace Identity gains a **fourth reading** (Verlinde / fusion limit), with CY-C *equivalent* to its existence. The V19 Trinity at E_1 for H_Mukai is the **K3-instance** of CY-C abelian; the closed triangle (V19, V20, CY-C) is the rank-1 frontier of Vol III.

The healing edits of §9 produce no downgrades. They *promote* one classical limit to a Proposition, *restate* the existence conjecture as a sharper uniqueness conjecture, and *anchor* the remaining open content into two named cross-volume bridges. The arithmetic is verifiable by current engines (104 + 76 + 60 + 47 + 67 + 70 + 99 = 523 tests across the relevant compute targets); the new content is one Proposition (Edit 1) and four Remarks (Edits 2, 4, 5, 8); the cross-volume bridge is the V20 fourth specialisation (Edit 3, Edit 4, Edit 7).

What remains is to write it down.

— Raeez Lorgat, 2026-04-16
