# Wave-7 AP-CY Catalog Audit — integrity of notes/cross_volume_aps.md

Date: 2026-04-18. Author: Raeez Lorgat. Status: **DIAGNOSTIC, NO EDITS**.

## Executive summary

Audit of the AP-CY1..AP-CY67 catalog as metacognitive-layer object (not the
mathematics it describes). Three findings:

1. **Catalog file exists and is non-phantom.** CLAUDE.md's pointer
   "See notes/cross_volume_aps.md for AP-CY1..AP-CY61" resolves to a
   154-line file containing AP-CY1..AP-CY67 (plus V2-AP1..V2-AP39).
   The pointer is stale on count (says AP-CY1..AP-CY61, actual is
   AP-CY1..AP-CY67) — minor AP271 reverse-drift.

2. **AP-CY numbering is contiguous (no gaps, no duplicates).**
   AP-CY1..AP-CY67, every index inscribed, no "(reserved)" slots.
   AP-CY1..AP-CY61 are one-paragraph entries; AP-CY62..AP-CY67 carry
   explicit `### AP-CY##` headers + triggers subsection. Heterogeneous
   format but complete.

3. **Two uncatalogued findings from this session's waves.**
   (a) Wave-4 Vol III CY-D stratification surfaced AP289 (Künneth-
       multiplicative vs additive); now inscribed in main CLAUDE.md
       AP289, but NOT in cross_volume_aps.md as AP-CY68.
   (b) Wave-6 κ_ch(K3×E) retraction campaign discovered TWO DISTINCT
       κ_ch invariants sharing the symbol — Route A (Hodge supertrace,
       Künneth-multiplicative, Ξ(K3×E)=0) and Route B (Heisenberg
       rank, additive under free-boson product, κ(K3×E)=3). Programme
       elects Route A canonical at `cy_d_kappa_stratification.tex:
       414-426` but 20+ Route B consumer sites remain unpropagated.
       Not catalogued as an AP-CY entry anywhere.

## AP-CY inscription-status table

Audited entries sampled for (a) body present, (b) canonical-violation
cite resolves, (c) counter/heal procedure inscribed.

| AP-CY | Title | Body | Counter | Notes |
|---|---|---|---|---|
| 1-5 | CY dim, trace, E_2, center, KL | Y | Y | One-liner taxonomic, no file:line |
| 6 | A_X CY3 inf-cat existence | Y | Y | Updates status post-April 2026 |
| 7-10 | CoHA, Borcherds, Jacobi, flop | Y | Y | AP-CY9 has concrete numerical check |
| 11-15 | Transitivity, part-refs, G(X), README | Y | Y | AP-CY14 explicitly scoped |
| 16-20 | Matrix quotients, MF, theta, A-hat, N bundle | Y | Y | Numerical disciplines |
| 21-25 | E_3 bar, Miki, E_1 bialgebra, docstring, R-matrix | Y | Y | AP-CY21 resolution noted |
| 26-30 | Verdier, sandbox, pole-unsafe, wrong-repo, factored | Y | Y | Operational hazards |
| 31-35 | Spectral-z, reorg, chain-level, κ_ch≠χ, B^(j) | Y | Y | AP-CY34 has 76 tests cited |
| 36-40 | κ_ch formula, κ_BKM coincidence, class M, incompat, ProvedHere | Y | Y | |
| 41-45 | Partial updates, normalization, tautology, CY-D false, N=2 | Y | Y | |
| 46-50 | No CY_4 Yangian, Mukai rank, 3d→6d, tautological tests, duplicate agents | Y | Y | |
| 51-55 | Rate-limit, mega-file, π_1 Conf, center ≠ averaging, κ_cat topological | Y | Y | AP-CY55 load-bearing |
| 56-60 | E_n conflation, narration, E_n scope, algebraizations, six routes | Y | Y | AP-CY57/CY61 anti-slop |
| 61 | Shallow correction | Y | Y | Meta-discipline |
| 62-67 | Geometric vs algebraic models | Y (full) | Y (triggers) | Rich format |

**Inscribed count: 67/67.** **Phantom (reserved / empty): 0.**
**Full body + trigger format: 6 (AP-CY62..AP-CY67).**
**Compact format: 61 (AP-CY1..AP-CY61).**

## Cross-check CLAUDE.md capsule vs primary catalog

CLAUDE.md §"Geometric vs Algebraic Model Conflations (AP-CY62--AP-CY67)"
reproduces operational capsules for AP-CY62..AP-CY67. Side-by-side check:

- AP-CY62 capsule ("specify geometric (FM) vs algebraic (bar/operadic)")
  agrees with catalog entry.
- AP-CY63 ("End^ch is algebraic, not on FM") agrees.
- AP-CY64 ("HH*(Weyl)=1-dim; Theorem H has no THH analogue is FALSE")
  agrees.
- AP-CY65 ("Yangian has spectral params via evaluation modules") agrees.
- AP-CY66 ("BZFN uses same S; two centers from two algebras") agrees.
- AP-CY67 ("spectral params are formal algebraic, FM enters via
  comparison") agrees.

**No AP271 reverse-drift between capsule and primary entries on AP-CY62..67.**

## Pointer-count drift (minor AP271)

CLAUDE.md line: "AP-CY1..AP-CY61" — stale. Actual catalog contains
AP-CY1..AP-CY67. Two non-load-bearing citations of the stale count
appear in CLAUDE.md top-matter ("Vol III (~693pp): ... See Vol III
CLAUDE.md and notes/cross_volume_aps.md for AP-CY1..AP-CY61.") and in
the Vol III cross-awareness section. Heal: update to AP-CY1..AP-CY67.

## Uncatalogued findings from current session

### Gap-1: AP289 Künneth-multiplicative not catalogued cross-volume

- Inscribed in Vol I CLAUDE.md as AP289 (general AP catalog).
- NOT inscribed in `notes/cross_volume_aps.md`.
- Subject matter is strictly Vol III (Hodge supertrace, Künneth on
  compact CY_d). Belongs in AP-CY catalog as AP-CY68.
- Recommendation: add AP-CY68 "Künneth-multiplicative Hodge supertrace"
  mirroring AP289 wording, citing `cy_d_kappa_stratification.tex`
  healed sites.

### Gap-2: κ_ch Route A / Route B collision

- Discovered Wave-6 2026-04-18 (this session).
- Two canonical κ_ch invariants share the symbol: Hodge supertrace
  (Route A, Künneth-multiplicative) and Heisenberg rank (Route B,
  additive under free-boson product).
- Programme elects Route A at `cy_d_kappa_stratification.tex:414-426`;
  20+ Route B consumer sites remain unpropagated across
  `k3_chiral_algebra.tex`, `k3e_bkm_chapter.tex`, `k3e_cy3_programme.tex`,
  `quantum_group_reps.tex`, `modular_koszul_bridge.tex`, engine tests.
- Nearest catalog neighbours: AP-CY55 (κ_cat topological vs
  algebraization), AP234 (two-Koszul-conductors-same-letter κ+κ^! vs K).
  Class is AP234-like: two distinct mathematical objects share symbol.
- Recommendation: add AP-CY69 "Two κ_ch conventions (Route A Hodge
  supertrace canonical; Route B Heisenberg rank legacy)" with heal
  = either (i) propagate Route A rewrite across 20+ sites, or
  (ii) retain Route B as `κ^{Heis}_k` explicitly, reserving bare
  κ_ch for Route A.

### Gap-3 (low priority): BCOV-Yukawa κ^{(d)} 19-site collision

Wave-5 κ-discipline sweep referenced per mission brief. Not located
in this session's adversarial_swarm files (grep returns 0). Either
(a) belongs to an earlier session, or (b) mission brief reference is
slightly misdated. Skip unless independently surfaced.

## Heal recommendations (commit plan, not executed)

1. **Pointer refresh**: update CLAUDE.md AP-CY1..AP-CY61 → AP-CY1..AP-CY67
   at the two non-load-bearing sites. Trivial, `sed`-safe.

2. **Inscribe AP-CY68 (Künneth)**: mirror AP289 into
   `notes/cross_volume_aps.md` after AP-CY67, using the full
   `### AP-CY68` header format matching AP-CY62..CY67.

3. **Inscribe AP-CY69 (Route A/B κ_ch collision)**: new entry after
   AP-CY68, documenting the two-convention split, naming
   `cy_d_kappa_stratification.tex:414-426` as canonical anchor,
   listing the 20+ consumer sites needing either Route A rewrite
   or explicit Route B relabelling as `κ^{Heis}_k`.

4. **(Deferred to a future wave)**: execute the Route A propagation
   across the 20 `.tex` files + 3 engines. This is the 200+ edit
   campaign flagged but not applied by the Wave-6 retraction note.

## No commits this session

Per mission brief: diagnostic audit only. No edits to
`cross_volume_aps.md`, CLAUDE.md, or any `.tex` file. Commit plan above
is queued for a subsequent wave where the scope is explicitly the
AP-CY catalog extension.
