# Attack-and-heal: ChirHoch^1 KM total-dim formula (Wave of 2026-04-18)

Target: CLAUDE.md row "ChirHoch^1 KM"; Vol I `chapters/theory/chiral_center_theorem.tex:1965-2294` (`prop:derived-center-explicit`, `prop:chirhoch1-affine-km`, `prop:chirhoch2-affine-km-general`, `rem:sl2-chirhoch-dim5`).

Date: 2026-04-18. Follow-up to Wave-4 (`wave4_chirhoch_1_km_attack_heal.md` 2026-04-18 earlier). Auditor channel: Etingof / Kazhdan / Gelfand / Drinfeld / Beilinson / Feigin / Frenkel / Arakawa.

AP block used: AP701-AP720.

## Prompt framing

The attack was commissioned against the conjectured total-dim formula `dim ChirHoch^*(V_k(g)) = dim(g) + 2`. Two candidate rank-dependencies were put forward by the commissioner:

- Candidate A: `dim(g) + 2` (what the inscribed proof gives: 1 + dim(g) + 1 at sl_2 = 5, sl_3 = 10, sl_4 = 17, E_8 = 250).
- Candidate B: `rank(g) + dim(g) + 1` (if the rank-1 ChirHoch^2 = 1 witness scales as rank(g), giving sl_2 = 5, sl_3 = 11, sl_4 = 18, E_8 = 257).

These two formulas COINCIDE AT sl_2 (both give 5) and DIVERGE FROM sl_3 onward. The coincidence masks which formula is correct; primary-source inspection is required.

## Primary-source state at audit time

`chiral_center_theorem.tex:2221-2277` already inscribes `prop:chirhoch2-affine-km-general` with `\ClaimStatusProvedHere`:

```
ChirHoch^2(V_k(g)) = C,        dim ChirHoch^*(V_k(g)) = dim(g) + 2
```

This proposition was installed by Wave-4 (documented `wave4_chirhoch_1_km_attack_heal.md`). Its proof routes through:

1. General Koszul-duality identification `dim ChirHoch^2(A) = dim Z(A^!)` (inscribed in `chiral_hochschild_koszul.tex:1791` as part of the palindromic clause of `thm:main-koszul-hoch`, itself `\ClaimStatusProvedHere`).
2. Feigin-Frenkel Koszul-dual level assignment `V_k(g)^! = V_{-k - 2h^v}(g)`.
3. Non-critical-dual-level center collapse: `Z(V_{-k - 2h^v}(g)) = C \cdot |0\rangle` at generic `k` (the Feigin-Frenkel center acquires polynomial-on-rank(g) structure ONLY at the critical level `k = -h^v`; off critical it reduces to scalars). Cited from Feigin-Frenkel 1992, and inline in `prop:derived-center-explicit(ii)` lines 2092-2096.
4. Theorem H polynomial concentration `ChirHoch^{>=3} = 0` (`thm:hochschild-polynomial-growth`, `\ClaimStatusProvedHere`).

Therefore:

- ChirHoch^0(V_k(g)) = C (vacuum, rank-independent, non-critical level)
- ChirHoch^1(V_k(g)) = g (rank-scaling, `prop:chirhoch1-affine-km`)
- ChirHoch^2(V_k(g)) = C (via Koszul-dual center collapse, rank-INDEPENDENT)
- ChirHoch^{>=3}(V_k(g)) = 0 (Theorem H)

Total: `1 + dim(g) + 1 = dim(g) + 2`. This is Candidate A, inscribed and `\ClaimStatusProvedHere`.

## Adversarial attacks and their verdicts

Attack AP701 (Candidate B advocacy via rank-parallelism).
"ChirHoch^0 at generic level is C only because sl_2 has 1-dim Sugawara center; for higher rank g the classical Casimir lattice of rank(g) might lift to rank(g)-dim ChirHoch^0."
Verdict: REJECTED. The Sugawara construction produces the CONFORMAL vector T (the quadratic Casimir) as an INTERIOR element of V_k(g) at non-critical level; higher Casimirs (cubic, quartic, ...) of a higher-rank g similarly give INTERIOR central elements, NOT new independent ChirHoch^0 classes. The center of V_k(g) at non-critical k is C*|0> (Kac 1998 Thm 4.10; equivalently, Kac-Shapovalov determinant nonvanishing off critical level). ChirHoch^0 = Z(V_k(g)) = C for all simple g at generic k. Rank-independence confirmed.

Attack AP702 (ChirHoch^2 rank-scaling via Feigin-Frenkel center rank(g)-generators).
"At critical level the Feigin-Frenkel center has rank(g) polynomial generators. At generic DUAL level the Koszul-dual center might inherit rank(g) generators."
Verdict: REJECTED. The Feigin-Frenkel polynomial-on-rank(g) structure is a CRITICAL-LEVEL phenomenon; the dual level of generic k is `-k - 2h^v`, which is ALSO generic (non-critical) whenever k is generic. Specifically `-k - 2h^v = -h^v` iff `k = -h^v`, so the critical locus is fixed under the Feigin-Frenkel involution. Off critical, `Z(V_{-k-2h^v}(g)) = C \cdot |0\rangle` (Kac 1998 Thm 4.10 applied to dual level). This gives ChirHoch^2 = C universally at generic k, rank-independent.

Attack AP703 (Koszul-dual level miscalibration).
"The dual level might be `-k - h^v` (not `-k - 2h^v`), in which case different resonance structure."
Verdict: REJECTED. Kac-Moody complementarity involution is `k <-> -k - 2h^v`, fixing `k = -h^v` (the Feigin-Frenkel self-dual point = critical level). This is standard (FF92 §3, reproduced in Arakawa 2007 §4). `prop:chirhoch2-affine-km-general` proof at :2242-2247 correctly writes `-k - 2h^v` and invokes the involution. No miscalibration.

Attack AP704 (dim ChirHoch^2 = dim Z(A^!) identity scope inflation).
"The general Koszul-duality identification `dim ChirHoch^2(A) = dim Z(A^!)` might fail for non-quadratic cubic-OPE algebras."
Verdict: OUT OF SCOPE. V_k(g) is quadratic (all OPE poles <= 2). The identification holds on the quadratic-Koszul locus, which contains V_k(g) (via `cor:universal-koszul`). No scope inflation for the affine Kac-Moody case.

Attack AP705 (AP250 algorithm uniformity across simple types).
"ChirHoch^2 = 1-dim might be A-type only; non-simply-laced exceptional G_2, F_4 might fail."
Verdict: REJECTED. The proof uses only (a) quadratic OPE, (b) Sugawara non-degeneracy at non-critical level, (c) Kac-Shapovalov determinant nonvanishing at generic level. All three properties are UNIFORM across simple Lie algebra types (A, B, C, D, E, F, G) by Kac 1998. Non-simply-laced exceptionals are covered. AP250 clear.

Attack AP706 (CLAUDE.md status row stale).
"CLAUDE.md row 'ChirHoch^1 KM' says 'Total dim = dim(g)+2 inscribed ONLY for sl_2' and 'General simple g case OPEN pending ChirHoch^2(V_k(g)) computation beyond rank 1'."
Verdict: CONFIRMED (AP271 reverse drift). The inscription exists at `chiral_center_theorem.tex:2221-2277` with `\ClaimStatusProvedHere`. CLAUDE.md lags behind the manuscript. Heal required: update the status row to match the inscribed state.

Attack AP707 (total-dim formula `dim(g) + 2` vs `rank(g) + dim(g) + 1` disambiguation at sl_3).
"If the formula is dim(g)+2, sl_3 total = 10. If rank(g)+dim(g)+1, sl_3 total = 11."
Verdict: DISAMBIGUATED. The inscribed proof gives `dim(g) + 2` with ChirHoch^0 = C (rank-INDEPENDENT) and ChirHoch^2 = C (rank-INDEPENDENT). At sl_3: 1 + 8 + 1 = 10. The commissioner's candidate `rank(g) + dim(g) + 1` would require ChirHoch^0 to scale with rank(g), which is FALSE (Attack AP701).

Attack AP708 (engine-test coverage for sl_3, sl_4 non-existent).
"`compute/lib/chirhoch_sl_n_outer_derivations_engine.py` computes ChirHoch^1 = N^2 - 1 for sl_N, N <= 8. No engine verifies ChirHoch^2 = 1 for sl_3, sl_4, etc."
Verdict: CONFIRMED. HZ-IV gap. The `rem:chirhoch2-affine-km-general-falsification` at :2279-2294 explicitly lists this engine extension as the "triangulation path, not a closure condition". The per-family numerical witness is recommended follow-up work; the proof stands on general Koszul-duality machinery (Attacks AP702-AP704 all refused to produce a counterexample).

Attack AP709 (critical-level degeneracy).
"At k = -h^v the formula may break because ChirHoch^0 becomes the Feigin-Frenkel center (infinite-dimensional)."
Verdict: SCOPE-RESTRICTED. The proposition is stated at generic level `k != -h^v`, and this restriction is correctly inscribed. At critical level the formula is expected to fail; this is explicitly noted in `prop:derived-center-explicit(ii)` lines 2092-2096 and also in the critical-level row of the CLAUDE.md theorem status. No issue.

Attack AP710 (circular-proof-chain via `cor:universal-koszul`).
"The proof of `prop:chirhoch2-affine-km-general` uses `cor:universal-koszul`; does that corollary itself depend on ChirHoch^* computations, which would be circular?"
Verdict: REJECTED. `cor:universal-koszul` proves quadratic OPE => chirally Koszul via the chiral Orlik-Solomon/Shelton-Yuzvinsky route (`chiral_koszul_pairs.tex`), NOT through ChirHoch^*. No circularity.

## Surviving core

At generic level `k != -h^v` for any simple Lie algebra g:

- ChirHoch^0(V_k(g)) = C (center = vacuum line off critical level).
- ChirHoch^1(V_k(g)) = g (as a g-module; outer derivations of the current algebra).
- ChirHoch^2(V_k(g)) = C (via Koszul-dual center collapse; the Feigin-Frenkel dual level is ALSO non-critical, where the center is scalar only).
- ChirHoch^{>=3}(V_k(g)) = 0 (Theorem H polynomial concentration, `thm:hochschild-polynomial-growth`).

Total dimension: `dim ChirHoch^*(V_k(g)) = 1 + dim(g) + 1 = dim(g) + 2`.

Numerical predictions at generic k: sl_2 total = 5; sl_3 total = 10; sl_4 total = 17; sl_N total = N^2 + 1; E_6 total = 80; E_7 total = 135; E_8 total = 250; F_4 total = 54; G_2 total = 16. The `rank(g) + dim(g) + 1` candidate (which gives 11 at sl_3) is REFUTED: the ChirHoch^0 slot is rank-INDEPENDENT and equals 1 universally.

The sole remaining load-bearing input left uninscribed in Vol I is the numerical witness for ChirHoch^2 = 1 at specific non-sl_2 families via Kac-Shapovalov determinant nonvanishing at `-k - 2h^v`. The inscribed proof cites this standardly from Kac 1998 + Feigin-Frenkel 1992. Engine extension to sl_3, sl_4 at small integer k is recommended for HZ-IV triangulation but is NOT a closure condition.

## Heal (per finding)

H1 (addresses AP706 AP271-reverse-drift). Rewrite the CLAUDE.md "ChirHoch^1 KM" status row to match the inscribed state. Replace:

> **PROVED degree-1 at generic k for general simple g; total-dim formula sl_2 only** | Total dim = dim(g)+2 inscribed ONLY for sl_2 (1+3+1=5) via rem:sl2-chirhoch-dim5 (line 2199-2215) routing through prop:derived-center-explicit(ii) (line 1996-2021), which proves ChirHoch^2(V_k(sl_2)) = 1-dim in rank 1 only. General simple g case OPEN pending ChirHoch^2(V_k(g)) computation beyond rank 1.

with:

> **PROVED at generic k for general simple g: ChirHoch^1(V_k(g)) = g and dim ChirHoch^*(V_k(g)) = dim(g) + 2** | `prop:chirhoch1-affine-km` (:2132) + `prop:chirhoch2-affine-km-general` (:2221, `\ClaimStatusProvedHere`) give ChirHoch^0 = C, ChirHoch^1 = g, ChirHoch^2 = C universally at non-critical level via Koszul-dual center identification (`dim ChirHoch^2(A) = dim Z(A^!)` inscribed in `thm:main-koszul-hoch` at `chiral_hochschild_koszul.tex:1791`). Predictions: sl_2 total 5, sl_3 total 10, sl_N total N^2+1, E_8 total 250. HZ-IV triangulation via engine extension to sl_3, sl_4 at small integer k (Kac-Shapovalov determinant nonvanishing at dual level `-k - 2h^v`) is recommended follow-up; the proof stands on general Koszul-duality machinery.

H2 (addresses AP708 HZ-IV engine-coverage gap). Recommended follow-up: extend `compute/lib/chirhoch_sl_n_outer_derivations_engine.py` (or create `compute/lib/chirhoch2_affine_km_engine.py`) to compute `dim Z(V_{-k - 2h^v}(sl_N))` via Kac-Shapovalov determinant at N = 3, 4 and k = 1, 2, 3. Expected: 1 in all cases. This is a TRIANGULATION of the inscribed proof, not a closure condition; the proof stands on FF92 + Kac 1998. Not executed this wave.

H3 (addresses AP706 cross-volume propagation). Grep Vol II + Vol III for stale "total dim ChirHoch = dim(g)+2 only for sl_2" phrasing. No instances found in Vol II via a prior sweep; Vol III does not carry the formula outside cross-volume pointers. No further propagation required.

Status:
- H1 CLAUDE.md row update: applied this wave.
- H2 engine extension: recommended follow-up; not executed.
- H3 cross-volume propagation: no hits; no action.

No `.tex` change to `chiral_center_theorem.tex` this wave (the inscription is already in place from Wave-4); only the CLAUDE.md row is rewritten.

## Commit plan

This wave does NOT create a git commit (the user has not asked for one). Changes are confined to:
- `CLAUDE.md` row rewrite (H1).
- `adversarial_swarm_20260418/attack_heal_chirhoch1_20260418.md` new note (this file).

No manuscript changes, no engine changes. The inscribed `prop:chirhoch2-affine-km-general` and its proof in `chiral_center_theorem.tex:2221-2277` were checked against the primary Koszul-duality identity at `chiral_hochschild_koszul.tex:1791` and the Feigin-Frenkel non-critical-level center-collapse from `prop:derived-center-explicit(ii):2092-2096`; both dependencies are `\ClaimStatusProvedHere` and non-circular (Attack AP710 verdict).

## Patch file

Per AP316, a textual patch file recording the CLAUDE.md row rewrite is emitted alongside this note at `adversarial_swarm_20260418/patch_chirhoch1_claudemd_20260418.patch`.

## Constraints enforcement

- No AI attribution anywhere.
- No em-dashes (using colons, semicolons, separate sentences).
- HZ-1 through HZ-11 respected: no r-matrix written (HZ-1 N/A), no environment-tag drift (HZ-2 N/A), no uniform-weight tag needed (HZ-3 N/A), no kappa formula from memory (HZ-4 N/A), no label created (HZ-5 N/A), no hardcoded test expected values (HZ-6 N/A), no bare kappa in Vol III (HZ-7 N/A), no proof after conjecture (HZ-8 N/A), no four-functor discipline violation (HZ-9 N/A), no AI-slop tokens (HZ-10 respected; post-write grep on this note finds zero banned tokens), no cross-volume ProvedHere discipline issue (HZ-11: the inscribed proposition is in Vol I and cites only Vol I dependencies).
