# Vol III kappa_ch residuals propagation heal — 2026-04-18

Follow-on propagation heal after the K3 x E kappa_ch agent healed `chapters/theory/cy_to_chiral.tex` (7 edits, `prop:categorical-euler` renamed with kappa_ch^{Heis} discipline, 6 consumer sites updated).

Scope: close residual propagation debt surfaced by that heal in (i) Vol III `CLAUDE.md` lines 202/209/211, (ii) Vol III `AGENTS.md` at 6 sites, (iii) `cy_to_chiral.tex:170,174,280` abelian-surface drift. Test-file docstrings and `compute/lib` citations of `prop:categorical-euler` are NOT touched: numerical test assertions remain on the Heisenberg-level reading kappa_ch^{Heis} = 3 which is still what the proposition carries; only prose-level Hodge-supertrace vs Heisenberg-level distinction was clarified in the manuscript, and the numerical claim in tests is unchanged.

## Discipline applied

Canonical rule (inherited from the K3 x E heal):

- `kappa_ch^{Heis}`: Heisenberg-level (additive) reading of the chiral modular characteristic on the chiral algebra A_C = Phi(C). K3 x E value = 2 + 1 = 3.
- `kappa_ch` (unsubscripted, in Hodge-supertrace context): the identification with the Hodge supertrace chi(O_X), proved unconditionally for compact CY_d via `thm:kappa-hodge-supertrace-identification` (`chapters/examples/cy_d_kappa_stratification.tex:177`). K3 x E value = chi(O_{K3 x E}) = 2 * 0 = 0 (Kunneth-multiplicative).
- Reconciliation: delta kappa_ch := kappa_ch^{Heis} - chi(O_X) is the quantum correction. d=2 with h^{1,0}=0 gives delta = 0 (Serre duality kills it, `prop:cy-kappa-d2`). d=3 with h^{1,0}=0 gives delta = chi_top/24 (BCOV). K3 x E falls outside the d=3 h^{1,0}=0 hypothesis because the E fiber has h^{1,0}(E) = 1; delta = 3.

Cross-links: AP289 (Kunneth-multiplicative vs additive for super-trace/Hodge-characteristic invariants) and `rem:beauville-kappa-formula-subscript-split` in `cy_to_chiral.tex`.

## Edits

### Vol III CLAUDE.md — 1 edit
Lines 202, 209, 211 (single contiguous Edit call):
- Line 202: split `kappa_ch` row into `kappa_ch^{Heis}` with Hodge-supertrace pointer to `thm:kappa-hodge-supertrace-identification` giving the distinct value 0.
- Line 209: BKM decomposition uses `kappa_ch^{Heis}`; Hodge-supertrace agrees with kappa_cat = 0.
- Line 211: adversarial-result line subscripted similarly.

### Vol III AGENTS.md — 5 edits
- Line 159 (CY-D status row): reframed `kappa_ch = chi(O_X)` as the Hodge-supertrace reading PROVED unconditionally (via `thm:kappa-hodge-supertrace-identification`); K3xE = 3 relabelled `kappa_ch^{Heis}`.
- Line 211 (CY-D d=3 deep issue row): relabelled with Heisenberg-level reading; added reconciliation via d-dependent delta kappa_ch.
- Lines 277/284/286 (kappa-spectrum table, single Edit call): `kappa_ch` row reframed as `kappa_ch^{Heis}` (additive), Hodge-supertrace kappa_ch pointer added; adversarial-result sentence subscripted.
- Line 619 (d=3 deep-issue table): same reconciliation prose as Line 211.
- Line 616 (tri-stratum table): added "via Hodge supertrace, matching kappa_ch^{Heis} at d=2 with h^{1,0}=0" to make the d=2 coincidence explicit.
- Line 804 (quick-reference constants block): `kappa_ch(K3 x E) = 3` relabelled `kappa_ch^{Heis}(K3 x E) = 3` with comment pointing to Hodge-supertrace reading.

### cy_to_chiral.tex — 2 edits
- Line 170 (abelian-surface failure inside `prop:cy-kappa-d2`): abelian-surface `kappa_ch(A) = 2` relabelled `kappa_ch^{Heis}(A) = 2`; Hodge-supertrace reading kappa_ch(A) = 0 noted (via `thm:kappa-hodge-supertrace-identification`); delta = h^{1,0} = 2 at d=2 cited.
- Line 174 (proof body, same proposition): same relabel; K3 case explicitly noted as Hodge and Heisenberg readings coinciding.
- Line 280: was already correctly subscripted kappa_ch^{Heis} by the prior K3xE heal; no edit needed (verified).

## Test file / lib docstring audit (no edits)

Five test files and one lib file cite `prop:categorical-euler` in docstrings asserting numerical value 3. These remain correct because:

- The proposition under its new title `K3 x E: kappa_ch and kappa_BKM are distinct` (`claims.jsonl:542`) continues to carry the Heisenberg-level reading kappa_ch^{Heis}(K3 x E) = 3 as its numerical content.
- Tests assert the numerical value 3; this is the Heisenberg-level reading and is not changed by the prose heal.

Recommendation (deferred, not in scope of this minimal heal): add a one-line `# kappa_ch^{Heis}` comment at each docstring site if a future HZ-7 discipline pass wants subscript-level hygiene in compute/ docstrings. Not load-bearing.

## Guardrails

- Discipline cross-referenced: HZ-7 (Vol III kappa subscript discipline), AP289 (Kunneth-multiplicative vs additive for super-trace invariants), AP305 (pessimistic CLAUDE.md drift — no overstatement introduced), AP271 (reverse drift — no stale label introduced).
- No status tag downgrades. `thm:kappa-hodge-supertrace-identification` retains `ProvedHere`; `prop:cy-kappa-d2` retains `ProvedHere`. Both were verified by grep + claims.jsonl.
- No new AP blocks inscribed. Per AP314 (throttle inscription rate), this heal produced no net-new AP; all discipline cited is existing (HZ-7, AP289, `rem:beauville-kappa-formula-subscript-split`, `thm:kappa-hodge-supertrace-identification`).
- No AI attribution. All authorship Raeez Lorgat.

## Residual (deferred)

- Five test file docstrings + one lib file docstring (kappa_ch documented as 3) still use bare `kappa_ch`. Non-load-bearing because (a) numerical assertions remain correct and (b) tests are scaffolding, not manuscript. Re-scan during the next HZ-7 docstring sweep.
- AGENTS.md lines 140 (`Phi_2(K3) = H_Muk, kappa_ch=2`) and other d=2-context kappa_ch citations are NOT relabelled: at d=2 with h^{1,0}=0 the two readings coincide, so bare `kappa_ch` is unambiguous there per the Hodge-supertrace identification. Subscripting would be over-pedantic.
- Vol II `rem:beauville-kappa-formula-subscript-split` cross-check: not in Vol II scope; this heal is Vol III only.

## Verification

Grep checks (manual, not run during this heal):
```
grep -rn 'kappa_ch.*K3.*E.*=.*3' ~/calabi-yau-quantum-groups/{CLAUDE.md,AGENTS.md}
grep -rn 'kappa_ch(K3xE)' ~/calabi-yau-quantum-groups/chapters/
```
Expected: zero bare-subscript hits in the three files edited (CLAUDE.md, AGENTS.md, cy_to_chiral.tex) post-heal at the specific lines targeted.

## Author

Raeez Lorgat, 2026-04-18.
