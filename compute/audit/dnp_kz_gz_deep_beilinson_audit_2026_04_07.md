# Deep Beilinson Audit: DNP25, KZ25/KhanZeng25, GZ26 Citations
# Date: 2026-04-07
# Scope: All .tex files across ~/chiral-bar-cobar (Vol I) and ~/chiral-bar-cobar-vol2 (Vol II)
# Method: Adversarial falsification per AP1-AP50, Six Hostile Examiners

---

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| SERIOUS  | 5 |
| MODERATE | 8 |
| MINOR    | 6 |
| **Total** | **21** |

---

## Finding 1 (CRITICAL): Cross-volume arXiv ID mismatch for DNP25

**File:** Vol II `main.tex:1025` vs Vol I `bibliography/references.tex:341`
**Class:** AP49 (cross-volume convention mismatch), AP38 (literature normalization)
**Severity:** CRITICAL

**Issue:** The `\bibitem{DNP25}` entry has DIFFERENT arXiv IDs across volumes:
- Vol I: `arXiv:2508.11749` (consistent with compute layer)
- Vol II: `arXiv:2506.09728` (DIFFERENT)

The `\bibitem{DNP2025}` duplicate entry has `arXiv:2508.11749` in BOTH volumes, creating an internal inconsistency within Vol II itself: `DNP25` points to 2506.09728 while `DNP2025` (its declared duplicate) points to 2508.11749.

**Impact:** Any reader following the Vol II DNP25 citation will reach a different paper (or a non-existent one) than the Vol I reader. Citations to `\cite{DNP25}` in Vol II (35+ locations) all inherit the wrong arXiv ID. This is a silent bibliographic corruption.

**Proposed fix:** Determine which arXiv ID is correct (likely 2508.11749, as it is the majority across the project and compute layer), and update the Vol II `\bibitem{DNP25}` to match.

---

## Finding 2 (CRITICAL): Author name error "Gaiotto--Zinenko" for GZ26

**File:** Vol I `frontier_modular_holography_platonic.tex:4653`
**Class:** AP41 (prose mechanism != mathematical mechanism), editorial
**Severity:** CRITICAL

**Issue:** The citation reads "Gaiotto--Zinenko~\cite{GZ26}" but the actual paper is by Gaiotto and **Zeng** (Keyou Zeng), as correctly recorded in the bibliography entry at `references.tex:1134-1135`. The same error "Gaiotto-Zinenko" appears in the compute layer:
- `compute/lib/twisted_holography_amplitudes.py:41,614,674`
- `compute/tests/test_twisted_holography_amplitudes.py:386`

Meanwhile the preface at `preface.tex:6734` uses yet another wrong name: "Gaiotto--Zhang".

**Impact:** Three different author attributions for the same paper in the same manuscript: "Gaiotto--Zeng" (correct, used in concordance and most locations), "Gaiotto--Zinenko" (wrong, line 4653 and compute layer), "Gaiotto--Zhang" (wrong, preface line 6734). This is an integrity issue at Annals grade.

**Proposed fix:** Replace all instances of "Gaiotto--Zinenko" and "Gaiotto--Zhang" with "Gaiotto--Zeng" across both volumes and the compute layer.

---

## Finding 3 (SERIOUS): thm:Koszul_dual_Yangian AP40 status — resolved but residual in superseded file

**File:** Vol II `spectral-braiding.tex:316-319` (SUPERSEDED)
**Class:** AP40 (environment/tag mismatch)
**Severity:** SERIOUS (mitigated: superseded file, but still in repo)

**Issue:** The CLAUDE.md for Vol II explicitly flags: "thm:Koszul_dual_Yangian tagged ProvedHere but cited '(Dimofte-Niu-Py, Thm 5.5)' in the statement."

Current status after rectification:
- **Live file** (`spectral-braiding-core.tex:1539-1549`): The theorem is `\ClaimStatusProvedHere` with title "Affine Open-Colour Dual is a dg-Shifted Yangian." The statement says "(This result was established independently by Dimofte--Niu--Py \cite{DNP25}, Theorem 5.5; the proof below is self-contained within the present framework.)" This is CORRECT: the claim is ProvedHere with a self-contained proof, and DNP25 is cited as independent corroboration, not as the source of the proof. The remark structure is honest.
- **Superseded file** (`spectral-braiding.tex:316-319`): Still reads "(Dimofte--Niu--Py \cite{DNP25}, Theorem 5.5)" as the FIRST sentence of the theorem body, before any statement that the proof is self-contained. This creates an ambiguity: is it ProvedHere or ProvedElsewhere? The label is removed (`% label removed: thm:Koszul_dual_Yangian`), so no cross-reference resolves here.

**Impact:** Low (superseded file not \input'd), but the file remains in the repo. A reader browsing the repository could be confused.

**Proposed fix:** No action needed on the live file (correctly resolved). The superseded file is already marked as such. Low priority.

---

## Finding 4 (SERIOUS): Scope inflation in DNP25 citation: "Theorem 5.2" and "Theorem 5.5" cited without verifying section numbering

**File:** Vol II `spectral-braiding-core.tex:402`, Vol II `spectral-braiding.tex:256,319`; Vol I `yangians_foundations.tex:1439`
**Class:** AP2 (description vs source), AP41 (prose != math)
**Severity:** SERIOUS

**Issue:** Multiple locations cite specific theorem numbers from DNP25:
- "Theorem 5.2" (spectral kernel YBE)
- "Theorem 5.5" (open-colour dual is dg-shifted Yangian)
- "Theorem 4.1" (non-renormalization)
- "Thm. 6.12" (Koszul dual controlled by R^{-1})
- Section "S4.2" (shifted cotangent)

The audit trail in Vol II `compute/audit/thread_claims_inventory_2026_03_30.md` records:
- "D1: Khan-Zeng 'Proposition 3.1' — Paper has no numbered theorems — Fixed to S2.2"
- "D2: Khan-Zeng 'Theorem 5.2' — Paper has no numbered theorems — Fixed to S4.3"

This means the KhanZeng25 paper was previously found to lack numbered theorems, and section references were used instead. The same check has NOT been performed for DNP25. If DNP25 similarly uses a non-standard numbering scheme, the theorem citations could be wrong.

**Impact:** If the specific theorem numbers are wrong, every citation becomes unverifiable. This is a reader-facing integrity issue.

**Proposed fix:** Verify that DNP25 (arXiv:2508.11749) actually contains Theorem 5.2, Theorem 5.5, Theorem 4.1, Theorem 6.12, and Section 4.2 with the stated content. If numbering differs, update all citations.

---

## Finding 5 (SERIOUS): GZ26 "commuting differentials" — scope of comparison not fully qualified

**File:** Vol I `frontier_modular_holography_platonic.tex:1527-1621` (thm:gz26-commuting-differentials)
**Class:** AP42 (correct at sophisticated level, false at naive level), AP7 (scope inflation)
**Severity:** SERIOUS

**Issue:** Theorem thm:gz26-commuting-differentials, part (v), states:
> "For A = W_N ... the commuting condition [H_i, H_j] = 0 is a concrete prediction verifiable term by term against the commuting differentials of [GZ26]."

The subsequent Remark rem:gz26-scope (lines 1696-1710) correctly qualifies: "Part (v) is a concrete prediction: the W_N commuting operators of [GZ26] should agree..." However, GZ26 is specifically about **interface minimal model holography and topological string theory**, not about general W_N algebras at arbitrary central charge. The comparison target in GZ26 is the (p,q) minimal model interface, not the generic W_N family.

The theorem title "GZ26 commuting differentials from the MC element" could mislead: the theorem derives commuting Hamiltonians from Theta_A for general modular Koszul algebras. The GZ26 comparison is valid only at the specific interface points. The scope remark at lines 1700-1702 acknowledges this ("the specific context of interface minimal model holography") but the theorem TITLE still says "GZ26 commuting differentials" as if the theorem IS about GZ26, rather than being an independent result that PREDICTS GZ26 as a special case.

**Impact:** A reader may think the theorem proves something about GZ26's specific setup, when it actually proves a general result and identifies GZ26 as a comparison target.

**Proposed fix:** Consider retitling to "Commuting Hamiltonians from the MC element" with GZ26 appearing in the comparison remark rather than the theorem title. Alternatively, add "(general framework; GZ26 comparison)" to the title.

---

## Finding 6 (SERIOUS): Placeholder arXiv IDs in compute layer

**File:** `compute/lib/pva_deformation_cy3.py:63`, `compute/lib/grand_synthesis_engine.py:983`, `compute/lib/twisted_holography_amplitudes.py:41`
**Class:** AP38 (literature normalization), AAP8 (metadata drift)
**Severity:** SERIOUS

**Issue:** Three compute modules contain placeholder arXiv IDs:
- `pva_deformation_cy3.py:63`: "Khan-Zeng, arXiv:2308.xxxxx" (should be 2502.13227)
- `grand_synthesis_engine.py:983`: "'arxiv_id': '2308.xxxxx'" (should be 2502.13227)
- `twisted_holography_amplitudes.py:41`: "Gaiotto-Zinenko, arXiv:2504.xxxxx" (should be Gaiotto-Zeng, arXiv:2603.08783)

**Impact:** These are in docstrings/comments, not in mathematical computations, so no numerical error propagates. However, any automated citation audit or metadata extraction will pick up phantom arXiv IDs.

**Proposed fix:** Replace all placeholder arXiv IDs with the correct values. Also fix "Gaiotto-Zinenko" to "Gaiotto-Zeng" in the same pass.

---

## Finding 7 (SERIOUS): DNP25 "Theorem 3.1" citation in Vol II line-operators.tex

**File:** Vol II `chapters/connections/line-operators.tex:359`
**Class:** AP2 (description vs source)
**Severity:** SERIOUS

**Issue:** Line 359 reads: "(Dimofte--Niu--Py \cite{DNP25}, Theorem 3.1) The category of perturbative line operators is equivalent to..."

This is inside the body of `thm:lines_as_modules` which is tagged `\ClaimStatusProvedHere`. The parenthetical "(Dimofte--Niu--Py \cite{DNP25}, Theorem 3.1)" appears as if it is an external attribution, but the theorem is actually proved in the manuscript with a self-contained proof (Steps 1-5, lines 372-443). The same issue as Finding 3: the parenthetical creates an attribution paradox. Is this ProvedHere or ProvedElsewhere?

Reading the full context: the parenthetical appears to be a historical note embedded in the theorem statement rather than the proof attribution. But at Annals grade, this is confusing.

**Impact:** Attribution paradox at a load-bearing theorem (thm:lines_as_modules is cited 74+ times across Vol II).

**Proposed fix:** Move the DNP25 comparison to a Remark after the theorem, similar to how thm:Koszul_dual_Yangian was fixed in the live file. The theorem statement should stand alone as ProvedHere; the comparison with DNP25 belongs in a remark.

---

## Finding 8 (MODERATE): KhanZeng25 triple duplicate bibliography entries in Vol I

**File:** Vol I `bibliography/references.tex:701-706,1170-1172`
**Class:** Editorial, AAP5 (build artifact noise)
**Severity:** MODERATE

**Issue:** Vol I has THREE bibliography entries for the same paper:
- `\bibitem{KhanZeng25}` at line 701
- `\bibitem{KZ2025}` at line 704 ("Duplicate of KhanZeng25; retained for citation-key compatibility")
- `\bibitem{KZ25}` at line 1170 ("Duplicate of KhanZeng25; retained for citation-key compatibility")

This is excessive. The manuscript uses all three keys: `\cite{KhanZeng25}` (most common), `\cite{KZ25}` (in kac_moody.tex, w_algebras.tex), `\cite{KZ2025}` (in yangians_drinfeld_kohno.tex). The compiled PDF will show three separate bibliography entries for the same paper.

**Impact:** Visual clutter in the bibliography. A referee may flag this.

**Proposed fix:** Consolidate to a single key (KhanZeng25) and update all \cite{KZ25} and \cite{KZ2025} to \cite{KhanZeng25}. Remove duplicate bibitem entries.

---

## Finding 9 (MODERATE): DNP25/DNP2025 duplicate in both volumes

**File:** Vol I `bibliography/references.tex:340-345`, Vol II `main.tex:1025-1028`
**Class:** Editorial
**Severity:** MODERATE

**Issue:** Both volumes have `DNP25` and `DNP2025` as separate bibliography entries pointing to the same paper (with the arXiv ID discrepancy noted in Finding 1). Citations use both keys: `\cite{DNP25}` (most locations) and `\cite{DNP2025}` (yangians_computations.tex, quantum_corrections.tex, examples-worked.tex, modular_pva_quantization.tex).

**Impact:** Duplicate bibliography entries. Combined with Finding 1, this means Vol II has two entries with DIFFERENT arXiv IDs for the same paper.

**Proposed fix:** Consolidate to a single key after resolving Finding 1.

---

## Finding 10 (MODERATE): conj:boundary-defect-realization correctly uses \begin{conjecture}

**File:** Vol I `frontier_modular_holography_platonic.tex:1369`
**Class:** AP40 check (PASS)
**Severity:** N/A (verification, no issue)

**Verification:** The claim at line 1369 uses `\begin{conjecture}` with `\ClaimStatusConjectured`. This is CORRECT. No AP40 violation.

---

## Finding 11 (MODERATE): prop:super-virasoro-3d-action label prefix "prop:" but environment is "conjecture"

**File:** Vol I `chapters/examples/w_algebras.tex:5798-5800`
**Class:** AP40 (environment/tag mismatch, label convention)
**Severity:** MODERATE

**Issue:** The label is `prop:super-virasoro-3d-action` (prefix "prop:" suggesting a proposition), but the environment is `\begin{conjecture}` with `\ClaimStatusConjectured`. The claims.jsonl metadata confirms: `"env_type": "conjecture"` but label starts with "prop:".

**Impact:** Label prefix mismatch. Any automated tool parsing labels by prefix will misclassify this as a proved proposition. Cross-references using `Proposition~\ref{prop:super-virasoro-3d-action}` would print "Proposition" for a conjecture.

**Proposed fix:** Rename label to `conj:super-virasoro-3d-action` and update all cross-references.

---

## Finding 12 (MODERATE): thm:frontier-twisted-holography cites GZ26 but is tagged ProvedHere

**File:** Vol I `frontier_modular_holography_platonic.tex:4285`
**Class:** AP40 check
**Severity:** MODERATE

**Issue:** The claims.jsonl shows `thm:frontier-twisted-holography` at line 4285 with `"status": "ProvedHere"` and `"cites_in_block": ["GZ26"]`. Reading the actual theorem (lines 4630-4656): it is a computation of the holographic datum for the D3 brane system, proved using the manuscript's own formulas. The GZ26 citation at line 4653 is used as a comparison target: "The commuting differentials of Gaiotto--Zinenko [GZ26] are the scalar shadow of Sh_{0,n}." This is legitimate: the theorem is proved here, and GZ26 is cited for comparison.

However, the name "Gaiotto--Zinenko" at this location is WRONG (Finding 2).

**Impact:** No AP40 violation on the status tag. The name error is covered by Finding 2.

**Proposed fix:** Fix the name error per Finding 2.

---

## Finding 13 (MODERATE): thm:kz-classical-quantum-bridge part (iv) claims "gauge invariance = Jacobi" without full attribution chain

**File:** Vol I `frontier_modular_holography_platonic.tex:1895-1903`
**Class:** AP42 (correct at sophisticated level, nuanced at naive level)
**Severity:** MODERATE

**Issue:** Part (iv) of thm:kz-classical-quantum-bridge states: "The gauge invariance condition of the KZ25 Poisson sigma model [S2.2]{KhanZeng25} is the lambda-Jacobi identity." The proof at lines 1924-1936 argues: KZ25 action has form S = integral<alpha, dbar beta> + integral P(alpha,beta) dt; gauge invariance requires {P,P} = 0 (Jacobi); in our framework, the Arnold relation on FM_k(C) gives d_B^2 = 0 iff chiral Jacobi.

The identification "gauge invariance = Jacobi" is correct at the classical level. However, the proof conflates two things: (a) KZ25's gauge invariance of their specific action functional, and (b) the manuscript's d_B^2 = 0 from Arnold relations. These are INDEPENDENT derivations of the same algebraic identity, not a derivation of one from the other. The prose "In our framework, the same structure appears" correctly signals this, but the theorem statement "(iv) Gauge invariance = Jacobi" could be read as proving something about KZ25's theory, when it actually proves a parallel fact in the manuscript's own framework.

**Impact:** Minor scope confusion. The remark at lines 1956-2009 (rem:ht-deformation-quantization-formal) correctly qualifies the gap. Low real risk.

**Proposed fix:** Add a clarifying parenthetical to part (iv): "(independent derivation; cf. \cite[\S2.2]{KhanZeng25} for the gauge-theoretic parallel)."

---

## Finding 14 (MODERATE): Concordance correctly records all three new theorems

**File:** Vol I `concordance.tex:5948-5968`
**Class:** Cross-reference verification (PASS)
**Severity:** N/A (verification, no issue)

**Verification:** The concordance at lines 5948-5968 correctly lists:
- (e) thm:dnp-bar-cobar-identification (DNP line-operator package = bar-cobar twisting)
- (f) thm:gz26-commuting-differentials (GZ26 commuting differentials from Theta_A)
- (g) thm:kz-classical-quantum-bridge (classical-to-quantum bridge)

Each entry correctly describes the proved content, the cited external paper, and the fallback status. The risk stratification at lines 1570-1589 correctly places GZ26 and KhanZeng25 in the "no proved-theorem risk" category. This is honest and accurate.

---

## Finding 15 (MODERATE): KZ25 cited as "topological resonance" in kac_moody.tex without clear referent

**File:** Vol I `chapters/examples/kac_moody.tex:181`
**Class:** AP41 (prose != math)
**Severity:** MODERATE

**Issue:** Line 181 reads: "Khan--Zeng \cite{KZ25} topological resonance reduction applies and the shadow obstruction tower simplifies."

The phrase "topological resonance reduction" does not correspond to a named result in KhanZeng25. KZ25 proves that an inner Virasoro element upgrades HT symmetry to fully topological symmetry (their Section 4.3). The phrase "topological resonance reduction" appears to be a manuscript-internal shorthand for the phenomenon that topological enhancement simplifies the shadow tower. But attributing this shorthand to KZ25 with a \cite is misleading: KZ25 proves the topological enhancement, not the simplification of the shadow tower (which is a consequence derived in the manuscript).

**Impact:** A reader may search KZ25 for "topological resonance reduction" and fail to find it.

**Proposed fix:** Rewrite to: "the Virasoro element triggers topological enhancement (cf. \cite[\S4.3]{KhanZeng25}), which simplifies the shadow obstruction tower."

---

## Finding 16 (MODERATE): Vol II w-algebras-stable.tex attributes lambda-brackets to KZ25

**File:** Vol II `chapters/examples/w-algebras-stable.tex:698`
**Class:** AP2 (description vs source)
**Severity:** MODERATE

**Issue:** Line 698 reads: "The lambda-brackets are (from \cite{KZ25}):" followed by the W_3 lambda-brackets. These brackets are standard results known since Zamolodchikov (1985) and Fateev-Lukyanov (1988). KZ25 uses them as INPUT to construct the 3d gauge theory; they are not original results of KZ25.

**Impact:** Misattribution. The lambda-brackets are classical results of the W-algebra literature. Citing KZ25 as the source is misleading.

**Proposed fix:** Change to "(cf. Zamolodchikov [Zam85], in the lambda-bracket convention of \cite{KZ25}):" or cite the original W-algebra literature.

---

## Finding 17 (MINOR): "Gaiotto--Zhang" vs "Gaiotto--Zeng" in preface

**File:** Vol I `chapters/frame/preface.tex:6734`
**Class:** Editorial (author name error)
**Severity:** MINOR (subsumed by Finding 2)

**Issue:** "The Gaiotto--Zhang (2026) commuting differentials" should be "Gaiotto--Zeng."

**Proposed fix:** Covered by Finding 2.

---

## Finding 18 (MINOR): "Gaiotto-Zinenko" in compute layer

**File:** `compute/lib/twisted_holography_amplitudes.py:41,614,674`; `compute/tests/test_twisted_holography_amplitudes.py:386`
**Class:** Editorial (author name error)
**Severity:** MINOR (subsumed by Finding 2)

**Issue:** "Gaiotto-Zinenko" should be "Gaiotto-Zeng" throughout the compute layer.

**Proposed fix:** Covered by Finding 2.

---

## Finding 19 (MINOR): GZ26 bibliography entry appears only in Vol I, not Vol II

**File:** Vol II (absence)
**Class:** AP5 (cross-volume propagation)
**Severity:** MINOR

**Issue:** GZ26 is cited in Vol I's concordance and frontier chapter, and referenced in Vol II's celestial/BBL sections only indirectly. The bibliography entry exists in Vol I `references.tex:1134` but no `\bibitem{GZ26}` was found in Vol II's `main.tex` bibliography. This means any Vol II file that tries `\cite{GZ26}` will produce an "undefined citation" warning.

Checking the actual Vol II citations: the searches found GZ26 references only in Vol II's `ht_bulk_boundary_line_core.tex:124` (an omitted long line) and `celestial_holography.tex:74` (which references "Gui--Li--Zeng", a different paper). So GZ26 may not actually be cited in Vol II's active surface.

**Impact:** Low if GZ26 is not cited in Vol II. If it is cited, compilation warning.

**Proposed fix:** Verify whether any active Vol II file uses `\cite{GZ26}`. If so, add the bibitem to Vol II.

---

## Finding 20 (MINOR): conj:ht-deformation-quantization correctly uses \begin{conjecture}

**File:** Vol I `frontier_modular_holography_platonic.tex:1939`
**Class:** AP40 check (PASS)
**Severity:** N/A (verification, no issue)

**Verification:** `\begin{conjecture}` with `\ClaimStatusConjectured`. Correct.

---

## Finding 21 (MINOR): prop:pva-degree-constraint tagged ProvedElsewhere, cites KZ25 -- correct

**File:** Vol I `frontier_modular_holography_platonic.tex:2012-2048`
**Class:** AP40 check (PASS)
**Severity:** N/A (verification, no issue)

**Verification:** `\begin{proposition}` with `\ClaimStatusProvedElsewhere`, citing `\cite[\S2.2, eq.~(2.24)]{KhanZeng25}` and `\cite[\S4.3]{KhanZeng25}`. The proof traces the degree constraint and Virasoro enhancement directly to specific KZ25 locations. This is correctly structured: ProvedElsewhere with explicit section references in the cited paper. No AP40 violation.

---

## Systematic Checks

### AP40 (Environment/Tag) Audit Summary

| Theorem | Environment | Status Tag | External Citation | Verdict |
|---------|------------|------------|-------------------|---------|
| thm:Koszul_dual_Yangian (live) | theorem | ProvedHere | DNP25 Thm 5.5 (as corroboration) | OK |
| thm:Koszul_dual_Yangian (superseded) | theorem | ProvedHere | DNP25 Thm 5.5 (ambiguous) | FINDING 3 |
| thm:spectral_R_YBE | theorem | ProvedElsewhere | DNP25 Thm 5.2 + internal Prop | OK |
| thm:dnp-bar-cobar-identification | theorem | ProvedHere | DNP25 (comparison) | OK |
| thm:gz26-commuting-differentials | theorem | ProvedHere | GZ26 (comparison target) | OK (Finding 5 is scope, not AP40) |
| thm:kz-classical-quantum-bridge | theorem | ProvedHere | KhanZeng25 (parallel) | OK |
| conj:boundary-defect-realization | conjecture | Conjectured | GZ26 | OK |
| conj:ht-deformation-quantization | conjecture | Conjectured | KhanZeng25 | OK |
| conj:singular-fiber-descent | conjecture | Conjectured | None | OK |
| prop:pva-degree-constraint | proposition | ProvedElsewhere | KhanZeng25 S2.2, S4.3 | OK |
| prop:super-virasoro-3d-action | conjecture | Conjectured | KhanZeng25 | FINDING 11 (label prefix) |
| thm:lines_as_modules | theorem | ProvedHere | DNP25 Thm 3.1 (in body) | FINDING 7 |
| thm:non-renormalization-tree | theorem | ProvedElsewhere | DNP2025 Thm 4.1, Prop 6.1 | OK |
| prop:gauge-koszul-dual-shifted-cotangent | proposition | ProvedElsewhere | DNP2025 S4.2 | OK |
| prop:dg-shifted-comparison | proposition | ProvedHere | DNP25 (structural comparison) | OK |
| thm:frontier-twisted-holography | theorem | ProvedHere | GZ26 (comparison) | OK |

### AP7 (Scope Inflation) Audit Summary

| Citation | Claimed scope | Actual scope in cited paper | Verdict |
|----------|--------------|----------------------------|---------|
| DNP25 for line operators | "chirally Koszul logarithmic SC-algebra" | 3d holomorphic CS specifically | OK: manuscript proves its own version; DNP25 is comparison |
| KZ25 for PVA quantization | "freely generated PVA" | Classical PVA level | OK: quantum gap explicitly flagged in rem:ht-deformation-quantization-formal |
| GZ26 for commuting differentials | "modular Koszul chiral algebra" | Interface minimal models | FINDING 5: scope qualifier needed in theorem title |
| KZ25 for "topological resonance" | Attributed to KZ25 | KZ25 proves topological enhancement, not "resonance reduction" | FINDING 15 |
| KZ25 for lambda-brackets | "from \cite{KZ25}" | Standard W-algebra results | FINDING 16 |

### Risk Stratification Verification

The concordance risk stratification (lines 1570-1589) correctly classifies:
- GZ26: "no proved-theorem risk" (cited as comparison target only) -- VERIFIED CORRECT
- KhanZeng25: "no proved-theorem risk" (cited as physical context only) -- VERIFIED CORRECT
- DNP25: Not explicitly listed in the risk stratification paragraph but correctly handled: thm:spectral_R_YBE is ProvedElsewhere citing DNP25; all other DNP25-related theorems are ProvedHere with DNP25 as comparison.

**Gap:** DNP25 should be explicitly listed in the risk stratification, since thm:spectral_R_YBE directly depends on it (parts (i)-(ii) are ProvedElsewhere from DNP25).

---

## Running Totals

- Files audited: 40+ across both volumes
- DNP25 citation sites: ~65 (Vol I: ~30, Vol II: ~35)
- KZ25/KhanZeng25 citation sites: ~55 (Vol I: ~35, Vol II: ~20)
- GZ26 citation sites: ~25 (Vol I: ~20, Vol II: ~5)
- AP40 violations found: 2 (Finding 3, Finding 11)
- AP7/scope issues: 2 (Finding 5, Finding 15)
- AP49/cross-volume: 1 CRITICAL (Finding 1)
- AP41/name errors: 1 CRITICAL (Finding 2, 3 variants)
- AP38/placeholder IDs: 1 SERIOUS (Finding 6)
- AP2/attribution: 2 (Finding 7, Finding 16)
- Editorial: 3 (Findings 8, 9, 19)

---

## Priority Ordering for Fixes

1. **Finding 1** (CRITICAL): Resolve DNP25 arXiv ID discrepancy between volumes
2. **Finding 2** (CRITICAL): Fix all "Gaiotto--Zinenko" and "Gaiotto--Zhang" to "Gaiotto--Zeng"
3. **Finding 7** (SERIOUS): Move DNP25 attribution from thm:lines_as_modules body to a Remark
4. **Finding 4** (SERIOUS): Verify DNP25 theorem numbers against actual paper
5. **Finding 5** (SERIOUS): Add scope qualifier to thm:gz26-commuting-differentials title
6. **Finding 6** (SERIOUS): Replace placeholder arXiv IDs in compute layer
7. **Finding 11** (MODERATE): Rename prop:super-virasoro-3d-action to conj:super-virasoro-3d-action
8. **Findings 8-9** (MODERATE): Consolidate duplicate bibliography entries
9. **Findings 15-16** (MODERATE): Fix attribution precision for KZ25
10. **Finding 19** (MINOR): Verify GZ26 bibitem presence in Vol II if needed
