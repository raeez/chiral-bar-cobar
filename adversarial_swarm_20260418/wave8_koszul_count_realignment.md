# Wave-8: Koszul meta-theorem count realignment (chapter opening)

Date: 2026-04-18
Scope: Vol I `chiral_koszul_pairs.tex` chapter-opening honest count +
programme-wide AP5 propagation sweep.
Relation to prior waves:
- Wave-4 Koszul count agent (a11163f0) truncated per AP313; heal deferred.
- Wave-7 AP271 sweep (aac22cb1) flagged this as load-bearing residue.
- This Wave-8 note closes the residue.

## Diagnosis

### 1. Internal self-contradiction in `chiral_koszul_pairs.tex`

At the time of this audit the chapter held two distinct honest counts:

- Chapter opening, :77-89 (old text): "Nine are unconditional
  equivalences ... $9 + 1 + 1 + 1$".
- Honest-count remark `rem:koszul-equivalences-meta-scope`, :2323-2365
  (current): "$8 + 1 + 1 + 1 + 1 = 12$ numbered items", explicitly
  admitting item (vi) Barr--Beck--Lurie is a proved consequence of (v)
  rather than an independent equivalence.

The chapter opening treated (vi) as one of the "nine unconditional";
the internal remark admitted (vi) as the consequence (AP273:
admitted-redundant item counted in independent-equivalence tally).
The two counts were inconsistent across a single chapter.

### 2. LaTeX typo (FM7 / B30) at :2365

`\end{remark>` (closing angle bracket instead of brace) at the end of
`rem:koszul-equivalences-meta-scope`. Live manuscript bug.

### 3. AP241 tropical Koszulness status

The honest-count remark references `thm:tropical-koszulness` in
`chap:higher-genus`. Grep confirms the label exists at
`chapters/theory/higher_genus_modular_koszul.tex:30161`. The
advertisement is an inscribed forward reference, NOT a phantom; no
retraction is required.

### 4. CLAUDE.md Koszul row

CLAUDE.md Theorem-Status table already carries the honest
"8 genuine bidirectional + 1 one-way ChirHoch + 1 Lagrangian
(perfectness-conditional) + 1 one-directional D-mod purity + 1
uniform-weight-conditional genus-refinement of (vii) = 8+4" split.
Chapter opening heal brings the typeset manuscript into line with the
CLAUDE.md row; no CLAUDE.md edit required.

## AP5 programme-wide propagation sweep

Live consumer audit for the forbidden patterns
`10 unconditional | ten unconditional | 10 Koszul equivalences |
twelve equivalences | nine unconditional | 9+1+1+1 | 8+1+1+1+1 |
fourteen equivalent | fourteen characterizations`:

### Vol I typeset sources
- `chapters/theory/chiral_koszul_pairs.tex`:
  - :77-93 chapter opening — HEALED (was "Nine are unconditional /
    $9+1+1+1$", now "Eight are genuinely independent ... $8+1+1+1+1$").
  - :2249-2365 "twelve equivalences / twelve characterisations" in
    Koszul-Reflection remark + honest-count remark — honest, scoped
    internally, match CLAUDE.md. No edit.
  - :2365 `\end{remark>` typo — HEALED.
- `chapters/theory/ftm_seven_fold_tfae_platonic.tex:589` — "twelve
  equivalences (plus partial/conditional extensions)" as neutral
  headline immediately followed by per-item list. Honest. No edit.
- `chapters/theory/koszulness_moduli_scheme.tex:987-1004, 1030-1035,
  1082-1085` — already enacts the
  "eight genuinely independent + Barr--Beck--Lurie adjoint + one-way
  Hochschild + conditional Lagrangian + one-directional D-module"
  split with retrospective framing of the "twelve / ten unconditional"
  name as a coordinate artefact resolved by the moduli scheme.
  Honest. No edit.
- `chapters/examples/landscape_census.tex` — no count-overclaiming
  strings in typeset text; the grep-hit at :1269 was an unrelated
  Yangian DK content line. No edit.
- `working_notes.tex:785-793, :4183-4185` — already "eight genuinely
  independent bidirectional equivalences plus the two proved
  consequences" + one Lagrangian + one one-directional purity.
  Honest. No edit.
- `standalone/koszulness_fourteen_characterizations.tex` — advertises
  "fourteen characterizations" as its own subject; compatible with the
  moduli-scheme atlas framing where each chart is unconditional on its
  home coordinate (part_viii_synthesis.tex:351-358 /
  koszulness_moduli_M_kosz.tex:14-20 quote). No edit.

### Vol II typeset sources
- `chapters/frame/part_viii_synthesis.tex:352` — "'10 unconditional + 4
  scoped'" in explicit quotation marks with retrospective framing:
  "is retrospectively understood as a coordinate artefact". Honest.
- `chapters/theory/koszulness_moduli_M_kosz.tex:15` — identical
  retrospective framing, explicit quotation marks. Honest.
- `chapters/connections/bar-cobar-review.tex:2004-2010, 2399, 3511-3517`
  — "twelve characterizations" as headline, per-item split
  "eight genuinely independent bidirectional + Barr--Beck--Lurie
  restatement + one-way chiral Hochschild + perfectness-conditional
  Lagrangian + one-directional D-module purity". Honest.
- `chapters/connections/holomorphic_topological.tex:1418` — "twelve
  characterizations" as neutral headline for `thm:koszul-equivalences-meta`.
  No expanded split because this is cross-reference context.
  Honest.

### Vol III
No typeset hits for the count-overclaim patterns.

## Tropical Koszulness advertisement (AP241)

`thm:tropical-koszulness` is inscribed at
`higher_genus_modular_koszul.tex:30161`. The honest-count remark in
`chiral_koszul_pairs.tex` references it as a separately-inscribed
standalone characterization that is NOT integrated into the unified
meta-theorem list. This is honest practice: the meta-theorem remains
8+1+1+1+1 = 12 items, and tropical Koszulness is a parallel inscribed
result elsewhere. No retraction required. The CLAUDE.md Koszul row
note "advertised in the preface as a 13th equivalence but is NOT
inscribed in the chapter meta-theorem; treat as heuristic pending
inscription" should be updated in a follow-up pass to reflect that
tropical Koszulness IS in fact inscribed; the heuristic caveat
belongs only to the preface-level advertisement if it survives.

## Heals applied

1. `chiral_koszul_pairs.tex:77-93` — chapter opening rewritten from
   "Nine are unconditional equivalences ... $9 + 1 + 1 + 1$" to
   "Eight are genuinely independent bidirectional equivalences ... The
   Barr--Beck--Lurie comparison is a proved consequence of the
   bar-cobar counit quasi-isomorphism, listed for completeness ...
   $8 + 1 + 1 + 1 + 1$". Matches internal honest-count remark and
   CLAUDE.md Koszul row.

2. `chiral_koszul_pairs.tex:2365` — `\end{remark>` fixed to
   `\end{remark}` (FM7 / B30).

## Post-heal verification

- Grep for `9+1+1+1` / `Nine are unconditional` in Vol I chapters:
  zero hits.
- Grep for `\end{...>` / `\begin{...>` in `chiral_koszul_pairs.tex`:
  zero hits.
- Cross-volume AP5 sweep (above): no further drift; all typeset
  consumers carry the 8+4 honest split.

## Deferred / out-of-scope

- CLAUDE.md Koszul row note about tropical Koszulness "not inscribed
  in the chapter meta-theorem" should be refreshed to record that
  tropical Koszulness IS inscribed at `higher_genus_modular_koszul.tex:30161`.
  This is follow-up metadata hygiene, not Wave-8 blocking scope.
- Line 6860 AP24 hook-warning on Virasoro complementarity
  `\kappa + \kappa' = 0` is pre-existing content outside Wave-8 scope.

## Commit plan

None. Mission constraint: "No commits." The heals above are local
edits; queue for inclusion in the next scheduled Koszul-hygiene
commit under normal pre-commit gates (build + tests + no AI
attribution).
