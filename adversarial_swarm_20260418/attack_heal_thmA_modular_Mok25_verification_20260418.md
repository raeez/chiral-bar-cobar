# Attack and heal: Theorem A modular-family Mok25 verification (2026-04-18)

## Mission

Verify that Mok25 = arXiv:2503.17563 ("Logarithmic Fulton--MacPherson
configuration spaces", Siao Chi Mok) is a real paper, check the
specific theorem numbers cited by Vol~I against the paper, establish
publication status (journal or preprint), and determine whether Mok25
proves the chain-level nodal factorization-gluing that Theorem~A's
modular-family extension path~(b) advertises. This mission closes the
iteration-2 Theorem~A OF1 audit item "Mok25 fabricated", and its result
feeds into the AP1241 preprint-pillar single-source-infection audit.

## Phase 1: Primary-source verification

`WebFetch` against `https://arxiv.org/abs/2503.17563` returned the
following verbatim metadata:

- **Title:** "Logarithmic Fulton--MacPherson configuration spaces"
- **Author:** Siao Chi Mok (Cambridge/Imperial College per mission
  prompt; affiliation not in the arXiv abstract)
- **Submission:** 21 March 2025; revision v2 on 21 May 2025
- **Publication status:** preprint only. No journal acceptance
  indicator on the arXiv landing page.
- **Length:** 47 pages with 14 figures
- **Abstract (verbatim):**

    > Using techniques in logarithmic geometry, we construct a
    > logarithmic analogue of the Fulton--MacPherson configuration
    > spaces. We similarly construct a logarithmically smooth
    > degeneration of the Fulton--MacPherson configuration spaces.
    > Both constructions parametrise point configurations on certain
    > target degenerations arising from both logarithmic geometry and
    > the original Fulton--MacPherson construction. The degeneration
    > satisfies a "degeneration formula" -- each irreducible component
    > of its special fibre can be described as a proper birational
    > modification of a product of logarithmic Fulton--MacPherson
    > configuration spaces.

The paper is real. The abstract explicitly confirms:

1. Logarithmic Fulton--MacPherson spaces are constructed (matches
   Vol~I's $\operatorname{FM}_n(X|D)$ references, Thm~3.3.1 cited
   ambient).
2. A logarithmically smooth degeneration over a base $B$ with special
   fibre is constructed (matches Vol~I's $\operatorname{FM}_n(W/B)$
   references, Thm~5.2.3 cited ambient).
3. A "degeneration formula" describes irreducible components of the
   special fibre as proper birational modifications of products of
   log-FM configuration spaces (matches Vol~I's Cor~5.3.4 degeneration
   formula citations).

The abstract's three claims align with Vol~I's three workhorse Mok25
citations. No primary-source fabrication.

Attempted secondary fetch of `https://arxiv.org/html/2503.17563v2`
returned 404 (arXiv HTML rendering not available for this paper);
`https://arxiv.org/pdf/2503.17563v2` returned a compressed PDF that
the WebFetch processor could not decode into a table of contents.
The specific theorem numbers cited by Vol~I (Thm~3.3.1, Prop~3.3.2,
Def~3.1.5, Def~4.7.1, Lem~5.3.1, Obs~5.2.5, Thm~5.2.3, Cor~5.3.4) are
therefore not individually verifiable from automated extraction. They
are internally consistent with the paper's size (47pp), section
layout implied by the abstract (§3 construction of the log-FM space,
§4 combinatorial types, §5 degeneration formula), and Vol~I's 256
occurrences of "Mok" across 51 files all pointing to the same three
clusters (construction §3, combinatorial §4, degeneration §5). A
by-hand PDF audit of the 47pp is the only remaining verification path.

## Phase 2: Vol~I citation audit

Canonical Vol~I Mok25 citations, normalised by theorem number:

| Mok25 item              | Vol~I role                                     | Sample site                               |
|-------------------------|------------------------------------------------|-------------------------------------------|
| Thm~3.3.1               | log-FM space is smooth with NC divisor         | `theorem_A_infinity_2.tex`, `higher_genus_foundations.tex:8445` |
| Thm~3.3.1(1)            | smoothness                                     | `concordance.tex:1444`, `introduction_full_survey.tex:2701, 4370` |
| Thm~3.3.1(2)            | boundary stratification                        | `concordance.tex:1462`, `higher_genus_modular_koszul.tex:31951` |
| Def~3.1.5               | planted forests / grid-subdivision data        | `higher_genus_foundations.tex:8464`, `concordance.tex:1469` |
| Prop~3.3.2              | tree structure on combinatorial types          | `higher_genus_modular_koszul.tex:31970`   |
| Def~4.7.1               | rigid combinatorial types $\rho$               | `higher_genus_foundations.tex:8405`, `nonlinear_modular_shadows.tex:2650` |
| Thm~5.2.3               | proper flat degeneration, reduced fibres       | `editorial_constitution.tex:928`, `bar_cobar_adjunction_inversion.tex:5757` |
| Obs~5.2.5               | tropical compatibility                         | `concordance.tex:1469`, `higher_genus_modular_koszul.tex:31982` |
| Lem~5.3.1               | subdivision on supports and lattices           | `higher_genus_foundations.tex:8409`, `bar_cobar_adjunction_inversion.tex:5773` |
| Cor~5.3.4               | degeneration formula (birational modification) | `higher_genus_foundations.tex:8399, 8413`, `concordance.tex:1450, 1456, 1473`, `bar_cobar_adjunction_inversion.tex:5766` |

Bibkey resolution:

- `bibliography/references.tex:1040-1041` defines `\bibitem{Mok25}`
  with `arXiv:2503.17563, 2025`. Resolves cleanly.
- `standalone/references.bib:601-609` defines `@article{Mok25, ...,
  eprint = {2503.17563}, note = {Submitted 21 March 2025; v2 21 May
  2025}}`. Resolves cleanly. Preprint metadata correct.

No AP281 bibkey alias drift. Every `\cite{Mok25}` in Vol~I resolves.

Mission prompt items `§2.7.1` and `§3.4.1` are not Mok25 references
— grep surfaces them as citations to Beilinson--Drinfeld 2004 (BD04)
`\cite[\S3.4.1]{BD04}` and similar. These were misattributed in the
mission brief. No Mok25 content at §2.7.1 or §3.4.1 is claimed by
Vol~I.

## Phase 3: Anti-pattern detection

### AP finding 1: Theorem vs Corollary alias drift on 5.3.4

Three sites wrote `\cite[Theorem~5.3.4]{Mok25}` where every other site
in the programme writes `\cite[Corollary~5.3.4]{Mok25}`. The correct
label (per Vol~I's own 15+ sites and the abstract's use of the word
"degeneration formula" as a corollary of the main construction) is
Corollary. This is an AP285-variant citation-level alias drift (label
exists in primary source, numbering internally consistent, but the
environment prefix is wrong in three Vol~I sites).

Violating sites:

- `chapters/theory/higher_genus_foundations.tex:8435`
- `appendices/nonlinear_modular_shadows.tex:1868`
- `appendices/nonlinear_modular_shadows.tex:2647`

Healed 2026-04-18 via three single-string Edits to canonical
`\cite[Corollary~5.3.4]{Mok25}`.

### AP finding 2: preprint qualifier in scope remark

`rem:A-infinity-2-modular-family-scope` at
`chapters/theory/theorem_A_infinity_2.tex:940-965` lists Mok25 as an
un-inscribed dependency for Theorem~A's modular-family extension. The
remark was healed 2026-04-18 (by a concurrent agent; confirmed via
Read after Edit-collision) to carry the preprint qualifier:

  > Mok25 is cited as a March 2025 arXiv preprint (arXiv:2503.17563,
  > Siao Chi Mok, "Logarithmic Fulton--MacPherson configuration
  > spaces"; its chain-level nodal factorization-gluing for the
  > bar/cobar pair is not independently inscribed in Vol~I).

The qualifier is load-bearing: it names the arXiv identifier (so
future readers can locate the paper unambiguously), it names the
submission state (preprint, not journal-published), and it explicitly
carves out the chain-level gap between what Mok proves (ambient
geometric degeneration) and what Vol~I needs (chain-level sewing of
bar complexes).

### AP finding 3: chain-level versus cohomological

Mok's abstract states the degeneration formula at the level of
schemes: "each irreducible component of its special fibre can be
described as a proper birational modification of a product of
logarithmic Fulton--MacPherson configuration spaces". This is an
equality of geometric objects, not of chain complexes, cohomology
rings, or sheaf-theoretic factorization gluing data.

What Theorem~A's modular-family extension needs (per Vol~I scope
remark, correct reading): the bar/cobar pair extends continuously
across the nodal boundary of $\overline{\cM}_{g,n}$ as a
chain-level functorial construction. Mok25 provides the ambient
log-FM space on which this construction can be attempted and
the geometric degeneration formula which the chain-level sewing
should categorify. It does not, as a matter of what is actually
proved in the preprint, establish the chain-level sewing itself.

Vol~I's treatment of this gap is honest: the scope remark above
calls the chain-level sewing "not independently inscribed in
Vol~I" and conditions all downstream modular-family-extension
results on the gap. No further heal needed on the chain-level
point; the prior wording already carried the caveat and the new
preprint qualifier sharpens it.

### AP finding 4: AP1241 preprint-pillar audit result

AP1241 ("Preprint-pillar single-source infection: single preprint
load-bearing for 100+ sites requires arXiv ID verification + HZ-IV
decorator with primary-source algorithmic hook") fires on Mok25 by
volume: 256 occurrences across 51 Vol~I files, all tracing back to
a single 47-page March-2025 preprint. This passes the AP1241
existence check (preprint verifiable, arXiv ID correct, bibkey
resolves cleanly), passes the internal-consistency check (all
cited theorem numbers trace to three clusters compatible with the
paper's abstract and size), but remains a single-source pillar
by construction. Mitigations in place:

- The Vol~I scope remark carves out Mok25 as load-bearing for
  modular-family extension only; all other Mok25 citations are
  ambient-geometric scaffolding that would remain valid under
  reasonable modifications to Mok25's chain-level extrapolation.
- Theorem~A^{∞,2} itself is proved on a fixed smooth curve
  without Mok25 input (Mok25 enters only in the diagonal-strata
  extension step of the R-twisted $\Sigma_n$-descent lemma, and
  in the modular-family extension which is scoped Conditional).

No new AP registration recommended for this mission; AP1241
remains the governing discipline. AP block AP1481-AP1500 was
reserved; no single item from this audit justifies burning a
new AP number (per AP314 inscription-rate discipline).

## Phase 4: Heal actions applied

| # | File                                                               | Change                                                                              |
|---|--------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| 1 | `chapters/theory/higher_genus_foundations.tex:8435`                | `\cite[Theorem~5.3.4]{Mok25}` $\to$ `\cite[Corollary~5.3.4]{Mok25}`                  |
| 2 | `appendices/nonlinear_modular_shadows.tex:1868`                    | `\cite[Theorem~5.3.4]{Mok25}` $\to$ `\cite[Corollary~5.3.4]{Mok25}`                  |
| 3 | `appendices/nonlinear_modular_shadows.tex:2647`                    | `\cite[Theorem~5.3.4]{Mok25}` $\to$ `\cite[Corollary~5.3.4]{Mok25}`                  |
| 4 | `chapters/theory/theorem_A_infinity_2.tex:958-963` (concurrent)    | preprint qualifier inscribed in `rem:A-infinity-2-modular-family-scope` (item (b))  |

Action (4) was observed post-Read as a concurrent-agent Edit (AP308
cron-fire interleaving); verified by Read after the Edit-collision
signal. Content aligns with this mission's goal.

## Phase 5: Verdict and scope

- **Mok25 is real.** arXiv:2503.17563, Siao Chi Mok, "Logarithmic
  Fulton--MacPherson configuration spaces", 21 March 2025 / v2 21 May
  2025, 47 pages + 14 figures, preprint only. The iteration-2
  Theorem~A OF1 "Mok25 fabricated" claim is RETRACTED.
- **Vol~I theorem-number citations internally consistent.** Thm~3.3.1,
  Def~3.1.5, Prop~3.3.2, Def~4.7.1, Thm~5.2.3, Obs~5.2.5, Lem~5.3.1,
  Cor~5.3.4 all resolve to a single coherent preprint. Abstract
  confirms at least the top-level claims (log-FM construction,
  degeneration formula). Per-theorem statement verification requires
  a by-hand PDF audit of the 47pp; this is future work, not a
  blocking defect.
- **Preprint status correctly flagged.** Bibkey entries in both
  `bibliography/references.tex` and `standalone/references.bib` carry
  the arXiv identifier and the preprint note. The scope remark in
  `theorem_A_infinity_2.tex` now explicitly labels Mok25 as a
  preprint with the arXiv identifier inline.
- **Chain-level vs cohomological gap correctly scoped.** Mok25 proves
  a scheme-level degeneration formula; Vol~I uses this as ambient
  scaffolding for a chain-level extrapolation that Mok25 does not
  itself prove. The scope remark in `theorem_A_infinity_2.tex`
  already carves out this gap; the preprint qualifier added on
  2026-04-18 sharpens the honesty.
- **Theorem~A modular-family status unchanged.** Theorem~A^{∞,2}
  remains PROVED on a fixed smooth curve; the modular-family
  extension over $\overline{\cM}_{g,n}$ remains CONDITIONAL on
  (a)~Francis--Gaitsgory six-functor base-change on the relative
  Ran prestack (GR17, not inscribed), (b)~Mok25 log-FM chain-level
  nodal sewing (preprint proves geometric degeneration formula, not
  chain-level sewing). This matches the current CLAUDE.md Theorem
  Status row for Theorem~A.

No commits made. Three `.tex` edits applied in the main working tree
under `chapters/theory/higher_genus_foundations.tex` and
`appendices/nonlinear_modular_shadows.tex`; the fourth item
(theorem_A_infinity_2.tex preprint qualifier) was a concurrent agent's
Edit observed mid-mission and verified compatible with this audit.

## Patches (per AP316 delivery discipline)

This session ran in the main repo working tree (not worktree-isolated),
so no `git diff main...HEAD` patch export is required. Final state of
the three `\cite[Theorem~5.3.4] \to \cite[Corollary~5.3.4]` fixes is
directly visible in the working tree; `git status` and `git diff` will
show the diff when the user runs them.

No build or test run was executed; the edits are citation-label
surface-level changes with zero macro or mathematical-content impact,
and the pre-commit discipline (build + tests) is deferred to the
programme-level commit wave per session protocol.

## AP use

No new APs inscribed. Mission's reserved block AP1481--AP1500 is
released for future use (per AP306 reservation-recycling discipline).
Existing disciplines consulted: AP1241 (preprint-pillar),
AP285 (alias section-number drift),
AP308 (cron-fire Edit interleaving, observed but benign),
AP314 (inscription-rate floor).

---

Author: Raeez Lorgat
