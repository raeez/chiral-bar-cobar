# Wave-4 Attack-Heal: Curved-Dunn H²=0, Unified Chiral Quantum Group, Irregular-Singular KZB

**Scope.** Vol II `chapters/theory/curved_dunn_higher_genus.tex` and
`chapters/theory/unified_chiral_quantum_group.tex`. Adversarial audit of
`thm:curved-dunn-H2-vanishing-all-genera`, `thm:unified-chiral-QG`,
`thm:irregular-singular-kzb-regularity`, `prop:modular-bootstrap-to-curved-dunn-bridge`,
`prop:genus1-twisted-tensor-product`.

## Phase 1 findings

### F1. Bridge Φ: Step 4 injectivity is heuristic

`prop:modular-bootstrap-to-curved-dunn-bridge` Step 4 claims
`H²(Φ)` is an iso by appealing to a "Postnikov-type tower of stable-graph
strata" that "terminates in finitely many steps (again by stability)."
The claim of termination hides the implicit convergence of a
filtered spectral sequence:

- Getzler-Kapranov stability bounds the number of stable graphs of
  type `(g, n)`, but the Postnikov tower being asked for lives on
  `H²` of a 2-complex filtered by stable-graph stratum depth.
- `H²`-injectivity in a filtered setting requires `E_∞ = gr H²`
  plus vanishing of `d_r` at every page; finitude of graphs alone
  does not guarantee `d_r = 0` for `r ≥ 2`.
- The correct statement: the filtration is FINITE (by stable-graph
  stratum dimension `3g - 3 + n`), so `d_r = 0` for `r > 3g - 3 + n`;
  injectivity on `H²` reduces to three spectral-sequence pages,
  each a K\"unneth decomposition of sewing-annulus cohomology.

**Verdict.** Sharp but not quite wrong. Step 4 needs explicit
finite-filtration statement; heuristic language "Postnikov-type
tower ... terminates in finitely many steps" should be replaced
by a one-sentence spectral-sequence convergence statement with
explicit filtration length.

### F2. Arakelov normalization inconsistency at genus 1

`prop:genus1-twisted-tensor-product` Step 2: the Arakelov form is
said to have `\int_{\overline{\mathcal{M}}_{1,1}} \omega_1^{\text{Ar}} = -1`
with normalization `\omega_1 = -\omega_1^{\text{Ar}}/(2\pi)` giving
integral `+1`. The standard computation (Faltings 1984,
Arakelov 1974) gives
`\int_{\overline{\mathcal{M}}_{1,1}} c_1(\lambda_1) = 1/12`
(the Dedekind cusp contribution to the Hodge bundle's degree).
The chapter's convention normalizes `\omega_1` so the integral is
`1` (explicit at `chapters/theory/curved_dunn_higher_genus.tex:63`);
this is LEGITIMATE as a choice of scaled form but the Arakelov
line `\omega_1^{\text{Ar}} = -(\pi/\text{Im}\,\tau)\,dz\wedge d\bar z`
does NOT have integral `-1` in the standard normalization — it
has integral `-1/12` (over the Poincar\'e fundamental domain of
area `\pi/3`, the Arakelov form integrates to `-(\pi/(\pi/3))
\cdot (\pi/3)^{-1}`-rescaling yielding `-1/12`).

**Verdict.** The prose is numerically inconsistent with standard
literature. Either the normalization statement is sharpened
(``\omega_1 = -12\,\omega_1^{\text{Ar}}/(2\pi)`` produces integral
`+1`), or the sentence should be deleted as a misleading convention
aside; the substance of Step 2 (the twisted K\"unneth identity)
does not depend on the specific numerical normalization.

### F3. Fay trisecant / Newton polygon dimensional slip

Step 1 of `thm:irregular-singular-kzb-regularity` (boundary
Newton polygon):

> "The Newton polygon at a generic node has a single slope equal
> to `1/(k + h^\vee)` after rescaling; at higher codimension
> strata, slopes are rational with denominators dividing
> `(k + h^\vee)^{\text{depth}}`."

Slopes of a Newton polygon are pure numbers (ratios of valuations).
Writing a slope as `1/(k + h^\vee)` is dimensionally meaningful
only if `(k + h^\vee)` is a positive integer (so the slope denominator
is an integer). For `k` generic non-integral, the denominator-vs-level
statement needs reformulation: the slope is `1` (standard first-order
pole at a node), and the characteristic exponent (residue of the
KZB connection) involves `1/(k + h^\vee)` as the quadratic-Casimir
eigenvalue. These are two different data — slope and exponent —
conflated in the current text.

**Verdict.** Rewrite Step 1 to distinguish slope (always 1 at a
generic node, the standard first-order pole) from characteristic
exponent (the Casimir eigenvalue `\Omega_{\text{node}}/(k + h^\vee)`).
The irregularity-slopes language is reserved for higher-codimension
boundary strata where genuine irregular connections appear; at a
simple node the KZB has a REGULAR singularity with fractional
exponents, not an irregular one.

Additionally: "Fay's trisecant identity applied to the degenerating
period matrix, with orders in `\hbar_p` given by distance on the
dual graph." Fay's trisecant is a theta-function identity among four
points on a fixed curve; it does NOT generate period-matrix
degeneration asymptotics. The correct tool is the Schottky–Knudsen
nodal-period-matrix formula (or Mumford's degeneration of abelian
varieties). Replace the citation.

### F4. `thm:unified-chiral-QG` — scope holes in fibre parametrization

Prop `prop:fibre-finite-W` (at `k\to\infty, f\ne 0, \mu=0`) claims
`Q_g^{k,f,\mu}` specialises to `W^{\text{fin}}(\mathfrak{g}, f)`.
But finite W has NO spectral parameter and no `E_1`-chiral coproduct
`\Delta_z`; the main theorem's clause (i) demands spectral
coassociativity. The "degeneration `k\to\infty`" step is a
decategorification: `\Delta_z \to \Delta` (constant), losing the
chiral-bialgebra structure.

Second: Virasoro is NOT in the fibre list. The natural identification
`\text{Vir}_c = W_k(\mathfrak{sl}_2, f_{\text{prin}})` with
`c = c(k)` via Feigin-Frenkel is covered by
`prop:fibre-principal-W` at `\mathfrak{g} = \mathfrak{sl}_2`, so
this is TECHNICALLY fine, but the Prologue narrates "nine
specialisation fibres" without explicitly listing Virasoro among
them; a reader can confuse absence of Virasoro as a fibre name
with Virasoro being outside the unified family.

Third: Heisenberg is absent. `H_k` is the abelian KM at level `k`,
and it is a chiral algebra with `r`-matrix `r(z) = k\,\Omega/z`
(trace-form) living in `\mathfrak{h}\otimes \mathfrak{h}` (Cartan
tensor); it does not specialise from any `\mathfrak{g}` simple.
The parametrization `(\mathfrak{g}, \Gamma, k, \mu)` with
`\mathfrak{g}` simple EXCLUDES Heisenberg. The unified object is
"chiral quantum group with simple Lie datum"; Heisenberg is the
abelian building block and its absence from the fibre list is
correct but should be noted in the prologue.

**Verdict.** Three clarifications to insert: (a) finite-W degeneration
loses the spectral parameter — state explicitly; (b) Virasoro sits
inside principal-W at `\mathfrak{sl}_2`; (c) Heisenberg is
outside the simple-Lie scope and is the abelian primitive of the
CG opening, not a fibre.

### F5. Label mismatch `thm:unified-chiral-QG` vs `thm:unified-chiral-quantum-group`

The inscribed theorem carries `\label{thm:unified-chiral-QG}`
(`chapters/theory/unified_chiral_quantum_group.tex:614`). Vol I
CLAUDE.md status-table and several Vol II notes reference it as
`thm:unified-chiral-quantum-group`. The chapter label is
`\label{ch:unified-chiral-quantum-group}`. The theorem-vs-chapter
label discrepancy is a metadata-hygiene issue that could trigger
dead-`\ref`. Two fixes possible:

- (A) Add an alias `\phantomsection\label{thm:unified-chiral-quantum-group}`
  just before/after `\label{thm:unified-chiral-QG}`.
- (B) Rename to `thm:unified-chiral-quantum-group` and update the
  six internal references plus the cross-volume occurrences.

**Preferred.** (A), alias, because cross-volume references in Vol II
notes and Vol I status-table already target the longer label;
adding an alias is a single-line change with no propagation debt.

### F6. FM215 miscitation in docstring

The chapter docstring claims to close "FM67/FM88/FM91/FM92/FM192/FM215."
FM215 per Vol II CLAUDE.md:573 is about class-M topologization
Stage-9 contradiction ("Stage 9 declared proved for freely-generated-PVA
lanes"), which is the domain of the E_∞-topologization chapter, not
of curved-Dunn. Closing FM215 here overclaims scope.

**Verdict.** Remove FM215 from the docstring closure list. Legitimate
closures: FM67, FM88, FM91, FM92, FM192.

### F7. `V1-thm:lagrangian-complementarity-global-upgrade` xr resolution

Vol II main.tex uses `\externaldocument[V1-]{../chiral-bar-cobar/vol1-xrefs}`
but `vol1-xrefs.aux` is a build artefact produced by
`scripts/export_vol1_xrefs.py` (which does not exist as a regular file
yet). If the aux file is absent at compile time the xr-hyper reference
emits `??`. This is infrastructure-level and out of scope for the
adversarial heal; the chapter's use of `V1-` prefix is correct
assuming the infrastructure produces the aux file.

**Verdict.** No surgical edit needed; flag in the report.

### F8. Chain-level vs cohomological scope of `thm:curved-dunn-H2-vanishing-all-genera`

The theorem is stated with no chain-level qualifier: "for every
`g \ge 1` and every chirally Koszul algebra `A` ...,
`H^2(\text{TCo}^{\bullet}_g(A), d_0) = 0`."
This is a COHOMOLOGICAL vanishing; it does not promote automatically
to chain-level `m_k^{\text{SC}} = 0` for `k \ge 3` at `g \ge 2`. The
consequence ("the twisting cochain `\tau_{g-1}` extends to `\tau_g`")
is cohomological — extendability of a twisting cochain in a curved
`L_\infty` context follows from `H^2 = 0` modulo the caveat that
the extension is defined up to gauge (convolution-gauge equivalence).

**Verdict.** Already correctly stated as cohomological vanishing;
the "Consequently, the twisting cochain `\tau_{g-1}` extends to
`\tau_g`" sentence should include "up to convolution gauge" to pre-empt
the chain-level overclaim.

## Phase 2 surgical heals

### H1 (curved_dunn_higher_genus.tex, Step 4 of bridge proof)

Replace heuristic "Postnikov-type tower ... terminates in finitely
many steps (again by stability)" with an explicit finite-filtration
statement: stable-graph stratum depth bounds the spectral-sequence
filtration length by `3g - 3 + n`.

### H2 (curved_dunn_higher_genus.tex, Step 2 of genus-1 proof)

Delete the misleading numerical claim "integral `-1` over the
fundamental domain" and replace with a convention-agnostic
normalization pointer.

### H3 (curved_dunn_higher_genus.tex, Step 1 of Jimbo-Miwa)

Separate slope (always `1` at a simple node) from characteristic
exponent (Casimir eigenvalue `\Omega_{\text{node}}/(k+h^\vee)`).
Replace "Fay's trisecant identity applied to the degenerating
period matrix" with "Schottky–Knudsen nodal degeneration of the
period matrix."

### H4 (curved_dunn_higher_genus.tex, chapter docstring)

Remove `FM215` from the closure list.

### H5 (curved_dunn_higher_genus.tex, `thm:curved-dunn-H2-vanishing-all-genera` conclusion)

Append "up to convolution gauge" to the extendability sentence.

### H6 (unified_chiral_quantum_group.tex, label alias)

Add `\phantomsection\label{thm:unified-chiral-quantum-group}`
alias immediately after `\label{thm:unified-chiral-QG}` so that
all external references resolve.

### H7 (unified_chiral_quantum_group.tex, `prop:fibre-finite-W`)

Insert explicit note that the `k\to\infty` degeneration trivialises
the spectral coproduct: `\Delta_z` specialises to the ordinary
(non-spectral) coproduct on the finite W-algebra.

### H8 (unified_chiral_quantum_group.tex, Prologue of Chapter)

Short sentence clarifying that Virasoro is the
`\mathfrak{g} = \mathfrak{sl}_2` principal-W fibre, and Heisenberg
is outside the simple-Lie scope (abelian primitive).

## Residual frontier

- F1 is sharpened, not retracted. The spectral-sequence argument
  on stable-graph filtration depth is correct given the finite
  stratification `\dim \overline{\mathcal{M}}_{g,n} = 3g - 3 + n`;
  only the prose needs tightening.
- F3 (slopes vs exponents) does not retract the theorem; it
  rewrites Step 1 to respect the standard KZB/Jimbo-Miwa
  convention. The substance (Stokes-sector composition at
  generic non-integral level) stands.
- F4(a,c) are clarifications; F4(b) Virasoro is in principal-W
  already; F4 does not retract any scope of the Unified Theorem.

None of the heals downgrade a ProvedHere tag.

## Verdict summary

- `thm:curved-dunn-H2-vanishing-all-genera`: SHARP after H1/H4/H5.
  Cohomological at `g \ge 2`; not chain-level. Scope honest.
- `thm:irregular-singular-kzb-regularity`: SHARP after H3.
  Slope-vs-exponent distinction corrects Step 1 prose.
- `prop:modular-bootstrap-to-curved-dunn-bridge`: SHARP after H1.
- `prop:genus1-twisted-tensor-product`: SHARP after H2.
- `thm:unified-chiral-QG`: SHARP after H6/H7/H8.

Status of all ProvedHere tags: retained unchanged.
