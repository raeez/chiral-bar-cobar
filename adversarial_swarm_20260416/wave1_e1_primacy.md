# Adversarial Wave 1 — The "E_1 Primacy / Ordered Bar" Pillar

**Date:** 2026-04-16
**Auditor:** adversarial referee, swarm wave 1
**Files audited:**

- `/Users/raeez/chiral-bar-cobar/standalone/e1_primacy_ordered_bar.tex` (2423 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex` (1034 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex` (7699 lines, sampled)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex` (11790 lines, sampled)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex` (2505 lines, sampled)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_construction.tex` (2536 lines, sampled)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex` (3491 lines, not deeply read)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex` (4959 lines, sampled)

**Anti-pattern checklist used (from CLAUDE.md):** V2-AP1, V2-AP2, V2-AP3, V2-AP4, V2-AP21, V2-AP22, AP152, AP-CY3, AP-CY4, AP-CY23, AP-CY56, AP-CY57, AP153, AP155, AP126.

**Headline finding.** The "E_1 primacy" pillar is *architecturally sound* but suffers from one global structural problem and roughly a dozen scope/precision violations that the manuscript has *already catalogued in its own AP list and partially honored in chapters/* — yet which it then *re-violates* in the standalone reformulations (`e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex`). The damage is concentrated in the standalone files; the integrated chapter (`ordered_associative_chiral_kd.tex`) handles the same material correctly. The healing path therefore is mostly *not* to retract the standalones but to backport the chapter-level discipline into them.

---

## Section 1 — Triage table

Severity scale: **WRONG** = mathematical error or contradiction; **WEAK** = correct but unsupported / scope-creeping; **NEEDS-TIGHTENING** = correct but invites misreading (AP violation by the manuscript's own catalogue); **SAFE** = stable for an Annals-class statement.

| # | Claim | File | Status |
|---|------|-----|-------|
| 1 | Ordered bar `B^ord(A) = T^c(s^{-1} A_bar)` with deconcatenation is the *primitive* object of modular Koszul duality | e1_primacy §1; N3 §1 | NEEDS-TIGHTENING |
| 2 | "Symmetric bar `B^Sigma(A)` is the `Sigma_n`-coinvariant image of `B^ord(A)` under av" | e1_primacy §3; N3 §3 | **WRONG** (V2-AP4: descent is R-twisted, not naive coinvariant) |
| 3 | Av : g^{E_1} → g^{mod} is a surjective dg Lie morphism | e1_primacy thm 4.2; N3 thm 4.3 | NEEDS-TIGHTENING (depends on #2) |
| 4 | av(r(z)) = κ(A) for Heisenberg; for non-abelian KM = κ_{dp} = k·dim(g)/(2h^v) | e1_primacy thm 4.4; N3 thm 4.4 | NEEDS-TIGHTENING (computation correct but provenance argument asymmetric) |
| 5 | av(Φ_{KZ}) = C(A); kernel = [Ω_{12}, Ω_{23}] | e1_primacy thm 4.5; N3 thm 4.6 | NEEDS-TIGHTENING (proof references Vol I, no chain-level check) |
| 6 | Non-splitting: 4 obstructions, including GRT_1 torsor + E_2 anomaly at genus 1 | e1_primacy prop 4.7 + 4.8 | WEAK (each obstruction stated but combined non-splitting argument is not assembled — ses splits at degree level individually) |
| 7 | Tier (b) ⊂ E_∞ chiral: KM, Vir, β-γ, W; "R-matrix derived from local OPE" | e1_primacy §6.5 (Tier b); N3 §7 | NEEDS-TIGHTENING (V2-AP1 / V2-AP10 — wording verges on saying VAs are E_∞ but not E_1, which is harmless; but tier (b) text simultaneously says "the kernel is nontrivial but reconstructible from A" — see #15) |
| 8 | Tier (c) genuinely E_1 = Yangian, EK quantum VA; *symmetric bar does not exist* | e1_primacy §7; N3 §7; ordered_chiral_homology §motivating | SAFE (this is the correct strict E_1 example) |
| 9 | Three coalgebra structures: Harrison coLie / coshuffle Sym^c / deconcatenation T^c | e1_primacy def 2.1; N3 def 2.1 | SAFE |
| 10 | Theorem A^{E_1}: ordered bar carries `F\Ass`-coalgebra; bar–cobar adjoint to `F\Ass`-coalgebras | e1_primacy thm 5.1; N3 §5 | NEEDS-TIGHTENING (the adjunction is asserted but the *coderived category* setup is missing — V2-AP31 calibre proof tag) |
| 11 | Theorem B^{E_1}: ordered inversion on Koszul locus | e1_primacy thm 5.2; N3 thm 5.3 | NEEDS-TIGHTENING (PBW-completeness hypothesis stated but never proved for the genuinely-E_1 examples) |
| 12 | Theorem C^{E_1}: ordered complementarity formula `Q + Q^! = H^*(M_{g,n}^{rib}, Z^{E_1}(A))` | e1_primacy thm 5.3; N3 thm 5.4 | **WRONG STATEMENT or WEAK as theorem** (Z^{E_1}(A) "the space of R-matrix-equivariant elements" is undefined in the file; circularity risk) |
| 13 | Theorem D^{E_1}: degree-2 package + scalar shadow recovery | e1_primacy thm 5.4; N3 thm 5.5 | NEEDS-TIGHTENING (genus-2 multi-weight cross-channel correction explicitly tagged ALL-WEIGHT but tag is empty — AP32 aware but unproved) |
| 14 | Theorem H^{E_1}: ordered chiral Hochschild | e1_primacy thm 5.5; N3 thm 5.6 | NEEDS-TIGHTENING (depends on #2 + UNIFORM-WEIGHT/ALL-WEIGHT discipline is asserted but not enforced) |
| 15 | Tier (b) "R(z) is fully determined by E_∞ vertex algebra structure; E_1 refinement adds no new data at degree 2 beyond what is in OPE" | e1_primacy §6.5 last sentence; N3 §7 | **WRONG** (V2-AP2 violation in the *positive* direction: the *kernel* of av and the chain-level associator are not zero for KM/Vir even though R(z) is OPE-derived; the manuscript claims kernel = 0 here, contradicting its own §4 non-splitting at the same point) |
| 16 | Heisenberg: r(z) = k/z, κ = k, kernel(av_2) = 0; ordered = symmetric | e1_primacy ex 2.4 + §8.1; N3 §8 | **CONVENTION CLASH** (V2-AP14 / AP151) — `ordered_associative_chiral_kd.tex` thm 17 says ordered Heisenberg bar is *curved* with `m_0 = k|0>` and `R(z) = exp(k\hbar/z)`; standalone files have `m_0 = 0` and `R(z) = k/z` (linear, not exponentiated). |
| 17 | "E_1 primacy" thesis itself | e1_primacy princ 5.7; N3 princ 5.8 | NEEDS-TIGHTENING (semantic ambiguity in word "primitive" — see Section 2.A) |
| 18 | Chiral quantum group equivalence triangle (R / A_∞ / Δ_z) | e1_primacy thm 9.1; N3 ch 9 | WEAK (the equivalence is "up to Φ" and concretely verified only for sl_2; Vol III status of CY-C is conjectural, and the present formulation does not flag the dependence) |
| 19 | Universal Miura coefficient (Ψ−1)/Ψ on cross-term, independent of spin | e1_primacy thm 9.4 | NEEDS-TIGHTENING (proof step 2 has a sign-juggling line: "+1−1 = +1" without explicit verification; numerical cross-check claim states "spins 2,3,4,5,6" but no engine cited) |
| 20 | Verlinde recovery: Z_g(k) = Σ_j S_{0j}^{2−2g} | e1_primacy prop 9.5 | **WRONG PROOF LINE** + AP155 violation. The proof sentence "S-matrix unitarity Σ_l S_{jl}^2 = δ_{j0}" is mathematically false (unitarity gives Σ_l S_{0l}^2 = 1, not δ_{j0}). Also: this is BD/Bernard recovery, NOT a *new* theorem; AP155 says do not overclaim. |
| 21 | Yangian unitarity: R(u)R(−u) = (u² − ℏ²)I_4 | e1_primacy ex 8.5 line 1881 | **SIGN CONFLICT** with `ordered_chiral_homology.tex` line 625 which has R_{12}(u)R_{21}(−u) = (ℏ² − u²)I (and lines 3833, 4015–4016, 4191 also use ℏ²−u²) |
| 22 | "ordering records the topological direction R_t" — `E_1` = "time-ordered product" | `ordered_associative_chiral_kd.tex` line 2131 | **WRONG / AP152 VIOLATION** ("time-ordered" vs "labeled-ordered" conflated) |
| 23 | "Cyclic chiral algebra" used as input for primacy theorems | e1_primacy thm 5.7 line 1055 | NEEDS-TIGHTENING (E_1-chiral *or* cyclic? scope drift — Definition 3.1 inputs "strongly admissible E_1-chiral", but Theorem 5.7 inputs "cyclic chiral algebra"; not the same class) |
| 24 | Spectral coassociativity `(Δ_{z_1}⊗id)Δ_{z_1+z_2} = (id⊗Δ_{z_2})Δ_{z_1}` | e1_primacy eq 9.2 (line 1953) | **WRONG** (in the *strict* form claimed, this is incompatible with the same paper's later statement that Δ_z is coassociative *only up to* the Drinfeld associator Φ — see ordered_chiral_homology.tex lines 738–749 which give `Φ_{123}` correction. The standalone version drops the Φ.) |
| 25 | Kernel dimension formula dim ker(av_n) = d^n − C(n+d−1, d−1) | e1_primacy rem 4.9 (1025–1043) | NEEDS-TIGHTENING (says "depends only on dim V, not on Lie-algebraic structure" — true on `V^⊗n` but the kernel of av on the *full ordered bar* depends on the chain-level differential, not just on V; conflation. Furthermore, the formula does not match the ordered_chiral_homology computation that gives ker(av_2) ≅ ⋀²V on sl_2 = 1-dim, consistent only because d=2.) |
| 26 | "BarSig(A) does not exist" for genuinely E_1 (Yangians) | e1_primacy thm 7.2(ii) | SAFE (correct interpretation of V2-AP4; but should be cross-referenced to the *Vol I chapter* `ordered_associative_chiral_kd` Prop 8.6 + Cor 8.7) |
| 27 | Three tiers (a)–(c) | e1_primacy §6; N3 §7 | NEEDS-TIGHTENING (Tier (a) "pole-free" pseudo-class is uninhabited by anything interesting; the *real* dichotomy is pole-free vs all-the-rest, not three tiers; and tier (b) says "ordered and symmetric bar complexes are quasi-isomorphic in this tier" — true at *cohomology*, false at *chain* level) |
| 28 | Av is dg Lie surjection ⇒ MC element projects to MC element | e1_primacy thm 4.6 | SAFE |
| 29 | Drinfeld associator inhabits ker(av) at degree 3 | e1_primacy prop 4.7(iii) | SAFE (this is a real theorem of Drinfeld; the contribution here is the *convolution-algebra* repackaging) |
| 30 | E_2 emerges on Drinfeld center of Rep^{E_1}(A) | NOT IN FILE — AP-CY56 negative finding | **MISSING** — neither e1_primacy nor N3 mentions that the E_2 braided structure on representations is the *derived* one (Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_ch(A))). The architecture talks about R-matrices and braiding but never identifies *which object carries the E_2*. AP-CY56 violation by *omission*. |

**Tally.** Out of 30 claims: SAFE = 5; NEEDS-TIGHTENING = 16; WEAK = 3; WRONG = 5 (#2, #12, #15, #20, #24); MISSING = 1 (#30); CONVENTION CLASH = 1 (#16); SIGN CONFLICT = 1 (#21).

---

## Section 2 — Per-claim detailed analysis

### 2.A. The "primacy" word (Claim #1, #17, attack/defense from your prompt §1)

**Attack.** In the categorical hierarchy E_∞ → E_n → ... → E_1, the *most* structured object is E_∞ (commutative); the *least* structured is E_1 (associative non-commutative). To call the *least* structured object "primitive" is a vocabulary inversion that misleads any reader trained on the standard ladder. The text wants to say "least restrictive / most general" but writes "primitive". Worse, "primitive" in coalgebra theory has a specific meaning (elements x with Δx = x⊗1 + 1⊗x); the deconcatenation coproduct's primitives are *V* itself, not the whole T^c(V).

**Defense (= the strongest correct statement).** The intended sense is "E_1 is the *initial* object in the chain `E_∞ ⊃ E_n ⊃ ... ⊃ E_1`": every E_∞-chiral algebra is automatically E_1-chiral by forgetting the Σ_n-equivariance of operations, and the bar functor commutes with this forgetful functor at the level of *underlying graded vector space*. The asymmetry that the standalone calls "primacy" is the asymmetry of the two-sided bar adjunction: B^ord retains data B^Σ throws away (the R-matrix), and that data is the *only* additional input you need to pass between E_1 and E_∞.

The mathematically clean statement is therefore **not** "E_1 is primitive" but:

> **Reformulation.** *The forgetful functor `Forget : E_∞-ChirAlg → E_1-ChirAlg` admits a left adjoint `Sym^{ch} : E_1-ChirAlg → E_∞-ChirAlg` (the chiral symmetrization). The bar functor B^ord on E_1-chiral algebras factors through the forgetful direction: B^Σ ∘ Sym^{ch} = B^ord on the image of Sym^{ch}. The data `(B^ord, av)` is the universal pair recording how a generic E_1-chiral algebra fails to be E_∞.*

Then "primacy" is just the existence of the right adjoint to the av map; it is not a statement that E_1 is "more primitive" than E_∞.

**Repair.** Replace every occurrence of "primitive" with one of:
- "underlying" (as in: E_1 is the underlying associative structure of an E_∞-chiral algebra),
- "least-symmetric",
- "generic" (E_1-chiral is the generic input class).

The word "primacy" in the title can stay but it should be defined explicitly in Section 1 as *adjoint primacy* (the universal property of forgetting Σ_n-equivariance), not as "more fundamental than E_∞".

### 2.B. The R-twisted descent contradiction (Claim #2 — WRONG)

**Attack.** `e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex` repeatedly assert that `B^Σ(A) = (B^ord(A))_{Σ_n}` (naive coinvariants):

- e1_primacy line 92: "is its `Σ_n`-coinvariant image"
- e1_primacy line 137: "`Σ_n`-coinvariant projection of the ordered bar complex"
- e1_primacy line 207: "each symmetric theorem is the `Σ_n`-coinvariant image of its ordered counterpart"
- e1_primacy line 392: definition of av is `(1/n!)Σ_σ σ·φ(g,n)` — the *naive* Reynolds operator
- N3 lines 88–93, 134, 149, 281, 349, 359, 388, 432, 457, 562, 605, 619, 657, 695, 885, 962: same language throughout.

Meanwhile **the same author's chapter** `ordered_associative_chiral_kd.tex` has Proposition 8.6 (line 505 ff.) **R-matrix twisted descent**:
```
B^Σ(A)_n ≃ (B^ord(A)_n)^{R-Σ_n}
```
with action `σ_i · (a_1 ⊗ ... ⊗ a_n) = τ_{i,i+1} ∘ R_{i,i+1}(z_i − z_{i+1}) (a_1 ⊗ ... ⊗ a_n)` (line 519–523), and Corollary 8.7 explicitly states that **only the pole-free case** reduces to the naive coinvariants:

```
For E_∞-chiral algebras with OPE poles (...) the descent is genuinely R-twisted.
```
(line 671)

**This is V2-AP4 violated by the standalone file**, in direct contradiction with the chapter proof of the very same fact. AP4 explicitly: "Ordered-to-unordered descent is R-matrix twisted: `B^Σ_n = (B^ord_n)^{R-Σ_n}`. Naive quotient only for pole-free."

**Defense (= upgrade path).** The standalone is doing *something* coherent: it is computing the av map *in cohomology*, where for E_∞-chiral algebras the formality bridge of Theorem 6.1 (line 1297 of e1_primacy) makes the chain-level twist disappear. For E_∞ tier (b), at the level of bar *cohomology*, the naive coinvariant projection and the R-twisted projection have isomorphic image. The standalone is implicitly working in this cohomological regime and has dropped the chain-level qualifier.

**Strongest correct version.** Restate every "av(...) = ..." identity in two registers:

1. **Chain level (universal):** av_n is the R-twisted symmetrization
   `av^R_n(φ) = (1/n!) Σ_{σ∈Σ_n} ρ_R(σ) · φ(g,n) ∘ ι^{rib}_{g,n}`
   with `ρ_R(σ_i) = τ_{i,i+1} ∘ R_{i,i+1}(z_i − z_{i+1})`. This is well-defined as a Σ_n-action iff R satisfies YBE + strong unitarity (Prop 8.6 of `ordered_associative_chiral_kd`).

2. **Cohomological (E_∞ tier (b)):** for any E_∞-chiral algebra with OPE poles, the formality bridge induces a quasi-isomorphism `(B^ord(A)_n)^{R-Σ_n} ≃ (B^ord(A)_n)_{Σ_n}` between R-twisted invariants and naive coinvariants. Only at this level does the formula `av = (1/n!) Σ σ` hold.

3. **Genuinely E_1 tier (c):** the R-twisted action is the *only* sensible action; the naive coinvariant has no meaning; B^Σ(A) does not exist.

The repair is *one definition + two corollaries*. It is not a downgrade; it is a healing that brings the standalone in line with the rigorous chapter and absorbs V2-AP4 into the central theorem.

**Repair location.** e1_primacy Definition 4.1 (line 421) of av; replace formula (4.2) with the R-twisted version + cite Prop 8.6 of `chapters/theory/ordered_associative_chiral_kd.tex`. Same edit in N3 Definition 4.1 (line 722).

### 2.C. The E_∞ tier (b) "no new data" claim (Claim #15 — WRONG)

**Attack.** e1_primacy lines 776–784:

> "In each case `r(z)` is fully determined by the underlying `E_∞` vertex algebra structure; the `E_1` refinement adds no new data at degree 2 beyond what is already visible in the OPE."

This is V2-AP2 inverted. V2-AP2 says: "R(z) ≠ τ does NOT imply genuinely E_1." The standalone is making the *converse* implicit claim: "E_∞ ⇒ R(z) is recoverable from the OPE ⇒ no genuinely new data at degree 2." But §4.7 of the same paper (Proposition 4.7, the non-splitting proposition, line 911 ff.) lists *four* obstructions to splitting, all of which apply equally to E_∞-chiral input (KM at any level k ≠ 0 has nonvanishing Drinfeld associator in ker(av_3)). The kernel of av at degree 2 is the antisymmetric part of r(z), which for non-abelian KM is nonzero (line 723–727).

The two passages are in direct internal contradiction: §6.5 says ker(av) reconstructible from A; §4.7 says ker(av) contains GRT_1 ambiguity invariant.

**Defense.** The intended (correct) statement is that for E_∞-chiral input, the chain-level r(z) is *uniquely* determined by the OPE *as a meromorphic 2-tensor* — i.e., the choice of r(z) is rigid — but the *bar-level data* it carries (the chain-level R-matrix as descent datum, the associator as degree-3 MC component) does *not* descend to the symmetric bar. The healing rephrases:

> *For tier (b), `r(z)` is determined by the OPE up to formality. The ordered bar carries chain-level R-matrix data that becomes trivial under cohomological averaging; this is the content of Theorem 6.1 (formality bridge).*

**Repair location.** e1_primacy lines 776–784. Strike the sentence "the E_1 refinement adds no new data at degree 2 beyond what is already visible in the OPE." Replace with: "the chain-level r(z) is determined by the OPE; what changes between the ordered and symmetric bar is the *chain-level R-matrix datum* and the degree-3 associator, both of which become trivial in cohomology by Theorem 6.1." This converts the false "no new data" line into a precise statement that aligns with §4.7.

### 2.D. The Heisenberg curvature/exp(R) convention clash (Claim #16 — CONVENTION CLASH)

**Attack.** Three different presentations of the Heisenberg ordered bar coexist:

- **Standalone e1_primacy.tex** (Example 2.4, line 367 ff.; §8.1, line 1645 ff.): linear, *uncurved*, `r(z) = k/z`, `κ = k`. The bar differential is "the collision residue" — there is no `m_0` mentioned.

- **Standalone N3.tex** (lines 472–497, 1645 ff.): same — linear, uncurved, `r(z) = k/z`.

- **chapters/theory/ordered_associative_chiral_kd.tex** (Theorem 17, line 2180 ff.): **curved cofree coalgebra** `(T^c(s^{-1}V), d_{Bar}, m_0, Δ)` with `m_0 = k|0⟩`, `d_{Bar}([s^{-1}J|s^{-1}J]) = 0` (degree-2 differential vanishes!), and **R(z) = exp(k\hbar/z)** as the exponentiated form.

- **standalone/holographic_datum.tex** line 551, **standalone/drinfeld_kohno_bridge.tex** lines 320, 1492, **standalone/survey_modular_koszul_duality_v2.tex** line 6676: all use **R(z) = exp(k\hbar/z)** consistently.

So *every* file in the project uses the curved/exponentiated form *except* the two newest standalones (e1_primacy, N3) that promote the "primacy" thesis. This is V2-AP14 (oscillation between conventions in single session) and AP151 (convention clash within file).

**Defense / upgrade.** The two presentations are equivalent at cohomology but differ at chain level. The curved version is *more honest* about the bar-cobar structure (it correctly accounts for the central extension by acknowledging `J_{(1)}J = k` is a scalar that escapes the augmentation ideal). The linear version is *more directly comparable* to the symmetric bar of Vol I Theorem A (where κ appears as the scalar `d[s^{-1}J|s^{-1}J] = k` in the augmentation differential).

**Strongest version.** Pick one convention *for the standalone* and either:

(a) Adopt the curved-coalgebra version uniformly. Then `r(z) = k/z` becomes the *infinitesimal* generator and `R(z) = exp(k\hbar/z)` is its exponentiation; both should appear. This matches `ordered_associative_chiral_kd` and the rest of Vol I.

(b) Keep the linear version but explicitly cite the curved version with a one-paragraph bridge identity. Note that the bar cohomology is the same; the chain models differ.

Currently the standalone reads as if the curved presentation does not exist. This is a false impression of the underlying mathematics.

**Repair location.** e1_primacy Example 2.4 (line 367) and §8.1 (line 1645 ff.); N3 lines 472–497. Insert a "Convention" environment naming both presentations and choosing one. Cite `ordered_associative_chiral_kd.tex` Theorem 17.

### 2.E. The Verlinde "recovery" — proof error + AP155 (Claim #20 — WRONG)

**Attack.** e1_primacy line 2231–2232 (proof of Proposition 9.5):

> "At genus 0: the S-matrix unitarity Σ_l S_{jl}^2 = δ_{j0} gives Z_0 = 1."

Mathematical error. S-matrix unitarity is `Σ_l S_{jl} \overline{S_{kl}} = δ_{jk}`. Specializing to j = k = 0 gives `Σ_l |S_{0l}|^2 = 1` (since S is symmetric and real for sl_2, Σ_l S_{0l}^2 = 1). The formula `Σ_l S_{jl}^2 = δ_{j0}` would require `S_{0l}^2 = δ_{l0}`, which is false: for sl_2 at level 1, all S_{0j} = 1/sqrt(2). The correct argument for `Z_0 = 1` is *not* unitarity but **Frobenius reciprocity** (the fusion category has a unique vacuum), or equivalently the trace formula at g=0 with no insertions which is computed differently.

**AP155.** The Verlinde formula `Z_g = Σ_j S_{0j}^{2-2g}` is Verlinde 1988, Witten's TQFT, Bernard 1988 (genus 1 with KZ), Felder 1994 (KZB). This is *not* a new result of the present paper. The standalone calls it "Verlinde recovery from ordered chiral homology" — but the construction recovers a *known* invariant via a *new* construction path, which AP155 mandates be flagged. The current presentation reads as if ordered chiral homology gives a new derivation; the *novelty* is architectural, not the formula.

**Defense / repair.** Two healings:

1. Fix the proof line: replace "S-matrix unitarity Σ_l S_{jl}^2 = δ_{j0}" with "Frobenius reciprocity in the modular tensor category Rep_{int}(V_k(sl_2)) gives a unique vacuum at genus 0, so Z_0 = 1."

2. Add an AP155 disclaimer: "Proposition 9.5 *recovers* the Verlinde formula (originally due to Verlinde 1988, Witten 1989, Bernard 1988, Felder 1994) via the ordered chiral homology construction. The formula is classical; the contribution here is the new derivation path through the chiral bar complex on `\overline\cM_g`."

### 2.F. The spectral coassociativity claim (Claim #24 — WRONG)

**Attack.** e1_primacy equation (9.2), line 1953–1956:
```
(Δ_{z_1} ⊗ id) ∘ Δ_{z_1+z_2}  =  (id ⊗ Δ_{z_2}) ∘ Δ_{z_1}
```
This is asserted as an axiom in the *strict* form (no associator). But:

- `ordered_chiral_homology.tex` line 738–749 says:
  ```
  (Δ_{z_1} ⊗ id) ∘ Δ_{z_2} = Φ_{123}(z_1,z_2) · (id ⊗ Δ_{z_2}) ∘ Δ_{z_1} · Φ_{123}(z_1,z_2)^{-1}
  ```
  i.e., coassociative *only up to* the Drinfeld associator Φ_{123}.

- The Drinfeld associator obstruction is the entire content of §4 non-splitting. It cannot also be absent from §9.

**Defense / repair.** The strict-coassoc version (e1_primacy 9.2) holds for the *Yang* R-matrix coproduct on the Yangian *up to a regular gauge equivalence* in a specific normalization, but only after passing to the cohomological derived center where Φ acts trivially. The chain-level coassoc requires Φ.

**Repair.** Replace eq (9.2) with the Φ-conjugated version. Add a remark: "At the chain level, (9.2) holds up to the Drinfeld associator Φ_{KZ}; only after passage to cohomology (or after fixing a Φ-trivialisation, equivalently a GRT_1-trivialisation) does the strict identity hold." This is consistent with §4.7(iv) and with `ordered_chiral_homology.tex`.

### 2.G. The non-splitting proposition (Claim #6 — WEAK)

**Attack.** Proposition 4.7 of e1_primacy lists four "obstructions to splitting":
- (i) fixed-degree triviality: extension is Lie-trivial at each n separately
- (ii) cross-degree obstruction: bar differential breaks Σ_n-equivariance
- (iii) associator representative: [Ω_{12},Ω_{23}] ∈ ker(av)
- (iv) GRT_1 torsor structure of splittings

But (i) admits a section *at each n*, (ii) merely says the section is incompatible with d_{bar}, (iii) is consistent with the existence of *some* section by the freeness of the inclusion — and (iv) is a *parametrisation* of sections, not a non-existence result.

The combined logic "no Lie section exists" is *not* assembled in the proof. The proof gives:
- (i) shows the obstruction 2-cocycle vanishes ⇒ section exists at each n;
- (ii) says it doesn't intertwine d ⇒ no compatible chain-level section;
- (iii) says any such section must include Φ_{KZ} component;
- (iv) says space of compatible sections is GRT_1-torsor.

But (iv) implies the space of sections is *non-empty* (every torsor is) — this contradicts the headline "non-splitting"! The theorem is consistent with the existence of *many* sections, parametrised by GRT_1.

**Defense.** The healing reads: "The extension does *not* split *canonically*; it has a non-trivial GRT_1-torsor of compatible Lie sections." This is a much stronger and more interesting statement. The current "does not split" prose is too weak/wrong.

**Repair.** Reword Proposition 4.7 as:

> **Proposition 4.7' (Sections of av).** *The short exact sequence of dg Lie algebras*
> *0 → ker(av) → g^{E_1} → g^{mod} → 0*
> *admits a non-canonical Lie section. The space of Lie sections compatible with the Maurer–Cartan equation is a torsor for the pro-unipotent Grothendieck–Teichmüller group GRT_1. At genus 1 a fourth class of sections is obstructed by the quasi-modular anomaly E_2 → \widehat E_2.*

This is the *strongest correct statement* and removes the false "does not split" headline.

### 2.H. AP-CY56 missing-E_2 finding (Claim #30 — MISSING)

**Attack.** The architecture in the standalone paper repeatedly invokes "the braided monoidal structure on the category of A-modules" (e1_primacy lines 211, 1241, 1291, 1429, 1533) — but **never** identifies *which object* carries the E_2. The braiding lives on `Rep^{E_1}(A)` only after passing to the *Drinfeld center* `Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_ch(A))`. The R-matrix *is* the universal half-braiding (AP-CY57). This is core Vol III machinery (CLAUDE.md HZ3-5, AP-CY3, AP-CY4, AP-CY56) that is not deployed at all in this Vol I file.

**Defense.** This is not a *wrong* claim, it is a *missing* one. The healing inserts a single explicit identification: **the E_2-braided category of line operators is `Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_ch(A))`, and the R-matrix `r(z)` is the infinitesimal half-braiding of the universal line operator.** This is AP-CY57 ("narration vs construction") in the *positive* direction: the standalone narrates "braided monoidal" without identifying the construction.

**Repair location.** e1_primacy §4 last paragraph (after Proposition 4.7); insert a Remark explicitly identifying the carrier of the E_2 structure. Cross-reference AP-CY3, AP-CY4, AP-CY56.

---

## Section 3 — AP audit (per AP, with line numbers)

### V2-AP1 (E_∞ INCLUDES KM/Vir/Heis; never "VAs are not E_∞")

- e1_primacy line 1278: "Every standard family in conformal field theory (Heisenberg, affine Kac–Moody, Virasoro, W-algebras, ...) is E_∞-chiral" — **CORRECT**.
- e1_primacy line 769: "If A is a vertex algebra in the Borcherds–Frenkel–Lepowsky–Meurman sense (more generally, any E_∞-chiral algebra with poles in its OPE)" — **CORRECT**.
- N3 line 769: same as above — **CORRECT**.
- ordered_associative_chiral_kd.tex line 666–669: "all vertex algebras with nontrivial singular OPE: KM, Vir, H, lattice algebras, W-algebras, all of which are E_∞-chiral, since every vertex algebra is E_∞" — **CORRECT** and explicit.
- ordered_associative_chiral_kd.tex line 2170: "The Heisenberg algebra is E_∞-chiral: it is a local vertex algebra with Σ_n-equivariant factorization structure. Its OPE has a double pole, but poles do not break E_∞-locality." — **CORRECT** (V2-AP1 honored).

**V2-AP1 status: CLEAN. No violations.**

### V2-AP2 (R(z) ≠ τ does not imply E_1)

- e1_primacy line 776–784 ("E_1 refinement adds no new data at degree 2 beyond OPE") — **VIOLATION** (Claim #15 above). Strictly speaking this is V2-AP2 in the converse direction, but the asymmetric handling of the kernel between §4.7 and §6.5 makes this a manuscript-internal contradiction.
- N3 same passage — **VIOLATION**.

**V2-AP2 status: 2 violations.**

### V2-AP3 (three bars: B^FG, B^Σ, B^ord)

- e1_primacy Remark 3.4 (line 344) — explicitly distinguishes the three; **CORRECT**.
- N3 §3.1 (line 306 ff.) — explicitly distinguishes three coalgebra structures; **CORRECT**.
- ordered_associative_chiral_kd.tex line 46–55 — explicitly distinguishes; **CORRECT**.

**V2-AP3 status: CLEAN. The three-bar distinction is well-honored in all files.**

### V2-AP4 (R-matrix twisted descent)

- e1_primacy lines 92, 137, 207, 392, 619, 657, 695, 885, 962: ALL state naive coinvariant projection without R-twist qualifier — **18 violations** in this file alone (Claim #2 above).
- N3 lines 88, 93, 134, 149, 281, 349, 359, 388, 432, 457, 562, 605, 619, 657, 695, 885, 962: same — **17 violations**.
- ordered_associative_chiral_kd.tex Prop 8.6 (line 505) and Cor 8.7 (line 650): **CORRECT** treatment of R-twisted descent.

**V2-AP4 status: ~35 violations in standalone files; chapter is clean.** This is the single largest AP violation in this audit. Healing is the §2.B repair: one definition + two corollaries.

### V2-AP21 (PVA ≠ P_∞-chiral)

- Not directly tested in these files; PVA appears only in cross-references (e1_primacy does not use PVA language).

**V2-AP21 status: not applicable to these files.**

### V2-AP22 (full hierarchy Comm < PVA < E_∞-chiral < P_∞-chiral < E_1-chiral)

- e1_primacy three-tier classification §6 sketches a *coarser* hierarchy: pole-free / E_∞ with poles / genuinely E_1. It does not place PVA or P_∞-chiral in the picture. This is a missed opportunity, not a violation: the three-tier story is correct as far as it goes.

**V2-AP22 status: not violated, but the standalone could be tightened by mapping its three tiers onto the V2-AP22 hierarchy. Currently uses a different (compatible) refinement.**

### AP152 (ordered ambiguity: labeled vs time-ordered)

- e1_primacy line 1279: "OPE is symmetric in the operator ordering" — uses "operator ordering" without specifying; mild AP152 risk.
- N3 line 804: "operator ordering" same — mild AP152.
- **ordered_associative_chiral_kd.tex line 2131**: "the E_1-structure is the time-ordered product" — **DIRECT AP152 VIOLATION**. This conflates the labeled-ordering on the holomorphic curve (which is what the ordered bar uses) with the time-ordering on the topological direction R_t (which is what Lorentzian QFT uses).

**AP152 status: 1 hard violation (chapter line 2131); 2 mild risk.** The chapter line should be revised to say "labeled-ordered (combinatorial)" not "time-ordered (analytic)".

### AP-CY3 (E_2 ≠ commutative)

- Not at issue in these files; no E_2 → E_∞ collapse asserted.

**AP-CY3 status: clean.**

### AP-CY4 (Drinfeld center vs derived center)

- e1_primacy mentions "derived center" in Item (iv) of §7 (line 845–854) but does not distinguish from Drinfeld center.
- N3 does not mention either explicitly.

**AP-CY4 status: not directly violated, but Z^der_ch(A) appears without the categorical comparison.**

### AP-CY23 (E_1-chiral bialgebra is correct Hopf framework)

- e1_primacy §9 ("Chiral quantum group equivalence") implicitly works in the E_1-chiral bialgebra framework but does not *name* it as such.
- N3 §9 same.

**AP-CY23 status: implicit honor but no explicit framework citation. Healing: insert a forward reference to AP-CY23 / Vol III Section 7 of e1_chiral_algebras.tex (~400 lines of E_1-chiral bialgebra axioms).**

### AP-CY56 (E_2 lives on Z(Rep^{E_1}(A)), not on A itself)

- e1_primacy lines 211, 1241, 1291, 1429, 1533: invokes "braided monoidal structure on the category of A-modules" without identifying that this is Z(Rep^{E_1}(A)). **5 instances of partial AP-CY56 violation by omission.**

**AP-CY56 status: 5 omission-type violations; healing in §2.H.**

### AP-CY57 (narration vs construction — "X gives Y" needs explicit arrow)

- e1_primacy line 211: "the spectral r-matrix, the KZ connection, the Drinfeld associator, and the full braiding of tensor categories of modules all live on the ordered side" — narration ("live on the ordered side") without construction of the half-braiding. AP-CY57 violation.
- e1_primacy line 1241: "the full function r(z) carries information about the braiding, the quantum group, and the line-operator algebra" — narration of "carries information about" without explicit recovery map.

**AP-CY57 status: ~6 narration-without-construction lines. Healing: replace each with an explicit map (see §2.H).**

### AP-CY55 (manifold invariants vs algebraization invariants)

- Not at issue in these files (Vol I, no manifold context).

### AP153 / AP154 (E_3 scope inflation; algebraic vs topological E_3)

- e1_primacy does not invoke E_3.
- N3 does not invoke E_3.
- `ordered_chiral_homology.tex` Theorem 1.3 (line 442 ff.) carefully distinguishes algebraic from topological E_3 — **CORRECT** (AP154 honored).

**AP153/AP154 status: clean.**

### AP155 (overclaiming novelty for known invariants)

- e1_primacy Proposition 9.5 ("Verlinde recovery") — AP155 violation (Claim #20).
- e1_primacy Theorem 9.4 ("Universal Miura coefficient") — flag for review: the (Ψ−1)/Ψ coefficient is reasonably new, but the proof approach via Miura is classical Frenkel–Reshetikhin / Procházka–Rapčák.

**AP155 status: 1 violation (Verlinde); 1 risk (Miura).**

### AP126 (level-stripped r-matrix; r-matrix at k=0 must vanish)

- e1_primacy Example 8.4 line 502: `r(z) = k Ω_g/z` — level prefix correct, AP126 honored.
- e1_primacy Example 8.5 line 1719: `r(z) = k Ω_g/z` (KM), `at k=0 the r-matrix vanishes identically` — AP126 honored.
- e1_primacy line 833: `av(r(z)) = κ_dp = k dim(g)/(2h^v)`, vanishes at k=0 — AP126 honored.
- e1_primacy line 1595–1606 (Yangian): `r(z) = ℏ Ω/z` with level ℏ — AP126 honored.

**AP126 status: clean. The standalone consistently includes the level prefix.**

### AP151 (convention clash within file: Heisenberg curved vs linear)

- See Claim #16. Convention clash *between files*, not within. Still a problem.

### AP139 (unbound variable in theorem)

- e1_primacy Theorem 5.4 (Theorem D^{E_1}, line 1188): `R^{E_1,bin}(z;ℏ)` — variables bound. **clean.**

### AP60 (only genuinely new content tagged ProvedHere)

- e1_primacy uses no ClaimStatus tags. As a standalone, this may be acceptable, but if the file is to be integrated into Vol I, every theorem needs a status tag.
- N3 has `\providecommand{\ClaimStatusProvedHere}{}` etc. (lines 110–113) but never uses them.

**AP60 status: latent risk (untagged theorems).**

---

## Section 4 — Consolidated punch list (criticality order)

### Critical (must fix before any Annals submission)

1. **Naive vs R-twisted coinvariant** (V2-AP4, ~35 instances). Replace `(B^ord)_{Σ_n}` with `(B^ord)^{R-Σ_n}` everywhere; insert one definition + two corollaries (pole-free naive case; cohomological collapse on E_∞ tier (b)).
2. **Tier (b) "no new data at degree 2"** (Claim #15, internal contradiction with §4.7). Strike the false sentence, replace with chain-level qualifier.
3. **Verlinde proof: false unitarity formula** (Claim #20, line 2231–2232). `Σ_l S_{jl}^2 = δ_{j0}` is wrong — replace with Frobenius reciprocity.
4. **Spectral coassociativity dropped Φ** (Claim #24, eq 9.2). Restore `Φ_{123}` conjugation.
5. **Yangian unitarity sign** (Claim #21). Reconcile `(u^2 − ℏ^2)I_4` (e1_primacy line 1881) with `(ℏ^2 − u^2)I` (ordered_chiral_homology lines 625, 3833, 4015–4016, 4191).

### Important (must fix for Annals quality)

6. **Heisenberg curved vs linear convention clash** (Claim #16). One file, one convention; cite the other.
7. **Non-splitting Proposition 4.7 misnamed** (Claim #6). Sections *do* exist; they form a GRT_1 torsor. Reword headline.
8. **Theorem 5.7 input class drift** (Claim #23). Cyclic chiral algebra ≠ E_1-chiral algebra.
9. **AP152 violation in ordered_associative_chiral_kd line 2131**. "Time-ordered" should be "labeled-ordered (combinatorial)".
10. **AP-CY56: identify carrier of the E_2 braiding** (Claim #30). Insert explicit `Z(Rep^{E_1}(A)) = Rep^{E_2}(Z^{der}_ch(A))` identification.
11. **AP155 disclaimer for Verlinde + Miura recovery** (Claim #20).

### Useful (would strengthen but not block)

12. Theorem A^{E_1} (5.1) — coderived category setup not made explicit.
13. Theorem B^{E_1} (5.2) — PBW-completeness hypothesis stated but not proved for tier (c).
14. Theorem C^{E_1} (5.3) — `Z^{E_1}(A)` defined only as "R-matrix-equivariant elements"; needs precise definition or explicit reference.
15. Universal Miura coefficient (9.4) — proof Step 2 has unverified sign cancellation; numerical cross-check claim cites no engine.
16. Three tiers should be mapped onto V2-AP22 hierarchy.
17. Insert explicit forward reference to Vol III AP-CY23 / e1_chiral_algebras.tex §7 for E_1-chiral bialgebra axioms.

### Cosmetic

18. "Primitive" → "underlying" / "least-symmetric" (semantic precision; word "primacy" can stay if the title-defining adjunction is named).
19. ClaimStatus tags absent in N3 despite providecommand at line 110–113.

---

## Section 5 — Three concrete upgrade paths (Annals-class strengthenings)

The architectural theorem of the pillar is:

> *(E_1 primacy.) The averaging map av : g^{E_1} → g^{mod} is a surjective dg Lie morphism whose Maurer–Cartan element projects to the modular MC element, and whose kernel is controlled at genus 0 by GRT_1 and at genus 1 by the quasi-modular anomaly E_2 → \widehat E_2.*

Three concrete upgrade paths:

### Upgrade Path A — "Adjoint primacy" theorem

**Statement.** *Let `Ch_{E_∞}` and `Ch_{E_1}` denote the (∞,1)-categories of E_∞-chiral and E_1-chiral algebras on a smooth curve X. The forgetful functor `U : Ch_{E_∞} → Ch_{E_1}` admits a left adjoint `Sym^{ch} : Ch_{E_1} → Ch_{E_∞}`. The bar functor `B^ord : Ch_{E_1} → CoAlg_{F\Ass}` and `B^Σ : Ch_{E_∞} → CoAlg_{F\Com}` fit into a commutative square*

```
        Sym^{ch}
Ch_{E_1} ─────→ Ch_{E_∞}
   │              │
B^ord│              │B^Σ
   ↓              ↓
CoAlg_{F\Ass} ─→ CoAlg_{F\Com}
        ⟨av⟩
```

*and `av` is the precise content of the right vertical arrow's failure to be an iso (failure measured by the `ker(av)` data).*

**Proof sketch.** Sym^{ch} is the chiral symmetric envelope (left adjoint to the forgetful functor that ignores Σ_n equivariance); existence follows from the special-adjoint-functor theorem in the (∞,1)-category of presentable categories. Naturality of the bar functors makes the square commute. The horizontal `av` is then the natural transformation between the two compositions, which by adjunction is determined by its component on free objects, where it is the Reynolds operator.

**Why this is stronger.** Replaces the vague "primitive" word with an honest categorical universal property. Connects to AP-CY56 / AP-CY57 by identifying *which* category carries which E_n structure.

### Upgrade Path B — R-twisted descent as the single load-bearing theorem

**Statement.** *Let A be a strongly admissible E_1-chiral algebra with classical r-matrix r(z). The following are equivalent:*

1. *r(z) satisfies the spectral classical Yang–Baxter equation `[r_{12}(z), r_{13}(z+w)] + [r_{12}(z), r_{23}(w)] + [r_{13}(z+w), r_{23}(w)] = 0`;*
2. *The R-twisted Σ_n-action `ρ_R(σ_i) = τ_{i,i+1} ∘ R_{i,i+1}(z_i − z_{i+1})` on `B^ord(A)_n` factors through Σ_n (i.e., satisfies the Coxeter relations);*
3. *The descent `(B^ord(A)_n)^{R-Σ_n}` defines a flat factorization D-module on Conf_n(X);*
4. *(For pole-free A:) the naive coinvariant `B^ord(A)_n / Σ_n` agrees with the R-twisted invariant.*

**Proof.** (1)⇔(2) is the Drinfeld–Kohno theorem (Prop 8.6 of `ordered_associative_chiral_kd.tex`, with explicit YBE+strong unitarity). (2)⇔(3) is the étale descent equivalence for principal Σ_n-bundles. (3)⇒(4) is corollary 8.7 (when r(z) = 0 the R-twist is trivial). (4)⇒(1) is the classical statement that `(B^ord)/Σ_n` is well-defined as a coalgebra iff r(z) = 0 ⇒ trivial CYBE.

**Why this is stronger.** Replaces ~35 informal "naive coinvariant" lines with a single definitive equivalence. Subsumes V2-AP4 and Cor 8.7 into one theorem. Makes the *meaning* of "av is the Σ_n-coinvariant projection" precise: it is the R-twisted projection, with the naive case as a special instance.

### Upgrade Path C — Five theorems as a single Reynolds-operator theorem

**Statement.** *Let g^{E_1} be the E_1 modular convolution dg Lie algebra and g^{mod} its symmetric counterpart. The Reynolds operator av : g^{E_1} → g^{mod} extends to a morphism of Maurer–Cartan moduli `MC(av) : MC(g^{E_1}) → MC(g^{mod})` such that:*

*(A^{E_1}) MC(av) intertwines the bar–cobar adjunction;*

*(B^{E_1}) MC(av) restricts to a quasi-isomorphism on the Koszul locus;*

*(C^{E_1}) MC(av) sends the ordered complementarity equation to the symmetric one;*

*(D^{E_1}) MC(av) sends the degree-2 R-matrix package to the scalar shadow series with explicit Sugawara correction at non-abelian KM;*

*(H^{E_1}) MC(av) sends the ordered chiral Hochschild complex to the symmetric one;*

*and the kernel of MC(av) at each degree is the family of "ordered invariants" obstructing recovery of the ordered side from the symmetric shadow:*

| Degree | ker(MC(av)) at this degree |
|--------|----------------------------|
| 1 | 0 (ker is empty at degree 1) |
| 2 | antisymmetric part of r(z); for KM, the Im(Ω_g) component in `Λ²g` |
| 3 | linearised associator [Ω_{12}, Ω_{23}]; for KM, the GRT_1-orbit of associators |
| 4+ | iterated commutators; the full higher-Drinfeld tower |
| genus 1 | quasi-modular anomaly E_2 → \widehat E_2 |

**Proof sketch.** Each row of the table comes from a degree-graded analysis of the Reynolds operator on a specific isotypic component. The five theorems A–H are recovered by reading off the projection on the trivial isotypic component at each genus and degree.

**Why this is stronger.** Replaces "five separate ordered theorems with separate proofs" with "one Reynolds-operator theorem stratified by degree". Makes the GRT_1 torsor structure of section 4.7 visible as the "extension class" of the SES at degree 3. Aligns with the (much later) formality bridge of §6: the bridge is precisely the chain-level inverse of MC(av) restricted to the cohomological E_2-page.

---

## Closing assessment

The "E_1 primacy / ordered bar" pillar is *philosophically right* and the integrated chapter (`ordered_associative_chiral_kd.tex`) executes it with mathematical rigor that aligns with the catalogued anti-patterns.

The standalone files `e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex` are **a step backwards** relative to the chapter: they re-violate V2-AP4 in ~35 places, contradict their own non-splitting proposition by claiming "no new data at degree 2" for E_∞ tier (b), and contain at least one mathematical error (Verlinde unitarity) and one sign conflict (Yangian unitarity).

The healing is *not* to retract. The healing is to backport `ordered_associative_chiral_kd.tex`'s discipline into the standalones via:

- one definition (R-twisted descent),
- two corollaries (pole-free reduction; cohomological collapse on E_∞),
- one Reynolds-operator theorem (Upgrade Path C),
- one categorical primacy statement (Upgrade Path A).

After these four edits the pillar is Annals-ready. Before them, several individual claims are wrong and the architectural narrative is partially incoherent.
