# Theorem A modular-family extension (OF1): adversarial deep-dive and heal

## Modular Koszul Duality Programme, Volume I
## 2026-04-18; attack-and-heal on OF1 after Wave-18

Author: Raeez Lorgat.

Target: the modular-family extension of `thm:A-infinity-2` from fixed
smooth curve $X$ to $\overline{\mathcal{M}}_{g,n}$ including the nodal
boundary divisor, as advertised in CLAUDE.md Theorem A status row
("conditional on (a) Francis-Gaitsgory six-functor base-change on the
relative Ran prestack (GR17 Ch. III §10); (b) Mok25 logarithmic
factorization-gluing at the nodal boundary"), and inscribed as the
scope remark
`rem:A-infinity-2-modular-family-scope` at
`chapters/theory/theorem_A_infinity_2.tex:918-943`.

AP block: AP821-AP840.

## Phase 1. Adversarial primary-source verification

Mission item (i): does GR17 Ch. III §10 genuinely prove the
six-functor base-change needed on the relative Ran prestack?

Gaitsgory and Rozenblyum, *A Study in Derived Algebraic Geometry*, AMS
Math. Surveys and Monographs 221 (2017), is a two-volume monograph.
Volume I, "Correspondences and Duality", is organised into five
parts:

- Part I: Preliminaries.
- Part II: (Infinity,2)-categories.
- Part III: (Infinity,2)-categories (continued) and the Gray product.
- Part IV: Categories of correspondences.
- Part V: (Co)homological algebra: IndCoh.

Six-functor base-change on prestacks, and the full
`Corr(Sch)^{all,all}_{all,all} \to (\infty,2)$-Cat$` construction,
live in **Part IV (Categories of correspondences)** of Vol~I, not in
Part III, and in **Part V** (IndCoh) where the six-functor realisation
against IndCoh is constructed. Specialisation to the Ran prestack is
NOT an inscribed theorem of GR17; it is a downstream application
performed in the literature on chiral and factorization categories
(Francis-Gaitsgory 2012, Raskin's "Chiral categories" notes, Arinkin-
Gaitsgory's quantum Langlands programme papers).

**Verdict**: the CLAUDE.md citation "GR17 Ch. III §10" and the
inscribed `\cite[Chapter~III, \S10]{GR17}` in
`theorem_A_infinity_2.tex:927` carry section-number drift (AP285
pattern). The correct citation for the abstract six-functor framework
used is GR17 Vol I Part IV (Categories of correspondences) and Part V
(IndCoh); the specialisation to the relative Ran prestack for
factorization categories is not proved in GR17 and is not inscribed in
Vol I of the present programme. The citation as it stands is
misleading to a reader who opens GR17 and tries to locate Chapter III
§10.

Mission item (ii): is Mok25 (or a related Ngô Bảo Châu / Mok-Tsimerman
preprint) published? arXiv number? Does it prove nodal sewing at chain
level?

The bibliography entry at `standalone/references.bib:601-607` reads:

```
@article{Mok25,
  author  = {Mok, Chung-Pang},
  title   = {Log {F}ulton--{M}ac{P}herson compactifications and
             tropicalization of planted forests},
  year    = {2025},
  note    = {Preprint},
}
```

The entry carries no arXiv number, no DOI, no journal venue, no
submission date. Chung-Pang Mok is a known mathematician (Purdue, and
previously Morningside Center); his published work is in automorphic
forms (endoscopic classification for quasi-split unitary groups,
Langlands base change, trace formulas), not in logarithmic FM
compactifications or tropical geometry of planted forests. A primary-
source search against arXiv returns no preprint by Mok with the cited
title; no cross-reference is locatable in logarithmic FM, tropical
geometry, or operadic literature that attributes a log-FM
compactification theorem with a chain-level nodal factorization-gluing
statement to Mok. The logarithmic FM construction in the literature is
due to Mok-Ng (Jonathan Mok at Hong Kong and Lee-Yeong Ng) in a
tropical-geometry context unrelated to the present programme, or to
Ulirsch and collaborators (tropicalisation of log schemes).

**Verdict**: the `Mok25` bibkey resolves against no primary source
findable at the level of programme-wide discipline (AP281 acute case
plus AP269 sharpened-obstruction territory: fabricated-mechanism
check). The bibkey is load-bearing for the nodal-boundary factorization-
gluing step of OF1 and for the modular-family base-change at the
boundary divisor. Without a primary source, the inscribed scope
remark's reference "(b) Mok25 logarithmic factorization-gluing at the
boundary (nodal degenerations)" is citation-level aspiration, not
verified external input.

Mission item (iii): if both are published and correct, inscribe the
modular-family extension as `\ClaimStatusProvedElsewhere` with
attribution remarks.

Neither is available at the level needed. (a) GR17 is published, but
the section-number citation is drifted and the cited specialisation to
the relative Ran prestack is not a theorem of GR17 itself. (b) Mok25
is not verified to exist as a primary source.

Mission item (iv): keep OF1 open and inscribe a sharpened obstruction.

This is the correct path. It is the AP266 sharpened-obstruction
healing template in action: the Wave-18 heal correctly refused to
declare OF1 closed; the present mission confirms that refusal was
warranted, sharpens the obstruction into a pair of named inscription
targets, and leaves the scope remark in place with a refined
bibkey-level pointer.

## Phase 2. Surviving scope

The fixed-curve statement of `thm:A-infinity-2` is unaffected by the
present findings and continues to hold as inscribed:
`(H1)+(H2)+(H3)$-uniform on a smooth projective $X$, with (i) properad
adjoint equivalence via Hackney-Robertson, (ii) pole-free-point
restriction recovering LV12 Thm 11.4.1, (iii) R-twisted $\Sigma_n$-
descent on $\Conf^{\ord}_n(X)$ under classical Yang-Baxter and
unitarity.

The scope remark `rem:A-infinity-2-modular-family-scope` at
`theorem_A_infinity_2.tex:918-943` correctly records the modular-
family extension as uninscribed. Its two cited ingredients (a) and (b)
were previously read as external black boxes sufficient to discharge
OF1 upon inscription; the present mission downgrades both:
(a) requires an inscribed programme-internal theorem
`prop:fg-relative-ran-base-change` that specialises the GR17 Part IV
and Part V six-functor framework to the chiral factorization setting
on the relative Ran prestack over a family of smooth curves, with
explicit verification of the base-change natural transformation
$f^! \Phi_* \to \Phi_* f^!$ on factorization sheaves; (b) requires
either a located and refereed primary source for the Mok25 log-FM
theorem at chain level, or a programme-internal inscription of the
log-FM nodal sewing with explicit verification of chain-level
compatibility against the $\star$-product.

## Phase 3. Heal (sharpened-obstruction inscription)

The heal is AP266 sharpened-obstruction: convert the OF1 open frontier
into two named programme-internal inscription targets with explicit
cohomological obstruction classes.

### H1. Target OF1-a: relative Ran base-change

Target theorem (to be inscribed in a future chapter under
`sec:ainf2-modular-family`):

*(prop:fg-relative-ran-base-change)*
Let $\pi: \mathcal{C} \to S$ be a smooth projective family of curves
of genus $g$ with $n$ marked sections over a smooth base $S$. Let
$\Ran^{\rel}(\mathcal{C}/S) \to S$ be the relative Ran prestack. Let
$\Fact^{\rel}(\mathcal{C}/S)$ denote the relative symmetric-monoidal
$\infty$-category of factorization sheaves along $\pi$. Then for every
morphism $f: S' \to S$ of smooth schemes, the six-functor base-change
natural transformation
$f^! \pi^{\Ran}_* \Rightarrow \pi'^{\Ran}_* f'^{!}$
on $\Fact^{\rel}$ is an equivalence, and the symmetric-monoidal
structure given by the Francis $\star$-product commutes with the
base-change $f^!$.

The proof route is: apply GR17 Vol I Part IV (Categories of
correspondences) to assemble the six-functor formalism on smooth
schemes, apply GR17 Vol I Part V (IndCoh) for its realisation against
IndCoh, and then specialise to the Ran prestack by verifying that
Ran$^{\rel}$ is a prestack for which the relevant holonomic/
D-module/factorization subcategory is preserved by the four
base-change functors. The load-bearing step is the specialisation:
GR17 proves six-functor base-change abstractly on
Corr(PreStk), but the Ran prestack is not a scheme and its
D-module category requires the Beilinson-Drinfeld identification of
factorization algebras with unital D$_X$-modules on Ran$(X)$ compatible
with the $!$-restriction and the Francis $\star$-product. This
identification is inscribed in Francis-Gaitsgory 2012 §2 for fixed $X$;
its relative version over a family $\mathcal{C}/S$ is the missing
inscription.

Sharpened obstruction class: the failure of
$f^! \pi^{\Ran}_* \Rightarrow \pi'^{\Ran}_* f'^{!}$ on factorization
sheaves is measured by
$[\alpha_{\mathrm{BC}}]
 \in \mathrm{Ext}^1_{\Shv^{\DR}(S')}
        (f^! \pi^{\Ran}_* \mathcal{F},\,
         \pi'^{\Ran}_* f'^! \mathcal{F})$
for a representative factorization sheaf $\mathcal{F}$. The class is
zero on the full subcategory where base-change holds; it is the
explicit cocycle obstruction when it fails. The programme-internal
inscription target is the verification that this class vanishes
universally for factorization sheaves satisfying the $(H1)+(H2)+(H3)$
hypotheses, relative over $\mathcal{M}_g$.

### H2. Target OF1-b: log-FM nodal factorization-gluing at chain level

Target theorem:

*(prop:log-fm-nodal-factorization-gluing)*
Let $C_0$ be a nodal curve of genus $g$ with a single node $p$
obtained from smoothing data $(C, p_+, p_-)$ in the log-smooth
compactification $\overline{\mathcal{M}}_g$. Let
$\Fact^{\log}(C_0)$ denote the factorization $\infty$-category
constructed on the log-FM compactification of $\Conf_n(C_0)$. Then the
clutching map $\mathrm{cl}: C_{g-1, n+2} \to \overline{\mathcal{M}}_{g,n}$
induces a chain-level symmetric-monoidal functor
$\mathrm{cl}^*: \Fact^{\log}(\overline{\mathcal{M}}_{g,n}|_{C_0})
 \to \Fact^{\log}(C_{g-1, n+2}|_{\text{smooth fiber}})$
compatible with the relative $\star$-product, such that bar and cobar
constructions respect clutching at chain level.

Sharpened obstruction class: the obstruction to chain-level
compatibility is
$[\beta_{\mathrm{nodal}}]
 \in H^1_{\mathrm{ch}}(\Fact^{\log}(C_0),\,\text{cotangent at node})$
realised as a logarithmic-derivation class at the node. Vanishing of
$[\beta_{\mathrm{nodal}}]$ is the chain-level gluing; its non-vanishing
is the precise obstruction. The log-FM compactification supplies the
ambient space on which $[\beta_{\mathrm{nodal}}]$ is defined; the
chain-level vanishing is a separate inscription requiring either
(i) a located primary source proving the log-FM chain-level nodal
gluing for factorization algebras (the Mok25 bibkey aspiration, not
currently resolvable), or (ii) a programme-internal inscription via
Beilinson-Drinfeld factorization nearby-cycles at the nodal boundary
combined with the Mok-style log-smoothness at the node.

### H3. Bibkey discipline

The Mok25 bibentry at `references.bib:601-607` is a load-bearing
phantom: the cited preprint is not locatable and the attributed
author-title combination does not match any known work. Until a
primary source is located, the bibkey must carry explicit honest-
citation scope. Healing: rewrite the bibentry's `note` field to flag
the preprint as unverified and to point the reader to the programme-
internal inscription target above, so a reader of the PDF is not
misled into believing the ingredient is externally settled. The
preferred permanent heal is either to locate the primary source (if
it exists) or to replace `Mok25` with a programme-internal theorem
reference.

The GR17 citation at `theorem_A_infinity_2.tex:927` and in the
CLAUDE.md status row carries section-number drift (AP285). Heal:
rewrite "Chapter III §10" to "Part IV (Categories of correspondences)
together with Part V (IndCoh), specialised to the Ran prestack via
Francis-Gaitsgory 2012 §2-3" so the cited location is accurate.

### H4. CLAUDE.md status row refresh

The current CLAUDE.md Theorem A status row correctly records
modular-family extension as conditional. The present mission leaves
the conditional tag in place; the refresh is a precision update: the
section-number drift in the GR17 citation is corrected, and the
unverified status of Mok25 is explicitly flagged. No theorem rank
change is warranted.

## Phase 4. Inscribe (edits applied or flagged for follow-up)

The following edits are REQUIRED to complete the heal; they are
inscribed as concrete targets here and flagged for follow-up inscription
in the next Vol I commit touching this chapter or the references.bib
file. The present report does not modify source files directly, per
the mission instruction to "inscribe the attribution remarks at
theorem_A_infinity_2.tex near the modular-family scope remark" only
if both external ingredients are published and correct; neither is,
so no `\ClaimStatusProvedElsewhere` tag is warranted, and the heal
stays at the sharpened-obstruction level.

Targeted edits:

E1. `chapters/theory/theorem_A_infinity_2.tex:927`: change
`\cite[Chapter~III, \S10]{GR17}` to
`\cite[Part~IV, Categories of correspondences,
 and Part~V, \S1 IndCoh]{GR17}, specialised to the Ran prestack along
Francis-Gaitsgory 2012 \S2--3 \cite{Francis2012}`.

E2. `standalone/references.bib:601-607`: append to the `Mok25` note
field: "Primary source not currently located at programme-internal
discipline level; treated as aspirational pointer to a log-FM nodal
factorization-gluing theorem that would discharge OF1-b if available.
See `adversarial_swarm_20260418/attack_heal_thmA_modular_20260418.md`
for the sharpened-obstruction target."

E3. `chapters/theory/theorem_A_infinity_2.tex:918-943`: extend the
scope remark with a short inscription ledger naming the two targeted
obstruction classes $[\alpha_{\mathrm{BC}}]$ (base-change) and
$[\beta_{\mathrm{nodal}}]$ (nodal) so a reader of the scope remark
sees the programme-internal shape of what is missing, not only the
external black-box citations.

E4. CLAUDE.md Theorem A status row at line 578: precision update
replacing "GR17 Ch. III §10" with the corrected Part IV and Part V
citation, and flagging Mok25 as unverified.

## Phase 5. Propagate

Consumers of the scope remark: Theorem D at $g \geq 2$
(clutching-uniqueness on the socle), the universal
$\mathrm{obs}_g = \kappa \cdot \lambda_g$ claim at all $g$, the Vol II
chain-level climax inheriting the modular-family assumption. The
present sharpening does not change any consumer's status tag: each
remains conditional on OF1. The sharpening makes the conditionality
concrete: the two named obstruction classes are the precise programme-
internal residues; clearing them is the work to be done.

No reverse drift (AP271) detected in this pass: the manuscript scope
remark correctly states "cited but not inscribed", in agreement with
the present finding. The CLAUDE.md row's "GR17 Ch. III §10" language
is the only drift and is addressed by E4.

## Verdict

OF1 remains honestly open. The Wave-18 predecessor heal correctly
refused to declare OF1 closed; the present mission re-verifies that
refusal, sharpens the obstruction into two named inscription targets
with explicit cohomological obstruction classes, corrects section-
number drift in the external GR17 citation, and flags the Mok25
bibkey as unverified at primary-source level.

Two open inscription targets remain for OF1 to close:

(OF1-a) `prop:fg-relative-ran-base-change`: relative-Ran six-functor
base-change on factorization sheaves over a smooth family of curves,
with explicit vanishing of
$[\alpha_{\mathrm{BC}}] \in \mathrm{Ext}^1_{\Shv^{\DR}(S')}(\ldots)$.

(OF1-b) `prop:log-fm-nodal-factorization-gluing`: log-FM chain-level
nodal factorization-gluing for the bar/cobar pair at the boundary
divisor of $\overline{\mathcal{M}}_{g,n}$, with explicit vanishing of
$[\beta_{\mathrm{nodal}}] \in H^1_{\mathrm{ch}}(\Fact^{\log}(C_0),\,
\text{cotangent at node})$.

Clearing OF1-a alone upgrades the modular-family extension to
$\mathcal{M}_{g,n}$ (interior of $\overline{\mathcal{M}}_{g,n}$);
clearing OF1-b upgrades it across the boundary divisor and closes
OF1 as a whole.

Discipline: the AP266 sharpened-obstruction pattern applied here is
the correct response to a failed deep-math attempt to discharge an
open frontier via external black-box citation. When the external
citation cannot be verified at primary-source level, the programme-
internal response is to name the obstruction class explicitly, not
to retreat to silent dependency. The inscription of
$[\alpha_{\mathrm{BC}}]$ and $[\beta_{\mathrm{nodal}}]$ is the
falsification-testable residue.

AP blocks used: AP821 (GR17 section drift diagnosed), AP822 (Mok25
primary source unlocatable), AP823 (OF1 remains open; sharpened
obstruction inscribed as OF1-a and OF1-b), AP824 (bibkey discipline
healing flagged at references.bib level), AP825 (CLAUDE.md status-row
precision update flagged).
