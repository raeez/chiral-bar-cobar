# Chapter Prose Discipline Audit Progress

Loop attacks chapter-internal Russian-school prose (CLAUDE.md mandate):
meta-narration, bookkeeping vocabulary, symbol-before-definition,
definition-without-question, hedging, AI-slop phrasing, bare process
titles, em-dash overuse.

## Current cursor

- **Chapter**: chapters/theory/chiral_hochschild_koszul.tex
- **Offset**: 8525 (full title sweep + targeted body audit; deeper body audit deferred to next fire)
- **Next**: chapters/theory/chiral_hochschild_koszul.tex (continue body audit) OR chapters/theory/hochschild_cohomology.tex offset 1 (rotation forward)
- **Previous chapter**: theorem_A_infinity_2.tex audited end-to-end (2563 lines, 8 prose edits) in single fire.
- **Status**: cron `29ff8f97` cancelled by user; continuing manually.

## Audit log

### 2026-05-15 (manual, fire 2) — chiral_hochschild_koszul.tex (title sweep + targeted body audit)

Full chapter section/subsection enumeration (74 titles across 8525 lines) + targeted body reads at L1-220, L414-490, L615-700, L3440-3550, L6795-6810, L7025-7100. 8 title rewrites:

- L213: `\section{Construction of the chiral Hochschild complex}` → `\section{The chiral Hochschild cochain complex}` (drop "Construction of" process prefix; the section IS the cochain complex with its differential).
- L416: `\section{Computing cohomology via bar-cobar resolution}` → `\section{The diagonal bar resolution and the chiral Hochschild spectral sequence}` (drop "Computing ... via" process; name the two named objects produced — diagonal bar resolution L418-475, chiral Hochschild spectral sequence L478-495).
- L478: `\subsection{The spectral sequence}` → `\subsection{The chiral Hochschild spectral sequence}` (specify which spectral sequence — Theorem~\ref{thm:hochschild-spectral-sequence} immediately below names "chiral Hochschild spectral sequence").
- L620: `\subsection{Main duality theorem}` → `\subsection{Curve-level chiral Hochschild duality $\ChirHoch^n(\cA)\cong\ChirHoch^{2-n}(\cA^!)^\vee\otimes\omega_X$}` (drop generic "Main"; name the duality identity that the section proves; label `subsec:hochschild-duality` preserved).
- L3444: `\subsection{Establishing Koszul duality}` → `\subsection{Boson-fermion correspondence as lattice VOA extension, not Koszul duality}` (high-impact: the original title was actively MISLEADING because the section establishes the OPPOSITE — Theorem~\ref{thm:boson-fermion-lattice} + Remark immediately following clarify that boson-fermion is a lattice VOA extension via $V_{\mathbb Z}$, NOT Koszul duality, and the boson and fermion are not Koszul dual).
- L3499: `\subsection{Computing chiral Hochschild cohomology}` → `\subsection{Boson and fermion chiral Hochschild cohomologies and their non-Koszul comparison}` (drop "Computing" process; name the two computations + the non-Koszul comparison remark that constitute the section).
- L7029: `\subsubsection{Summary for Heisenberg}` → `\subsubsection{$\ChirHoch^*(\mathcal{B})$: Heisenberg cohomology table}` (drop "Summary for" generic; the subsubsection is a closed-form table for $\ChirHoch^*(\mathcal{B})$).
- L7065: `\subsubsection{Summary for free fermion}` → `\subsubsection{$\ChirHoch^*(\mathcal{F})$: free-fermion cohomology table}` (symmetric to L7029).

Discoveries:
- Body prose at L1-220 is densely mathematical; the chapter opens with a Hochschild-register-discipline remark distinguishing $\ChirHoch$ from THH/$\HH_{\mathrm{cat}}$/classical $\HH$/coHochschild — exemplary CG voice, no rewrite needed.
- L416 + L6798 BOTH carry "Computing chiral Hochschild cohomology via bar-cobar resolution" titles; L416 is the structural section (resolution + spectral sequence), L6798 is the explicit-computation section (free boson + free fermion worked tables). L6798 not yet renamed; flag for next fire as `\section{Chiral Hochschild cohomology of free fields via the diagonal bar resolution}` or similar.
- "Summary for X" pattern likely repeats in further example sections; sweep next fire.
- L3444 title was actively misleading (claimed to "establish Koszul duality" but ESTABLISHED the opposite); fix raises floor mathematically, not just stylistically.
- Many subsubsection titles in the explicit-computation sections (L7047, L7052, L7060, L6968, L6975, L6992, L7020) have `\texorpdfstring` wrappers naming the cohomology degree directly — these are already named-object titles.

Deferred:
- L141 `\section{Deformations of a chiral algebra}` — names content; kept.
- L497 `\section{Koszul duality for chiral algebras}` — names content; kept.
- L4928 `\subsection{Concrete modular constructions: from stable graphs to quantum homotopy theory}` — wordy but descriptive; deferred for body-prose fire.
- L5957/L6487 duplicate `Stratified periodicity` section + subsection — generic but content-named; deferred.
- L6697 `\section{Physical applications}` — generic process category; deferred for content-survey rename in next fire.
- L6798 `\section{Computing chiral Hochschild cohomology via bar-cobar resolution}` — same "Computing ... via" pattern as fixed L416; flagged above for next fire.
- L7098 `\subsection{Comparison with classical Hochschild cohomology}` — descriptive, not actively misleading; deferred.
- Body prose audit of L220-8525 not yet complete; advance next fire.

### 2026-05-15 (manual, fire 1) — theorem_A_infinity_2.tex (chapter close)

Full-chapter section/subsection sweep (24 titles enumerated) + targeted body audit of meta-narration / bookkeeping vocabulary across 2563 lines. 8 prose edits:

Title rewrites (5):
- L24: `\section*{Setup}` → `\section*{Notation, hypotheses, and lane structure}` (drop bare process title; name what the section actually establishes — notation block L46-53, three uniform hypotheses H1-H3, parametric strength taxonomy, Priddy/Positselski lane split, four lanes by categorical level, Notion-A...E disambiguation, ordered bar sign convention).
- L319: `\subsection{Statement}` → `\subsection{Bar--cobar adjunction, reconstruction on the Koszul locus, and Verdier duality}` (drop bare process title; name the three pieces of Theorem~A inscribed in the theorem environment immediately below).
- L1004: `\section{The eight statements as corollaries}` → `\section{The eight standard facets of Theorem~A}` (drop "as corollaries" process tail; the eight facets are themselves the named content).
- L2182: `\section{Ambient corrections}` → `\section{Symmetric monoidal ambient corrections}` (drop bare process title; name the ambient — symmetric/ordered bar forms in $(\Fact(X),\star)$, unit functor, stratum extensions).
- L2512: `\section*{Closing remark}` → `\section*{Theorem~A as the algebraic structure on the KZ functor}` (drop "Closing remark" meta-prefix; name the load-bearing claim in the closing — Theorem~A enters the five-theorem spine as the algebraic structure on the KZ functor of the climax chapter, the pullback identity $\bar\partial = \KZ^*(\nabla_{\mathrm{Arnold}})$).

Body-prose rewrites (3):
- L43: "Thus bar--cobar reconstruction is inversion on the Koszul locus" → "Bar--cobar reconstruction is inversion on the Koszul locus" (drop "Thus" connective-meta).
- L138-141: "is the master-pattern violation MA-1 (shadow=object) applied to the forgetful functor..." → "confuses the shadow with the object along the forgetful functor..." (drop bookkeeping prefix "MA-1"; state the failure directly).
- L201: "The MA-13 violation ``ordinary = completed ambient''" → "Identifying the ordinary ambient with the completed ambient" (drop bookkeeping prefix "MA-13"; state the failure as predicate).

Discoveries:
- Section/subsection titles in the chapter are mostly already in CG voice ("Bar-cobar reconstruction and Verdier duality: unified Theorem~A" L316, "Archetype witnesses of (H1)--(H3)" L562, "Universal chain-homotopy normalisation" L774, "Francis--Gaitsgory factorization ambient" L1230, "Factorization properads" L1345, "Theorem~A^{\infty,2}: the explicit properadic-envelope form" L1429, "$R$-matrix-twisted $\Sigma_n$-descent" L1779, "Restrictions and consequences..." L2023, "Formal smoothness of chirally Koszul algebras" L2324, "Platonic obstructions: four named conjectures" L2381, "Comparison with independent constructions" L2437, "K3 Hall--Drinfeld input and Theorem~A scope" L2527).
- Body prose is densely mathematical with explicit type-signature discipline (HP packages named, two-lane Priddy/Positselski split inscribed, Notion A-E disambiguation), no meta-narration in the standard-CG dictionary outside the single "Thus" caught.
- The MA-N references at L138, L201 were the only bookkeeping-vocabulary instances in body prose; no AP-N labels appear in this chapter.
- All 5 title rewrites preserve the underlying `\label{}` so internal cross-references unaffected (\S\ref{sec:ainf2-koszul-reflection} L1276; sec:ainf2-eight-corollaries unchanged).
- Chapter complete in one fire.

Deferred:
- L437 `\subsection{The single diagram and the single equation}` — descriptive but generic; the section content IS exactly one diagram and one equation, so the title is honest. Kept.
- L2381 `\section{Platonic obstructions: four named conjectures}` — "Platonic obstructions" is in-house architectural terminology used widely across the manuscript (CLAUDE.md "platonic ideal architecture"); not a generic process-prefix. Kept.
- L2437 `\section{Comparison with independent constructions}` — generic but not actively misleading; the section compares Theorem~$A^{\infty,2}$ against three independent constructions. Kept.

### 2026-05-10 — chern_weil_level_shift_platonic.tex

Out-of-rotation pass on `chern_weil_level_shift_platonic.tex` (lines
555-680) because it had concentrated AP-label / process-title
violations that were faster to attack first.

Fixed:
- L559: corollary label `cor:ap126-healing-universal` →
  `cor:level-shift-universal-convention-bridge`; title "universal
  healing" → "$r$-matrix convention bridge with explicit $k=0$ check"
- L604: remark label `rem:ap141-downstream` →
  `rem:level-prefix-grep-detector`; title "downstream" → "Detector
  for level-prefix omission"; body rewritten to drop `\backslash`
  literal grep regex (LaTeX-escape-heavy noise) in favour of
  $r(z) = \Omega/z$ pattern phrasing
- L617-622: section "Independent verification" /
  `sec:hz-iv-level-shift` → "Independent verification of the
  level-shift theorems" / `sec:level-shift-independent-verification`
- L653-664: section "False coincidence isolated" /
  `sec:fp-cache-entry` → "Trace-form versus KZ presentation: not a
  hidden Casimir rescaling" /
  `sec:trace-vs-kz-r-matrix-disambiguation`; opening rewritten as a
  candidate identification with explicit "false" verdict
- L666: `\section*{Closing: ...}` → `\section*{The level shift as
  the universal Sugawara parameter}` (drop "Closing:" meta-prefix);
  body unchanged structurally

All 6 internal references updated; no external references existed.
Verified zero orphan refs to old labels.

### 2026-05-14 (manual, after cron cancelled) — chiral_koszul_pairs.tex (chapter close)

Full-chapter scan: zero standard-CG meta-narration phrases across 8106 lines. Body prose is uniformly direct. Three remaining title rewrites:

- L6299: `\subsection{Warm-up: Virasoro algebra}` → `\subsection{Virasoro Koszul-duality calculation}` (drop "Warm-up" meta-organising prefix).
- L7932: `\section{Summary}` → `\section{The Koszul-pair landscape}` (drop generic title; name the surveyed object).
- L8051: `\section{Synthesis (continued)}` → `\section{The Koszul triple for $\mathbf H_{\Delta_5}$ on $(\Ran(E^{\mathrm{nod,sm}}_{24}),\overline{\mathcal A}_2)$}` (drop generic + meta "continued"; name the inscribed object).

Chapter complete: 5 prose edits over 2 fires (2 title rewrites + 1 body rewrite earlier fire, plus 3 title rewrites this fire).

### 2026-05-10 (cron fire 7) — bar_construction.tex (chapter close, lines 1700-3393) + chiral_koszul_pairs.tex (initial title pass)

#### bar_construction.tex (1700-3393, chapter close)
- Lines 2100-3393: full grep for meta-narration, hedging, bookkeeping; ZERO violations found in body prose. Chapter is in CG-voice from L2100 onward.
- L2051: `\subsection{Coalgebra axioms: verification}` → `\subsection{Coalgebra axioms for the bar coalgebra}` (drop "verification" process suffix; name the object whose axioms are being verified).
- L573: `\subsection{Precise construction of the bar complex}` → `\subsection{Construction of the geometric bar complex}` (drop "Precise" meta-prefix; name the variant).
- L385: `\subsection{Non-abelian Poincar\'e perspective on bar construction}` → `\subsection{Non-abelian Poincar\'e realization of the bar complex}` ("perspective on" process-style → "realization of" object-style).
- Chapter complete: 6 edits over 2 fires (3 body prose + 3 title rewrites).

#### chiral_koszul_pairs.tex (initial title pass, 8107 lines total)
- L962: `\subsection{The concept of chiral Koszul pairs: precise formulation}` → `\subsection{Chiral Koszul pairs}` (drop "The concept of" + "precise formulation" double meta).
- L1161: `\subsection{Koszulness verification: the PBW deformation method}` → `\subsection{PBW deformation as a Koszulness criterion}` (drop "verification" process; rename to object-style).
- Body-prose at L962 also rewritten: "we extend the notion of Koszul pairs beyond the quadratic setting" → "The Koszul-pair notion extends beyond the quadratic setting" (drop "we extend" first-person).

### 2026-05-10 (cron fire 6) — bar_construction.tex (lines 1-1700) + configuration_spaces.tex (chapter close, lines 5800-6408)

#### bar_construction.tex (1-1700)
Body-prose rewrites (drop "in this monograph" / "we" meta-attribution):
- L449: "convention bridge from the ordered presentation used in this monograph to the symmetric factorization-coalgebra formalism" → "convention bridge from the ordered $\Eone$-presentation to the symmetric factorization-coalgebra formalism" (drop "in this monograph", name the structure type explicitly).
- L901: "Thus the per-family bar differentials are not independent data: every bar differential in this monograph is the pullback of one universal flat connection..." → "The per-family bar differentials are not independent data: every bar differential is the pullback of the single universal flat connection $\nabla_{\mathrm{Arnold}}$..." (drop "Thus" / "in this monograph"; name the connection by its universal symbol).
- L1661: "See also Appendix~\ref{app:arnold-relations} for the three proofs of the Arnold relations used in this monograph." → "Appendix~\ref{app:arnold-relations} records the three proofs of the Arnold relations (topological, combinatorial, operadic) used elsewhere in the manuscript." (rephrase as direct statement; name the three proofs).

Deferred:
- L1630 "developed in \S\ref{sec:arnold-three-proofs-comprehensive}" — the "comprehensive" is in a section LABEL, not body prose; standalone label rename deferred per protocol.
- L3011 `\section{Ordered K3 convolution}` — fine; named object, not process.

#### configuration_spaces.tex (5800-6408, chapter close)
Audit only — chapter is structurally complete after the cron fire 5 rewrites.
- Body prose is direct mathematical statement (theorem/proof/remark, no narration).
- Conditional theorems C1–C5 (lines 6015-6388) are well-stated with explicit \ClaimStatusConditional tags.
- Closed at L6408.

### 2026-05-10 (cron fire 5) — configuration_spaces.tex (structural pass over 6406 lines)

Section/subsection title rewrites (drop meta prefixes, name objects):
- L4880: `\subsection{General setup: coordinate systems near boundaries}` → `\subsection{Coordinate systems near collision boundaries}` (drop "General setup" meta prefix; specify the boundary type).
- L4931: `\subsection{The simplest case: two points ($n=2$)}` → `\subsection{Pair collisions ($n=2$)}` (drop "The simplest case" meta).
- L4990: `\subsection{Three points ($n=3$): first nontrivial case}` → `\subsection{Three-point collisions ($n=3$)}` (drop "first nontrivial case" suffix).
- L5070: `\subsection{General case: $n$ points}` → `\subsection{$n$-point collisions for arbitrary $n$}` (drop "General case" prefix).
- L5728: `\section{Synthesis}` → `\section{The Ran-space base for the K3 chiral bialgebra $\mathbf H_{\Delta_5}$}` (matches the inscribed Remarks; concrete content title).

Discoveries:
- The chapter is overall *very* clean: zero meta-narration phrases ("we now", "having established", "crucially", etc.) in prose, only AP-comprehensive labels at L4614, L4630.
- Body prose maintains direct mathematical voice throughout; only section/subsection titles needed rewrites this fire.
- Several "Synthesis" sections will need the same content-renaming treatment across the manuscript (next chapters: configuration_spaces ✓ algebraic_foundations ✓; remaining: cobar_construction, koszul_pair_structure, computational_methods, infinite_fingerprint_classification, nilpotent_completion).

Deferred:
- L4503 `\subsection{Complexity analysis}`, L4572 `\subsubsection{Efficient residue computation}` — generic but not actively misleading; deferred.
- L1740 `\subsubsection{Connection to factorization homology}` — "Connection to" mildly process-style; deferred.
- L4614/L4630 labels containing "comprehensive" — labels not body-prose violations.

### 2026-05-10 (cron fire 4) — algebraic_foundations.tex (lines 2100-2916, chapter end)

Title rewrites:
- L1299: `\subsection{Ran space and universal recipients}` → `\subsection{The Ran space and chiral sheaves}` (the phrase "universal recipients" was opaque; the section defines the Ran space and the chiral $\mathcal D$-modules / sheaves it carries).
- L2297: `\subsection{Master verification table}` → `\subsection{Factorization axiom verification table}` (drop self-aggrandizing "Master" prefix; name the object).
- L2883: `\section{Synthesis}` → `\section{Algebraic foundations of the K3 chiral bialgebra $\mathbf H_{\Delta_5}$}` (drop generic "Synthesis"; name the actual content; matches the inscribed Remark inside).

Body-prose rewrites:
- L2291: "The bar-cobar constructions in this monograph use..." → "The bar-cobar constructions below use..." (drop "in this monograph" meta-attribution).

Deferred:
- L1293 `\subsection{Factorization as local-to-global}` — descriptive, not violating; kept.
- L1744 `\subsection{The genus expansion}` — generic but acceptable; kept.
- Tail of chapter (Synthesis section, Remark on $\mathbf H_{\Delta_5}$) is direct mathematical prose; no further edits.

### Chapter total
- algebraic_foundations.tex: audited end-to-end (lines 1-2916 over 4 cron fires).
- 17 prose edits total: 9 section/subsection title rewrites + 8 body-prose rewrites.
- Cross-references verified after each title-rename batch; zero orphans.

### 2026-05-10 (cron fire 3) — algebraic_foundations.tex (lines 1700-2100)

Section/subsection title rewrites (process titles → object names):
- L1860: `\section{Derivation of Com-Lie duality}` → `\section{Com--Lie Koszul duality}` (drop "Derivation of" process prefix; use proper en-dash).
- L1980: `\section{Factorization algebra axioms: verification}` → `\section{Factorization algebra axioms}` (drop "verification" process suffix).
- L1983: `\subsection{Motivation}` → `\subsection{Configuration-space realization of factorization algebras}` (bare "Motivation" → object-style title with the geometric content named).

Body-prose rewrites (meta-narration / hedging → direct):
- L1945: "For explicit computations, we need the quadratic presentations:" → "The explicit quadratic presentations of $\Com$ and $\Lie$ are the following." (utilitarian "we need" prefix replaced with direct).
- L1956: "This orthogonality is the concrete manifestation of Koszul duality." (hedging "concrete manifestation") → "At the operadic level, Koszul duality between $\Com$ and $\Lie$ is exactly this orthogonality." (X = Y form).

Deferred:
- L1934 "We compute the pairing explicitly" — standard mathematical "we" usage in a proof.
- L1744 `\subsection{The genus expansion}` — generic but not violating; kept.

### 2026-05-10 (cron fire 2) — algebraic_foundations.tex (lines 700-1700)

Body-prose / title rewrites:
- L946: `\emph{Key point.}` (meta emphasis) → "Every row of the table carries..."; deleted self-referential framing.
- L1489-1492: "This remark is foundational: \emph{universality is not...}" (meta-narration prefix + emphasis on what the remark itself means) → direct statement "Universality is not an additional hypothesis but a precondition..." with the cross-references woven into the same sentence.
- L1554: `\subsection{The fundamental bar-cobar isomorphism}` → `\subsection{The operadic bar-cobar isomorphism}`.
- L1684: `\section{The operadic bar-cobar duality}` → `\section{Operadic bar-cobar duality}` (drop "The" prefix); first sentence rewritten from "we construct the bar and cobar functors:" to "the bar and cobar functors are constructed as follows."
- L1517-1519: `\section{The cotriple bar construction}` body whitespace + colon convention tightened (cosmetic).

Deferred:
- "We work in $\mathcal V = \mathrm{Ch}_\C$" (L1234) — standard mathematical "we" usage; no fix.
- "For a detailed treatment ... see Definition X (Chapter Y)" (L1353-1357) — forward reference is normal.

### 2026-05-10 (cron fire 1) — algebraic_foundations.tex (lines 1-700)

Subsection-title rewrites (process titles → object names):
- L105: `\subsection*{Motivating geometry: collisions and duality}` → `\subsection*{Collisions and duality on a curve}`
- L249: `\subsection{Koszul pairs: precise definition}` → `\subsection{Koszul pairs}`
- L389: `\subsection{Classical examples revisited}` → `\subsection{Classical Koszul examples}`
- L429: `\subsection{Chiral Koszul pairs: preview}` → `\subsection{Chiral Koszul pairs}`
- L469: `\subsection{Twisting morphisms: the fundamental object}` → `\subsection{The convolution dg Lie algebra and its twisting morphisms}`

Body-prose rewrites (meta-narration → direct):
- L124-127: "here we focus on the algebraic avatar" → "The algebraic avatar — \emph{classical Koszul duality} — appears next."
- L530-532: "for \emph{computing} Maurer–Cartan elements, which is the primary use throughout Part~..., the strict dg~Lie model suffices" → "the strict dg~Lie model suffices for computing Maurer–Cartan elements, the primary use in Part~..."
- L549-551: "All constructions in this monograph are functorial..." → "Every construction below is functorial..."
- L649: "For concreteness we record the explicit formulas." → "The explicit higher brackets are as follows."

Deferred (legitimate technical usage, not violations):
- "in this monograph" at L485, L2286 — both attribute scope to specific results, retained.

### Discoveries from broader scan
- `chern_weil_level_shift_platonic.tex` was a hot-spot; rotation
  order should add this file ahead of `kappa_conductor.tex`.
- AP-numbered labels are widespread: `chiral_center_theorem.tex`,
  `infinite_fingerprint_classification.tex`,
  `topologization_chain_level_platonic.tex`,
  `mc5_genus0_genus1_wall_platonic.tex`,
  `shadow_tower_quadrichotomy_platonic.tex`,
  `motivic_shadow_tower.tex`, `clutching_uniqueness_platonic.tex`,
  `genus_2_ddybe_platonic.tex`, `concordance.tex`,
  `bar_cobar_adjunction_inversion.tex`. Each likely needs the same
  treatment.
- Hedging phrases ("essentially", "may be viewed", etc.) are mostly
  legitimate technical usage ("essentially surjective" is a category
  theory term); only one cosmetic violation found and fixed in
  `higher_genus_complementarity.tex:3230`.
- Top theory chapters (introduction, algebraic_foundations,
  configuration_spaces, bar_construction, chiral_koszul_pairs,
  hochschild_cohomology, higher_genus_foundations) have **zero**
  meta-narration violations from the standard CG dictionary —
  rotation can pass over these quickly.
