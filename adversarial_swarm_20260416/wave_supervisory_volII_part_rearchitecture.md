# Wave Supervisory — Vol II main.tex Part Re-architecture around the Four Pillars

**Author of record.** Raeez Lorgat.
**Date.** 2026-04-16.
**Mandate.** Produce, in parallel with Vol I (`wave_supervisory_volI_part_rearchitecture.md`) and Vol III (`PLATONIC_MANIFESTO_VOL_III.md`), a re-architecture of Vol II's `main.tex` Part skeleton around the four Vol II pillars now visible after Wave 12 (`wave12_vol2_main.md`), Wave 14 (`wave14_reconstitute_chiral_hochschild_trinity.md`), the Pentagon supervisory (`wave_supervisory_sc_chtop_pentagon.md`), the MC5 supervisory (`wave_supervisory_mc5_theorem.md`) and the Universal Trace supervisory (`UNIVERSAL_TRACE_IDENTITY.md`).

**Status.** Architectural blueprint. **No edits to `~/chiral-bar-cobar-vol2/main.tex`. No commits. No build invoked.** The pre-commit hook reminder is observed by NOT issuing any `git` operation; the deliverable is a `.md` plan only.

**Voice.** Russian-school, Chriss–Ginzburg. SHOW the Pentagon; CONSTRUCT the bridge from Vol I's single-colour Trinity to Vol III's CY-to-chiral functor; PROVE each part-opener with the named Platonic theorem at the head, not at the tail.

---

## §1. Current 8-Part state of Vol II

`main.tex` (2384 lines) currently exposes the following architecture (extracted from `\part` declarations between L1217 and L1471):

| # | Part title | First chapter | Page extent (approx) |
|---|------------|---------------|----------------------|
| Front matter | Notation and conventions | L1089 | ~30pp |
| (Preface)  | `chapters/frame/preface.tex` | L1212 | ~25pp |
| (Intro)    | `chapters/theory/introduction.tex` | L1214 | ~40pp |
| **I**  | **The Open Primitive** | `theory/foundations` | ~110pp |
| **II** | **The $E_1$ Core** | `connections/bar-cobar-review` | ~75pp |
| **III**| **The Seven Faces of $r(z)$** | `connections/dnp_identification_master` | ~85pp |
| **IV** | **The Characteristic Datum and Modularity** | `examples/rosetta_stone` | ~120pp |
| **V**  | **The Standard HT Landscape** | `connections/ym_boundary_theory` | ~95pp |
| **VI** | **Three-Dimensional Quantum Gravity** | `connections/thqg_gravitational_complexity` | ~120pp |
| **VII**| **The Frontier** | `connections/spectral-braiding-frontier` | ~95pp |
| Conclusion | `\part*{Conclusion and Aftermatter}` | L1468 | ~20pp |
| Appendices | `appendices/brace-signs` | L1479 | ~15pp |

Total: 8 numbered Parts + frontmatter + conclusion + appendices, ~830pp. The naming is poetic (Open Primitive, Seven Faces, Standard Landscape, 3d Quantum Gravity) but **the four Vol II pillars are NOT named at the Part level**. They are scattered across chapter source.

---

## §2. Diagnosis — why the present skeleton no longer carries the load

Wave 12 (`wave12_vol2_main.md` §6) is unambiguous:

> No single chapter assembles the pentagon. The five are gestured at across Parts I–IV but no `\begin{theorem}[Pentagon equivalence]` exists.

Plus four further structural failures, confirmed independently:

1. **(Pentagon homeless.)** The five presentations of $\mathrm{SC}^{\mathrm{ch,top}}$ (operadic, Koszul dual, factorization, BV/BRST, convolution) are individually present in Parts I–IV but no chapter or Part is named for the Pentagon Theorem. The phantom `prop:sc-koszul-dual-three-sectors` (zero `\label` matches, two `\ref`) carries this weight illegitimately, and `thm:dual-sc-algebra` mis-states the closed-colour Koszul dual as $\mathrm{Com}^! = \mathrm{Lie}$ (FM156: should be $E_2\{1\}$).

2. **(MC5 missing.)** Vol I's MC chain MC1 → MC2 → MC3 → MC4 currently terminates at MC4 (`N5_mc5_sewing.tex` is misnamed: it is in fact the analytic-sewing standalone, not MC5). Vol II's `concordance.tex`, `examples/w-algebras*.tex`, `connections/typeA_baxter_rees_theta.tex` cite "MC4 closed" without the eval-core qualifier (AP47 violation), and Vol II offers no Part-level home for the closing MC5 theorem `d_{\bar,5} = \mathrm{KZ}^*(\nabla^{(5)}_{\mathrm{Arnold}})`.

3. **(FM157 nine-file mis-attribution.)** `Liv06` (Livernet, *A rigidity theorem for pre-Lie algebras*, JPAA 207) is bound at `main.tex:1627` and cited at `line-operators.tex`, `modular_swiss_cheese_operad.tex`, `bar-cobar-review.tex`, `introduction.tex`, `preface.tex`, `preface_trimmed.tex`, `bv_brst.tex`, `concordance.tex`, `standalone/preface_full_survey.tex` for SC Koszulity. Wrong paper everywhere. The correct attribution is Hoefel (arXiv:0809.4623) + Hoefel–Livernet (arXiv:1207.2307).

4. **(AP151 nine-hbar zoo.)** Nine distinct $\hbar$ conventions coexist in chapter source (`ordered_associative_chiral_kd_core`, `dnp_identification_master`, `kontsevich_integral`, `spectral-braiding-core`, `thqg_3d_gravity_movements_vi_x`, `ht_physical_origins`, `thqg_modular_bootstrap`, `3d_gravity`) plus two unbridged $q$ conventions ($q_{\mathrm{KL}}$ vs $q_{\mathrm{DK}}$, with $q_{\mathrm{KL}}^2 = q_{\mathrm{DK}}$ never stated). No conventions block in `main.tex`.

5. **(PVA descent triple-labeled.)** `thm:recognition` exists at three labels (`thm:recognition`, `thm:recognition-foundations`, `thm:recognition-SC`); `pva-descent.tex` is a zombie of `pva-descent-repaired.tex` (FM172/FM173). The PVA-descent pillar (V2-AP21/22 — "PVA = classical limit, NOT P_∞-chiral") has no canonical Part-level home.

6. **(MT-E and MT-F untagged.)** Two `\begin{maintheorem}` envs (`thqg_gravitational_complexity.tex:1675`, `affine_half_space_bv.tex:204`) carry no `\ClaimStatus`; they index downstream as ProvedHere with no provenance. AP40 violation.

The cumulative effect: a reader cannot find the Pentagon, cannot find MC5, gets the wrong reference for SC Koszulity, hits two unbridged $q$ definitions, lands on a zombie PVA file, and meets two untagged main theorems. **The Part skeleton is not load-bearing for the mathematics it now contains.**

---

## §3. Three options

### Option A — "Four-Pillar Part-spine" (full re-architecture)

Replace the seven interior numbered Parts (Open Primitive, $E_1$ Core, Seven Faces, Characteristic Datum, Standard Landscape, 3d Quantum Gravity, Frontier) by **four Pillar Parts** plus Foundations + Applications + Frontier:

```
Part I   — Foundations (the open–closed two-colour setup)
Part II  — Pillar I:  The SC^{ch,top} Pentagon (Wave V15)
Part III — Pillar II: The E_1-chiral bialgebra (V2-AP1–24)
Part IV  — Pillar III: The MC chain (closing at MC5; Wave V12)
Part V   — Pillar IV: PVA descent as classical limit (V2-AP21/22)
Part VI  — The E_1 sector applications (Yangians, line operators, $W$-algebras)
Part VII — H(T) and the Standard HT Landscape
Part VIII— Three-Dimensional Quantum Gravity + Frontier
```

This is the strongest re-architecture: the four pillars become four full Parts, each opening with its Platonic theorem at the head and unrolling examples afterwards. **Cost:** every chapter cross-reference re-bucketed; ~30 cross-volume citations updated.

### Option B — "Pillar Part 0 + existing Parts" (minimal)

Insert a single new "Part 0: Four Pillars" containing four ~30pp chapters (one per pillar) at the head of the manuscript, leaving Parts I–VII untouched. Cross-references unchanged; existing Part skeleton preserved.

**Cost:** minimal. **Drawback:** the four pillars become a "preamble" and the seven existing Parts continue to scatter the supporting material. The Pentagon proof would live in a Part 0 chapter while the five presentations remain in Parts I–IV, replicating the current architectural failure.

### Option C — "Hybrid with pillar openers"

Keep the current 7 interior numbered Parts but install a **Pillar opener** at the head of each of Parts I, II, III, V (matching the four pillars' natural homes), and a master `chapters/foundations/sc_chtop_pentagon.tex` chapter at the head of Part I as the master Pentagon theorem. Parts IV (Characteristic Datum), VI (3dQG), VII (Frontier) keep their current openers.

**Cost:** moderate. **Advantage:** preserves Vol II's poetic Part naming while elevating the four pillars to visible structural elements. **Drawback:** the four pillars are not Parts; they are openers within existing Parts. The reader still needs the existing Part structure to find each pillar.

### Recommendation: **Option C with one structural promotion**

Adopt Option C **plus** one structural change: split current Part I (The Open Primitive) into:

- **Part I — Foundations and the Pentagon** (~80pp): contains the new `sc_chtop_pentagon.tex` chapter at the head + existing `foundations`, `locality`, `axioms`, `equivalence`, `factorization_swiss_cheese`, `raviolo`, `fm-calculus`, `orientations`, `fm-proofs`.
- **Part II — PVA Descent (Pillar IV opener)** (~30pp): elevates `pva-descent-repaired.tex`, `pva-expanded-repaired.tex` into their own Part, opening with the PVA-descent theorem `MT-B` at the head, declaring V2-AP21/22 (PVA ≠ P_∞-chiral; classical shadow) explicitly. Deletes the zombie `pva-descent.tex`.

Then renumber:

- Part III = current Part II (The $E_1$ Core), opening with the **E_1-chiral bialgebra theorem (Pillar II)** as a master theorem at the head.
- Part IV = current Part III (Seven Faces of $r(z)$), opening with the **Seven Faces master diagram** (already partly assembled in `dnp_identification_master.tex`).
- Part V = current Part IV (Characteristic Datum and Modularity), opening with the **MC5 closing theorem (Pillar III)** as the master theorem at the head, citing the new `standalone/N5_mc5_theorem.tex`.
- Part VI = current Part V (Standard HT Landscape).
- Part VII = current Part VI (Three-Dimensional Quantum Gravity).
- Part VIII = current Part VII (Frontier).

**Result:** 8 numbered Parts, four of them (I, II, III, V) opened by a named Pillar theorem, the other four reserved for applications/landscape/frontier. The Pentagon, PVA descent, E_1-chiral bialgebra, and MC5 each get their own Part-opener.

Option C-promoted is the recommendation. Justification: it solves the architectural homeless-Pentagon problem WITHOUT disrupting the existing Vol II naming aesthetic (which the readership already follows), and it grants each pillar a Part-opener home. The cost is one new chapter (`sc_chtop_pentagon.tex`) and the elevation of `pva-descent-repaired.tex` to its own Part — surgical changes.

---

## §4. Detailed chapter mapping for Option C-promoted

### Part I — Foundations and the Pentagon (~110pp, was current Part I "The Open Primitive")

Order:

1. (NEW) `chapters/foundations/sc_chtop_pentagon.tex` — **Pillar I opener**. Contains `thm:sc-chtop-pentagon` (Pentagon of equivalences) at the head, with the five edges $\Phi_{12}, \Phi_{23}, \Phi_{34}, \Phi_{45}, \Phi_{51}$ as named lemmas. ~30pp. Per `wave_supervisory_sc_chtop_pentagon.md` §4.
2. `chapters/theory/foundations.tex` — bar-cobar setup, recognition theorem (single canonical `thm:recognition`).
3. `chapters/theory/locality.tex` — locality axioms; PIN duplicates of `thm:recognition` deleted.
4. `chapters/theory/axioms.tex` — **conventions block at head**: $\hbar = 1/(k+h^v)$ (algebraic), $q_{\mathrm{KL}} = e^{i\pi\hbar}$, $q_{\mathrm{DK}} = q_{\mathrm{KL}}^2 = e^{2\pi i \hbar}$, $q_\tau = e^{2\pi i \tau}$ (modular nome). Three named symbols, single bridge identity. Closes AP151 permanently.
5. `chapters/theory/equivalence.tex` — equivalences of axiomatisations.
6. `chapters/theory/bv-construction.tex` — BV/BRST setup. Pentagon edge $\Phi_{34}$ cited.
7. `chapters/theory/factorization_swiss_cheese.tex` — BD–CG factorization. **Reframe `thm:bd-cg-equivalence` (L1624), `thm:factorization-koszul-duality` (L1803), `thm:colour-projections` (L2260) as corollaries of Pentagon $\Phi_{12}$, $\Phi_{23}$.**
8. `chapters/theory/raviolo.tex` — Costello–Gaiotto raviolo geometry. Includes `def:log-SC-algebra`.
9. `chapters/theory/raviolo-restriction.tex` — restriction.
10. `chapters/theory/fm-calculus.tex` — Fulton–MacPherson calculus.
11. `chapters/theory/orientations.tex` — operadic orientations.
12. `chapters/theory/fm-proofs.tex` — FM-stratum proofs.

### Part II — PVA Descent: the Classical Limit (Pillar IV opener) (~30pp)

Order:

1. `chapters/theory/pva-descent-repaired.tex` — **Pillar IV opener**. Contains `MT-B` (cohomological descent to a shifted PVA, `\ClaimStatusProvedHere`) at the head. Establishes V2-AP21 (PVA ≠ P_∞-chiral) explicitly in the Part-opener prose: PVA is the *classical shadow* (descend to cohomology); P_∞-chiral is the *homotopy intermediate* (do NOT descend); the two run in *opposite directions*.
2. `chapters/theory/pva-expanded-repaired.tex` — explicit examples: V_k(g), Heisenberg, Virasoro, K3-Mukai (cross-volume to Vol III).
3. (DELETE) `chapters/theory/pva-descent.tex` — zombie file (FM172). Replaced by repaired version. The deletion is part of the migration checklist.
4. (DELETE) duplicate `MT-A'` mirror at `introduction.tex:1155` — collapsed to a single restatement citing `MT-B`.

### Part III — The $E_1$-Chiral Bialgebra (Pillar II opener) (~75pp, was current Part II "The $E_1$ Core")

Order:

1. (NEW or upgrade existing) `chapters/connections/e1_chiral_bialgebra_master.tex` — **Pillar II opener**. Contains the master theorem on the E_1-chiral bialgebra structure (V2-AP1–24 as antecedents): the E_1-chiral bialgebra is the right Hopf framework (NOT E_∞ vertex bialgebra; AP-CY23 of Vol III). The coproduct $\Delta_z$ on $B^{\mathrm{ord}}(A)$ with deconcatenation; the antipode $S$; the $R$-matrix as universal half-braiding (AP-CY25 correction). Pentagon Edge $\Phi_{23}$ enters here as the chiral Higher Deligne brace.
2. `chapters/connections/bar-cobar-review.tex` — three bars distinct: `B^{\mathrm{ord}}` (open), `B^\Sigma` (unordered, $R$-twisted descent), `B^{\mathrm{FG}}` (zeroth pole only). **Install named-symbol macros** (closes V2-AP3 / FM-VOL2-BAR1).
3. `chapters/connections/line-operators.tex` — line operators. **`thm:homotopy-Koszul` (`MT-D`) reframed**: Step 2 as ∞-morphism with explicit Drinfeld associator (FM158 healed). Liv06 → Hoefel09 + HL12 (FM157 healed at this site).
4. `chapters/connections/ordered_associative_chiral_kd_core.tex` — ordered KD core.
5. `chapters/connections/dg_shifted_factorization_bridge.tex` — dg shifted bridge.
6. `chapters/connections/thqg_gravitational_yangian.tex` — gravitational Yangian (Pillar II × Vol III bridge).
7. `chapters/connections/typeA_baxter_rees_theta.tex` — type-A weight-Rees telescope (rename per FM177, supply Q-operator OR rename "Baxter").
8. `chapters/connections/shifted_rtt_duality_orthogonal_coideals.tex` — shifted RTT.
9. `chapters/connections/casimir_divisor_core_transport.tex` — Casimir divisor.

### Part IV — The Seven Faces of $r(z)$ (~85pp, was current Part III)

Order: unchanged. Opener: existing `dnp_identification_master.tex` opener. **Spectral-braiding-core.tex updates**: `thm:dual-sc-algebra` (L3730) FM156 fix to $E_2\{1\}$; phantom `prop:sc-koszul-dual-three-sectors` ref replaced by `lem:edge-12` of Pentagon. `thm:Koszul_dual_Yangian` split into (a) classical Drinfeld Yangian ProvedElsewhere[DNP25] + (b) A_∞-shifted refinement ProvedHere with arity-4+ coherences (closes FM163, FM241, FM246).

### Part V — The Characteristic Datum and Modularity (Pillar III opener) (~120pp, was current Part IV)

Order:

1. (NEW: cross-reference in Part-opener prose) `\input{standalone/N5_mc5_theorem.tex}` (or absorbed into a new `chapters/connections/mc5_closing.tex`) — **Pillar III opener**. Contains `thm:mc5-sewing` (the 5-point sewing theorem, AP47-qualified to eval-gen-core, with the genus-1 corner $\delta_{1|3}^*$ as the first crossing of the genus filter). Per `wave_supervisory_mc5_theorem.md` §2. ~25pp. The MC chain MC1 → MC2 → MC3 → MC4 → MC5 closes here.
2. `chapters/examples/rosetta_stone.tex` — examples Rosetta stone.
3. `chapters/examples/examples-computing.tex` — computing.
4. `chapters/examples/examples-complete-proved.tex` — complete-proved cases.
5. `chapters/examples/examples-worked.tex` — worked examples. **Add "(eval-gen core of DK_g)" qualifier at every MC4 cite** (closes AP47 / FM-VOL2-MC4-1 here).
6. `chapters/examples/w-algebras-virasoro.tex` — Virasoro.
7. `chapters/examples/w-algebras-w3.tex` — $W_3$.
8. `chapters/connections/hochschild.tex` — Hochschild. **Split `thm:global-triangle-boundary-linear` into LG version + chiral G/L/C version** (closes FM126).
9. `chapters/connections/brace.tex` — brace.
10. `chapters/theory/modular_swiss_cheese_operad.tex` — modular SC.
11. `chapters/connections/relative_feynman_transform.tex` — relative Feynman.
12. `chapters/connections/modular_pva_quantization_core.tex` — modular PVA. **Write `prop:genus1-twisted-tensor-product` explicitly** (closes FM87 phantom-label).
13. `chapters/connections/ht_physical_origins.tex` — HT physical origins.

### Part VI — The Standard HT Landscape (~95pp, was current Part V)

Order: unchanged. Carries Pillar IV (PVA descent) applications: every chapter using PVA cites `MT-B` from Part II.

### Part VII — Three-Dimensional Quantum Gravity (~120pp, was current Part VI)

Order: unchanged. **`thm:E3-topological-DS-general` restricted** to (good-integer-graded principal nilpotents) ∪ (verified non-principal cases); strikes "all class M" (closes FM81/FM82). **`MT-E` (Gravitational complexity, L1675) `\ClaimStatus` tag added** (closes AP40 violation).

### Part VIII — The Frontier (~95pp, was current Part VII)

Order: unchanged. Includes `chapters/connections/affine_half_space_bv.tex`. **`MT-F` `\ClaimStatus` tag added** (L204). **`prop:affine-is-log-SC` (L1548) reframed**: SC^{ch,top} acts on the *pair* $(\mathrm{Obs}^{\mathrm{cl}}(U), \mathrm{Obs}^{\mathrm{cl}}(\partial U))$, not on $A$ alone (closes FM209 / AP165).

### Conclusion + Appendices: unchanged.

**Total Part count:** 8 (I Foundations+Pentagon, II PVA, III E_1-bialgebra, IV Seven Faces, V Characteristic+MC5, VI HT Landscape, VII 3dQG, VIII Frontier). Four pillar-opener Parts (I, II, III, V); four landscape/application Parts (IV, VI, VII, VIII). Total chapter count: ~52 (+1 pentagon, +1 MC5, –1 zombie pva-descent, +1 e1-bialgebra-master). Page count: ~830pp → ~870pp.

---

## §5. Part openers (1–2 paragraphs each, Platonic theorem at the head)

### Part I opener — Foundations and the Pentagon

> Vol II's central operadic object is the Swiss-cheese chiral-topological coloured operad $\mathrm{SC}^{\mathrm{ch,top}}$, a two-coloured operad on a smooth complex curve $C$. Its closed colour records bulk OPE on $C$ via the Fulton–MacPherson compactification; its open colour records totally-ordered topological insertions on a real boundary; the two are coupled by the *Swiss-cheese half-disk* action of the bulk on the boundary. **Pentagon Theorem** (`thm:sc-chtop-pentagon`, ProvedHere): the five presentations $\mathsf{P}_1$ (operadic generators-and-relations), $\mathsf{P}_2$ (Koszul dual), $\mathsf{P}_3$ (factorization / derived chiral centre), $\mathsf{P}_4$ (BV/BRST observables), $\mathsf{P}_5$ (convolution $L_\infty$) are pairwise equivalent as coloured dg-operads, and the five edges $\Phi_{12}, \Phi_{23}, \Phi_{34}, \Phi_{45}, \Phi_{51}$ fit into a pentagon that commutes up to a canonical 2-cocycle $\omega \in H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ with $[\omega] = 0$.
>
> The Pentagon is the **Vol II two-colour analog** of Vol I's Koszul Reflection Theorem (Pillar I of Vol I): single-colour Koszul $K \colon A \mapsto \Omega(\bar B(A))^\vee$ becomes coloured Koszul on the SC^{ch,top}-algebra pair $(B, A)$, with each colour reflected separately and coherence supplied by the bulk-on-boundary mixed sector. Part I unrolls the Pentagon, then completes the foundations: locality, axiom systems, BD–CG factorization, raviolo geometry, FM calculus.

### Part II opener — PVA Descent (Pillar IV)

> Cohomological descent realises a chiral algebra's *classical shadow* as a Poisson Vertex Algebra (PVA). **PVA Descent Theorem** (`MT-B`, `pva-descent-repaired.tex`, ProvedHere): for any logarithmic $\mathrm{SC}^{\mathrm{ch,top}}$-algebra $A$ in classes $G/L/C$, the cohomological filtration descends to a $(-1)$-shifted PVA structure on $H^*_{\mathrm{ch}}(A)$. This is the **Vol II analogue** of Vol I's Shadow Quadrichotomy (Pillar IV of Vol I): the four shadow classes $G, L, C, M$ that classify chiral algebras by m_k-tower depth correspond, after PVA descent, to four classical-Poisson regimes — formal-symplectic ($G$), rational-Poisson ($L$), convergent-Poisson ($C$), and divergent (class $M$, where PVA descent is replaced by descent to a P_∞-chiral object running in the *opposite* direction).
>
> The opposing-direction language is V2-AP21 made structural. PVA = classical shadow (descend); P_∞-chiral = homotopy intermediate (do NOT descend). The Part is short (~30pp) but load-bearing: every Vol II application (Parts VI, VII, VIII) that invokes a "classical limit" cites `MT-B` from here, and every Vol III citation of "the classical shadow of Phi(C)" routes through this Part.

### Part III opener — The E_1-Chiral Bialgebra (Pillar II)

> The E_1-chiral bialgebra is the correct Hopf framework for chiral algebras with non-trivial OPE. **E_1-Chiral Bialgebra Theorem** (master theorem at `e1_chiral_bialgebra_master.tex`, ProvedHere): for any $E_1$-chiral algebra $A$ on a curve $C$, the ordered bar coalgebra $B^{\mathrm{ord}}(A)$ carries a coproduct $\Delta_z$ (deconcatenation along $\mathrm{Conf}^{\mathrm{ord}}(\RR)$), an antipode $S$, and an $R$-matrix $R(z) \in \mathrm{Aut}(B^{\mathrm{ord}}(A) \otimes B^{\mathrm{ord}}(A))$ that is the universal half-braiding (NOT extracted from $\Delta(1)$; AP-CY25 correction). The data $(B^{\mathrm{ord}}(A), \Delta_z, S, R(z))$ satisfies the chiral pentagon for $\Delta_z$ and the coloured hexagon for $R(z)$.
>
> This is the **Vol II analogue** of Vol I's $\kappa$-Conductor / BRST (Pillar II of Vol I): single-colour BRST $d_{\mathrm{BRST}} = \kappa \cdot Q$ becomes the coloured Hopf data $(\Delta_z, S, R(z))$ on the open colour of $\mathrm{SC}^{\mathrm{ch,top}}$. The $\kappa$-conductor is recovered as the trace $\mathrm{tr}_R(R(z))$ at $z = 0$. AP-CY23 of Vol III (E_1-chiral, NOT E_∞ vertex bialgebra) is structural here.

### Part IV opener — The Seven Faces of $r(z)$ (unchanged)

(Existing opener prose retained. Cross-link added to Part III: each of the seven faces of $r(z)$ is the linearisation of $R(z)$ from Part III at the relevant degeneration.)

### Part V opener — Characteristic Datum and Modularity (Pillar III)

> The chiral correlator's modular structure is encoded in the n-point sewing of the bar differential. **MC5 Sewing Theorem** (`thm:mc5-sewing`, `standalone/N5_mc5_theorem.tex`, ProvedHere on eval-gen core): for any strong completion tower $\cA$ of finite resonance rank, the 5-point chiral correlator extends as a holomorphic section across the eleven boundary divisors of $\bar M_{0,5}$ — ten rational separating divisors $\delta_{0|S,S^c}$ governed by MC4, plus the genus-1 corner $\delta_{1|3}^*$ governed by the elliptic supertrace $F^{(1)}_3 \otimes \Phi^{\mathrm{ec}}_2$. The bar differential satisfies $d_{\bar,5} = \mathrm{KZ}^*(\nabla^{(5)}_{\mathrm{Arnold}})$, the pullback of Arnold's universal KZ connection at $n = 5$.
>
> This is the **Vol II analogue** of Vol I's Climax Theorem (Pillar III of Vol I): single-colour Climax $d_{\bar} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$ becomes the coloured n-point sewing closure at the first crossing of the genus filter. Part V unrolls MC5 first, then the Rosetta Stone of examples, the Hochschild calculus (split into LG + chiral G/L/C versions per FM126), the brace structure, the modular-SC operad, the relative Feynman transform, the modular PVA quantization, and the HT physical origins.

### Part VI opener — The Standard HT Landscape (unchanged, with Pillar IV bridge)

(Existing opener retained. Add: "Each chapter that invokes a 'classical limit' cites the PVA Descent Theorem (`MT-B`) from Part II.")

### Part VII opener — Three-Dimensional Quantum Gravity (unchanged)

(Existing opener retained. Add: "The closed-colour observable algebra of every 3d gravity model in this Part is a $\mathrm{SC}^{\mathrm{ch,top}}$-algebra (Pentagon, Part I); the Yangian deformation in `thqg_gravitational_yangian.tex` is the E_1-chiral bialgebra structure of Part III specialised to gravity.")

### Part VIII opener — The Frontier (unchanged)

(Existing opener retained. Add: "Every conjectural pillar extension — full-category MC5 (`conj:mc5-full`), nonabelian Yangian, A_∞-shifted Koszul refinement — lives here, with its dependence on the four Pillar Parts of I/II/III/V explicit.")

---

## §6. Reading paths (per Vol III precedent)

Three reading paths through the proposed 8-Part structure:

### Path 1 — The Algebraist (Parts I, II, III, IV; ~30 chapters)

For a reader interested in the operadic, Koszul, and Hopf structures: the Pentagon (Part I), PVA descent as classical limit (Part II), the E_1-chiral bialgebra with its half-braiding $R(z)$ (Part III), and the seven faces of $r(z)$ (Part IV). Skip the modular sewing details (Part V), the HT landscape (Part VI), 3dQG (Part VII), Frontier (Part VIII). This path supports a graduate course on operadic homotopy methods for chiral algebras.

### Path 2 — The Physicist (Preface, Part I, Part III, Part V, Part VII; ~25 chapters)

For a reader interested in BV/BRST observable algebras, Hopf data on chiral algebras, modular sewing, and 3d quantum gravity: the Pentagon edge $\Phi_{34}$ (BV/factorization, Part I), the E_1-chiral bialgebra (Part III), the MC5 closing theorem and the modular Swiss-cheese (Part V), the 3dQG applications (Part VII). Skip the PVA descent (Part II), the seven r(z) faces (Part IV), the HT landscape (Part VI), Frontier (Part VIII). This path supports a graduate course on BV/BRST and chiral observables in 3d quantum gravity.

### Path 3 — The Number Theorist (Preface, Part I, Part II, Part V, Part VIII; ~20 chapters)

For a reader interested in the modular and arithmetic content: the Pentagon (Part I) for the operadic backdrop, PVA descent (Part II) for the classical-Poisson shadow, MC5 + the modular Swiss-cheese + the HT physical origins (Part V), and the Frontier conjectures on full-category MC5, modular completion, and Borcherds-style automorphic structure (Part VIII). Skip the E_1-bialgebra technicalities (Part III), the r(z) seven faces (Part IV), the standard HT landscape (Part VI), 3dQG (Part VII).

---

## §7. Cross-volume bridge role: Vol II as the BRIDGE register

Vol II's distinctive role in the three-volume programme is **architectural mediation**:

```
Vol I              Vol II                                   Vol III
single-colour  --  two-colour SC^{ch,top}      --  CY-to-chiral functor
chiral algebra     (Pentagon)                       Phi: CY_d-Cat -> E_n-ChirAlg
Trinity            Pentagon                          K3 Yangian + Six Routes
```

The Pentagon (Pillar I) is the operadic mechanism that **mediates** between Vol I's single-colour Trinity (chiral Hochschild trinity, Wave 14 Theorem A) and Vol III's $\Phi$ functor:

- **Vol I → Vol II direction.** Each of Vol I's three chiral Hochschild complexes ($C^*_{\mathrm{ch,op}}$, $C^*_{\mathrm{ch,fact}}$, $C^*_{\mathrm{ch,BV}}$) is the Hochschild shadow of a Pentagon edge: $\Phi_{12}$ realises operadic = factorization at the cohomology level; $\Phi_{34}$ realises factorization = BV; $\Phi_{45} \circ \Phi_{51}$ realises convolution = operadic. The single-colour Trinity is the *image* of the Pentagon under $A \mapsto C^*_{\mathrm{ch}}(A,A)$. Vol II's Pentagon Part-opener cites this explicitly.
- **Vol II → Vol III direction.** The $\Phi$ functor outputs at $d=2$ a closed-colour ($E_2$-chiral) algebra; at $d=3$ an open-colour ($E_1$-chiral) algebra. Vol II's Pentagon supplies the coloured operad on which $\Phi$'s output is an algebra. The half-disk closed-on-open mixed sector is the operadic home of Vol III's K3 Yangian Drinfeld coproduct $\Delta_z$ (which is the open-colour $\Delta_z$ of Vol II's Part III specialised to the K3 Heisenberg).
- **Bridge identity.** $q_{\mathrm{KL}}^2 = q_{\mathrm{DK}}$ is the algebraic shadow of the Pentagon's mixed half-disk: bulk full-loop monodromy (closed colour, $q_{\mathrm{DK}}$) is the square of boundary half-loop monodromy (open colour, $q_{\mathrm{KL}}$). This is structural in Vol II, where it appears in the conventions block at the head of Part I and in the q-convention bridge supervisory (`wave_supervisory_q_convention_bridge.md`).

Vol II's prose in the new Part I opener and the new Part III opener should each contain a short paragraph explicitly naming this bridge role:

> Vol II is the bridge register of the programme. Vol I supplies the single-colour chiral Hochschild Trinity (Pillar I of Vol I); Vol III supplies the geometric source via the CY-to-chiral functor $\Phi$ (Pillar α of Vol III). Vol II's Pentagon mediates: each Trinity equivalence is the shadow of a Pentagon edge under $A \mapsto C^*_{\mathrm{ch}}(A,A)$; each $\Phi(C)$ output at $d \in \{2, 3\}$ is a Pentagon-algebra on the appropriate colour. The Pentagon is what makes the cross-volume programme commute.

---

## §8. Migration checklist (numbered, in execution order)

1. **(Pre-flight.)** Verify build passes on current `main.tex` (`cd ~/chiral-bar-cobar-vol2 && make fast`). Verify tests pass (`make test`). Record current page count, undef-ref count, undef-cite count.
2. **(Conventions block.)** Insert the conventions block ($\hbar, q_{\mathrm{KL}}, q_{\mathrm{DK}}, q_\tau$ with bridge identities) at the head of `chapters/theory/axioms.tex`. Closes AP151. Verify all 9 hbar conventions in chapter source are now expressible in terms of the canonical $\hbar$.
3. **(Pentagon chapter.)** Create `chapters/foundations/sc_chtop_pentagon.tex` per `wave_supervisory_sc_chtop_pentagon.md` §4. ~30pp. Insert at the head of Part I in `main.tex`.
4. **(Pentagon downstream.)** Reframe `thm:bd-cg-equivalence`, `thm:factorization-koszul-duality`, `thm:colour-projections` in `factorization_swiss_cheese.tex` as corollaries of Pentagon edges. Close FM156 at `spectral-braiding-core.tex:3730` and `bv_brst.tex:2059` (replace `Com^! = Lie` by `E_2{1}`; replace phantom `prop:sc-koszul-dual-three-sectors` by `lem:edge-12`). Close FM209 at `affine_half_space_bv.tex:1548` (algebra-vs-pair fix).
5. **(Liv06 → Hoefel09 + HL12.)** Rebind in `main.tex:1627` bibliography. Update at 9+ files: `line-operators.tex`, `modular_swiss_cheese_operad.tex`, `bar-cobar-review.tex`, `introduction.tex`, `preface.tex`, `preface_trimmed.tex`, `bv_brst.tex`, `concordance.tex`, `standalone/preface_full_survey.tex`. Closes FM157.
6. **(PVA Part-promotion.)** Promote `pva-descent-repaired.tex` and `pva-expanded-repaired.tex` to a new `\part{PVA Descent: the Classical Limit}` between current Parts I and II. Delete zombie `pva-descent.tex` (closes FM172). Collapse duplicate `MT-A'` mirror in `introduction.tex:1155`. Verify `MT-B` is the canonical statement.
7. **(E_1-chiral bialgebra master.)** Create or upgrade `chapters/connections/e1_chiral_bialgebra_master.tex` to host Pillar II opener. Cite Vol III AP-CY23 / AP-CY25 as the antipattern context. Insert at head of Part III (renumbered).
8. **(MC5 chapter.)** Per `wave_supervisory_mc5_theorem.md` §6: rename `standalone/N5_mc5_sewing.tex` → `standalone/N5b_analytic_sewing.tex`; create `standalone/N5_mc5_theorem.tex` from the supervisory draft. Insert at head of Part V (renumbered) via `\input` or via a new `chapters/connections/mc5_closing.tex` wrapper.
9. **(MC4 eval-core qualifier.)** At every "MC4 closed" or "MC4 package" cite in Vol II chapter source, append "(eval-generated core of DK_g)". Files: `examples/w-algebras-stable.tex`, `examples/w-algebras-frontier.tex`, `examples/w-algebras.tex`, `connections/typeA_baxter_rees_theta.tex`, `concordance.tex`. Closes AP47 / FM-VOL2-MC4-1.
10. **(Triple-label collapse.)** `thm:recognition`, `thm:recognition-foundations`, `thm:recognition-SC` collapse to one canonical label. Update all `\ref` sites. Closes FM173.
11. **(MT-E and MT-F status tags.)** Add `\ClaimStatus...` tags to `thqg_gravitational_complexity.tex:1675` (MT-E) and `affine_half_space_bv.tex:204` (MT-F). Closes AP40 violations.
12. **(thm:Koszul_dual_Yangian split.)** In `spectral-braiding-core.tex`, split `thm:Koszul_dual_Yangian` into (a) classical (ProvedElsewhere[DNP25] + new pairing lemma) and (b) A_∞-shifted (ProvedHere with arity-4+ coherences). Closes FM163, FM241, FM246.
13. **(thm:E3-topological-DS-general scope-restriction.)** In `3d_gravity.tex`, restrict outer scope to (good-integer-graded principal nilpotents) ∪ (verified non-principal cases). Closes FM81/FM82.
14. **(thm:global-triangle-boundary-linear split.)** In `hochschild.tex`, split into LG version (existing) + chiral G/L/C version (new). Closes FM126.
15. **(prop:genus1-twisted-tensor-product.)** Write the proposition explicitly in `modular_pva_quantization_core.tex` (Gauss–Manin uncurving + $\Lambda^2 H^1 \otimes$ curvature + Arakelov pairing). Closes FM87.
16. **(B-bar named macros.)** In `axioms.tex` macro block, install `B^{\mathrm{ord}}, B^\Sigma, B^{\mathrm{FG}}` as named macros; propagate to chapter source. Closes V2-AP3 / FM-VOL2-BAR1.
17. **(Standalone caveat parity.)** Three pairs (preface_full_survey vs preface; class_m_global_triangle vs ht_bulk_boundary_line_core; stokes_gap_kzb_regularity vs modular_swiss_cheese_operad). Lift the more honest of the two into both. Closes FM-VOL2-CAV1.
18. **(Test-tautology fix.)** In `compute/tests/test_adversarial_verification.py:712-719`, replace hardcoded `expected = [Rational(1,24), Rational(7,5760), Rational(31,967680)]` by an independent Arakelov heat-kernel computation. Closes V2-AP28 / FM225.
19. **(Cross-volume update.)** Update Vol I CLAUDE.md, Vol III CLAUDE.md to cite the new Pentagon Theorem `thm:sc-chtop-pentagon` and the new MC5 `thm:mc5-sewing`. Run `grep -rn 'five presentations' chapters/` in all three volumes; update ~17 sites.
20. **(Theorem-index regenerate.)** Update `theorem_index.tex` (Vol II) to bucket by new Part structure. Verify every theorem entry's Part assignment matches the new `\part{...}` declaration.
21. **(Final build.)** `cd ~/chiral-bar-cobar-vol2 && make fast`. Expect: 0 undef refs, 0 undef cites, page count ~870pp, ~17 new theorems registered (Pentagon + 5 edges + Pentagon-coherence + MC5 + 5 MC5 clauses + e1-bialgebra master + sub-lemmas).
22. **(Test suite.)** `make test`. Expect: ~150 new tests (Pentagon: ~120; MC5: ~30) on top of existing ~34K Vol II test suite.
23. **(Pre-commit hook reminder.)** Verify (a) build passes, (b) tests pass, (c) no AI attribution. Commit by Raeez Lorgat. The pre-commit hook is the gate; the migration is not done until all three are green.

---

## §9. Risk assessment

| Risk | Severity | Mitigation |
|---|---|---|
| Pentagon proof in `sc_chtop_pentagon.tex` exceeds chapter budget (~30pp) | Medium | Split into a chapter (Pentagon statement + edge sketches) + a standalone (full proof of each edge + coherence). Standalone can run ~60pp. |
| Liv06 → Hoefel09+HL12 rebind missed at one site | Low | After Step 5, run `grep -rn 'Liv06\|Liv15\|Livernet 2006' chapters/ standalone/`; expect zero hits. |
| MC5 chapter conflicts with existing genus-1 sewing material in `modular_swiss_cheese_operad.tex` | Medium | MC5 is the *closing* theorem; existing genus-1 material in Part V chapters becomes corollaries / examples of MC5. Cross-references need careful alignment. |
| PVA Part-promotion breaks cross-volume citations from Vol I, Vol III | Low | Existing `MT-B` label (`thm:pva-descent-repaired` or similar) preserved verbatim; only the Part number changes. AP-CY13 / V2-AP26 (no hardcoded Part numbers) discipline catches this. |
| Pillar II opener (`e1_chiral_bialgebra_master.tex`) duplicates content from `bar-cobar-review.tex` and `line-operators.tex` | Medium | The opener is a master-theorem chapter (~20pp); existing chapters cite the master theorem rather than restate it. V2-AP27 (no duplicated content) discipline applies. |
| Conventions block in `axioms.tex` conflicts with chapter-local conventions | High at install time, low after | After install, run `grep -rn 'hbar\|q = e' chapters/` and verify every $\hbar$ and $q$ definition matches the canonical block. Audit per FM-VOL2-Q1. |
| Test suite slowdown from ~150 new tests | Low | Pentagon and MC5 engines are mostly compile-time symbolic; test runtime should grow by < 5%. |
| Cross-volume CLAUDE.md updates desync | Medium | Step 19 explicit. Run cross-volume grep at every commit. AP-CY13 / V2-AP30 discipline. |
| MT-E and MT-F status tags chosen incorrectly | Low | MT-E (gravitational complexity) and MT-F (affine half-space BV) both have proof blocks; status tag should be `ProvedHere`. Verify proof-env presence per AP-CY40. |
| Page count creeps beyond 900pp target | Low | Current ~830pp + Pentagon (~30pp) + MC5 (~25pp) + e1-bialgebra master (~20pp) − zombie pva-descent (~10pp) = ~895pp. Within 900pp soft cap. |

---

## §10. Inner music — Vol II's symphony

Vol II's symphony plays the **bridge** between Vol I (single-colour chiral algebras) and Vol III (CY categories via $\Phi$). Its inner music is the **two-colour cadence** of bulk meeting boundary.

The Pentagon Theorem is the **five-theme round** (operadic, Koszul, factorization, BV, convolution) — five voices that enter separately and resolve into a single cadence at $[\omega] = 0$. Its tonic chord is the Swiss-cheese half-disk: bulk acts on boundary, and the action is uniquely determined up to contractible choice.

The four pillars play four movements:

- **Movement I (Part I, allegro).** Pentagon: rapid five-voice exposition. The Swiss-cheese arena reveals itself in five views; each view is a distinct theme; the cadence vanishes the 2-cocycle.
- **Movement II (Part II, andante).** PVA descent: slow descent from the chiral key to the classical key. The tempo halves; the chiral OPE poles degenerate to formal residues; the Poisson bracket emerges as the leading order in $\hbar$.
- **Movement III (Part III, scherzo).** E_1-chiral bialgebra: brisk Hopf-data dance. The coproduct $\Delta_z$ deconcatenates; the antipode $S$ inverts; the half-braiding $R(z)$ exchanges. Three movements in one — the coproduct, the antipode, the R-matrix all entwined.
- **Movement IV (Part V, finale).** MC5 closing theorem: the n-point sewing reaches the genus-1 bubble. The 5-point function meets the elliptic supertrace; the bar differential $d_{\bar,5} = \mathrm{KZ}^*(\nabla^{(5)}_{\mathrm{Arnold}})$ is universal; the chain MC1 → MC2 → MC3 → MC4 → MC5 closes at the first genus crossing.

The four movements together compose the **bridge symphony**. Vol I's single-colour symphony plays in parallel (Koszul Reflection / κ-Conductor / Climax / Shadow Quadrichotomy); Vol III's geometric symphony plays in counterpoint (Φ-functor / Borcherds / CY-A_3 / K3 Yangian). Vol II is the modulating section — the place where the two outer keys (single-colour and geometric) meet in a coloured pentagon.

The cadence $[\omega] = 0$ at the Pentagon is the symphony's **central cadence**. After it, every other theorem in Vol II resolves consistently. Without it, the symphony stalls polyphonically without a tonic.

---

## §11. Cross-volume harmony

| Vol I Pillar (single-colour) | Vol II Pillar (two-colour) | Vol III Pillar (CY-geometric) |
|---|---|---|
| **Pillar I.** Koszul Reflection $K \colon A \mapsto \Omega(\bar B(A))^\vee$, $K^2 \simeq \mathrm{id}$ | **Pillar I.** SC^{ch,top} Pentagon: coloured Koszul on the pair $(B, A)$; pentagon coherence = $K^2 \simeq \mathrm{id}$ on coloured pairs | **Pillar α.** Platonic CY-to-Chiral Functor $\Phi \colon \mathrm{CY}_d\text{-Cat} \to E_n\text{-ChirAlg}$, target colour determined by $d$ |
| **Pillar II.** $\kappa$-Conductor / BRST: single-colour conductor formula $\kappa(A) + \kappa(A^!) = \rho_K$ | **Pillar II.** E_1-chiral bialgebra: coloured Hopf data $(\Delta_z, S, R(z))$; conductor $= \mathrm{tr}_R(R(0))$ | **Pillar β.** Borcherds Reflection Trace: $\kappa_{\mathrm{BKM}} = c_N(0)/2$ universally; trace on the Borcherds-lifted automorphic form |
| **Pillar III.** Climax: $d_{\bar} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$ universally | **Pillar III.** MC chain MC1 → MC2 → MC3 → MC4 → MC5; $d_{\bar,n} = \mathrm{KZ}^*(\nabla^{(n)}_{\mathrm{Arnold}})$ at every $n$; MC5 = first genus crossing | **Pillar γ.** Inf-Categorical CY-A_3 Resolution: $\mathrm{HH}^{-2}_{E_1} = 0$; Goodwillie layers vanish; space of E_3-liftings contractible |
| **Pillar IV.** Shadow Quadrichotomy $G/L/C/M$ | **Pillar IV.** PVA Descent: classical-Poisson shadows of $G/L/C$; class $M$ → P_∞-chiral (opposite direction) | **Pillar δ.** K3 Abelian Yangian + Six-Route Specialisation; six independent constructions converging at $G(K3 \times E)$ |

The four-pillar parallelism is exact across all three volumes. Each Vol II pillar is the *two-colour generalisation* of the corresponding Vol I pillar AND the *operadic ancestor* of the corresponding Vol III pillar:

- **Pillar I horizontal harmony.** Vol I's $K$ on a single chiral algebra $A$ = single-colour reflection. Vol II's Pentagon on $(B, A)$ = coloured reflection. Vol III's $\Phi$ outputs an algebra of the appropriate colour (closed at $d \le 2$, open at $d \ge 3$).
- **Pillar II horizontal harmony.** Vol I's BRST conductor $\kappa = \mathrm{tr}(Q^2)$ = single-colour trace. Vol II's $R(z)$-data = coloured Hopf trace. Vol III's $\kappa_{\mathrm{BKM}} = c_N(0)/2$ = trace on the Borcherds lift, the geometric specialisation at K3.
- **Pillar III horizontal harmony.** Vol I's Climax $d_{\bar} = \mathrm{KZ}^*$ = single-curve sewing. Vol II's MC5 = n-point sewing closing at the genus-1 wall. Vol III's CY-A_3 inf-cat resolution = the same closure at the *infinity-categorical* level for CY_3 chiral algebras.
- **Pillar IV horizontal harmony.** Vol I's $G/L/C/M$ = single-colour shadow classification. Vol II's PVA descent = classical shadow on $G/L/C$, with class $M$ requiring the opposite-direction P_∞-chiral. Vol III's K3 Yangian + six routes = geometric specialisations, each route producing a distinct shadow class for the corresponding CY input.

The diagonal cells of the harmony table are also load-bearing: Vol I Pillar III × Vol II Pillar I = the Climax Theorem's pullback identity, applied to the closed colour of the Pentagon, gives the closed-colour KZ specialisation $q_{\mathrm{DK}}$ monodromy; applied to the open colour, gives $q_{\mathrm{KL}}$. The bridge $q_{\mathrm{KL}}^2 = q_{\mathrm{DK}}$ is the Pentagon's mixed half-disk.

---

## §12. What this delivery does NOT do

- Does **not** edit `~/chiral-bar-cobar-vol2/main.tex`. (Per mandate.)
- Does **not** create the new chapter files `chapters/foundations/sc_chtop_pentagon.tex`, `standalone/N5_mc5_theorem.tex`, `chapters/connections/e1_chiral_bialgebra_master.tex`. (Future waves; supervisory drafts already exist for the first two.)
- Does **not** delete the zombie `chapters/theory/pva-descent.tex`. (Migration step 6.)
- Does **not** invoke `git`, `make`, or any build/test pipeline. (Pre-commit hook reminder observed.)
- Does **not** install the conventions block, rebind Liv06, or any of the 23 migration steps. (All listed in §8 as planned actions; none executed by this delivery.)
- Does **not** propose changes to Vol I or Vol III main.tex. (Vol I rearchitecture in `wave_supervisory_volI_part_rearchitecture.md`; Vol III in `PLATONIC_MANIFESTO_VOL_III.md`.)

**Status of the deliverable.** Architectural blueprint for Vol II at the four-pillar Part level. ~3,800 words. Recommendation: Option C-promoted (8 numbered Parts, with Parts I, II, III, V opened by the four pillar theorems). Migration checklist: 23 numbered steps, in execution order. Risk assessment: complete. Cross-volume harmony with Vol I and Vol III: explicit table.

---

## Appendix A. Two-line summary of each Part-opener theorem

| Part | Pillar | Master theorem | Statement |
|---|---|---|---|
| I | Pentagon (Pillar I) | `thm:sc-chtop-pentagon` | Five presentations of $\mathrm{SC}^{\mathrm{ch,top}}$ pairwise equivalent; pentagon coherence $[\omega] = 0$ |
| II | PVA descent (Pillar IV) | `MT-B` | Cohomological descent to a $(-1)$-shifted PVA for log SC^{ch,top}-algebras of class $G/L/C$ |
| III | E_1-chiral bialgebra (Pillar II) | E_1-bialgebra master | $(B^{\mathrm{ord}}(A), \Delta_z, S, R(z))$ is a chiral Hopf algebra; $R(z)$ = universal half-braiding |
| IV | Seven Faces of $r(z)$ | `dnp_identification_master` | Seven faces = seven degenerations of $R(z)$ |
| V | MC5 closing (Pillar III) | `thm:mc5-sewing` | 5-point sewing extends across all 11 boundary divisors of $\bar M_{0,5}$, including the genus-1 corner $\delta_{1|3}^*$ |
| VI | (HT landscape applications) | (none new) | — |
| VII | (3dQG applications) | (none new) | — |
| VIII | (Frontier conjectures) | (none new) | — |

## Appendix B. Pentagon × MC5 × Trinity × E_1-bialgebra interlock

The four pillars are not independent. They interlock as follows:

```
Pentagon (I)  ----- edge Phi_{12} ------>  E_1-bialgebra (III)
   |                                              |
   |                                              |
   V                                              V
PVA descent (IV)                              MC5 closing (V)
   |  (classical limit)                          |  (n=5 specialisation)
   V                                              V
H^*_ch(A) Poisson VA                       d_bar_5 = KZ*(nabla^{(5)})
```

- Pentagon → E_1-bialgebra: Edge $\Phi_{12}$ (operadic → Koszul) restricted to the open colour gives the coproduct $\Delta_z$ on $B^{\mathrm{ord}}(A)$.
- Pentagon → PVA descent: The closed-colour $E_2 \to E_2\{1\}$ Koszul (FM156-corrected) at the level of associated graded gives the classical Poisson structure (PVA descent target).
- E_1-bialgebra → MC5: The half-braiding $R(z)$ at $n = 5$ degeneration gives the elliptic 3-point function on the bubble $\delta_{1|3}^*$.
- PVA descent → MC5: The classical limit of the bar differential $d_{\bar,5} = \mathrm{KZ}^*(\nabla^{(5)}_{\mathrm{Arnold}})$ at $\hbar \to 0$ gives the Poisson sewing on the genus-1 corner.

Each pair of pillars meets at a named edge of the interlock. The four pillars together generate the full Vol II content.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution. No commit. No edit to Vol II `main.tex` or any Vol II source file. Delivered to `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_supervisory_volII_part_rearchitecture.md` per Wave Supervisory mandate parallel to Vol I (`wave_supervisory_volI_part_rearchitecture.md`) and Vol III (`PLATONIC_MANIFESTO_VOL_III.md`).
