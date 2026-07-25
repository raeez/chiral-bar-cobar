# The ordered chiral formulation — artifacts of 2026-07-25

Four PDFs produced on 2026-07-25, none of which had LaTeX source anywhere on
disk. They are stored here because they were the only copies. Extracted text
accompanies each so the content is greppable without a PDF reader.

| file | pages | built | role |
|---|---|---|---|
| `A0-first-198pp.pdf` | 198 | 06:51 KST | first version; **carries no-go theorems H.9–H.13** |
| `A1-second-199pp.pdf` | 199 | 09:16 KST | minor revision of A0 |
| `A2-maximal-246pp.pdf` | 246 | 16:38 KST | widest coverage; 42 sections |
| `A3-current-153pp.pdf` | 153 | 18:44 KST | **current**; restructured into 7 parts, 30 chapters, 4 appendices |

`analysis-brief.md` and `A0-contents-and-spine.md` are the accompanying
comparison of this formulation against the legacy Volume I architecture.

## The primitive object

```
A ∈ Alg^aug_{E_1}( FactD(X), ⊗^! )
```

an augmented `E_1`-algebra in factorisation right `D`-modules on a smooth
complex algebraic curve `X`. The chiral coefficient records collision on `X`;
the internal `E_1` multiplication records ordered fusion along a transverse
oriented line. The ordered bar is the transverse interval amplitude

```
Bar^ord_X(A) ≃ 1 ⊗^L_A 1 ≃ ∫_{([0,1], ∂[0,1])} A
```

and the chiral coefficient is **not** contracted: no logarithmic residue is
asked to do bar-differential work. Five geometric carriers — diagonal,
interval, plane, circle, nodal curve — are kept distinct, and none determines
the next.

## Content deltas between versions

`A3` is not a superset of `A2`. Counts of occurrences in the extracted text:

| content | A0 (198pp) | A2 (246pp) | A3 (153pp) |
|---|---|---|---|
| no-go theorems H.9–H.13 | 13 | 0 | 0 |
| `duoidal` | — | 18 | 3 |
| determinant line / anomaly domain | 29 | 30 | 2 |
| prime form / bidifferential (genus ≥ 2) | 8 / 4 | 17 / 10 | 0 / 0 |
| Feigin–Frenkel centre | 12 | 17 | 2 |
| central charge | 59 | 56 | 8 |
| Motzkin / Riordan triage | 0 / 0 | 6 / 4 | 0 / 0 |
| Hall algebra | 19 | 20 | 38 |

Two of these are load-bearing.

**The duoidal retraction (A2 → A3).** A2 claimed Beck–Chevalley interchange
makes the factorisation category duoidal, so an ordered chiral algebra is a
bimonoid. A3 withdraws this: the canonical comparison is a *retraction with an
idempotent* (`πι = id`, `e = ιπ`, image = common-decomposition summand), strong
duoidality holds only on aligned windows, and sheaf-level locality is the family
of disjointness-locus squares. Inscribed with proofs in
`standalone/locality_and_bar_denominators.tex`.

**The no-go theorems (A0 only).** H.9–H.13 are the mechanism by which the
legacy five-`κ` `5×5` matrix, the Universal Trace Identity, and the
averaging-map route to quantum groups are *retracted* rather than merely
unmentioned. H.13 — current-algebra level, Virasoro `c`, determinant-line
curvature, BRST ghost-number anomaly, and Borcherds-product weight are
invariants *in different theories* — has no successor in A2 or A3. Recovering
it is outstanding.

## Unaudited claims

Flagged for audit and not yet audited:

- the anticommutation of the two edge-contraction differentials via
  independence of determinant lines (A3 §5.2 / appendix A). A3 cut
  determinant-line discussion from 30 mentions to 2 while still resting the
  boundary identity on the product orientation of two determinant lines.
- the bicoloured master equation with two independent genera (A3 ch. 20)
- holomorphic–topological recognition (A0 Thm 10.5)

## Falsified on inspection

`A2` §31.2 states plainly that its formula (195) "is an exact chain-space
count… A homology dimension requires the differential", and §31.5 makes the
Motzkin identification conditional on a quasi-isomorphism that does not exist.
`A3` drops the triage entirely. The disposal is completed in
`standalone/locality_and_bar_denominators.tex` §5 and verified in
`compute/tests/test_witt_pentagonal_rigidity.py`: the bar cohomology of
`U(L_1)` is 2-dimensional in every positive degree (Goncharova), and the
circulating sequences `1,2,5,12,30,…` and `3,6,15,36,91,…` are neither that
cohomology nor a bar chain count.
