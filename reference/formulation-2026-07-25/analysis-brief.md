# Analysis brief — Chiral Koszul duality: new formulation vs. legacy manuscript

Author of all material: Raeez Lorgat.

## What this bundle is

Two artifacts covering the same subject, at very different levels of correctness.

**A. The new formulation** (`01_new_formulation/`) — *Chiral Koszul Duality:
Noncommutative Factorisation D-Modules, Ordered Quantum Fields, and the Geometry
of Defects*, 198 pages, July 2026. Primitive object: an augmented $E_1$-algebra
in factorisable right D-modules on a smooth complex curve $X$. This is the
current, correct formulation.

**B. The legacy manuscript** (`02_`–`05_`) — Volume I of a three-volume
programme, ~413,000 lines of LaTeX across 156 files, plus a Python compute
engine (~500 modules, ~119K tests). Written under an architecture ("the Open
Beilinson tower", five theorems A/B/C/D/H, a five-archetype classification, a
$5\times5$ $\kappa$-matrix) that the new paper supersedes and in several places
explicitly retracts.

The bundle exists so the two can be compared and the salvageable content of B
identified and re-derived under A's corrections.

## The structural corrections A makes to B

These are not stylistic. Each is a category error in B that A fixes.

1. **The bar is transverse.** A §1.5: $\mathrm{Bar}^{\mathrm{ord}}_X(A) =
   \mathbf 1 \otimes^L_A \mathbf 1 = \int_{([0,1],\partial[0,1])} A$. The chiral
   coefficient is *not* contracted; no logarithmic residue is asked to produce a
   pole. The de Rham differential of a configuration space, the residue
   differential along a collision divisor, and the simplicial bar differential
   are three distinct operators. B's canonical statement places
   $B^{\mathrm{ord}}(A_b) = T^c(s^{-1}\bar A_b)$ *on $\overline{M}_{g,n}$ over
   the relative factorisation stack*, fusing the transverse and modular
   directions at the level of the primitive object. Everything downstream in B
   inherits this.

2. **Two bar–cobar theorems, not one.** A spine (iii): internal associative
   bar–cobar on connected positive-weight objects and their Mittag–Leffler
   completions, versus Francis–Gaitsgory pro-nilpotence for chiral convolution
   on $D(\mathrm{Ran}\,X)$ — *different monoidal products*, joined only by a
   named monoidal comparison. B's "Theorem A" fuses them and carries a list of
   hypothesis packages ($H_{\mathrm{fact}}$, $H_{\mathrm{conv}}$,
   $H_{\mathrm{VD}}$) to hold the fusion together.

3. **$A^! := \mathrm{RHom}_A(\mathbf 1,\mathbf 1)$** — the endomorphism algebra
   of the augmentation boundary condition; double dual = derived augmentation
   completion. Quadratic, PBW/nonhomogeneous, curved, and Verdier duality are
   *comparison constructions to the universal bar resolution*. B promotes the
   Verdier comparison to the definition
   ($A^!_\infty = \mathbb D_{\mathrm{Ran}} B_X(A_b)$).

4. **The duoidal law** (A §3) — two monoidal products on the Ran category
   (pointwise $\otimes$, chiral convolution) with Beck–Chevalley interchange; an
   ordered chiral algebra is a bimonoid whose pointwise multiplication is a
   morphism of factorisation coalgebras; the bar carries two commuting
   coproducts (deconcatenation, chiral factorisation). **B has no analogue.**
   This is A's principal new structural theorem.

5. **Two genera, two loop operators.**
   $d\Theta + \tfrac12[\Theta,\Theta]_X + \tfrac12[\Theta,\Theta]_\perp
   + \hbar_X\Delta_X\Theta + \hbar_\perp\Delta_\perp\Theta = 0$;
   ribbon genus (CY trace, Hochschild chains, open TFT) and chiral genus
   (modular sewing, Deligne–Mumford, conformal blocks) independent; bicoloured
   Feynman transform. B runs a single Maurer–Cartan equation and a single genus,
   and its entire modular tower is built on the collapsed version.

6. **Order does not contain exchange.** Chambers of $\mathrm{Conf}_n(\mathbb R)$
   are contractible, so a bare $E_1$ algebra has no canonical braid. Dunn
   additivity: the universal $E_2$ acting on an $E_1$ algebra is its Hochschild
   centre. B builds a large apparatus ($\mathsf{SC}^{\mathrm{ch,top}}$, five
   presentations, T1–T5 topologisation obstructions) around this point.

7. **No-go theorems** (A appendix H.9–H.13), which retract B's scalar programme
   by name:
   - H.9 — the kernel dimension of $V^{\otimes n}\to \mathrm{Sym}^n V$ contains
     no multiplication, coproduct, monodromy, or coherence equation, hence no
     $r$-matrix, associator, or quantum group.
   - H.10 — $\partial^2 = 0$ on $\overline{M}_{g,n}$ assigns no coefficient
     operations to boundary strata.
   - H.11 — the derived centre is terminal among algebraic central actions on
     the boundary; it does not detect a decoupled bulk.
   - H.12 — central charge does not classify.
   - H.13 — current-algebra level, Virasoro $c$, determinant-line curvature,
     BRST ghost-number anomaly, and Borcherds-product weight are invariants *in
     different theories*; they are not one universal scalar.

   H.12 and H.13 together retract B's five-$\kappa$ $5\times5$ matrix as a
   classifying invariant and the "Universal Trace Identity". H.9 retracts B's
   averaging-map route to quantum groups.

## What B holds that A does not

**Essential:**

- **Computed bar cohomology for named chiral algebras** (`03_computed_results/`).
  Virasoro: $\dim H^n = M(n+1)-M(n)$, first differences of Motzkin numbers
  ($1,2,5,12,30,76,196,512,1353,3610$), generating function
  $4z/(1-z+\sqrt{1-2z-3z^2})^2$, explicit four-term recurrence.
  $\mathfrak{sl}_2$: Riordan numbers $R(n+3)$ ($3,6,15,36,91,232,603,1585$),
  generating function $(1+x-\sqrt{1-2x-3x^2})/(2x(1+x))$.
  **The same discriminant $\sqrt{1-2x-3x^2}$ appears in both**; the data file
  attributes this to Drinfeld–Sokolov reduction, unproved. Plus engines for
  $W_3$, $W_4$, $W_n$, $\beta\gamma$, lattice, $N{=}2$ SCA, non-simply-laced,
  simple quotients, and $G_2$ chain dimensions.

  A's stated evidentiary standard (§G.8) is "one operation, calculated in
  several faithful realizations, with every passage preserving the category of
  the object." A then supplies **no numerical example**: tables 28.10 and G.7
  are structural, and the strongest example computation in the paper is
  Prop. 29.1 (the bar of a free algebra contracts onto $M[1]$).

  **Caveat: these were computed under B's conflated bar and must be re-derived
  under $\mathbf 1 \otimes^L_A \mathbf 1$ before the numbers mean what they
  claim. The engines survive the correction; the numbers may not.**

- **Genus-2-and-above analytic material.**
  `higher_genus_modular_koszul.tex`: 45,298 lines, 286 statements, 333 proofs,
  against A §26.9 ("Genus two and beyond") which is a few paragraphs. The
  framing is wrong (one genus where A has two), but prime forms, plumbing
  coordinates, degeneration, and Siegel theta content gets re-sorted into
  $\hbar_X$ vs $\hbar_\perp$, not discarded.

- **The verification harness.** Not mathematics, but the only mechanism in
  either artifact capable of catching a wrong constant.

**Present in B, absent from A, plausibly real (all unaudited):**

| file | statements / proofs | coverage in A |
|---|---|---|
| `yangians_drinfeld_kohno.tex` | 68 / 96 | §21–22, recognition framing only |
| `chiral_modules.tex` | 56 / 58 | §18.7 + §4.6, thin |
| `en_koszul_duality.tex` | 49 / 42 | stops at $E_1/E_2$ + Dunn |
| `derived_langlands.tex` | 23 / 21 | "Langlands" ×5, no content |
| `heisenberg_eisenstein.tex` | 20 / 21 | "Eisenstein": 0 occurrences |
| `entanglement_modular_koszul.tex` | 13 / 13 | §31.8, one subsection |
| `symmetric_orbifolds.tex` | 12 / 10 | "orbifold": 0 occurrences |

**Superfluous in B:** `concordance.tex` (13,465 lines), `master_concordance`,
`editorial_constitution`, `master_reconstruction`, and the `_platonic` family
(`shadow_tower_quadrichotomy`, `chiral_climax`, `grand_unification`,
`universal_conductor_K`, `infinite_fingerprint_classification`,
`motivic_shadow_tower`). A discharges this entire function in appendix H —
eleven sections, ~7 pages, five no-go theorems. Also superfluous: everything
keyed to the G/L/C/M/B archetypes and $r_{\max}$ shadow-depth, and the
scalar-computing engines (`abjm_holographic_datum`, four AGT/Nekrasov engines,
`analytic_langlands_shadow`, `arithmetic_resurgence`).

## Questions for the analysis

1. **Audit A on its own terms.** Are the nine spine statements (§1.9) proved as
   claimed? Where are the gaps? Pay particular attention to: the duoidal /
   Beck–Chevalley interchange claim (§3); the anticommutation of the two
   edge-contraction differentials via independence of determinant lines (§5.4,
   appendix A); the bicoloured master equation (§24); and Theorem 10.5
   (holomorphic–topological recognition).

2. **Is correction #1 (the transverse bar) fully carried through A?** Or does A
   still, anywhere, let a residue differential do bar-differential work?

3. **Re-derive the bar cohomologies under A's bar.** Do Virasoro $\to$ Motzkin
   differences and $\mathfrak{sl}_2 \to$ Riordan survive
   $\mathbf 1\otimes^L_A\mathbf 1$? If they change, what do they become? If they
   survive, is the shared discriminant $\sqrt{1-2x-3x^2}$ explained by
   Drinfeld–Sokolov, and can that be made a theorem?

4. **Triage B against A.** For each of the 156 chapter files in
   `05_full_manuscript_source/`, classify as: *port unchanged*, *rewrite under
   the correct carrier*, or *retract*. Flag any content in the "retract" pile
   that is independently true even though its framing is dead.

5. **What is missing from both?** Given A's ordering-of-dependence diagram
   (Theorem 0.1, eq. 5), which arrows have no worked example anywhere in either
   artifact?

## Bundle layout

```
00_README_ANALYSIS_BRIEF.md        this file
01_new_formulation/                the 198pp paper (PDF + extracted text + spine)
02_repo_architecture/              CLAUDE.md (the legacy architecture doc), main.tex, FRONTIER.md
03_computed_results/               verified computational output + engine/test inventories
04_unique_content_chapters/        the 15 legacy files with content absent from the paper
05_full_manuscript_source/         all 156 chapter + appendix .tex files
MANIFEST.txt                       file listing with sizes
```

Start with `01_new_formulation/paper_fulltext.txt` and
`03_computed_results/`. `05_` is reference, not required reading.
