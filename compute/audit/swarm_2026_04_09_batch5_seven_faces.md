# Adversarial Swarm 2026-04-09/10 — Batch 5: Seven Faces of r(z)

**Scope.** 10 agents, 10 distinct angles on the Seven Faces of r(z) claim across Vol I (Part V) and Vol II (Part III, bbl-core). Coordination via `reconciliation_learnings.md`.

## Authoritative canonical enumeration (Batch 5 discovery)

Both Vol I and Vol II use the SAME seven faces in the SAME order, contra initial CLAUDE.md speculation:

- **F1**: Bar-cobar twisting morphism (π_A ∈ Tw(B̄^ch(A), A)) — Vol I `thm:hdm-face-1` at `holographic_datum_master.tex:202-229`
- **F2**: DNP25 line-operator r-matrix (dg-shifted Yangian) — `holographic_datum_master.tex:237-298`
- **F3**: Khan-Zeng 2025 classical PVA λ-bracket — `holographic_datum_master.tex:300-371`
- **F4**: Gaiotto-Zeng 2026 commuting sphere Hamiltonians — `holographic_datum_master.tex:372-440`
- **F5**: Drinfeld 1985 Yangian r-matrix — `holographic_datum_master.tex:441-511`
- **F6**: Semenov-Tian-Shansky 1983 Sklyanin Poisson bracket — `holographic_datum_master.tex:513-585`
- **F7**: Feigin-Frenkel-Reshetikhin 1994 Gaudin Hamiltonians — `holographic_datum_master.tex:586-654`

**Master theorems:** Vol I `thm:seven-faces-master` at `holographic_datum_master.tex:136-164`; Vol II `thm:seven-face-master-3d-ht` at `dnp_identification_master.tex:209-239`. Both ClaimStatusProvedHere. Same seven faces, same order, same attributions.

## CRITICAL: CLAUDE.md canonical reference is WRONG

`CLAUDE.md` line 770 says:
> "Part V (Seven Faces of r(z): R-matrix, Yangian, Sklyanin, DK, celestial, holographic)"

This is **factually incorrect on three counts**:
1. Only 6 items listed, not 7 (numerical mismatch with "Seven")
2. "DK", "celestial", "holographic" are NOT among the seven faces — they are **separate chapters** elsewhere in Part V / Part III
3. The actual F3 (Khan-Zeng PVA), F4 (GZ26 sphere Hamiltonians), F7 (FFR94 Gaudin) are ENTIRELY MISSING from the CLAUDE.md shorthand

AP115 violation: architectural CLAUDE.md claim not enacted in .tex. Per the CLAUDE.md dictum "metadata-source gap is the most dangerous anti-pattern".

**Fix**: update CLAUDE.md line 770 to: "Part V (Seven Faces of r(z): bar-cobar twisting, DNP25, KZ25, GZ26, Drinfeld, Sklyanin/STS83, FFR94 Gaudin)".

## 10-angle verdict table

| # | Angle | Verdict | Key finding |
|---|---|---|---|
| 1 | Face count audit | SEVEN-PROVED (CLAUDE.md miscount) | Both volumes have 7 faces; CLAUDE.md parenthetical lists 6 wrong items |
| 2 | F1 R-matrix / bar-cobar face | FACE-PROVED (identification, new for Vir/W_N) | AP126 violation at L448-456 (bare Ω/z); av(r)=κ not proved in face chapter; FM11 Sugawara not addressed |
| 3 | F5 Yangian face | FACE-CONDITIONAL-ON-DK45 | Hbar-deformation NOT derived; imported from Drinfeld 1985. AP126 bare Ω/z at L448. Master-theorem headline drops DK-4/5 qualifier |
| 4 | F6 Sklyanin face | FACE-LITERATURE-ONLY (rational only) | Vol I genus-0 reduces to citation chain; Sklyanin 1982 eight-vertex R-matrix NOT in bibliography; elliptic case is Belavin-Drinfeld 1982 in `genus1_seven_faces.tex`, not Sklyanin-labeled |
| 5 | DK face | FACE-OVERCLAIMS-DK45 | DK ladder in `thqg_line_operators_extensions.tex:1526-1530` claims "DK-4 Proved" by citing `thm:completed-bar-cobar-strong` but DK-4 IS part of `conj:dk-compacts-completion`. DK is NOT a face — it's a hierarchy |
| 6 | Celestial face | FACE-METAPHORICAL | Celestial NOT in the seven-face master theorem at all! Lives in `celestial_holography_core.tex` as `conj:modular-twisted-celestial`. Two "thm:" labels on `\begin{evidence}` environments (AP125 violation) |
| 7 | Holographic face | FACE-PARTIAL-WITH-GAP | `prop:hdm-u-a-recoverability` is Heuristic; 4 recovery theorems exist and are proved at low arity; global Drinfeld double assembly conjectural beyond Koszul locus |
| 8 | 7th face identification | CLAUDE.md SHORTHAND IS STALE | No hidden 7th face; CLAUDE.md list is obsolete/wrong |
| 9 | Cross-volume consistency | CONSISTENT on content, MINOR-DRIFT on linkage | Same 7 faces in both volumes; no explicit master-theorem cross-reference; Vol I Face 2 proof delegates to Vol II with loose citation |
| 10 | Honest reformulation | COMPLETE LaTeX ready to apply | 7-face honest theorem with explicit face-by-face status tags |

## New critical findings

### F17 — CLAUDE.md Seven Faces parenthetical is stale (AP115)

`CLAUDE.md:770` lists "R-matrix, Yangian, Sklyanin, DK, celestial, holographic" as the Seven Faces. None of these match the actual faces F1-F7. The real faces are bar-cobar twisting, DNP25, KZ25, GZ26, Drinfeld, Sklyanin, FFR94-Gaudin. This is a metadata-source gap; the canonical reference document is wrong about the most distinctive Part V claim.

### F18 — AP126 violations in Seven Faces chapters

1. `holographic_datum_master.tex:448-456` eq:hdm-drinfeld-rmatrix: `r^{Dr}(z) = \Omega/z` with bare Ω (no level prefix). Fails k=0 check nominally; the surrounding context at L471 does have `1/(k+h^v)` Sugawara-shifted form, but the Drinfeld quote equation itself violates HZ-1.
2. `holographic_datum_master.tex:476, 496, 568, 633, 739, 2309`: affine KM collision residue written as `Ω/((k+h^v)z)` divisor-denominator form rather than canonical `k·Ω/z`. Sugawara-absorbed convention; inconsistent within the same chapter (L544, 559, 935 do use canonical `kΩ/z`).
3. `compute/lib/twisted_holography_amplitudes.py:24`: `r(z) = Omega/z` bare in comment/docstring.

### F19 — AP125 violations in celestial chapter

`celestial_holography_core.tex:961` and `:989` — labels `\label{thm:ch-core-celestial-gluon-ope}` and `\label{thm:ch-core-celestial-graviton-ope}` on `\begin{evidence}[...; \ClaimStatusHeuristic]` environments. Per HZ-5, `thm:` prefix must match `\begin{theorem}`; these should be `ev:` or demoted to `rem:`. This misleads any agent grepping `thm:` to enumerate proved theorems — both are explicitly heuristic.

### F20 — Missing celestial-CFT citations

`celestial_holography_core.tex` body does NOT cite the Costello-Paquette line (`CostelloP2201`, `CPS2208`, `CPS2306`, `Costello2302`, `FernandezCostelloP24`) despite all being in the main bibliography. The celestial OPE derivation pattern-matches to the Pasterski-Shao-Strominger graviton OPE but PSS is **mentioned in prose at L1001 without a `\cite`**. Donnay-Puhm-Strominger and Bhardwaj-Nahm not in bibliography at all. Vol II's celestial programme is citationally under-supported relative to its claims.

### F21 — Sklyanin 1982 missing from bibliography

The eight-vertex elliptic R-matrix of Sklyanin 1982 is **not in either bibliography** (only `Belavin81` and `BelavinDrinfeld82`). The F6 "Sklyanin" face is about the 1983 Semenov-Tian-Shansky rational Poisson bracket, not Sklyanin's 1982 R-matrix. Terminology mismatch: calling the face "Sklyanin" without citing Sklyanin's eponymous paper.

### F22 — F5/F7 redundancy

`thm:hdm-face-7` at L625-626 literally says `H_i^{Gaudin} = (k+h^v)·H_i^{GZ}` — F7 is an algebraic rescaling of F4, not an independent face. This preserves the "Seven" count only by convention; mathematically there are 6 independent structural realizations plus one rescaling.

### F23 — F3 higher-genus conjectural

`thm:kz-classical-quantum-bridge` at `frontier_modular_holography_platonic.tex:1806-1808` clause (iv) literally states "At higher genus, the geometric-algebraic identification is conjectural". Depends on `conj:master-bv-brst`. The Seven Faces master theorem statement at L136-164 does NOT qualify F3 with this conjectural higher-genus clause — propagation gap.

### F24 — F4 W_N normalization-convention gap

`thm:gz26-commuting-differentials` clause (v) is a "prediction" not a theorem; `rem:gz26-wn-comparison-conjectural` at L1612-1618 admits the term-by-term W_N comparison with GZ26 operators depends on an unestablished normalization convention. Again not reflected in the master theorem statement.

### F25 — DK is not a face, it's a hierarchy

CLAUDE.md lists "DK" as one of the seven faces but the manuscript never treats DK as a face. DK-0 through DK-5 is a **ladder** in `thqg_line_operators_extensions.tex:1487-1563`, with DK-0/1/2 proved all types, DK-3 proved type A, DK-4 OVERCLAIMED (see F26), DK-5 Frontier. The "DK face" is an error in CLAUDE.md.

### F26 — DK-4 overclaim

`thqg_line_operators_extensions.tex:1526-1530` states: "DK-4 (completed bar-cobar equivalence): the completed bar-cobar adjunction gives an equivalence on pro-categories. Proved by the MC4 strong completion-tower theorem (Vol I, Theorem thm:completed-bar-cobar-strong)."

This is an overclaim. `thm:completed-bar-cobar-strong` is the ALGEBRAIC MC4 theorem on the chiral-algebra side. DK-4 as defined ("pro-category equivalence on the line-operator/quantum-group side") is a REPRESENTATION-THEORETIC statement that is part of `conj:dk-compacts-completion` (Conjectured at `yangians_computations.tex:3498`). Conflation of two different objects.

## Batch 5 convergent recommendations

### Immediate fixes (concrete, low-risk)

1. **CLAUDE.md:770** — rewrite the Part V parenthetical to list the actual seven faces (bar-cobar, DNP25, KZ25, GZ26, Drinfeld, Sklyanin/STS83, FFR94-Gaudin). Drop "DK, celestial, holographic" from the list — these are separate chapters, not faces.

2. **AP126 sweep in Seven Faces chapters** — fix the 3 violations in `holographic_datum_master.tex` (L448, L476 area) and `compute/lib/twisted_holography_amplitudes.py:24`. Canonical form `k·Ω/z`.

3. **AP125 sweep in celestial chapter** — rename `\label{thm:ch-core-celestial-gluon-ope}` → `\label{ev:ch-core-celestial-gluon-ope}` and same for graviton (or demote to remarks).

4. **Add Costello-Paquette citations to celestial body** — the bibliography has them; `celestial_holography_core.tex` body just fails to cite them at the OPE derivation sites.

5. **Add Pasterski-Shao, Donnay-Puhm-Strominger, Sklyanin 1982 bibitems** — missing from main bibliography.

### Structural fixes (require coordination)

6. **Seven Faces master theorem rewrite** (Angle 10) — replace `thm:seven-faces-master` body with the honest reformulation that carries explicit face-by-face status: F1 unconditional, F2 imported from Vol II, F3 genus-0 only + higher-genus conjectural, F4 KM+Vir only + W_N conjectural, F5/F6/F7 identification + classical theory imported. Complete LaTeX at `swarm_2026_04_09_batch5_seven_faces.md` referenced below.

7. **DK-4 downgrade** — fix `thqg_line_operators_extensions.tex:1526-1530` to mark DK-4 as part of `conj:dk-compacts-completion`, not as discharged by the algebraic MC4 theorem. Separate obligation from Batch 4's MC3 status downgrade.

8. **Vol II preface boundary-bulk hedging** (F15 from reconciliation) — still unfixed, now also affects Seven Faces Face 7 (Holographic) which inherits the boundary-bulk thesis framing.

## Honest reformulation of Seven Faces theorem (Angle 10 deliverable)

Full LaTeX in the Angle 10 report. Key structural features:
- Genericity hypothesis `k ≠ -h^v` explicit
- Each face carries its own status tag (unconditional / genus-0 / KM+Vir / generic level / imported)
- F1 is unconditional (subject to Theorem B def pivot)
- F2 marked as Vol II import
- F3 clause (iv) conjectural marker preserved
- F4 W_N remark preserved
- F5 identification + Drinfeld imported split
- F6 identification + STS imported split
- F7 stated as (k+h^v)·F4 rescaling explicitly
- "Agreement diagram commutes on the chirally Koszul locus at every face marked unconditional"

Ready to apply atomically to both `holographic_datum_master.tex:136-164` and `dnp_identification_master.tex:209-239` with volume-suffixed labels `thm:seven-faces-honest-v1` and `thm:seven-faces-honest-v2`.

## Batch 5 deliverable inventory

All 10 Batch 5 deliverables are ready-to-apply or actionable:

| # | Deliverable | Target | Ready? |
|---|---|---|---|
| 1 | CLAUDE.md Seven Faces correction | CLAUDE.md:770 | ✅ |
| 2 | AP126 sweep (3 sites) | `holographic_datum_master.tex` + compute/lib | ✅ |
| 3 | AP125 rename (2 sites) | `celestial_holography_core.tex:961,989` | ✅ |
| 4 | CP citation add (multiple sites) | `celestial_holography_core.tex` body | ✅ |
| 5 | 3 new bibitems (Pasterski-Shao, Donnay-Puhm-Strominger, Sklyanin82) | `bibliography/references.tex` | ✅ |
| 6 | Seven Faces honest reformulation | `holographic_datum_master.tex:136-164` + `dnp_identification_master.tex:209-239` | ✅ |
| 7 | DK-4 downgrade in ladder | `thqg_line_operators_extensions.tex:1526-1530` | ✅ |
| 8 | F3 higher-genus conjectural qualifier hoisted to master theorem | `thm:seven-faces-master` | ✅ |
| 9 | F4 W_N remark hoisted to master theorem | same | ✅ |
| 10 | F7 as (k+h^v)·F4 rescaling explicit in master theorem | same | ✅ |

## Open items for Batch 6+

- **Vol II Seven Faces CHAPTERS deep audit** (beyond master theorem): each of `dnp_identification_master.tex`, `spectral-braiding-core.tex`, `ht_bulk_boundary_line_core.tex`, `celestial_boundary_transfer_core.tex`, `affine_half_space_bv.tex`, `fm3_planted_forest_synthesis.tex`, `kontsevich_integral.tex` — are these the "additional material" chapters, not faces, or do they overlap?
- **Genus-1 Seven Faces** (`genus1_seven_faces.tex`): elliptic version, different Face 5 (Belavin-Drinfeld elliptic), needs separate audit.
- **Compute engine for seven-face agreement**: `theorem_seven_face_categorification_engine.py` + `theorem_three_way_r_matrix_engine.py` — do their test assertions match the seven authoritative faces or the CLAUDE.md wrong-six?
- **Vol III Seven Faces r_CY** per CLAUDE.md Vol III "IV (Seven Faces r_CY)" — does Vol III have its own seven faces, and how do they relate?
