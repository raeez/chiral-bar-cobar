# Wave-10 Attack + Heal: Vol II Part V "The Standard HT Landscape"

Target: `~/chiral-bar-cobar-vol2/main.tex` lines 1583-1632; primary chapter
`chapters/connections/ht_physical_origins.tex` (1580 lines).

Role: first-principles adversarial mathematician in the Beilinson tradition.
Discipline: Costello-Gwilliam factorization algebras; Beem-Lemos-Liendo-Peelaers-Rastelli-van~Rees 4d/2d; Costello-Li dimensional reduction; Gaiotto-Williams boundary chiral algebras; Paquette-Williams boundary VOAs.

## Phase 1 Attack

### (i) CG deficiency opening — PARTIAL

The Part V opener (main.tex:1589-1612) restates the fingerprint $\varphi'(\cA)$ and transgression $B_\Theta(\cA)$, names Yang-Mills boundary (class L), celestial holography, logarithmic HT monodromy, and the anomaly-completed triangle.
It does NOT open with a genuine deficiency in the Beem-Lemos-Liendo-Peelaers-Rastelli-van~Rees framework that only the HT landscape can close. Instead it reads as a table of contents.
Status: COSMETIC; not a heal priority for this wave.

### (ii) Per-family 3d HT inscription — PARTIAL

`ht_physical_origins.tex` enumerates the following 3d HT correspondences:
 - Class L (affine KM): 4d/2d from $\cN=4$ SYM (`thm:cl-n4-chirality`); Kac-Moody from HCS boundary (line 661 example); Sugawara on YM disk.
 - Class M (Virasoro / $\cW_N$): AGT `thm:agt` + Hitchin $\cW$-algebra subsection (line 820).
 - Class G (Heisenberg): absent as a direct HT origin; only implicit through the NC-torus Rieffel-Morita deformation (lines 86-108) and the Chan-Paton Steinberg story (lines 142-232).
 - Class C ($\beta\gamma$): absent as a direct HT origin at the standard-landscape level; $\beta\gamma$ does appear across Vol II in bv_brst.tex, but Part V has no entry.
 - Quiver Yangians / $N=4$ SYM Coulomb/Higgs: Paquette-Williams `thm:paquette-williams-boundaries` stops at "boundary VOA"; there is no inscribed Yangian/quiver-Yangian row.

The silent-non-coverage families of Vol I Rem `rem:census-silent-non-coverage`
(N=2 SCA, log $\cW(p)$, cosets, non-rational lattice, roots-of-unity / admissible)
have NO corresponding "honest frontier" inscription in Vol II Part V.
VERDICT: the HT landscape is presented as complete up to ongoing conjectures
(`conj:cl-general-chirality`, `conj:closed-string-cobar`), but Vol I has
already fingered five families as silent non-coverage. Not mirroring that
inscription is an AP215-type preface-advertising-stronger-than-proved
violation.

### (iii) Silent-non-coverage mirror — ABSENT

`ht_physical_origins.tex` contains neither the remark
`rem:census-silent-non-coverage` nor any analogue. Grep over
`chapters/connections/` for
`silent.{0,4}non.coverage` returns zero hits; the only matches in the Vol II
tree are `notes/swarm_vol2_dependency_dag_2026_04_17.md` and `AGENTS.md`.
HEAL TARGET: inscribe a Remark "HT landscape: honest frontier rows" listing
the same five families flagged in Vol I Rem `rem:census-silent-non-coverage`,
with each line saying what the 3d HT origin (currently) is NOT yet known to be.

### (iv) Yangian disambiguation (AP170) — MISSING FROM PART V

AP170 requires every file mentioning the Yangian to distinguish
`def:e1-chiral-yangian` (weaker: $E_1$-factorization + RTT) from
`def:chiral-yangian-datum` (stronger: $(\cA, S(z), \Delta^{\mathrm{ch}},
\{m_k\})$ + modular MC tower). The two definitions live in
`chapters/connections/line-operators.tex:2119-2121`,
`chapters/connections/dg_shifted_factorization_bridge.tex:2238-2239`,
`chapters/connections/ordered_associative_chiral_kd_core.tex:5072-5074`.
`ht_physical_origins.tex` cites `thm:yangian-recognition` twice (lines 292,
779) but NEVER resolves which of the two Yangian definitions the "dg-shifted
Yangian package" instantiates. From the architecture (ordered bar + line
operators), the target is `def:chiral-yangian-datum`; but the Part V reader
is not told so.
HEAL TARGET: insert a Remark near line 300 (inside the two-colour subsection)
explicitly pointing to both definitions and stating which one the HT landscape
recognition produces.

### (v) Cross-volume to Vol I Part III — RESOLVES

Spot check: `part:examples` (`main.tex:1589`), Theorem~A-D references in
`ht_physical_origins.tex:186-187`, `V1-thm:e1-module-koszul-duality`
(line 317), `V1-thm:verdier-bar-cobar` (line 699),
`V1-thm:bar-semi-infinite-km` (line 710), `V1-thm:bar-semi-infinite-w`
(line 715), `V1-thm:thqg-swiss-cheese` (line 755). All resolve to
phantomsection stubs in Vol II `main.tex` (verified via `part:examples`
matching `\ref{part:examples}`).

### (vi) Cross-volume to Vol III Part V "CY Landscape" — MISSING

Vol III `main.tex:983` has `\part{The CY Landscape}`. Vol II Part V chapters
contain zero references to Vol III Part V "CY Landscape". The 3d HT gauge
theories coming from CY compactification (local surface $\cN=2$ twist, CY3
DT, CY4 little-string) are the natural bridge; Part V should
cross-reference.
HEAL TARGET: insert a one-paragraph cross-volume note near the end of the
HCS subsection (line 593) pointing to Vol III "CY Landscape" for the
CY-geometric origins of the 3d HT theories listed per-family in Vol II
Part V.

### (vii) W(p) logarithmic tempered split — N/A

Part V does not discuss W(p). The split H^{reg} vs H^{log} lives in Vol II
`logarithmic_wp_tempered_analysis_platonic.tex`. Part V's silent-non-coverage
row for log $\cW(p)$ (heal item iii above) must SIMPLY point to that chapter
without re-inscribing the split here.

## Phase 2 Heal — surgical .tex edits

Target: `~/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex`.

1. After line 300 (end of `rem:ordered-mult-two-colour`): insert a Remark
disambiguating the two Yangian definitions (AP170).

2. After line 593 (end of `thm:hcs-dimensional-reduction`): insert a one-paragraph cross-volume bridge pointing to Vol III "CY Landscape".

3. Before the closing Dictionary subsection (before line 1552): insert the
silent-non-coverage mirror Remark.

## Heal audit trail

- Vol I canonical: `chapters/examples/landscape_census.tex:4260-4306`,
`rem:census-silent-non-coverage`.
- Vol II AP170 discipline: `line-operators.tex:2119-2121`,
`dg_shifted_factorization_bridge.tex:2238-2239`,
`ordered_associative_chiral_kd_core.tex:5072-5074`.
- Vol III cross-target: `~/calabi-yau-quantum-groups/main.tex:983`
`\part{The CY Landscape}`.
- `thm:yangian-recognition` resolves to
`~/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-core.tex:1922-1924`.

No commit. Heals applied to `ht_physical_origins.tex` only.
