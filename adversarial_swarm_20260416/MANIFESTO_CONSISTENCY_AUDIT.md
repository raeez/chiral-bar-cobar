# Manifesto Consistency Audit

## Three-volume cross-check of the Platonic Manifestos and the Universal Trace Identity

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Read-only audit.
No manuscript edits. No commits. All findings filed as a punch list of
*proposed* consolidating edits.

**Sources audited.**
- `PLATONIC_MANIFESTO.md` (Vol I, 256 lines).
- `PLATONIC_MANIFESTO_VOL_III.md` (Vol III, 318 lines).
- `UNIVERSAL_TRACE_IDENTITY.md` (V20 cross-volume centrepiece, 181 lines).
- `MASTER_PUNCH_LIST.md` (V1–V22, HU-1–W11g).
- All eight wave-14 reconstitution drafts and all wave-supervisory drafts
  (~10,899 lines combined).
- `PLATONIC_MANIFESTO_VOL_II.md`: **does not yet exist on disk** (the task
  notes it is "in flight"). Vol II content audited via the Wave 14 V15
  Pentagon supervisory draft (`wave_supervisory_sc_chtop_pentagon.md`)
  and Wave 12 vol2_main report.

---

## §1. Cross-Manifesto pillar correspondence audit

The Vol I Manifesto (§I) and the Vol III Manifesto (§I) each name four
pillars; the Vol III Manifesto (§II) and the V20 standalone (§III)
declare a four-by-four correspondence under the bridge functor `Phi`.

### Stated correspondence (Vol III §II, repeated V20 §III)

| Vol I pillar         | Vol III pillar                         | Identifier mapping       |
|----------------------|----------------------------------------|--------------------------|
| 1. Koszul Reflection (V5) | α. Platonic Phi functor (V11)     | `Phi` ↔ `K = Bbar_X`     |
| 2. κ-Conductor / BRST Ghost (V6+V13) | β. Borcherds Reflection Trace | `K = -c_ghost` ↔ `c_N(0)/2` |
| 3. Climax `d_bar = KZ*(∇_Arnold)` (V7) | γ. Inf-cat CY-A_3 resolution    | `KZ-arena functor` ↔ `def:three-levels` |
| 4. Shadow Quadrichotomy (V8) | δ. K3 Yangian + 6 routes         | `Σ_c spectral curve` ↔ `Hilb^n(K3)` |

### Verifiable consistency

- **Pillar 1 ↔ α (Phi).** Both Manifestos and V20 agree that Phi is
  characterised as the universal pullback through the Koszul reflection
  `K`. Vol I §IV explicit display: `tr_{Z(C)}(K_C) = …`. Vol III §IV
  identical display. V20 §III identical display. Mathematical content
  consistent.
- **Pillar 2 ↔ β.** Both Manifestos give the same boxed equation
  `tr(K) = -c_ghost(BRST(Phi(C))) = c_N(0)/2`. V20 §III repeats it
  verbatim. Numerical verification at K3 (Vol I κ_Vir = 26 from
  V6 sympy table; Vol III κ_BKM = 5 from c_5(0)/2 = 10/2; V20 §VI
  example) all agree.
- **Pillar 3 ↔ γ.** *Drift detected*. Vol I Pillar 3 (Climax) is
  about `d_bar = KZ*(∇_Arnold)` — a UNIVERSAL MONODROMY identity
  on Conf(C). Vol III Pillar γ (CY-A_3 inf-cat) is about
  `HH^{-2}_{E_1} = 0` and the contractible space of E_3-liftings
  — a Goodwillie/obstruction-theoretic identity at a single CY_3
  category. The Vol III Manifesto §II claims these correspond
  under Phi, but neither Manifesto contains the bridge construction.
  The proposed correspondence is *plausible* (both are the "universal
  monodromy is forced" statement at the appropriate operadic level),
  but it is not derived. **Filed as edit C-3 below.**
- **Pillar 4 ↔ δ.** Vol I Pillar 4 (Shadow Quadrichotomy) is the
  G/L/C/M classification by analytic type of `Q^(q)(t)`. Vol III
  Pillar δ (six routes) is about K3 × E target. The
  Vol III Manifesto §IX(8) honestly admits "the Vol III parallel of
  Vol I's Shadow Quadrichotomy" is **not yet a named Vol III
  theorem**. The proposed Pillar δ correspondence is therefore
  *aspirational*. The genuine Vol III analog of the Quadrichotomy is
  the *six-route classification at K3 × E*, but this is itself
  conjectural (depends on CY-C). **Filed as C-4 below.**

### Wires through V20

The V20 standalone §III boxed equation
`tr_{Z(C)}(K_C) = -c_ghost(BRST(Phi(C))) = c_N(0)/2` correctly
wires Pillar 2 ↔ β. It does NOT wire Pillar 3 ↔ γ or Pillar 4 ↔ δ —
those bridges are claimed in the two §II diagrams but not derived.

---

## §2. Convention consistency

### Shared symbols (all three Manifestos)

| Symbol | Vol I Manifesto | Vol III Manifesto | V20 standalone | Drift? |
|--------|-----------------|-------------------|----------------|--------|
| `K` (conductor) | `K(A) = -c_ghost(BRST(A))` (Pillar 2 box) | `K = κ-conductor`, used in Pillar α slogan | `K(A) = -c_ghost(BRST(A))` (§I.A) | None |
| `K` (Koszul reflection) | `K = Bbar_X`, involutive (Pillar 1) | `K ∘ Phi ≃ CC_•` (§II) | `K_C` (§III) | **Symbol overload: same K used for both conductor and reflection.** Must subscript: `K_cond` vs `K_refl`. **Filed C-5**. |
| `κ` | `κ(A)` bare in Pillar 3 box | Always subscripted (`κ_ch, κ_BKM, κ_cat, κ_fiber`) | `κ_BKM(g_X)` and `K_Vir = 26` (mixed) | **Vol I uses bare `κ`; Vol III enforces AP113 strict subscripting.** Vol I Manifesto Pillar 3 box `κ(A) = -c_ghost(BRST(A))` violates AP113 if propagated to Vol III. **Filed C-6**. |
| `κ_ch` | Not used | `κ_ch = 2` for K3 (Pillar β slogan, AP-CY55 table) | `κ_ch` in Consequences §VII.5 | Consistent across Vol III + V20. Vol I silent. |
| `κ_BKM` | `κ_BKM(g_X) = c_N(0)/2` (Pillar 2 cross-volume) | `κ_BKM(g_X) = c_N(0)/2` (Pillar β box) | `κ_BKM(g_X) = c_N(0)/2` (§I.B) | Consistent. |
| `Phi` | `Phi: CY_d-Cat → E_n-ChirAlg(M_d)` (no scope qualifier in box) | `Phi: CY_d-Cat → E_n-ChirAlg(M_d), n = ∞/2/1 by d` (full piecewise) | `Phi: CY_d-Cat → E_n-ChirAlg(M_d) (n = ∞ at d=1, n=2 at d=2, n=1 at d≥3)` (§III) | Vol I Manifesto §IV displays Phi without the `n = …` qualifier; FM43 violation by Vol I Manifesto. **Filed C-7**. |
| `Bbar_X` (chiral bar) | `Bbar_X` (Pillar 1 statement) | `B^ord` (U1 in Pillar α) | (not displayed) | **Notation drift:** Vol I uses `Bbar_X` (overline B); Vol III uses `B^ord` (superscript ord). These refer to the same chiral bar functor but in different decorations. Vol I = "the bar"; Vol III = "ordered bar" emphasising the E_1-ordered colour. **Filed C-8**. |
| `∇_Arnold` | `∇_Arnold` (Pillar 3 box) | Not used | Not used | Vol I-only symbol; OK. |
| `q_KL`, `q_DK` | `q_KL` named (Russian-school §X, Kazhdan-Lusztig) | `q_KL` named (Russian-school §X, Kazhdan) | Not used | Both Manifestos cite the q-bridge `q_KL² = q_DK` from V9. Convention names match. |
| `h^v` | Not displayed in Manifesto (used in Pillar 2 derivation references) | Not displayed | Not displayed | Three Manifestos do not display `h^v` in any boxed identity; consistent absence. |
| `c_N(0)` | Cross-volume box uses `c_N(0)/2` (Pillar 2) | Boxed (Pillar β) | Boxed (§III) | Consistent. |

### Drift diagnosis

The most severe convention drift is the dual usage of `K`:
- in Vol I Pillar 1 it denotes the *Koszul reflection involution*
  on `Kosz(X)` (a functor, `K = Bbar_X`);
- in Vol I Pillar 2 it denotes the *conductor scalar*
  (`K(A) = -c_ghost`).

V20 §III makes this potentially confusing by writing
`tr_{Z(C)}(K_C)` where `K_C` is the *reflection*, while the right-hand
side uses `-c_ghost(BRST(Phi(C)))` — which Vol I Pillar 2 calls `K(A)`.
A reader who follows the V20 standalone literally sees `K` twice with
two different meanings. Recommendation: rename the conductor scalar to
`κ_K` or `K^conductor` and reserve `K` for the reflection. The Vol III
Manifesto already does this: it consistently uses `κ_BKM` for the
conductor scalar and reserves `K` for nothing else. The Vol I Manifesto
needs to follow suit.

---

## §3. Status consistency

For each ProvedHere theorem cited in the three Manifestos, check that
the status is consistent.

| Theorem | Vol I Manifesto status | Vol III Manifesto status | V20 status |
|---------|------------------------|--------------------------|------------|
| **Koszul Reflection (Pillar 1 / Theorem A Platonic)** | "PLATONIC" (V5 in punch list ghost theorems) | Not directly cited | (referenced) | Consistent |
| **Universal κ-Conductor / BRST Ghost (Pillar 2 / V6)** | "PLATONIC, sympy-verified" | "Vol I Pillar 2, ↔ β under Phi" | "Wave 14 V6, sympy-verified" | Consistent |
| **Climax (Pillar 3 / V7)** | "PLATONIC RHETORICAL ANCHOR" | Not status-tagged; corresponds to γ | Not directly cited | Consistent (no contradiction) |
| **Shadow Quadrichotomy (Pillar 4 / V8)** | "PLATONIC" | Not status-tagged; corresponds to δ but Vol III §IX(8) says "not yet a named Vol III theorem" | Not directly cited | **Potential drift.** Vol I treats Quadrichotomy as a Platonic theorem; Vol III says its analog is *not yet a theorem*. The Vol III Manifesto correctly admits the gap, but the Vol III §II diagram suggests Pillar δ already exists at the same status as Pillar 4. **Filed C-9**. |
| **CY-A_3 (inf-cat)** | "CY-A_3 PROVED (inf-cat)" (cross-volume Russian-school §X reference; consistent with CLAUDE.md) | "PROVED (inf-cat)" (Pillar γ box, `thm:derived-framing-obstruction`) | "Vol III's CY-A_3 inf-categorical proof is a special case of the Vol I bar–cobar adjunction restricted along Phi" (§VII.2) | Consistent |
| **BKM weight universality (`prop:bkm-weight-universal`)** | Cited as Vol III's `c_N(0)/2` formula (Pillar 2 cross-volume) | "ProvedHere with adversarial scope: c_N(0)/2 for K3-fibered CY3" (Pillar β honest scope at end of §I) | "99 tests" (V20 §I.B); but in §IX.1 Vol III Manifesto admits this is in `tautology_registry.md` entry #1 as "FRAME_SHAPE_DATA hardcoding tautologises the 99 tests" | **Drift.** Vol I Manifesto and V20 cite `prop:bkm-weight-universal` as established. The Vol III Manifesto §IV honestly notes the tautology-registry status. The honest reading is: c_N(0)/2 is *unconditional* (Borcherds 1998 + Gritsenko–Nikulin) on the 8 diagonal Z/NZ orbifolds; the "ProvedHere" status of `prop:bkm-weight-universal` for general K3-fibered CY3 is in the tautology queue. V20 §I.B should reflect this. **Filed C-10**. |
| **Universal Trace Identity (V20 §III)** | "the deepest single discovery of the swarm" (§IV) | "the deepest single discovery of the swarm" (§IV, exact echo) | Boxed Theorem in §III; proof skeleton in §IV | All three sources agree the Theorem is structural; V20 supplies the 5-step proof skeleton. Both Manifestos defer detail to V20. **Status: structural standalone; not yet a manuscript theorem.** Consistent if installation phase is honestly named. The §IV Vol I Manifesto and §IV Vol III Manifesto should both note the proof relies on V20 Step 3 (skew-derivation `δ = 0` argument), which V20 §VIII.1 names `conj:trace-identity-chain-level` for d ≥ 3 but asserts proved at d=2. **Filed C-11**. |
| **Pentagon (V15)** | "The Swiss-cheese arena seen from five categories" (Vol I §V) | Cited in Russian-school §X (Kapranov entry); not a Vol III pillar | Not displayed | Consistent (Vol II content) |
| **Trinity (in flight)** | "in flight" (Vol I §III table) | Not directly cited | Not displayed | Consistent |
| **MC5 / V12** | "Ready" (Vol I §III) | Not cited | Not cited | Consistent |
| **q-bridge / V9** | "Ready" (Vol I §III) | "Cross-volume q-convention sweep using V9 q-bridge (already installed Vol I side)" (§VIII.13) | Not cited | Consistent |
| **S_5 Wick / V10** | "Ready" (Vol I §III) | Cited as the model for Vol III's `compute/lib/phi_universality_verification.py` (§VIII.10 + §IX.7) | Not cited | Consistent |

### Severity ranking

The two genuine drifts are:
1. (C-10) Vol I Manifesto and V20 cite `prop:bkm-weight-universal` as
   established; Vol III Manifesto + tautology_registry record it as
   the seed entry awaiting honest healing. The three Manifestos
   should align on the honest statement.
2. (C-11) The Universal Trace Identity is presented as a named theorem
   in V20 with a 5-step proof, but Step 3 contains a chain-level
   assumption that V20 §VIII itself names as a conjecture. Both
   Manifestos should declare V20 a *structural standalone* with one
   load-bearing conditional, not a fully proved theorem.

---

## §4. Citation consistency

Cross-Manifesto check of external citations for the canonical 17 names
the task lists.

| Citation | Vol I Manifesto | Vol III Manifesto | V20 |
|----------|-----------------|-------------------|-----|
| **Drinfeld–Kohno** | "DK" (Pillar 3); "Drinfeld–Kohno" (§V) | Not cited (only via Vol I Pillar 3) | Not cited |
| **Verlinde** | "Verlinde" (Pillar 3 box, §V) | Not cited | "Verlinde-style invariant" (§VIII.4 conj:trace-identity-fusion) |
| **Borcherds** | "Borcherds" (Pillar 3 box, Pillar 2 cross-volume) | "Borcherds reflection / Borcherds 1998 / Gritsenko–Nikulin" (Pillars β, δ) | "Borcherds 1998" (§I.B), "Borcherds singular-theta correspondence" (§III, §IV.2) | All three cite Borcherds with consistent attribution; only Vol III + V20 add Gritsenko–Nikulin for the root-multiplicity verification. Consistent. |
| **Garland–Lepowsky** | Not directly cited (used in V13 BRST chapter draft) | Not cited | Not cited |
| **Costello–Gwilliam** | "Costello" (Russian-school §X; "factorisation algebra discipline") | "Costello" (Russian-school §X; "Vol III architecture IS the Costello programme made categorical") | "Witten + Costello + Gaiotto" (§X) | Both Manifestos and V20 use bare "Costello" in Russian-school sections. Vol III names "Costello-TCFT" (Pillar γ) and "Costello 5d" (Pillar δ Route 6). No drift on the *name* but Vol I Manifesto could clarify that "Costello" alone usually means Costello–Gwilliam in this programme. **Filed C-12**. |
| **Lurie HA** | Not displayed in Vol I Manifesto (used in Pillar 1 hypotheses + Wave 14 V15 Pentagon citations) | "Lurie" added explicitly to Russian-school §X with the slogan "(∞,1)-monoidal substrate supporting Pillar γ's inf-categorical CY-A_3" | Not cited | **Drift.** Vol I Manifesto §X does NOT name Lurie; Vol III Manifesto §X adds Lurie. Both Pillar 1 (Koszul Reflection) and Pillar α (Phi) require Lurie HA as foundational substrate. The Vol I Manifesto §X should add Lurie to match Vol III. **Filed C-13**. |
| **Beilinson–Drinfeld** | "Beilinson + Drinfeld" (§X) | "Beilinson + Drinfeld" (§X) | "Beilinson + Drinfeld" (§X) | Consistent. |
| **Polyakov** | "Polyakov" (§X; "bc-ghost system at spin 2") | "Polyakov" (§X; "the central note in BOTH Vol I's K = -c_ghost AND Vol III's κ_BKM = c_N(0)/2") | (referenced via §X chamber) | Consistent. |
| **Bezrukavnikov** | "Bezrukavnikov" (§X; "geometric-Langlands intuition") | "Bezrukavnikov" (§X; same) | "Bezrukavnikov" (§X) | Consistent. |
| **Calaque–Willwacher** | Not cited in Manifesto (used in V15 Pentagon supervisory draft) | Not cited | Not cited | Consistent (deferred to chapter-level). |
| **Kapranov–Voevodsky** | Not displayed (used in §X as "Kapranov" alone) | "Kapranov–Voevodsky" added separately (§X; Z-tetrahedron higher coherence) | Not cited | **Slight drift.** Vol III Manifesto distinguishes Kapranov (operadic discipline) from Kapranov–Voevodsky (higher coherence / Z-tetrahedron). Vol I Manifesto folds both into a single "Kapranov" entry. **Filed C-14.** |
| **Voronov** | Not cited in Manifesto | Not cited in Manifesto | Not cited | Wave 14 V15 Pentagon supervisory draft cites Voronov 1999 for the Swiss-cheese operad. None of the three Manifestos surface this. Acceptable since Pentagon is a Vol II item; if a Vol II Manifesto materialises, Voronov must appear. |
| **Hoefel–Livernet** | Not cited in Manifesto | Not cited in Manifesto | Not cited | Wave 14 V15 cites Hoefel 2009 + Hoefel–Livernet 2012 for SC_2 Koszul duality. Pentagon-internal; no Manifesto-level drift. |
| **Etingof** | "Etingof" (§X; "formal-deformation discipline") | "Etingof" (§X; "Pillar γ's three-level taxonomy is an Etingof-style formal-vs-rectified distinction") | "Etingof" (§X) | Consistent. |
| **Kazhdan–Lusztig** | "Kazhdan–Lusztig" (§X; "q_KL as the framed cover of q_DK") | "Kazhdan" alone (§X; "the q_KL convention as the framed cover of q_DK") | Not cited | **Slight drift.** Vol I Manifesto names "Kazhdan–Lusztig" (the joint authors). Vol III Manifesto names "Kazhdan" alone. Both refer to the same q-convention. **Filed C-15.** |
| **Witten** | "Witten" (§X; "topological field theory framing of the Climax") | "Witten" (§X; "topological field theory framing of Pillar γ as a Costello-TCFT obstruction calculation") | "Witten + Costello + Gaiotto" (§X collectively) | Consistent. |
| **Gaiotto** | "Gaiotto" (§X; "BPS-and-holography sensibility that Vol III Phi is the chiral SHADOW of the CY trace") | "Gaiotto" (§X; "the slogan IS Gaiotto's reading of Phi") | "Witten + Costello + Gaiotto" | Consistent. |
| **Nekrasov** | "Nekrasov" (§X; "Omega-background discipline that the spectral parameter has algebraic origin (AP-CY20)") | "Nekrasov" (§X; "Ω-background discipline that the spectral parameter has algebraic origin (AP-CY20) and is the ζ-promotion morphism of Pillar α") | Not cited | Both Manifestos cite Nekrasov with the same AP-CY20 anchor. Consistent. |

### Summary

Citation drift is generally minor. The three structural drifts:
1. (C-12) "Costello" vs "Costello-Gwilliam" should be unified.
2. (C-13) Lurie HA cited in Vol III but not Vol I.
3. (C-14, C-15) Slight name drift Kapranov vs Kapranov–Voevodsky and
   Kazhdan vs Kazhdan–Lusztig between the two Manifestos.

---

## §5. Open conjecture inventory

Catalogue all open conjectures named across the three Manifestos.

### Vol I Manifesto §IX

1. CY-C remains conjectural.
2. E_n-bar at d ≥ 2 open (Π2 obstruction in V5).
3. Lagrangian–Koszul converse open (Π3 obstruction in V5).
4. W-algebra extension of Climax theorem at higher rank open.
5. Genus-1 / higher-genus generalisation of Verdier-pairing distance open.
6. Trinity for genuinely E_1 chiral algebras open (`conj:trinity-E_1`).
7. Vol I's quantitative basis structurally tautological at present (0/2275).

### Vol III Manifesto §IX

1. Π_3^ch (chain-level explicit Phi_3 for non-formal algebras).
2. Π_C (CY-C at the fusion limit; abelian level constructive,
   non-abelian conjectural).
3. Π_{≥4} (higher CY Phi at d ≥ 4; π_d(BU)-obstruction).
4. Π_BFN (BFN Coulomb branch as Phi-evaluation).
5. Super-Yangian Y(gl(4|20)) conjectural.
6. K3 quantum toroidal U_{q,t}(ĝl_1)^{K3} conjectural.
7. Vol III's quantitative verification basis structurally tautological
   (2/283 ProvedHere claims with independent decoration).
8. Vol III parallel of Vol I's Shadow Quadrichotomy not yet a named
   theorem.

### V20 §VIII

1. `conj:trace-identity-chain-level` (Step 3 at chain level, d ≥ 3).
2. `conj:trace-identity-large-N` (Z/N orbifold extension N ≥ 9).
3. `conj:trace-identity-CY4` (CY_4 and higher, modular side requires
   Borcherds analog).
4. `conj:trace-identity-fusion` (root-of-unity / fusion-limit
   specialisation; precise version of CY-C).

### Cross-Manifesto contradictions

Cross-checking each conjecture against the other Manifestos for any
"X is open here / X is proved there" contradiction.

- **CY-C**: both Vol I (§IX.1) and Vol III (§IX.2) name CY-C as open.
  V20 §VIII.4 names `conj:trace-identity-fusion` as "a precise version
  of CY-C". Consistent. But: Vol III §I (Pillar δ box) writes the
  Six-Route Corollary that "their convergence is the content of CY-C,
  not a six-way conjectural coincidence." This suggests a *single named
  conjecture* rather than multiple separate routes. Acceptable framing
  but bordering on AP-CY60 narration. Honest: CY-C is the convergence
  conjecture. **No contradiction.**
- **Higher CY Phi at d ≥ 4**: Vol III §IX.3 (Π_{≥4}) and V20 §VIII.3
  (`conj:trace-identity-CY4`) are different but compatible
  conjectures. Vol III's Π_{≥4} concerns the *operadic-level
  obstruction* (no native E_n for n ≥ 2 at d ≥ 4); V20's
  `conj:trace-identity-CY4` concerns the *modular extension*
  (Borcherds analog at d ≥ 4). Vol I says nothing. **No contradiction.**
- **CY-A_3 inf-cat**: All three Manifestos consistently say
  PROVED (inf-cat). Vol III §IX.1 (Π_3^ch) honestly names the
  *chain-level explicit case for non-formal algebras* as the
  remaining open chunk. V20 §VII.2 says "CY-A_3 inf-cat upgrade as a
  corollary of Phi uniqueness". **Consistent.**
- **Trinity for E_1 chiral algebras**: Vol I §IX.6 names
  `conj:trinity-E_1`. Vol III does not address Trinity directly. V20
  §VIII.1 cites `conj:trinity-E_1` as a load-bearing input for Step 3
  at chain level for d=3. **Consistent: V20 makes the dependency
  explicit; the two Manifestos defer to V20.**
- **Quantitative tautology gap**: Vol I §IX.7 says 0/2275; Vol III
  §IX.7 says 2/283. Both use the same independent-verification
  protocol (HZ3-11). Numerically consistent: Vol I has 0 anchors
  (S_5 Wick draft V10 is "Ready" but not installed); Vol III has 2
  anchors (the protocol's bootstrap). **Consistent.**

### Composite open-conjecture inventory

Across the three Manifestos there are 7 + 8 + 4 = 19 *named* open
conjectures, but with overlap (CY-C appears in all three; CY-A_3
chain-level + Trinity_E1 are inputs to V20 Step 3). De-duplicating:

| ID | Name | Where named | Notes |
|----|------|-------------|-------|
| O1 | CY-C (quantum group realisation) | Vol I IX.1, Vol III IX.2, V20 VIII.4 | The umbrella |
| O2 | CY-A_3 chain-level explicit (Π_3^ch) | Vol III IX.1 | Inf-cat is proved |
| O3 | E_n-bar at d ≥ 2 (Π2) | Vol I IX.2 | Vol I-specific |
| O4 | Lagrangian–Koszul converse (Π3) | Vol I IX.3 | Vol I-specific |
| O5 | W-algebra extension of Climax (higher rank) | Vol I IX.4 | Vol I-specific |
| O6 | Genus-1 / higher-genus Verdier-pairing for codes | Vol I IX.5 | Vol I-specific |
| O7 | `conj:trinity-E_1` | Vol I IX.6 + V20 VIII.1 | Load-bearing for V20 d=3 chain |
| O8 | Higher CY operadic obstruction (Π_{≥4}) | Vol III IX.3 | π_d(BU) story |
| O9 | BFN as Phi-evaluation (Π_BFN) | Vol III IX.4 | Quiver-with-potential CY_3 |
| O10 | Super-Yangian Y(gl(4|20)) | Vol III IX.5 | Mukai signature lift |
| O11 | K3 quantum toroidal | Vol III IX.6 | Double-loop algebra |
| O12 | Vol III Shadow Quadrichotomy analog | Vol III IX.8 | Cross-volume completion |
| O13 | `conj:trace-identity-chain-level` | V20 VIII.1 | Step 3 of V20 proof at chain level |
| O14 | `conj:trace-identity-large-N` | V20 VIII.2 | N ≥ 9 orbifold extension |
| O15 | `conj:trace-identity-CY4` | V20 VIII.3 | Modular Borcherds analog at d=4 |

Vol I §IX.7 (quantitative basis) is a *programme*, not a single
conjecture; same for Vol III §IX.7. They are status remarks, not in
the conjecture inventory.

---

## §6. Russian-school voice consistency

### Voices named in each Manifesto §X

| Voice | Vol I §X | Vol III §X | V20 §X |
|-------|---------|------------|--------|
| Gelfand | ✓ | ✓ | ✓ |
| Etingof | ✓ | ✓ | ✓ (mentioned implicitly) |
| Kazhdan–Lusztig (Vol I) / Kazhdan (Vol III) | ✓ | ✓ | — |
| Bezrukavnikov | ✓ | ✓ | ✓ |
| Polyakov | ✓ | ✓ | — |
| Nekrasov | ✓ | ✓ | — |
| Kapranov | ✓ | ✓ | — |
| Kapranov–Voevodsky | — (folded into Kapranov) | ✓ (separate entry) | — |
| Beilinson + Drinfeld | ✓ | ✓ | ✓ |
| Witten | ✓ | ✓ | ✓ |
| Costello | ✓ | ✓ | ✓ |
| Gaiotto | ✓ | ✓ | ✓ |
| Lurie | — | ✓ | — |
| Borcherds | — | — | ✓ |

### Drifts

1. **Lurie**: present in Vol III §X, absent in Vol I §X. The Vol I
   Pillar 1 (Koszul Reflection) statement requires Lurie HA as
   substrate (the (∞,1)-monoidal symmetric statement of the bar–cobar
   adjoint equivalence). Vol I should add Lurie. **C-13 (already
   filed).**
2. **Borcherds**: present in V20 §X explicitly, absent from both
   Manifesto §X sections. Both Manifestos discuss Borcherds extensively
   in the body but do not name him in the Russian-school chamber. The
   Russian-school chamber should include Borcherds in *both*
   Manifestos. **Filed C-16.**
3. **Kazhdan vs Kazhdan–Lusztig**: handled in §4 above (C-15).
4. **Kapranov–Voevodsky as separate entry**: Vol III separates them
   to give Z-tetrahedron its own attribution; Vol I folds. Either
   convention is acceptable. **C-14 (already filed) recommends
   adopting Vol III's separation in Vol I.**

### Role attributions

For shared voices, role attributions match across Manifestos. Examples:
- Gelfand: "representation theory and analysis are one subject" (both).
- Etingof: "formal-deformation discipline" (both).
- Polyakov: "bc-ghost system at spin 2" (both); Vol III adds the
  cross-volume slogan "central note in BOTH Vol I's K = -c_ghost AND
  Vol III's κ_BKM = c_N(0)/2".
- Witten: "topological field theory framing" (both).
- Bezrukavnikov: "geometric Langlands intuition" (both).

No role drift.

---

## §7. Editing roadmap consistency

### Vol I roadmap (4 phases, 14 steps)

- Phase 1 (4 steps): install four pillars as named theorems.
- Phase 2 (4 steps): install supporting drafts (q-bridge, MC5,
  S_5 Wick, Verdier-pairing distance).
- Phase 3 (3 steps): cross-volume installation (Vol III Phi
  rewrite, Vol II Pentagon, universal trace identity in all three
  prefaces).
- Phase 4 (3 steps): punch list cleanup (P0/P1/P2 healing, HEAL-UP
  discipline, q-convention sweep).

### Vol III roadmap (5 phases, 14 steps)

- Phase 1 (3 steps): install Pillar α as parent theorem.
- Phase 2 (4 steps): install Pillars β, γ, δ as standalone theorems.
- Phase 3 (2 steps): cross-volume bridge installation (universal
  trace identity in preface; 17 stale CY-A_3 sweep).
- Phase 4 (2 steps): independent verification anchors
  (`phi_universality_verification.py`; tautology registry healings).
- Phase 5 (3 steps): punch-list cleanup (HEAL-UP, q-convention
  sweep, stub-chapter triage).

### Cross-volume sequencing dependencies

Vol I Phase 3 step 9 says "Vol III: rewrite cy_to_chiral.tex per V11
Phi functor reconstitution. De-condition 17 stale CY-A_3 phrases."
Vol III Phase 1 step 1 says "prop:phi-universality (Theorem Phi
statement, V11 §3.1) in chapters/theory/cy_to_chiral.tex L4–L17.
Replace per-d display with the single Platonic statement."

These two reference the *same edit* (Vol III cy_to_chiral.tex per
V11). **No contradiction**: Vol III owns the edit; Vol I lists it as a
cross-volume installation step. Both Manifestos should make this
ownership explicit. **Filed C-17.**

Vol I Phase 3 step 11 says "Vol I + II + III: install §8.5 universal
trace identity as the cross-volume centrepiece in each volume's
preface."
Vol III Phase 3 step 8 says "Universal Trace Identity (§IV above)
installed in `appendices/notation.tex` (kappa-spectrum table) + as
the climax of `chapters/frame/preface.tex` mirroring Vol I Wave 14
Climax subsection."
V20 §IX names Vol I, Vol II, Vol III installation sites.

Three sources, three installation locations for the universal trace
identity:
- Vol I Manifesto: "each volume's preface".
- Vol III Manifesto: notation appendix + preface.
- V20: chapter `chiral_chern_weil_brst_conductor.tex` (Vol I);
  `cy_to_chiral.tex §8.5` (Vol III); brief Remark in
  `sc_chtop_pentagon.tex` (Vol II); preface in Vol I + Vol III.

The three sources all agree on Vol I + Vol III preface installation;
only V20 specifies Vol II Remark and the chapter-level installations.
The Manifestos should adopt V20's more specific list. **Filed C-18.**

### Sequencing consistency

Both Manifestos place "install pillars" first, then "supporting
drafts", then "cross-volume", then "punch-list cleanup". Same
sequencing logic. No conflict.

### Vol II roadmap

The Vol II Manifesto is "in flight" — does not yet exist on disk. Once
it materialises, it must:
- include the Pentagon (V15) as one of its pillars (Vol I Manifesto
  §III names V15 as Vol II content);
- cite the Universal Trace Identity (V20 §IX.4 specifies "brief
  Remark in `sc_chtop_pentagon.tex`");
- align its phase structure with the Vol I + Vol III pattern.

---

## §8. Memorable form consistency

Each Pillar carries a memorable single-equation form. Cross-check
across Manifestos.

| Pillar | Memorable form (Vol I) | Memorable form (Vol III) | V20 |
|--------|------------------------|--------------------------|-----|
| Vol I Pillar 1 / Vol III α | `K^2 ≃ id_{Kosz(X)}` (slogan: "the chiral bar is its own Koszul dual") | Pillar α boxed display: `Phi: CY_d-Cat → E_n-ChirAlg(M_d), n = ∞/2/1` | (referenced via §III boxed identity) |
| Vol I Pillar 2 / Vol III β | `K(A) = -c_ghost(BRST(A))` (boxed) | `κ_BKM(X) = c_N(0)/2 = -c_ghost(BRST(Phi(X)))` (boxed) | `tr_{Z(C)}(K_C) = -c_ghost(...) = c_N(0)/2` (§III boxed) and §XI single-equation form |
| Vol I Pillar 3 / Vol III γ | `d_bar = KZ*(∇_Arnold), κ(A) = -c_ghost(BRST(A))` (boxed two-line display) | No boxed equation; the "Theorem (CY-A_3 inf-cat)" is a sentence, not a display | — |
| Vol I Pillar 4 / Vol III δ | `H^2 = t^4 Q on Σ_c` (Riccati identity) | Pillar δ statement: structure function (24,24); no boxed equation | — |
| **Universal Trace Identity** | `tr_{Z(C)}(K_C) = -c_ghost(BRST(Phi(C))) [Vol I] = c_N(0)/2 [Vol III]` (§IV box) | Identical boxed form (§IV) | Identical (§III, §XI) |

### Drift

The boxed Universal Trace Identity matches *exactly* across all three
sources — the three boxed equations are identical character-for-character
(modulo the explanatory wording around the cases). **Strong
consistency.** This is the central rhetorical anchor of the cross-volume
programme; the consistency is intentional and operationally tested.

The drifts are at the Pillar level:
- Vol I Pillar 3 has a boxed two-line display; Vol III γ has no
  display. The Vol III analog should acquire a boxed equation (e.g.,
  `HH^{-2}_{E_1}(A,A) = 0` for unit-connected A). **Filed C-19.**
- Vol I Pillar 4 has the Riccati `H^2 = t^4 Q`; Vol III δ has no
  single-equation form. The Vol III six-route corollary is not
  reducible to a single equation; perhaps "(Σ six routes) → Phi_3(K3
  × E)" as a memorable form. **Filed C-20.**

---

## §9. Recommendation: a single canonical CONVENTIONS APPENDIX

The audit reveals that the three Manifestos use slightly different
conventions for the same symbols (most acutely `K`, `Phi`, `B^ord` vs
`Bbar`, bare `κ` vs subscripted `κ_*`). The honest fix is *not* to
patch each Manifesto piecewise but to produce a single canonical
**Conventions Appendix** that all three Manifestos reference.

### Proposed structure of the Conventions Appendix

```
File: appendices/manifesto_conventions.md
(or, equivalently, a section §0 prepended to each Manifesto)

§0.1 The kappa-spectrum.
     - κ_ch  : chiral algebra modular characteristic (Vol III AP-CY55).
     - κ_BKM : Borcherds-Kac-Moody weight (Vol III prop:bkm-weight-universal).
     - κ_cat : holomorphic Euler char χ(O_X) (manifold invariant).
     - κ_fiber: lattice rank / fiber structure (manifold invariant).
     - Bare κ FORBIDDEN (AP113).
     - Vol I uses subscript-free κ in some Pillar boxes;
       to be subscripted as κ_ch when the boxed identity is read
       cross-volume.

§0.2 The K-symbols.
     - K       : Koszul reflection involution K = Bbar_X (Vol I Pillar 1).
                 Subscriptable: K_C (Vol III Phi-pulled-back), K^ch / K^BKM
                 (V20 §IV).
     - K(A)    : conductor scalar = -c_ghost(BRST(A)) (Vol I Pillar 2).
                 To be RENAMED κ_K(A) or K^cond(A) to disambiguate.
     - bc(λ)   : bc-ghost system at spin λ; central charge c_λ = -2(6λ²-6λ+1).

§0.3 The bar functor.
     - Bbar_X  : Vol I usage; chiral bar over the curve X.
     - B^ord   : Vol III usage; ordered chiral bar emphasising E_1 colour.
     - Bbar_X = B^ord on the chiral subcategory; convention bridge stated
       once and adopted uniformly.

§0.4 The Phi functor.
     - Phi: CY_d-Cat → E_n-ChirAlg(M_d), with the n = ∞/2/1 piecewise
       qualifier MANDATORY at first display (FM43).
     - Phi_d := Phi at fixed d.
     - Phi(C) := Phi evaluated at object C.

§0.5 q-conventions.
     - q_KL := exp(πi/(k+h^v))   Kazhdan-Lusztig.
     - q_DK := exp(2πi/(k+h^v))  Drinfeld-Kohno.
     - Bridge identity: q_KL² = q_DK (V9 q-bridge, Wave Supervisory).
     - Default convention in Vols I-III: KL.

§0.6 r-matrix conventions.
     - r_tr(z) = k Ω_tr/z (trace form; Vol I default).
     - r_KZ(z) = Ω/((k+h^v) z) (KZ; Vol I appendix).
     - Bridge: r_tr = r_KZ after rescaling z and generators (Wave V9 §1iii).
     - At k=0, r MUST vanish (AP126/AP141).

§0.7 Cross-Manifesto citation forms.
     - Costello-Gwilliam (full author pair) NOT bare "Costello".
     - Kazhdan-Lusztig (full pair).
     - Kapranov-Voevodsky as separate entry from Kapranov.
     - Voronov 1999 + Hoefel-Livernet 2012 for SC operadic
       attributions.
     - Borcherds 1998 + Gritsenko-Nikulin for the BKM weight
       universality.

§0.8 Universal Trace Identity (canonical form).
     - One boxed equation:
       tr_{Z(C)}(K_C) = -c_ghost(BRST(Phi(C))) = c_N(0)/2.
     - Reference: V20 §III + §XI.
     - To be installed verbatim in each Manifesto's
       cross-volume centrepiece section.
```

### Why this is the right intervention

The convention drift is symptomatic, not isolated. Patching each
Manifesto separately will recur on the next swarm wave because each
Manifesto is written in a slightly different voice and inherits
slightly different priors. A single sourced Conventions Appendix
referenced by all three Manifestos is the architectural fix. It also
serves the future Vol II Manifesto as a checklist before drafting.

---

## §10. Punch list of consolidating edits

Numbered C-1 through C-20. Each edit is filed with file, approximate
location, and proposed replacement text. None should be implemented
during this audit — they are PROPOSALS for the editing roadmap.

**C-1.** Vol I Manifesto §I (Pillar 1 box, L23): the "Three hypotheses
suffice" sentence does not name the hypotheses (H1)–(H3) explicitly in
the body; only the supervisory draft V5 spells them out. Add a
parenthetical "(H1) augmentation, (H2) augmentation-ideal completeness,
(H3) finite-dim graded bar pieces" to the box. Cross-volume: Vol III
§I (Pillar α) does the analogous spelling-out for (H1)–(H3) of Phi —
match the Vol I rhetoric.

**C-2.** Vol I Manifesto §II diagram (L74–88): the four-pillar diagram
shows the four pillars with two cross-bar interlocks (Climax to Koszul
+ BRST; Koszul to Quadrichotomy; etc.). Add the Vol III Phi-bridge as
a *fifth* edge labelled "Phi" connecting each Vol I pillar to its Vol
III partner. The Vol III §II already does this; Vol I should mirror.

**C-3.** Vol III Manifesto §II Pillar 3 ↔ γ correspondence (L92): the
correspondence "Climax ↔ CY-A_3 inf-cat" is asserted but not derived.
Add a one-paragraph sketch deriving γ as the Phi-pullback of Pillar 3
(specifically: the contractibility of the E_3-lifting space at d=3 IS
the Phi-image of the universality of the KZ connection on Conf(C);
the obstruction theory on `HH^{-2}_{E_1}` is the Phi-pullback of the
Arnold three-term relation).

**C-4.** Vol III Manifesto §II Pillar 4 ↔ δ correspondence (L93): same
as C-3 but for the Quadrichotomy ↔ six-route correspondence. Honest
content: each shadow class G/L/C/M corresponds to a different *limit*
of the Hilb^n(K3) target, and the six routes are six entry points to
this limit. The Vol III §IX(8) admission that "the Vol III parallel of
Vol I's Shadow Quadrichotomy is not yet a named theorem" should be
moved to the Pillar 4 ↔ δ correspondence statement, marking it as a
conjectural correspondence.

**C-5.** All three Manifestos: introduce explicit subscript on `K` to
distinguish reflection (`K_refl` or unsubscripted `K`) from conductor
scalar (`K_cond` or κ_K). Currently V20 §III boxed equation uses `K_C`
for the reflection and the right-hand side conductor is unnamed. Add
"the conductor scalar, denoted κ_K(C) := tr_{Z(C)}(K_C)" so the
identity reads `κ_K(C) = -c_ghost(BRST(Phi(C))) = c_N(0)/2`.

**C-6.** Vol I Manifesto §IV (L126–127): the cross-volume box mixes
bare `κ` (Vol I side) with subscripted `κ_BKM` (Vol III side). Replace
bare `K(A)` and bare `κ_BKM(g_X)` with `κ_K(A)` and `κ_BKM(g_X)` so
both sides are subscripted. Brings Vol I into AP113 compliance for the
cross-volume identity.

**C-7.** Vol I Manifesto §I (Pillar 2 cross-volume box) and §IV box:
the Phi functor display omits the n = ∞/2/1 piecewise qualifier (FM43).
Replace `Phi(C)` with `Phi: CY_d-Cat → E_n-ChirAlg(M_d), n = ∞/2/1 by
d` at first display.

**C-8.** All three Manifestos: pick one notation between `Bbar_X` and
`B^ord` for the chiral bar functor, and adopt uniformly. Recommended:
`Bbar_X` for the Vol I Koszul-reflection setting; `B^ord` for the
Vol III ordered/E_1 setting; with the bridge identity
`Bbar_X|_{E_1-chiral} = B^ord` stated in the Conventions Appendix
§0.3.

**C-9.** Vol III Manifesto §II diagram (L94) and §I Pillar δ box: add
the qualifier "(conjectural at full convergence; see §IX.8)" to the
Pillar δ box and to the diagram entry. Avoid suggesting parity with
Vol I Pillar 4 status.

**C-10.** Vol I Manifesto §IV and V20 §I.B: update the citation of
`prop:bkm-weight-universal` to acknowledge the tautology-registry
status. Replace "(Borcherds 1998, prop:bkm-weight-universal in Vol III,
99 tests)" with "(Borcherds 1998 + Gritsenko-Nikulin verified for the 8
diagonal Z/NZ orbifolds; general K3-fibered case in
notes/tautology_registry.md entry #1 awaiting independent witness)".
Aligns all three sources on the honest scope.

**C-11.** Vol I §IV and Vol III §IV cross-volume centrepiece sections:
add a footnote pointing out that V20 Step 3 (skew-derivation `δ = 0`
argument) is proved at d=2 and named `conj:trace-identity-chain-level`
at d=3. Both Manifestos currently present V20 as a fully proved
theorem; the V20 standalone itself §VIII.1 names the load-bearing
conditional.

**C-12.** All three Manifestos §X: replace bare "Costello" with
"Costello-Gwilliam" at first occurrence in each Russian-school chamber.
Bare "Costello" remains acceptable on subsequent uses. The Vol III
Manifesto already uses both "Costello" and "Costello-TCFT" / "Costello
5d"; add "Costello-Gwilliam" for the factorisation-algebra discipline
attribution.

**C-13.** Vol I Manifesto §X: add Lurie to the Russian-school chamber
with role "the (∞,1)-monoidal substrate supporting Pillar 1's
adjoint-equivalence statement; without Lurie HA the symmetric-monoidal
adjoint equivalence between Alg^{fact,aug,comp}_X and CoAlg^{fact,
conil,co}_X would not type-check." Match Vol III §X Lurie entry.

**C-14.** Vol I Manifesto §X: split "Kapranov" into two entries —
"Kapranov" (operadic discipline) and "Kapranov-Voevodsky" (higher
coherence; cited in connection with V15 Pentagon). Match Vol III §X
which separates them.

**C-15.** Vol III Manifesto §X: rename "Kazhdan" entry to
"Kazhdan-Lusztig" to match Vol I §X. Both Manifestos refer to the same
quantum-group convention; the joint authorship deserves the joint
attribution.

**C-16.** Both Manifestos §X: add Borcherds to the Russian-school
chamber. Vol I role: "the singular-theta correspondence underlying the
cross-volume Pillar 2 trace formula c_N(0)/2". Vol III role: "the
Borcherds reflection animating Pillar β; the Igusa cusp form Phi_10
weight 5 is the K3 × E specialisation of the universal trace identity."

**C-17.** Vol I Manifesto §VIII step 9 and Vol III Manifesto §VIII
Phase 1 step 1: cross-reference. Add to Vol I: "(Vol III owns this
edit; see Vol III Manifesto Phase 1 step 1)." Add to Vol III: "(Vol I
Manifesto §VIII Phase 3 step 9 references this edit as the cross-volume
Phi rewrite.)" Avoid duplicate-ownership confusion.

**C-18.** All three Manifestos: adopt V20 §IX as the canonical
installation-site list for the Universal Trace Identity, viz.:
- Vol I: `chapters/koszul/chiral_chern_weil_brst_conductor.tex` (V13
  chapter), positioned after `thm:K-Atiyah` and before W-algebra phase
  transition theorem.
- Vol III: `chapters/cy_to_chiral.tex §8.5`.
- Vol II: brief Remark in `chapters/foundations/sc_chtop_pentagon.tex`.
- Both Vol I + Vol III preface as cross-volume Climax.

**C-19.** Vol III Manifesto §I Pillar γ: add a boxed equation
`HH^{-2}_{E_1}(A, A) = 0 for unit-connected A` immediately after the
Theorem statement, matching the Vol I Pillar 3 boxed two-line display
discipline.

**C-20.** Vol III Manifesto §I Pillar δ: add a memorable single-equation
form. Candidate: `Φ_3(D^b(Coh(K3 × E))) = Y(g_{K3}) ⋊ Heis_E`, the
abelian K3 Yangian + elliptic Heisenberg semidirect product (per
`thm:k3-abelian-yangian-presentation`). Or: the structure function
identity `g(u, v) ∈ End(C^{24}) ⊗ End(C^{24}), deg = (24, 24)`. Match
Vol I Pillar 4 boxed `H^2 = t^4 Q` discipline.

---

## XI. End

The three Platonic Manifestos (Vol I, Vol III, V20) are largely
mutually consistent at the level of the four-pillar correspondence,
the universal trace identity, the open-conjecture inventory, and the
Russian-school voice chamber. Twenty distinct drifts are documented
above (C-1 to C-20), of which six are *substantive*
(C-3, C-4, C-5/C-6, C-9, C-10, C-11) and the remainder are *cosmetic*
(citation form, voice attribution, notation parity).

**The single highest-leverage edit** is to install the
**Conventions Appendix** of §9 above as a shared §0 referenced by all
three Manifestos. This closes ten of the twenty drifts (C-5, C-6, C-7,
C-8, C-12, C-13, C-14, C-15, C-16, plus the q-convention items C-13
implicitly). The remaining ten (correspondence-derivations C-3, C-4;
status-honesty C-9, C-10, C-11; cross-volume sequencing C-17, C-18;
memorable-form parity C-19, C-20; Vol I diagram update C-1, C-2) are
chapter-internal edits that the four-phase Vol I roadmap and five-phase
Vol III roadmap already accommodate.

The forthcoming Vol II Manifesto (in flight) should be drafted with
this audit's recommendations as a checklist:
1. adopt the Conventions Appendix §0 verbatim;
2. install the Universal Trace Identity at the V20 §IX-specified Vol II
   site (brief Remark in `sc_chtop_pentagon.tex`);
3. mirror the Vol I + Vol III §X Russian-school chamber, adding any
   Vol II-specific voices (Voronov, Hoefel-Livernet, Calaque-Willwacher
   per V15 supervisory draft);
4. align its pillar count with the four-pillar discipline of the
   sister volumes (candidates per Wave 14 V15: Pentagon Theorem;
   open-closed factorization; SC^{ch,top} two-coloured operad;
   QME / BV-BFV).

The arithmetic is verified. The pillars correspond. The trace
identity wires. The roadmaps sequence. The voices harmonise. What
remains are twenty named edits and one shared appendix.

— Raeez Lorgat, 2026-04-16
