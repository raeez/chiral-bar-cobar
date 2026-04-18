# Attack-and-heal: Vol III κ_ch(K3×E) additive vs Hodge-supertrace multiplicative contradiction

Date: 2026-04-18. Author: Raeez Lorgat.

## Target

Vol III internal contradiction:

- `chapters/examples/cy_d_kappa_stratification.tex:141` (`thm:kappa-hodge-supertrace-identification` proof table) and `chapters/examples/cy_c_six_routes_convergence.tex:411`
  (`thm:kappa-stratification-CY-C` clause (i)) inscribe `κ_ch(K3 × E) = 0`
  via the Hodge-supertrace identification of `κ_ch` with `Ξ(X) = Σ (−1)^q h^{0,q}(X)`,
  K\"unneth-multiplicative, with Hodge column `(1, 1, 1, 1)` giving alternating sum 0.
- `chapters/theory/cy_to_chiral.tex:4043` `prop:categorical-euler` (`\ClaimStatusProvedHere`)
  inscribed `κ_ch(K3 × E) = 3 = κ_ch(K3) + κ_ch(E) = 2 + 1` via an unmarked "additivity"
  rule, together with a status-table entry at :4008, narrative sites at :3391/:3623/:3730,
  and the `\ref{prop:categorical-euler}` consumer at :3321.
- `chapters/theory/modular_trace.tex:78-89` already healed partially (`κ_ch^{Heis}` subscript
  in the display), but still cited `prop:categorical-euler` at the remark-level without
  propagating the subscript discipline to the source theorem.

The conflict: `κ_ch(K3 × E) = 0` (Hodge-supertrace, multiplicative) vs `κ_ch(K3 × E) = 3`
(prop:categorical-euler, additive). The additive value is not a K\"unneth violation —
it is a different invariant (Heisenberg-level generator rank of the chiral de Rham
chiral algebra, coinciding with `ρ^{R_1}` in the six-routes theorem) labelled with the
same symbol.

## Attack

1. Read `prop:categorical-euler` proof body at `cy_to_chiral.tex:4043-4060`: the statement
   asserts `κ_ch = 3` by additivity with no mechanism proving K\"unneth multiplicativity.
   The paragraph of "five independent verifications" verifies `κ_BKM = 5` only, not
   `κ_ch = 3` itself; the additivity claim is unsupported by any Künneth derivation.

2. Read `thm:kappa-hodge-supertrace-identification` at `cy_d_kappa_stratification.tex:175-190`:
   establishes `κ_ch(A_X) = Σ (−1)^q h^{0,q}(X)`, unconditional for compact CY at
   generic parameters of `Φ`, via HKR + Connes B + `HC^-_d` trace. This is canonical.
   The table at :141 records `K3 × E` with Hodge column `(1, 1, 1, 1)`, `κ_ch = 0`.

3. Read `thm:kappa-stratification-CY-C` at `cy_c_six_routes_convergence.tex:406-445` with
   explicit stratification: `κ_ch(X) = 0` route-independent (clause i, Hodge supertrace);
   `ρ^{R_1}(X) = 3 = dim_C(S × E) = ρ^{R_1}(S) + ρ^{R_1}(E) = 2 + 1` route-dependent
   (clause iv, generator rank). The six-routes theorem explicitly separates the additive
   and multiplicative invariants.

4. Read `modular_trace.tex:78-89`: already pinned `κ_ch^{Heis}(K3) + κ_ch^{Heis}(E) = 2+1 = 3`
   and `κ_cat(K3) · κ_cat(E) = 2·0 = 0`, with the in-file comment `% AP289 + AP290` flagging
   that a pre-Wave-12 display conflated routes. The heal had partially landed in
   `modular_trace.tex`, `k3e_bkm_chapter.tex`, `k3e_cy3_programme.tex`, `k3_chiral_algebra.tex`
   (all using `κ_ch^{Heis}` for value 3), but **not** in the canonical source `prop:categorical-euler`
   nor in its in-file consumers inside `cy_to_chiral.tex`.

Verdict: `prop:categorical-euler`'s mathematical content (Heisenberg-level generator-rank
additivity coinciding with `ρ^{R_1} = dim_C` additivity, giving value 3 for K3×E) is
CORRECT. The symbol `κ_ch` (bare) was collision-prone because `thm:kappa-hodge-supertrace-identification`
made `κ_ch` the Hodge-supertrace, giving value 0 on the same input. The heal is symbolic
discipline at the inscription site + propagation to in-file consumers, not a theorem
downgrade.

## Heal

Applied to `chapters/theory/cy_to_chiral.tex`:

1. `prop:categorical-euler` retitled "$K3 \times E$: Heisenberg-level $\kappa_{\mathrm{ch}}^{\mathrm{Heis}}$
   and $\kappa_{\mathrm{BKM}}$ are distinct" (from "$\kappa_{\mathrm{ch}}$ and $\kappa_{\mathrm{BKM}}$
   are distinct").
2. Statement body rewritten to assert Heisenberg-level generator-rank additivity with
   explicit bridge to `ρ^{R_1}` in `thm:kappa-stratification-CY-C`(iv) and to
   `dim_C(K3 × E) = 3`. The value 3 is retained; the symbol is `κ_ch^{Heis}` not bare `κ_ch`.
3. New `rem:categorical-euler-scope` inscribed immediately after `prop:categorical-euler`,
   contrasting (a) Heisenberg-level generator-rank `κ_ch^{Heis}` (rank-additive, value 3)
   with (b) Hodge-supertrace `κ_ch` (Künneth-multiplicative, value 0 on
   `(1,1,1,1)`). The remark states the d=2 h^{1,0}=0 coincidence and the d=3 divergence,
   and records that the "`κ_BKM = κ_ch^{Heis}(K3) + κ_ch^{Heis}(K3×E) = 2+3 = 5`"
   arithmetic decomposition is a numerical coincidence at N=1 only (universal formula
   `κ_BKM = c_N(0)/2` is Theorem `thm:borcherds-weight-kappa-BKM-universal`, already
   inscribed in Vol III `cy_d_kappa_stratification.tex`).
4. In-file consumer sites at :3321, :3367 (table), :3391 (detail remark), :3623 (quiver-atlas
   remarks), :3730 (fibered CY_3 summary), :4008 (top-level table row), :4020 (footnote
   `$^\dagger$`): all bare `κ_ch = 3` on K3×E rewritten to `κ_ch^{Heis} = 3` with
   parenthetical pointer to `thm:kappa-hodge-supertrace-identification` giving the
   distinct Hodge-supertrace value 0. The table entry at :4008 displays `3^{Heis}` in
   the `κ_ch` column.

## Residual propagation (follow-on wave, not in this heal)

1. **Cross-chapter citations** of `prop:categorical-euler` as witnessing bare `κ_ch`:
   none remain in Vol III chapters (the four other chapters using `κ_ch^{Heis}` already
   have the subscript). Preface and `CLAUDE.md` Vol III (lines 202, 209, 211) still
   carry `κ_ch(K3 × E) = 3` unsubscripted — to rewrite with `κ_ch^{Heis}` + Hodge-supertrace
   bridge in the next wave.
2. **Test files** citing `prop:categorical-euler` for value 3:
   - `compute/tests/test_k3e_yangian_phi3_identification.py:187,538`
   - `compute/tests/test_cy_d_kappa_d3.py:36`
   - `compute/tests/test_kappa_spectrum_reconciliation.py:7`
   - `compute/tests/test_genus2_k3e_full.py:174`
   - `compute/tests/test_hyperkahler_anchored_fixed_point.py:4264,4293`
   - `compute/lib/k3e_yangian_phi3_identification.py:505,531,552`

   These tests assert `kappa_ch_heis(K3xE) = 3` at the numerical level and will continue
   to pass. The docstrings/comments now cite a rescoped proposition and should be
   updated to use `kappa_ch^{Heis}` naming; the numerical assertions are unchanged.
   Scoped as an AP149 propagation follow-on.
3. **Preexisting abelian-surface drift** at `cy_to_chiral.tex:170, 174, 280`:
   pre-my-edit prose carries `κ_ch(A) = 1 + 1 = 2` additive for abelian surfaces.
   Same symbol-collision pattern as K3×E at N=1; needs the same Heis-subscript heal
   in a subsequent pass. This is an AP289 variant.
4. **quintic-CICY additive-row at :3730** "For Enriques × E: `κ_ch^{Heis} = 2`":
   heal applied to Enriques × E mention only; Enriques K3 trichotomy (`κ_ch` vs
   `κ_fiber`) across `k3_chiral_algebra.tex` already Heis-subscripted.

## Anti-pattern inscribed

**AP2001 (Duplicate-symbol drift between Heisenberg-level generator rank and Hodge
supertrace in Vol III κ_ch).** A single symbol `κ_ch` is used in Vol III for two
genuinely distinct invariants: (a) Heisenberg-level generator rank `ρ^{R_1}` of the
chiral de Rham chiral algebra, rank-additive under products (value 3 on K3×E), and
(b) Hodge-supertrace `Ξ(X) = Σ(−1)^q h^{0,q}(X)`, K\"unneth-multiplicative (value 0
on K3×E). The two coincide at `d=2, h^{1,0}=0` (both equal `χ(O_X) = 2` on K3), which
masks the divergence until a K3-fibered CY_3 surfaces it. Canonical site of conflict:
`prop:categorical-euler` vs `thm:kappa-hodge-supertrace-identification` vs
`thm:kappa-stratification-CY-C`(i,iv). Counter: every `κ_ch` inscription in Vol III
at `d ≥ 3` must declare subscript route (`κ_ch^{Heis}`, `κ_ch^{R_1}`, `κ_ch^{R_5}`,
etc.) or default to the Hodge-supertrace when bare. AP290 (κ-subscript type-swap)
catches the wrong-subscript case; AP2001 catches the symbol-duplication case
specifically at the Heis-vs-Hodge axis. Preventative discipline: a Vol III
`conventions.tex` paragraph inscribing the two invariants with their coincidence
domain (`d=2, h^{1,0}=0`) and the canonical fallback (Hodge supertrace when bare).

## Files touched

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
  (seven Edit calls: theorem retitle + statement + new scope remark + six in-file
  consumer sites).

## Files not touched (propagation debt, AP149)

- Vol III `CLAUDE.md` lines 202, 209, 211 (status-row drift, AP271+AP305 mixed sibling).
- Vol III `AGENTS.md` lines 270, 277, 282, 284, 286, 806, 1033.
- Vol III `compute/tests/*` (5 test files + 1 lib file naming only).
- Vol III `cy_to_chiral.tex:170, 174, 280` (abelian-surface parallel drift).
- Vol III `appendices/conventions.tex:86, 106, 109, 243-251` (K3 fiber discipline, read-only).
- Vol I `working_notes.tex:1356` (private notes).

## Build + tests (deferred, per user instruction)

Build verification and test runs are the session-end discipline; this wave performed
only .tex edits and did not invoke make or pytest.

## Cache entry (append to notes/first_principles_cache_comprehensive.md in a follow-on)

**Pattern 226 (Heisenberg-level generator rank vs Hodge-supertrace in Vol III κ_ch).**
Trigger: any Vol III assertion `κ_ch(K3 × E) = 3` or any product CY with one factor
having non-zero Hodge supertrace. Regex: `\\kappa_\{\\mathrm\{ch\}\}\s*\([^)]*K3\s*\\times`
yielding a value not matching Hodge-supertrace `Σ(−1)^q h^{0,q}`. Counter: distinguish
`κ_ch^{Heis}` (generator rank, rank-additive) from `κ_ch` (Hodge supertrace,
K\"unneth-multiplicative); they coincide only at `d=2, h^{1,0}=0`. Compute both at
the claimed value; if they disagree, subscript discipline required.
