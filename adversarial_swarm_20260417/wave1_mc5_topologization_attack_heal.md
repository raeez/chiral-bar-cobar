# Wave 1 (2026-04-17): Adversarial Attack and Heal — MC5 Class M Chain-Level + Topologization Tower

Target. (i) Vol I `chapters/theory/mc5_class_m_chain_level_platonic.tex` `thm:mc5-class-m-chain-level-pro-ambient` (lines 229–321) and the three-ambient equivalence `prop:ambient-equivalence` (lines 501–576); the AP203 healing claim that "uniqueness of central degree-2 m_0 via Hodge + vacuum-proportionality (H^{2,0}(curve)=0)" is now closed; the assertion `c_r = S_r` proved chain level via a harmonic projector. (ii) Vol II `chapters/connections/e_infinity_topologization.tex` `thm:iterated-sugawara-construction` (lines 223–314), `thm:e-infinity-topologization-ladder` (lines 354–469), and the W_∞ convergence theorem `thm:w-infty-e-infty-topological-convergence` (lines 644–765). (iii) Status-table claim that Class L (V_k(g), k ≠ −h^v) is chain-level on the ORIGINAL complex via a CG factorization rerouting that makes [Q, ~G_1] = T_Sug "STRICT chain-level (not up to Q-exact)". (iv) The status table assertion that Class M chain-level on the original complex is "the single remaining open direction" of the topologization tower.

The attack proceeds in seven nontrivial fronts F1–F7. Each front is then assigned a verdict: SURVIVES (the inscription is correct as stated), SCOPE-QUALIFIED (the inscription is correct after a stated narrowing), or RETRACT (the inscription overclaims and must be downgraded to a conjecture or removed). The heal section follows.

## Attack

### F1 — Pro-ambient Mittag–Leffler "in every cohomological degree"

`thm:mc5-class-m-chain-level-pro-ambient` Step 3 reads: "for every cohomological degree m the inverse system {H^m(C^•_BV(A_{≤N}, Σ_g))}_N and {H^m(B^{ch,(g)}(A_{≤N}))}_N satisfy Mittag–Leffler. This is immediate from `prop:standard-strong-filtration`(iv): at each fixed cohomological degree and each fixed total-conformal-weight filtration piece, the tower stabilises after finitely many stages." The argument is a single sentence; the mechanism it invokes is "weight-stabilisation".

The attack: weight-stabilisation at fixed total conformal weight is genuine for the ALGEBRA truncation (A_{≤N})_h is constant in N for N ≥ h, by the L_0 grading of A. But the relevant invariant is H^m of the BAR complex of A_{≤N}, NOT of A itself. The bar complex couples words s^{-1} a_1 | ... | s^{-1} a_r whose total conformal weight is bounded by w; a word of total weight w can have up to ~w factors of weight 1, so the bar-word count at fixed w grows polynomially in w. At fixed w, the truncation to N still feels every (A_{≤N})_h with h ≤ w; this is finite-dimensional for each N and stable for N ≥ w. So far Mittag–Leffler holds **at fixed total conformal weight**.

The pro-system is over N (truncation level), not over w. At fixed cohomological degree m, the bar complex spreads across ALL weights: cocycles of cohomological degree m at total weight w for arbitrarily large w can survive or be killed by the bar differential; passage to A_{≤N} can promote cocycles to coboundaries via mixing with high-weight pieces of A. The Mittag–Leffler claim, as stated, requires that for each fixed m, the image filtration im(H^m(B(A_{≤N+k})) → H^m(B(A_{≤N}))) stabilises in k uniformly in m. The proof references `prop:standard-strong-filtration`(iv) but that proposition (per the contract in the file at lines 280–300) supplies stabilisation **at fixed weight w**, not at fixed cohomological degree m.

Verdict: SCOPE-QUALIFIED. The Mittag–Leffler assertion is correct at fixed (cohomological degree, total bar weight). It is uniform in m only after one further input: that the bar differential is weight-preserving (true), so each cohomological degree splits as a direct sum (or product) over weights, and the Mittag–Leffler condition holds DEGREEWISE in (m, w). The corollary `cor:mc5-class-m-chain-level-on-inverse-limit` (Milnor exact sequence) goes through verbatim once one quantifies over (m, w): the lim¹ obstruction at each (m, w) vanishes. The proof should add the explicit (m, w)-bigrading sentence to make Step 3 honest.

### F2 — "Ambient artefact" framing of direct-sum failure

`rem:direct-sum-obstruction-is-ambient-choice` (lines 374–403) claims: "direct-sum chain-level MC5 for class M is genuinely false" is "correct as a remark about the specific ambient Ch(Vect) of bounded direct sums with naive chain homotopies. It is not a statement about the mathematical content of MC5 class M." The justification: "the direct sum ⊕_h B^{(g)}(A)_h embeds as a dense subspace of the product ∏_h B^{(g)}(A)_h, and these two presentations of the underlying graded vector space differ only by the ambient-category convention".

The attack: density alone does not transport chain-level statements. A chain map f: C → D between direct sums and a chain map g: ~C → ~D between completions agree on the dense subspace iff g restricts to f. But if f is **not** a chain-level qi on Ch(Vect) (which is the input asserted in the original Vol II remark) and g is a qi on the product, then the two facts coexist without contradiction; the failure on Ch(Vect) is then **not** an ambient artefact in the sense of "go to a richer category and the same morphism becomes a qi". Rather, the "morphism" changes: the contracting homotopy h^∞ = Σ_j h · m_0^{j-1} is defined as an infinite series, which is not a morphism in Ch(Vect) at all (the sum of an infinite family of nonzero linear maps in Vect is not defined). Switching ambient changes the morphisms one is allowed to consider; THAT is the substance, not density.

This is not a refutation of the theorem — the theorem holds on the pro-ambient — but the rhetorical move "ambient artefact, not a gap" understates the content. The mathematical content is: **the homotopy needed to contract the harmonic discrepancy is not an honest chain map in Ch(Vect); it only becomes a continuous chain map after passing to the J-adic / pro / weight-completed ambient**. This is meaningful: one is enlarging the class of morphisms, not just the class of objects.

Verdict: SCOPE-QUALIFIED. The theorem stands; the framing should clarify that the ambient enrichment is morphism-level (the contracting homotopy is an admissible map only in the topological/pro-ambient), not merely object-level (the bar complex always was a pro-object).

### F3 — c_r = S_r at chain level versus at cohomology

The status table records "c_r = S_r proved (not just named): harmonic projector on H_g coincides with av on degree-r component." The harmonic projector P_g is defined at the level of cohomology (it is the projector onto harmonic representatives in the (BV, Hodge-style) decomposition); it is not a chain-level operator on B^{(g)}(A). The shadow coefficient S_r is a chain-level invariant: it is the leading coefficient of the r-fold A_∞ coproduct correction δ^{(r)} appearing in the bar differential.

The attack: S_r is **defined** as a chain-level invariant (a coefficient in the bar differential expansion); c_r appears in the harmonic discrepancy `eq:harmonic-discrepancy` as a curvature scalar. The identification c_r = S_r at chain level requires that the expansion δ^{(r)}_harmonic of the BV-side correction agrees with the bar-side coefficient S_r as a polynomial in the central charge. This is a calculation, not a tautology. AP172 in the catalogue warns against confusing chain-level Gerstenhaber operations with their cohomology shadows; the same warning applies here.

Verdict: SCOPE-QUALIFIED. The identity c_r = S_r is correct on cohomology (both sides extract the same number from the leading divergence of the harmonic series); the chain-level identity requires a witness that the harmonic discrepancy's leading scalar agrees with the chain-level shadow coefficient. For Virasoro this is verifiable (S_4(Vir_c) = 10/[c(5c+22)] computed independently in `shadow_tower_higher_coefficients.tex`); for principal W_N at higher r it depends on the Fateev–Lukyanov screening computation. The chapter should cite the explicit S_r computation it depends on, not the harmonic projector alone.

### F4 — AP203 Hodge / vacuum-proportionality

The CLAUDE.md status entry for MC5 records: "AP203 HEALED: uniqueness of central degree-2 m_0 via Hodge + vacuum-proportionality (H^{2,0}(curve)=0 kills competing bar-length-2 insertions)." This is asserted as the healing of an earlier ambiguity in which centre m_0 was being used.

The attack: H^{2,0}(curve)=0 is correct for genus-0 (P^1 has no holomorphic 2-form because the curve is 1-dimensional; H^{p,q} for a curve has q ≤ 1). For higher genus the relevant cohomology is on the bar complex over the moduli M̄_{g,n} or on the universal curve; the vanishing H^{2,0}(curve) = 0 is then a triviality (a curve has dim_C = 1, so H^{2,0} is zero by dimension) and does not suffice to kill competing bar-length-2 insertions over M̄_{g,n}, where the relevant Hodge group is on a HIGHER-dimensional base. The phrasing "H^{2,0}(curve)=0" is correct but weaker than what is needed for the higher-genus version.

The "vacuum-proportionality" mechanism is: any central degree-2 bar insertion, by chiral algebra translation invariance, factors through the vacuum module, hence is proportional to the vacuum vector. This IS a uniqueness mechanism, but it is representation-theoretic, not Hodge-theoretic. Combining the two as "Hodge + vacuum-proportionality" risks reading as a single argument when in fact it is two independent inputs: Hodge for the codomain vanishing on the curve fibre (trivial), and vacuum-proportionality for the source uniqueness (the substantive content).

Verdict: SCOPE-QUALIFIED. The AP203 healing is correct in substance; the prose conflates a trivial dimensional fact with the load-bearing vacuum-proportionality argument, leaving the reader uncertain which step is doing the work. The healing chapter should separate the two inputs.

### F5 — Class L original-complex via CG factorization F^{CS}_k

Status table claim: "[Class L] **E_3^top on ORIGINAL complex** via Dunn-additivity rerouted through CG factorization algebra F^{CS}_k on R×C (single-colored, not SC^{ch,top}!) + explicit η_1^(i) = (1/2(k+h^v)) Σ f^a_bc :bar c_b c^c bar c_a: and η_1^(ii) = (1/2(k+h^v)) Σ f_{ab}^c :bar c_a bar c_c c^b:, making [Q, tilde G_1] = T_Sug STRICT chain-level (not up to Q-exact)".

The attack: a search of the Vol II repository for the explicit string `tilde G_1`, `F^{CS}_k single-coloured`, and `STRICT chain-level (not up to Q-exact)` returns no inscription matching this verbatim formula in the connections/ directory; the inscription is asserted in CLAUDE.md but the Vol II `e_infinity_topologization.tex`, `bv_brst.tex`, and surrounding chapters discharge Sugawara identities at the level of Q_tot-cohomology (`eq:Ja-Qexact-tower` says J_a = [Q_tot, ~c_a] "on H^•(A^BV_{3d}, Q_tot)"). Theorem `thm:iterated-sugawara-construction` line 232 explicitly says "in H^•(A^BV_{3d}, Q_tot)", **not** chain level. The claim of strict chain-level [Q, ~G_1] = T_Sug for class L on the ORIGINAL complex is therefore not yet inscribed; the chain-level statement remains a CLAUDE.md aspiration.

Verdict: RETRACT or INSCRIBE. The status-table assertion that class L original-complex topologization is chain-level (not up-to-Q-exact) overstates what the chapter actually proves. Either (a) inscribe the explicit η_1 formulae and verify [Q, ~G_1] = T_Sug strictly (no Q-exact remainder) in the bulk BV chain complex, or (b) downgrade the status table to "PROVED on Q_tot-cohomology; chain-level explicit (η_1^(i), η_1^(ii)) inscription pending".

### F6 — Iterated Sugawara: antighost commutativity is asserted, not derived

`def:higher-spin-stress-tower` axiom (T5) declares "[G^{(n)}, G^{(m)}] = Q_tot-exact on cohomology". `thm:iterated-sugawara-construction` Step 2 leans on this axiom. `rem:antighost-BRST-commutativity` then "explains" axiom (T5) by appealing to "the classical fact that the truncated W_∞[μ] structure constants are degenerate at the classical level in the sense that the Poisson bracket {T^(n), T^(m)} is a normally ordered polynomial of total spin n+m-1 which reduces on cohomology to a total derivative of a lower-spin Casimir combination" with citations Linshaw Theorem 7.1 and BMP §4.3.

The attack: the cited Linshaw and BMP statements describe the classical W_∞[μ] Poisson algebra, NOT the BV-BRST commutativity of antighost currents G^{(n)}. The leap from {T^{(n)}, T^{(m)}} = total derivative of lower Casimirs to [G^{(n)}, G^{(m)}] = Q_tot-exact is not automatic: it requires (a) lifting the classical Poisson identity to a quantum OPE identity (the Linshaw existence theorem provides this for the algebra of T^{(n)}'s, not of G^{(n)}'s); (b) verifying that the antighost lifts intertwine the OPE algebra (this is the content of the truncated W_{1+∞} structure on the BRST primitives); (c) verifying that the 1/n-symmetrised substitution in `eq:G-n-formula` produces antighosts which themselves satisfy a closed OPE algebra. None of (a)–(c) is established in the chapter; the antighost commutativity is **postulated as axiom (T5)**, not proved.

Verdict: SCOPE-QUALIFIED. Theorems `thm:e-infinity-specialisation-Vir` (N=2, axiom (T5) vacuous) and `thm:e-infinity-specialisation-WN` for small N (where antighost commutativity can be checked by hand, e.g. N=3) survive. The W_∞ specialisation `thm:e-infinity-specialisation-Winfty` and `thm:w-infty-e-infty-topological-convergence` rest on axiom (T5) at all spins simultaneously and should be marked CONJECTURAL, contingent on the open antighost-commutativity verification (or on a structural argument from a 3d HT BV theory with full higher-spin gauge symmetry).

### F7 — "Single remaining open direction" framing

Status table: "Original chain-level for class M is the single remaining open direction; everything else PROVED on original complex." Combining F5 and F6: Class L original-complex chain-level requires the η_1 explicit verification (F5); the iterated-Sugawara ladder requires antighost-commutativity at all spins (F6). Neither is currently inscribed at the level the status table claims.

Verdict: SCOPE-QUALIFIED. The "single open direction" framing is misleading. The honest inventory has at least three open directions: (i) class M original-complex chain-level (acknowledged); (ii) class L original-complex chain-level via the η_1 formulae (asserted closed but not inscribed verbatim); (iii) iterated-Sugawara antighost-commutativity at general spin (postulated as an axiom, not derived). The status table should be revised to reflect the actual inscription state.

## Survivors

- `thm:mc5-class-m-chain-level-pro-ambient`: SURVIVES the attack, after the Mittag–Leffler argument is qualified to fix (cohomological degree, total bar weight) bigrading (F1).
- `prop:ambient-equivalence`: SURVIVES; the three ambients are canonically equivalent. The framing of the direct-sum obstruction should be sharpened (F2).
- `cor:mc5-class-m-chain-level-on-inverse-limit`: SURVIVES via Milnor exact sequence at each (m, w).
- `thm:e-infinity-specialisation-Vir` (Virasoro N=2 → E_3-top on Q_tot-cohomology): SURVIVES.
- `thm:iterated-sugawara-construction` for n ≤ 3 (antighost-commutativity verifiable by hand): SURVIVES.
- AP203 healing: SURVIVES in substance; prose conflates Hodge dimension with vacuum-proportionality (F4).
- c_r = S_r at cohomology: SURVIVES; chain-level identity requires explicit S_r citation per family (F3).

Not surviving in current form: chain-level [Q, ~G_1] = T_Sug for class L on original complex (F5); antighost-commutativity at general spin (F6); "single open direction" framing (F7); W_∞ E_∞ chain-level convergence (F6 propagation).

## Platonic Reconstitution

### MC5 chain-level table (per ambient × per class)

| Ambient | Class G (Heis) | Class L (KM, k≠−h^v) | Class C (βγ, bc) | Class M (Vir, W_N) |
|---|---|---|---|---|
| Ch(Vect) (direct sum, naive) | strict chain qi (MacLane) | strict chain qi (PBW + E_2-collapse) | strict chain qi (FMS bosonisation) | NO chain qi: harmonic series Σ δ_r^harm not a morphism in Ch(Vect) |
| pro-Ch(Vect) (truncation tower) | strict chain qi | strict chain qi | strict chain qi | strict pro-qi (Mittag–Leffler in (m, w); F1) |
| Ch_J(TopVect) (J-adic) | strict chain qi | strict chain qi | strict chain qi | strict continuous chain qi (h^∞ continuous; F2) |
| CompCl(F) (filtered-completed) | strict chain qi | strict chain qi | strict chain qi | strict chain qi |
| Cohomology (D^co, coderived) | qi | qi | qi | qi (coacyclic characterisation) |

Reading: the class-M row is the only place where the ambient choice is load-bearing. In Ch(Vect) chain-level fails for class M because the contracting homotopy h^∞ = Σ_j h·m_0^{j-1} is not an admissible morphism (infinite sum of nonzero maps in Vect). In any of pro/J-adic/weight-completed, h^∞ becomes admissible and the chain qi holds strictly. The three ambient-rich entries are equivalent by `prop:ambient-equivalence`.

### Topologization tower table (per family × per claim level)

| Family | Q_tot-cohomology (E_n on H^•) | Chain-level on original complex | Chain-level weight-completed |
|---|---|---|---|
| Class G: Heis_k | E_3^top (commutative, Dunn) | E_3^top (commutativity is on the nose) | E_3^top |
| Class L: V_k(g), k≠−h^v | E_3^top via Sugawara on cohomology (`thm:E3-topological-km`) | CONJECTURAL with explicit η_1 candidate (F5) | E_3^top via PBW + Wakimoto |
| Class C: βγ, bc | E_3^top via FMS bosonisation to Heis | E_3^top (via class G route) | E_3^top |
| Critical level k=−h^v | E_2^top (Sugawara collapses, dim drop) | E_2^top | E_2^top |
| Class M: Vir, W_N (single conformal vector, N=2) | E_3^top via half-BRST + DS (`thm:E3-topological-DS-general`) | OPEN | E_3^top via half-BRST + MC5 weight-completed |
| Higher-spin tower depth k ≥ 3 (W_N, N≥3) | E_{k+2}^top CONDITIONAL on antighost-commutativity axiom (T5) (F6) | OPEN | OPEN, propagates F6 |
| W_∞[μ] generic μ | E_∞^top CONDITIONAL on (T5) at all spins (F6) | OPEN | OPEN |

Reading: the topologization story is genuinely PROVED only on Q_tot-cohomology and only at single-conformal-vector depth (N=2). Higher-spin tower assertions are CONDITIONAL on antighost-commutativity (axiom (T5)); W_∞ E_∞-top is the inverse limit of those conditional statements and inherits the conjecture.

## Open Frontier

After the attack, the honest open frontier of the MC5 + topologization complex is:

1. **Class L chain-level on original complex via η_1 formulae**: inscribe the candidate η_1^(i), η_1^(ii) in `bv_brst.tex` or `e_infinity_topologization.tex` and compute [Q, ~G_1] − T_Sug as a chain-level cocycle; verify that the remainder is identically zero (not Q-exact). If the remainder is Q-exact but nonzero, the claim downgrades to E_3^top on cohomology only.
2. **Antighost-commutativity at higher spin**: prove [G^{(n)}, G^{(m)}] = Q_tot-exact for n, m ≥ 3 from the Costello–Gaiotto bulk BV structure, not from the classical W_∞[μ] Poisson identity. Until this is done, axiom (T5) of `def:higher-spin-stress-tower` is a hypothesis, not a theorem; `thm:e-infinity-specialisation-Winfty` and the W_∞ convergence theorem inherit conditional status.
3. **Class M chain-level on the original complex (Ch(Vect))**: this is the acknowledged open direction. Per F2 it is genuinely meaningful: it asks whether the contracting homotopy can be reorganised to be an honest morphism in Ch(Vect) without passing to a richer ambient. Most likely answer: NO (the harmonic series is genuinely not a Ch(Vect) morphism); the right reformulation is to declare the ambient as part of the data of the original complex, in which case the question dissolves into F2.
4. **Mittag–Leffler at fixed cohomological degree (uniform in m)**: F1's bigrading repair should be inscribed; the Step 3 sentence should explicitly bigrade by (m, w).
5. **AP203 prose separation**: F4's two-input clarification should be inscribed in the chapter; the phrase "Hodge + vacuum-proportionality" should be split into "Hodge dimension count (trivial; the curve has dim_C = 1) + vacuum-proportionality (substantive; the load-bearing argument)".
6. **c_r = S_r per family**: F3 asks for the explicit witness that the harmonic discrepancy's r-th coefficient agrees with the chain-level shadow coefficient S_r, family by family. Vir done; W_N at r > 4 to inscribe.

These six items are the post-Wave-1 frontier. None of them invalidates a survivor; each is a refinement to the inscription, a downgrade of an overclaimed status, or a genuine residual open question.
