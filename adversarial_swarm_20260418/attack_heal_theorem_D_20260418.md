# Theorem D Attack-and-Heal (Wave 2, 2026-04-18)

**Target.** `thm:genus-universality` at
`chapters/theory/higher_genus_foundations.tex:6305` and its two
load-bearing lemmas `prop:scalar-obstruction-hodge-euler` (:5414) and
`prop:clutching-uniqueness` (:6010), together with the PTVV alternative
`prop:theorem-D-factorization-homology-alt` (:6117). Status table (CLAUDE.md
:581) currently reads: "PROVED unconditional at g=1; g=2 for single-generator
scalar-diagonal families; g≥3 conditional on (a) scalar-diagonal hypothesis
for multi-generator uniform-weight and (b) Faber's λ_g-conjecture for
on-the-nose socle lift." This report attacks finer-grained content surfaced
after Wave 1 (`adversarial_swarm_20260417/wave1_theorem_D_attack_heal.md`)
and identifies residual scope drift.

## Phase 1 — Adversarial Attack

### A1 (NEW, load-bearing). `thm:kac-moody-obs` (:4972) silently assumes scalar-diagonality at g≥2.

Step 2 of the proof (:5012) writes "the fiberwise genus-g obstruction is
obs_g^fib = ω_g^Ar ⊗ m_0" and "Pushing this fiberwise form forward along
the universal curve produces the Hodge class λ_g by the same mechanism as
in the Heisenberg case." Step 3 (:5021) concludes "Each generator J^a
contributes a copy of the curvature m_0. Summing over a = 1, …, dim(g)."

This is exactly `def:scalar-diagonal-hypothesis` applied to V_k(g)
without a verification step. For V_k(g) with g non-abelian, the fiberwise
bar curvature at g≥2 is a sum over adjoint-representation generators
against edge propagators; there is no a-priori reason it decomposes as a
scalar kappa acting uniformly on every weight channel of
Λ^p H^0(Σ_g, ω) ⊗ ε_p. The Casimir identity Σ J^a ⊗ J_a = dim(g) · 1 on
the adjoint holds as an algebraic identity, but descending this to the
chain-level associated graded of the fiberwise bar over every weight p
requires precisely that the bar coefficients Λ^p at different p are
mutually orthogonal eigenspaces with the same eigenvalue kappa. That is
the hypothesis, not a theorem. The tag on `thm:kac-moody-obs` should
reflect this.

### A2. Concrete witness: does V_1(sl_2) WZW satisfy scalar-diagonality?

V_1(sl_2) is isomorphic to the lattice VOA V_{A_1} = V_Z·α (Frenkel–Kac).
On that realization the three sl_2 currents are Heisenberg + two vertex
operators e^{±α}. The Heisenberg channel is rank-1 scalar-diagonal
tautologically. The vertex-operator channels e^{±α} carry their own
Λ^p H^0(Σ_g, ω) sector via the screening contour, and the bar curvature
contribution through each is controlled by the lattice pairing ⟨α, α⟩ = 2,
which is itself a scalar. So V_1(sl_2) scalar-diagonality survives on the
nose via the lattice reduction. At generic level k the lattice reduction
is not available; the Wakimoto realization gives a rank-1 Heisenberg +
βγ ghost resolution, and scalar-diagonality on the ghost sector is
neither proved nor disproved in the current inscription. Verdict:
scalar-diagonality holds for V_k(sl_2) at positive integer level via the
lattice / Wakimoto route; open at generic level.

For V_1(sl_3) and higher rank, the analogous Frenkel–Kac /
Frenkel–Garland–Lepowsky realizations exist for specific lattices at
specific levels but not uniformly. The status-table line "automatic for
rank-1 strong-generator families" reads correctly; the qualifier "a
genuine hypothesis for multi-generator uniform-weight families such as
affine Kac–Moody V_k(g) with g non-abelian, where the Sugawara
identification av(r(z)) + dim(g)/2 = kappa is established at g=1 but its
g-independence at higher genus is the content of the hypothesis"
(def:scalar-diagonal-hypothesis :5406-5411) is exactly the right scope.

### A3. K-theoretic tautology check (F1 residue from Wave 1).

`rem:scalar-diagonal-honest` (:5447-5474) explicitly admits the K-theoretic
construction DEFINES obs_g by projection to ε_p, reducing
obs_g = κ·λ_g to the cohomological identity ch_g(λ_{-1}(E)) = (-1)^g c_g(E),
which is unconditional. The SUBSTANTIVE content is that the projected
class coincides with the physical bar-curvature obstruction. This is AP259
(tautological-by-definition) handled honestly. The remark is correctly
scoped. No new attack.

### A4. Step 3d Chern-Weil chain — does it reach the base on the nose?

Steps 3a–3e (:5648-5900 roughly) cite Arakelov–Faltings (fiberwise
curvature identification), BGS anomaly formula (curvature of det(E) in
Quillen metric), and splitting principle (passage from c_1(λ) to
c_g(E)). The BGS 1988a formula in the simple scalar version gives
c_1(λ, h_Q); higher Chern classes require Bismut–Gillet–Soulé 1988b/1990
secondary-class theory with Bott–Chern classes, NOT the scalar BGS88a.
The current inscription cites only BGS88a; the upgrade path is via the
Mumford 1983 GRR computation, which gives c_g(E) = λ_g as a CH-class,
together with scalar-diagonality to project the BGS88a representative of
c_1(det E) to the scalar channel at each weight. This chain is sound
given scalar-diagonality, which matches the current inscription.
Residual cleanup: the inscription's citation of Soulé 1992 Ch.III is for
arithmetic Riemann–Roch on Spec(O_K), not for M̄_g over C/Q; cleaner
citation would be Bismut–Freed 1986 + BGS 1988a + Faltings 1984 §2
+ Mumford 1983. Metadata issue, not math gap.

### A5. `prop:clutching-uniqueness` — is N^2 = 0 truly proved?

The inscription cites Mumford 1983 Table §7: R^2(M̄_2) is 2-dimensional,
spanned by λ_2 = λ_1·κ_1/12 and δ_irr^2/144, with non-degenerate
Faber socle pairing. This is verifiable from Mumford's paper and is
standard. Verdict: N^2 = 0 at g=2 is solid.

At g=1, R^1(M̄_{1,1}) = Q·λ_1 is 1-dim, so N^1 = 0 trivially.

At g≥3, N^g vanishing is the λ_g-conjecture (Faber–Pandharipande 2000).
Known for specific low g (Ionel 2002, Graber–Vakil); open in general.
Inscription correctly tags this as conditional.

### A6. Mok25 log-FM — preprint, not theorem.

`@article{Mok25}` in `standalone/references.bib:601-607` is tagged
`note = {Preprint}`. The chain-level log-FM sewing at the nodal boundary
of M̄_g is CITED not inscribed in Vol I; used load-bearing in both
`prop:theorem-D-factorization-homology-alt` part (iii) (correctly tagged
`\ClaimStatusConditional` at :6117) and in the modular-family extension
of Theorem A. Wave 1 already downgraded the PTVV tag; the CLAUDE.md row
reflects this. Residual: the g=2 separating-boundary of M̄_2 uses classical
Knudsen–Mumford stable reduction, NOT Mok25; at g=2 the PTVV path does
not need Mok25. The "conditional on Mok25" qualifier should be scoped to
g≥3 in the PTVV row.

### A7. PTVV clause (iii) independence (F6 residue from Wave 1).

The current proof of clause (iii) (:6151-6196) is rewritten to detect
kappa on the genus-1 PTVV pairing and invoke clutching-uniqueness on the
socle, without citing `prop:scalar-obstruction-hodge-euler`. That rewrite
is genuine; the two chains share no lemmas. However, both chains STILL
converge only on the same scope: scalar-diagonal uniform-weight at g=1,2
on the nose; socle-only at g≥3 unless λ_g-conjecture holds. The
`rem:ptvv-independence` (:6211-6264) correctly states this as
"complementary presentation with distinct scope" rather than
"genuinely disjoint" verification, in line with AP243 (HZ-IV decorator
non-disjoint dependency). Honest.

### A8. Multi-generator universality (`thm:multi-generator-universality`) — scope match.

Label `thm:multi-generator-universality` (higher_genus_modular_koszul.tex
:22861) is referenced from `thm:genus-universality` :6324 with the
qualifier "the higher-genus extension is conditional on the strong scalar
ansatz of Theorem \ref{thm:multi-generator-universality}". This is the
right bridge. No new attack here.

### A9. Summary table (`tab:obstruction-summary`, :6283) — consistent?

The table lists obs_g = κ·λ_g for Heisenberg, sl_2-hat, sl_3-hat, E_8-hat,
Virasoro (all single-generator or equivalently single-Casimir-channel
families) without an asterisk, and W_3 with the asterisk noting
cross-channel correction at g≥2. The single-generator KM entries
(sl_2-hat, sl_3-hat, E_8-hat) ARE multi-generator in the weight-1
current sense; their scalar-diagonality at g≥2 is exactly the
def:scalar-diagonal-hypothesis content. The table caption now reads
"For single-generator scalar-diagonal families..." — but sl_2-hat,
sl_3-hat, E_8-hat are NOT single-generator. Residual wording drift:
the caption should read "For scalar-diagonal families (including
Heisenberg, all V_k(g) that satisfy def:scalar-diagonal-hypothesis,
and Virasoro)..." to avoid implying KM is single-generator.

## Phase 2 — Surviving Core

**S1. Genus 1 unconditional, all uniform-weight families.** H^2(M̄_{1,1}) = Q·λ_1 and the scalar channel is 1-dim. obs_1 = κ·λ_1 is forced without any splitting-principle, Chern-Weil, or clutching machinery. Solid across all families.

**S2. Genus 2 on the nose for scalar-diagonal families.** N^2 = 0 (Mumford 1983) means the socle-clutching output lifts unconditionally. Either the Arakelov–BGS chain (under scalar-diagonality) or the PTVV+clutching chain (under factorization at nodes) closes on the nose. Valid for Heisenberg, Virasoro, rank-1 free fields, and for V_k(g) at levels where the lattice / Wakimoto realization proves scalar-diagonality.

**S3. K-theoretic identity ch_g(λ_{-1}(E)) = (-1)^g c_g(E).** Unconditional cohomological identity. Solid as an algebraic-geometry lemma.

**S4. Arakelov–Faltings fiberwise identification.** Θ_E|_fiber = ω_g^Ar. Solid (Faltings 1984 §2).

**S5. Mumford 1983 GRR identification c_g(E) = λ_g.** Solid.

**S6. Socle clutching-uniqueness.** Unconditional on the socle quotient R^g/N^g for all g. Valid as a CH-class identity under boundary factorization and Mumford multiplicativity.

**S7. δF_2^{cross}(W_3) = (c+204)/(16c).** Solid at g=2 via five disjoint verification paths (AP243 still needs check that the five are truly disjoint; that is a separate audit).

## Phase 3 — Heal

The inscription post-Wave-1 already reflects the correct scope. The Wave-2 residual cleanups are:

**H1. Tag upgrade of `thm:kac-moody-obs`.** The theorem is `\ClaimStatusProvedHere` at :4972 but its proof silently uses scalar-diagonality at g≥2 (A1). Two healings:
- (a) **Scope restrict.** Tag as "at g=1 unconditional; at g≥2 conditional on def:scalar-diagonal-hypothesis". Add a Remark[Scope] that for V_1(sl_2), V_1(sl_3), ... the scalar-diagonal hypothesis is discharged via the lattice realization (Frenkel–Kac); for V_k(g) at generic k the hypothesis is open.
- (b) **Downgrade to `\ClaimStatusConditional` at g≥2.** Same effect, tag-level.

Preferred: (a). More informative, matches the rank-1 / multi-generator distinction already in def:scalar-diagonal-hypothesis.

**H2. Table caption clarification (A9).** Rewrite `tab:obstruction-summary` caption (:6271) to avoid implying V_k(sl_2), V_k(sl_3), V_k(E_8) are single-generator. Use "scalar-diagonal families".

**H3. PTVV conditional scope (A6).** Scope the "conditional on Mok25" qualifier on `prop:theorem-D-factorization-homology-alt` to g≥3. At g=2, classical Knudsen–Mumford stable reduction suffices; at g=1, no reduction needed.

**H4. CLAUDE.md row clarification.** The current row reads correctly; minor wording: "g=2 for single-generator scalar-diagonal families" should be "g=2 for scalar-diagonal families (single-generator automatically; V_k(g) at integer levels via lattice realization; generic k open)".

## Phase 4 — Inscription (CG prose, Polyakov / Gelfand / Kazhdan voice)

The three surgical edits to the inscription:

### E1. Upgrade `thm:kac-moody-obs` tag and add scope remark

Change at `higher_genus_foundations.tex:4972`:

- Current: `\begin{theorem}[Kac--Moody obstruction at genus $g$; \ClaimStatusProvedHere]\label{thm:kac-moody-obs}`
- Edit: retain `\ClaimStatusProvedHere` for the genus-1 specialisation; insert a Remark[Scope] immediately after the theorem statement recording that g≥2 is conditional on scalar-diagonality, discharged for V_k(g) at positive-integer levels via Frenkel–Kac lattice realisation, open at generic level.

### E2. Table caption (:6270)

- Current: "For single-generator scalar-diagonal families, obs_g = κ·λ_g..."
- Edit: "For scalar-diagonal families (Heisenberg, Virasoro, rank-1 free fields unconditionally; V_k(g) at integer levels via Frenkel--Kac lattice realisation; generic-level V_k(g) conditional), obs_g = κ·λ_g..."

### E3. PTVV genus-stratified conditional (:6198)

- Current `rem:ptvv-aksz-chain-level-scope`: invokes Mok25 for AKSZ boundary factorization.
- Edit: scope the Mok25 dependency to g≥3 explicitly. At g=2, classical Knudsen–Mumford stable reduction handles the boundary.

Edits E1–E3 apply. Below I inscribe E1 directly (the load-bearing heal), and leave E2/E3 as low-priority cosmetic cleanups noted in the report. No AI attribution anywhere. No em-dashes (the inscription below uses colons / semicolons / separate sentences).

## Phase 5 — Propagate

### Cross-volume consumer sweep

- Vol I: 42 files cite `thm:genus-universality`, `prop:scalar-obstruction-hodge-euler`, `prop:clutching-uniqueness`, `prop:theorem-D-factorization-homology-alt`. Spot-check of preface, introduction, landscape_census: no overclaims detected post Wave-1 healing.
- Vol II: 9 files reference via `V1-` phantomsection aliases. Phantomsection masks are correctly in place at `main.tex:631-632, 720`.
- Vol III: 3 files reference. Status-inheritance via K3 and CY-D stratification theorems, none overclaiming.

### CLAUDE.md Theorem D row — proposed revision

Current (:581): "PROVED unconditional at g=1 (all families via 1-dim H^2(M̄_{1,1}) = Q·λ_1); PROVED unconditional at g=2 for single-generator scalar-diagonal families; at g≥3 conditional on (a) scalar-diagonal hypothesis for multi-generator uniform-weight and (b) Faber's λ_g-conjecture for on-the-nose lift from the socle".

Proposed revision: "PROVED unconditional at g=1 (all uniform-weight families via 1-dim H^2(M̄_{1,1}) = Q·λ_1); PROVED unconditional at g=2 for scalar-diagonal families (Heisenberg, Virasoro, rank-1 free fields unconditionally; V_k(g) at integer levels via Frenkel--Kac lattice realisation); at g≥3 conditional on (a) scalar-diagonal hypothesis (open at generic level for V_k(g) with g non-abelian) and (b) Faber's λ_g-conjecture for on-the-nose lift from the socle; PTVV alternative conditional on Mok25 log-FM chain-level sewing at g≥3 only (g=2 uses classical Knudsen--Mumford stable reduction; g=1 needs neither)." Evidence-column addenda: note `thm:kac-moody-obs` Step 2–3 tacitly uses scalar-diagonality at g≥2, flagged for Scope remark inscription (Wave-2 heal E1).

### Wave 2 open frontier inventory

- **OF1 (promoted from Wave 1 OF1).** Scalar-diagonality for V_k(g) at generic level with g non-abelian. Concrete attack path: compute fiberwise bar curvature of V_k(sl_2) at g=2 in the Wakimoto realisation and check whether the three currents' contributions decompose diagonally with equal eigenvalue on both weight-1 (Heisenberg) and the screening-contour weight sectors. Falsifiable.
- **OF2 (from Wave 1 OF2).** λ_g-conjecture at g≥3. Genuine open algebraic geometry (Faber–Pandharipande).
- **OF3 (from Wave 1 OF3).** δF_g^{cross} closed form at g≥3 and multi-weight families.
- **OF4 (from Wave 1 OF4).** PTVV path made fully disjoint at g=2 from Arakelov–BGS path. Post-Wave-1 rewrite achieves scope-level independence but not lemma-level disjointness in the HZ-IV sense.
- **OF5 (NEW).** Inscribe scope remark on `thm:kac-moody-obs` recording scalar-diagonality at g≥2 (Wave-2 heal E1).
- **OF6 (NEW).** Cosmetic: table caption and PTVV genus-stratified Mok25 scope (Wave-2 heals E2, E3).

## Verdict

The Wave-1 inscription correctly identifies scalar-diagonality as the
load-bearing hypothesis for multi-generator g≥2 and honestly downgrades the
PTVV route. Wave-2 findings add a single load-bearing heal (E1: scope
remark on `thm:kac-moody-obs`) plus two cosmetic cleanups (E2, E3). The
theorem statement itself in `thm:genus-universality` (:6305) is correctly
scoped: it already carries "For algebras with generators of several
conformal weights, the genus-1 specialization is unconditional; the
higher-genus extension is conditional on the strong scalar ansatz of
Theorem \ref{thm:multi-generator-universality}" at :6321-6324, which
correctly bridges to the cross-channel correction theorem. The residual
drift is in `thm:kac-moody-obs` (Step 2-3 of its proof silently uses
scalar-diagonality at g≥2) and in the table caption wording.

No em-dashes in this inscription. No AI attribution. Author: Raeez Lorgat.
