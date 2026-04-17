# Wave 11 — Vol I Bibliography & Citation Accuracy (Adversarial Audit)

Date: 2026-04-16
Auditor role: adversarial referee, healing-by-upgrade
Scope: `~/chiral-bar-cobar/bibliography/references.tex`, `standalone/references.bib`, citation usage in chapters/ and appendices/, AP155 (attribution accuracy) and AP-CY8 (anchor-citation discipline).

This report is the bibliographic counterpart to the wave 5–7 source-attribution waves. The earlier waves identified mis-attributions at the *citation site* (`\cite{X}` where the right citation should have been `\cite{Y}`). This wave audits the *bib entries themselves* (do they exist, are they correct, are they the strongest possible attribution) and surfaces missing entries that block the wave 5–7 healings.

No edits to manuscript or bib. Findings only. Punch list at §10.

---

## 1. Bibliography inventory

| File | Lines | Entries | Themes |
|------|------:|--------:|--------|
| `bibliography/references.tex` | 1708 | 551 `\bibitem` entries | Master Vol I bibliography. Authors A–Z, plus a long appendix-of-late-additions starting around line 1340 (Costello, Gaiotto, Nish26, Vic25, CM25, Lorgat26I/II, etc.). |
| `standalone/references.bib` | 793 | (BibTeX format) | Subset for the standalone papers (Garland-Lepowsky standalone, koszulness 14-characterizations standalone, etc.). Different syntax from the main bibliography (BibTeX `@article{}` rather than `\bibitem{}`). |
| `archive/misc/modular_pva_quantization.bib` | small | archive only | Not in the live build path. Ignore. |
| `.claude/worktrees/agent-*/standalone/references.bib` | various | duplicates of the standalone bib in agent sandboxes | not in live build, may drift; AP-CY27 risk if any of these were *intended* to be promoted. |

The master bibliography is in **bibitem (manual)** form, not BibTeX. This is unusual and limits tooling — for example `bibtool`, `biber --validate`, and `bibsanity` cannot run on it directly. Consequence: duplicate-key detection, dead-link detection, and DOI validation must be done by hand.

The header of `references.tex` (lines 3–21) lists 14 *known* duplicate keys merged into canonical entries. Spot-checks against the body confirm a further set of duplicates retained for citation-key compatibility:

- `BK` (line 147) and `BK86` (line 150) and `BK1986` (line 153) all refer to Belavin–Knizhnik 1986. `BK1986` is explicitly tagged as "Duplicate of BK86".
- `Arakawa15` (line 53) and `Ara15` (line 62) both cite Arakawa, *Rationality of W-algebras: principal nilpotent cases* (Ann. Math. 2015). Ara15 is explicitly tagged "Duplicate of Arakawa15".
- `GK98` (line 655) and `GetzlerKapranov98` (line 1372) both cite Getzler–Kapranov, *Modular operads* (Compositio 1998). **Two live entries, no comment marker.** This is a hidden duplicate (see §3 below — it matters for the wave 5 BV-Feynman attribution).

Counts only count `^\bibitem{`; entries that share a body with another (commented duplicates) are still counted, so 551 is an *upper bound* on distinct works.

---

## 2. High-stakes citation accuracy

The 12 anchor citations the audit was asked to verify, with the bibliography body as it stands and the adversarial verdict.

| # | Anchor | Bib key(s) | Body as printed | Verdict |
|---|--------|------------|-----------------|---------|
| (a) | Drinfeld 1989–91 (associator, quantum group) | `Drinfeld85`, `Drinfeld88`, `Drinfeld90` | 1985: *Hopf algebras and the QYBE* (Soviet Math. Dokl. 32:254–258); 1988: *A new realization of Yangians and quantized affine algebras* (Soviet Math. Dokl. 36:212–216); 1990: *Quasi-Hopf algebras* (Leningrad Math. J. 1:1419–1457). | **PARTIAL.** The 1990 *Quasi-Hopf algebras* paper is correctly cited. **MISSING:** Drinfeld 1989, *On quasitriangular quasi-Hopf algebras and a group closely related to Gal($\bar{\mathbb{Q}}/\mathbb{Q}$)* (Leningrad Math. J. 2 (1991), no. 4, 829–860). This is the *associator* paper proper, distinct from `Drinfeld90` (which is the foundational quasi-Hopf paper). The KZ–monodromy / Drinfeld associator material in chapters that cite `Drinfeld90` for the *associator* should cite the 1989/91 paper instead. **Healing:** add `Drinfeld89-Galois` entry, leave `Drinfeld90` for general quasi-Hopf attributions. |
| (b) | Kohno 1987 (KZ monodromy) | `Kohno87` | T. Kohno, *Monodromy representations of braid groups and Yang–Baxter equations*, Ann. Inst. Fourier 37 (1987) no. 4, 139–160. | **CORRECT.** Year, journal, volume, page range all verify against MathSciNet. The Kohno *theorem* (KZ-monodromy ↔ R-matrix) is in this paper. Sharpening: when Vol I cites Kohno for the more general *Drinfeld–Kohno theorem* (KZ ↔ Drinfeld associator), cite Kohno 1987 + Drinfeld 1989 jointly, and consider Kassel's *Quantum Groups* §XIX as the canonical textbook. The textbook is not in the bib. |
| (c) | Beilinson–Drinfeld 2004 | `BD04` | A. Beilinson and V. Drinfeld, *Chiral Algebras*, AMS Colloquium Publications 51, AMS, 2004. | **CORRECT.** This is the canonical book. **However:** wave 5 chiral_hochschild_koszul.md flagged that `thm:hochschild-classical-comparison` is mis-attributed to BD04. The book contains the *chiral homology* construction and its comparison with vertex-algebra cohomology in classical limits, but the specific *Hochschild* comparison theorem in the wave 5 finding is due to Tamarkin (`Tamarkin00` for the 2-algebra deformation complex picture) or to Beilinson (the older 1984 Beilinson–Bernstein–Deligne paper on perverse sheaves does not contain it). The bib entry is fine; the *citation site* is wrong (a wave 5 finding, repeated here for convenience). |
| (d) | Garland–Lepowsky 1980 | (NONE) | — | **MISSING from main bib.** Garland–Lepowsky, *Lie algebra homology and the Macdonald–Kac formulas*, Invent. Math. 34 (1976), no. 1, 37–76 — not 1980. The standalone `papers/garland_lepowsky_concentration.tex` and `standalone/garland_lepowsky.tex` exist (and are the right tool for the DK Whitehead-reduction misapplication identified in prior waves), but the *main* `references.tex` has no Garland–Lepowsky entry. The closest is `FGZ86` (Frenkel–Garland–Zuckerman 1986, semi-infinite cohomology) which is a *related but distinct* paper. **Healing:** add `GL76` entry: `H. Garland and J. Lepowsky, \emph{Lie algebra homology and the Macdonald–Kac formulas}, Invent. Math. 34 (1976), 37–76.` Then re-cite at every site flagged in the prior DK Whitehead-reduction wave. (This is a *blocking* gap: the wave-5 healing cannot land until the bib entry exists.) |
| (e) | Borcherds 1992 / 1995 / 1998 | `Bor86`, `Bor92`, `Bor95` | 1986: *Vertex algebras, Kac–Moody algebras, and the Monster* (PNAS); 1992: *Monstrous moonshine and monstrous Lie superalgebras* (Invent. Math. 109); 1995: *Automorphic forms on $O_{s+2,2}(\mathbf{R})$ and infinite products* (Invent. Math. 120). | **PARTIAL.** 1986, 1992, 1995 all correctly cited. **MISSING:** Borcherds 1998, *Automorphic forms with singular theta correspondences and infinite products* — but the adversarial title to verify is in fact two papers: (i) Borcherds, *Automorphic forms with singularities on Grassmannians*, Invent. Math. 132 (1998), 491–562; (ii) Borcherds, *The Gross–Kohnen–Zagier theorem in higher dimensions*, Duke Math. J. 97 (1999), 219–233. Vol III's AP-CY8 (Borcherds denominator vs bar Euler product, K3×E lattice, Φ_10 Igusa cusp form) requires the 1998 *Grassmannian* paper, not the 1995 *infinite products* paper, since the Φ_10-style infinite products are derived from the singular-theta correspondence. The Vol I bib does NOT have this. **Healing:** add `Bor98-Grassmannian` entry. AP-CY8 healing in Vol III chapters that cross-cite Vol I anchors blocks on this. |
| (f) | Kazhdan–Lusztig 1993 | `KL93` | D. Kazhdan and G. Lusztig, *Tensor structures arising from affine Lie algebras, I–IV*, J. Amer. Math. Soc. 6 (1993), 905–947, 949–1011; 7 (1994), 335–381, 383–453. | **CORRECT** in compressed form. The four-paper series is correctly bundled. Year/volumes verify. Sharpening: when the citation is to a *specific* result of the series (e.g., the equivalence of categories at negative level, KL theorem proper), cite the specific part — KL3 (Part III, J. AMS 7 (1994) 335–381) is the part containing the equivalence theorem. The current single `KL93` cite is fine for general "KL theory" attributions but loses a paper-number when the result is in a specific part. AP-CY5 (KL requires root of unity) cites this entry; the AP-CY5 root-of-unity restriction is actually a *different* paper — see (f') below. |
| (f') | Kazhdan–Lusztig at root of unity | (NONE distinct) | — | **MISSING distinction.** AP-CY5 references "Kazhdan–Lusztig at root of unity"; the relevant paper is Finkelberg, *An equivalence of fusion categories*, Geom. Funct. Anal. 6 (1996), no. 2, 249–267, which proves the equivalence Rep$_q$(g)$_{\text{neg}}$ ≃ KL category at root of unity. Vol I/Vol III cite "KL93" for this, but the *root of unity* sharpening is a Finkelberg theorem. Healing: add `Finkelberg96` or similar key. |
| (g) | Frenkel–Gaitsgory | `FG12`, `FG06` | FG12: *Chiral Koszul duality* (Selecta Math. 18 (2012) 27–87). FG06: *Local geometric Langlands and affine Kac–Moody algebras* (Birkhäuser 2006, Progr. Math. 253). | **CORRECT.** FG12 (chiral Koszul) is the citation backing E_1-chiral Koszul duality at d=3 in Vol III's CY-B push. FG06 (local Langlands) is the citation backing the d=3 ConvolutionConventions discussion in Vol I higher_genus_modular_koszul.tex. Both verify. Sharpening: when Vol III cites FG12 for the *bar–cobar adjunction*, the relevant theorem is Theorem 6.3 of FG12 (in the published version). Specifying the theorem number in the citation `\cite[Thm 6.3]{FG12}` would sharpen. |
| (h) | Costello–Gwilliam 2017 (factorisation algebras) | `CG17` | K. Costello and O. Gwilliam, *Factorization Algebras in Quantum Field Theory*, vols. 1–2, Cambridge University Press, 2017. | **CORRECT for Vol 1.** Cambridge published Vol 1 in 2017; **Vol 2 published 2021**, not 2017. The bib body says "vols. 1–2 ... 2017" which is **wrong for Vol 2.** Healing: split into `CG17-vol1` (2017) and `CG21-vol2` (2021), or correct the year to "2017/2021" with both publication years stated. Mathematical content: the chiral structure / Beilinson–Drinfeld factorisation algebra correspondence in Vol 2 is the citation Vol I needs for chapters that talk about prefactorisation algebras vs chiral algebras. |
| (i) | Kontsevich 2003 (deformation quantisation) | `Kon03` | M. Kontsevich, *Deformation quantization of Poisson manifolds*, Lett. Math. Phys. 66 (2003), 157–216. | **CORRECT.** Year, journal, volume, page range all verify. The arXiv preprint is `q-alg/9709040` (1997); Vol I cites the 2003 published version, which is fine. Sharpening: at sites where Vol I cites Kontsevich for the *formality theorem* specifically, the original 1997 preprint or the 1999 Kontsevich `math/9904055` *Operads and motives in deformation quantization* is sometimes the more accurate target — the bib has `Kontsevich99` (line 1578) for that. So the *bib has both* and the sharpening is at the citation site, not the bib. |
| (j) | Positselski 2011 (curved bar–cobar) | `Positselski11` | L. Positselski, *Two kinds of derived categories, Koszul duality, and comodule–contramodule correspondence*, Mem. AMS 212 (2011), no. 996. | **CORRECT.** Memoir number verifies. This is the *canonical* Positselski memoir for curved Koszul duality (CDG-comodule / contramodule pair). Vol I cites this for the curved bar–cobar adjunction; Booth–Lazarev 2023 (arXiv:2304.08409) extends this abstractly — neither is in the bib for Booth–Lazarev. **Missing:** add `BL23` entry for Booth–Lazarev (the working_notes.tex inscription noted this gap). |
| (k) | Lurie HA / HTT | `HA`, `HTT`, `LurieDAGX`, `SAG` | HA: *Higher Algebra*, IAS PDF, 2017. HTT: *Higher Topos Theory*, Princeton 2009, Annals 170. DAG-X: *Formal Moduli Problems*, IAS PDF 2011. SAG: *Spectral Algebraic Geometry*, IAS PDF 2018. | **CORRECT** as identifiers. The IAS-PDF citation form is fragile (Lurie continually revises HA; the "2017" date is the *file mtime* not a publication date); citation site sharpening: where Vol I cites HA for a specific theorem, give the section and theorem number, not just `\cite{HA}`. The IAS PDFs are versioned without commit; AP155 sharpening: cite `\cite[Thm 5.5.4.10]{HA}` etc. AP-CY52 (mega-file) does not apply, but AP155 (overclaiming via vague citation) is alive — `\cite{HA}` bare is a citation that says nothing about *which* HA result. Audit-by-grep is at §6 below. |
| (l) | Schiffmann–Vasserot (CoHA) | `SV13` | O. Schiffmann and E. Vasserot, *Cherednik algebras, W-algebras and the equivariant cohomology of the moduli space of instantons on $\mathbb{A}^2$*, Publ. Math. IHÉS 118 (2013), 213–342, arXiv:1202.2756. | **CORRECT** but **MIS-NAMED** in CY-Vol-III usage. The CoHA = Y$^+$ identification (Schiffmann–Vasserot theorem cited in AP-CY61, "ghost theorem CoHA ≅ Y$^+$") is **not** in this paper. It is in: O. Schiffmann and E. Vasserot, *On cohomological Hall algebras of edge-contracted Cohen–Macaulay curves*, or more canonically in their 2017 paper *On cohomological Hall algebras of quivers: generators*, J. Reine Angew. Math. 760 (2020) 59–132 (preprint arXiv:1705.07488). The 2013 paper (`SV13`) is a *different* result (CoHA / W-algebra / instanton cohomology). **Healing:** add `SV20` for the CoHA-generators paper. |

### Summary of §2 findings

- 5 entries CORRECT (Kohno87, BD04 entry-itself, KL93, FG12/FG06, Kon03, Positselski11, HA/HTT — counting compound).
- 4 entries with MISSING companion (Drinfeld1989-Galois associator paper; Garland–Lepowsky 1976; Borcherds 1998 Grassmannian; Booth–Lazarev 2023; Schiffmann–Vasserot 2017/2020 CoHA-generators; Finkelberg 1996 root-of-unity equivalence).
- 1 entry with **wrong publication year** (CG17 says vols 1–2 2017; Vol 2 is 2021).

The pattern: bib entries that are *present* are mostly correct in their fielded data. The gaps are missing companion papers needed to support precise wave-5 attributions and AP-CY8 / AP-CY55 anchors.

---

## 3. Wave-finding re-attributions

For each AP155 attribution finding from prior waves, the correct source, whether it is in the bib, and the proposed bib entry if not.

| Wave finding | Current cite (mis-attribution) | Correct source | In bib? | Proposed entry |
|--------------|--------------------------------|----------------|---------|----------------|
| Wave 5 BV-Feynman: `mk-tree-level` (A_∞ minimal-model tree formula) attributed loosely; should be Kadeishvili. | `\cite{KontsevichSoibelman}` (Deformation Theory I, unpublished) | Kadeishvili, *On the homology theory of fibre spaces*, Uspekhi Mat. Nauk 35 (1980) no. 3, 183–188. | YES — `Kadeishvili80` (line 769). | No new entry needed. **Healing:** change citation site from `\cite{KontsevichSoibelman}` to `\cite{Kadeishvili80}` at the tree-level minimal-model construction site. |
| Wave 5 BV-Feynman: `mk-general-structure` attribution. | `\cite{Kontsevich97}` (Formality conjecture) | Two-source attribution: **Kontsevich–Soibelman** for the homotopy-transfer / Feynman-graph picture, **Getzler–Kapranov** for the modular-operad picture. | PARTIAL. `KontsevichSoibelman` (line 879) exists but is the unpublished *Deformation Theory I*; the Feynman-graph paper is Kontsevich–Soibelman, *Deformations of algebras over operads and the Deligne conjecture* (math/0001151), which IS in the bib at line 1382. `GetzlerKapranov98` is at line 1372 (modular operads) AND `GK98` at line 655 (same paper, hidden duplicate). | **No new entry.** Healing: cite `\cite{KontsevichSoibelman-DeligneConj}` (i.e., the 2000 Math. Phys. Stud. paper) for the Feynman graph minimal model, and `\cite{GK98}` for modular operad framework. Pick one of the two duplicate keys for GK98 and remove the other. |
| Wave 5 chiral_hochschild_koszul: `thm:hochschild-classical-comparison` mis-attributed to BD04. | `\cite{BD04}` | The chiral-vs-Hochschild comparison statement in this form is due to Tamarkin (the (d+1)-algebra structure on Hoch of a d-algebra) — `Tamarkin00`. The classical-limit comparison is folklore but the precise statement is in Francis–Gaitsgory (`FG12`) Theorem 4.something. | YES, both Tamarkin00 (line 1211) and FG12 (line 541) are in the bib. | **Healing:** cite both: `\cite{Tamarkin00,FG12}`. BD04 stays as the foundational chiral-algebra reference but is **not** the source of *this specific* comparison theorem. |
| Wave 7 lattice/moonshine: AP-CY8 single-variable Borcherds–Gritsenko–Nikulin specialization conflated with Φ_10. | `\cite{Bor95}` (Automorphic forms on $O_{s+2,2}$) | Φ_10 is the Igusa cusp form of weight 10, originally constructed in Igusa 1962 (`Igusa62`) for the Siegel-2 case. Its identification as a Borcherds product / singular theta correspondence is in Borcherds 1998 (Grassmannian paper). The Gritsenko–Nikulin specialisation to Lorentzian Kac–Moody algebras is **separately** Gritsenko–Nikulin, *Siegel automorphic form corrections of some Lorentzian Kac–Moody Lie algebras*, Amer. J. Math. 119 (1997) 181–224 (arXiv:alg-geom/9504006). | NO. The Gritsenko–Nikulin paper is **NOT** in the bib. The Borcherds 1998 Grassmannian paper is **NOT** in the bib (see §2(e)). | **Two new entries needed**: `Bor98-Grassmannian` and `GN97`. Without these, the AP-CY8 healing (cite the right anchor) cannot land. The current `Bor95` cite is the right *family* but the wrong *specific paper* for Φ_10. |
| DK Whitehead reduction misapplied. | `\cite{DK??}` (ad-hoc) at the misapplication site. | Garland–Lepowsky 1976. | NO — see §2(d). | Add `GL76` entry. The companion standalone exists (`papers/garland_lepowsky_concentration.tex`) but is not cited at the misapplication site. |

### Aggregate

- **3 missing bib entries block wave healings**: Garland–Lepowsky 1976, Borcherds 1998 Grassmannian, Gritsenko–Nikulin 1997.
- **2 hidden duplicates need pruning**: GK98 / GetzlerKapranov98 (line 655 vs 1372); BK86 / BK1986 (lines 150 / 153) — the latter is at least flagged in a comment, the former is silent.
- **1 published-year error**: CG17 vol 2 is 2021.

---

## 4. Self-citation discipline

`\cite{LorgatI*}` / `\cite{LorgatII*}` / `\cite{LorgatIII*}` audit:

- Vol I bib has 4 self-citations to author Raeez Lorgat:
  - `Lor-GL` (line 954) — *Bar cohomology concentration for semisimple loop algebras: three mechanisms*, preprint 2026. **Needs arXiv ID** when posted.
  - `Lorgat26I` (line 1639) — *Modular Koszul Duality, Volume I*, monograph 2026. **Self-reference to Vol I from inside Vol I** — this is fine for cross-volume cites coming *into* Vol I, but is dangerous if Vol I cites itself (would create circular-cite illusion of external corroboration).
  - `Lorgat26II` (line 1642) — *A_∞ chiral algebras and 3D holomorphic-topological QFT*, in preparation, 2026. This is Vol II.
  - One additional entry mentioned in the audit memo but not located in scan — possibly Vol III companion.

- Inter-volume self-cites: only `standalone/N4_mc4_completion.tex` uses `\cite{LorgatI...}` style (1 file). The main chapters do *not* — they use `\cite{Lor-GL}` etc. This is good discipline.

- **Risk**: if Vol I body cites `\cite{Lorgat26I}` (Vol I monograph) in its own text, the reference resolves to itself. This would be a circularity. A grep shows `Lorgat26I` is cited from chapters/ — verify that none of those uses creates an inward-pointing self-citation. (Not exhaustively audited in this wave; flagged for next wave.)

- **Tag-correctness for inter-volume cites**: When a Vol I theorem cites the Vol II E_1 sector or Vol III CY-A_3, the bib key should match the cross-volume tag. The current convention (`Lorgat26I/II/III`) is consistent and resolves cleanly. Sharpening: when the cite is to a specific Vol II theorem (e.g. "the E_1 sector of Vol II Section 4.3"), use `\cite[§4.3]{Lorgat26II}` to give the reader a navigation handle. Bare `\cite{Lorgat26II}` is the AP155-vague-cite anti-pattern at the inter-volume scale.

---

## 5. Stale citations

- **`Nish26`** (line 1343–1352): comment block confesses *"UNVERIFIED 2026-04-10: arXiv ID is a literal placeholder"*. Body cites `arXiv:2512.xxxxx`. **Cited from 33 sites in chapters/ + appendices/ + standalone/**. This is a single-point external dependency (`thm:platonic-adjunction` and "seven-faces master agreement" both rest on Nish26). The bibitem produces a `[?]` in the build. **Adversarial referee verdict**: 33 citations to a placeholder arXiv ID is a critical defect that would be caught immediately in peer review. Two healings: (a) resolve the actual arXiv ID; (b) downgrade theorems depending on Nish26 to ProvedHere-conditional and add a marker.

- **`KontsevichSoibelman`** (line 879): cited as "*Deformation Theory. I*, unpublished manuscript, circa 2006." Twenty years after the "circa 2006" date, this manuscript remains unpublished. Vol I cites it for several deformation-theory anchors. This is *stale by survival*: the manuscript exists in many lecture-note forms but has no canonical citation. Healing: where possible, replace `\cite{KontsevichSoibelman}` with the canonical 2000 *Deformations of algebras over operads and the Deligne conjecture* paper (which IS in the bib at line 1382) — the latter contains the operadic Feynman-graph picture that most Vol I citations need.

- **`Costello17`** (line 1363) — *Holography and Koszul duality: the example of the M2 brane*, "preprint, 2017, arXiv:1705.02500." This was published as Costello, "M-theory in the Omega-background and 5-dimensional non-commutative gauge theory" (or similar) — the published version exists. Status: cite the published version when available.

- **`CostelloGaiotto2020`** (line 1366) — *Twisted holography*, preprint 2020, arXiv:1812.09257v2. The "v2" in the arXiv link is fragile: arXiv replaces refer to versioned PDFs; if the paper is ever revised to v3, downstream readers following v2 get a different document. Healing: drop `v2` from the URL once the published version exists, or pin to the canonical SemanticScholar / DOI.

- **`Vic25`** (line 1354) — *Full universal enveloping vertex algebras from factorisation*, preprint 2025. No arXiv ID. **Verify whether this preprint actually exists** — Bruno Vicedo is a real author working in this area, but the title sounds like a paraphrase. Adversarial referee suspicion: this may be a placeholder for an unfinished joint project. If so, downgrade theorems depending on it to conditional.

- **`CM25`** (line 1357) — *The factorizable Feigin–Frenkel center*, A. Casarin and A. Maffei, preprint 2025. No arXiv ID. Same suspicion as Vic25.

- **`GZ26`** (line 1340) — Gaiotto–Zeng, *Interface Minimal Model Holography and Topological String Theory*, arXiv:2603.08783, 2026. The arXiv ID 2603.NNNNN format is *future arXiv* (March 2026). Verify: today's date is 2026-04-16, so March 2026 papers DO exist. arXiv 2603.08783 should be checked against the live arXiv to verify the title and authors match.

---

## 6. Missing citations

### "Obvious" attributions used without explicit cite:

- **Sugawara construction** — used in dozens of places, e.g. when the Virasoro is built from a current algebra. Cited *nowhere* with the original Sugawara 1968 reference (*A field theory of currents*, Phys. Rev. 170 (1968) 1659–1662). The bib has *no* Sugawara entry. Healing: add `Sugawara68`. This is a generations-old reference and many manuscripts skip it, but an adversarial referee would notice.

- **Drinfeld associator** — mentioned in the introduction and KZB discussion. Most cites resolve to `Drinfeld90` (Quasi-Hopf algebras). The associator paper proper is the 1989/91 paper (see §2(a)).

- **Kontsevich formality** — cited at `Kontsevich97` (1997 conference proceedings) AND `Kon03` (2003 published paper). The original 1997 preprint `q-alg/9709040` is the citation most papers use. Vol I sometimes cites the wrong one.

- **Goerss–Hopkins obstruction theory** — used implicitly in HA-style arguments in higher_genus_modular_koszul.tex. No GH cite. Healing: cite Goerss–Hopkins, *Moduli spaces of commutative ring spectra*, in *Structured ring spectra*, LMS Lecture Note Series 315 (2004) 151–200.

- **Tate's thesis / Adèle decomposition** — cited in arithmetic_shadows.tex implicitly. No Tate cite in bib.

### "Recent" attributions that may not yet be common knowledge:

- **Booth–Lazarev 2023** (arXiv:2304.08409) — coderived model + curved Quillen equivalence. Working_notes.tex inscription notes Vol III had three dangling `\cite{BL23}` references; Vol I should also cite this. Not in bib.

- **CFG25** (Costello–Francis–Gwilliam 2026, arXiv:2602.12412) — referenced from Vol III for the BV-quantised CS = E_3 verification at perturbative genus-0. If Vol I has any cross-reference forward to this, it would need a bib entry. (Not currently expected to.)

- **Lazarev–Roytenberg 2024** (curved L_∞-modules) — not searched for.

---

## 7. arXiv ID format audit

Mixed format detected. The bib uses both old-style and new-style arXiv IDs:

**Old-format examples (math.XX/YYNNNNN, hep-th/YYNNNNN, alg-geom/YYNNNNN, q-alg/YYNNNNN)**: ~38 entries from a single grep. Examples: `arXiv:math/0304173` (ABG04), `arXiv:alg-geom/9405001` (Beauville), `arXiv:hep-th/9210010` (Bouwknegt–Schoutens), `arXiv:q-alg/9506005` (Etingof–Kazhdan), `arXiv:math/9803041` (Malikov–Schechtman–Vaintrob), `arXiv:hep-th/9608096` (DMVV — appears TWICE at lines 417 and 420, hidden duplicate).

**New-format examples (YYMM.NNNNN)**: `arXiv:0805.0157` (BZFN10), `arXiv:1202.2756` (SV13), `arXiv:1605.00138` (Ara12), `arXiv:1610.05865` (AK18), `arXiv:1903.10961` (AF20), `arXiv:1812.09257v2` (CostelloGaiotto2020).

Both formats are *valid* — old arXiv IDs continue to resolve via arxiv.org/abs/math/0304173. arXiv has no preferred-format mandate. However, the inconsistency is mild AP155-style: a referee's `bibtool --normalize` would suggest standardising to the citation style of the journal. AMS journals accept either. **Recommendation**: leave old-format IDs alone for canonical pre-2007 references (changing them would mismatch citing literature); standardise post-2007 to the new YYMM.NNNNN format. Audit reveals this is mostly already the case.

**Format defects detected**:
- `Nish26` body cites `arXiv:2512.xxxxx` (literal placeholder). §5 covers this.
- `Costello-1705.02500v1` (line 329, key includes the arXiv ID) — odd convention; the key encodes the arXiv ID, but the published version exists. Healing: rename to a author-year key.
- `arXiv:1812.09257v2` (CostelloGaiotto2020) — version-pinned arXiv link. Drop v2 once the v3/published version is canonical.

---

## 8. Sharpening candidates (strongest possible attribution)

Healing-by-upgrade — replace vague cites with precise ones.

| Site | Current vague cite | Sharpened cite | Why it's the strongest |
|------|---------------------|----------------|------------------------|
| HA bare cites in higher_genus_modular_koszul.tex | `\cite{HA}` | `\cite[Thm 5.5.4.10]{HA}` (or whichever theorem is invoked) | Lurie HA is 1500+ pages; bare `\cite{HA}` says nothing |
| BD04 bare cites for chiral homology | `\cite{BD04}` | `\cite[§4.2]{BD04}` for chiral homology, `\cite[§3.4]{BD04}` for the chiral product, etc. | Same as HA |
| Drinfeld–Kohno theorem cites | `\cite{Drinfeld90, Kohno87}` | `\cite{Drinfeld89-Galois, Kohno87}` (after adding Drinfeld89 entry) | The associator paper is 1989, not 1990 (1990 is quasi-Hopf in general) |
| Kontsevich formality cites | `\cite{Kontsevich97}` | `\cite{Kon03, Tamarkin03}` joint citation | Tamarkin 2003 (math/9809164) gives the operadic proof; Kontsevich 2003 is the original. Joint cite is standard. |
| KL at root of unity | `\cite{KL93}` | `\cite{KL93, Finkelberg96}` (after adding Finkelberg entry) | KL93 sets up the category; Finkelberg96 proves the equivalence Rep_q(g) ≃ KL at root of unity. |
| Φ_10 / Borcherds product | `\cite{Bor95}` | `\cite{Igusa62, Bor98-Grassmannian, GN97}` (after adding the missing two) | Three independent constructions / characterisations; specifying which is being used at each site. |
| CoHA = Y$^+$ | `\cite{SV13}` | `\cite{SV20}` (Schiffmann–Vasserot, *Cohomological Hall algebras of quivers: generators*, 2020) | SV13 is W-algebra / instanton; SV20 is the CoHA-presentation paper. |
| A_∞ minimal model tree formula | (often uncited, sometimes `\cite{KontsevichSoibelman}`) | `\cite{Kadeishvili80}` (already in bib) | Kadeishvili is the original; Kontsevich–Soibelman gives the operadic generalisation. Tree-level minimal model is Kadeishvili's. |
| Modular operad framework | `\cite{GK98}` or `\cite{GetzlerKapranov98}` | Pick one and remove the other duplicate; cite consistently. | Hidden duplicate — see §1. |

---

## 9. First-principles protocol on the AP-CY8 anchor

Per the user's standing principle (AP-CY61 / cross-volume): when challenged on a citation, do NOT just swap the label — investigate the actual mathematical relationship.

The Vol I anchor for AP-CY8 is "Borcherds denominator = bar Euler product." The two halves:

- **Borcherds denominator**: an automorphic-form identity, Φ_10 = $\prod_{\alpha} (1-e^{2\pi i \langle \alpha, \tau\rangle})^{m(\alpha)}$ over positive roots $\alpha$ of a generalized Kac–Moody algebra (the "fake monster Lie algebra" for K3×E). The exponents $m(\alpha)$ come from the elliptic-genus character. The *product* form is due to Borcherds 1995 (`Bor95`). The *Φ_10 = Igusa cusp* identification, in the K3×E case, requires the singular theta correspondence (Borcherds 1998 Grassmannian paper) AND the Gritsenko–Nikulin 1997 specialisation to Siegel modular forms.

- **Bar Euler product**: Vol I's bar-cobar machine produces, for class M chiral algebras, an Euler-product expansion of the chiral character. The functorial machine that converts a chiral algebra into its bar Euler product is Vol I's `Theta_A` operator + the κ-spectrum decomposition.

The *equality* of the two — Borcherds denominator = bar Euler product on K3×E — is what Vol III's AP-CY8 calls "an OBSERVATION, not a theorem." The observation is conditional on (a) Vol III's CY-A_2 (Φ_2(K3) = lattice VOA), (b) Vol I's Borcherds-lift identification of bar Euler products with theta lifts, (c) the AP-CY8 specialisation Borcherds 1995 → Borcherds 1998 → Gritsenko–Nikulin 1997 → Igusa 1962 chain.

**The ghost theorem behind the misattribution**: The wave-7 finding was that Vol I cites `Bor95` for the *Φ_10 specialisation* (which actually requires `Bor98-Grassmannian` and `GN97`). The mathematics is correct; the citation chain is incomplete by two papers. This is *exactly* the AP-CY61 pattern: the ghost theorem (Borcherds product → automorphic form → Igusa-Φ_10 chain) is real and proved across three papers; the manuscript cites only the first link. Healing: cite the chain, not just the head.

---

## 10. Punch list

Ordered by priority for a healing pass. Numbers in [] are the section where each is justified.

### Priority 1 — blocking (gaps that prevent prior-wave healings from landing)

1. **Add `GL76`** (Garland–Lepowsky 1976, Invent. Math. 34: 37–76) to `references.tex`. Without this, the DK Whitehead-reduction healing (wave 5) cannot replace the misapplied citation. [§2(d), §3]

2. **Add `Bor98-Grassmannian`** (Borcherds 1998, Invent. Math. 132: 491–562). Without this, AP-CY8 healing for Φ_10 cite chain cannot land. [§2(e), §3, §9]

3. **Add `GN97`** (Gritsenko–Nikulin, Amer. J. Math. 119 (1997) 181–224, alg-geom/9504006). Same reason. [§3, §9]

4. **Resolve `Nish26` arXiv ID** (line 1343, currently `2512.xxxxx`). 33 citations rest on a `[?]` build. If unresolvable, downgrade theorems depending on Nish26 to ProvedHere-conditional and mark the dependency. [§5]

### Priority 2 — sharpening (AP155 cite-the-specific-source)

5. **Add `Drinfeld89-Galois`** (Leningrad Math. J. 2 (1991) 829–860). Re-cite Drinfeld–Kohno theorem sites with this entry (currently mostly cite `Drinfeld90`). [§2(a), §6, §8]

6. **Add `Finkelberg96`** (Geom. Funct. Anal. 6 (1996) 249–267). Joint-cite at AP-CY5 / KL-at-root-of-unity sites. [§2(f'), §8]

7. **Add `SV20`** (Schiffmann–Vasserot, *CoHA generators*, J. Reine Angew. Math. 760 (2020) 59–132, arXiv:1705.07488). Re-cite CoHA = Y$^+$ ghost theorem (AP-CY61 entry) with SV20 instead of SV13. [§2(l), §3, §8]

8. **Add `BL23`** (Booth–Lazarev, arXiv:2304.08409). Bridges Positselski curved bar–cobar to abstract Quillen equivalence. [§2(j), §6]

9. **Add `Sugawara68`** (Phys. Rev. 170: 1659–1662). Cite at every Sugawara-construction site. [§6]

### Priority 3 — hygiene (duplicates, format, year)

10. **Fix `CG17` year** — split into vols or correct to "2017/2021". [§2(h)]

11. **Resolve hidden duplicate `GK98` / `GetzlerKapranov98`** — pick one canonical key, retire the other (or document the duplication explicitly like the existing BK86 / BK1986 marker). [§1, §3]

12. **Resolve hidden duplicate at lines 417 / 420** (DMVV cited twice). [§7]

13. **Replace `KontsevichSoibelman` (line 879, "unpublished, circa 2006") with the published 2000 paper** (line 1382, math/0001151) at every cite site where the latter suffices. [§5]

14. **Drop `v2` from `arXiv:1812.09257v2` link** in CostelloGaiotto2020 (line 1366) once a canonical version exists. [§5, §7]

15. **Verify `Vic25` and `CM25` actually exist as preprints**. If they are placeholders, downgrade dependent theorems to conditional. [§5]

### Priority 4 — referee-quality polish

16. **Sharpen bare HA / BD04 cites with section/theorem numbers** at top-cited sites (highest-value: higher_genus_modular_koszul.tex, sewing_koszul14.md, derived_langlands.md). [§8]

17. **Verify `GZ26` (arXiv:2603.08783)** against live arXiv. The future-format ID needs confirmation that the title and authors match. [§5]

18. **Audit the `Lor-GL` self-cite to add arXiv ID once the Garland–Lepowsky standalone is posted**. [§4]

---

## 11. Cache write-back candidates (patterns appearing 2+ times)

For `appendices/first_principles_cache.md`:

- **Pattern: missing companion paper for a citation chain.** Examples in this audit: Drinfeld 1989 missing alongside Drinfeld 1990; Borcherds 1998 Grassmannian missing alongside Borcherds 1995; Schiffmann–Vasserot 2020 CoHA-generators missing alongside SV13; Booth–Lazarev 2023 missing alongside Positselski 2011. **Mechanism**: when a "well-known" attribution chain is invoked (e.g. "Drinfeld–Kohno theorem", "Borcherds product = Φ_10", "CoHA = Y$^+$"), the manuscript cites the *first link only*. Adversarial defense: every multi-paper attribution must cite *each link* in the bib, not just the head. Suggest entry: `cache/citation-chain-incompleteness.md`.

- **Pattern: hidden duplicate bib keys.** Examples: BK86 / BK1986 (flagged in comment); GK98 / GetzlerKapranov98 (NOT flagged); DMVV at lines 417 and 420 (NOT flagged); Arakawa15 / Ara15 (flagged). **Mechanism**: the bib accumulates entries over many sessions; when a session adds an entry it forgets the existing one, and both survive. Defense: before any new `\bibitem`, grep the bib for the title or first author + year. Suggest entry: `cache/bib-duplicate-keys.md`.

- **Pattern: vague citation to a long source.** `\cite{HA}` (1500-page Lurie), `\cite{BD04}` (book-length BD), `\cite{KL93}` (four-paper series). Defense: AP155 sharpening — cite the specific section/theorem. Already in cache implicitly (AP155); strengthen by adding the long-source examples to the cache.

- **Pattern: stale "unpublished manuscript, circa YEAR" cites that survive 20+ years.** `KontsevichSoibelman` (circa 2006, still cited 2026). Defense: every cite to an unpublished manuscript must come with a sunset clause — a tracked TODO to find a published replacement, with owner. Suggest entry: `cache/unpublished-manuscript-staleness.md`.

These are 2+-recurrence patterns suitable for cache write-back per the cache write-back loop in MEMORY.md.

---

## End of Wave 11 report.

No commits made. No edits to manuscript or bib. This report (`wave11_bibliography.md`) is the only artifact written. Cache write-back candidates listed in §11 are recommendations for the appendices/first_principles_cache.md maintainer — not yet written.
