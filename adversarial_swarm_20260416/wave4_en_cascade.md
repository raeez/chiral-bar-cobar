# Wave 4 Adversarial Audit — The E_n Cascade and the Operadic Circle

**Date:** 2026-04-16
**Auditor:** adversarial-referee role for Vol I
**Target files:**
- `~/chiral-bar-cobar/standalone/en_chiral_operadic_circle.tex` (3882 lines, primary target)
- `~/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex` (7459 lines)
- `~/chiral-bar-cobar/standalone/N1_koszul_meta.tex` (1044 lines)
- `~/chiral-bar-cobar/standalone/sc_chtop_pva_descent.tex` (1594 lines)
- `~/chiral-bar-cobar/chapters/theory/configuration_spaces.tex` (4959 lines)
- `~/chiral-bar-cobar/chapters/theory/chiral_center_theorem.tex` (2697 lines)

The primary target is *Paper E* (`en_chiral_operadic_circle.tex`), which is the
new standalone monograph "E_n-Chiral Algebras, Derived Centres, and the Operadic
Circle" (~80–100 pp target, Inventiones-aimed). Its abstract claims (lines
96–116) that "the E_n operadic circle E_3 → E_2 → E_1 → E_2 → E_3 is **proved
to close** for simple g via the E_3 identification theorem" and that "the
chiral quantum group equivalence identifies three structures (R-matrix, A_∞,
coproduct) on the Koszul locus." This is precisely the configuration AP150 was
written to guard against. The standalone is, in places, an honest construction
of the circle and, in places, a confabulation. This report disentangles the two.

---

## Section 1. Triage of major claims

| # | Claim | Location | Triage |
|---|------|----------|--------|
| C1 | The E_n operadic circle E_3 → E_2 → E_1 → E_2 → E_3 closes for simple g (abstract; Cor. 7.7 = `cor:e-circle-partly-closes`) | L111, L2349–L2370 | **PARTIAL CONFABULATION.** The "closing" is a theorem only at the level of formal deformation families on the Costello–Francis–Gwilliam side (Thm 7.4 = `thm:e-e3-identification`, L2264–L2284). The full E_3 ≃ E_3 closing is `Conjecture 11.1 = conj:e-drinfeld-center-equals-bulk` (L3178). The abstract abuses "proved to close" — see §3. |
| C2 | Arrow 1 ("Restriction to a codimension-2 defect", L1989–L1996) | Def 6.2 | **NOT PROVED.** Stated as a definition; no theorem produces an E_2-chiral algebra from an arbitrary E_3-top algebra plus a defect. Cited only as the bulk-to-boundary leg of the holographic interpretation (Rem. 11.7). |
| C3 | Arrow 2 (Ordered bar B^ord) | L1997–L2002 | **PROVED** that the ordered bar is an E_1-chiral coassociative coalgebra (Princ 3.10 = `princ:e-sc-location`, L1097–L1131). |
| C4 | Arrow 3 (Drinfeld centre Z: E_1-Cat → E_2-Cat) — "the **sole source** of nontrivial braiding" (Thm 6.3) | L2030–L2079 | **MISLEADING SCOPE.** The proof is correct (π_1(Conf_2(R^3))=1 vs π_1(Conf_2(C))=Z) but the framing "Drinfeld centre is the sole source" elides arrow 1's failure to produce nontrivial braiding by definition (cf. AP-CY54, AP-CY57 in cache). |
| C5 | Arrow 4 (Higher Deligne: HH^*(A) is E_{n+1} for E_n A) — Francis '13 | L2014–L2019, L2361–L2363 | **SCOPE INFLATION (AP153).** Francis's HDC is invoked here for E_2-chiral inputs, but the HDC for chiral algebras (with formal-disk OPE) requires either an E_∞ input or a careful chain-level model. The standalone never specifies which version of HDC it is invoking — see §3. |
| C6 | Arrow 5 (Closing) — "the E_3-top algebra obtained by traversing (1)–(4) should be equivalent to the original" | L2020–L2026 | **EXPLICITLY CONJECTURAL** ("should be equivalent"; conjecture 11.1). Honest. |
| C7 | Chiral centre theorem: Z_{SC^chtop}(A) ≃ C^•_ch(A,A) (Thm 3.4) | L927–L944 | Stated for E_∞-chiral A only. Proof sketches operadic centre construction (Def 3.5). The actual heavy lifting is in `chiral_center_theorem.tex` Thm 5.4 (`thm:chiral-deligne-tamarkin`, L1418–L1486). |
| C8 | SC^chtop has closed colour FM_k(C) ≃ E_2 and open colour E_1; SC^chtop is *not* E_3 (Rem 4.2) | L1192–L1204 | **CORRECT** and explicitly negates Dunn additivity for two-coloured operads. This is the strongest single observation in the standalone — see §3. |
| C9 | Topologisation theorem (Thm 5.1, KM; Thm 5.5, DS for W-algebras) | L1438–L1480, L1626–L1689 | **PROVED** (cohomological + chain-level model). Original-complex chain-level lift remains conjectural for class M (Conj 5.2, Rem 5.10). Honest. |
| C10 | E_3 identification theorem (Thm 7.4) — Z^der_ch(V_k(g)) ≃ A^λ from CFG perturbative CS | L2264–L2329 | **CONDITIONAL THEOREM.** Proof relies on CFG '25 ("in preparation", L3804–L3806) and on dim H^3(g)=1. Step 4 ("global extension") is an order-by-order matching, not a global isomorphism. |
| C11 | Chiral quantum group equivalence (R-matrix ↔ A_∞ ↔ coproduct), Thm 9.1 | L2599–L2673 | **PARTIAL.** The triangle relies on Etingof–Kazhdan reconstruction (cited but not proved); the γ leg uses the "universal R-matrix of the Drinfeld double" with a hand-waved canonical element. See §2 for the e_i ⊗ e^i objection. |
| C12 | Theorem H: ChirHoch^* concentrated in {0,1,2} (Thm 3.6) | L996–L1013 | **OVERSTATED FOR VIRASORO.** The standalone says "{0,1,2}"; `chiral_center_theorem.tex` L2025–L2041 says ChirHoch^•(Vir_c) is concentrated in {0,2} with H^1=0. **DIRECT INTERNAL CONTRADICTION** — see §2 (C12). |
| C13 | Five notions of E_1-chiral algebra; only B↔C proved on Koszul locus (Thm 8.2) | L2432–L2556 | **HONEST CATALOGUE.** Five derived centres declared not known to coincide in general (Warning 8.3, L2531–L2556). Good failure-mode hygiene. |

---

## Section 2. Per-claim attack / defense / repair

### Claim C1: The circle closes for simple g

**Attack.** Cor 7.7 (L2349–L2370) titled "The E_n circle **partly closes** for simple g" lists five steps, but only step (v) is a theorem and only at the level of formal deformation families. Steps (i) and (iii) are *definitions* (Arrow 1 is not a theorem; Arrow 3 is the application of a functor). The headline in the abstract ("The E_n operadic circle E_3 → E_2 → E_1 → E_2 → E_3 is **proved to close** for simple g") is therefore stronger than the corollary actually says.

**Defense.** The corollary is in fact entitled "partly closes" (L2349) and the body is honest. The abstract elides the qualifier.

**Repair.** Modify abstract (L111–L112) to read "...is **proved to close at the level of formal deformation families** for simple g, conditional on CFG '25." The current "proved to close" without the qualifier reads as a full closure theorem and feeds AP150.

### Claim C5 (the central AP153 violation): Higher Deligne for E_2 inputs

**Attack.** L2014–L2019 invokes "the higher Deligne conjecture proved by Francis: HH^*(A) for an E_n-algebra A carries an E_{n+1}-structure" as the engine of arrow 4. The standalone uses this with A = the boundary E_2-chiral algebra V_k(g). But Francis 2013 (Compos. Math.) proves HDC for E_n-algebras in spectra/chain complexes — *not* for chiral algebras. For chiral inputs, the relevant HDC variant is the one packaged in the standalone's own Thm 3.4 (`thm:e-center-hochschild`), which requires the input to be **E_∞-chiral** (L930: "Let A be an E_∞-chiral algebra"). The standalone's own theorem statement contradicts the standalone's own informal use of HDC.

**Defense.** Vol III's AP153 explicitly warns about exactly this scope inflation: "E_3 algebra structure on Hochschild cochains (Deligne conjecture) applies to E_∞ algebras, NOT to E_1 algebras." The standalone, Section 9, argues that the input is E_∞-chiral on the Koszul locus (all standard families), so HDC applies. But this defense is invoked nowhere in Section 6 (the operadic-circle section). The reader sees Arrow 4 as universal, which it is not.

**Repair.** Two healings:
1. **Restrict scope.** Replace L2014 "An E_2-algebra carries E_3" with "An E_∞-chiral algebra (i.e. all standard vertex algebras: Heisenberg, Kac–Moody, Virasoro, W_N) has its chiral Hochschild cochains carrying E_2 from the chiral direction (Thm 3.4) and, conditional on cohomological topologisation, E_3-top." The arrow becomes arrow-by-arrow honest.
2. **Distinguish two E_3s (AP154).** The arrow-4 E_3 from HDC is the **algebraic** Deligne E_3; the arrow-5 E_3 (input bulk) is the **topological** Costello E_3. Their identification is non-trivial and is precisely Thm 7.4. The current text (L2014–L2026) treats them as the same E_3, which is the AP154 conflation.

### Claim C8: SC^chtop is not E_3 (Rem 4.2)

**Attack.** None — this is the strongest observation in the standalone. It correctly distinguishes Dunn additivity (single-colour) from the two-coloured product structure of FM_k(C) × E_1(m) and explicitly notes the directionality constraint (no open-to-closed) breaks the symmetry. This is the *correct* version of what AP-CY54/AP-CY57 ask for.

**Defense.** None needed.

**Strengthening path (UPGRADE, not retract).** The standalone could promote this remark to an explicit theorem: "**Theorem (No Dunn additivity for SC^chtop):** the directionality constraint SC^chtop(...,top,...;cl) = ∅ obstructs the Dunn additivity isomorphism E_2 ⊗ E_1 ≃ E_3, and the passage from SC^chtop to E_3-top requires the *additional* datum of an inner conformal vector (Section 5)." This is a publishable separation theorem and the cleanest single statement in the operadic-circle architecture.

### Claim C12: Theorem H is internally contradictory for Virasoro

**Attack.** This is the most consequential finding of the audit.

- Standalone Thm 3.6 (`thm:e-theorem-H`, L996–L1013): "Let A be a Koszul chiral algebra. ChirHoch^•(A) is concentrated in cohomological degrees **{0,1,2}**." Three nonvanishing degrees: H^0 = naive centre, H^1 = first-order deformations, H^2 = obstructions.
- Standalone Prop 10.4 (`prop:e-vir-complete`, L3033–L3074): Vir_c has "ChirHoch^* concentrated in {0,1,2}, polynomial."
- BUT chapters/theory/chiral_center_theorem.tex L2025–L2041 (Prop 6.7 stated as `\ClaimStatusProvedHere`): **"ChirHoch^0 = C, ChirHoch^1 = 0, ChirHoch^2 = C·Θ", concentrated in {0,2}** with Hilbert series P(t) = 1 + t^2.

The standalone is wrong about Virasoro, OR the chapter is wrong, OR Thm 3.6 is correct as cohomological **amplitude** (in {0,1,2}) but H^1 happens to vanish for Vir while H^0 and H^2 do not. The third reading is consistent with both, but then standalone L3061–L3063 saying Vir's ChirHoch^* is "concentrated in {0,1,2}, polynomial" is misleading — the actual polynomial is 1 + t^2 (no t term). This propagates to L3151 ("ChirHoch dim ... polynomial" for Vir): the actual dimension is 2, not "polynomial in some t."

**Ghost theorem.** The cohomological amplitude {0,1,2} is *correct as an upper bound* (proved as `thm:hochschild-polynomial-growth` in the chapter, cited as L62 of `chiral_center_theorem.tex`). The exact occupation pattern depends on the algebra: H_k has (1,1,1) (standalone L1031–L1041 and Ex 3.7); KM has (1, dim g, 1) (L1053–L1058); Vir has (1, 0, 1).

**Repair.** Three actions:
1. Reword Thm 3.6 from "concentrated in {0,1,2}" to "**of cohomological amplitude ≤ 2** (i.e. ChirHoch^i = 0 for i ≥ 3)" to match the chapter's terminology and avoid asserting non-vanishing in degree 1.
2. Update Prop 10.4 (`prop:e-vir-complete`) row "ChirHoch^*" to "(C, 0, C), Hilbert series 1 + t^2" with explicit reference to Prop 6.7 of `chiral_center_theorem.tex`.
3. Update Rem 10.6 (`rem:e-glm-comparison`, L3151) "ChirHoch dim ... polynomial" to the actual values: G=3, L=dim(g)+2, M=2 (Vir).

This is a healing UPGRADE: the standalone's main "Theorem H" becomes truer (an amplitude bound, not an occupation claim) and gains a sharper companion (the explicit Hilbert series per family).

### Claim C11: Chiral QG equivalence — γ uses ill-defined canonical element

**Attack.** Thm 9.1, leg γ (L2660–L2667): "The image of R = Σ e_i ⊗ e^i under Δ^ch ⊗ id gives the vertex R-matrix." For an infinite-dimensional chiral algebra, the canonical element Σ e_i ⊗ e^i is not in A ⊗ A^!; it lives in a completion. The standalone never specifies the topology. For the Heisenberg, this is the element exp(k Σ a_n ⊗ a_{-n}/n) ∈ A ⊗̂ A^!, which is well-defined in the formal-power-series completion only because of the level-grading. For Virasoro, there is no comparable explicit form (and the Drinfeld double of Vir is not standard).

**Ghost theorem.** The leg γ is correct on the Koszul locus *with finite-type grading* (which the chapter assumes throughout): the completion is automatic, e_i ⊗ e^i is well-defined as a pro-element. The standalone's standing assumption (L2599–L2604) "On the Koszul locus" implicitly carries this hypothesis, but the proof never names it.

**Repair.** Add to Thm 9.1 the standing hypothesis "with finite-type grading" and replace the bare R = Σ e_i ⊗ e^i by R ∈ Â ⊗̂ Â^!_{conil} with explicit reference to `chiral_center_theorem.tex` standing assumptions (L65–L104).

### Claim C2: Arrow 1 is not a theorem

**Attack.** Def 6.2, arrow (1) (L1989–L1996): "A bulk E_3-top algebra of observables on M^3 restricts to a factorisation algebra on a codimension-2 defect curve C ⊂ M^3." This is asserted as a definition. There is no construction of the restriction map and no proof that the restricted object is E_2-chiral (rather than E_2-topological); the normal bundle giving "one holomorphic + one topological" direction is also asserted, not proved.

**Defense.** The arrow is true in the precise setting of holomorphic–topological field theory: when the bulk is hCS on C × R and the defect is C × {0}, the restriction is the boundary chiral algebra, which is E_2-chiral (the formal disk OPE). This is the Costello–Gwilliam construction.

**Repair.** State arrow 1 as a *proposition*, not a definition: "Proposition (Bulk-to-boundary restriction in HT theory): For an HT field theory on C × R^k with bulk E_3-top algebra A_bulk (k ≥ 2 contributing the topological factor) and a holomorphic boundary C × {0} carrying chiral algebra A_∂, the restriction map A_bulk → A_∂ presents A_∂ as the boundary E_2-chiral algebra of an SC^chtop-pair." Cite Costello–Gwilliam Vol II.

### Cross-cutting attack: The "circle" image is a stack of arrows, not a single object

The five-arrow "circle" eq. (6.1) (L1973–L1983) is a sequence of operations across operadic levels:
- (1) restrict (E_3 → E_2): not a theorem, see C2
- (2) ordered bar B^ord (E_2 → E_1): proved (C3)
- (3) Drinfeld centre Z (E_1 → E_2): correct as functor, but lives at the categorified level (E_1-monoidal cat → E_2-braided monoidal cat), not at the algebra level
- (4) HH^* (E_2 → E_3): scope-inflated (C5/AP153)
- (5) closing: conjectural (C6)

The level mismatch in arrow 3 (output is a *category*, input is an *algebra*) is the most critical structural problem. The standalone never reconciles the level passage. Z(A-mod) is an E_2-braided monoidal CATEGORY; HH^*(...) is an E_3-ALGEBRA; the composite `Z` then `HH^*` is therefore well-typed only if there is an intermediate category-to-algebra map (the End of the identity functor, as L3380–L3388 invokes). This is correct, but the level passage is hidden inside the proof of `lem:e-heis-morita-hochschild` (L3335–L3413). The standalone should make the level zigzag explicit:

```
algebra A (E_1) → category A-mod (E_1-monoidal) → centre Z(A-mod) (E_2-braided monoidal cat)
              → End(id_{Z(A-mod)}) (E_2-algebra) → HH^*(...) (E_3-algebra)
```

**Repair.** Add a "Pentagon of levels" remark adjacent to Def 6.2, making the algebra/category zigzag explicit. Currently this is implicit and is the most readable AP-CY56 violation: at each step, *which object* carries the E_n structure?

---

## Section 3. AP150 audit — Does the standalone confabulate the operadic circle?

**AP150 statement (Vol III CLAUDE.md):** "Agents stitch disparate results into composite structures that do not exist in the literature or the manuscript. Counter: before writing any composite diagram, verify EACH ARROW independently."

**Verdict: PARTIAL CONFABULATION with a real defended core.**

Per-arrow ledger:

| Arrow | Construction | Source | Status | Verdict |
|------|---------|--------|---------|---------|
| (1) E_3-top → E_2-chiral | Restriction along codim-2 defect | Costello–Gwilliam Vol II (uncited) | Definition, not theorem | Plausible but unconstructed in the standalone |
| (2) E_2-chiral → E_1-chiral | Ordered bar B^ord(A) = T^c(s^{-1}Ā) | Princ 3.10 | THEOREM | Genuine |
| (3) E_1-chiral → E_2-braided | Drinfeld centre Z(A-mod) | Standard categorical centre | Functor application | Real; needs level-zigzag clarification (§2) |
| (4) E_2-braided cat → E_3-top alg | HH^* (HDC) | Francis 2013 (cited L2018) | Misapplied (AP153) | Scope-inflated. HDC needs E_∞ input (chapter 3 confirms). On the Koszul locus where input is E_∞-chiral, HDC produces algebraic E_3, not topological E_3-top. The "top" subscript jumps levels. |
| (5) Output E_3-top ≃ Input E_3-top | "Closing" | Conj 11.1 + Thm 7.4 (CFG identification) for simple g, formal deformation families only | CONJECTURAL with a one-case theorem | Honest at the conjecture level; abstract overstates |

**The circle that *can* be defended (steelman):**
> For an E_∞-chiral algebra A on a complex curve C with an inner conformal vector (so that topologisation applies), there is a four-step *zigzag* (not a circle):
> 1. Take the ordered bar B^ord(A) (E_1-chiral coalgebra; PROVED Princ 3.10).
> 2. Take its E_2-monoidal category of comodules Comod(B^ord(A)).
> 3. Take its Drinfeld centre Z(Comod(B^ord(A))) (E_2-braided monoidal cat; standard).
> 4. Take the End algebra of the identity, identified with C^•_ch(A,A) via Hochschild–coHochschild duality (PROVED for class G in `lem:e-heis-morita-hochschild`, L3335).
> Apply the topologisation theorem (Thm 5.1 / 5.5) to obtain E_3-top on the BRST cohomology.
> Conjecturally (Conj 11.1), this matches the bulk E_3-top from the HT field theory in arrow (1).

This zigzag is honest and is in fact what the proofs at L3329–L3736 actually compute. The "circle" framing is rhetorical packaging.

**The circle that is *confabulated*:**

The image E_3 → E_2 → E_1 → E_2 → E_3 as a *single closed diagram* of operadic shifts (eq. 6.1, L1973–L1983) is **not** a theorem in the literature. The closest precedents are:
- Lurie's iterated centre (HA Section 5.3): centres of E_n-algebras carry E_{n+1} structure, but the iteration *increases* n monotonically, never returning.
- Kapustin–Saulina–Witten holography for 3d-2d boundaries: bulk-boundary correspondence for E_3 → E_2, no circle back.
- Costello–Gaiotto's hCS → KM: a single arrow (3) → (2) at the chiral level, no circle.

The "circle" is a Lorgat construction. As presented, it is not a theorem. The honest statement is the four-step zigzag above plus the closing conjecture.

**Per AP150 counter-template:** before writing any composite diagram, verify EACH ARROW independently. The arrows that survive: (2), (3) [as functor], (4) [restricted to E_∞ input], + topologisation (Thm 5.1/5.5). The arrows that fail to survive as theorems: (1) [definition only] and (5) [conjecture]. The circle should be explicitly relabelled as a "diagram of constructions" with arrows tagged Theorem / Definition / Conjecture.

---

## Section 4. AP-CY56 audit — E_n on the right object

**AP-CY56 statement:** at d=3, A is E_1 (NATIVE). E_2 lives on Z(Rep^{E_1}(A)), NOT on A.

The standalone is on a complex *curve* (n = 2 on the dimensional axis, L156–L181), so the d=3 vs d=2 axis from Vol III does not apply directly. But the underlying principle — *which object carries the E_n structure* — applies *across* operadic levels. Audit:

| Object | Standalone claim | Should carry | Verdict |
|--------|------------|----------|--------|
| A (E_∞-chiral input) | E_∞-chiral with R(z) = id (Thm 6.5, L2127) | E_∞-chiral | OK |
| A (E_1-chiral input) | E_1-chiral (notion B, Def 8.1) | E_1-chiral | OK |
| B^ord(A) (ordered bar) | E_1-chiral coassociative coalgebra (Princ 3.10, L1097) | E_1-coalgebra | OK |
| Z^der_ch(A) (derived chiral centre) | E_2 from chiral direction (Thm 3.4, L927) | E_2-algebra | OK |
| (Z^der_ch(A), A) pair | SC^chtop-pair (Princ 3.10, L1107) | SC^chtop-pair | OK |
| H^•_Q(Z^der_ch(V_k(g))) (BRST cohom) | E_3-top (Thm 5.1, L1450) | E_3-top | OK after topologisation |
| Z(A-mod) (Drinfeld centre) | "Categorical Drinfeld centre" (Warning 3.9, L1081–L1084) | E_2-braided monoidal CATEGORY | OK as type, but level zigzag hidden |
| Arrow 4 output | "E_3-top" (eq 6.1, L1982) | Algebraic E_3 from HDC, then conjecturally E_3-top via topologisation | **CATEGORY ERROR** (AP154) |

The arrow-4 category error is the cleanest single AP-CY56 / AP154 violation: the standalone tags Z^der_ch as "E_3-top" when the HDC output is algebraic E_3 and the *topological* E_3 requires the additional step of topologisation (Thm 5.1). The standalone elides this step in eq. (6.1).

**Repair.** Replace eq. (6.1) (L1973–L1983) with an annotated version:

```
E_3-top (bulk, conjectural input)
  → E_2-chiral (boundary, restricted via HT theory; Defn arrow 1)
  → E_1-chiral (B^ord; Thm/Princ 3.10)
  → E_2-braided monoidal cat (Z(A-mod); Drinfeld centre functor)
  → E_3 algebraic (HH^*; Francis HDC, on E_∞-chiral input)
  → E_3-top (after topologisation; Thm 5.1/5.5)
  ≃ E_3-top (input)? (conjecture)
```

Six arrows become explicit; the algebraic-vs-topological E_3 distinction (AP154) becomes visible; the restriction-to-Koszul-locus / E_∞-chiral hypothesis becomes audible at the right step.

---

## Section 5. First-principles analyses (per AP-CY61 / AP186 / AP158)

### Analysis A: "The operadic circle E_3 → E_2 → E_1 → E_2 → E_3 closes for simple g"

- **What it gets RIGHT:** there is a real composite construction (the four-step zigzag of §3) that for simple g at non-critical level produces an E_3-top algebra from the boundary E_∞-chiral algebra V_k(g), and Thm 7.4 identifies this output with the CFG perturbative-CS algebra at the level of formal deformation families parametrised by λ = k + h^∨.
- **What it gets WRONG:** the framing "closes" suggests an equality of E_3-top algebras (input ≃ output) rather than an identification of formal deformation families. Step 4 of the proof of Thm 7.4 (L2322–L2328) is "global extension" from the formal disk, but the formal disk does not see the global topology; the global isomorphism is therefore conjectural beyond the formal series level.
- **Correct relationship:** for simple g at non-critical level, the perturbative-CS bulk E_3-top algebra A^λ from CFG is **isomorphic order-by-order in λ = k + h^∨ to the algebraic E_3 from HDC applied to V_k(g)**, with the identification mediated by the Cartan 3-form (the unique class in H^3(g) for simple g). The full E_3-top equivalence (including topologisation upgrade) is conjectural beyond the formal-family level.
- **Type:** specific/general + chain/cohomology (formal-family identification overstated as global isomorphism; algebraic E_3 conflated with topological E_3-top).

### Analysis B: "Higher Deligne for E_2-algebras is the Francis 2013 theorem"

- **What it gets RIGHT:** Francis's HDC is a real theorem, and it does say that HH^*(A) for an E_n-algebra A carries E_{n+1}.
- **What it gets WRONG:** Francis works in the topological/spectral context (E_n in spaces or chain complexes). For chiral algebras with formal-disk OPE, the analogue is the chiral Deligne–Tamarkin theorem (`thm:chiral-deligne-tamarkin`, chapter L1421), which the standalone *itself* proves only for E_∞-chiral inputs. For E_1-chiral / Yangian-type inputs, the chiral Deligne–Tamarkin theorem is open.
- **Correct relationship:** there are two HDCs at play. (a) Topological HDC (Francis 2013): for E_n in chain complexes, HH^* is E_{n+1}. (b) Chiral HDC (this manuscript, `thm:e-center-hochschild` for E_∞-chiral input, L927). The two coincide on the Koszul locus where the chiral algebra is E_∞-chiral; they diverge for genuinely E_1-chiral algebras (where chiral HDC is open).
- **Type:** algebraic/topological + scope error (two distinct HDCs conflated; topological HDC's scope inflated to chiral E_2 inputs without checking).

### Analysis C: "The Drinfeld centre is the sole source of nontrivial braiding"

- **What it gets RIGHT:** π_1(Conf_2(R^3)) = 1 vs π_1(Conf_2(C)) = Z is a real topological fact; restriction from a 3-manifold to a curve does kill the nontrivial braiding.
- **What it gets WRONG:** "sole source" suggests every nontrivial braiding traces back to a Drinfeld centre. False: the Etingof–Kazhdan vertex R-matrix is a *primary datum* (Notion C of Def 8.1, L2459), not constructed from a Drinfeld centre. Yangian R-matrices arise from Hopf-algebraic structure on Y(g), not from Drinfeld-centre construction (though Drinfeld doubles do produce R-matrices, those are *not* the Yangian R-matrices — see Vol I AP150 cache entry on E_n operadic circle).
- **Correct relationship:** the Drinfeld centre is **a source** (in fact the canonical categorical source) of E_2-braided monoidal categories from E_1-monoidal input. It is not the unique source: braided monoidal categories also arise from (i) modular tensor categories of CFTs, (ii) Yangian module categories with their MO R-matrix, (iii) factorisation-algebra structure on a 2-manifold. "Sole" is an overclaim.
- **Type:** specific/general + necessary/sufficient (one source elevated to the source).

### Analysis D: "SC^chtop is not E_3"

- **What it gets RIGHT:** Dunn additivity E_n ⊗ E_m ≃ E_{n+m} requires single-coloured operads. SC^chtop has two colours with directionality (no open-to-closed), which breaks the symmetry.
- **What it gets WRONG:** nothing significant. This is a clean statement.
- **Correct relationship (UPGRADE):** the obstruction to SC^chtop ≃ E_3-top is precisely the inner-conformal-vector data; topologisation (Thm 5.1) provides this data and effects the passage.
- **Type:** No error. Steelman: this could be promoted to "Theorem (No Dunn additivity for SC^chtop)" — see §2 strengthening.

### Analysis E: "Theorem H concentrates ChirHoch in {0,1,2}"

- **What it gets RIGHT:** the cohomological *amplitude* is ≤ 2 (i.e. ChirHoch^i = 0 for i ≥ 3), which is `thm:hochschild-polynomial-growth` of the chapter (chiral_center_theorem.tex L62).
- **What it gets WRONG:** "concentrated in {0,1,2}" suggests non-vanishing at each of 0, 1, 2. Vir_c has H^1 = 0 (chapter L2025–L2041): "concentrated in {0,2}".
- **Correct relationship:** Theorem H is an *amplitude* theorem (upper bound on the support), not an *occupation* theorem. The exact occupation depends on the algebra. For Heisenberg: (1,1,1). For KM: (1, dim g, 1). For Vir: (1, 0, 1). For DS reductions of KM: (1, 0, 1) (by `prop:DS-ChirHoch-compatibility`, chapter L2344).
- **Type:** label/content + necessary/sufficient (an amplitude bound mislabeled as an occupation pattern; sufficient for non-vanishing somewhere in {0,1,2}, not for non-vanishing at each degree).

---

## Section 6. Three upgrade paths

### Upgrade 1 (LOCAL — restate the circle as a zigzag of theorems and conjectures)

**Action.** Rewrite eq. (6.1) and Cor 7.7 to make every arrow's status explicit. Replace the "circle" rhetoric with an "operadic zigzag" diagram tagged with theorem labels at each step. Promote `Rem 4.2` (SC^chtop is not E_3) to a theorem.

**Strongest correct statement.** "**Theorem (Operadic zigzag for E_∞-chiral algebras with inner conformal vector at non-critical level):** For A an E_∞-chiral algebra on a complex curve, with an inner conformal vector at non-critical level, the four-step composition (B^ord, then Comod, then Drinfeld centre, then End-of-identity = chiral Hochschild) yields the derived chiral centre Z^der_ch(A); BRST cohomology of Z^der_ch(A) carries E_3-top by topologisation (Thm 5.1/5.5). The cohomological closing Z^der_ch(A) ≃ A_bulk^E_3-top from a putative bulk HT theory is proved at the level of formal deformation families for simple g at non-critical level (Thm 7.4) and conjectural (Conj 11.1) in general."

**Healing target.** Convert AP150 from a real risk to a non-applicable warning by making the per-arrow status auditable.

### Upgrade 2 (STRUCTURAL — separate algebraic E_3 from topological E_3-top throughout)

**Action.** Adopt the AP154 template throughout the standalone: every E_3 occurrence tagged as either E_3^alg (Deligne, from HDC on E_∞-chiral input, no conformal vector required) or E_3^top (topologised, requires inner conformal vector). The current text uses "E_3^top" for both, which causes the arrow-4 category error of §4.

**Strongest correct statement.** Two-step E_3 hierarchy: "**Lemma (Two E_3 structures and their identification):** For an E_∞-chiral algebra A on a curve, (a) algebraic Deligne E_3 on Z^der_ch(A) from chiral HDC (this manuscript, Thm 3.4 + Francis 2013 in chain complexes) is well-defined unconditionally; (b) topological E_3-top on H^•_Q(Z^der_ch(A)) is defined when an inner conformal vector exists (Thm 5.1/5.5); (c) under the topologisation hypothesis, the two structures agree on cohomology."

**Healing target.** Eliminate the AP154 conflation across the manuscript. Establish a clean "algebraic E_3 lifts to topological E_3-top under topologisation" interface.

### Upgrade 3 (COMPLETION — close the circle for class M via the coderived category)

**Action.** Reformulate Conj 11.1 (closing) to live in the *coderived* category from the start, rather than asking for ordinary chain-level chiral Hochschild equality. Rem 5.10 already identifies the coderived category as the expected absorber of the class-M obstructions; promote this from a remark to a working hypothesis throughout.

**Strongest correct statement.** "**Conjecture (Coderived closing):** For every E_∞-chiral algebra A with inner conformal vector at non-critical level, the operadic zigzag closes in the coderived category D^co(E_3-top): there is an isomorphism Z^der_ch(A) ≃ A_bulk in D^co(E_3-top) of the bulk E_3-top algebra of any HT field theory whose boundary chiral algebra is A. Reduces to Thm 7.4 (formal-family identification) for simple g at non-critical level, after specialisation to the formal series subcategory."

**Healing target.** Make the closing conjecture refutable by tying it to a specific category in which both sides live (currently the conjecture's category of equivalence is unspecified, which is the AP-CY56 violation that lets it absorb counterexamples).

---

## Section 7. Consolidated punch list

Sorted by severity, healing-first:

| # | Item | File | Line | Action | Severity |
|---|------|------|------|--------|----------|
| P1 | Standalone Vir ChirHoch contradicts chapter (Vir has H^1=0, not C) | en_chiral_operadic_circle.tex | 996–1013, 3033–3074, 3151 | Reword Thm 3.6 to "amplitude ≤ 2". Update Vir entries to (1,0,1). | HIGH |
| P2 | Abstract overstates "circle proved to close" | en_chiral_operadic_circle.tex | 111–112 | Add qualifier "at the level of formal deformation families, conditional on CFG '25" | HIGH |
| P3 | Eq. (6.1) circle elides algebraic/topological E_3 distinction (AP154) | en_chiral_operadic_circle.tex | 1973–1983 | Rewrite as 6-arrow zigzag with each arrow tagged | HIGH |
| P4 | Arrow 1 stated as definition, not theorem | en_chiral_operadic_circle.tex | 1989–1996 | Promote to proposition citing Costello–Gwilliam Vol II | HIGH |
| P5 | Arrow 4 (HDC) scope-inflated to non-E_∞ inputs (AP153) | en_chiral_operadic_circle.tex | 2014–2019 | Restrict to E_∞-chiral input; cite Thm 3.4's standing hypothesis explicitly | HIGH |
| P6 | "Drinfeld centre is sole source of braiding" overclaim | en_chiral_operadic_circle.tex | 2009–2013, 2030–2079 | Replace "sole" with "canonical categorical"; list Yangian/MTC/factorisation-algebra alternatives | MED |
| P7 | γ leg of Thm 9.1 uses ill-defined Σ e_i ⊗ e^i | en_chiral_operadic_circle.tex | 2660–2667 | Add finite-type-grading hypothesis; replace by completed pro-element | MED |
| P8 | "Closing" Conj 11.1 unspecified ambient category | en_chiral_operadic_circle.tex | 3178–3195 | Rephrase in coderived category (per Rem 5.10) | MED |
| P9 | Stalk-wise reduction Lemma 11.6 for class L only sketches the m_4 vanishing | en_chiral_operadic_circle.tex | 3518–3543 | Strengthen via cohomological vanishing argument from `thm:hochschild-polynomial-growth` | MED |
| P10 | Cor 7.7 titled "partly closes" but body says "closing the circle" (step v) | en_chiral_operadic_circle.tex | 2349, 2364–2369 | Reword step (v) "closing the circle at the level of formal deformation families" | MED |
| P11 | Rem 4.2 (SC^chtop is not E_3) is a hidden gem | en_chiral_operadic_circle.tex | 1192–1204 | Promote to numbered theorem | LOW (upgrade) |
| P12 | "Pentagon of equivalences" (Rem 4.6) admits no pentagon theorem closes 5 directly | en_chiral_operadic_circle.tex | 1303–1314 | Either prove the pentagon or rename "Star of equivalences through operadic hub" | LOW |
| P13 | Five-notions warning (Warning 8.3) is well-done | en_chiral_operadic_circle.tex | 2531–2556 | Keep; cite as model for AP-CY-style hygiene | (model) |
| P14 | Three-Hochschild warning (Warning 3.9) is well-done | en_chiral_operadic_circle.tex | 1067–1092 | Keep; expand to mention Gel'fand–Fuchs as a fourth (per chapter L2037) | LOW |
| P15 | CFG '25 cited as "in preparation" — Thm 7.4 conditional | en_chiral_operadic_circle.tex | 3804–3806, 2264–2329 | Mark Thm 7.4 as `\ClaimStatusConditional` on CFG '25 | HIGH |
| P16 | "Original-complex chain-level lift" remains open for class M (Conj 5.2) | en_chiral_operadic_circle.tex | 1550–1572, 1876–1881 | Already honest; cross-reference to AP-CY51 Vol III for parallel chain-vs-cohomology gap | LOW |

**Two non-actionable observations (steelmen):**

- **S1.** The standalone is structurally honest in its hardest places: the SC^chtop ≠ E_3 remark, the three-Hochschild warning, the five-notions warning, and the layered (cohomological / model / original-complex) chain-level analysis are all examples of the manuscript anticipating its own AP failure modes. The defects are concentrated in the rhetorical packaging (abstract, eq 6.1, Cor 7.7), not in the proof content.
- **S2.** The four-step zigzag of §3 (B^ord → Comod → Z → End-of-id = chiral Hochschild) is genuinely new mathematics. Even after retracting the "circle" rhetoric, the manuscript supports an Inventiones-grade theorem on the operadic zigzag. The healing should preserve this.

---

## Footer — sources cross-checked

- AP150 (Vol III CLAUDE.md, L1097–L1108 of CLAUDE.md as injected): "agent confabulation of an E_n operadic circle E_3 → E_2 → E_1 → E_2 → E_3 that does not exist in any manuscript." → addressed throughout §3, §6.
- AP153 (Vol III CLAUDE.md, L1113–L1119): "E_3 algebra structure on Hochschild cochains (Deligne conjecture) applies to E_∞ algebras, NOT to E_1 algebras." → addressed in §2 C5, §5 Analysis B, §7 P5.
- AP154 (Vol III CLAUDE.md, L1121–L1128): "two distinct E_3 structures (algebraic Deligne vs topological Sugawara)." → addressed in §4, §5 Analysis B, §6 Upgrade 2, §7 P3.
- AP-CY56 (Vol III CLAUDE.md, L1130–L1135): native vs derived object. → addressed in §4.
- V2-AP21/22/23 (Vol III CLAUDE.md): hierarchy Comm < PVA < E_∞-chiral < P_∞-chiral < E_1-chiral. → standalone L153–L159 reproduces hierarchy correctly.
- Vol I AP150 (Vol III CLAUDE.md): "every claimed multi-step structure must be verified arrow-by-arrow." → addressed in §3 ledger.

The wrong-claim pattern most worth caching for future agents:

> **A multi-step composite of operadic functors (B^ord, Drinfeld centre Z, HH^*) is presented as a "circle" returning to its starting level. The composite is well-defined as a zigzag of constructions; the closing is a conjecture identifying the output's E_n level with a separate input's E_n level. The conflation of the two E_3s (algebraic Deligne from HDC vs topological Sugawara from inner conformal vector) is the source of the apparent closure: the output is naturally algebraic E_3, and only after topologisation becomes E_3-top, where it can plausibly be identified with the bulk E_3-top input.**

This would be a worthwhile cache entry under "construction/narration + algebraic/topological".
