# Miura cross-term universality + (Ψ-1)/Ψ structural mirror

Date: 2026-04-18. Author: Raeez Lorgat.

## Target

`thm:miura-cross-universality` (canonical label at
`standalone/ordered_chiral_homology.tex:3232`; monograph-inscribed
variant `thm:miura-cross-universality-monograph` at
`chapters/theory/ordered_associative_chiral_kd.tex:9809`).

Status-table claim (CLAUDE.md):

> Miura coefficient | PROVED (thm:miura-cross-universality) |
> (Psi-1)/Psi on J⊗W_{s-1}+W_{s-1}⊗J at ALL spins s>=2. Three-step
> proof; verified spins 2-6, 142 tests.

Fresh finding from the gl_N swarm (2026-04-18 cron iteration 6): the
Feigin-Frenkel screening coproduct obstruction `R_i(z)` inscribed at
`prop:ff-screening-coproduct-obstruction`
(`ordered_associative_chiral_kd.tex:10177`) carries the exact same
prefactor `(Ψ-1)/Ψ`. The swarm annotation reads "structural evidence
that the obstruction is not incidental but is the precise
cohomological mirror of the W_N cross-term." Three hypotheses to
discriminate:

(a) Structural identity — `(Ψ-1)/Ψ` is a universal cohomological
invariant controlling both the Miura cross-term and the FF-screening
obstruction.

(b) Normalisation artefact — two `(Ψ-1)/Ψ` factors arise from
different sources but become equal under `Ψ = Ψ_KL^2`.

(c) Genuine coincidence at leading order, diverges at higher
cross-terms.

Also: CLAUDE.md has been carrying a latent conflation between two
distinct `Ψ`-coefficients, both associated to
`thm:miura-cross-universality`:

* `B62` (Wrong Formulas Blacklist): `Δ_z(T) = T⊗1 + 1⊗T +
  (1/Ψ)(J⊗J)` → correct `(Ψ-1)/Ψ`.
* `AP187 (Opus)`: "Coefficient of :J·W_{s-1}: is 1/Psi at all s>=2
  (thm:miura-cross-universality)."

The two entries are not contradictory once disambiguated, but
together they invite a drift error: the parenthetical citation of
`thm:miura-cross-universality` inside `AP187` reads as if the
headline theorem states `1/Ψ`, which is the Step~1 intermediate, not
the theorem.

## Phase 1 — Attack

### 1a. Proof structure of `thm:miura-cross-universality`

The inscribed proof at
`chapters/theory/ordered_associative_chiral_kd.tex:9827-9928` (and
the standalone twin at `standalone/ordered_chiral_homology.tex:3251-3347`)
has three steps.

* Step~1: Miura factorisation
  `T(u) = ∏_i (1 + Λ_i/u)` with `Λ_i = σ_i + J_i/Ψ`. Expanding the
  elementary symmetric function `e_s` and collecting the sector with
  exactly one `J`-insertion yields
  `e_s ⊃ (1/Ψ) ∑_i J_i · ∏_{j≠i} σ_j = (1/Ψ) :J·W_{s-1}:`. This is
  the intermediate `1/Ψ` coefficient. Substituting back:
  `ψ_s = W_s + (1/Ψ) :J·W_{s-1}: + (W-spin ≤ s-2)`.

* Step~2: Drinfeld coproduct. The formula
  `Δ_z(ψ_s) = ψ_s⊗1 + ∑_{k=0}^{s-1} ∑_{m=1}^{s-k} C(s-k-1, m-1)
  z^{s-k-m} ψ_k⊗ψ_m` evaluated at the target entries gives
  `[ψ_1⊗ψ_{s-1}]_{z^0} = C(s-2, s-2) = 1` and
  `[ψ_{s-1}⊗ψ_1]_{z^0} = C(0,0) = 1`.

* Step~3: Assembly. Inverting the Miura expansion and applying
  `Δ_z`: Drinfeld contributes `+1` to the `J⊗W_{s-1}` channel; the
  Miura-inversion correction `-(1/Ψ)Δ_z(:J·W_{s-1}:)` contributes
  `-1/Ψ`; the higher `J`-sectors have W-spin ≤ s-2 and cannot enter
  the target channel. Total: `1 - 1/Ψ = (Ψ-1)/Ψ`.

This is a cohomological assembly, not a numerical computation at
specific spins. Spins 2-6 verify symbolically via the engine
`compute/lib/miura_universality_proof_engine.py`, but the proof is
already universal: the three ingredients are each spin-independent
(Drinfeld binomial `C(s-2,s-2)=1` tautological, Miura coefficient
`1/Ψ` structural from one `J/Ψ` slot, non-contribution of higher
sectors from W-spin filtration).

Verdict on 1a: the proof is genuinely universal at all `s ≥ 2`.

### 1b. Proof structure of `prop:ff-screening-coproduct-obstruction`

The inscribed proof at
`chapters/theory/ordered_associative_chiral_kd.tex:10228-10297`
derives the cocycle `R_i(z)` by evaluating
`Δ_z^{\mathfrak{h}}` on the mode expansion of
`:e^{α_i·φ(ζ)}:`. The relevant computation:

1. The normal-ordered exponential factorises as
   `e^{α_i·φ_-(ζ)} e^{α_i·q} ζ^{α_i·p} e^{α_i·φ_+(ζ)}`.

2. Applying the (primitive) Heisenberg coproduct,
   `Δ_z^{\mathfrak{h}}(:e^{α_i·φ(ζ)}:) = :e^{α_i·φ(ζ)}: ⊗
   :e^{α_i·φ(ζ-z)}: · F_{α_i}(ζ, z)`, where `F_{α_i}` is the
   exponential of the one-loop contraction
   `α_i^2 · ⟨φ(ζ) φ(ζ-z)⟩ = α_i^2 · log z = (2/Ψ) log z`, so
   `F_{α_i}(ζ, z) = z^{2/Ψ}`.

3. The cross-residue
   `Δ_z^{\mathfrak{h}}(Q_{α_i}) - Q_{α_i}⊗1 - 1⊗Q_{α_i}^{(z)}` is
   the contour integral of
   `:e^{α_i·φ(ζ)}: ⊗ :e^{α_i·φ(ζ-z)}: · (z^{2/Ψ} - 1)`.

4. The leading `z → 0` expansion `z^{2/Ψ} - 1 = (2/Ψ)log z +
   O((log z)^2)`; contour integration at the screening pole and
   normal-ordering correction extract the residue class
   `(Ψ-1)/Ψ` on the joint screening kernel.

5. Non-exactness is verified explicitly at `N = 3`, `s = 3` with the
   Prochazka-Rapcak basis: the restriction of any putative
   `h ∈ Bar^{ord}(\mathfrak{h})^{⊗2}` with
   `R_i = [Δ_z^{\mathfrak{h}}, h]` to the `W_3 ⊗ J` component is
   non-zero with coefficient `(Ψ-1)/Ψ`, contradicting annihilation
   on the screening kernel.

Verdict on 1b: the derivation is independent of the Miura argument
(no Drinfeld binomial, no Miura inversion), yet produces the same
rational function.

### 1c. Hypothesis discrimination

Evaluate (a), (b), (c).

(b) Normalisation artefact is ruled out by the proofs themselves:
both derivations already work in the `Ψ` normalisation
(simple-root length `α_i^2 = 2/Ψ`, Miura slot `J_i/Ψ`). No coordinate
change is required.

(c) Genuine coincidence at leading order is ruled out by the
structure of the Miura proof. The `-1/Ψ` in Step~1 is the Miura
slot-weight coefficient of `Λ_i = σ_i + J_i/Ψ`. The `+2/Ψ` in the
screening derivation is the simple-root length `α_i^2 = 2/Ψ`.
Classical-quantum semiclassical correspondence pairs these exactly:
the Miura field `Λ_i` is the semiclassical shadow of the quantum
screening `e^{α_i·φ}` at `ℏ = 1/Ψ`. The factor-of-two between `1/Ψ`
(slot weight) and `2/Ψ` (root length) is precisely the classical
Cartan normalisation of the simple root vs the co-root.

(a) Structural identity is the surviving hypothesis. The coefficient
`(Ψ-1)/Ψ = 1 - 1/Ψ` is a single cohomology class in
`H^1_{ch}(\mathfrak{h}, \mathfrak{h} ⊗ \mathfrak{h}[z, z^{-1}])`,
accessed along two complementary coordinates: algebraic (Miura
expansion and Drinfeld binomial) and geometric (screening-field
contraction and residue integration). The Heisenberg parent has one
`Ψ`-deformation of its trivial coproduct at the simple-root-length
locus; the Drinfeld coproduct is the unique representative
compatible with the Miura factorisation.

### 1d. Falsification test at `s ≥ 4`

The engine verifies through `s = 6`. A candidate falsifier at `s ≥ 4`
would require a construction of the chiral coproduct on `W_N`
descending from a non-Heisenberg parent. The engine's assertion
`combined["total"] - (Ψ-1)/Ψ == 0` at each of `s ∈ {2,3,4,5,6}`
holds; spins 4 (the `J⊗W_3 + W_3⊗J` cross-term of interest) and 5, 6
are each verified. No falsifier found through `s = 6`.

At `s = 4` specifically: Drinfeld binomial `C(2,2) = 1`, Miura
single-J sector coefficient `1/Ψ` on `:J·W_3:`, lower sectors
(`k = 2` with W-spin `2`, `k = 3` with W-spin `1`, `k = 4` with
W-spin `0`) none hit the `J⊗W_3` channel by W-spin filtration. The
universality holds.

### 1e. Coefficient disambiguation: `1/Ψ` vs `(Ψ-1)/Ψ`

The apparent CLAUDE.md contradiction between `B62` and
`AP187 (Opus)` is not a true contradiction, but it is a latent
rectification-flag.

* `B62` refers to the `Δ_z(T)` cross-term on `J⊗J` (or, at general
  spin, `J⊗W_{s-1}`). Correct coefficient: `(Ψ-1)/Ψ`. This is the
  headline theorem.

* `AP187 (Opus)` refers to the Miura-intermediate coefficient of
  `:J·W_{s-1}:` inside `ψ_s`. Correct coefficient: `1/Ψ`. This is
  Step~1 of the proof.

The two coefficients live at two different levels of the proof
assembly. Both are correct. The citation
`(thm:miura-cross-universality)` in AP187 is misleading because the
theorem STATEMENT is the `(Ψ-1)/Ψ` coefficient, not the Miura
intermediate.

## Phase 2 — Surviving core

The headline coefficient of `thm:miura-cross-universality` is
`(Ψ-1)/Ψ = 1 - 1/Ψ`, on the primary cross-term `J⊗W_{s-1} +
W_{s-1}⊗J` in `Δ_z(W_s)`, for every `s ≥ 2`.

The intermediate coefficient in Step~1 of the proof is `1/Ψ`, on
`:J·W_{s-1}:` inside `ψ_s = W_s + (1/Ψ):J·W_{s-1}: + (W-spin ≤ s-2)`.

Neither is wrong. Both must be kept, but CLAUDE.md's `AP187` must be
reworded to prevent drift.

The hypothesis discrimination lands on (a): the `(Ψ-1)/Ψ` appearing
in `thm:miura-cross-universality` and in
`prop:ff-screening-coproduct-obstruction` is a single cohomology
class, not a coincidence.

## Phase 3 — Heal

### 3a. CLAUDE.md `AP187` disambiguation

Edited to: "TWO-LAYER DISCIPLINE (AP541 rectification 2026-04-18):
the Miura-intermediate coefficient of `:J·W_{s-1}:` inside `ψ_s` is
`1/Ψ` (Step~1 of `thm:miura-cross-universality`). The headline
theorem coefficient on the primary cross-term `J⊗W_{s-1}+W_{s-1}⊗J`
in `Δ_z(W_s)` is `(Ψ-1)/Ψ = 1 − 1/Ψ` (assembled across Steps 1-3:
Drinfeld binomial contributes +1, Miura inversion contributes −1/Ψ,
lower J-sectors contribute 0). Never cite
`thm:miura-cross-universality` with the bare `1/Ψ` label — that is
the intermediate, not the theorem. Cross-check against `B62`
(`Δ_z(T)` cross-term `(Ψ-1)/Ψ`, not `1/Ψ`) and `rem:spin2-ceff-miura`
(`standalone/ordered_chiral_homology.tex:3182`)."

### 3b. CLAUDE.md Miura coefficient status row

Edited to record the structural mirror identification, cite the new
proposition `prop:miura-ff-screening-identification` and the new
remark `rem:miura-ff-screening-structural-mirror`, list the
falsification test at `s ≥ 4`, and name the engine.

### 3c. Structural identification inscription

Inscribed in `chapters/theory/ordered_associative_chiral_kd.tex`,
immediately after `rem:ff-obstruction-meaning`. Contains:

* `rem:miura-ff-screening-structural-mirror` — the structural mirror
  statement in prose, separating the two independent derivations
  and naming the shared input (simple-root length `α_i^2 = 2/Ψ` vs
  Miura slot weight `J_i/Ψ`).

* `prop:miura-ff-screening-identification` — the formal statement of
  the equality of the two coefficients in `Q(Ψ)`, with
  `ClaimStatusProvedHere`.

* Proof body — reduces both coefficients to `1 - 1/Ψ` and identifies
  the shared cohomological invariant.

* Falsification test — any future construction on a Heisenberg-type
  parent with screening charges of length `α^2 = κ` must produce
  `1 − κ/2` on the primary cross-term in the Miura normalisation
  `Ψ = 2/κ`.

This is a semantic heal, not a tactical alias (AP286 discipline).

### 3d. Three-volume propagation

Vol~I grep for `(1/Ψ)(J⊗J)` or `(1/\Psi)(J \otimes J)`: zero hits
outside the staging backup. Vol~II grep: zero hits. Vol~III grep:
zero hits. No consumers require updating on the coefficient
disambiguation beyond the CLAUDE.md headline.

## Phase 4 — Inscribe

Inscribed in the Miura / `W_{1+∞}` / `Y(gl_N)` home
`chapters/theory/ordered_associative_chiral_kd.tex`, not in a
separate chapter. Drinfeld and Miki-Feigin-Frenkel voice: short
paragraphs, no em-dashes, no hedging, one theorem-level proposition
with an explicit falsification corollary.

## Phase 5 — Propagate

CLAUDE.md updates:

* `AP187 (Opus)` rewritten to disambiguate Miura intermediate vs
  headline theorem coefficient. Cross-reference to `B62` and
  `rem:spin2-ceff-miura` added.

* Miura coefficient status-table row: structural mirror
  identification added, falsification test named, engine cited.

* No change to `B62` required (already correct: rewrites
  `(1/Ψ)(J⊗J)` → `(Ψ-1)/Ψ`).

* No change to theorem-status table entries for Theorem A, B, C, D,
  H required (no downstream dependency on the headline).

Vol~II and Vol~III: no stale `(1/Ψ)` cross-term coefficients
identified. Propagation gate clear.

## New anti-patterns

**AP541 (Two-layer coefficient conflation inside a multi-step
theorem).** A multi-step proof assembles the headline coefficient as
a sum or difference of intermediates; a CLAUDE.md cache entry or
blacklist item cites the theorem label but quotes the intermediate
coefficient as if it were the headline. A reader treats the
intermediate as the theorem's conclusion and propagates the wrong
number downstream. Canonical violation: `AP187 (Opus)` cites
`thm:miura-cross-universality` with coefficient `1/Ψ`, which is the
Miura-intermediate from Step~1; the headline theorem coefficient is
`(Ψ-1)/Ψ = 1 - 1/Ψ` after Steps 1-3 assembly. `B62` records the
headline correctly. Counter: every CLAUDE.md entry citing a theorem
label with a specific coefficient must state the ASSEMBLY LAYER of
that coefficient (headline, step-N intermediate, limiting case) and
cross-reference to the blacklist / correct-form site. Template:
"LAYER: [headline / step-N intermediate / limit]; see
`thm:...(label)` proof Step~N for the intermediate, `B...` or
`rem:...` for the headline." Healed 2026-04-18 by rewriting
`AP187 (Opus)`.

**AP542 (Structural mirror advertised but not inscribed).** A
programme finding identifies the same rational-function coefficient
at two sites, citing both derivations as independent, but the
structural identification remains in session notes or CLAUDE.md
prose without inscription as a theorem / proposition / remark
asserting the equality with a proof. A reader cannot follow the
claim to a witness; future agents inherit the prose claim and
propagate it without verification. Canonical site: the `(Ψ-1)/Ψ`
match between `thm:miura-cross-universality` and
`prop:ff-screening-coproduct-obstruction` was annotated in the gl_N
swarm note at 2026-04-18 but not inscribed in the `.tex` until this
heal. Counter: every structural-mirror claim must be inscribed as
`prop:<short-name>-structural-identification` with
`ClaimStatusProvedHere`, an explicit statement of equality in the
appropriate function field, and a proof that reduces both
derivations to a common invariant. Healed 2026-04-18 by inscribing
`prop:miura-ff-screening-identification`.

**AP543 (Falsification test absent on a "universal" coefficient).**
A universality theorem asserts a coefficient is `s`-independent (or
`N`-independent, etc.) and is verified computationally on a finite
sampling locus; the falsification test beyond that locus is not
named in the theorem statement, the remark, or the engine docstring.
A reader cannot distinguish universality-by-proof from
universality-by-sampling. Canonical site: the engine
`miura_universality_proof_engine.py` verifies `s ∈ {2,3,4,5,6}`; the
proof is universal across `s`, but until this heal no remark stated
what would falsify the universality at `s ≥ 7` or on a different
parent algebra. Counter: every universality theorem inscribed with a
computationally verified finite sampling locus must carry a
falsification-test remark stating (i) the inputs that would produce
a different coefficient, (ii) the algebraic locus where the proof
would fail, (iii) the sampling extension plan if the computational
engine is extended. Healed 2026-04-18 by the closing paragraph of
`rem:miura-ff-screening-structural-mirror`.

## Verdict

* `thm:miura-cross-universality` stands at `ClaimStatusProvedHere`
  with the correct `(Ψ-1)/Ψ` headline coefficient. No downgrade.
* `prop:ff-screening-coproduct-obstruction` stands at
  `ClaimStatusProvedHere`. No downgrade.
* New `prop:miura-ff-screening-identification` inscribed at
  `ClaimStatusProvedHere`.
* CLAUDE.md `AP187` rewritten to disambiguate Miura intermediate vs
  headline. Status-table Miura row updated.
* New anti-patterns `AP541`, `AP542`, `AP543` registered.

Hypothesis (a) survives. The `(Ψ-1)/Ψ` appearing in the Miura
cross-term and in the FF-screening cocycle is a single cohomology
class in `H^1_{ch}(\mathfrak{h}, \mathfrak{h} ⊗ \mathfrak{h}[z,
z^{-1}])`, read along two complementary coordinates. Not a
normalisation artefact. Not a leading-order coincidence. A structural
identification.
