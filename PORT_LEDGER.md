# Port ledger

Disposition of the legacy corpus against the normative volume
(`reconstruction/reconstruction.tex`, built by `make volume`).

## The three roots

| root | build | pages | status |
|---|---|---:|---|
| `reconstruction/reconstruction.tex` | `make volume` | 104 | **normative**. Merges all four PDF witnesses plus the repository corpus. |
| `main_ordered_chiral.tex` | `make skeleton` | 35 | superseded; its two unique results are merged into the normative volume. |
| `main.tex` | `make legacy-manuscript` | — | retracted architecture. Reference only. |

The normative volume arrived as upstream LaTeX (`reconstruction/UPSTREAM_BUILD_README.md`,
`SOURCE_CORPUS_MANIFEST.md`, `INPUT_SHA256_MANIFEST.txt`). Four changes were
made when deploying it into this repository:

1. **Typography.** `book` + `lmodern` → `book` + `raeez-math-template`
   (`localtheorems`), so the volume sets in EB Garamond like every other
   document here. Its own page geometry, theorem environments, and tcolorbox
   status/no-go boxes are preserved. Consequences handled: `imakeidx` removed
   (the template already loads `makeidx` and calls `\makeindex`); `mathrsfs`
   and `bm` dropped (zero uses, and the template's `newtxmath` leaves too few
   free math alphabets); `bbm` dropped in favour of the document's own
   documented `\one = \mathbf 1` fallback, for the same reason; `\widebar`
   guarded against the template's definition.
2. **Root renamed** `main.tex` → `reconstruction.tex`. With `TEXINPUTS`
   including the repository root, a document named `main` picks up the memoir
   manuscript's `main.ind` and fails on memoir index internals.
3. **Bibliography regenerated.** The shipped `.bbl` was `plainnat`
   author–year; the template sets `amsrn`. Regenerated with bibtex, which also
   picked up the added `Goncharova1973` entry.
4. **Two results merged in** — see below.

## Merged into the normative volume

Both were absent from every witness.

- **`part3_examples.tex` — the Virasoro row computed.** The upstream
  `thm:legacy-audit` refutes the $\mathfrak{sl}_2$ Motzkin/Riordan claim by
  computing the answer, but refutes the Virasoro claim only by
  *non-determination*. Added `thm:pentagonal` (bar homology of $U(L_1)$ is
  constant 2 in the pentagonal weights, Euler character $\prod(1-q^n)$
  saturating it degree by degree), `prop:one-sequence` ($M(n)=R(n)+R(n+1)$,
  so the shared discriminant carries no Drinfeld–Sokolov content), and the
  remarks recording that the asserted sequence agrees with the truth at $n=2$
  alone and has the wrong type.
- **`part1_foundations.tex` — `prop:lambda-sector`.** The upstream frontmatter
  *asserts* that the aligned idempotent records the sector where the mixed law
  is defined. Now proved, with the remark that no $\lambda$ is thereby
  constructed.

## Verification

Two independent harnesses, cross-checked against each other:

| harness | method | scope |
|---|---|---|
| `compute/lib/witt_pentagonal_rigidity.py` | exact `Fraction`, sparse elimination, `d²=0` asserted per space | Witt/Goncharova, $\mathfrak{sl}_2$, $\mathfrak{sl}_3$, Motzkin/Riordan identities |
| `compute/lib/reconstruction_bar_models.py` | sympy `Rational` dense matrices | quantum/Jordan plane bar windows, $\mathfrak{sl}_2$ CE, $A_2$ Hall–Serre, stable trace Jacobi |

They share exactly one claim, $H^*(\mathfrak{sl}_2)=1,0,0,1$, and agree on it
with no shared code, basis, sign convention, or linear-algebra backend
(`compute/tests/test_harness_cross_agreement.py`). 23 tests pass.
Upstream outputs preserved at `compute/results/reconstruction_*`.

**Nothing has been deleted.** Every file listed here remains tracked at its
original path and is reachable in git history. "Cut" means *removed from the
normative build*, not removed from the repository. The retracted-architecture
manuscript still builds via `make legacy-manuscript`.

## Why the corpus was cut from the build

The legacy architecture placed the bar complex on $\overline{M}_{g,n}$ over a
relative factorisation stack, fusing the transverse and modular directions in
the primitive object. Downstream this produced one Maurer–Cartan equation
where there are two, one genus where there are two, a five-`κ` matrix treating
invariants from different theories as one classifying invariant, and an
averaging-map route from `ker(V^⊗n → Sym^n V)` to quantum groups.

The normative volume separates the two associative directions
(`volume/two_directions.tex`), replaces the fused bar with the transverse
interval amplitude `1 ⊗^L_A 1` (`volume/ordered_bar.tex`), and restores the
obstruction theorems that make the retraction explicit rather than tacit
(`volume/no_go.tex`). Specifically:

| retracted claim | retracted by |
|---|---|
| averaging map ⇒ quantum group | No-go 7.1 (no quantum group from dimension loss) |
| `∂²=0` on `M_{g,n}` ⇒ modular operations | No-go 7.2 (no modular object from topology alone) |
| derived centre = physical bulk | No-go 7.3 (no bulk from a boundary centre) |
| central charge classifies | No-go 7.4 (no classification by central charge) |
| five `κ` are one invariant; Universal Trace Identity | No-go 7.5 (no identification of anomalies of different types) |
| `Bar^⊥(A) = Bar^ch_Ass(A)` | No-go 7.6 (no unnamed comparison of bars) |
| Motzkin/Riordan = bar cohomology | No-go 7.7 + Theorem 5.6 (exact audit) |

## Already upgraded

| legacy source | upgraded into | status |
|---|---|---|
| aligned-decomposition law (153pp witness only, no repo source) | `volume/aligned_locality.tex` | proved, compiles |
| `chapters/theory/bar_construction.tex`, `cobar_construction.tex` | `volume/ordered_bar.tex`, `volume/bar_cobar_reconstruction.tex` | proved; hypotheses named |
| `chapters/theory/koszul_pair_structure.tex`, `chiral_koszul_pairs.tex` (11.5K lines) | `volume/bar_cobar_reconstruction.tex` §quadratic/PBW/curved | partial — see below |
| Motzkin/Riordan tables in `chapters/examples/bar_complex_tables.tex`, `landscape_census.tex` | `volume/enveloping_audit.tex` | **falsified and replaced**; `compute/tests/test_witt_pentagonal_rigidity.py`, 17 tests |
| `κ_BKM(Φ_N) = c_N(0)/2` as universal scalar | `volume/bar_denominators.tex` | **retracted**; replaced by the typed denominator product + Igusa corollary |
| no-go theorems H.9–H.13 (198pp witness only) | `volume/no_go.tex` | restored with proofs |

The Motzkin/Riordan entry is the one place a legacy claim was *falsified*
rather than reframed. `compute/lib/bar_dims.json` had already flagged the
Riordan row `summary_table_INCONSISTENT`; the truth is `dim H^n(Bar^⊥ U(L_1)) = 2`
for every `n ≥ 1` (Goncharova) and `dim H^n(sl_2) = 1,0,0,1` (Whitehead).

## To upgrade — mathematics that survives the reframing

Ranked by volume. The framing is wrong in each; the content is not known to be.

| lines | file | what must change |
|---|---|---|
| 45298 | `chapters/theory/higher_genus_modular_koszul.tex` | 286 statements, 333 proofs under a single fused genus. Prime forms, plumbing coordinates, degeneration, Siegel theta must be re-sorted into independent `g_⊥` and `g_X`. Largest single body of unported mathematics. |
| 8550 | `chapters/theory/chiral_hochschild_koszul.tex` | discriminate the three Hochschild theories; state which is `RHom_{A^e}(A,A)` |
| 8110 | `chapters/theory/chiral_koszul_pairs.tex` | Koszul-pair material is sound; needs the two-monoidal-product separation |
| 7786 | `chapters/examples/kac_moody.tex` | recompute bar homology as CE homology per Theorem 5.1; drop `κ`-matrix rows |
| 7251 | `chapters/examples/free_fields.tex` | free/square-zero bars are correct; re-typed carrier |
| 6536 | `chapters/examples/lattice_foundations.tex` | as above |
| 6535 | `chapters/theory/configuration_spaces.tex` | Fulton–MacPherson screens and partition collisions port largely intact |
| 5884 | `chapters/theory/chiral_modules.tex` | 56 statements; thin coverage in every witness. Port target. |
| 5121 | `chapters/frame/heisenberg_frame.tex` | Heisenberg = abelian Chern–Simons; keep, retype |
| 3451 | `chapters/examples/beta_gamma.tex` | retype carrier |
| 3394 | `chapters/theory/deformation_quantization.tex` | curved/PBW duality already partially upgraded |
| — | `chapters/examples/yangians_*.tex` (877K bytes, 3 files) | RTT Yangian, Drinfeld–Kohno: 68 statements / 96 proofs. Needs the exchange-data hypotheses stated. |
| — | `chapters/theory/en_koszul_duality.tex` | 49 statements; stops at `E_1/E_2` + Dunn in every witness |
| — | `chapters/theory/derived_langlands.tex` | 23 statements; no coverage in any witness |
| — | `chapters/examples/heisenberg_eisenstein.tex` | 20 statements; no coverage in any witness |
| — | `chapters/examples/symmetric_orbifolds.tex` | 12 statements; no coverage in any witness |

## Retracted frame — content keyed to the dead architecture

These are not to be ported as written. Where a statement inside them is
independently true, it must be re-derived in the normative frame, cited to a
primary source, not transcribed.

`chapters/connections/master_reconstruction.tex`,
`master_concordance.tex`, `concordance.tex` (13465 lines),
`editorial_constitution.tex`, `grand_unification_platonic.tex`,
`frontier_modular_holography_platonic.tex`,
`chapters/theory/shadow_tower_quadrichotomy_platonic.tex`,
`chiral_climax_platonic.tex`, `universal_conductor_K_platonic.tex`,
`infinite_fingerprint_classification.tex`, `motivic_shadow_tower.tex`,
`motivic_shadow_full_class_m_platonic.tex`, `kappa_conductor.tex`,
`three_invariants.tex`, `climax_theorem.tex`,
`chapters/frame/open_beilinson_tower_platonic.tex`,
`part_ii/iii/iv_platonic_introduction.tex`, and the remaining `*_platonic.tex`
family.

Everything keyed to the G/L/C/M/B archetypes and `r_max` shadow-depth, and the
scalar-computing engines (`abjm_holographic_datum`, the AGT/Nekrasov engines,
`analytic_langlands_shadow`, `arithmetic_resurgence`) fall here too.

## Open constructions, named and absent

1. **A mixed distributive law `λ` for any example.** Located but not
   constructed: Proposition 1.7 shows it can only live on the
   common-decomposition sector. Zamolodchikov–Faddeev is the natural
   candidate. Until this exists, the doubly noncommutative object is a
   definition without a model.
2. **Anticommuting edge-contraction differentials.** `d_⊥ d_X + d_X d_⊥ = 0`
   via independence of the two determinant lines. Asserted in all witnesses;
   the 153pp witness cut determinant-line discussion from 30 mentions to 2
   while still resting the boundary identity on it. Unproved here.
3. **Higher-genus material re-sorted into two genera.** Item 1 of the
   to-upgrade table.

## Method note

The classification above is a triage on filename and on the statement counts
recorded in the witness analysis, not a per-statement audit of 104,106 lines.
A file in "to upgrade" is not certified correct; it is certified *not
obviously keyed to the retracted architecture*. Each must be audited when
ported.
