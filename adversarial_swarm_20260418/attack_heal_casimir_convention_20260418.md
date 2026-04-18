# Attack-and-heal: Casimir-level convention audit (AP141 / AP144 / AP312)

**Author.** Raeez Lorgat
**Date.** 2026-04-18
**Scope.** Vol I sl_2 / simple g Casimir normalization consistency across chapters, standalones, appendices, and engines.
**Status.** ATTACK — three genuine convention-mixing / cross-file-contradiction findings isolated; no HEAL edits committed in this report (heal-plan only).

## Mission

Per CLAUDE.md AP-RMATRIX consolidated record, two r-matrix conventions coexist on the affine Kac-Moody locus:

- Trace form: `r(z) = k \Omega_tr / z` (AP126 k=0 check: vanishes at abelian limit).
- KZ: `r(z) = \Omega / ((k + h^\vee) z)` (k=0 gives `\Omega / (h^\vee z) != 0` for non-abelian g).

Bridge identity named in landscape_census.tex:641 and yangians_foundations.tex:1215:
`k \Omega_tr = \Omega / (k + h^\vee)` at generic k.

A critical-level agent earlier this session reported:
`sl_2 Killing-form Casimir gives \Omega|_Sym^2 = 1/4, \Omega|_Alt^2 = -3/4`
while the engine uses `1/2, -3/2` (factor-of-2 discrepancy, "trace-form convention").

The audit examines whether the bridge identity is internally consistent, and whether the sl_2 Casimir convention matches across the critical-level theorem / engine / test layers.

## Finding F1 (AP144 bridge-identity inconsistency, severe)

Two distinct Casimir-to-Casimir rescaling identities live in Vol I without cross-reconciliation.

**Version A (basis rescaling, k-independent).** At `appendices/appendix_q_conventions.tex:16, 26` and `appendices/q_convention_bridge_appendix.tex:75-76, 104, 153-156`:

> "The normalised Killing form satisfies (·,·) = 2h^\vee (·,·)_tr, so the Casimirs satisfy \Omega = 2h^\vee \Omega_tr."

This is a tensor-level identity: normalized Killing form is `2 h^\vee` times the trace form, hence the inverse Casimir tensors are rescaled by `2 h^\vee`. It is k-independent.

**Version B (r-matrix bridge, k-dependent).** At `chapters/examples/landscape_census.tex:641`, `chapters/examples/yangians_foundations.tex:1215`, and CLAUDE.md AP-RMATRIX:

> "k \Omega_tr = \Omega / (k + h^\vee) at generic k."

This cannot be a tensor identity (LHS depends linearly in k, RHS depends as `1/(k+h^\vee)`); rearranged it says `\Omega_tr = \Omega / [k(k+h^\vee)]`, which is neither k-independent nor consistent with Version A.

**Reconciliation.** Version A is the genuine tensor identity between the two Casimir conventions. Version B is a SHORTHAND for equality of r-matrices along the torsor of Casimir-plus-Sugawara rescalings ("Casimir rescaling within the torsor, not a face-changing identity", `worldview_synthesis_2026_04_17.tex:533`). The appendix (`appendix_q_conventions.tex:26`) is HONEST about this:

> "substituting into r_{KZ} produces `2 h^\vee \Omega_tr / ((k+h^\vee) z) != k \Omega_tr / z` except after the basis rescaling absorbed in the Sugawara renormalisation."

The chapter-level and CLAUDE.md inscriptions read Version B as an unqualified identity, which it is not. This is a genuine AP144 bridge-identity violation: the bridge is stated in three canonical sources without naming the absorption step that makes it legitimate.

**Heal-plan F1.** (i) In CLAUDE.md AP-RMATRIX and the "Key Constants" block, rewrite `k \Omega_tr = \Omega / (k+h^\vee)` as:

> "Bridge: `k \Omega_tr / z = \Omega / ((k+h^\vee) z)` as flat KZ connections on Conf_2(C), via the basis rescaling `\Omega = 2 h^\vee \Omega_tr` plus the Sugawara absorption `(2h^\vee) / (k+h^\vee) \to k` which is a rescaling of the formal r-matrix parameter in the Yangian presentation, NOT a tensor identity."

(ii) In `landscape_census.tex:641`, replace the table-header `r^coll(z) = k \Omega_tr / z = \Omega / ((k+h^\vee) z)` with a parenthetical `(same KZ datum, Casimir rescaling \Omega = 2 h^\vee \Omega_tr absorbed into the level prefix)` pointing at `appendix_q_conventions.tex:26`.

(iii) In `yangians_foundations.tex:1215`, replace "at generic k" (silent on which k) with "at generic k modulo Sugawara rescaling (see appendix_q_conventions.tex:26)".

Downstream: this is AP144 operational. It does not invalidate any theorem; it names the absorption step that was silent.

## Finding F2 (AP312 three-way scalar contradiction: sl_2 Casimir eigenvalues)

The sl_2 quadratic Casimir tensor \Omega acting on V_{1/2} \otimes V_{1/2} carries two conflicting numerical signatures across Vol I:

**Normalized-Killing-form convention (\Omega eigenvalues {+1/4, -3/4}).**

- `chapters/examples/yangians_drinfeld_kohno.tex:7584-7586`: "the Casimir \Omega acts on V_{1/2} \otimes V_{1/2} with eigenvalue +1/4 on the symmetric (triplet, j=1) component and -3/4 on the antisymmetric (singlet, j=0) component."
- `standalone/e1_primacy_ordered_bar.tex:2035-2042`: `exp(2\pi i k \Omega_{sl_2}) = e^{-3\pi i k/2}` on V_0 (singlet) and `e^{\pi i k/2}` on V_1 (triplet) — matches eigenvalues `(-3/4, +1/4)` on (singlet, triplet).

**Trace-form / 2x convention (\Omega eigenvalues {+1/2, -3/2}).**

- `standalone/ordered_chiral_homology.tex:7317-7322`: "At k=-h^\vee for V_{-2}(sl_2): kappa=0, ALL monodromy is trivial (eigenvalues -1, +3 are integers)."

Check: with \Omega eigenvalues {+1/2, -3/2}, k \Omega at k=-2 gives {-1, +3}. Integer, matches the quoted text. With \Omega eigenvalues {+1/4, -3/4}, k \Omega at k=-2 gives {-1/2, +3/2}. NOT integer, contradicts the quoted text.

**Critical-level agent (this session's earlier finding).**

> "sl_2 Killing-form Casimir gives \Omega|_Sym^2 = 1/4, \Omega|_Alt^2 = -3/4 (standard Killing normalization); the engine uses 1/2, -3/2, exactly 2x standard — the trace-form convention."

This fingerprints AP312 (three-file divergence: chapter uses Killing normalization; `ordered_chiral_homology.tex` uses trace-form 2x; engines reportedly use trace-form 2x).

**Heal-plan F2.** (i) Add a remark `rem:sl2-casimir-normalization-pinned` to `chapters/examples/yangians_drinfeld_kohno.tex` at line 7586 (directly after the eigenvalue inscription), stating:

> "Throughout Vol I we fix the normalized Killing form with \Omega eigenvalues {+1/4, -3/4} on (triplet, singlet). The trace-form convention with \Omega_tr eigenvalues {+1/2, -3/2} appears in standalone exposition and in the affine r-matrix engine; both are related by \Omega = 2 h^\vee \Omega_tr = 4 \Omega_tr for sl_2 (h^\vee = 2). A k \Omega_tr evaluation at k = -h^\vee = -2 gives {-1, +3}; a k \Omega evaluation at k = -2 gives {-1/2, +3/2}. The 'integer monodromy at critical level' slogan is a trace-form statement and must be flagged."

(ii) In `standalone/ordered_chiral_homology.tex:7321`, replace "(eigenvalues -1, +3 are integers)" with "(eigenvalues of k \Omega_tr on (singlet, triplet) are -1, +3 integers; equivalently k \Omega has eigenvalues -1/2, 3/2 — both conventions give trivial monodromy after the 2\pi i exponential, the 'integer' qualifier refers to the trace-form convention)".

(iii) Same edit at `standalone/genus1_seven_faces.tex:913`, `standalone/survey_modular_koszul_duality_v2.tex:7285`.

(iv) Audit the affine r-matrix engine (`compute/lib/quantum_rmatrix_barcomplex.py` via `yangians_foundations.tex:1221` reference) to confirm whether test values use trace-form or Killing. This was flagged by the critical-level agent but not spot-checked in this pass — recommended follow-up.

## Finding F3 (AP312 cross-file numerical contradiction: dim H^1(sl_2))

The chapter-level inscriptions and the standalone inscriptions disagree on `dim H^1(\bar B(\widehat\fsl_{2,k}))` at generic level.

**Chapter-level (canonical, three sources agree).**

- `chapters/theory/bar_construction.tex:1633`: "widehat{\fsl}_{2,k}: dim H^1 = 3 = dim sl_2."
- `chapters/connections/concordance.tex:5925`: "H^1(\bar B(A)) \cong sl_2 (3-dimensional)."
- `chapters/examples/landscape_census.tex:2265` (Whitehead argument): consistent with dim H^1 = 3 (Whitehead lemma is invoked at sl_2).

**Standalone-level (three sources agree on "4 -> 8").**

- `standalone/ordered_chiral_homology.tex:7322`: "dim H^1 doubles from 4 to 8."
- `standalone/genus1_seven_faces.tex:916`: "dim H^1 jumps from 4 (generic level) to 8 (critical level) for sl_2."
- `standalone/survey_modular_koszul_duality_v2.tex:7286-7287` and `:1329` and `:2859`: "H^1 doubles from 4 to 8 for sl_2."
- `standalone/holographic_datum.tex:718`: "H^1 doubles (from 4 to 8 for sl_2)."

**First-principles check.** At generic non-critical level, the chiral bar H^1 for V_k(g) simple is spanned by the weight-1 primary currents J^a, giving `dim H^1 = dim g`. For sl_2: 3. The "4" in the standalones likely counts {J^+, J^-, J^3, T} where T is the Sugawara stress tensor treated as an additional weight-1 class (which it is not — T has weight 2). The most charitable reading is that "4" counts {J^+, J^-, J^3} plus one additional class arising from the mode structure, but there is no inscribed derivation of "4" in any of the five standalones. The claim "H^1 doubles from 4 to 8" has zero chapter-level backing and disagrees with the Whitehead-derived `dim H^1 = 3` at generic level.

**Predicted correct critical-level jump.** From Frenkel-Teleman (cited in `kac_moody.tex:4417-4421`) and `thm:oper-bar` at `kac_moody.tex:4402-4412`: at k = -h^\vee, `H^n(\bar B(\widehat\fg_{-h^\vee})) \cong \Omega^n(Op_{\fg^\vee}(D))`. For sl_2 (so \fg^\vee = sl_2, oper space is the module of Schwarzian derivatives / projective connections), dim \Omega^1(Op_{sl_2}(D)) is the cotangent module of the oper space which has formal dimension 1 per geometric point — not 8. The genuine critical-level jump is NOT a numerical doubling of a discrete dimension; it is a change of object from a finite-dim g-module to an infinite-dim \Omega^*(Op) algebra. The "4 -> 8" prose in the five standalones is a confabulated numerical shorthand for the qualitative jump described in `kac_moody.tex:4372-4412`.

**Heal-plan F3.** (i) Retract the "4 -> 8 doubling" claim from all five standalones. Replace with a one-sentence qualitative statement:

> "At generic non-critical k, the first bar cohomology is H^1 = sl_2 (3-dim, spanned by the currents, via Whitehead lemma). At critical level k = -h^\vee, the bar cohomology transitions to H^*(B(\widehat\fsl_{2,-2})) \cong \Omega^*(Op_{sl_2}(D)) (Frenkel-Teleman, thm:oper-bar in Vol I kac_moody.tex:4402-4412), an infinite-dimensional algebra of differential forms on the oper space rather than a finite-dim doubling."

Five files: `ordered_chiral_homology.tex:7322`, `genus1_seven_faces.tex:915-917`, `survey_modular_koszul_duality_v2.tex:1329, 2859, 7286-7287`, `holographic_datum.tex:718`.

(ii) CLAUDE.md "Critical level jump" row in Theorem Status table reads "H^1 doubles (4 -> 8)". Correct to: "H^1 transitions from 3-dim currents (generic) to infinite-dim \Omega^1(Op_{sl_2}(D)) (critical, Frenkel-Teleman)." Surgical edit.

(iii) Grep cross-volume: `grep -rn '4.*to.*8\|doubles.*from.*4\|jumps.*from.*4' ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups` to confirm no Vol II / Vol III inherited the "4 -> 8" gloss.

## Spot-checks (r-matrix convention consistency per AP141)

Five r-matrix formulas across Vol I were checked for level-prefix consistency:

| Site | Formula | Convention | k=0 check (trace-form) | Verdict |
|------|---------|-----------|-------------------------|---------|
| landscape_census.tex:378 | `k \Omega_tr / z` | trace-form | r(0) = 0 ✓ | consistent |
| yangians_drinfeld_kohno.tex:6854 | `r_KZ(z) = k \Omega / z` | trace-form (labelled KZ) | r(0) = 0 ✓ | consistent label mismatch — "KZ" here means "KZ-equation context" not "KZ normalization"; honest but confusable |
| yangians_drinfeld_kohno.tex:7579 | `r(z)/kappa = \Omega / (z(k+h^\vee))` | KZ | rewritten, non-zero at k=0 | consistent |
| kac_moody.tex:46-50 | `k \Omega_tr / z` (trace) vs `\Omega/((k+h^\vee)z)` (KZ) both named | both conventions named | both checks passed inline | consistent (this file is the honest convention inscription) |
| bv_brst.tex:2702 | `r^KM(z) = k \Omega / z` | trace-form | r(0) = 0 ✓ | consistent |

Five of five pass AP141 k=0 check. The only label-level issue is the "r_KZ" label at `yangians_drinfeld_kohno.tex:6854` naming the trace-form expression; suggest renaming to `r^{KM-tr}(z)` to avoid future FM1 drift.

## Summary of heal-plan APs (minimal, per AP314)

Inscribing ONE new AP (the AP314 discipline caps at one per wave):

**AP1881 (Tensor identity stated as equation, then absorbed via Sugawara without naming the absorption).** When a programme-wide source states `X = Y` as an equation, but the two sides are tensors of different normalisations (Killing vs trace-form) or rational functions of different algebraic structures (linear-in-k vs `1/(k+h^\vee)`), the equation cannot be a tensor identity. Two healings: (a) name the absorption step (e.g., Sugawara rescaling, Casimir 2h^\vee ladder) that converts one side to the other as flat connections or as r-matrices up to formal-parameter rescaling, or (b) rewrite as separate chunks with a bridge lemma (`lem:casimir-sugawara-absorption`) inscribing the absorption formula explicitly. Canonical violation: `k \Omega_tr = \Omega/(k+h^\vee)` appearing as an equation in `landscape_census.tex:641`, `yangians_foundations.tex:1215`, CLAUDE.md AP-RMATRIX, and cross-volume "Key Constants" without the absorption. Honest source: `appendices/appendix_q_conventions.tex:26` names the Sugawara absorption. Related: AP144 (convention clash), AP312 (cross-file scalar contradiction), AP272 (unstated cross-lemma via folklore citation — here "Sugawara rescaling" is the folklore that closes the gap). Counter: for every bridge identity of the form `scalar_1 \cdot tensor_1 = tensor_2 / rational`, substitute both sides at a concrete k (e.g., k = 1, k = h^\vee) and verify that the RHS is a well-defined rational function not merely a formal parameter rename; if the sides diverge, the equation is a rescaling torsor claim and must name the torsor.

No AP1882-AP1900 used in this wave (AP314 discipline).

## Cache entry

Pattern 226 (first-principles cache, session 2026-04-18). **"Bridge identity `k \Omega_tr = \Omega/(k+h^\vee)` is a rescaling torsor claim, not a tensor identity."** Trigger: CLAUDE.md AP-RMATRIX, landscape_census.tex, or yangians_foundations.tex asserts the bridge as an equation; agent treats both sides as the same tensor and plugs one into a formula derived from the other. Counter: verify k-dependence — LHS scales linearly in k, RHS scales as `1/(k+h^\vee)`; these cannot be the same tensor. Primary source: `appendices/appendix_q_conventions.tex:26` — the two sides are equal only after the Sugawara-absorption rescaling is performed on the formal parameter, which is a torsor action not a tensor identity. Appended to `notes/first_principles_cache_comprehensive.md`.

## Verdict and open items

**Three genuine findings (F1 AP144, F2 AP312 sl_2 Casimir, F3 AP312 dim H^1).** All three are honest cross-file / convention-absorbtion drift detectable by first-principles check:
- F1 by substituting k = 0, 1, 2 into both sides of the bridge identity.
- F2 by computing k \Omega eigenvalues at k = -2 and checking "integer" claim.
- F3 by invoking Whitehead lemma at sl_2 generic level.

**Priority order.** F2 and F3 are load-bearing at the critical-level theorem in CLAUDE.md status table + standalones; they propagate to the reader's understanding of the critical-level jump. F1 is a hygiene fix of the programme's bridge-identity prose. I recommend F3 first (largest numerical discrepancy with strongest first-principles witness), F2 second (scope clarification), F1 last (hygiene).

**Recommended engines / tests to run post-heal.**

- Recompute `compute/lib/quantum_rmatrix_barcomplex.py` test points at k = 0 (must give r = 0 in trace-form), k = -h^\vee (must give the Sugawara-limit formula). Report the sign convention of \Omega used in the engine.
- Add an HZ-IV decorator to any test claiming "sl_2 Casimir eigenvalues" with `verified_against = {chapter_Killing_form, standalone_trace_form_2x, primary_source_EFK98}` and `disjoint_rationale` stating the two conventions are related by \Omega = 2h^\vee \Omega_tr.

**Open: dim H^1 at generic level.** The standalones' "4" has no derivation. Two candidates:
(a) Accounting error (correct value is 3); five standalones carry a typo propagated from one source.
(b) Genuine different object (perhaps `H^1_{cyc,prim}` from `concordance.tex:6032` which counts cyclic-primitive classes, or the weighted-mode H^1 from PBW spectral sequence E_1 page).

Preferred resolution is (a) based on the direct bar computation `H^1 = \bar A^* / (OPE-modes)` and Whitehead vanishing at sl_2. First-principles heal restores 3.

**No HEAL edits were written during this audit.** The agent observed the audit constraint (report-only) and inscribes the heal-plan here for subsequent attack-and-heal follow-through. Next wave: apply the three-file edit for F3 and the one-file edit for F2 in a single commit, then address F1 programme-wide.
