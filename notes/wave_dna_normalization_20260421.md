# Wave/DNA normalization — cross-volume audit pointer (2026-04-21)

Canonical audit + rename map for the cross-volume wave/DNA label
cleanup lives in Vol III under
`~/calabi-yau-quantum-groups/notes/wave_dna_normalization_20260421.md`
and `wave_dna_rename_map_20260421.txt`.

## Vol I local counts (before rectification)

Manuscript `.tex` under `chapters/`, `frame/`, `examples/`, `theory/`,
`connections/`, `bibliography/`, `appendices/`:

- 1191 lines containing `wave\d+` or `DNA`.
- 879 of those are inside `\label{...}`, `\ref{...}`, etc. (internal).
- ~312 are prose-level violations requiring semantic rewrite.
- Vol~I is the original home of the Wave~13--20 programme, so it
  carries the bulk of labels that Vol~II and Vol~III reference.

## Vol I prose hotspots (Chriss--Ginzburg rectification order)

| Count | File |
|---|---|
| 70 | `chapters/theory/derived_langlands.tex` |
| 50 | `chapters/theory/chiral_climax_platonic.tex` |
| 45 | `chapters/examples/w_algebras_deep.tex` |
| 34 | `chapters/theory/theorem_B_scope_platonic.tex` |
| 34 | `chapters/theory/bar_cobar_adjunction_curved.tex` |
| 31 | `chapters/examples/lattice_foundations.tex` |
| 28 | `chapters/frame/part_iv_platonic_introduction.tex` |
| 25 | `chapters/connections/concordance.tex` |

See Vol III canonical file for full normalization rules, collision
resolution, and the 929-entry rename map.
