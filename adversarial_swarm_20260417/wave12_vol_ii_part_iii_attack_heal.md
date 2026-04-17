# Wave 12 Attack-Heal: Vol II Part III (Seven Faces of r(z))

**Target**: Vol II Part III, `\part{The Faces of r(z): a GRT_1(Q)-torsor}`
(main.tex:1469-1511), eight input chapters.

## Part III topology

Opener (main.tex:1469-1502) frames Part III as the nine-face
GRT_1(Q)-torsor: F1 bar hub, F2 DNP R-twist, F3 BBL slab, F4 celestial
soft factors, F5 affine half-space BV, F6 FM_3 planted forest, F7
Kontsevich integral, F8 Brown motivic, F9 Willwacher operadic.

Chapter roster:
1. `connections/dnp_identification_master.tex` (42 KB) — master chapter
   with F1–F7 enumerated, seven-face master theorem, Sasaki
   commutativity, Drinfeld–Kohno four-path.
2. `theory/grt_parametrized_seven_faces.tex` (44 KB) — F8 (Brown
   motivic), F9 (Willwacher operadic), F7/F7' disambiguation,
   Casimir-rescaling chained equality, super-variant.
3. `connections/spectral-braiding-core.tex` (226 KB)
4. `connections/ht_bulk_boundary_line_core.tex` (135 KB)
5. `connections/celestial_boundary_transfer_core.tex` (49 KB)
6. `connections/affine_half_space_bv.tex` (79 KB)
7. `connections/fm3_planted_forest_synthesis.tex` (18 KB)
8. `connections/kontsevich_integral.tex` (26 KB)

## Phase 1 — Audit (eight gates)

- **(i) CG deficiency opening.** Opener states the Part II E_1-core
  setup, reads r(z) as collision residue through nine GRT-orbit
  representatives. This is a retrieval opener (not pure CG deficiency)
  but is mathematically honest: Part III exists *because* the raw bar
  complex produces a single r(z) that different literatures name
  differently. ACCEPT.
- **(ii) Per-face inscription.** F1–F7 inscribed in the master chapter
  with explicit per-face status qualifiers (F1 unconditional, F2
  unconditional, F3 g=0 only, F4 W_N comparison conjectural, F5
  non-critical, F6 unconditional, F7 non-critical). F8, F9 inscribed in
  `grt_parametrized_seven_faces.tex`. PASS.
- **(iii) Primary citations per face.** F2 DNP = arXiv:2508.11749
  (Dimofte–Niu–Py) verified at main.tex and
  `grt_parametrized_seven_faces.tex:232`. F3 KZ25 + GLZ22. F4 GZ26. F5
  Drinfeld 1985. F6 STS83. F7 FFR94. F8 Brown 2012 arXiv:1102.1312. F9
  Willwacher 2015 arXiv:1009.1654. All match Vol I Part V citation set
  modulo 3d HT adaptations. PASS.
- **(iv) AP244 distinctness (not collapse).** Explicitly addressed at
  `rem:seven-vs-four-resolution` (dnp_identification_master.tex:471):
  "seven vs four" naming debate resolved via Sasaki commutativity —
  diagram commutes whichever cardinality is chosen. No collapse. PASS.
- **(v) Cross-volume cross-ref to Vol I Part V.** **FAIL → HEAL.** The
  cross-volume bridge section (line 732) described Vol I as "the
  holographic-datum master chapter" without naming the Vol I part. HEAL
  inscribed below.
- **(vi) DNP25 authors correct.** Dimofte–Niu–Py, arXiv:2508.11749,
  confirmed in `\index{Dimofte--Niu--Py!...}` entries and primary
  citations at F2. PASS.
- **(vii) AP170 Yangian two definitions disambiguated in F5.** F5 is
  labelled "dg-shifted Yangian of DNP25" with ℏ = 1/(k+h∨) for affine
  KM. The DNP identification remark (`rem:dnp-chain-level-status`)
  disambiguates cohomological vs chain-level vs type-BCD scope. The
  classical-Yangian-vs-chiral-Yangian distinction (AP170's
  `def:e1-chiral-yangian` vs `def:chiral-yangian-datum`) is not
  reasserted inline in Part III but is inherited from the Part II
  `unified_chiral_quantum_group.tex`. PASS (relative to Vol II
  convention).
- **(viii) AP248 SC dioperad discipline.** No misuse of Dunn additivity
  on SC^{ch,top} in Part III (zero hits). The SC^{ch,top}^! ≄ SC^{ch,top}
  asymmetry is correctly noted at `rem:dnp-master-koszul-dual-operad`
  (line 788: "(SC^{ch,top})^! ≃ (Lie, Ass, shuffle-mixed), which is NOT
  self-dual to SC^{ch,top}"). PASS.

## Phase 2 — Heal

**HEAL-1 (Gate v)**: add explicit Vol I Part V cross-reference to the
cross-volume bridge. Applied at
`dnp_identification_master.tex:738-749`: names the Vol I *Seven Faces
of r(z)* part and inscribes the F_i^{V1} = F_i^{V2} boundary-reduction
bijection between chiral-algebra-on-curve faces and boundary-algebra
faces of the 3d HT slab. (Hardcoded `Part~V` avoided per V2-AP26; uses
part-title name-form.)

## Constitutional hygiene

- AP/HZ/CLAUDE.md leakage in Part III chapters: zero hits across both
  master files.
- AI attribution: none in Part III.
- No em-dashes, no AI-slop tokens in heal.

## Residual

None mandatory. Possible future refinement: inline one-sentence
reassertion of AP170 distinction in F5 intro (currently inherited from
Part II); non-blocking.
