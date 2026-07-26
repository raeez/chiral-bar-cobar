# The 408-page revision: what is here and what is not

The revision *Chiral Koszul Duality: The Geometry of Ordered Quantum Fields*
(408pp, built 2026-07-26 18:27 KST) arrived as a PDF plus its root file only.
The root is installed at `reconstruction/geometry.tex`; the PDF is preserved at
`reference/formulation-2026-07-25/B0-geometry-408pp.pdf`.

**7 of its 53 source files are present. 46 are missing.** `make geometry`
refuses to build and prints the list rather than producing a partial document
that reads as complete.

## Present — `core/`

These are the reconstruction sources already deployed here, and the revision
preserves them: `\input{core/...}` in the new root resolves against the same
seven files.

```
core/frontmatter.tex      core/part3_examples.tex   core/appendices.tex
core/part1_foundations.tex core/part4_physics.tex
core/part2_duality.tex     core/part5_audit.tex
```

Spot-checked as unchanged between the 104pp and 408pp renderings: the
aligned-decomposition splitting theorem, no-go 3 (no global strong-duoidal
isomorphism), the bar denominator product, Zamolodchikov–Faddeev confluence,
and the necklace/trace material.

## Missing — 46 files

`compat.tex`, `combined_bibliography.tex`, and:

| directory | count | files |
|---|---:|---|
| `detailed/` | 44 | `00_first_principles`, `00_factd`, `00_duoidal`, `00_ordered_ran`, `00_mixed_operad`, `00_internal_bar`, `00_internal_duality`, `00_koszul_morita_square`, `00_exchange_center`, `00_ht_recognition`, `00_quantum_line_theory`, `00_bimodular`, `00_anomalies`, `00_noncomm_examples`, `00_physical_derivations`, `00_higher_sources`, `00_historical_lineage`, `00_ordered_low_arity`, `01_diagonal_language`, `02_chiral_operations`, `03_partition_complex`, `04_fm_resolution`, `05_pole_geometry`, `06_formal_disc`, `07_chevalley_ran`, `08_koszul_duality`, `09_duality_center`, `10_ordered_monodromy`, `11_kz_quantum_groups`, `12_modular_master`, `13_conformal_blocks`, `14_brst_w`, `15_examples`, `16_arithmetic`, `17_quantum_field_theory`, `A_signs`, `B_low_arity`, `C_stratified_spectral_sequence`, `D_logical_separations`, `E_local_geometry`, `F_field_theory_derivations`, `G_exact_models` |
| `frontier/` | 2 | `frontier_master`, `inner_music_synthesis` |

Empty `detailed/` and `frontier/` directories are in place so the files drop
straight in.

## What the revision changes in the shared core

One rename matters. The Motzkin/Riordan audit, previously
*Theorem 15.2 (Exact audit of the Motzkin and Riordan claims)*, is now
*Theorem 15.2 (Carrier theorem for the planar series)*. The reframing is an
improvement: the series are "assigned to their actual combinatorial complexes",
and the theorem now says explicitly that a chain-level identification of either
planar series with an ordered bar "requires a specified transverse
multiplication and a quasi-isomorphism from its planar complex to that bar."

It still does not compute a Virasoro bar. `Goncharova` and `pentagonal` remain
at zero occurrences in the 408-page rendering.

## The two results still additive

Neither is in the revision. Both remain in `core/`, so they survive into the
408-page structure when the missing files arrive.

- **`core/part3_examples.tex`, the Virasoro row.** The revision's own theorem
  asks for a specified transverse multiplication and a quasi-isomorphism. The
  transverse presentation is $U(L_1)$ for the positive Witt algebra, and there
  the bar homology is constant $2$ in the weights $(3n^2\mp n)/2$ with Euler
  character $\prod_{n\ge1}(1-q^n)$ saturating it degree by degree. No
  quasi-isomorphism from a Motzkin or Riordan complex can exist, because the
  target is known. Verified $n=1,2,3,4$.
- **`core/part1_foundations.tex`, `prop:lambda-sector`.** Proves the assertion
  that the aligned idempotent records the sector where the mixed distributive
  law is defined.

## Build

```bash
make volume     # 104pp, builds fully from source here — normative until the 46 files land
make geometry   # 408pp structure; refuses and lists what is missing
```
