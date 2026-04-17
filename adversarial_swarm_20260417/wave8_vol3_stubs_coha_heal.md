# Wave 8: Vol III CoHA citation + stub inventory heal

**Date.** 2026-04-17.
**Mission.** Heal two Vol III metadata-layer residuals flagged by Waves 4-7:
(i) `coha_wall_crossing_platonic.tex` uncited in Vol III CLAUDE.md status
table; (ii) stale "4 stub chapters" claim.
**Non-commit.** Per session directive, no commit produced.

## Finding 1. CoHA wall-crossing chapter was uncited

`~/calabi-yau-quantum-groups/chapters/examples/coha_wall_crossing_platonic.tex`
(643 lines, Ch 25, input line 1064 of `main.tex`) was the 2026-04-16
healing inscription for the ledger-strict CoHA / Yangian / wall-crossing
separations that the companion `toric_cy3_coha.tex` elided. Six
theorem-level environments:

- `def:three-coha-objects` (path algebra / Ginzburg dg algebra / critical CoHA)
- `def:bar-of-coha-platonic` (bar complex of the CoHA)
- `thm:coha-is-algebra-not-coalgebra` (L193)
- `thm:coha-chiralization-preserves-algebra` (L281)
- `thm:ks-wall-crossing-mc-on-coha-dgla` (L346)
- `thm:conifold-cluster-wall-crossing` (L446)
- `cor:y-plus-vs-full-Y` (L501)

Despite presence in the .tex and in Wave-7 (#44 ledger-strict
verification), the chapter had no row in the Vol III CLAUDE.md main
theorem table.

**Heal.** Inserted a single "CoHA wall-crossing ledger" row in the Main
Theorems table citing the five theorem-level results, with
status qualifiers:

- algebra-vs-coalgebra separation: PROVED
- positive-half-vs-full-Yangian: PROVED for C^3 (Prochazka-Rapcak), CONDITIONAL for
  general toric on a Hopf-pairing lemma
- motivic-Hall-vs-chiral-convolution: PROVED for C^3, CONDITIONAL elsewhere on CY-A_3
- chiralisation preserves algebra-side: PROVED
- conifold wall-crossing = cluster mutation: PROVED

Inserted after the "6 routes to G(K3xE)" row, before "Borcherds spectral
flow", since the ledger-strict content is thematically closest to the
six-routes + wall-crossing cluster.

## Finding 2. "4 genuine stub chapters" line was entirely stale

The Vol III CLAUDE.md Identity section claimed:

> **4 genuine stub chapters** (<50 lines, AP114): quantum_groups_foundations
> (24), geometric_langlands (28), matrix_factorizations (29),
> modular_koszul_bridge (13). Develop or comment out. **3 thin chapters**
> (50-100 lines, may need development): cyclic_ainf (55), cy_categories
> (70), e1_chiral_algebras (90).

Verified line counts + theorem-environment counts (grep for
`^\begin\{(theorem|proposition|lemma|definition|conjecture|corollary)\}`):

| Chapter | Former claim | Actual lines | Theorem envs |
|---------|--------------|--------------|--------------|
| quantum_groups_foundations | 24 lines, stub | 405 | 15 |
| geometric_langlands | 28 lines, stub | 731 | 15 |
| matrix_factorizations | 29 lines, stub | 479 | 13 |
| modular_koszul_bridge | 13 lines, stub | 1047 | 31 |
| cyclic_ainf | 55 lines, thin | 239 | 5 |
| cy_categories | 70 lines, thin | 256 | 11 |
| e1_chiral_algebras | 90 lines, thin | 3340 | (developed) |

ALL seven listed chapters have been substantively developed since the
stale line was written. Shortest chapter in `chapters/` is
`connections/padic_langlands_cy.tex` (104 lines). No file satisfies the
AP114 criterion (<50 lines, zero theorems). AP114 remains live as a
maintenance rule; the specific allegation list was an archaeology
artefact.

**Heal.** Replaced the stub inventory paragraph with a refreshed
statement listing current line counts + theorem-env counts and declaring
no current AP114 violations, while preserving the AP114 re-audit
injunction.

## Heal sites

1. `~/calabi-yau-quantum-groups/CLAUDE.md:81` — refreshed stub inventory.
2. `~/calabi-yau-quantum-groups/CLAUDE.md:115` — inserted CoHA wall-crossing
   row in the Main Theorems table.

## No development of stub chapters (AP114 branch)

Per task scope, no mathematical development. Since no chapter currently
meets the stub criterion, no comment-out was required either. If the
criterion should be tightened (e.g. <200 lines AND fewer than 5 theorem
envs), `cyclic_ainf.tex` (239, 5 envs) would be the single candidate and
could be flagged `% STUB - DEVELOP OR REMOVE` in a future pass. Not done
here.

## Constitutional hygiene

- No bare `$\kappa$` introduced in Vol III prose (subscripts preserved:
  kappa_ch, kappa_BKM where cited).
- No AP / HZ indices in typeset prose. The stub-inventory paragraph
  mentions "AP114" only inside CLAUDE.md (scaffolding file), never in
  `.tex`.
- No em-dash, no banned tokens in the inserted CLAUDE.md row.
- No AI attribution anywhere in the edits.

## Files touched

- `~/calabi-yau-quantum-groups/CLAUDE.md` (two surgical edits).
- `~/chiral-bar-cobar/adversarial_swarm_20260417/wave8_vol3_stubs_coha_heal.md`
  (this note).

No .tex source modified; no build required.
