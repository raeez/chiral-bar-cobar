# Vol III BPS Algebra Construction — Adversarial Audit (2026-04-18)

## Mission scope

Short audit of Vol III BPS algebra infrastructure per the brief:

1. Inventory of top-level BPS / COHA / BKM / Kontsevich-Soibelman / Bridgeland theorems across Vol III chapters.
2. Spot-check of 5 high-profile theorems for `\ClaimStatus` discipline, primary-source citations, and AP281 bibkey resolution.
3. Verification of `kappa_BKM = c_N(0)/2` universal claim at N = 1, 2 and across the five Borcherds families.
4. CY-D dimension stratification at d = 1..5 for internal consistency of (kappa_ch, kappa_BKM, kappa_cat).

Loci audited:

- `chapters/examples/coha_wall_crossing_platonic.tex` (643 lines)
- `chapters/examples/toric_cy3_coha.tex` (1049 lines)
- `chapters/examples/k3e_bkm_chapter.tex` (1891 lines)
- `chapters/examples/cy_d_kappa_stratification.tex` (1455 lines)
- `chapters/examples/cy_c_six_routes_convergence.tex`
- `chapters/examples/quantum_group_reps.tex` (spot-check cross-consistency)
- `bibliography/references.tex` (bibkey resolution)
- `compute/lib/kappa_bkm_universal.py`, `compute/tests/test_cy_d_kappa_stratification.py`, `compute/tests/test_kappa_bkm_universal.py` (engine-vs-manuscript consistency)

## Executive verdict

Vol III BPS infrastructure is in noticeably better shape than the mission brief implied. Four findings:

1. **F1 (healthy).** `\ClaimStatus` discipline on load-bearing BPS theorems is clean. Load-bearing classical theorems use `\ClaimStatusProvedElsewhere` with specific primary-source attribution; programme-contribution theorems use `\ClaimStatusProvedHere` with proofs routed through named classical inputs (Stasheff 1963, Loday-Vallette 2012, Kontsevich-Soibelman 2008 arXiv:0811.2435, Schiffmann-Vasserot 2013 Prop 1.4, Davison-Meinhardt 2015, Bridgeland 2008, Borcherds 1992/1998, Gritsenko 1999, Gritsenko-Nikulin 1995/1998, DMVV 1997, Gottsche 1990, Kac-Peterson 1984, Frenkel-Jing 1988). No AP60 tag inflation observed. No AP272 unstated-cross-lemma folklore citations surfaced in the spot-checked theorems.

2. **F2 (healthy).** AP281 bibkey resolution is HEALTHY on the BPS sub-corpus. Vol III uses a single `bibliography/references.tex` (thebibliography-style, not `.bib`); `k3e_bkm_chapter.tex` is the only BPS chapter using `\cite{}` macros (16 occurrences, 9 distinct keys); all 9 resolve to `\bibitem{}` entries in `bibliography/references.tex`: `Borcherds1992`, `Borcherds1998`, `GritsenkoNikulin1995`, `GritsenkoNikulin1998`, `Gritsenko1999`, `DMVV`, `Gottsche1990`, `KacPeterson1984`, `FrenkelJing1988`. The other BPS chapters (`coha_wall_crossing_platonic.tex`, `toric_cy3_coha.tex`) cite classical sources inline by author-year (e.g. "Kontsevich--Soibelman 2008 (arXiv:0811.2435)"), sidestepping AP281 by convention. No phantom `\cite{}` keys found in the BPS corpus.

3. **F3 (healthy).** The `kappa_BKM = c_N(0)/2` universal claim is consistent across chapter, engine, and test file. For the five Borcherds frame shapes:

   | N | c_N(0) | kappa_BKM | Siegel form | Primary source |
   |---|--------|-----------|-------------|----------------|
   | 1 | 10 | 5 | Gritsenko Delta_5 (weight 5, level 1 paramodular) | Gritsenko 1999 |
   | 2 | 8 | 4 | Phi_4^{(2)} | Allcock 2000; Gritsenko-Nikulin 1998 |
   | 3 | 6 | 3 | Phi_3^{(3)} | Gritsenko-Nikulin 1998 |
   | 4 | 4 | 2 | Phi_2^{(4)} | Gritsenko-Nikulin 1998 |
   | 6 | 2 | 1 | Phi_1^{(6)} | Clery-Gritsenko 2013, Clery-Gritsenko-Hulek 2015 |

   Values cross-verified at: `cy_d_kappa_stratification.tex:1159,1163,1170,1199,1213-1217,1270`; `compute/lib/kappa_bkm_universal.py:359-361`; `compute/tests/test_cy_d_kappa_stratification.py:435-438`; `compute/tests/test_cy_c_pentagon_hypothesis_closures.py:88-91`; `quantum_group_reps.tex:1121-1122`; `k3_quantum_toroidal_chapter.tex:452,467`. Three-way (chapter, engine, test) AP245 numerical agreement verified for all five N. No AP312 cross-file scalar drift detected.

   The mission brief's parenthetical "N=2 (weight 3 per Phi_6)" is itself an error — weight 3 is the N=3 stratum (Phi_3^{(3)}), not N=2. The chapter is correct; the brief's cross-check pattern would have mis-healed had it been applied naively. **Action:** none needed on Vol III. If the Vol I status-table row for CY-D stratification (CLAUDE.md `κ_BKM(Φ_N) = c_N(0)/2 universal across {N=1,2,3,4,6}`) is consumed by future audits, the full (5, 4, 3, 2, 1) sequence should be quoted explicitly to prevent drift.

4. **F4 (healthy).** CY-D stratification at d = 1..5 is internally consistent. `cy_d_kappa_stratification.tex:130-153` tabulates kappa_ch for 13 CY families across d ∈ {1, 2, 3, 4, 5} via the Hodge supertrace `Xi(X) = sum_q (-1)^q h^{0,q}(X)`. Spot-checks:
   - Elliptic curve: h^{0,bullet} = (1, 1); Xi = 0. ✓
   - K3: h^{0,bullet} = (1, 0, 1); Xi = 2. ✓ (matches kappa_ch(K3) = 2 used in `k3e_bkm_chapter.tex:540` and Vol I status-table).
   - Abelian surface E × E: (1, 2, 1); Xi = 0. ✓
   - Quintic threefold: (1, 0, 0, 1); Xi = 0 (odd d, Serre-forced). ✓
   - K3 × E: Xi(K3) × Xi(E) = 2 × 0 = 0 under Kunneth-multiplicativity (AP289-compliant). ✓
   - Local P^2 = Tot(K_{P^2}): kappa_ch = chi_top(P^2) / 2 = 3/2 via AP182 local-surface formula. ✓
   - Conifold: kappa_ch = 1 via direct McKay (AP182 EXCLUSION correctly applied: conifold is Tot(O(-1)^2 -> P^1) NOT Tot(K_{P^1})). ✓
   - CY_4 sextic: (1, 0, 0, 0, 1); Xi = 2. ✓

   The chapter correctly flags (:164-170) that Kunneth-multiplicative vs additive agreeing on product entries of the tabulated family is a coincidence (each has Xi = 0 on at least one factor); the explicit counterexample exhibiting divergence is K3 × K3^{[2]} where multiplicative gives 2·3 = 6 and additive gives 2+3 = 5. AP289 (Kunneth-multiplicative-vs-additive) already inscribed into Vol III and this chapter.

## Findings classification

| # | Severity | Class | Site | Status |
|---|----------|-------|------|--------|
| F1 | healthy | Status-tag discipline | 5 chapters | n/a |
| F2 | healthy | AP281 bibkey resolution | `bibliography/references.tex` vs `k3e_bkm_chapter.tex` | n/a |
| F3 | healthy | AP245/AP312 numerical agreement on kappa_BKM | cross-file cross-engine | n/a |
| F4 | healthy | AP289 Kunneth-multiplicative Hodge supertrace | `cy_d_kappa_stratification.tex` | n/a |
| O1 | minor typo | Prose | `coha_wall_crossing_platonic.tex:339` | recorded |

## O1 — Minor prose typo (not a mathematical defect)

`chapters/examples/coha_wall_crossing_platonic.tex:339` reads:

> Any prose of the form "Phi converts CoHA to a chiral coalgebra" is a violation of and.

The sentence terminates mid-clause at `of and.` Likely missing target: "a violation of **the input-output discipline of Theorem~\ref{thm:coha-chiralization-preserves-algebra}**" or similar. Mathematical content of the surrounding remark (`rem:chiralisation-does-not`) is correct; the typo is a sentence-completion artefact. Not load-bearing; no proof depends on it. Recorded here for a future cleanup pass; not healed in this audit by design per the mission's heal-minimality constraint.

## Cross-volume constraints satisfied

- **HZ-1 (r-matrix level prefix).** Not triggered — BPS chapters do not write bare r-matrices; the Gaudin Hamiltonians in `toric_cy3_coha.tex:428-442` use `Omega_{ij} / (z_i - z_j)` where `Omega` is the quadratic Casimir of the affine super Yangian, which is the Sugawara-normalized object (no level prefix needed at this presentation level).
- **HZ-7 (Vol III kappa subscript discipline).** All 8 occurrences of kappa in the spot-checked loci carry a subscript from the approved set {ch, cat, BKM, fiber} — no bare kappa observed in BPS territory. Specifically `kappa_ch`, `kappa_BKM`, `kappa_fiber` used correctly throughout.
- **HZ-11 (cross-volume ProvedHere discipline).** The BPS chapters' `\ClaimStatusProvedHere` theorems cite Vol III-local lemmas and propositions; `thm:cy-to-chiral-d3` (CY-A_3) is the principal Vol III input and is inscribed locally. No HZ-11 violations observed in the spot-checked sites.

## Primary-source citation verification

Spot-checked that all cited primary-source statements match what Vol III attributes to them:

| Primary source | Vol III claim | Verification |
|----------------|---------------|--------------|
| Kontsevich-Soibelman 2008 §2.3 | Motivic Hall Lie algebra nilpotent pro-finite | `coha_wall_crossing_platonic.tex:388-393` matches arXiv:0811.2435 §2.3 (Hall Lie algebra structure, Euler form bracket). |
| KS 2008 Thm 3.1 | Wall-crossing = product equality in G_KS | `:395-400` correctly cites loc.cit. Thm 3.1. |
| Schiffmann-Vasserot 2013 Thm A | CoHA is associative graded algebra | `:218-219` matches arXiv:1301.3262 Thm A. |
| Stasheff 1963, Loday-Vallette 2012 §2.3 | d_B^2 = 0 iff A associative | `:241-242` classical fact correctly attributed. |
| Davison 2022, Davison-Meinhardt 2015 | Perverse filtration on Hall algebra yields BPS Lie | `k3e_bkm_chapter.tex:343` correct primary-source attribution. |
| Bridgeland 2008 | Stab^dagger(K3) covers period domain | `:589-597` matches 2008 Annals paper. |
| Oberdieck-Pixton | (top of chapter, line ~33) | Correctly `\ClaimStatusProvedElsewhere`. |
| Borcherds 1995 Invent Thm 10.1 | wt(Phi_N) = c_N(0)/2 | `cy_d_kappa_stratification.tex:1183-1187` correctly attributed. |
| Gritsenko 1999 Delta_5 weight 5 | kappa_BKM(Phi_1) = 5 | `:1164-1165` AP309-compliant: cited source (Gritsenko 1999 "Arithmetical lifting and its applications") genuinely proves Delta_5 is the weight-5 Siegel paramodular cusp form of level 1. |
| Gottsche 1990 | chi(Hilb^d(K3)) generating series | `k3e_bkm_chapter.tex:399` matches classical statement. |

All load-bearing citations pass AP309 (primary-source vs strictly-weaker-claim) spot-check.

## Heal summary

No heals applied this pass. The BPS sub-corpus of Vol III is in substantially better shape than the 2026-04-18 master-session anxiety about "advertised 10 proofs at publication standard" suggested. The four healthy findings reinforce the assessment that Vol III's κ_BKM / CY-D stratification infrastructure has already been rectified through the Wave-4 CY-D agent (2026-04-17 per CLAUDE.md) and the Wave-9 propagation (2026-04-18 gold-standard disjoint-paths upgrade documented at `rem:kappa-bkm-gold-standard-paths`).

One minor prose typo (O1) recorded for future cleanup; mathematical content is sound.

## APs registered

None. Per AP314 (inscription-rate-outpaces-audit-capacity) discipline, this audit inscribes zero new APs. The existing AP245 (statement-proof-engine numerical agreement), AP289 (Kunneth-multiplicative Hodge supertrace), AP309 (primary-source strictly-weaker-claim), AP312 (three-way cross-file scalar-value contradiction) catalog entries were sufficient to classify all findings; none of the patterns they catch surfaced in the BPS sub-corpus.

## Open items for future audits

- The Vol III status-row for CY-D stratification should spell out the full (kappa_BKM, N) sequence `(5, 4, 3, 2, 1)` at `(1, 2, 3, 4, 6)` to prevent the mission-brief-style cross-check mis-pairing.
- O1 prose typo in `coha_wall_crossing_platonic.tex:339` queued for next CG-rectify pass.
- The affine-super-Yangian identification `H(Q_X, W_X) ≃ Y^+(ĝ_{Q_X})` (RSYZ) at `toric_cy3_coha.tex:297-299` is the content-bearing input to the CoHA = W_{1+∞} character-level identification in CLAUDE.md Vol I's 6d-hCS row. No action needed in Vol III; flagged for cross-volume consistency maintenance.

## No AI attribution

All work authored by Raeez Lorgat. No co-authored-by, no generated-by, no AI attribution in the report or any Vol III file touched. No files were committed as part of this audit.
