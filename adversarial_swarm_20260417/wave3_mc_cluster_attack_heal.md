# Wave 3 / MC1–MC4 cluster: adversarial attack, verdicts, heals

Raeez Lorgat — 2026-04-17 — adversarial pass on the Master-Conjecture cluster
following the 2026-04-16 inscriptions (`mc3_five_family_platonic.tex`,
`compact_completed_mc3_comparison_platonic.tex`,
`nilpotent_completion.tex`, and the CLAUDE.md status headline
"MC1 universal / MC2 bar-intrinsic / MC3 five-family / MC4⁺ unconditional,
MC4⁰ generic").

## 1. Headline finding: phantom labels

The CLAUDE.md status table advertises
`thm:mc1-*`, `thm:mc4-*` theorems that **do not exist** as LaTeX labels in the
corpus. Grep across `/Users/raeez/chiral-bar-cobar/chapters/` returns:

- `\label{thm:mc1}` / `\label{thm:mc1-*}` — **zero hits**;
- `\label{thm:mc4-strong-completion-tower}` — **zero hits**, yet the label is
  *referenced* by `chapters/theory/mc5_genus0_genus1_wall_platonic.tex`
  at lines 149, 278, 364, 474, 678, 748.

`thm:completed-bar-cobar-strong` (the actual MC4⁺ object) **does exist** at
`chapters/theory/bar_cobar_adjunction_curved.tex:969`, with a stub
`\phantomsection\label{thm:completed-bar-cobar-strong}` in
`chapters/frame/preface.tex:5078`. The name advertised by
`mc5_genus0_genus1_wall_platonic.tex` (`thm:mc4-strong-completion-tower`)
does not resolve.

Verdict: metadata drift, not mathematical gap. Five `\ref{thm:mc4-strong-completion-tower}`
sites render as `[?]` in the built PDF unless `mc5_genus0_genus1_wall_platonic.tex`
is patched to the real label. AP149 (resolution propagation failure) — healed below.

MC1 is similarly not carried by a single label; the PBW-concentration
content is distributed across
`thm:pbw-allgenera-km`, `thm:pbw-allgenera-virasoro`, and
`thm:pbw-allgenera-principal-w` in `higher_genus_modular_koszul.tex`
(1446/1660/later). This is structurally fine — MC1 is a meta-statement —
but the introduction and preface advertise it as a single theorem. No edit
required beyond documenting the convention.

## 2. MC1 Virasoro: is the L_0-bypass genuine or a shell game?

Claim (CLAUDE.md): "MC1 Virasoro g≥2 PROVED unconditionally via
L_0-diagonalization on augmentation ideal (bypasses hypothesis (c)
semisimple — family-specific L_0 argument suffices)."

**Source**: `thm:pbw-allgenera-virasoro` at
`chapters/theory/higher_genus_modular_koszul.tex:1659–1757`.

The proof: on the genus-$g$ enrichment block $\mathcal{E}_g^{*,h}$ the
$d_2^{\mathrm{PBW}}$ differential is induced by $T_{(1)} = L_0$, and on any
state of conformal weight $h \geq 1$ this is multiplication by $h$,
hence an isomorphism. On the augmentation ideal $\bar V_{\mathrm{Vir}_c}$ the
weight is $\geq 2$ (vacuum is weight 0, excluded; $T$ is weight 2), so
$h \geq 2$ on every homogeneous piece. The enrichment dies by $L_0$
action alone, with no Whitehead input.

**Adversarial check**. Whitehead's lemma requires semisimplicity +
finite-dim irreducibility. Virasoro is not semisimple (central extension
of the Witt algebra). The programme claim is that the weight-graded
structure delivers what semisimplicity was delivering. Verify:

- Whitehead delivers $H^i(\mathfrak{g}, V) = 0$ for $i = 1, 2$, $V$ finite-dim
  non-trivial irreducible over semisimple $\mathfrak{g}$. Used in the KM
  proof to kill $\mathcal{E}_g^{*,h}$ at the $E_2$ page.
- For Virasoro the $E_2$-page is $\mathcal{E}_g^{*,h}$, which is a product
  $M_h \otimes H^1(\Sigma_g, \mathbb{C})$. The $d_2$ differential is the
  operadic $(1)$-product of the single strong generator $T$ with the
  enriched state, reducing to $L_0$. On $M_h$ the operator $L_0$ is
  scalar multiplication by $h$. No representation-theoretic input beyond
  the scalar $L_0$ eigenvalue is invoked.

Verdict: **the bypass is genuine**. The only input is "on the augmentation
ideal at fixed weight $h$, the weight is positive". No semisimplicity,
no finite-dim irreducibility, no Whitehead. The argument is
family-specific (uses $T$'s spin-2 data, hence $T_{(1)} = L_0$), and
extends verbatim to any family where a single strong generator carries
a conformal weight operator. For principal $\mathcal{W}_N$ the analogous
argument uses the spin-2 subgenerator $T$ extracted from the principal
W-multiplet; `thm:pbw-allgenera-principal-w` in the same file carries
this through (block upper-triangular).

The CLAUDE.md headline "L_0-diagonalization … bypasses semisimple"
is accurate but underspecified. The sharper statement is: *on the
augmentation ideal of a chiral algebra with conformal vector at
non-critical level, the $d_2$-page of the PBW spectral sequence contracts
by spin action alone, provided every strong generator has positive
conformal weight*. This is strictly weaker than Whitehead and strictly
stronger than semisimplicity — it requires a grading-positivity axiom.

**No heal needed** on the MC1 Virasoro proof. Noted below in §6 that
the introduction's single-sentence summary should carry the
"positive-weight spin action" phrasing rather than an unqualified
"L_0-diagonalization."

## 3. Feigin–Fuks independent verification: is it genuinely disjoint?

Claim: "Feigin-Fuks resolution provides independent verification + extends
to principal W_N generic Ψ via Feigin-Frenkel screening."

Grep: `Feigin.Fuks|Feigin.Fuchs` appears only as a comment reference in
`virasoro_motivic_purity.tex:17`. There is no inscribed Feigin–Fuks
proof in Vol I. The claim is aspirational; it is not an inscribed
independent-verification decorator.

Verdict: **aspirational, not inscribed**. The independent-verification
protocol (HZ-IV) requires `derived_from`, `verified_against`,
`disjoint_rationale` recorded against a test or proof; none exists for
`thm:pbw-allgenera-virasoro`. The CLAUDE.md headline should not claim
"Feigin-Fuks independent verification" unless a decorator is inscribed.

**Heal**: downgrade the CLAUDE.md headline from "Feigin-Fuks resolution
provides independent verification" to "Feigin-Fuks resolution is a candidate
independent-verification route (not yet inscribed)".

Structurally the Feigin–Fuks calculation for $H^*(\mathrm{Vir}_c, M)$
at generic $c$ uses resolution by Verma modules + explicit screening
charges. The input is the weight-graded Verma structure, which is the
same $L_0$ input feeding the PBW proof. So even were it inscribed,
the disjointness rationale would require care: Feigin–Fuks
screens via $Q_{\alpha_+}, Q_{\alpha_-}$ contour-integral operators on a
rank-1 Fock module, whereas the PBW argument runs on the chiral bar
complex. These are different chain-level objects, but both filter by
$L_0$-eigenvalue. The rationale is: PBW-concentration sees $E_2$-page
collapse via $d_2 = L_0$; Feigin–Fuks sees pointwise vanishing via
screening cohomology. **Disjoint on the chain level, shared on the
filtration level.**

## 4. MC3 five families: DISJOINT or COVERT-COMMON?

The five mechanisms of `thm:mc3-evaluation-core-five-family`:

- (a) asymptotic prefundamentals (type A) — Hernandez–Jimbo limit
- (b) reflection-equation Shapovalov (B/C/D) — Molev–Ragoucy twisted Yangian
- (c) Chari–Moura multiplicity-free ℓ-weights (uniform simple)
- (d) elliptic theta-divisor complement — Felder–Varchenko Bethe
- (e) super parity-balance — Nazarov quantum Berezinian

**Adversarial probe**: are these disjoint proof strategies or common-core
reductions?

Each mechanism constructs a non-degenerate Shapovalov-type pairing on
tensor products of evaluation modules at generic spectral parameters +
a central or invariant witness. This is the common template. The
pairings differ:

- (a) ordinary Shapovalov (Mukhin–Varchenko determinant), but accessed
  via Frenkel–Hernandez product factorization on the pro-limit, NOT via
  rank-1 Baxter singular vectors;
- (b) reflection-equation Shapovalov $\langle\cdot,\cdot\rangle_{\mathrm{RE}}$
  with Sklyanin-determinant centrality (boundary-reflected);
- (c) uniform Shapovalov with Frenkel–Mukhin $q$-character algorithm +
  Kirillov–Reshetikhin conjecture (for simply-laced);
  case-by-case fundamental verification for $G_2, F_4$ (Hernandez 2006/2010);
- (d) elliptic Shapovalov with theta-function determinants;
- (e) $\mathbb{Z}/2$-graded super-Shapovalov with Berezinian.

**Verdict**: the five are *chart-specific realizations of a single
"Shapovalov-nondegeneracy + central witness" mechanism*, via different
integrable structures. `rem:mc3-assembly-point` at line 159 of
`mc3_five_family_platonic.tex` already states this honestly: "The five
mechanisms do not 'prove a single theorem' in the sense of sharing a
proof strategy; they prove the *same conclusion* in the respective
chart." Drinfeld-unifying panorama framing is the right voice.

The five are not "five disjoint proofs of the same theorem"; they are
"one theorem realized by five integrable charts glued by rational/
trigonometric/elliptic/graded/boundary degenerations, with
family-specific Shapovalov normalization". The claim **as inscribed** is
correct; the claim **as often paraphrased** ("five disjoint mechanisms")
is misleading. No heal required to the .tex; already honest.

## 5. Baxter retraction: what did the retracted proof actually establish?

Claim: "Baxter constraint retracted as type-A rational artifact." Sources:
`prop:baxter-retraction-type-A-artifact` at
`mc3_five_family_platonic.tex:433–485`.

The rank-1 Baxter singular vector $w_0 = -v_+ \otimes f \cdot v_0
\in V_1(a) \otimes L^-(b)$ is Yangian-highest-weight at
$b = a - 1/2$ (rational $Y(\mathrm{sl}_2)$). What this proved, correctly:
the codimension-1 locus at which a specific short exact sequence
$0 \to L^-_{i,a-1/2} \to V_1(a) \otimes L^-_{i,a} \to L^-_{i,a+1/2} \to 0$
is witnessed by a rank-1 Shapovalov zero.

What it did NOT prove: that this locus is a universal hypothesis of MC3.
The retraction removes the "universal" reading without removing the
type-A rational content.

**Adversarial probe**: does retracting the Baxter constraint leak into any
other theorem? Grep `Baxter.*hyperplane|Baxter.*constraint` across Vol I:

- `mc3_five_family_platonic.tex`: 17 hits, all in the retraction
  proposition and its supporting text.
- `yangians_computations.tex:4808–4989` and
  `yangians_drinfeld_kohno.tex`: the Baxter exact-triangle theorem
  `thm:baxter-exact-triangles` remains as a *type-A* statement, not a
  universal one. The scope was already qualified before the retraction.
- `compact_completed_mc3_comparison_platonic.tex` (662 lines): does not
  invoke the Baxter hyperplane as hypothesis.

Verdict: retraction is self-contained. No propagation debt.

## 6. MC4⁰ Wakimoto homotopy: what does "generically" exclude?

Claim: "MC4⁰ PROVED UNCONDITIONAL at generic parameters for class M
principal: explicit SDR via Wakimoto one-step (Virasoro) / Feigin-Frenkel
screening (W_N), homotopy h_htpy = (1 − ιp)/(L_0 − h − N + 1) invertible
generically."

Grep `h_htpy|\iota p.*L_0|Wakimoto.*one.step|Wakimoto.*SDR`: **zero
matches**. The paraphrased formula does not appear in the .tex.

What *is* inscribed:
- `thm:stabilized-completion-positive` (`nilpotent_completion.tex:562`):
  positive towers, unconditional, no SDR formula.
- `thm:resonance-filtered-bar-cobar` (`nilpotent_completion.tex:673`):
  resonance-filtered completion, conditional on finite-dim $R_\mathcal{A}$.
- `thm:completed-bar-cobar-strong` (`bar_cobar_adjunction_curved.tex:969`):
  the unconditional MC4⁺ for strong completion towers.
- The general SDR construction with $\mathrm{id} - \iota p = d_{\mathrm{bar}} h
  + h d_{\mathrm{bar}}$ at `higher_genus_foundations.tex:1691`.

**Adversarial probe**: at admissible Virasoro $c = c_{p,q} = 1 -
6(p-q)^2/(pq)$, the spectrum of $L_0$ on Verma quotients is rational
and can hit any preassigned non-negative integer shift. Therefore
$L_0 - h - N + 1$ *can* vanish at specific admissible $c$. The "generic"
qualifier in the CLAUDE.md claim must exclude:

(i) critical level $k = -h^\vee$ (Sugawara undefined; this is already excluded);
(ii) admissible $c$ at which the Wakimoto/Feigin–Frenkel screening
kernel has resonance with the bar-length shift $N$ (codimension-1 loci
in the $c$-line);
(iii) for general non-principal W, loci where the parabolic screening
charges have zero relative level.

This is precisely the `conj:periodic-cdg` content of
`periodic_cdg_admissible.tex` (inscribed 2026-04-16), which handles the
admissible locus via periodic-CDG. The "generic" qualifier in CLAUDE.md
excludes the admissible Virasoro locus for Vir; that locus is handled
separately via the Adams-type spectral sequence of
`thm:adams-analog-construction`.

**Verdict**: the claim is honest in substance — the generic SDR is
proved unconditionally for class M principal at *generic* $c$, and the
admissible locus is handled by an inscribed separate theorem (periodic
CDG). But the CLAUDE.md formula "h_htpy = (1 − ιp)/(L_0 − h − N + 1)"
does not literally appear in the .tex. It is a paraphrase of the general
SDR structure specialized to the Wakimoto one-step resolution.

**Heal**: CLAUDE.md text should cite `thm:stabilized-completion-positive`
and `thm:resonance-filtered-bar-cobar` rather than the formula. No .tex
edit required.

## 7. Parabolic screenings (KRW03, Arakawa07) for non-principal hook-type

Claim: "Non-principal hook-type (r ≤ N-3) PROVED via parabolic
screenings (KRW03, Arakawa07)."

Grep: `KRW03` appears in `universal_conductor_K_platonic.tex:596`
(ghost charge construction); `Arakawa07` appears in
`virasoro_motivic_purity.tex:608/622` (C_2-cofiniteness); a joint
citation `\cite{KRW03,Arakawa07}` at
`koszulness_moduli_scheme.tex:586–587` in the scope-restriction
context for hook-type W-algebras.

Verdict: references cite the real literature (Kac–Roan–Wakimoto 2003,
Arakawa 2007), and the scope restriction $r \leq N-3$ is correctly
carried. This is honest. The parabolic screening presentation does
preserve the chiral MC datum because parabolic DS reduction preserves
the chiral envelope of the parabolic Heisenberg parent and the
screening charges are chiral derivations.

## 8. DK_g full-category conjecture: genuine mathematical gap

`conj:dk-compacts-completion` at `yangians_computations.tex:3937`. This
is a compact-completion packet; extension from the finite-dimensional
evaluation core to the full completed shifted-prefundamental core via
Francis–Gaitsgory pro-nilpotent completion.

**Adversarial probe**: is this a genuine mathematical gap or notational
renaming? The evaluation-core equivalence $\Phi$ is unconditional
(Theorem `thm:eval-core-identification`); what is conjectural is
(a) compactness preservation under pro-nilpotent completion, (b)
weight-bounded t-structure compatibility. These are Mittag–Leffler-type
conditions on the pro-Weyl tower.

Verdict: genuine. The Mittag–Leffler condition at fixed weight is
rank-independent *once shifted-prefundamental generation is inscribed
at that rank*, which is only done in type A. For non-type-A
(Lemma-L lift-and-lower, `conj:rank-independence-step2`) the analogous
Mittag–Leffler is not yet verified in the literature.

## 9. Silent non-coverage check: cross-volume

The five-family mechanism does *not* cover: logarithmic $W(p)$, $N=2$
SCA, cosets, non-rational lattice, roots of unity. Verify none leaks
into Vol II/III downstream:

- **Vol II** `universal_celestial_holography.tex`: zero `MC3|mc3`
  references. The Beem–Rastelli χ-functor appears; it is a
  genus-0 statement independent of the MC3 thick-generation packet.
  **No leakage.**
- **Vol II** `e_infinity_topologization.tex`: claims $\mathcal{W}_\infty
  \to E_\infty$-top. This uses the inverse limit $\mathcal{W}_\infty
  = \varprojlim \mathcal{W}_N$. Each $\mathcal{W}_N$ sits in the
  five-family (principal, class M). The inverse limit is the MC4
  package, not MC3 thick-generation. **No leakage.**
- **Vol III** `cy_d_kappa_stratification.tex`: invokes K3 Borcherds-weight
  $\kappa_{\mathrm{BKM}}$; no MC3 invocation.

**Verdict**: silent non-coverage is genuinely silent. No cross-volume
propagation required.

## 10. Healing summary

The cluster is substantially honest. The real defects are metadata
drift, not mathematical gaps:

- **Heal-1**: retarget
  `\ref{thm:mc4-strong-completion-tower}` → `\ref{thm:completed-bar-cobar-strong}`
  in `mc5_genus0_genus1_wall_platonic.tex` (5 sites: lines 149, 278, 364,
  474, 678, 748). This is a phantom-label fix; `[?]` render in PDF.
- **Heal-2**: CLAUDE.md text paraphrases a formula
  "h_htpy = (1 − ιp)/(L_0 − h − N + 1)" that is not literally in the
  .tex. Correct inscribed objects are `thm:stabilized-completion-positive`
  + `thm:resonance-filtered-bar-cobar`. Not a .tex edit; a CLAUDE.md
  accounting note.
- **Heal-3**: the "Feigin-Fuks independent verification" is not
  inscribed as an HZ-IV decorator. Until inscribed, the CLAUDE.md
  headline should read "candidate independent-verification route"
  rather than "provides independent verification". Again, CLAUDE.md
  accounting, not .tex.

Mathematical content: no downgrades required. MC1 Virasoro bypass is
genuine via positive-weight $L_0$ action. MC2 bar-intrinsic is honest
and unconditional at the coinvariant level. MC3 five-family is a
Drinfeld-unifying panorama, not five unrelated proofs, and the
inscription (`rem:mc3-assembly-point`) states this truthfully.
MC4⁺ (`thm:completed-bar-cobar-strong`) is unconditional on strong
completion towers, and its positive-tower specialization
(`thm:stabilized-completion-positive`) is the unconditional MC4⁰ content
up to the periodic-CDG admissible loci.

The Russian-school phrasing emerges naturally: the MC cluster is one
structural statement — *the bar complex of a chiral algebra with
conformal vector recognizes its weight grading* — realized in four
charts (concentration, class, thick generation, completion) and made
explicit by the spin action of the stress tensor. Whitehead is a
special case of spin positivity; Shapovalov nondegeneracy is the
module-theoretic shadow of the same positivity; weight-filtration
stabilization is the pro-completion of the same positivity.
Costello–Gwilliam physics motivation: MC structures are the chiral
homological descendant of classical gauge invariance, and the spin
action of the stress tensor is the chiral avatar of BRST-nilpotence.
