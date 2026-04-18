# Theorem A modular-family: Mok25 logarithmic factorization-gluing at the nodal boundary — attack-and-heal (2026-04-18)

Raeez Lorgat. Wave-12 companion to the GR17 agent. Tackles the SECOND ingredient of the
modular-family extension of `thm:A-infinity-2` from fixed smooth curve $X$ to
$\overline{\mathcal{M}}_{g,n}$ including the nodal boundary: Mok25
logarithmic factorization-gluing at the boundary (nodal degenerations). First ingredient
(GR17 six-functor base-change on the relative Ran prestack) is handled by the companion
agent `attack_heal_thmA_modular_20260418.md` / `wave1_theorem_A_attack_heal_v2.md`.

## Mok25 statement audit

Mok25 is REAL: Siao Chi Mok, arXiv:2503.17563, "Logarithmic Fulton–MacPherson configuration
spaces", submitted 21 March 2025, v2 21 May 2025 (Cambridge / Imperial College London,
algebraic geometry). The earlier iteration-2 Theorem A audit's "AP269 fabricated mechanism"
framing was a bibkey-drift artefact (`author = {Mok, Chung-Pang}` in
`standalone/references.bib:601-607` caused a search against the wrong Mok's publications);
it is RETRACTED per `attack_heal_mok25_programme_audit_20260418.md` +
`attack_heal_mok25_retraction_propagation_20260418.md`.

What Mok25 inscribes, with primary-source section/theorem numbers:

- Theorem 3.3.1: $\FM_n(X \mid D)$ is a smooth compactification of
  $C_n(X \setminus D)$ with normal-crossings boundary, whose codim-1 strata are
  the FM collision divisors $D^{\mathrm{FM}}_{ij}$ and the puncture-collision
  divisors $D^{\mathrm{punc}}_{i,\alpha}$.
- Theorem 5.2.3: flatness of the universal degeneration $W \to B$ with reduced
  fibres.
- Definition 3.1.5: planted-forest combinatorial data $(S_\rho, P, m)$
  indexing the strata.
- Definition 4.7.1: rigid combinatorial types $\rho$.
- Lemma 5.3.1: combinatorial cutting map $\kappa$ is a subdivision, bijective on
  supports and lattices.
- Corollary 5.3.4: special-fibre decomposition — the irreducible components of
  the special fibre of $\FM_n(W/B)$ biject with rigid types $\rho$, each
  component a modification of $\prod_{v \in V(S_\rho)} \FM_{I_v}(Y_v \mid D_v)$.

What Mok25 DOES NOT inscribe (load-bearing for Thm A modular-family):

- Factorization-sheaf-valued nearby-cycle functor $\Psi_\Delta$ along the
  boundary divisor of $\overline{\mathcal{M}}_{g,n}$.
- Chain-level transport of a factorization sheaf $\mathcal{F}$ satisfying
  (H1)+(H2)+(H3) through the subdivision of the special fibre.
- Relative log-FM compactification
  $\FM_n(\mathcal{C}/\overline{\mathcal{M}}_{g,n})$ chain-level gluing across
  the universal stable curve's node.
- Preservation of the bar-length Mittag-Leffler condition
  (`rem:A-inf-2-ml-step-2`) across the sewing.

## First-principles assessment of scope

Mok25 is a GEOMETRIC paper on a FIXED pointed curve $(X,D)$
(`configuration_spaces.tex:1383` "Fixed versus relative log FM spaces" remark
makes this explicit). The Theorem A modular-family extension needs three
additional layers beyond Mok25:

1. **Sheaf transport**: a factorization nearby-cycle functor $\Psi_\Delta$ in
   the Beilinson–Drinfeld sense (`BD04` Ch. 3) applied to factorization sheaves
   satisfying (H1)+(H2)+(H3).
2. **Chain-level vs cohomological**: Mok's Cor 5.3.4 gives a decomposition at
   the level of the special fibre; chain-level properad-equivalence across the
   boundary stratum requires Mittag-Leffler preservation across the sewing,
   which is NOT a Mok25 statement.
3. **Relative vs fixed**: Mok25's log-FM is for a fixed pointed curve; the
   Theorem A modular-family extension requires the RELATIVE log-FM over the
   universal stable family, referenced in Mok25 but not proved in
   `\cite[Theorem~3.3.1]{Mok25}`.

Preservation of (H3) — finite-dim graded bar pieces — across nodal sewing is a
per-class fact: unconditional on class G (Heisenberg, lattice at generic rank,
free chiral algebras: direct preservation), conditional on class L (affine
Kac–Moody at generic non-critical level: Beilinson–Drinfeld chiral sewing
preserves factorization structure on the Koszul locus), scope-restricted on
class M (Virasoro, principal $\mathcal{W}_N$: see MC5 chain-level class-M
weight-completed inscription, Vol II `universal_celestial_holography.tex`; raw
direct-sum class-M is genuinely false, MC5 scope artefact). Mok25 is
class-agnostic; the (H3) preservation question is orthogonal.

## Heal option chosen: (C) sharpened obstruction

Option (A) — inscribe `lem:mok25-log-factorization-gluing-properad` with full
proof body citing Mok25 Thm/Prop numbers — is NOT supportable: Mok25 alone
does not prove the factorization-sheaf-valued nearby-cycle theorem.
Option (B) — `\ClaimStatusProvedElsewhere` with attribution — would be
dishonest since Mok25 does not independently prove the chain-level
properad-level gluing on the relative log-FM.
Option (C) — sharpen the obstruction per AP266 — matches the GR17 agent's
$[\alpha_{\mathrm{BC}}]$ template and preserves programme honesty.

The heal inscribes a companion obstruction class $[\beta_{\mathrm{nodal}}]$
for the nodal factorization-gluing, extending the GR17 agent's
$[\alpha_{\mathrm{BC}}]$ into the modular-family scope remark at
`rem:A-infinity-2-modular-family-scope`.

## Inscribed obstruction class

```
beta_nodal: Psi_Delta (pi_log)_* F ==> (pi_log)_{*, D_Delta}
             (F(C') otimes_{F(hat D_p)} F(C''))
```

as a natural transformation on $\Fact^{\rel}(\mathcal{C}/\overline{\mathcal{M}}_{g,n})$
at the $\Delta$-boundary divisor $D_\Delta$ of the stable-graph stratification,
its failure measured by

```
[beta_nodal] in Ext^1_{Shv^{DR}(D_Delta)}( Psi_Delta (pi_log)_* F,
                  (pi_log)_{*, D_Delta} (F(C') otimes_{F(hat D_p)} F(C'')) )
```

Universal vanishing of $[\beta_{\mathrm{nodal}}]$ on the conilpotent-complete
(H1)+(H2)+(H3) subcategory, at every irreducible boundary divisor of
$\overline{\mathcal{M}}_{g,n}$, is the programme-internal inscription target
for ingredient (b).

Three structural observations sharpen the honest load-bearing claim
(inscribed as enumerated items (b1)-(b3) of the remark):

- (b1) Mok25 is geometric, not factorization-sheaf-valued. Cor 5.3.4
  supplies the boundary-space geometry; $\Psi_\Delta$ is a separate BD04
  Ch. 3 construction not inscribed at chain level in Vol I.
- (b2) Chain-level vs cohomological split. Mittag-Leffler preservation
  across the sewing is proved for class G (direct) and class L (BD chiral
  sewing at generic non-critical level); class M scope-restricted.
- (b3) Fixed-curve vs relative log-FM. Mok25's Thm 3.3.1 is for fixed
  pointed curve; the relative log-FM over $\overline{\mathcal{M}}_{g,n}$
  is the load-bearing missing ingredient.

## Scope remark edit zone

Inscribed text placed INSIDE `rem:A-infinity-2-modular-family-scope` at
`theorem_A_infinity_2.tex`, immediately after the GR17 agent's
$[\alpha_{\mathrm{BC}}]$ paragraph (line 1008). My insertion spans
approximately 110 new lines + an AP1241 single-preprint-pillar registration
(both ingredients are covered honestly in the same paragraph).

Companion edit: `rem:log-fm-fixed-vs-relative` label inscribed at
`configuration_spaces.tex:1383` (previously unlabeled remark, AP264 phantom-ref
avoidance: my (b3) paragraph cites it).

## Status delta for CLAUDE.md Theorem A row

Current row reads: "modular-family extension CONDITIONAL on ... (b) Mok25
logarithmic factorization-gluing at the nodal boundary, to globalise the
equivalence across the full compactified base. Neither (a) nor (b) is
inscribed as a theorem in Vol I."

Proposed delta (post-GR17-agent + this agent):

> "modular-family extension CONDITIONAL on clearance of two inscribed
> obstruction classes: (a) the relative-Ran base-change class
> $[\alpha_{\mathrm{BC}}] \in \mathrm{Ext}^1_{\Shv^{\DR}(S')}$ (inscribed
> at `rem:A-infinity-2-modular-family-scope`, sharpening the GR17 Part
> IV + Part V §1 + Francis2012 §2--3 citation chain); (b) the nodal
> factorization-gluing class $[\beta_{\mathrm{nodal}}] \in
> \mathrm{Ext}^1_{\Shv^{\DR}(D_\Delta)}$ (inscribed at
> `rem:A-infinity-2-modular-family-scope`, sharpening the
> Mok25 Thm 3.3.1 + Cor 5.3.4 + Lemma 5.3.1 citation chain). Vanishing
> of $[\alpha_{\mathrm{BC}}]$ is unconditional abstractly on IndCoh
> (GR17); restriction to factorization subcategory is the residual
> target. Vanishing of $[\beta_{\mathrm{nodal}}]$ is unconditional on
> class G, conditional on class L (generic non-critical level, BD chiral
> sewing), scope-restricted on class M (MC5 weight-completed). AP1241
> single-preprint-pillar registration: programme-wide load on Mok25
> (March 2025 arXiv preprint, v2 May 2025) is a scope item, not a
> soundness item; Theorem $A^{\infty,2}$ remains unconditional on fixed
> smooth curve $X$."

This upgrade is NOT from CONDITIONAL to UNCONDITIONAL; it is from
"cited-but-not-inscribed" to "sharpened-obstruction + per-class scope".
The modular-family extension is no longer a rhetorical closure; it is a
well-defined programme-internal inscription target with a
falsification test (compute $[\beta_{\mathrm{nodal}}]$ at a class-L
example: affine KM $V_k(\mathfrak{sl}_2)$ at $k = 1$, simplest nodal
$g=2$ clutching; the vanishing should follow from BD chiral sewing and
can be verified in compute).

## Coordination with GR17 agent

Non-conflicting edit zones respected. The GR17 agent edited:
- Paragraph 1 of the remark (opening)
- Enumerated item (a) with sharpened GR17 citation
- The $[\alpha_{\mathrm{BC}}]$ paragraph (lines 975-1008)

This agent edited:
- Enumerated item (b) wording was NOT touched (already present with honest
  Mok25 citation at lines 958-963 from a prior pass)
- The $[\beta_{\mathrm{nodal}}]$ paragraph inserted after the GR17 agent's
  handoff sentence at line 1007 ("The nodal boundary requires, in
  addition, clearance of the companion logarithmic class
  $[\beta_{\mathrm{nodal}}]$ supplied by ingredient (b).")
- The AP1241 single-preprint-pillar registration folded into the same
  remark at the tail.
- Companion `rem:log-fm-fixed-vs-relative` label inscription at
  `configuration_spaces.tex:1383`.

Zero edit-conflict. The two sharpened obstruction classes
$[\alpha_{\mathrm{BC}}]$ and $[\beta_{\mathrm{nodal}}]$ form a
matched pair analogous to the interior/boundary decomposition of
$\overline{\mathcal{M}}_{g,n}$.

## AP discipline

- **AP241** (advertised-but-not-inscribed characterization): avoided. The
  heal does NOT inscribe a new theorem; it sharpens the cited ingredient
  into a named obstruction class. CLAUDE.md headline will be rewritten
  to match the inscribed scope.
- **AP249** (base-change / extension theorems require inscription, not
  citation): heal discharges by inscribing the obstruction class rather
  than silently citing Mok25 as "nodal sewing done".
- **AP266** (sharpened-obstruction healing register): heal matches the
  positive template. Obstruction class inscribed with explicit
  Ext-group home, coefficient supplied by the Mok25 geometry +
  Beilinson–Drinfeld factorization nearby cycles.
- **AP272** (unstated cross-lemma via folklore citation): avoided. The
  cross-lemma (factorization nearby cycles) is cited explicitly to
  `\cite[Ch.~3]{BD04}` with the honest note "not inscribed at chain
  level in Vol I".
- **AP287** (cross-volume theorem existence without HZ-11 attribution):
  avoided. The scope-restricted class-M claim forwards to Vol II
  `universal_celestial_holography.tex` with explicit attribution.
- **AP281** (bibkey phantom-citation rate): Mok25 bibkey verified in
  `standalone/references.bib:601-607` with correct author (Siao Chi Mok),
  title, eprint 2503.17563. No phantom.

## No commits

Per task constraints. Edits are on disk; commit decision deferred to
programme-level rectification wave.
