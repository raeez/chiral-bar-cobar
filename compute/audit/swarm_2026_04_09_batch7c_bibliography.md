# Adversarial Swarm 2026-04-09/10 — Batch 7c: Full Bibliography Audit (3 volumes)

**Scope.** 10 agents across all three volumes' bibliographies: wrong titles, misattributed authors, fabricated entries, missing citations, alias clusters, arXiv ID plausibility, literature baseline completeness.

## Master verdict — bibliography is the WEAKEST layer of the programme

Three classes of catastrophic-scale problems found:

### Class 1: MANUSCRIPT-BLOCKING defects

**C1.1 — Vol III HAS NO BIBLIOGRAPHY.** `/Users/raeez/calabi-yau-quantum-groups/main.tex:508-509`:
```
\bibliographystyle{alpha}
% \bibliography{references}
```
The `\bibliography` line is commented out. **Zero `.bib` files exist** anywhere under `calabi-yau-quantum-groups/`. No `references.tex`. No `\input` of Vol I's bibliography. **Every Vol III `\cite{...}` currently emits `[?]` at build time.** 18 of 26 Vol III cite keys are dangling even if Vol I's bib were re-enabled. This is not a polish item — Vol III is not citation-resolvable.

**C1.2 — `CFG25` is FABRICATED and propagated cross-volume.** Vol I `bibliography/references.tex:340-341` and Vol II `main.tex:2074-2075` both contain:
```
\bibitem{CFG25}
K. Costello, J. Francis, and O. Gwilliam,
"Chiral Koszul duality", arXiv:2602.12412, 2026.
```
**This paper does not exist.** The title "Chiral Koszul duality" is Francis-Gaitsgory 2012 (already correctly `FG12`). Costello and Gwilliam are not coauthors. arXiv:2602.12412 is future-dated and invalid (Feb 2026, well beyond current arXiv numbering as of 2026-04-10). **Recommendation: delete in both volumes; replace `\cite{CFG25}` with `\cite{FG12}`** wherever cited.

**C1.3 — `Nish26` has LITERAL PLACEHOLDER arXiv ID.** `bibliography/references.tex:1243` contains `arXiv:2512.xxxxx` — the literal string "xxxxx". 23 downstream `\cite{Nish26}` instances across 9 Vol I files (`higher_genus_modular_koszul.tex` ×8, `concordance.tex` ×8, plus 7 more). Batch 7a Angle 4 found `thm:platonic-adjunction` (`higher_genus_modular_koszul.tex:26593`) is "ProvedHere" but its existence rests on Nishinaka 2026 (Single-point dependency + placeholder arXiv ID = AP11 × 2).

### Class 2: CRITICAL title / author / content misattributions

**C2.1 — Huang 2005 is wrong** (Vol I). `bibliography/references.tex:675-676`:
```
Y.-Z. Huang, "Differential equations and intertwining operators",
Comm. Contemp. Math. 7 (2005), no.3, 375-400, arXiv:math/0502533.
```
- arXiv:math/0502533 is actually titled "Differential equations, duality and modular invariance" published at **CCM 7 (2005) no.5, 649-706**
- The title "Differential equations and intertwining operators" is a DIFFERENT Huang paper (arXiv:math/0301068)
- Current entry mismatches title + pagination with the arXiv ID

**C2.2 — Vol II `Huang2005` is a THIRD Huang paper** (Verlinde conjecture / PNAS / math/0412261), distinct from both Vol I `Huang05` intentions. **math/0502533 (the canonical MC5 sewing comparison paper) is MISSING from Vol II entirely.**

**C2.3 — Mok25 author misattributed across THREE volumes.** Vol I `references.tex:928`, Vol II `main.tex:1745,1750,1753`, `compute/lib/theorem_concordance_rectification_engine.py:91` all say "S. C. Mok". Canonical is "C.-P. Mok" (Chung-Pang Mok, Purdue) per `standalone/references.bib:569`. Standalone programme summaries use "L. Mok" (also wrong). Vol III `modular_koszul_bridge.tex:23` inherits the wrong attribution.

**C2.4 — `LuninMathur2001` wrong first initial.** Vol I `references.tex:1401-1402`: "S. D. Lunin" — should be "O. Lunin" (Oleg Lunin).

**C2.5 — `BPRS15` key/content mismatch.** Vol I `references.tex:202-203`: key suggests 4 authors (Beem-Poland-Rychkov-Simmons-Duffin) but content has 3 (Poland-Rychkov-Vichi). Published 2019, key says 2015.

**C2.6 — `HerNeg24` title likely fabricated.** Vol I `references.tex:648-649`: Hernandez-Negut CMP 379 (2020) 189-215 paper title given as "Shifted quantum groups and matter multiplets" — does not match any Hernandez-Negut publication.

**C2.7 — Vol II `CG18` vs `Costello-Gaiotto18` HYPHEN-ONLY COLLISION.** Vol II `main.tex:1490` (`CostelloGaiotto18`, no hyphen) → arXiv:1812.09257 Twisted Holography. Vol II `main.tex:2077` (`Costello-Gaiotto18`, with hyphen) → arXiv:1804.06460 VOAs and 3d N=4. **Two physically distinct papers differing only by a hyphen in the cite key**. Any author typing `\cite{Costello-Gaiotto18}` expecting "Twisted Holography" silently gets "VOAs and 3d N=4". Silent-citation-corruption hazard.

**C2.8 — Vol II `DNP25` arXiv ID drift.** `main.tex:1504` (`DNP25`) cites arXiv:2506.09728. `main.tex:1506` (`DNP2025`) cites arXiv:2508.11749. Same title, same authors (Dimofte-Niu-Py), different arXiv IDs. Vol I uses 2508.11749. Vol II `DNP25` is wrong.

### Class 3: SYSTEMIC missing literature baseline

**C3.1 — Borcherds 1986 (original VOA definition) MISSING from Vol I.** Vol I has only `Bor92` Monstrous Moonshine (the successor paper). The foundational "Vertex algebras, Kac-Moody algebras, and the Monster" PNAS paper — the defining reference for VOA — is absent. Cited implicitly throughout the manuscript.

**C3.2 — Witten 2007 "Three-dimensional gravity revisited" (arXiv:0706.3359) MISSING.** Vol II Part VI's 3D gravity climax relies on it via Maloney-Witten 2010 but never directly cites Witten 2007. Load-bearing for the Brown-Henneaux crown proposition at `higher_genus_modular_koszul.tex:2839`.

**C3.3 — Vol III 7 missing references (confirmed from Batch 6)**:
- Kapranov 2015 "Chiral algebras from Calabi-Yau manifolds" — direct precursor to Vol III's Φ functor
- Kapustin-Rozansky-Saulina 2009 (arXiv:0810.5415) — Conjecture CY-C is literally restated KRS
- Costello-Gaiotto 2018 (arXiv:1804.06460) — CG19 Φ for Higgs branches IS Vol III's Φ
- Davison 2017 (arXiv:1602.02110) — BPS algebras integrality
- Borcherds 1995 product formula — load-bearing for K3×E BKM denominator narrative
- Maulik-Nekrasov-Okounkov-Pandharipande 2006 — GW/DT correspondence
- Okounkov-Reshetikhin 2003 — Schur process / Nekrasov partition

**C3.4 — Vol II Seven Faces 11 missing references (from Batch 7b)**:
- Finkelberg-Tsymbaliuk 2017 (shifted Yangians) — Face 5
- Sklyanin 1982 (eight-vertex R-matrix) — Face 6 terminology mismatch
- Etingof-Varchenko 1998 (E_{τ,η}(sl_2)) — Face 6 elliptic case
- Talalaev 2006 (quantum Gaudin) — Face 7
- Rybnikov 2006 (Bethe algebras) — Face 7
- Calogero 1975, Moser 1975, Etingof-Felder-Ma 2009, Olshanski 2002 — Face 4 integrable systems baseline
- Pasterski-Shao 2017, Donnay-Puhm-Strominger 2018 — celestial face
- Felder 1994 — **present** (found as `Fel94`, Batch 7b was wrong to flag)

**C3.5 — Kontsevich-Soibelman 2008 motivic DT (arXiv:0811.2435)** — referenced inline in `standalone/shadow_towers.tex:2287` but no `\bibitem` in Vol I, II, or III. Load-bearing for Vol III ζ-DT and pentagon identity claims.

**C3.6 — Joyce-Song 2011 + Davison 2017** — referenced by name in 6+ Vol III prose files and Vol I standalone with **zero `\cite{}` instances anywhere**.

## 10-angle summary table

| # | Angle | Verdict | Key findings |
|---|---|---|---|
| 1 | Vol I wrong titles | 7 confirmed issues | Huang05, CFG25, LuninMathur, BPRS15, HerNeg24, Mok25, 8 forward-dated 2026 entries |
| 2 | Vol I missing citations | 30 undefined-but-cited, 57 dead | Top concentration: holography chapters; alias clusters for Costello-Gaiotto / Nakajima / Polchinski |
| 3 | Vol II wrong titles | 8+ issues | Mok25 wrong author (propagated from Vol I); CG18 hyphen collision (critical); DNP25 arXiv drift; 3× CDG20 aliases, 4× CG18 aliases |
| 4 | Vol II missing citations | 17 undefined, 26 dead | Top: `thqg_line_operators_extensions.tex` (10 of 17 undefined); Felder 1994 IS present contra Batch 7b |
| 5 | Vol III wrong titles | N/A | No bibliography to be wrong in |
| 6 | Vol III missing citations | **STRUCTURAL ABSENCE** | `\bibliography` commented out in main.tex:509; zero .bib files; 18 of 26 cite keys dangling |
| 7 | Cross-volume consistency | DRIFT on 12 of 12 checked papers | Huang, Mok, CDG, CG, DNP all differ across volumes; `CFG25` fabrication propagated |
| 8 | arXiv ID plausibility | 8 forward-dated + 2 placeholders + 1 suspicious serial | `Nish26` literal `2512.xxxxx`; `Nafcha` serial 30037; `DNP25` Vol II wrong arXiv |
| 9 | Literature baseline completeness | Major gaps in 6 of 8 areas | Borcherds 1986, Witten 2007, KS 2008, Joyce-Song, Davison, Kapranov, KRS all missing at the load-bearing level |
| 10 | Synthesis + fix plan | 28 items, ~50-55 touches | Tiered plan: 2 in-place corrections + 26 new bibitems; ready-to-apply LaTeX for Tier 1-3 |

## Batch 7c deliverable: 28-item fix plan

**Tier 1 — CRITICAL in-place corrections** (don't change keys):
1. Huang05 title/pagination fix (Vol I) — ready LaTeX supplied
2. Mok25 author fix (Vol I + Vol II + compute engine) — ready LaTeX supplied
3. Delete `CFG25` (Vol I + Vol II) + replace `\cite{CFG25}` with `\cite{FG12}`
4. Fix `Nish26` arXiv ID placeholder or mark `\ClaimStatusConditional` on all 23 downstream citing theorems
5. Fix Vol II `DNP25` arXiv ID drift

**Tier 2 — CRITICAL missing for proved theorems** (add bibitems + wire citations):
6. Huang05b (PNAS announcement, math/0412261) + Huang08 (CCM 10)
7. Kapranov 2015 "Chiral algebras from CY manifolds" — Vol III
8. Kapustin-Rozansky-Saulina 2009 — Vol III (CY-C direct precursor)
9. Costello-Gaiotto 2018 VOAs (arXiv:1804.06460) — Vol III
10. Davison 2017 integrality — Vol III
11. Borcherds 1986 original VOA — Vol I
12. Witten 2007 3D gravity revisited — Vol II

**Tier 3 — HIGH chapter prose** (existing citations that need wiring):
13-24. Pasterski-Shao, Donnay-Puhm-Strominger, Sklyanin82, Felder94 (actually present), EV98, Talalaev06, Rybnikov06, FinkelbergTsymbaliuk17, Costello-Paquette celestial citations, Calogero75, Moser75, EFM09, Olshanski02

**Tier 4 — Alias consolidation**:
25. CDG20 (3 aliases → 1)
26. CG18 (4 aliases → 1) — critical because of hyphen collision in Vol II

**Tier 5 — MED precursors**:
27. Borcherds 1995 product formula, MNOP 2006, Okounkov-Reshetikhin 2003
28. Kontsevich-Soibelman 2008 motivic DT, Joyce-Song 2011, Bridgeland 2007, Bondal-van den Bergh, Keller-Vossieck

**Estimated: 50-55 file touches across ~12 files**. Tier 1 is ~5 touches. Tier 2 is ~10 touches. Tiers 3-5 are ~35-40 touches.

## New critical findings (F54-F63)

**F54 — Vol III has NO bibliography** (C1.1). Manuscript-blocking defect.

**F55 — `CFG25` is fabricated** (C1.2). Cross-volume propagated fabrication — the "Chiral Koszul duality" title is plagiarized from Francis-Gaitsgory 2012 with Costello/Gwilliam added as fake coauthors and a future arXiv ID.

**F56 — `Nish26` has literal placeholder arXiv `2512.xxxxx`** (C1.3). Cited 23 times.

**F57 — Vol II `DNP25` arXiv ID drift** (C2.8). `DNP25` and `DNP2025` cite different arXiv numbers for the same paper.

**F58 — Vol II `CG18` hyphen collision** (C2.7). Silent-citation-corruption hazard: hyphen-only distinction between two physically distinct papers.

**F59 — 8 forward-dated 2026 papers in Vol I**: CFG25, Moriwaki26a/b, Nafcha, CDN26, LQ26, GZ26, Nish26. At least CFG25 and Nish26 are confirmed problematic; the other 6 need independent arXiv verification.

**F60 — Borcherds 1986 (original VOA definition) MISSING from Vol I**. Only `Bor92` Monstrous Moonshine (the successor paper) is present.

**F61 — Witten 2007 "3D gravity revisited" MISSING**. Vol II's gravity climax doesn't cite the foundational paper.

**F62 — Vol I has 30 undefined-but-cited keys + 57 dead bibitems** across 2510 `\cite{}` calls. Top undefined concentration in holography/black-hole chapters.

**F63 — `LuninMathur2001`, `BPRS15`, `HerNeg24` all have wrong authors/titles** (Tier A findings beyond the already-flagged Huang05/Mok25/CFG25).

## Cross-batch implications

**For reconciliation ledger F1-F16**:
- F55 (CFG25 fabricated) is a new class: fabricated entry with plagiarized title
- F56 (Nish26 placeholder) extends F36 (Nishinaka 2026 single-point dependency) to a bibliography-format issue
- F60, F61 are new MISSING precursors beyond the Vol III 7 found in Batch 6
- F54 (Vol III no bibliography) is worse than "gap" — it's a structural absence

**For Batch 4 Huang/Mok plan (items 5, 6)**:
- Batch 4 Angle 5 correctly identified the Huang wrong title and Mok wrong author
- Batch 7c confirms and adds: Huang has ~3 concurrent 2005 papers with confusable titles, and the `CG18` Vol II collision compounds the citation corruption risk
- Batch 4 fix for Huang/Mok should proceed as planned but also include `CFG25` deletion and Vol II `DNP25` arXiv ID correction

**For Batch 6 Vol III 7-missing (items 10)**:
- Batch 6 correctly identified 7 missing Vol III references
- Batch 7c confirms all 7 + adds Borcherds 1986, Witten 2007, KS 2008, JoyceSong 2011 to the universal missing list
- **But this is moot until Vol III bibliography is re-enabled** (C1.1)

**For Batch 7a U^mod_X findings (F36)**:
- Nishinaka 2026 was flagged as single-point external dependency
- Batch 7c finds the arXiv ID is literally `2512.xxxxx` placeholder — not just a single-point dependency but a MISSING citation
- The 23 Vol I files citing `Nish26` currently have dangling citations at the bibliography-resolution level

## Open items for Batch 8+

- **Independent arXiv verification** of the 8 forward-dated Vol I entries (CFG25 confirmed fabricated, others need external check)
- **Vol III bibliography creation**: either uncomment `\bibliography{references}` and create the file, or add inline `thebibliography` block
- **CG18 disambiguation** in Vol II: rename one of the hyphen-colliding keys
- **Compute engine sweep** for "Mok25" author string mismatches
- **Fabricated-entry audit protocol** going forward: any "Costello-Francis-Gwilliam" authorial combination should trigger cross-check, given CFG25 fabrication pattern
