# Brief Audit: Khan-Zeng PVA as Seven Faces Face 3 (Vol I scope)

Date: 2026-04-18. Author: Raeez Lorgat.
Scope: Vol I inscription of F3 (Khan-Zeng PVA) per CLAUDE.md B84.
Companion to `adversarial_swarm_20260418/wave3_khan_zeng_scope_attack_heal.md`
(Vol II scope, same date). This brief does NOT duplicate Wave 3; it records
Vol-I-specific findings only.

## 1. Locator map for F3 = Khan-Zeng in Vol I

Genus-0 Face 3 (citation-level scaffolding):

- `chapters/connections/holographic_datum_master.tex:165-166` — Face 3 is
  "leading lambda-bracket coefficient of the classical Poisson vertex
  algebra of Khan-Zeng (genus 0 only)", bundled into the seven-face
  heptagon together with F1 (bar-cobar twist), F2 (DNP25 line operators),
  F4 (Gaiotto-Zeng sphere Hamiltonians), F5 (Drinfeld Yangian),
  F6 (Sklyanin/STS83), F7 (FFR94 Gaudin).
- `chapters/connections/holographic_datum_master.tex:318-319` — paragraph
  attributing the 3d Poisson sigma model construction to KZ25.
- `standalone/introduction_full_survey.tex:4138-4139` — Face 3 named
  "the PVA classical r-matrix of `\cite{KhanZeng25}`".
- `standalone/genus1_seven_faces.tex:135-137` — identical bundling at
  genus 1.

Genus-1 upgrade of F3:

- `chapters/connections/genus1_seven_faces.tex:853-856` — Face F3^{(1)} in
  `thm:g1sf-master` is "generating function of the elliptic lambda-bracket
  of the classical PVA on E_tau (Khan-Zeng, genus-1 specialisation)";
  parenthetical, cited not inscribed. The same file at :906-909 states
  "F2, F3, F6 follow by the same elliptic-regularisation argument applied
  to their genus-0 counterparts, with the detailed cross-volume
  verifications recorded in Vol II". This is the Vol I seam where F3
  delegates substance to Vol II.

W_3 case-by-case (load-bearing in Vol I):

- `chapters/examples/w_algebras.tex:3178-3380` — the W_3 3d HT Poisson
  sigma model is inscribed as `prop:w3-3d-action` with
  `\ClaimStatusProvedElsewhere` `\cite{KhanZeng25}`. Also
  `prop:virasoro-beltrami-phase-space`, `prop:schwarzian-central-charge`,
  `prop:virasoro-3d-gravity-action` (all ProvedElsewhere, KZ25).
- `chapters/examples/w_algebras.tex:3233` — the proof body of the
  "full topological symmetry enhancement" paragraph applies
  `\cite[Theorem 4.1]{KhanZeng25}` directly.
- `chapters/examples/w_algebras.tex:5849-5903` — `def:super-virasoro-pva`
  (N=1 super-Virasoro PVA), ProvedElsewhere.
- `chapters/examples/w_algebras.tex:6043-6045` — the finite-generator-degree
  polynomial bound compares to `\cite[\S3]{KhanZeng25}`.
- `chapters/connections/semistrict_modular_higher_spin_w3.tex:64-65,152` —
  the semistrict W_3 chapter uses KZ25 as the load-bearing bulk theory for
  the boundary-to-bulk dictionary, with `\cite[\S4]{KhanZeng25}` cited at
  the nonlinear generator-degree count.

Topologization citation (separate from F3-as-face but uses same KZ25 input):

- `chapters/theory/en_koszul_duality.tex:3072` — `thm:topologization`
  "Cohomological topologization for affine Kac-Moody" tagged
  `{\cite{KhanZeng25}}` in the theorem header.
- `chapters/theory/topologization_chain_level_platonic.tex:79,124,704-707` —
  three citations, each correctly naming "cohomological" scope
  (per AP-TOPOLOGIZATION, AP158/167/168).

## 2. Chapter-level vs standalone-only?

F3 is NOT chapter-level-inscribed as a stand-alone theorem in Vol I.
Chapter-level presence is confined to (a) the seven-face heptagon
bundling of `holographic_datum_master.tex` and `genus1_seven_faces.tex`
(which enumerates the face and attributes without proving a dedicated
F3 identification theorem) and (b) the W_3 and N=1 super-Virasoro
per-case instantiations in `w_algebras.tex` at ProvedElsewhere.
The comprehensive F3 bridge theorem — a statement of the form
"the leading lambda-bracket coefficient of the Khan-Zeng classical
PVA equals the collision residue r_A(z) of the bar-intrinsic twist" —
is NOT present as a labelled Vol I theorem. Closest inscription is
`thm:g1sf-master` clause (F3^{(1)}) at genus 1, which states the
identification parenthetically and delegates proof to
elliptic-regularisation of genus-0 counterparts recorded in Vol II.

Scope classification under HZ-11 / AP287: F3 in Vol I is a
CITATION-LEVEL face. The load-bearing theorem `thm:E3-topological-free-PVA`
lives in Vol II `chapters/connections/3d_gravity.tex:7041-7070`
(per Wave 3 note :6). Vol I consumers use KZ25 exclusively via
`\cite{KhanZeng25}` at `\ClaimStatusProvedElsewhere` tags, with the single
exception of the `thm:topologization` header tag which reads
"; {\cite{KhanZeng25}}" in its title — this is header-attribution-only,
not a proof-chain delegation (the proof body routes through Vol II
`thm:iterated-sugawara-construction` and the local Sugawara construction,
and `thm:topologization` is a distinct object from F3).

## 3. B84 scope qualifier "freely-generated PVAs with conformal vector"

Programme-wide application of the qualifier in Vol I: consistent at
CITATION level. Every `\cite{KhanZeng25}` site in Vol I either
(i) names the face heptagon ornamentally, (ii) invokes the W_3 case
where freeness and conformal vector are direct, or (iii) invokes the
Virasoro/affine-KM case where freeness holds by inspection and
conformal vector is the given input. The "check gr_Li(A) first"
advisory of B84 has NO Vol-I-inscribed decision procedure
(`prop:kz-admissibility-test` is listed in the Wave 3 heal plan as
a Vol II deliverable; no Vol I analogue exists).

NO Vol I site was found claiming Khan-Zeng covers non-freely-generated
or without-conformal-vector algebras. The Vol I standalone
`standalone/en_chiral_operadic_circle.tex:1562-1563` explicitly writes
"all conformal vertex algebras with freely generated PVA associated
graded (Khan-Zeng)", which is the correct qualifier.

One Vol I site worth flagging defensively:
`chapters/examples/deformation_quantization.tex:107` reads "For the
gauge-theoretic origin of PVA structures via 3d holomorphic-topological
theories, see Khan-Zeng". This is bare and does not qualify to
freely-generated-with-conformal-vector. The immediate prose context is
already restricted to "would-be OPE" E_infinity-chiral input, which
implicitly selects the qualifier, but a future agent reading that one
sentence in isolation could infer universal coverage. Flag only;
heal is not load-bearing.

## 4. F3 independence from F1 (bar-cobar), F2 (DNP25), other faces

The seven-face master theorem `thm:g1sf-master` lists seven realisations
of the same collision residue r_A^{(1)}(z, tau) on affine KM at
non-critical level, asserting a boxed seven-fold identification. F3 is
NOT independent from F1 in the theorem's logical architecture: F1 is
the base object (bar-cobar twisting morphism), F2-F7 are identifications
of F1 with alternative physical/algebraic presentations. The boxed
equation at `chapters/connections/genus1_seven_faces.tex:879-896`
presents all seven as equalities, so F3's content is the ASSERTION
"bar-intrinsic collision residue equals the leading lambda-bracket
coefficient of the Khan-Zeng PVA", not a free-standing PVA theorem
of Vol I's own.

This is architecturally honest (F3 is a bridge face, not a pillar) but
deserves note for AP247 discipline: the seven-face theorem is a
correspondence programme, not a single unified functor. Each face Fi
is a per-face identification with a different algorithmic/categorical
input; the boxed "equals" chain lives on a specific working locus
(affine KM non-critical) where all seven inputs are defined and finite.

F3's independence from F2 (DNP25 line-operator r-matrix, also Vol I):
F2 and F3 are genuinely independent inputs — F2 routes through
categorical line-operator OPE in 4d HT gauge theory; F3 routes through
classical PVA in 3d HT Poisson sigma model. They identify because both
compute the same collision residue on the programme's working locus;
this identification is the content of the seven-face theorem and is
NOT a tautology.

## 5. Heal (Vol I only)

Three low-weight Vol I edits proposed. Executed in this session:

(E1) `chapters/examples/deformation_quantization.tex:107` —
qualifier added: "see Khan-Zeng (freely-generated PVAs with
conformal vector)". Prevents AP247 / AP309 bare-citation drift.

(E2) `chapters/connections/genus1_seven_faces.tex:906-909` —
scope remark cross-reference to Vol II `thm:E3-topological-free-PVA`
inscribed as `rem:g1sf-f3-vol-ii-scope` immediately after the
proof of `thm:g1sf-master`, making the Vol I delegation to Vol II
explicit (per AP287 cross-volume attribution discipline).

(E3) None — the W_3 per-case inscriptions at `w_algebras.tex`
are already ProvedElsewhere-tagged and cite KZ25 correctly.

NOT executed in this session (out of Vol I scope):

- The five items of the Wave 3 commit plan, all of which touch Vol II
  or CLAUDE.md B84 propagation across CLAUDE.md's own line. Owner:
  next Vol II pass.

## 6. AP register (minimal, per AP314)

One AP block inscribed this pass. See CLAUDE.md append.

- **AP2081** — Bare-citation drift on a scope-qualified external pillar.
  Template: any `\cite{XY25}` for an external construction carrying a
  load-bearing hypothesis ("freely-generated PVA with conformal vector")
  that lacks the qualifier at the citation site, in a prose context that
  does not lexically restrict to the qualifier's satisfaction set.
  Counter: at every `\cite{KhanZeng25}` / `\cite{KZ25}` / `\cite{KZ2025}`
  site in Vol I or Vol II, grep the surrounding 3 lines for one of the
  restrictor phrases "freely generated", "conformal vector",
  "non-critical level", "W_N", "affine Kac-Moody", "Virasoro", "Heisenberg",
  "classical PVA"; zero hits on any phrase is a bare-citation violation
  and forces addition of the qualifier. Distinct from AP272 (unstated
  cross-lemma via folklore citation) and AP309 (primary-source citation
  for a strictly weaker claim); AP2081 is specifically the case where the
  primary source IS the correct reference at full strength but the
  qualifier is absent from the citation context, inviting a reader to
  overgeneralise the construction's applicability.

## 7. Build / test status

No build or test invocation this pass (mission is audit + two inline
remarks). Per session protocol, build + test re-run deferred to the
Vol II propagation pass which also executes the Wave 3 commit plan.
