# Theorem A modular-family extension (OF1-a): GR17 relative-Ran base-change

## Modular Koszul Duality Programme, Volume I
## Wave 12, 2026-04-18 — attack-and-heal on OF1-a, first-ingredient audit

Author: Raeez Lorgat.

Target: the first of two ingredients in `rem:A-infinity-2-modular-family-scope`
(`chapters/theory/theorem_A_infinity_2.tex:940-965`), namely the
Francis--Gaitsgory six-functor base-change on the relative Ran prestack.
Sibling agent handles Mok25 log-FM nodal gluing.

Predecessor: `adversarial_swarm_20260418/attack_heal_thmA_modular_20260418.md`
(Phase 4 "flagged for follow-up" edits E1 and E3 were inscribed as
targets but not applied). This Wave-12 note APPLIES them.

## Phase 1. Adversarial primary-source audit

GR17 is Gaitsgory--Rozenblyum, *A Study in Derived Algebraic Geometry*,
AMS Math. Surveys Monogr. 221 (2017), Vol I (Correspondences and
Duality). Its five-part structure is Part I (Preliminaries), Part II
(infinity,2-categories), Part III (Gray product), **Part IV (Categories
of correspondences)**, **Part V ((Co)homological algebra: IndCoh)**.

Six-functor base-change on prestacks, and the
`Corr(Sch)^{all,all}_{all,all} \to (\infty,2)$-Cat$` construction,
live in Part IV; its IndCoh realisation is Part V. The chapter file
already cites GR17 elsewhere under this canonical layout:

- `theorem_A_infinity_2.tex:639` cites `[Chapter~I.3]{GR17}` for
  stability/presentability of $\Shv^{\DR}(\Ran(X))$ — standard.
- `theorem_A_infinity_2.tex:640` cites `[Chapter~IV.5, \S1.3]{GR17}`
  for the symmetric monoidal structure — standard.
- `theorem_A_infinity_2.tex:643` cites `[Chapter~IV.5, Theorem~3.1.2]{GR17}`
  for the $(\infty,2)$-enhancement — standard.
- `theorem_A_infinity_2.tex:949` (pre-heal) cited
  `[Chapter~III, \S10]{GR17}` for the modular-family base-change —
  **WRONG section**. GR17 Chapter III is Gray-product and
  $(\infty,2)$-categories infrastructure; §10 exists (Gray tensor-
  coherence machinery), but the six-functor base-change citation that
  supports relative-Ran propagation lives in Part IV (correspondences)
  realised against Part V (IndCoh). Section drift matches AP285 pattern.

**Verdict (primary-source audit)**: the existing citation carries
AP285 section-drift. The abstract six-functor framework is correctly
located at GR17 Part IV + Part V; the specialisation to the Ran
prestack for factorization algebras on a FIXED smooth curve is proved
in Francis 2012 §2--3 (\cite{Francis2012}). The RELATIVE version over
a family $\mathcal{C}/S$ of smooth curves is NOT inscribed in GR17 and
NOT inscribed in Vol~I; it is the OF1-a inscription target.

## Phase 2. First-principles assessment

Question: is the relative-Ran six-functor base-change a mechanical
specialisation of GR17, or a genuine new theorem?

Three observations.

(i) GR17 Part IV proves six-functor base-change abstractly on
`Corr(PreStk)^{proper,all}_{ind-inf-sch,all}` (\cite[IV.5 Thm 1.2.2]{GR17}
for the relevant universal property). The statement is universal;
base-change along any proper morphism of ind-inf-schemes holds by fiat
against the IndCoh realisation.

(ii) The Ran prestack $\Ran(X)$ is not a scheme; it is a colimit-type
prestack over the category of finite sets with surjections. Its $\Shv^{\DR}$
category is presentable (GR17 I.3) and the Francis--Gaitsgory factorization
subcategory $\Fact(X) \hookrightarrow \Shv^{\DR}(\Ran(X))$ is stable
presentable symmetric monoidal under $\star$ (Francis 2012 §4;
`prop:fg-ambient-properties` in the chapter). So base-change passes
abstractly; the non-trivial step is that the factorization $\star$-
subcategory is PRESERVED by $f^!$ under the base-change diagram.

(iii) For a family $\pi: \mathcal{C} \to S$, the relative Ran prestack
$\Ran^{\rel}(\mathcal{C}/S) \to S$ is the fibre-wise Ran construction
over each $s \in S$; its total-space formulation uses the fibre product
$\Ran^{\rel}(\mathcal{C}/S) = \Ran(\mathcal{C}) \times_{\Ran(S)} S$ with
the diagonal $S \to \Ran(S)$. Base-change along $f: S' \to S$ gives a
pullback square; six-functor base-change on this square is an instance
of GR17 IV.5 Thm 1.2.2 applied to $f^!$ on $\Shv^{\DR}$, and the
factorization subcategory is preserved because $f^!$ is symmetric
monoidal against $\otimes^!$, which agrees with $\star$ on the
diagonal-supported locus (Francis 2012 Prop 4.1).

Conclusion: specialisation is NOT purely mechanical — the preservation
of the factorization subcategory under $f^!$ and the compatibility of
the relative $\star$-product with the base-change natural transformation
is the load-bearing step, not extracted verbatim from GR17 IV.5 Thm
1.2.2 alone. It is ALSO not a genuinely new theorem in the "independent
deep result" sense: it is a 1--3-page lemma combining GR17 IV.5 with
Francis 2012 §4 plus Beilinson--Drinfeld factorization nearby-cycles
discipline. This places the inscription in the middle regime:
`\ClaimStatusProvedElsewhere` alone is insufficient (the specialisation
is non-trivial); full `\ClaimStatusProvedHere` inscription requires the
1--3-page proof body to be written.

## Phase 3. Heal choice

Options per mission:

(A) `\ClaimStatusProvedHere` + inscribe `lem:gr17-base-change-on-relative-ran`.
    Requires a full proof body. Deferred: the programme has not yet
    committed to write this inscription; it is a genuine 1--3 pages of
    derived-prestack technology.

(B) `\ClaimStatusProvedElsewhere` + Remark[Attribution]. Insufficient:
    the specialisation is non-trivial; no single external source proves
    the relative-Ran statement verbatim.

(C) AP266 sharpened-obstruction: name the specific base-change class
    $[\alpha_{\mathrm{BC}}]$ whose vanishing completes the extension,
    state its cohomological residence, correct the GR17 section-drift,
    and leave the inscription as a named target.

Heal chosen: **(C) sharpened obstruction**. This is the honest response
when the external citation is nearly-but-not-quite specialisable and
the inscription work is genuinely open. It converts "cited but not
inscribed" into "named obstruction class with explicit $\mathrm{Ext}^1$
residence"; a future Vol~I commit either inscribes `lem:gr17-base-change-
on-relative-ran` (path A) or the obstruction class remains as the
precise programme-internal residue.

This is consistent with the Beilinson dictum: a smaller true theorem
(the obstruction class is explicit, its vanishing is the precise
missing inscription) replacing a larger false one (the CLAUDE.md status
row had previously advertised the base-change as a citation-settled
external black box under a mis-located GR17 section number).

## Phase 4. Edits applied

**E1 (GR17 section-drift correction, AP285).** At
`chapters/theory/theorem_A_infinity_2.tex:947-952`, replaced

```
\cite[Chapter~III, \S10]{GR17}
```

with

```
\cite[Part~IV (Categories of correspondences), and Part~V, \S1
(IndCoh)]{GR17}; the specialisation to factorization sheaves on the
Ran prestack for a fixed smooth curve is \cite[\S2--3]{Francis2012}
```

**E3 (sharpened-obstruction inscription).** Extended
`rem:A-infinity-2-modular-family-scope` at
`chapters/theory/theorem_A_infinity_2.tex:965-1013` with an
``\emph{Sharpened obstruction for (a) (relative-Ran base-change).}''
paragraph stating:

- the relative Ran prestack $\Ran^{\rel}(\mathcal{C}/S) \to S$ and
  its fibre-product presentation over a smooth family $\pi:
  \mathcal{C} \to S$;
- the base-change natural transformation
  $\alpha_{\mathrm{BC}}: f^{!} \pi^{\Ran}_* \Rightarrow
   \pi'^{\Ran}_* f'^{!}$ on $\Fact^{\rel}(\mathcal{C}/S)$;
- the obstruction class
  $[\alpha_{\mathrm{BC}}]
   \in \mathrm{Ext}^{1}_{\Shv^{\DR}(S')}
        (f^! \pi^{\Ran}_* \mathcal{F},\,
         \pi'^{\Ran}_* f'^! \mathcal{F})$
  measuring its failure on the factorization subcategory;
- the scope statement: universal vanishing on the (H1)+(H2)+(H3)
  subcategory relative over $\mathcal{M}_g$ clears the OF1-a open
  frontier and extends $\thmref{A-infinity-2}$ horizontally to the
  interior $\mathcal{M}_{g,n}$; boundary requires OF1-b
  ($[\beta_{\mathrm{nodal}}]$, sibling-agent target).

**V2-AP26 check.** Post-edit hook flagged ``Part~IV (Categories of
correspondences)'' and ``GR17 Part~IV--V''. These are EXTERNAL GR17
book-location references, the canonical BibTeX `\cite[...]{GR17}` arg
format and the corresponding prose. V2-AP26 targets IN-PROGRAMME
self-references to our own Vol~I parts (``see Part~IV of this volume''),
not third-party book section citations. No action.

**E2 (Mok25 note-field rewrite)**: deferred to sibling agent's scope.

**E4 (CLAUDE.md status-row refresh)**: noted; no CLAUDE.md edits per
this session's policy. The current Vol~I CLAUDE.md Theorem A row
already carries "CONDITIONAL on GR17 + Mok25"; the present heal does
not change the conditional tag, only sharpens the residue.

## Phase 5. Theorem A status delta

Pre-heal: modular-family extension CONDITIONAL on (a) GR17 Ch III §10
[drifted citation], (b) Mok25.

Post-heal (this Wave-12 first-ingredient pass): modular-family extension
CONDITIONAL on

- (a) $[\alpha_{\mathrm{BC}}] \in \mathrm{Ext}^{1}$ relative-Ran
  base-change class vanishing universally on (H1)+(H2)+(H3) over
  $\mathcal{M}_g$ (sharpened; cited framework GR17 Part IV + Part V +
  Francis 2012 §2--3 now correct);
- (b) $[\beta_{\mathrm{nodal}}]$ log-FM nodal gluing class (sibling
  agent inscription target).

No theorem rank change. No CLAUDE.md row rank change. Downstream
consumers (Theorem D clutching, universal $\mathrm{obs}_g = \kappa
\cdot \lambda_g$, Vol~II climax) inherit the unchanged conditional
status, with a more precise residue pointer.

## Phase 6. Cross-volume propagation (AP5)

Grep checks:

- Vol~I other occurrences of `Chapter~III, \S10]{GR17}`: zero (only
  the just-healed site).
- Vol~I other occurrences of `relative Ran` or `Ran^{\rel}`: only
  this site, preface stubs, and adversarial notes. No drift to
  propagate.
- Vol~II / Vol~III propagation: sibling inspection out of scope for
  this first-ingredient pass.

No reverse drift detected (AP271). Manuscript scope remark now
correctly states "relative version... is the load-bearing missing
inscription"; CLAUDE.md status row will benefit from a future
precision update pointing at $[\alpha_{\mathrm{BC}}]$ by name.

## Residual inscription targets

(OF1-a, this mission): inscribe `lem:gr17-base-change-on-relative-ran`
with 1--3-page proof body combining GR17 Part IV--V, Francis 2012 §4,
and Beilinson--Drinfeld factorization nearby-cycles; verify
$[\alpha_{\mathrm{BC}}]$ vanishes universally on (H1)+(H2)+(H3).

(OF1-b, sibling): `prop:log-fm-nodal-factorization-gluing`,
$[\beta_{\mathrm{nodal}}]$ vanishing.

Both targets stand; this mission converts OF1-a from drifted-citation
black box into named cohomological obstruction with corrected framework
citation.

## Verdict

OF1-a honestly sharpened. GR17 citation drift corrected (AP285
discharged). Obstruction class $[\alpha_{\mathrm{BC}}]$ named and
placed in its $\mathrm{Ext}^{1}_{\Shv^{\DR}(S')}$ residence. Heal (C)
is the correct Beilinson-discipline response: no overclaim, no silent
retreat, explicit residue.

AP blocks used: AP241 (advertised-but-not-inscribed discipline
applied), AP249 (base-change cited not inscribed — now sharpened),
AP266 (sharpened-obstruction inscribed), AP272 (unstated cross-lemma
via folklore citation — GR17 Part IV--V + Francis 2012 named
precisely), AP285 (section-number drift corrected), AP287
(cross-volume theorem existence without HZ-11 attribution — this
mission stays Vol~I-internal so HZ-11 does not fire).
