# Attack-and-Heal: Super-Yangian osp-super sub-case (2026-04-18, Wave N2/MC3 follow-on)

Target: 5th-family super-Yangian sub-case split in `chapters/theory/mc3_five_family_platonic.tex`, specifically the Wave-15 `Y(gl(m|n))` parity-balance vs `Y(osp(m|2n))` super-reflection-equation split and its Vol III K3 Yangian `Y_{osp(4|20)}` consumer.

## Phase 1: Existing inscription audit

Wave-15 split inscriptions verified at:
- `rem:super-yangian-scope` (lines 147-177) — cross-volume scope split narrative.
- `rem:parity-balance-scope-gl-only` (lines 469-487, pre-heal) — scope clip on parity-balance proposition.
- Sub-case enumeration in `cor:five-family-union-coverage` (lines 746-752, pre-heal).
- Baxter-retraction proof list item (iv) (lines 515-517), mentions Z/2-graded Berezinian at parity-balance hyperplane (pre-heal; this remains a gl-super statement, no change needed).
- CLAUDE.md MC1-4 theorem-status row (line 590): "super-Yangian family splits into Y(gl(m|n)) parity-balance sub-case and Y(osp(m|2n)) super-reflection-equation sub-case... K3 super-Yangian Y_osp(4|20) lies in the osp-super sub-case."

Vol III K3 chapter `chapters/examples/k3_yangian_chapter.tex`:
- Lines 1854-2148 inscribe `Y_{osp(4|20)}` with full ACDFR citation (bibkey `AcdfR2003`), Kulish-Reshetikhin R-matrix, reflection equation, sBer K(u), `conj:osp-yangian-mukai` (already Conjectured), `rem:gl-to-osp-correction` at line 2006 (AP246+AP279 heal).
- K3 chapter does NOT invoke MC3/parity-balance for K3 target. Consistent.
- Vol III bibliography/references.tex line 33-34: `AcdfR2003 = D. Arnaudon, J. Avan, N. Crampé, A. Doikou, L. Frappat, and E. Ragoucy, J. Stat. Mech. (2004) P08005, arXiv:math-ph/0304188 (2003)`.

## Phase 2: Attack findings

**F1 (primary, AP309 variant).** The Wave-15 split was stated in the scope remarks but NOT inscribed as a sibling proposition. Both `rem:super-yangian-scope` (lines 159-163 pre-heal) and `rem:parity-balance-scope-gl-only` (lines 482-486 pre-heal) forwarded the osp-super sub-case to `prop:mc3-type-BCD-reflection-shapovalov-platonic` "generalised to Z/2-graded reflection equations". Inspection of that proposition (lines 258-299):

- Statement scope: `Y^{tw}_\hbar(so_n)`, `Y^{tw}_\hbar(sp_n)` — Molev-Ragoucy twisted Yangians only.
- R-matrix: ordinary (ungraded) rational R.
- Pairing: ordinary reflection-equation pairing.
- Central witness: `sdet K(u)` (ordinary Sklyanin determinant).

The Z/2-graded reflection-equation generalisation differs in four load-bearing places:
1. R-matrix: Kulish-Reshetikhin rational `R^{osp}(u) = Id − ℏ P_s/u − ℏ Q / (u + ℏ κ_{osp}/2)` with graded permutation `P_s` and invariant projector `Q`.
2. Pairing: Z/2-graded reflection-equation pairing (supertraces).
3. Central witness: super-Sklyanin-Berezinian `sBer K(u)`, NOT ordinary `sdet K(u)`.
4. Non-degeneracy and singular-vector steps are the super analogues of Molev-Ragoucy, partial evidence in ACDFR at osp(1|2), osp(2|2) only; rank-(m,2n) open.

The proof of `prop:mc3-type-BCD-reflection-shapovalov-platonic` (lines 284-298) invokes three distinct Molev-Ragoucy inputs (non-degeneracy, singular vectors, centrality lemma) that are ordinary (non-graded). The statement "generalised to Z/2-graded reflection equations" is a silent promotion from a verified ordinary theorem to a conjectural graded sibling. AP309 (primary-source citation for strictly weaker claim, silently extrapolated to stronger claim), scoped at remark forwarding level rather than proof-body level.

**F2 (arXiv prefix drift).** Vol I line 155 (pre-heal) wrote `arXiv:math/0304188`; Vol III bibentry line 34 writes `arXiv:math-ph/0304188`. The canonical arXiv identifier for the ACDFR 2003 paper "General boundary conditions for the sl(N) and sl(M|N) open spin chains" is `math-ph/0304188`. Vol I prefix `math/` was wrong (AP285 alias section-number-drift variant, at arXiv-prefix level). Same drift at line 476 (pre-heal) in `rem:parity-balance-scope-gl-only`.

**F3 (attribution precision).** The ACDFR 2003 paper (math-ph/0304188) covers `sl(N)` and `sl(M|N)` open spin chains. The `osp(m|n)` reflection-equation presentations cited in Vol III bibentry ("see also the osp(m|n) reflection-equation presentations... in the related series of papers") are a separate series by the same authors, NOT the 2003 paper itself. Both the pre-heal Vol I `rem:super-yangian-scope` and `rem:parity-balance-scope-gl-only` cited ACDFR 2003 as THE source of the osp-super reflection-equation construction, which overstates what that single paper proves.

**F4 (Vol III consistency).** Vol III K3 chapter is correctly scoped (AP246 healed: Y(gl) → Y(osp) rename atomic; `conj:osp-yangian-mukai` conjectural; `rem:gl-to-osp-correction` inscribed). No Vol III violation.

**F5 (CLAUDE.md MC3 row).** The CLAUDE.md row correctly names the split and points at `rem:super-yangian-scope` + `rem:parity-balance-scope-gl-only`. The row does not claim the osp-super sub-case is proved, so no CLAUDE.md update needed (AP271 reverse-drift negative).

## Phase 3: Heal

Option chosen: inscribe a separate Conjectured proposition for the osp-super sub-case rather than force `prop:mc3-type-BCD-reflection-shapovalov-platonic` to cover both. Rationale: the two statements share reflection-equation scaffolding but differ in R-matrix, pairing, and central witness; per AP279 (rename heal island-local, semantic drift not just name) and AP274 (rhetorical functor identification across disjoint objects), forwarding one into the other was a rhetorical fusion of two disjoint objects. The sibling proposition is the honest statement.

Edits to `chapters/theory/mc3_five_family_platonic.tex`:

1. Lines 147-177: `rem:super-yangian-scope` updated. Removed "mechanism of Proposition~\ref{prop:mc3-type-BCD-reflection-shapovalov-platonic} in its Z/2-graded form". Replaced with "sibling to Proposition~\ref{prop:mc3-type-BCD-reflection-shapovalov-platonic}, inscribed as the separate Conjecture~\ref{conj:mc3-osp-super-reflection-equation-platonic}, not as a specialisation...". Fixed arXiv prefix `math/` → `math-ph/`. Added attribution precision ("the orthosymplectic reflection-equation presentations appear in the related series of papers by the same group").

2. Lines 469-487 → expanded: `rem:parity-balance-scope-gl-only` updated. Removed "covered by Proposition~\ref{prop:mc3-type-BCD-reflection-shapovalov-platonic} generalised to Z/2-graded reflection equations, an instance of the twisted B/C/D mechanism". Replaced with "covered by Conjecture~\ref{conj:mc3-osp-super-reflection-equation-platonic}, a sibling statement to the ordinary twisted B/C/D reflection-equation proposition... the two share the reflection-equation scaffolding, but their R-matrix, pairing, and central witness differ, so the statements are genuinely sibling rather than parent-specialisation." Fixed arXiv prefix. Added attribution-precision parenthetical.

3. NEW `\begin{conjecture}[Orthosymplectic super-Yangian reflection-equation Shapovalov; \ClaimStatusConjectured]` at `\label{conj:mc3-osp-super-reflection-equation-platonic}` (the Kulish-Reshetikhin R-matrix with κ_osp = m − 2n − 2, graded permutation, invariant projector, K(u) reflection matrix in ACDFR series, evaluation-generated core thickness at generic parameters, sBer K(u) as central witness).

   AP40 post-heal: initially inscribed as `\begin{proposition}[...\ClaimStatusConjectured]`, hook flagged AP40 (ClaimStatusConjectured inside proof-bearing environment); healed to `\begin{conjecture}` with `conj:` label prefix (HZ-2 decision tree: uncertain proof ⇒ default `\begin{conjecture}`).

4. NEW `\begin{remark}[Scope and residual frontier of the osp-super reflection-equation conjecture]` at `\label{rem:mc3-osp-super-reflection-equation-scope}`: enumerates three inputs (non-degeneracy of Z/2-graded RE pairing; graded singular-vector short exact sequences; Z/2-graded centrality of sBer K(u)) that are unverified at rank (m,2n) and explicitly ties the K3 super-Yangian `conj:osp-yangian-mukai` in Vol III to this chapter's conjecture: "closing either closes the other."

5. Lines 746-752 (`cor:five-family-union-coverage` sub-case enumeration): retargeted `Proposition~\ref{prop:mc3-type-BCD-reflection-shapovalov-platonic}` to `Conjecture~\ref{conj:mc3-osp-super-reflection-equation-platonic}` for the osp-super sub-case, kept the ordinary B/C/D proposition reference as sibling cross-reference, with explicit `\ClaimStatusConjectured` scope tag at the corollary clause.

Grep verified after heal: all `\ref{conj:mc3-osp-super-...}` resolve to the new conjecture label; all `\ref{prop:mc3-type-BCD-reflection-shapovalov-platonic}` resolve to the unchanged ordinary proposition.

## Phase 4: Cross-volume check (AP5)

- Vol II grep for `mc3-osp-super` or `prop:mc3-super-parity-balance`: 0 hits (no cross-volume consumers).
- Vol III grep for `mc3-osp-super` or `prop:mc3-super-parity-balance`: 0 hits.
- Vol III `k3_yangian_chapter.tex` remains the sole consumer of the K3 super-Yangian claim and already carries `conj:osp-yangian-mukai` at Conjectured. Cross-volume dependency chain now: Vol III `conj:osp-yangian-mukai` and Vol I `conj:mc3-osp-super-reflection-equation-platonic` share the same (a)-(b)-(c) gap, inscribed at the new Vol I `rem:mc3-osp-super-reflection-equation-scope`.
- CLAUDE.md MC1-4 row unchanged: it already describes the split without claiming the osp-super sub-case is proved.

## Phase 5: Build + test status

`make fast` from Vol I root fails: `pdflatex: command not found` in session environment (AP293 prerequisite-missing pattern). Build verification deferred to a session with pdflatex available; edits are LaTeX-syntactically clean (env renames atomic, label renames atomic, `\ref` consumers verified resolved via Grep). No commits requested.

## AP ledger (minimal per AP314)

Session inscribed NO new AP blocks. The four findings (F1-F4) map to existing patterns:
- F1 → AP309 (primary-source citation for strictly weaker claim, silently extrapolated) scoped at remark-forwarding layer.
- F2 → AP285 (alias section-number drift) at arXiv-prefix level.
- F3 → AP272 (unstated cross-lemma via folklore citation) at attribution-precision level.
- F4 positive (Vol III already AP246+AP279-healed).
- F5 negative (AP271 not fired).

The heal pattern itself is an instance of AP266 (sharpened-obstruction healing register): a failed bare "covered by ordinary B/C/D" becomes an explicit Conjectured sibling proposition with the three (a)-(b)-(c) gaps enumerated, tied to the K3 Vol III consumer, yielding a Beilinson falsification test (closing (a)-(b)-(c) closes both). No AP inflation (respects AP314).

## Files touched

- `chapters/theory/mc3_five_family_platonic.tex` (Vol I): 5 edits (2 remark rewrites, 1 new conjecture, 1 new scope remark, 1 corollary sub-case retarget).

No changes to Vol II, Vol III, CLAUDE.md, or bibliography files. AP5 cross-volume propagation clean.
