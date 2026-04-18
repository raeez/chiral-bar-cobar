# Attack-and-Heal: Quantum Determinant Decreasing-Column Ordering

Session 2026-04-18. Target: `lem:qdet-central-all-N` + `rem:qdet-decreasing-ordering` + `rem:qdet-column-ordering` in `chapters/theory/ordered_associative_chiral_kd.tex`; test file `compute/tests/test_quantum_determinant_centrality.py`; CLAUDE.md `FM33a` + qdet status row.

## Phase 1. Map of the terrain

Three locations inscribe the qdet ordering claim:

1. `chapters/theory/ordered_associative_chiral_kd.tex:10850-10899` — `lem:qdet-central-all-N` (`\ClaimStatusProvedElsewhere`) attributing to Molev `\cite{Molev07}` Thm 1.6.4 + 1.11.2 via antisymmetriser.
2. `ordered_associative_chiral_kd.tex:10901-10940` — `rem:qdet-decreasing-ordering` stating the increasing-index variant `\mathrm{qdet}^\uparrow T(u)` fails centrality "at order `\Psi^2`" for `N \geq 3`.
3. `ordered_associative_kd.tex:12290-12298` — `rem:qdet-column-ordering` summarising with "74 compute tests".

Test file has six test functions plus one HZ-IV sentinel. Report-counter-based static tally: 54 (`test_centrality`, `(N,M) in {(2,2),(3,2)}` × 3 Ψ × 3 u × 3 v) + 3 (`test_n2_explicit`) + 3 (`test_n3_explicit`) + 3 (`test_qdet_is_scalar`) + 3 (`test_classical_limit`) + 8 (`test_consistency_across_sites`, 4 M × 2 checks) = **74 assertions via `report()` counter** — matches manuscript claim exactly. The HZ-IV sentinel adds 3 `assert` statements not counted toward the 74.

## Phase 2. Molev citation check

Molev, "Yangians and Classical Lie Algebras," AMS Mathematical Surveys and Monographs 143, 2007. Theorem 1.6.4 is the column-determinant formula in §1.6 (column ordering: the proof in Molev uses a specific product convention under the RTT relation that collapses the antisymmetriser iteration); Theorem 1.11.2 in §1.11 establishes centrality via the antisymmetriser image in `(\bC^N)^{\otimes N}`. The lemma's `\ClaimStatusProvedElsewhere` tag with Molev attribution is correctly scoped; the chiral extension (Steps at :10882-10898) is a one-paragraph bridge argument via `\Delta_z`, sound given the classical input.

## Phase 3. First-principles N=3 centrality computation

Pure-Python verification using `fractions.Fraction` for exact arithmetic on the evaluation representation `(\bC^3)^{\otimes 2}` with `L_k(u) = (u-a_k)I + \Psi P_{0,k}`, Yang R-matrix convention.

Four candidate qdet variants tested:

- `col_dec` (Molev `eq:glN-qdet`): column-determinant, `j=N-1` leftmost, spectral shift `u-j\Psi` at column `j`. Formula: `\sum_\sigma \mathrm{sgn}(\sigma) T_{\sigma(N-1),N-1}(u-(N-1)\Psi) \cdots T_{\sigma(0),0}(u)`.
- `col_inc` (same spectral shifts, REVERSED product order): `j=0` leftmost, spectral shift on factor at position `j` is `u-(N-1-j)\Psi`. Formula: `\sum_\sigma \mathrm{sgn}(\sigma) T_{\sigma(0),0}(u-(N-1)\Psi) \cdots T_{\sigma(N-1),N-1}(u)`.
- `row_dec`: row-determinant, `i=N-1` leftmost, shift `u-i\Psi` at row `i`.
- `qdet^\uparrow` (CLAUDE.md remark definition at :10904-10913): row-determinant with `u-(N-i)\Psi` shift, `i=1` leftmost. Equivalent in 0-indexed form to `T_{0,\sigma(0)}(u-(N-1)\Psi) \cdots T_{N-1,\sigma(N-1)}(u)`.

Results at `N=3, M=2`, generic rational `(u,v,\Psi,\mathrm{params})`:

| variant | `max |[qdet,t_{ij}(v)]|` | central? |
|---------|-------------------------|----------|
| `col_dec` | `0` (exact) | YES |
| `col_inc` (reversed product, same shifts) | `0` (exact) | YES |
| `row_dec` | `2.12 \times 10^{-2}` | NO |
| `qdet^\uparrow` (CLAUDE.md row-det, reverse shifts) | `2.12 \times 10^{-2}` | NO |

Element equalities (are the formulas the same element?):

- `col_dec = col_inc` (exact `Fraction` zero difference) — **the product-order of the column-determinant is actually ordering-agnostic given fixed spectral shifts**, because the sum over `S_N` and the signs absorb the reorientation.
- `col_dec \neq row_dec` (difference `\sim 7 \times 10^{-2}`) — column- and row-determinants give DIFFERENT Yangian elements.

**Failure-order for `qdet^\uparrow`**: log-log slope of `|[qdet^\uparrow, t_{ij}]|` vs `\Psi` as `\Psi \to 0` at `N=3`:

| `\Psi` | commutator_max | log-slope (prior) |
|--------|----------------|-------------------|
| 1/8 | 1.71e-5 | — |
| 1/16 | 1.11e-6 | 3.941 |
| 1/32 | 1.80e-7 | 2.632 |
| 1/64 | 2.84e-8 | 2.659 |
| 1/128 | 3.96e-9 | 2.843 |
| 1/256 | 5.22e-10 | 2.924 |
| 1/512 | 6.69e-11 | 2.963 |

Asymptotic slope converges to **3**, not 2. The leading failure order is `O(\Psi^3)`, NOT `O(\Psi^2)` as the manuscript remark claims.

## Phase 4. Findings ledger

**F1. 74-test claim VERIFIED.** Static assertion count = 74 (via `report()` counter). HZ-IV sentinel adds 3 `assert`s, not counted. Test coverage: `N \in \{2,3\}`, `M \in \{1,2,3,4\}`, `\Psi \in \{0, 0.5, 1.0, 2.0\}`, three-point `(u,v)` sampling per (N,M,\Psi). Multi-N coverage is present.

**F2. Molev citation Thm 1.6.4 + 1.11.2 CORRECTLY ATTRIBUTED.** Column-determinant formula + antisymmetriser centrality proof are in Molev's monograph at the cited theorems. `\ClaimStatusProvedElsewhere` tag is honest.

**F3. CRITICAL — `rem:qdet-decreasing-ordering` contains a factual error on failure ORDER.** The remark at :10929-10930 states: "the commutator `[\mathrm{qdet}^\uparrow T(u), t_{ij}(v)]` is generically nonzero at order `\Psi^2` in the trigonometric expansion." First-principles evaluation at `N=3, M=2` with asymptotic `\Psi \to 0` gives log-log slope converging to 3: the leading failure order is `O(\Psi^3)`, not `O(\Psi^2)`. The qualitative claim "not central" is correct; the quantitative "order `\Psi^2`" is wrong by one power.

**F4. CRITICAL — `rem:qdet-decreasing-ordering` conflates two distinct things.** The remark contrasts decreasing-index qdet with an INCREASING-index `qdet^\uparrow` defined at :10904-10913 via `\prod_{i=1}^N T_{i,\sigma(i)}(u-(N-i)\Psi)` — this is a ROW-determinant with the REVERSED spectral-shift pattern (factor at leftmost position has the LARGEST shift). What actually fails centrality at `N \geq 3` is the **row-determinant** (equivalently, the increasing-index column-det with reversed spectral shifts); what stays central is any column-determinant with the standard shift pattern `u-j\Psi` at column `j`, INDEPENDENTLY of product order. The remark's own load-bearing sentence at :10935-10937 admits this: "both orderings are preserved by `\Delta_z` (the argument of Lemma is ordering-agnostic), so the decreasing-index qdet is the chirally central element for every `N \geq 1`." This contradicts the remark's headline claim that "only the decreasing-index formula produces a central element."

**F5. The central invariant is the SPECTRAL-SHIFT PATTERN, not the product ordering.** First-principles derivation: at `N=3, M=2`, `col_dec` and `col_inc` (same shifts `u-j\Psi`, reversed product order `j=0` leftmost vs rightmost) give the SAME element (exact-`Fraction` zero difference). Both are central. The non-central variant `qdet^\uparrow` uses REVERSED shifts (leftmost position gets `(N-1)\Psi`); this is where centrality fails. Molev Thm 1.6.4 proves the column-determinant with the canonical shift pattern is central; the column-vs-row contrast is the genuine structural distinction, as is the shift-pattern reversal.

**F6. CLAUDE.md FM33a entry is imprecise.** "qdet column ordering DECREASING (j=N-1 leftmost). Left-to-right NOT central at N>=3 (agrees N=2 by coincidence). Cite Molev 1.6.4." The "left-to-right" phrasing conflates the product-order invariance with the spectral-shift-pattern load-bearingness; a reader interprets "left-to-right" as product-order, but what is actually load-bearing is the shift pattern.

**F7. Chiral coproduct compatibility.** The manuscript lemma proof at :10882-10898 argues `\Delta_z` preserves centrality via the antisymmetriser commuting with `T_i(u) \mapsto \Delta_z(T_i(u))`. The test file does not perform an independent numerical check of `[\mathrm{qdet}\,\Delta_z(T)(u), \Delta_z(t_{ij})(v)] = 0`; it tests centrality only for the raw (non-`\Delta_z`-specialised) qdet. Adding a `\Delta_z` test at `N=3` would tighten the HZ-IV decorator (currently sentinel runs at `N=2` only).

## Phase 5. Heal plan

**H1 (high priority).** Rewrite `rem:qdet-decreasing-ordering` to distinguish:
- `col_dec` = `col_inc` = the column-determinant with canonical spectral shifts (central at all `N \geq 1`, product-order agnostic as an element of `Y(\gl_N)`);
- `qdet^\uparrow` with REVERSED spectral shifts (the row-det / increasing-index variant the remark currently critiques);
- `row_dec` with standard shifts but row-det (ALSO non-central at `N \geq 3`; not currently discussed).

Correct the "order `\Psi^2`" to "order `\Psi^3`" with the log-log slope witness as justification. Reframe the headline: "The SPECTRAL-SHIFT PATTERN, not the product ordering, is load-bearing."

**H2 (CLAUDE.md).** Rewrite FM33a to: "qdet spectral-shift pattern: column `j` carries shift `u-j\Psi`. Column-determinant with this pattern is central independently of product order (`col_dec` = `col_inc` as elements). The row-determinant, and the shift-reversed variant `qdet^\uparrow` with shift `u-(N-j-1)\Psi`, fail centrality at order `\Psi^3` for `N \geq 3`. Coincide with central form at `N = 2` by rank coincidence. Cite Molev 1.6.4."

**H3 (test file).** Add one new test `test_qdet_increasing_fails_at_n3` that builds `qdet^\uparrow` with reversed shifts and asserts `|[qdet^\uparrow, t_{ij}]| > 10^{-3}` at `N=3, \Psi=1` (non-central), contrasting with the central `col_dec` assertion already in `test_centrality`. This makes the ordering-sensitivity verification EXPLICIT in the test suite rather than implicit.

**H4 (test file).** Upgrade HZ-IV sentinel `test_qdet_centrality_hz_iv_sentinel` to include an `N=3` path, narrowing the scope gap at HZ-IV path (i): currently runs only `N=2, M=2` even though the manuscript claim is "central at all `N \geq 2`". Adding `N=3` as a second sentinel point closes an AP277 variant (decorator prose cites `N \in \{2,3\}` but body tests only `N=2`).

**H5 (manuscript, minor).** Update `rem:qdet-column-ordering` at :12290-12298 to remove the misleading sentence "only the decreasing-index ordering is central" and replace with the shift-pattern-central framing. The "74 compute tests" figure is correct and stays.

## Phase 6. Beilinson epistemic audit

CLAUDE.md FM33a + `rem:qdet-decreasing-ordering` propagated a SLOGAN ("decreasing column ordering is load-bearing") that is PARTIALLY TRUE (the shift-pattern version of the claim is correct; the product-order version is wrong). This is an AP186 shallow-correction pattern: the "decreasing" label captured the right FAMILY (column-det with canonical shifts) but the wrong DISTINGUISHING FEATURE (product order instead of shift pattern). The lemma's proof body at :10935-10937 already contained the correct statement (ordering-agnostic) while the remark headline contradicted it — an AP300 in-file ProvedHere-vs-retracted-mechanism drift where the proof proves one thing and the remark claims another without bridge.

The Beilinson-rectified scope:
- `col_dec` with spectral shifts `u-j\Psi` (`j=0,\ldots,N-1`) at column `j`: CENTRAL (Molev 1.6.4 + 1.11.2).
- `col_inc` (same shifts, reversed product order): CENTRAL; equals `col_dec` as element of `Y(\gl_N)`.
- Any row-determinant or shift-reversed variant: NON-CENTRAL at `N \geq 3`, failure at order `\Psi^3` (first-principles `Fraction`-exact verification).
- `N=2` coincidence: all four variants central because `S_2` has single non-trivial cycle collapsing the distinctions.

## Phase 7. No commit

Per pre-commit hook + AP314 restraint: inscribing 0 new APs this session. The finding is a heal-in-place of existing remark + CLAUDE.md FM33a, not a new anti-pattern. The relevant existing APs are AP186 (shallow correction without first-principles investigation), AP238 (statement-proof contradiction within a proposition), AP300 (in-file ProvedHere-vs-retracted-mechanism drift). No AP registration — each of these is an existing catalogue entry re-firing.

Heals H1-H5 drafted above; inscription into the manuscript + CLAUDE.md pending the next session with explicit user approval for the edit sequence (per "no commit" constraint on this audit session). The manuscript as it stands is MOSTLY CORRECT: `lem:qdet-central-all-N` stands (Molev citation is honest); `rem:qdet-decreasing-ordering` contains a load-bearing conflation + factual error on failure order that should be healed in a dedicated edit.

Author: Raeez Lorgat
