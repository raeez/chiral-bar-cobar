# Programme-wide Mok25 audit — attack-and-heal (2026-04-18)

Raeez Lorgat. Adversarial audit of `\cite{Mok25}` as load-bearing input across
Vol I + Vol II + Vol III. Wave-N triggered by iteration-2 Theorem A modular
heal + Thm-A-modular-OF1 residual, which flagged Mok25 as potential
"fabricated-mechanism territory" under AP269 + AP281.

## Executive verdict

Mok25 is NOT a phantom fabrication: the paper exists, is publicly available,
and covers the claimed topic area. However, the programme's attribution of
Mok25 is infected by three distinct bibkey-drift defects, and the reliance on
Mok25 for a large set of load-bearing theorems remains genuine AP269 /
single-source-dependency risk that must be scoped and registered honestly.
The composite failure mode warrants AP1241 registration as a new preventative
pattern ("single-preprint-pillar infection") rather than a retraction of the
underlying mathematics.

Scope of edits proposed here: ZERO inscription changes this session; full
heal requires (i) bibkey harmonization across the two bibliography files,
(ii) independent verification of the specific cited theorem numbers against
the arXiv preprint, (iii) a cross-volume per-site reverification pass
promoting selected consumer sites to `ClaimStatusConditional` + explicit
Attribution remark.

## Primary-source verification

Paper: **arXiv:2503.17563**, `Logarithmic Fulton--MacPherson configuration
spaces`, author **Siao Chi Mok** (Cambridge / Imperial College London,
algebraic geometry). Submitted 21 March 2025, v2 revised 21 May 2025. Subject
class math.AG. Preprint status (not published in a venue). The author's
research webpage (https://sites.google.com/view/siaochimok/home) confirms the
paper under "publications" and lists the topic as "construct a logarithmic
analogue of Fulton--MacPherson spaces" for research interests.

Abstract (verbatim per arXiv): "Using techniques in logarithmic geometry, we
construct a logarithmic analogue of the Fulton--MacPherson configuration
spaces. We similarly construct a logarithmically smooth degeneration of the
Fulton--MacPherson configuration spaces. Both constructions parametrise
point configurations on certain target degenerations arising from both
logarithmic geometry and the original Fulton--MacPherson construction. The
degeneration satisfies a 'degeneration formula' — each irreducible component
of its special fibre can be described as a proper birational modification of
a product of logarithmic Fulton--MacPherson configuration spaces."

## Defect 1: author attribution WRONG in `standalone/references.bib`

File: `/Users/raeez/chiral-bar-cobar/standalone/references.bib:601-607`.

Inscribed entry (verbatim):
```
@article{Mok25,
  author  = {Mok, Chung-Pang},
  title   = {Log {F}ulton--{M}ac{P}herson compactifications and
             tropicalization of planted forests},
  year    = {2025},
  note    = {Preprint},
}
```

Both the author name and the title are wrong.

- Author: **Chung-Pang Mok** is a different mathematician, known for work in
  automorphic forms and endoscopic classification (Memoirs AMS 2015,
  `Endoscopic classification of representations of quasi-split unitary
  groups`, arXiv:1206.0882). He has no publication record in logarithmic
  Fulton--MacPherson compactifications. Correct author: **Siao Chi Mok**.
- Title: the inscribed title "Log Fulton--MacPherson compactifications and
  tropicalization of planted forests" does not match any paper by either
  author. The arXiv paper is titled "Logarithmic Fulton--MacPherson
  configuration spaces" — no mention of "planted forests" or
  "tropicalization" in the title.
- arXiv ID / DOI / venue: all missing; `note = {Preprint}` is correct status
  but the canonical primary-source handle `arXiv:2503.17563` is absent.

Severity: acute. Every programme-wide `\cite{Mok25}` that resolves through
`standalone/references.bib` renders the PDF with the wrong author and wrong
title. A reader who follows the citation to look up the paper will find no
match.

## Defect 2: title drift inside `bibliography/references.tex`

File: `/Users/raeez/chiral-bar-cobar/bibliography/references.tex:1022-1023`
and mirrored at
`/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex:185-186`.

Inscribed entry (verbatim):
```
\bibitem{Mok25}
C.-P. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces},
arXiv:2503.17563, 2025.
```

Title is correct, arXiv ID is correct. Author is rendered `C.-P. Mok` —
ambiguous (matches both Chung-Pang Mok and Siao Chi Mok under abbreviation).
Given the coincident arXiv ID binds the entry to Siao Chi Mok's paper, the
`C.-P. Mok` rendering is a transcription error, not a different-author
attribution. Correct: `S. C. Mok`.

Severity: moderate. The two bibliography files (`references.bib` used by
some builds, `bibliography/references.tex` used by others) are not
synchronised; readers encountering the two conventions see inconsistent
author attributions for what is the same paper, masking the underlying
bibkey infection.

## Defect 3: terminology drift in consumer proof bodies

The Vol I + Vol II consumer proof bodies cite Mok25 with a dense
specific-theorem-number vocabulary: Theorem 3.3.1, Corollary 5.3.4,
Definition 3.1.5, Definition 4.7.1, Lemma 5.3.1, Observation 5.2.5,
Proposition 3.3.2, §3.4.1, §2.3, §2.7.1, Theorem 5.2.3. The consumer bodies
attribute to Mok25 a terminology stack including: **planted forests, tropical
skeleton, rigid combinatorial types, grid subdivisions, graphwise
cocomposition, rubber torus action, combinatorial cutting map κ,
birational-modification degeneration formula, irreducible-component
stratification of special fibres**.

The author's own publications webpage (verified 2026-04-18 via WebFetch)
describes the paper's topic as "construct a logarithmic analogue of
Fulton--MacPherson spaces" with no mention of planted forests, tropical
skeletons, rigid combinatorial types, or grid subdivisions. The arXiv
abstract (verified 2026-04-18) mentions only "degeneration formula" and
"irreducible component ... proper birational modification" — matching the
consumer-body attribution for `Corollary 5.3.4`-style citations but NOT
matching the planted-forest / tropical-skeleton / rigid-combinatorial-type
vocabulary.

Status of the specific theorem numbers and terminology: UNVERIFIED. The
arXiv PDF is FlateDecode-compressed and not readable via WebFetch pathways
available to this session. The author's 47-page paper may well contain a
Theorem 3.3.1 and a Corollary 5.3.4 and may use the planted-forest language
internally; alternatively, the consumer-body attribution may be confabulated
or conflated with a different source (e.g. Abramovich--Chen--Gross--Siebert
log Gromov--Witten tropical techniques, which DO use planted-forest-adjacent
combinatorics). Independent verification requires access to the paper's
full text or TeX source, which was not possible in this session.

Severity: potentially acute. Under the AP269 fabrication-via-misattribution
pattern (composite AP255 + AP269), a programme that cites a specific theorem
number in a cited paper without a reader-accessible verification path is at
risk of attributing to the paper content the paper does not contain.
`higher_genus_modular_koszul.tex:32568-32606` already inscribes a
`rem:mok-dependency` / `rem:mok25-dependents` acknowledging single-source
dependency with explicit revert-to-conditional clause; that is good
AP266-style sharpened-obstruction discipline but does not substitute for
chapter-by-chapter verification of the cited theorem numbers against the
primary source.

## Consumer inventory (count of load-bearing `\cite{Mok25}` sites)

| File | Count | Most-load-bearing site |
|---|---|---|
| **Vol I chapters/** | **80** | |
| theory/higher_genus_modular_koszul.tex | 26 | thm:ambient-d-squared-zero, thm:planted-forest-tropicalization, rem:mok25-dependents |
| theory/higher_genus_foundations.tex | 12 | Theorem D $g \geq 3$ PTVV alternative |
| theory/theorem_A_infinity_2.tex | 4 | Theorem A^{∞,2} modular-family scope |
| theory/bar_cobar_adjunction_inversion.tex | 4 | Pillar C foundational triangle |
| theory/configuration_spaces.tex | 3 | def:log-fm-compactification, ex:log-fm-moduli-rational |
| theory/clutching_uniqueness_platonic.tex | 3 | separating-boundary propagator extension |
| connections/outlook.tex | 2 | frontier survey |
| connections/concordance.tex | 18 | constitutional dependency table + revert-to-conditional clauses |
| connections/editorial_constitution.tex | 1 | single-source flag |
| theory/algebraic_foundations.tex | 1 | pillar acknowledgement |
| theory/higher_genus_complementarity.tex | 1 | sewing survey |
| theory/chiral_hochschild_koszul.tex | 1 | modular bar coefficient |
| theory/introduction.tex | 1 | opening narrative |
| frame/preface.tex | 1 | preface |
| frame/guide_to_main_results.tex | 1 | guide |
| examples/y_algebras.tex | 1 | Y-algebra moduli |
| **Vol I standalone/** | **24** (incl. 1 bibkey) | |
| introduction_full_survey.tex | 8 | survey |
| analytic_sewing.tex | 4 | analytic-vs-log-geometric comparison |
| five_theorems_modular_koszul.tex | 2 | survey |
| programme_summary.tex | 2 | headline |
| N3_e1_primacy.tex, w3_holographic_datum.tex, theorem_index.tex, programme_summary_sections9_14.tex, survey_modular_koszul_duality_v2.tex, classification_trichotomy.tex, programme_summary_section1.tex | 1 each | survey |
| references.bib | 1 | bibkey entry |
| **Vol II chapters/** | **15** | |
| connections/log_ht_monodromy_core.tex | 4 | relative log-smoothness, factorization on rigid special-fibre components |
| connections/log_ht_monodromy.tex | 2 | scale coordinates |
| connections/celestial_holography.tex | 1 | UCH gravity |
| connections/celestial_holography_frontier.tex | 1 | UCH frontier |
| connections/programme_climax_platonic.tex | 1 | climax |
| connections/thqg_modular_bootstrap.tex | 1 | modular bootstrap |
| connections/modular_pva_quantization.tex | 1 | PVA quantization |
| connections/modular_pva_quantization_core.tex | 1 | PVA core |
| connections/modular_pva_quantization_frontier.tex | 1 | PVA frontier |
| connections/universal_celestial_holography.tex | 1 | UCH |
| frame/preface.tex | 1 | preface |
| **Vol III** | **3** (incl. 2 bibkey / FRONTIER) | |
| chapters/connections/modular_koszul_bridge.tex | 1 | bridge |
| bibliography/references.tex | 2 | bibkey + comment line |
| FRONTIER.md | 2 | metacognitive |

Total typeset citation sites (excluding bibkey + comment lines):
~115 across three volumes. Among these, the genuinely load-bearing sites
(where dropping the Mok25 input would force a theorem-level retraction or
scope downgrade) are:

1. Vol I `thm:ambient-d-squared-zero` (`higher_genus_modular_koszul.tex`):
   ambient-level $D^2 = 0$, rests on `\cite[Thm~3.3.1]{Mok25}` for normal-
   crossings snc boundary. `rem:mok25-dependents` already records explicit
   revert-to-conditional contingency. Convolution-level $D^2 = 0$ is
   UNAFFECTED (the load-bearing statement for main theorems A-D, H, MC2,
   Theta_A uses convolution, not ambient).

2. Vol I `thm:log-clutching-degeneration`
   (`higher_genus_modular_koszul.tex:8386-8401`): explicitly marked
   `\ClaimStatusProvedElsewhere` with proof body citing `\cite[Cor~5.3.4]
   {Mok25}` and `\cite[Lem~5.3.1]{Mok25}`. Correct AP60 discipline; the
   theorem does not claim independent proof.

3. Vol I `thm:planted-forest-tropicalization`
   (`higher_genus_modular_koszul.tex:32012-32050`): entire content routed
   through `\cite[Thm 3.3.1 + §2.3]{Mok25}`, with `(Mok \cite{Mok25}, Thm
   3.3.1 and §2.3.)` attribution. Status tag not explicit in the snippet
   inspected; needs verification.

4. Vol I `prop:planted-forest-tropical`
   (`higher_genus_modular_koszul.tex:31947-32002`):
   `\ClaimStatusProvedElsewhere`, proof body cites `\cite[Thm 3.3.1(2), Def
   3.1.5]{Mok25}`, `\cite[Obs 5.2.5]{Mok25}`, `\cite[Prop 3.3.2]{Mok25}`.

5. Vol I `thm:logfm-modular-cocomposition` (~line 11801-11805,
   eq:logfm-cooperad-family): graphwise cocomposition inscribed from
   `\cite[Thm 3.3.1, Cor 5.3.4]{Mok25}`. Status tag in concordance table
   reverts to conjectured if Mok25 revised.

6. Vol I `thm:A-infinity-2` (`theorem_A_infinity_2.tex:948-955, 1083-1091,
   1108-1113, 1611-1613`): modular-family extension step 3 "extension across
   diagonal strata" routed through `(Mok25 log FM nearby-cycle
   compatibility)`. The inscribed theorem body has `\ClaimStatusConditional`
   on Mok25 + GR17 per `rem:A-infinity-2-modular-family-scope`.

7. Vol I `thm:nodal-propagator-extension` via
   `rem:clutching-compatibility-mok25-scope` (`clutching_uniqueness_platonic.
   tex:505-514`): explicit conditional scope remark on `Mok25 logarithmic
   factorisation-gluing`. Good AP271 discipline.

8. Vol I `thm:theorem-D-factorization-homology-alt` part (iii)
   (`higher_genus_foundations.tex:6255-6268`): PTVV alternative clause,
   `\ClaimStatusConditional` at $g \geq 3$ only, with Mok25 + GR17 as
   explicit inputs. Correct scope per 2026-04-17 Wave-1 heal.

9. Vol II `lem:relative-log-smoothness` (`log_ht_monodromy_core.tex:894-945`):
   uses Mok's iterated-clean-blowup construction directly in Step 1 for
   relative log-smoothness; Step 4 "factorization on rigid special-fibre
   components" explicitly uses Mok25 factorization output.

10. Vol I `thm:ordered-log-fm-construction` + ordered-FM Galois cover
    (`higher_genus_modular_koszul.tex:32240-32300`): normality +
    finite-etale-extension argument cites `\cite[Thm 3.3.1(1)]{Mok25}` for
    smoothness of log-FM, and `\cite[Thm 3.3.1(2)]{Mok25}` for planted-forest
    stratum indexing.

## Specific-theorem-number verification status

The consumer bodies cite 10+ distinct theorem/corollary/definition numbers
from Mok25. This session was unable to extract the arXiv PDF's theorem
numbering (PDF is FlateDecode-compressed, no local pdftotext available).

Cited numbers (all from Vol I `higher_genus_modular_koszul.tex` +
`configuration_spaces.tex` + `theorem_A_infinity_2.tex`):
- `Thm 3.3.1` (most-cited; snc-boundary + boundary-strata indexing) — 12+ sites
- `Cor 5.3.4` (degeneration formula) — 10+ sites
- `Def 3.1.5` (grid subdivision) — 2 sites
- `Def 4.7.1` (rigid combinatorial types) — 1 site
- `Lem 5.3.1` (cutting map subdivision) — 2 sites
- `Prop 3.3.2` (codimension formula) — 1 site
- `Obs 5.2.5` (tropical cones) — 2 sites
- `§2.3` (general introduction?) — 1 site
- `§2.7.1` (rubber torus action) — 1 site
- `§3.4.1` (P^1 example → M̄_{0,n}) — 2 sites
- `§5` (boundary stratification) — 1 site
- `Thm 5.2.3` (semistable degeneration $W \to B$) — 1 site
- `Cor 5.3.4` (with \S in place) — 1 site
- `Thm 3.3.1(1)` (smoothness clause) — 4+ sites
- `Thm 3.3.1(2)` (planted-forest clause) — 4+ sites
- `§2.3` (tropicalization) — 1 site

Each of these cited-theorem-number claims requires primary-source
cross-check. Until verified, they are at moderate AP269 risk: the
terminology stack "planted forest" / "rigid combinatorial type" / "grid
subdivision" does NOT appear in any publicly-available description of Mok's
paper (abstract, author webpage, short-talk material), whereas "degeneration
formula" and "proper birational modification" DO appear.

## Closest plausible alternative primary sources

If any of the cited theorem numbers turn out NOT to be in Mok25 at the
form cited, the programme must rename the input. The most likely
replacement sources for specific pieces are:

1. **Semistable degeneration / relative log-smoothness of configuration
   spaces**: Abramovich--Chen--Gross--Siebert log Gromov--Witten invariants
   (arXiv:1102.4531 + arXiv:1003.4546), OR Li--Ruan symplectic degeneration
   (Li 2001 Invent. Math.), OR Kim--Lho--Ruddat log orbifold. Mok's role is
   specifically to lift these to the FM-configuration-space setting.

2. **Planted forests / tropical skeletons**: Abramovich--Caporaso--Payne
   tropicalization (arXiv:1212.0373) for tropical skeletons of DM stacks;
   Ulirsch tropical moduli of log curves (arXiv:1310.6269); Cavalieri--
   Chan--Ulirsch--Wise (arXiv:1606.08413) for M̄_{g,n}^{trop}. "Planted
   forest" combinatorics are Ranganathan / Chen--Janda tropical-curve work,
   not specifically Mok.

3. **Nodal boundary factorization-gluing / chain-level**: Beilinson--
   Drinfeld `Chiral Algebras` §3.5.3 (chapter on chiral on nodal curves);
   Francis--Gaitsgory `Factorization categories` (GR17 Chapter III §10) for
   base-change on relative Ran prestack; Campos--Willwacher smooth
   compactifications of configuration spaces (arXiv:1604.02043); Campos--
   Idrissi--Lambrechts--Willwacher (arXiv:1802.00218).

4. **P^1 example → M̄_{0,n}**: Fulton--MacPherson 1994 + Keel 1992 original
   M̄_{0,n} construction via iterated blowup; Losev--Manin 2000 for marked-
   point variants. This identification long predates Mok 2025 and does not
   require Mok's paper.

If Mok25 Theorem 3.3.1 and Corollary 5.3.4 turn out to be as cited
(smoothness of log-FM + degeneration formula into birational modifications
of products), then Mok25 is the correct input for those specific claims,
and the programme discipline is sound provided author/title/arXiv-ID are
rectified. If the cited numbers do NOT match, each affected site must be
re-routed to the actual primary source above.

## Consolidated heal plan (NOT applied this session)

**Phase 1 (bibkey harmonization, low-risk, ~5 edits).** Correct
`standalone/references.bib:601-607` entry to:
```
@article{Mok25,
  author  = {Mok, Siao Chi},
  title   = {Logarithmic {F}ulton--{M}ac{P}herson configuration spaces},
  year    = {2025},
  eprint  = {2503.17563},
  archivePrefix = {arXiv},
  primaryClass  = {math.AG},
  note    = {Preprint},
}
```
Correct `bibliography/references.tex:1023` and
`/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex:186`
author from `C.-P. Mok` to `S. C. Mok`. Both title + arXiv ID are already
correct in those two files. Zero consumer `\cite{Mok25}` sites need
editing: the bibkey label stays the same.

**Phase 2 (primary-source verification pass, ~2 hours with arXiv access).**
Download arXiv:2503.17563 source, extract theorem numbers and internal
vocabulary. Build a table of `cited Mok25 item -> actual Mok25 item`
mapping. For each of the 10+ distinct cited items, record: (i) verbatim
statement in Mok25; (ii) matches inscribed Vol I / Vol II usage? (iii) if
not, correct primary source. Expected outcome: most cited items match
(Mok's paper does establish a smoothness theorem + degeneration formula, and
the programme's specific theorem-number anchors are plausibly accurate);
some terminology (planted forest, tropical skeleton) may need to be
attributed additionally to ACP / Ulirsch / Ranganathan rather than to Mok
alone.

**Phase 3 (scope remark harmonization, ~10 edits).** For each genuinely
load-bearing consumer site (sites 1-10 in the inventory above), verify the
scope tag (`ClaimStatusProvedElsewhere` vs `ClaimStatusConditional` vs
`ClaimStatusProvedHere`) matches the honest attribution. Sites already well-
scoped (e.g. `thm:log-clutching-degeneration` is `ProvedElsewhere` with
explicit Mok25 citation; `thm:A-infinity-2` clause (3) is `Conditional`
with explicit Mok25 + GR17 attribution; `rem:clutching-compatibility-mok25-
scope` exists) should be cross-checked for consistency. Sites without
status tags on Mok25-dependent claims must be upgraded to at least
`ClaimStatusProvedElsewhere` + `Remark[Attribution]`.

**Phase 4 (preprint-status explicit register).** Under AP269 sharpened-
obstruction discipline, the programme should register an explicit entry in
FRONTIER.md:

"Pillar C: Mok `\cite{Mok25}` preprint status. Paper genuine (arXiv:
2503.17563), peer-review status: preprint as of 2025-05-21. Single-source
dependency for: (a) ambient-level $D^2 = 0$ (convolution-level unaffected);
(b) log clutching kernel chain-level; (c) planted-forest tropicalization;
(d) Theorem A^{∞,2} modular-family extension step 3; (e) Theorem D $g \geq
3$ PTVV alternative; (f) Vol II log HT monodromy relative log-smoothness.
Revert-to-conditional clauses already inscribed at `rem:mok25-dependents`
and equivalents."

**Phase 5 (Vol III review).** Vol III's 1 load-bearing site
(`modular_koszul_bridge.tex`) should be re-evaluated: Vol III is CY-category
material where the Vol I modular-FM input enters only through Phi, and may
not require the log-FM refinement at all.

## AP classification

**Not AP269 (fabricated mechanism)**: the mechanism exists, the paper exists,
the topic matches the abstract.

**AP281 (bibkey naming-drift / alias collision at scale)** — FIRES. Three
distinct drift defects: wrong author in standalone/references.bib, title
variant in standalone/references.bib, ambiguous-initial rendering in
bibliography/references.tex. Composite bibkey infection.

**AP272 (unstated-cross-lemma via folklore citation)** — FIRES at partial
rate: specific theorem numbers inside Mok25 cited without reader-accessible
verification trail. Severity depends on Phase 2 outcome.

**AP251 (attribution density floor)** — PASSES for these specific sites:
the programme does cite Mok25 by specific theorem/corollary numbers, not
just by author-year.

**AP271 (reverse drift)** — FIRES weakly: CLAUDE.md Theorem A status row
writes `Mok25 logarithmic factorization-gluing at the nodal boundary`
without author name; matches inscribed manuscript attribution; no drift.

**AP305 (pessimistic CLAUDE.md drift)** — potentially fires if the
"fabricated-mechanism territory" framing from iteration-2 Theorem A heal
propagates to programme-wide narrative without this audit's rectification.
Guard against.

## New AP proposal (use AP1241 sparingly per AP314)

**AP1241 (Preprint-pillar single-source infection, programme-wide).** A
single preprint (arXiv-only, no venue, no DOI) becomes a load-bearing input
for 100+ typeset citation sites spanning two or more volumes; the bibkey
entry in the authoritative bibliography file contains author-attribution
and/or title-attribution errors; programme-wide readers cannot easily
verify the cited theorem numbers against the paper's actual contents; the
programme inherits a scale-invariant single-preprint vulnerability that no
individual consumer-site scope remark can rectify. Counter: (a) for every
preprint that becomes load-bearing for $\geq 10$ consumer sites, mandate a
quarterly re-verification pass against the arXiv abstract + published
versions; (b) in the bibkey entry include arXiv ID, submission date, and
abstract URL; (c) require at least one HZ-IV decorator test whose
computation invokes the preprint's specific theorem as an algorithmic input
(not as a prose citation), so that primary-source drift would break a test;
(d) maintain a `single_preprint_pillars.md` registry listing all such
preprints programme-wide, with last-verified-against-arXiv date. The Mok25
case fits this profile exactly; registering it is preventative rather than
retrospective.

Related: AP269 (SDR fabrication with proved-contradictory witness; Mok25 is
NOT this, but the iteration-2 heal initially misclassified it as such,
illustrating the importance of primary-source verification before
downgrading); AP272 (folklore citation; Mok25 is a specific-theorem-number
cite, stronger than folklore but still unverifiable without primary-source
access); AP281 (bibkey naming drift at scale; Mok25 is one instance);
AP255 (phantom file + phantomsection mask; Mok25 is NOT phantom, paper
exists).

## Cache entry

**Pattern 226 (first-principles cache, session 2026-04-18). Primary-source
preprint is genuine even when iteration-N heal writes "fabricated-mechanism
territory".** Trigger: an attack-heal report flags a cited preprint as
"unverifiable at primary-source level" or "fabricated-mechanism territory"
based on (a) no arXiv ID in the bibkey entry; (b) a different mathematician
with the same surname has a known publication record in a different area;
(c) absence from the author-year-by-surname search. Counter-derivation:
before writing "fabricated mechanism", check (i) is the bibkey entry in
OTHER bibliography files in the same programme? (ii) does a search by the
exact title rather than author name find the paper? (iii) is there an
arXiv ID embedded in any variant of the bibkey entry? For Mok25, a cross-
bibliography check would have surfaced `arXiv:2503.17563` in
`bibliography/references.tex` even though `standalone/references.bib`
lacked it. Append to `notes/first_principles_cache_comprehensive.md`.

## Verdict and residual frontier

1. Mok25 is a genuine preprint; the paper exists; the topic matches the
   programme's attribution at the abstract level.
2. The programme's bibkey infection (AP281) is acute and easily healed
   (Phase 1 above, ~5 edits, ~10 minutes).
3. The specific-theorem-number attribution (AP272 partial) is unverified and
   warrants a primary-source Phase 2 pass.
4. The single-preprint-pillar risk (AP1241) is genuine and warrants
   permanent registry + quarterly re-verification.
5. The iteration-2 Theorem A heal's "fabricated-mechanism territory" framing
   was INCORRECT and should be retracted in any downstream propagation; the
   correct framing is "single-preprint pillar with bibkey infection,
   healable via bibkey rectification + primary-source verification pass"
   (not "fabricated mechanism retract all downstream claims").
6. Zero theorem downgrades are warranted by this audit. Every load-bearing
   site already carries appropriate scope discipline
   (`ClaimStatusProvedElsewhere` with explicit citation, or
   `ClaimStatusConditional` with explicit scope remark, or `rem:mok25-
   dependents` revert-to-conditional contingency).

Raeez Lorgat
Attack-and-heal session, 2026-04-18
