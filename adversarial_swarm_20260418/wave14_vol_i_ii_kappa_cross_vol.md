# Wave-14 Vol I + Vol II κ_ch(K3×E) Cross-Volume AP5 Sweep

**Date.** 2026-04-18
**Scope.** Propagate Wave-13 Vol III canonical convention
(`rem:beauville-kappa-formula-subscript-split` at
`~/calabi-yau-quantum-groups/standalone/cy_to_chiral.tex:293-298`)
to Vol I + Vol II consumer sites.
**Agent.** Claude Opus 4.7 (AP5 propagation sweep).
**Status.** Live-manuscript heal complete; zero commits (per task spec).

## Canonical Convention (Wave-13 Vol III adjudication)

Two genuinely distinct κ-invariants on compact CY products,
previously merged under the single symbol `κ_ch`:

- **Route A (canonical `κ_ch`, Hodge supertrace).**
  `κ_ch(X) := Ξ(X) = Σ_q (-1)^q h^{0,q}(X)`.
  Künneth-**multiplicative**: `Ξ(X × Y) = Ξ(X) · Ξ(Y)`.
  Values: `Ξ(K3) = 2`, `Ξ(E) = 0`, `Ξ(K3 × E) = 0`.

- **Route B (`κ_ch^{Heis}`, Heisenberg-level additive).**
  Generator-count / dimension invariant of the chiral de~Rham complex.
  Additive under Cartesian product (Künneth for free-boson generators):
  `κ_ch^{Heis}(X × Y) = κ_ch^{Heis}(X) + κ_ch^{Heis}(Y)`.
  Values: `κ_ch^{Heis}(K3) = 2`, `κ_ch^{Heis}(E) = 1`,
  `κ_ch^{Heis}(K3 × E) = 3 = dim_C(K3 × E)`.

AP289 discipline: super-trace / elliptic-genus / Hodge characteristic
invariants are Künneth-multiplicative; only Euler characteristic
under disjoint union is additive. The original confusion came from
reading `κ_ch(K3) = 2` (where Route~A and Route~B happen to coincide)
as licensing additivity at `K3 × E`.

## Hit inventory (programme-wide grep, live manuscript only)

Grep pattern: `\\kappa_\{\\mathrm\{ch\}\}\(K3 | \\kappa_\{ch\}\(K3 | kappa_ch\(K3 | kappa\(K3.*\\times.*E`
Scope: `{Vol I, Vol II}/{chapters,standalone,appendices}/`.

### Vol I — 7 Route-B sites across 4 files (ALL HEALED)

1. `chapters/connections/concordance.tex:10923` — "modular characteristic
   ($κ_ch = 3 ≠ 5 = κ_BKM$)" in the four-obstruction enumeration.
   **Healed** → `κ_ch^{Heis}` + V3- ref.
2. `chapters/connections/concordance.tex:10931` — four-κ invariant list
   "`κ(A) = 3, κ_BCOV = 0, κ_MacMahon = 0, κ_BKM = 5`".
   **Healed** → `κ^{Heis}(A) = 3`.
3. `chapters/connections/concordance.tex:10940, :10947` — K3-1 / K3-3
   structural result bullets (additive "`κ(K3 × E) = 3 = dim_C`" and
   `κ_BKM = κ(K3) + κ(K3 × E) = 2 + 3 = 5`).
   **Healed** → `κ^{Heis}` on both bullets, with ratio relabelled.
4. `chapters/connections/concordance.tex:11032` — `Spec_κ(K3 × E) = {2,3,5,24}`.
   **Left as bare κ** (polysemy spectrum ranging over all four routes;
   legitimate as a listing, not a value-claim).
5. `chapters/theory/higher_genus_modular_koszul.tex:3619-3620` —
   `rem:kappa-holo-k3e` Brown–Henneaux remark additive chain
   `κ(K3) + κ(E) = 2 + 1 = 3`.
   **Healed** → `κ^{Heis}` + scope note on multiplicative Route~A
   giving 0 + V3- ref + AP289 citation.
6. `standalone/cy_to_chiral_functor.tex:620-625` — proof of
   `prop:v3-st-k3e-spectrum` ("`κ_ch = dim_C(K3 × E) = 3`, additivity").
   **Healed** → `κ_ch^{Heis}` + scope note + V3- ref.
7. `standalone/cy_to_chiral_functor.tex:720-724` — K3-1 structural
   result in section-head text.
   **Healed** → `κ_ch^{Heis}` + Route-A contrast (`Ξ(K3 × E) = 0`)
   + V3- ref.
8. `standalone/programme_summary_sections5_8.tex:705` and
   `standalone/programme_summary.tex:2008` — duplicate `ssec:k3-times-e`
   subsection prose "`κ_ch(K3 × E) = 3 = dim_k`".
   **Healed (both)** → `κ_ch^{Heis}` + Route-A contrast + V3- ref,
   with `κ_BKM/κ_ch^{Heis}` ratio label updated.
9. `standalone/programme_summary.tex:2018` and
   `standalone/programme_summary_sections5_8.tex:715` — `Spec_κ(K3 × E)`
   polysemy spectrum. **Left as bare κ** (same rationale as Vol I #4).

**Atomic renames.** 7 substantive renames across 4 files
(concordance.tex × 3 contiguous sites, higher_genus_modular_koszul.tex,
cy_to_chiral_functor.tex × 2, programme_summary.tex + its
sections5_8 twin). Each edit bundles the rename with
(a) V3- phantomsection cross-reference,
(b) Route-A contrast (`Ξ(X × Y) = 0` for K3×E),
(c) AP289 multiplicative-vs-additive citation where natural.

### Vol II — 0 live-manuscript hits

Only references to `κ_ch(K3)` / `κ_ch(K3 × E)` live in
- `CLAUDE.md:1349` (AP-CY42 cross-volume catalogue — metacognitive)
- `notes/first_principles_cache_comprehensive.md` × 5
  (cache patterns — metacognitive)

Per the manuscript-metadata-hygiene constitutional rule (CLAUDE.md
§Manuscript Metadata Hygiene, §AP-manuscript-metadata-hygiene),
these are LEGITIMATE in metacognitive files; no heal applied.

## V3- phantomsection alias added

`main.tex:2214` (Vol I), beneath the Wave-13 cross-volume scaffolding
block, under a new comment
`% --- Wave-14 cross-volume scaffolding heal (2026-04-18, AP5 κ_ch K3×E propagation) ---`:

```latex
\phantomsection\label{V3-rem:beauville-kappa-formula-subscript-split}%
% Vol III cy_to_chiral.tex:293-298 (Route A / Route B adjudication)
```

Vol II does not require a phantomsection alias (zero Vol II consumer
sites).

## Grep gate

### Before heal

Vol I: 7 Route-B hits at non-polysemy sites + 3 polysemy `Spec_κ` hits.
Vol II: 0 live-manuscript hits.

### After heal

```
$ grep -rn '\\kappa_\{\\mathrm\{ch\}\}\(K3 | \\kappa_\{ch\}\(K3 | kappa_ch\(K3 | kappa\(K3.*\\times.*E' \
     chapters/ standalone/ appendices/
chapters/connections/concordance.tex:11032: $\operatorname{Spec}_\kappa(K3 \times E)   # polysemy spectrum — OK
standalone/programme_summary_sections5_8.tex:720:\operatorname{Spec}_\kappa(K3 \times E)   # polysemy spectrum — OK
standalone/programme_summary.tex:2023:\operatorname{Spec}_\kappa(K3 \times E)            # polysemy spectrum — OK
```

Zero Route-B value-claim bare-`κ_ch(K3×E)` hits in Vol I live
manuscript. Zero Vol II live-manuscript hits before or after.

## Classification summary

| Site | Convention on face | Route | Heal applied |
|------|--------------------|-------|--------------|
| concordance.tex:10923 | `κ_ch = 3 ≠ 5 = κ_BKM` | B | → `κ_ch^{Heis}` |
| concordance.tex:10931 | `κ(A) = 3` | B | → `κ^{Heis}(A)` |
| concordance.tex:10940 | `κ(K3×E) = 3 = dim_C` | B | → `κ^{Heis}` |
| concordance.tex:10947 | `κ_BKM = κ(K3) + κ(K3×E) = 5` | B | → `κ^{Heis}` |
| concordance.tex:11032 | `Spec_κ(K3×E) = {2,3,5,24}` | polysemy | LEFT |
| higher_genus_modular_koszul.tex:3619 | `κ(Ω^ch(K3×E)) = 2+1 = 3` | B | → `κ^{Heis}` |
| cy_to_chiral_functor.tex:623 | `κ_ch = dim_C(K3×E) = 3` (proof) | B | → `κ_ch^{Heis}` |
| cy_to_chiral_functor.tex:720 | `κ_ch(K3×E) = 3 = dim_C` (K3-1) | B | → `κ_ch^{Heis}` |
| programme_summary.tex:2008 | `κ_ch(K3×E) = 3 = dim_k` | B | → `κ_ch^{Heis}` |
| programme_summary_sections5_8.tex:705 | (duplicate of :2008) | B | → `κ_ch^{Heis}` |
| programme_summary.tex:2018 | `Spec_κ(K3×E) = {2,3,5,24}` | polysemy | LEFT |
| programme_summary_sections5_8.tex:715 | (duplicate of :2018) | polysemy | LEFT |

## Commit plan (not executed this wave per task spec)

1. Stage Vol I edits (5 files):
   - `main.tex` (+2 lines — comment + phantomsection alias)
   - `chapters/connections/concordance.tex` (3 edits, ~10 lines touched)
   - `chapters/theory/higher_genus_modular_koszul.tex` (1 edit, ~8 lines)
   - `standalone/cy_to_chiral_functor.tex` (2 edits, ~18 lines)
   - `standalone/programme_summary.tex` (1 edit, ~12 lines)
   - `standalone/programme_summary_sections5_8.tex` (1 edit, ~12 lines)
2. Commit message (draft):

   ```
   Vol I Wave-14 κ_ch(K3×E) AP5 propagation

   Propagate Wave-13 Vol III canonical convention
   (rem:beauville-kappa-formula-subscript-split) to Vol I consumer
   sites: 7 Route-B renames κ_ch → κ_ch^{Heis} across 5 files, with
   Route-A (Hodge-supertrace) contrast Ξ(K3×E) = 0 cited at each
   heal. Route-A and Route-B label genuinely distinct invariants
   (AP289 Künneth-multiplicative vs additive). V3-phantomsection
   alias added at main.tex:2214. Three polysemy-spectrum
   Spec_κ(K3×E) sites left bare (legitimate listing over all
   routes). Vol II has zero live-manuscript hits.

   AP5 + AP289 + AP290 + Wave-13 (aa885c0d) + Wave-10 H3 (a0f44b6d).
   ```

3. Build check: `pkill -9 -f pdflatex; sleep 2; make fast` before commit.

## Residual

- Vol II `CLAUDE.md:1349` AP-CY42 cross-volume entry still writes
  "`Factor = kappa_ch(K3)`" — this is in the CLAUDE.md metacognitive
  layer; per AP236 / metadata-hygiene rule, metacognitive layer stays
  untouched by manuscript-propagation waves. Optional future work:
  refresh the Vol II CLAUDE.md AP-CY42 line to `κ_ch^{Heis}(K3) = 2`
  to mirror the Vol III canonical convention (purely cosmetic in
  the metacognitive layer).
- Vol II `notes/first_principles_cache_comprehensive.md` entries 11,
  36, 144, 145 still use `kappa_ch(K3×E) = 3`. Same metacognitive-layer
  rationale; deferred.
- The `Spec_κ(K3 × E) = {2, 3, 5, 24}` polysemy-spectrum notation is
  preserved bare across 3 sites. Optional cosmetic upgrade:
  `Spec_κ(K3 × E) = {Ξ = 0, κ_ch^{Heis} = 3, κ_BKM = 5, κ_fiber = 24}`
  — but this buries the polysemy list's punch; current bare-κ form
  is preferred.

## Cross-volume sanity

- Vol III canonical anchor:
  `rem:beauville-kappa-formula-subscript-split` at
  `~/calabi-yau-quantum-groups/standalone/cy_to_chiral.tex:293-298`.
  Confirmed present and authoritative (Wave-13 heal aa885c0d).
- Vol III live manuscript uses `κ_ch^{Heis}` consistently at
  `main.tex:443-446`, `k3_quantum_toroidal_chapter.tex:462`,
  `k3_chiral_algebra.tex:241, 447-541`. Vol I is now in sync.
- Vol II has no live-manuscript K3×E consumer sites. No propagation
  required. If any are later added, they MUST use `κ_ch^{Heis}`
  on the Route-B face and cite the V3- alias.

## AP register

- **AP5** (cross-volume propagation): applied programme-wide.
- **AP234** (two-Koszul-conductors-same-letter): analogous pattern,
  two invariants same symbol; resolved by explicit superscript.
- **AP289** (Künneth-multiplicative vs additive for super-trace):
  the load-bearing first-principles discipline; cited at each heal.
- **AP290** (HZ-7 κ-subscript type-swap): not directly triggered in
  Vol I (Vol I does not enforce κ-subscript universally), but the
  heal respects the Wave-13 Vol III κ_ch^{Heis} superscript
  convention, making cross-volume consumer refs type-consistent.
- **AP-CY69** (Beauville κ-formula Route A / Route B split):
  Vol III anchor; Vol I now synchronized.

---
End of Wave-14 Vol I + Vol II cross-volume κ_ch(K3×E) AP5 sweep note.
