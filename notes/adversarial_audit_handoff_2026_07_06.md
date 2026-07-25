# Three-Volume Adversarial Audit + Repair Campaign — Full Handoff Report

Date: 2026-07-06. Session: hostile-referee audit of all three volumes
(8 deep-read audit agents + 2 bibliography cite-check agents + direct
main-thread verification), followed by a partially-completed repair
campaign (interrupted by user; 15 repair agents killed mid-flight).
This document contains EVERY issue found, EVERY fix already applied
(all uncommitted, in the working trees), and the COMPLETE remaining
work queue with file:line targets and corrected values, so a future
agent can resume without the original conversation.

Repos:
- Vol I:   /Users/raeez/chiral-bar-cobar          (~652k lines .tex, 291 files)
- Vol II:  /Users/raeez/chiral-bar-cobar-vol2     (~365k lines, 222k in build)
- Vol III: /Users/raeez/calabi-yau-quantum-groups (~693pp)

Claim-status census (Vol I): 2052 ProvedHere, 557 ProvedElsewhere,
1830 Conditional, 386 Conjectured, 46 Heuristic, 1 Retracted;
1683 theorem + 1291 proposition envs vs 3338 proofs;
265 occurrences of "hypothesis package".

---

## PART A — AUDIT FINDINGS (the full issue inventory)

### A1. Theorem A (`chapters/theory/theorem_A_infinity_2.tex`, 2713 lines)

Statements: `thm:koszul-reflection` (l.323–406) and `thm:A-infinity-2`
(l.1565–1657), both `\ClaimStatusConditional`.

- **G1 (fatal, OPEN).** The ambient category Fact(X) in which the whole
  adjunction lives is never constructed. Its symmetric monoidal
  structure, strict unit, and (∞,2)-enhancement are clauses (b)–(d) of
  `prop:fg-ambient-properties` (l.1424–1462) whose proof is literally
  headed `\begin{proof}[Status]` and says "The remaining clauses are an
  explicit hypothesis package in this volume... no numbered GR theorem
  is used". Main proof (l.429–435) concedes the LV12/Vallette transfer
  "is not a published GR17 model structure theorem". Net: Theorem A =
  "if a suitable category exists, LV12+Positselski apply in it."
- **G2 (OPEN).** `thm:hackney-robertson-model` (l.1528–1549), tagged
  ProvedElsewhere, asserts a "combinatorial model structure" on the
  (∞,2)-category FactProp(X); proof is `\begin{proof}[References]` with
  a gestural "formal transfer". HR arXiv:1905.11393 concerns
  ∞-properads in sSet, not D-module factorization ambients; "model
  structure on an (∞,2)-category" is not coherent as stated.
- **G3 (FIXED — see B4).** Step 2 of the main proof (l.1687–1709)
  derived acyclicity from exact ⋆-base-change + ML convergence, which
  are hypotheses of the theorem itself (l.1575–1579); the remark
  `rem:A-inf-2-ml-step-2` (l.1744–1770) patches the wrong-filtration
  attachment. Fixed: Step 2 now names both as standing hypotheses and
  points to the remark.
- **G4 (PARTIALLY FIXED — see B4; chain-level verification OPEN).**
  `prop:A-universal-chain-homotopy` (l.916–1011),
  h_{A_b} = h_LV/N(A_b): the proof claimed "the Priddy contraction is
  normalised so that h_LV has unit pairing" — LV12 Thm 7.4.1 has no
  pairing normalization; no pairing on the convolution algebra is
  defined; scalar division of a homotopy operator unjustified; the
  Virasoro denominator was imported circularly "through the chiral
  Hochschild trace pairing of Theorem H" (H is downstream of A). The
  file confesses "A direct chain-level verification... is not
  inscribed" (Frontier F1†). Fixed: false normalization claim and
  Theorem-H circularity removed; the chain-level verification on
  Garland–Lepowsky strata REMAINS THE OPEN OBLIGATION.
- **G5 (OPEN).** Reconstruction clause (KR-ii): E2-collapse delegated to
  `thm:ftm-seven-fold-tfae-via-hub-spoke`
  (ftm_seven_fold_tfae_platonic.tex:201) which is restricted to a
  genus-zero finite-type PBW window while Theorem A claims arbitrary
  genus (l.340). Archetype "proof" (`rem:five-archetype-K-squared`,
  l.838–867) is five one-liners; the E2 page is described via the
  object it should compute; no differential exhibited.
- **FIXED (B4):** dangling `\ref{def:symmetric-bar}` (l.2058) →
  `def:geometric-bar`; 13 stale `\ref{lem:R-twisted-descent}` (renamed
  2026-05-17 to `lem:R-twisted-descent-unitary`, comment l.1970) →
  repointed; "Francis star-product"/"Francis 2012" Gaitsgory-erasure
  (7 sites) → "Francis–Gaitsgory"; garbled "(Francis HA appendix;
  Lurie HA §5.5)" → Lurie only.
- **Novelty verdict:** after subtraction, the genuinely novel rigorous
  content is (a) the R-twisted ordered→symmetric descent cocycle
  argument (Steps 1–2 real; stratum extension (R3) wholly hypothesis;
  Drinfeld–Kohno-adjacent), (b) the (H3) witness counting lemma
  P(q)/(1−P(q)). The rest restates FG12 + Positselski + LV12 under
  assumed packages.

### A2. Theorem H (`chapters/theory/chiral_hochschild_koszul.tex`, 9990 lines)

Statement: `thm:main-koszul-hoch` (l.3397, Conditional); concentration
clause `thm:hochschild-polynomial-growth` (l.3578). Hypothesis package
(H1)–(H6) at `def:theorem-h-pbw-finite-window-lane` (l.410–441).

- **(a) OPEN.** The engine is a named open conjecture:
  `prop:fm-tower-collapse` (l.1348) assumes stratum-wise acyclicity =
  `conj:ordered-twisted-tensor-acyclicity` (l.2167/2169). The symmetric
  route's `thm:bar-concentration` (chiral_koszul_pairs.tex:1578) is
  itself Conditional; its proof reads "acyclic in positive degrees by
  hypothesis". Localization-to-stratum step nowhere proved.
- **(b) OPEN.** The duality shift [2] is a Definition containing an
  unexhibited proof: `def:theorem-h-shift-normalization-package`
  (l.935–973) lists as datum (v) "a proof that...";
  `lem:hochschild-shift-computation` (l.1064) admits "the shift is the
  non-formal part... Definition ... is precisely the hypothesis."
- **(c) FIXED (B3).** False identity at l.696–699:
  d_dR(η12) ≡ −η23−η31 mod smooth — but d(dlog(z1−z2)) = 0
  identically. Fixed: replaced by the correct mechanism — η12 closed on
  the open stratum; d_config acts through the Stokes boundary
  restriction; the boundary identity is η13|_{D12} = η23|_{D12}
  (restriction form of Arnold). NOTE: the "for general n, the argument
  extends" gesture (l.707) REMAINS OPEN.
- **(d) FIXED (B3).** Semicontinuity used backwards in
  `lem:chiral-quadratic-koszul` Step 1 (l.1295–1301): nondegeneracy is
  open (rank lower semicontinuous), does NOT propagate to collision
  divisors. Fixed: open-dense locus by semicontinuity; divisors handled
  by the FM3 local model clause (which itself remains the load-bearing
  conditional step).
- **(e) OPEN.** ML/perfectness certificates exist only for rank-1
  Heisenberg (l.1906); `rem:theorem-H-filter-exactness` (l.3376–3387)
  concedes affine/Virasoro/W lanes are pure hypothesis. The averaging
  step `cor:hochschild-averaging-symmetric` (l.2933) needs per-family
  Yang–Baxter + strong unitarity, verified for no archetype. Even the
  flagship Heisenberg (1,1,1) table is Conditional (admitted l.1951):
  `prop:heisenberg-two-point-mixed-mode-residue-formula` (l.2541) shows
  the mechanism FAILS on mixed-mode combinations.
- **Literature warning (OPEN — must be engaged):** De Sole–Kac
  variational Poisson cohomology is NONVANISHING in unboundedly many
  degrees for Virasoro-type PVAs; Bakalov–De Sole–Heluani–Kac vertex
  algebra cohomology never engaged. This cuts against concentration;
  any resumed proof effort must confront it.
- **FIXED (B3):** Goncharova/Fuks garble (l.3829→3840): H*(L+) is NOT
  C[c2]; correct: dim H^q(L+;C)=2 for q≥1, generators in weights
  (3q²∓q)/2, cup products vanish. "Whitehead's theorem" for
  HH¹(Weyl)=0 → Sridharan 1961 (bibitem `Sridharan61` added).
  Weibel-Ch.9-for-Clifford misattribution → replaced by an actual
  parity/charge-derivation argument (charge derivation inner via zero
  mode of J = :ψψ*:). Fresse2017 Ch.7 (4 sites) → Loday–Vallette
  \cite[Ch.~7]{LV12} (Fresse2017 is the GT book, wrong source).
- **Post-Shelton–Yuzvinsky-excision status:** effectively conjectural;
  ~15 downstream Conditional corollaries consume it as if proved;
  chapter head (l.14–16, 50–53) asserts amplitude [0,2] as delivered.

### A3. Master Reconstruction (`chapters/connections/master_reconstruction.tex`, ~1260 lines) — ALL OPEN

Theorem `thm:mr-master` (l.542–559, Conditional) is an organizational
schema: (M1) is the conjunction of five pointers.
- **Morita 1↔0 (l.328–368): CIRCULAR.** H0 includes "the enriched
  Yoneda–Morita comparison is fully faithful and essentially
  surjective" — the hypothesis IS the conclusion. Proof admits it
  (l.364–366). Fix: restate as definition of level-0 object +
  named open recognition problem; adjust (M1).
- **Drinfeld-double 4→3 (l.462–495): IOU.** The displayed equivalence
  Bimod(Z^der_ch(A_b)) ≃ Z_Dr(Line(A_b)) appears nowhere else in the
  repo; proof cites "Joyal–Street + chiral promotion of [EGNO Ch.7]" —
  EGNO proves nothing chiral; the promotion is never constructed.
  Fix: restate as named conjecture; genus-1 obstruction in
  H²(grt^ell,...) is undefined in-chapter.
- **Modular 5→4 (l.497–530): IOU by citation-stretch.** BD04 §4.5 +
  TUY do not prove trace+clutching recovers a line category up to
  Morita. Fix: restate as named conjecture.
- **Determinant gerbe (l.157–159): UNDEFINED.** Used once, defined
  nowhere in the repo. Define precisely or name as hypothesis datum.
- Line/brane category `Line(A_b)`: no definition in-chapter; H4 demands
  it rigid braided (l.480–481); inconsistent with
  thqg_introduction_supplement_body.tex:134 (A^!-mod) vs l.295–296
  (A_b-modules). RECONCILE.
- `Z^der_ch` defined by fiat as C•_ch(A_b,A_b) (l.147–149);
  chart-independence asserted, not proved.
- Mixed-Ran factorization category def (l.72–121): axiom (iv) "local
  mixed-collision model governed by SC^{ch,top} operations" is a name,
  not an axiom.
- `thm:mr-vertical-dictionary` (l.806–893): theorem env wrapping a
  table; proof = "Each row is the named comparison theorem in the
  cited volume" (cross-volume IOUs).
- Theorem-H step (l.409–460) honestly admits dependence on
  `conj:ordered-twisted-tensor-acyclicity`.
- Bookkeeping liturgy: l.1156–1237 (numerical-signature status
  remarks), l.1239–1259 ("permanent rule") — rewrite as mathematics or
  excise.

### A4. Landscape census (`chapters/examples/landscape_census.tex`, ~6800 lines)

- **Five-archetype "classification": NOT a theorem (OPEN).** Headline
  ref `thm:archetype-shadow-classification` (census:416–417) resolves
  to a `\phantomsection\label{}` shim in main.tex:2242 (inside a block
  of ~313 such shims, "2026-05-17 second-pass sweep: 146 residuals");
  `def:archetype-shadow-depth` defined NOWHERE. Real result:
  `thm:quadrichotomy`
  (chapters/theory/shadow_tower_quadrichotomy_platonic.tex:447),
  Conditional, scoped to computed conductor-domain rows (G:5, L:2,
  C:4, M:10 at census:1385); class C inserted by fiat ("declare
  class(βγ_λ) := C"); archetype B a single external witness. Fix:
  repoint census refs to thm:quadrichotomy with honest finite-list
  scope.
- **Bershadsky–Polyakov central charge WRONG (FIXED in 2 files; see B5;
  propagation to ~5 more files + compute OPEN — see C1).**
- **Monster characters WRONG (OPEN).** census:6509–6525: H1(3A)=782
  (true McKay–Thompson coefficient 783 = 1+782 with χ_196883(3A)=782)
  and H1(3C)=1 (true 0: T_3C = j(3τ)^{1/3}, χ_196883(3C) = −1, so
  1+(−1)=0). The "proof" is incoherent. Fix values + proof coherently
  with the table's own definition of H1.
- **Lattice rank WRONG (OPEN).** census:652: "rank-3 lattice
  II_{2,2}⊕⟨2⟩" has rank 5 as written; intended likely II_{1,1}⊕⟨2⟩
  (rank 3). Check signature usage in context.
- **BCOV genus-2 reconciliation WRONG (OPEN).** census:6708–6714:
  claims conventions "differ by sign and a combinatorial factor of
  5/2"; actual ratio of 5/144 to 35/3456 is 24/7. Rewrite honestly;
  delete "rational constant of order 0.04".
- **κ-matrix internal contradictions (OPEN).** κ^Heis_ch: rank(g) at
  census:583 vs rank(g)·k at kac_moody.tex:202–203; κ_cat: 0-by-
  convention (matrix) vs dim g(k+h^∨)/2h^∨ (kac_moody.tex); census:
  732–741 decrees bare κ IS the κ^Hodge coordinate (κ(Vir_c)=c/2)
  while matrix row M sets κ^Hodge_ch = 0. Of 25 matrix entries, 19 are
  0-by-convention or "open"; only row B populated. Enforce one
  convention; write "open" where undefined.
- **Shadow tower attribution (OPEN).** census:1246–1255: S3=2,
  S4=10/[c(5c+22)], S5=−48/[c²(5c+22)] carry decorative
  "(Zamolodchikov 1985)"/"(BPZ 1984)" tags — those coefficients are
  not in those papers. Keep Zamolodchikov citation ONLY for the norm
  c(5c+22)/10. `prop:virasoro-shadow-canonical` defers derivation to
  an appendix; S3, S5 are the manuscript's own constructs — say so.
- **Numerology (OPEN, judgment needed).** W3 dims {0,2,5,16} fitted to
  a(n)=3a(n−1)+a(n−2)−1 then tabulated (census:4066–4081); sl3-hat from
  three data points (census:4705ff); "rank-plus-one pattern"
  (census:4572) rests on two families, one admitted wrong (Riordan
  R(5)=6≠5 at census:4193); Bruinier "Z/8 torsion" proof contains
  "lcm(2,4)·gcd(⋯)=8" (census:6601); "3+5=8 as evidence" (census:657)
  60 lines before such identities are called "N=1 coincidences"
  (census:604); "K=496 = dim E8×E8" garnish (census:3444). Excise or
  demote to explicitly-labelled empirical observations.
- **Bookkeeping leak (OPEN).** census:3020: "Pattern 218 of the
  first-principles cache" in manuscript prose.
- Verified CORRECT in census (do not "fix"): Sugawara c, dual Coxeter
  data incl. ϱ(E8)=121/126, ⟨Λ|Λ⟩=c(5c+22)/10, W3 coefficient
  16/(22+5c), Fateev–Lukyanov c(W_N) with K_N = 4N³−2N−2,
  βγ/bc ±2(6λ²−6λ+1), φ_{0,1}^{K3} coefficients (1,10,−64,108),
  wt(Δ5)=5, FP λ_g constants, Mukai II_{4,20}, c+=4, χ(K3)=24.
  Also: prior wrong S4=40/[...] already self-corrected at census:1238.

### A5. Compute layer (`compute/`: 1379 engines, 1637 test files)

Verdict: ~20–30% genuine, ~50% self-referential arithmetic, ~20% pure
theater. The `@independent_verification` decorator
(compute/lib/independent_verification.py:166) checks only that two
STRING LISTS don't overlap.
- `tests/test_theorem_A_bar_cobar_isomorphism.py:87–88`:
  `anchors_agree = True; assert anchors_agree`. Pure theater. REWRITE
  or delete.
- `lib/s5_virasoro_wick.py`: Gram entries HARD-CODED (l.163–165,
  `G_11 = 5*c_sym`) despite docstring claiming computation;
  `s3_from_three_point_arnold_residue` returns `Fraction(2)` (l.250);
  `lambda_channel_combinatorial_weight` returns `Fraction(-48,10)`
  (l.337) with `_perfect_matchings` never called. The one genuine step:
  sympy Schur complement → c(5c+22)/10. FIX: actually compute Gram
  entries from Virasoro commutation relations; call the enumerator.
- `tests/test_kappa_conductor.py:165–179`: comment admits check fails,
  then `kappa_H1 = 1; neg_c_ghost_H1 = 1; assert`; l.192–193
  `kappa_Vir = 26; assert kappa_Vir == 26`. REWRITE.
- `test_chirhoch_dimension_engine.py` + `chirhoch_heisenberg()`
  (lib:304–334): hard-coded dims (1,1,1) + greps that strings appear in
  the manuscript. Pure circularity. REWRITE.
- GOLD STANDARD to imitate: `lib/bar_modular.py` /
  `test_bar_modular.py` — sl3 CE differential as explicit matrices mod
  p ∈ {5,7,11}, d²=0 verified, H*(sl3) = Λ(x3,x5) matched against the
  classical answer. This test can actually fail.
- 46 test files contain hard-coded-True patterns; 86 self-describe
  comparison against "manuscript" values. Systematic rewrite required:
  make every "derivation" function compute from commutation relations.
- BP constants in compute/ still encode the OLD WRONG values
  (196, 98/3, c=2−24(k+1)²/(k+3)) — must be updated to corrected
  values (see C1) or tests will contradict the fixed manuscript.

### A6. Vol I bibliography (`bibliography/references.tex`, ~885 entries)

- FIXED (see B1/B2): FernandezCostelloP24, BittlestonCostello25,
  HerNeg24, CIKLP-Winfty-Universal, SheltonYuzvinsky1997, AvE23,
  Positselski2018 year→2019, GLZ22 article number→109791,
  Manin1991ThreeFoldedMotivicDualiy (excised + prose fixed at
  arithmetic_shadows.tex:14749), Nish26 + Nishinaka25 (phantoms,
  excised; all sites repointed), Williams17Virasoro added,
  Sridharan61 added.
- **OPEN: 113 dangling cite keys** used in chapters/ with no bibitem.
  Known: Borcherds92, Borcherds95, CG21, CostelloGwilliam,
  KazhdanLusztig1993, KazhdanLusztig1994, Zam85, FF82, CKL20,
  ArakawaFasquel23, Sugawara1968, plus a ~40-key Siegel-modular/K3
  cluster (Igusa64, Humbert1899, Tsushima80, ...). Regenerate the list
  (extract \cite keys, diff against \bibitem keys), add verified
  entries; do NOT invent.
- **OPEN: remaining "inferred from key naming" stubs** (self-declared
  machine-inferred block at old lines 2519–2598):
  Ibukiyama1998Paramodular ("manuscript"), GaberdielHohenegger2013
  ("conference proceedings"), Kachru2017ms, DongMason94 (venue-less),
  COZZ26 ("Preprint 2026", uncited), Kapranov15 ("preprint 2015",
  uncited), HJ12 ("personal communication"). Verify each via web
  search; complete or excise.
- 185 entries never cited (mostly deliberate aliases; harmless).
- Unverifiable but plausible, LEFT IN PLACE: Vic25/Vicedo25 (B. Vicedo,
  "Full universal enveloping vertex algebras from factorisation",
  preprint 2025, no arXiv ID), CM25 (Casarin–Maffei), Moriwaki26a
  (arXiv:2602.08729), CFG25 (arXiv:2602.12412 — verified real by the
  Vol II audit). Verify Vic25/CM25 when possible.

### A7. Vol II audit (`/Users/raeez/chiral-bar-cobar-vol2`) — ALL OPEN

Structure: 8 parts, 108 files/222k lines in build (63k quarantined
notes NOT in build). Status tags: 1533 ProvedHere, 318 Conditional,
151 Conjectured. Every headline theorem is Conditional.

- **FALSE FORMALITY INPUT (top priority).**
  chapters/theory/sc_chtop_heptagon.tex:2205–2231,
  `prop:heptagon-edge-34`, stamped ProvedHere via "Swiss-cheese
  formality of Kontsevich–Tamarkin" + "coloured Swiss-cheese formality
  map (Getzler–Jones 1994, coloured variant via Vallette 2014)".
  The Swiss-cheese operad is NOT FORMAL: M. Livernet, "Non-formality
  of the Swiss-cheese operad", J. Topology 8 (2015) 1156–1166 (see
  also Idrissi). Getzler–Jones 1994 cellular model famously flawed.
  Volume never cites Livernet's non-formality. This edge is the
  load-bearing globalisation step in `thm:chd-deligne-tamarkin`
  (chiral_higher_deligne.tex:415–423) feeding clause (1) of the climax
  `thm:chiral-higher-deligne` (chiral_higher_deligne.tex:463).
  FIX: state Livernet's theorem; rewrite to the strongest true
  statement (per-colour Tamarkin formality + whatever the argument
  genuinely gives); restamp; propagate to consumers.
- **Master theorem assumes its conclusion.**
  chapters/connections/programme_climax_platonic.tex:127
  (`thm:universal-holography-master`): the datum Ξ includes as
  hypotheses the CG BV model, the boundary quasi-iso η^∂, AND the
  bulk–Hochschild comparison χ_{HT,A} (l.148–166); the proof
  (l.1012–1110) erects three "pillars" and concludes "Their
  intersection is the chain-level comparison χ_{HT,A}" — no map
  constructed; "intersection" is a metaphor; text concedes at l.253.
  Also the convergence pillar cites β_{W_N}=12(H_N−1) which is
  `conj:beta-N-harmonic-closed-form` (cited at l.1030–1035) while W_N
  for all N is in the theorem's scope. FIX: honest conditional
  restatement (pillars = consistency evidence, not existence proof).
- **Coherences by remark.** `prop:chd-stasheff-4`
  (chiral_higher_deligne.tex:326–350) verifies exactly two brace
  identities; `rem:chd-stasheff-higher-degree` (352–374) declares all
  higher degrees "follow by the same template". The McClure–Smith
  cell-by-cell combinatorics is missing — this is where the actual
  Deligne-conjecture content lives. OPEN.
- **Under-defined foundational object.** `def:chd-alg` (121–146):
  RHom over a "chiral endomorphism operad" in an unspecified category;
  `def:chd-geom` (148–163) places Hom(A^⊠k,A) on FM_k(C) while A lives
  on X; `prop:chd-models-equivalent` compares two ill-defined objects.
  OPEN.
- **Status inflation.** `cor:rung-heisenberg` stamped ProvedHere while
  assuming hypAbelianHTBV+hypTLift → restamp Conditional.
  `bar-cobar-review.tex:3105–3141`: "one-loop exact BV-BRST ⇒ chirally
  Koszul" via an unconstructed "loop-order spectral sequence" that
  "degenerates at E2". OPEN.
- 3d gravity Part VI self-admits "the physical partition-function
  bridge [is] conjectural" (3d_gravity.tex:52–60) — ensure labels
  match throughout.
- Composition estimate: ~10–15% rigorous self-contained proof, ~30–35%
  conditional IOUs, ~35–40% survey/restatement, ~10–15% status
  bookkeeping ("Status/licensing tags α+β+γ+δ" apparatus pervasive —
  voice sweep needed).
- Genuine novelty candidates (all unfinished): (i) chiral braces on
  chiral Hochschild complex via FM_k(C) log-forms with Stokes
  homotopies (coherent only to degree 4); (ii) two-coloured cobar
  obstruction class [o_oc]; (iii) Banach-radius numerics β_Vir=6,
  β_{W_N}=12(H_N−1) (conjectural N≥4).

### A8. Vol II bibliography (in main.tex lines 2773–4840; ~663 entries) — FIXES SPECIFIED, NOT YET APPLIED

Apply these corrected bibitems in /Users/raeez/chiral-bar-cobar-vol2/main.tex:

1. `GGW21` (main.tex:2877) misattributed+fake venue → replace with:
   `B.~R.~Williams, \emph{Renormalization for holomorphic field theories}, Comm.\ Math.\ Phys.\ \textbf{374} (2020), no.~3, 1693--1742, arXiv:1809.02661.`
   ALSO fix prose "Gwilliam–Grady–Williams structures" at
   chapters/theory/axioms.tex:624 → Williams.
2. `GrRW22` (main.tex:2902) fabricated chimera → replace with:
   `O.~Gwilliam, E.~Rabinovich, and B.~R.~Williams, \emph{Quantization of topological-holomorphic field theories: local aspects}, arXiv:2107.06734.`
   (E. Rabinovich, not "V.").
3. `GKW25` (main.tex:2883) wrong paper (2312.16573 is
   Sharapov–Skvortsov–Van Dongen) → replace with:
   `D.~Gaiotto, J.~Kulp, and J.~Wu, \emph{Higher operations in perturbation theory}, J.\ High Energy Phys.\ \textbf{2025} (2025), no.~5, 230, arXiv:2403.13049.`
   (Becomes an alias of GKW24/GKW2025 — consider consolidating. Cited
   at fm-calculus.tex:1291, raviolo.tex:822,888.)
4. `BittlestonCostello25` (main.tex:3446) wrong title+initial → the
   cite sites (holomorphic_topological.tex:1008,1158,1214, "lift to
   eleven dimensions") want Raghavendran–Saberi–Williams:
   `S.~Raghavendran, I.~Saberi, and B.~R.~Williams, \emph{Twisted eleven-dimensional supergravity}, Comm.\ Math.\ Phys.\ \textbf{402} (2023), 1103--1166, arXiv:2111.03049.`
5. `BittlestonCostelloZeng24` (main.tex:3449) wrong title → 
   `R.~Bittleston, K.~Costello, and K.~Zeng, \emph{Self-dual gauge theory from the top down}, arXiv:2412.02680, 2024.`
6. `HR09` (main.tex:3515) fabricated placeholder, never cited → delete
   or replace with Hellerman–Schmidt-Colinet, *Bounds for state
   degeneracies in 2D CFT*, JHEP 08 (2011) 127, arXiv:1007.0756.
7. `Mok2025` (main.tex:3139) wrong author "C.-P. Mok" → Siao Chi Mok
   (arXiv:2503.17563); or delete (never cited; Mok25 at 3136 correct).
8. `FV20` (main.tex:2933) unverifiable Fresse–Vallette → cited at
   spectral-braiding-core.tex:4157,4330 for Koszul-operad convolution
   where LV12 (cited alongside) suffices; swap cites to LV12, delete
   entry (or verify the intended Fresse–Willwacher paper first).
- Unverifiable placeholders: GZ26 (main.tex:2898; cited
  dnp_identification_master.tex:230,327), COZZ26 (3177; cited
  dg_shifted_factorization_bridge.tex:27), Nish26 (3375; cited AS A
  THEOREM ATTRIBUTION at thqg_gravitational_complexity.tex:1792 —
  apply the same BD04 §3.7 / CG17 repair as Vol I),
  CostelloLi2020 key/year mismatch (entry is 2016 arXiv:1606.00365;
  triplicated as CL16, Costello-Li19).
- 35 dangling cite keys (~50 citations). Top: CreutzigLinshaw2019 (3),
  Felder1995 (2), Feh23 (2), DMVV1997 (2), DabholkarMurthyZagier2012
  (2), Yang1967, Schwinger1951, OguisoSakai2001, MorrisonVafa1996II,
  Mor26. Alias misses: MaloneyWitten→MW10,
  KontsevichSoibelman2011→kontsevich-soibelman,
  Costello2011→costello-renormalization, Fehily23/Feh23,
  ES98/EtingofSchiffmann1998, CG16→CG17. Lists saved by the audit
  agent in its scratchpad as dangling.txt/nevercited.txt (scratchpad
  may be gone; regenerate by diffing \cite keys vs \bibitem keys).
- One duplicate key Ara07 (second copy commented at 3822). No
  McClure–Smith or Kajiura–Stasheff entries exist despite the
  Deligne/OCHA content — add them.

### A9. Vol III audit (`/Users/raeez/calabi-yau-quantum-groups`) — FIX LIST SPECIFIED, NOT YET APPLIED

- **κ_BKM circularity.**
  chapters/examples/cy_d_kappa_stratification.tex:2171–2209
  (`thm:borcherds-weight-kappa-BKM-universal`): the theorem statement
  contains "κ_BKM(Φ_N) := c_N(0)/2" — its own conclusion as a
  definition; proof body (~2220) "κ_BKM is by definition the weight
  of Φ_N" + Borcherds Thm 13.3 (wt = c(0)/2) = Definition∘Citation.
  Also cy_d:2326, k3e_bkm_chapter.tex:348 (file concedes κ_BKM "is not
  a modular characteristic of any constructed chiral algebra").
  FIX: Definition (κ_BKM := wt(Φ)) + Theorem ProvedElsewhere
  (Borcherds 1998 Thm 13.3; Gritsenko 1999 Thm 1.2: wt = c(0)/2);
  delete the novelty claim at 2182–2185; same demotion for
  `thm:k3e-universal-kBKM-two-scopes` (k3e:1619).
- **N≥2 ladder FALSE + internally contradictory.**
  k3e_bkm_chapter.tex:1624–1650 claims (c_N(0)) = (10,8,6,4,2),
  κ = (5,4,3,2,1) for N ∈ {1,2,3,4,6}, attributing weights "3,2,1" to
  Govindarajan–Krishna — misattribution. Internal 3-way conflict at
  N=2: Scope A says c2(0)=8/κ=4 (echoed cy_d:2198–2199); Scope B
  (Gritsenko–Cléry row (1,2;3), k3e:1636–1650) gives weight 3,
  c(0,0)=6; conj:ez-n2-2A-decomposition (k3e:~1811–1815) gives
  c^{2A}(0,0)=4 → κ=2. CORRECT VALUES (Jatkar–Sen;
  Govindarajan–Krishna arXiv:0907.1410, JHEP 05 (2010) 014):
  weights (5, 3, 2, 3/2, 1), i.e. c_N(0) = (10, 6, 4, 3, 2); N=4 is
  HALF-INTEGRAL (weight 3/2, square-root denominator) — so also delete
  "each Φ_N has integral weight" and "strictly monotone decreasing"
  (k3e:1631). Error mechanism at cy_d:2199: 8 is the half-sum of the
  1^8 2^8 frame shape (= weight of η(τ)^8η(2τ)^8 = k(2)+2), not the
  constant term of the Jacobi input. The "naive decomposition fails"
  argument survives with κ=3 vs 1 at N=2 — recompute. Reconcile the
  2A conjecture with the GC cusp-weighted sum (on Γ0(2) the weight
  formula input is the cusp-weighted sum, GC Thm 3.1; cf.
  cy_d:2323–2330).
- **BV-residue fake derivation.** k3e:1696 `thm:bl-bv-k3e-kappa5`:
  k3e:1722 admits "The residue ... is this weight normalisation, not
  a vanishing order" — the value 5 inserted, not derived. Demote to
  remark/heuristic or supply the residue computation.
- **Self-citing theorem.** quantum_group_reps.tex:1377–1398
  (`thm:chiral-qg-equiv-vol3`): (a) stated on "Kosz^ord(X)" — used
  once in the repo, never defined; (b) proof appeals to "MC3"/"five-
  family mechanism", absent from the volume's theory chapters;
  (c) l.1396–1397 "(Vol I \ref{thm:chiral-qg-equiv-vol3})" — the
  theorem CITES ITSELF. The coproduct-reconstruction step is admitted
  open at rem:yangian-forgetful-arrow (683–697). FIX: define the
  locus (pattern: Vol I def:chiral-koszul-pair,
  chiral_koszul_pairs.tex:975), remove self-ref, status Conjectured
  at full strength with the proved sub-case separated.
- **KL relabel.** quantum_groups_foundations.tex:531–543: proof body
  `\begin{proof}[Attribution]` — nothing chiral verified. Restate as
  Kazhdan–Lusztig (J. AMS 1993–1994) ProvedElsewhere + chiral upgrade
  as the open step.
- **Compute by fiat.** compute/lib/borcherds_lift.py:143–145:
  `return c_table.get(0,0)/2.0` encodes the identity; tests cover N=1
  only. FIX: compute weight independently from frame-shape half-sums;
  test wt == c(0)/2 across N ∈ {1,2,3,4,6} with (5,3,2,3/2,1).
- Claim-status macros nearly absent volume-wide (3 occurrences vs 807
  theorem envs; 313 conjecture envs) — the theorem/conjecture boundary
  is carried by prose only. Systematic labelling pass needed.
- Vol III cite-check was interrupted mid-run after finding "three
  garbled entries" (identities not recorded before kill) — RERUN the
  Vol III bibliography audit from scratch.

### A10. Cross-cutting / direct findings

- **Theorem D chain bottoms out honestly-but-thinly:**
  thm:universal-generating-function (genus_expansions.tex:2054) →
  thm:genus-universality (higher_genus_foundations.tex:7669) →
  prop:scalar-obstruction-hodge-euler (higher_genus_foundations.tex:
  6640), whose own Remark (6673–6700) admits: under the K-theoretic
  definition the identity obs_g = κλ_g reduces to the unconditional
  ch_g(λ_{-1}(E)) = (−1)^g c_g(E) (classical GRR/Mumford), and the
  substantive content is exactly what the scalar-diagonal hypothesis
  (def 6612, "a genuine hypothesis" for non-abelian KM) assumes. The
  generating function κ((x/2)/sin(x/2)−1) is κ × the PROVED
  Faber–Pandharipande λ_g integral. Honest framing exists in-file;
  ensure every downstream quotation of Theorem D carries the
  scalar-diagonal/uniform-weight scope.
- **Verlinde "recovery" (higher_genus_modular_koszul.tex:38537)**:
  standard TUY/Verlinde mathematics (S-matrix table arithmetic
  verified correct) wrapped in a hypothesized-but-unconstructed
  "ordered-chain-to-TUY comparison morphism". The comparison morphism
  is the actual open mathematics.
- **313 phantomsection label shims in main.tex (~2200–2344)**: fake
  anchors for broken refs. Inventory which are referenced; repoint to
  real theorems or restate claims without fake refs.
- **Vol I file `chapters/theory/higher_genus_modular_koszul.tex`** is
  45,307 lines with one \section spanning 27,500 lines — structural
  pathology; long-term: split.
- LaTeX environment balance verified OK on all files edited this
  session; pre-existing mismatch in concordance.tex (331 begin / 332
  end, present in HEAD — likely an end{ inside a comment; harmless
  but check).

---

## PART B — FIXES ALREADY APPLIED (uncommitted, working tree, verify with git diff)

B1. Vol I references.tex: 7 garbled entries fixed (FernandezCostelloP24
    → Costello–Li arXiv:1606.00365 with key-retained comment;
    BittlestonCostello25 → RSW CMP 402 (2023) 1103–1166,
    arXiv:2111.03049; HerNeg24 → D. Hernandez, IMRN 2023 no. 13,
    arXiv:2010.06996 [prose at yangians_computations.tex:4423
    "Hernández–Neguț" → "Hernández"]; CIKLP-Winfty-Universal →
    Linshaw, Compos. Math. 157 (2021) 12–82, arXiv:1710.02275;
    SheltonYuzvinsky1997 → B. Shelton & S. Yuzvinsky, JLMS (2) 56
    (1997) 477–490 correct title; AvE23 → Arakawa–van Ekeren, JEMS 25
    (2023), arXiv:1905.11473; Positselski2018 year → 2019; GLZ22 →
    article no. 109791). Manin1991ThreeFoldedMotivicDualiy excised
    (entry + prose at arithmetic_shadows.tex:14749 + index line).
B2. Phantom Nishinaka purge (Vol I): bibitems Nish26 + Nishinaka25
    removed; ~25 cite/prose sites across
    higher_genus_modular_koszul.tex, concordance.tex, free_fields.tex,
    nonlinear_modular_shadows.tex, guide_to_main_results.tex,
    outlook.tex (index), chiral_hochschild_koszul.tex,
    frontier_modular_holography_platonic.tex repointed to
    \cite[\S3.7]{BD04} / \cite{CG17} / \cite{Williams17Virasoro} /
    \cite{Vic25,Vicedo25}; "Nishinaka envelope" → "factorization/
    chiral envelope"; "Nishinaka admissibility" → "bounded-pole
    admissibility"; concordance §retitled "Factorization envelopes of
    Lie conformal algebras". Williams17Virasoro bibitem added (LMP 107
    (2017) 2189–2237, arXiv:1603.02349). NOTE: grep confirmed zero
    remaining "Nishinaka|Nish26" in Vol I; Vol II still has its own
    Nish26 (see A8).
B3. chiral_hochschild_koszul.tex: false d_dR(η12) identity → Stokes
    boundary mechanism with restriction identity η13|D12 = η23|D12;
    semicontinuity direction fixed; Goncharova statement fixed;
    Whitehead → Sridharan61 (bibitem added after Priddy1970);
    Clifford degree-1 argument rewritten (parity + inner charge
    derivation via J = :ψψ*:); Fresse2017 → LV12 (4 sites).
B4. theorem_A_infinity_2.tex: FG credit restored (7 substitutions);
    \ref{lem:R-twisted-descent} → \ref{lem:R-twisted-descent-unitary}
    (replace-all); \ref{def:symmetric-bar} → \ref{def:geometric-bar};
    Step 2 rewritten to name standing hypotheses as hypotheses;
    "(Francis HA appendix; Lurie HA §5.5)" → Lurie only;
    h_LV/N(A_b) proof: false LV-normalization claim replaced by honest
    statement of the open obligation (Frontier F1†), Theorem-H
    circular import removed, "§Essential constants" config-file leak
    removed, Zamolodchikov norm attributed to direct Gram-matrix
    computation.
B5. Bershadsky–Polyakov correction, APPLIED ONLY IN
    bershadsky_polyakov.tex + landscape_census.tex (grep-verified 0
    remaining "196" in both):
    c(k) = −(2k+3)(3k+1)/(k+3) = 25 − 6(k+3) − 24/(k+3)
    [KRW minimal: c = 8k/(k+3) − 6k − 1]; K^c = 50; κ+κ' = 25/3;
    c* = 25 at k = −3±2i; image c ≤ 1 (k>−3), c ≥ 49 (k<−3), gap
    (1,49); k=−3/2 gives c=0; σ^(2) = 25; dual quartic denominator
    (50−c)(272−5c); pole pairs (0,50), (−22/5, 272/5); unified sl3
    shift formula rewritten: c = c0 − b(k+3−s)²/(k+3) with
    (c0,b,s) = (2,24,1) principal / (1,6,2) minimal,
    K = 2c0 + 4bs ∈ {100, 50}; BP shape = s=2 translate of Virasoro
    1 − 6(t−1)²/t; Verdier bucket {0,13,250/3,25/3} (+8 with B row);
    landmark conductors {0, 2dim g, 0, 26, 100, 50, 48};
    "98/3 from Arakawa–Fasquel" → 25/3.

---

## PART C — REMAINING WORK QUEUE (resume here; agents were killed mid-flight)

C1. **BP propagation (Vol I).** Apply B5's corrected values to:
    chapters/theory/higher_genus_complementarity.tex (~59, 3848–3863,
    7317–7318); chapters/theory/universal_conductor_K_platonic.tex
    (~1113–1215; K_ghost^leg = −6(4k²+9k+3)/(k+3) is a separate
    invariant — verify separately, don't blindly change);
    chapters/theory/ordered_associative_chiral_kd.tex (~4120–4123);
    chapters/theory/chiral_center_theorem.tex (~3037–3151);
    chapters/connections/concordance.tex (grep); then repo-wide grep
    for 196 / 98/3 / 49/3 / 24(k+1)² in BP contexts (SKIP 196884,
    year-1968, and W3-PRINCIPAL values — W3's c≤2 / c≥98 / K=100 are
    CORRECT); w_algebras.tex + w_algebras_deep.tex may also quote BP.
    Then compute/: update BP engines/tests and run them.
C2. **Census factual fixes** (A4 items: Monster characters, lattice
    rank, BCOV 24/7, quadrichotomy repointing, shadow-tower
    attributions, κ-matrix convention enforcement vs kac_moody.tex,
    Pattern-218 excision, numerology demotions).
C3. **master_reconstruction.tex honesty repair** (A3 items).
C4. **Vol II repairs** (A7: Swiss-cheese/Livernet fix + propagation;
    master-theorem honest restatement; cor:rung-heisenberg restamp;
    Stasheff-coherence gap statement) and Vol II bibliography (A8 —
    fully specified, mechanical).
C5. **Vol III repairs** (A9 — fully specified) and RERUN Vol III
    bibliography cite-check (interrupted; 3 unrecorded garbled entries
    found before kill).
C6. **Vol I dangling bib keys** (A6: 113 keys + inferred stubs).
C7. **Compute-layer rewrite** (A5: kill assert-True theater; make
    hard-coded "derivations" compute; model on bar_modular.py).
C8. **Voice / de-scaffolding sweeps** (the standing user goal):
    every manuscript file in all three volumes must read as if written
    by Costello/Gaiotto/Witten/Polyakov/Gelfand/Etingof/Dirac — pure
    mathematics and physics; zero project-management vocabulary.
    Contamination signatures to grep (skip % comments):
    "first-principles cache", "cache entry|pattern", "Pattern [0-9]",
    "AP[0-9]", "MA-[0-9]", "Wave [0-9]", "round [0-9]", "batch",
    "swarm", "attack-heal", "rectif", "CLAUDE", "session", "TODO",
    "FIXME", "dashboard", "status table", "licensing tag",
    "Frontier F[0-9]", "FRONTIER", "repo(sitory)?", "inscri(be|ption)",
    "we now turn to", "having established", "let us now",
    "this brings us to", "it is worth noting", "notably,",
    "crucially,", "remarkably,", "furthermore,", "moreover,",
    "in the present work", "2026-05-17", "second-pass sweep",
    "residuals surfaced". Rules: restate process references as direct
    mathematics or delete pure narration (quote deletions); never
    delete mathematics/hypotheses/formulas/claim-status macros;
    rewrite rather than remove when in doubt. Regions and exclusions
    used by the killed fleet (all now unowned): Vol I theory / Vol I
    connections+frame+appendices (incl. the 313 main.tex shims and
    editorial_constitution.tex build-status check) / Vol I examples
    A–L and M–Z / standalone/ (extra rules: no cross-volume refs, no
    ClaimStatus macros in submission-ready papers; check
    survey_modular_koszul_duality.tex vs _v2.tex duplication) /
    Vol II theory / Vol II rest / Vol III chapters.
C9. **Consistency pass after C1–C8**: rebuild all three volumes
    (Vol I: pkill pdflatex; make fast. Vol II: make. Vol III: make
    fast), fix compile breaks, run make integrity / audit / census
    where defined, and re-verify no stale constants (grep the
    corrected-value tables above).

## PART D — STRUCTURAL VERDICT (for orientation, not action)

The manuscript's real load-bearing assets: the tangential-log-curve /
real-oriented-blowup foundations (precise), the ordered bar sign
conventions, the R-twisted descent construction, the census's
classical data (mostly correct), the FP/GRR scalar lane of Theorem D
(classical but correctly assembled), bar_modular.py-style genuine
computations, and an unusually honest hypothesis-package apparatus.
The recurring failure mode: substantive content moved into hypothesis
packages/definitions whose discharge is the actual open mathematics;
plus fabricated citation decoration and (in spots) outright false
identities, now partially excised per Part B. The five theorems'
honest statuses after audit: A conditional-on-unconstructed-ambient;
B not audited in depth this session (raw class-M falsity already
documented in-repo); C0/C1 conditional, C2 package-gated;
D proved on the scalar-diagonal lane (classical GRR + FP) and
hypothesis-gated beyond; H effectively conjectural (engine =
named open conjecture; concentration contradicted by the
De Sole–Kac literature unless the Koszul-locus scope genuinely
escapes it — this is the single most important unresolved
mathematical confrontation in Vol I).
