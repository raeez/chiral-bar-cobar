# Wave-5 Programme Climax Attack-Heal (2026-04-17)

## Target
Vol II Part VI `thm:programme-climax` + `thm:universal-holography-master`
(`chapters/connections/programme_climax_platonic.tex`, 1120 lines);
companion `chapters/theory/logarithmic_wp_tempered_analysis_platonic.tex`
(1047 lines).

## Phase 1 — Attack findings

### (i) Programme-climax literal scope
The theorem statement at line 186-222 is already SCOPE-QUALIFIED to the
"non-logarithmic standard landscape (Virasoro, W_N for any N, Schellekens
c=24 holomorphic, Monster V♮, or irrational coset Com(B,C))" with W(p)
EXPLICITLY EXCLUDED ("the logarithmic W(p) triplet is excluded at the
current scope") and cross-referenced to `rem:wp-tempering-status` and
`conj:f1-wp-tempering`. The Wave-1 audit verdict is already inscribed.
No structural scope repair needed on the theorem statement itself.

### (ii) C₂-cofinite standard landscape enumeration
Line 96-107: Virasoro Vir_c (c≠0 generic), W_{N,c} principal (N≥2
generic c), Schellekens 71 holomorphic c=24, Monster V♮, irrational cosets
Com(H_k, V_k(sl_2)) in VSKR+BGG locus. W(p) excluded via F1. Singlet M(p)
folded into Virasoro sub-channel handling. Enumeration is complete and
matches the audit scope.

### (iii) Emptiness of non-tempered stratum
- Virasoro: `thm:tempered-stratum-contains-virasoro` UNCONDITIONAL ✓
- W_N principal: `thm:wn-tempered-all-N` UNCONDITIONAL via β-independent
  Stirling dominance (β_N-value is irrelevant to tempering). ✓
- Schellekens 71 + Monster: closed via Kapustin-Saulina DW vanishing
  (`thm:schellekens-71-all-alpha-zero`, `prop:monster-alpha-explicit-zero`).
  Gauge pillar, not shadow-tower pillar; out of Wave-5 scope.
- Irrational cosets: `thm:irrational-coset-tempered` via parafermion
  reduction.
- W(p): CONJECTURAL, correctly `\ClaimStatusConjectured` as F1.

### (iv) Orlik-Solomon H^• = H^•_reg ⊕ H^•_log decomposition
Companion chapter lines 582-610. The decomposition is introduced via:
- H^•_reg = polynomial dlog-residue classes (carry the S_r structure
  constants).
- H^•_log = logarithmic Gurarie-Flohr sector (carries (log z_{ij})^n
  growth, annihilated by the Arnold/OS residue).
- The two sectors are orthogonal under the Arnold/OS pairing.

This decomposition is NOT independently stated as a theorem in Vol II;
it is presented as a remark `rem:correlation-vs-shadow-massey`. For
Beilinson hygiene this is adequate because it is derivative of the
Orlik-Solomon algebra structure on FM_r(C) (classical, Arnold 1969 +
Orlik-Solomon 1980); no downstream theorem relies on it as a primitive
inscription.

### (v) Shadow-tower Massey vs correlation-function Massey (Wave-4 split)
Sharp split is correctly inscribed in `rem:correlation-vs-shadow-massey`
(lines 536-610 of W(p) chapter). Claim (a) correlation Massey boundedness
on H^•_log FALSIFIED by Gurarie-Flohr (closed negative). Claim (b) shadow
Massey boundedness on H^•_reg OPEN = `conj:tempered-stratum-contains-wp`.
The conjecture's status is correctly `\ClaimStatusConjectured` at
line 619. NOT falsified by Gurarie-Flohr per explicit sharp split at
lines 607-610.

### (vi) Propagation — THREE PROBLEMS IDENTIFIED

**P1.** `cor:wp-dichotomy-healed` (lines 802-829, companion chapter) is
tagged `\ClaimStatusProvedHere` but its bullet at line 819-820 cites W(p)
tempering VIA `Conjecture~\ref{conj:tempered-stratum-contains-wp}`.
PROVING an emptiness claim via a disjunct that is conjectural is an
AP40/AP4 violation — the proved conclusion cannot exceed the conjunction
of the proved conjuncts. Status must downgrade to a SCOPE-QUALIFIED
variant: the non-tempered stratum is empty on the NON-LOGARITHMIC
C₂-cofinite landscape unconditionally, and empty on the FULL C₂-cofinite
landscape CONDITIONAL on `conj:tempered-stratum-contains-wp`.

**P2.** `thm:programme-climax` proof (line 367-370) uses
`β_{W_N} = (N+1)(N+2)/2 by Fateev-Lukyanov`, but `cor:rung-w-N` proof
(line 631) uses `β_N = 12(H_N-1) = Σ_{s=2}^N 12/s` via
`thm:beta-N-closed-form-proved-all-N`, and `rem:beta-A-W3-wline-
integer-sequence` (line 319-320) RETRACTS `β_N = (N+1)(N+2)/2`. The same
chapter asserts BOTH forms in separate places. This is an internal
inconsistency. For Wave-5 surgical heal: the `thm:programme-climax`
proof line must be updated to the proved closed form `β_N = 12(H_N-1)`.
For N=3: 12(1+1/2+1/3 - 1) = 12·5/6 = 10 ✓ (matches β_3=10 used at
line 311); for N=2: 12(1/2) = 6 ✓. Both β-values are consistent with
the single closed form.

**P3.** `rem:evidence-for-tempering-criterion` (line 885-903 of W(p)
chapter) asserts W(p) tempered via "the present chapter" without
flagging the conjectural status that the reader encounters at
Conjecture 618. Propagation needs a status qualifier.

### (vii) Physical interpretation
Line 1077-1090: the physical reading is "every three-dimensional quantum
theory with a holomorphic-topological twist, a boundary vertex algebra,
and a conformal vector at non-critical level admits a canonical
derived-centre description at the level of its factorisation
observables." The non-tempered-EMPTY claim translates to: no
C₂-cofinite non-logarithmic chiral boundary admits a non-unitary
gravitational dual; class M* logarithmic W(p) is OPEN as to whether its
putative 3d HT dual is unitary. Costello-Gaiotto-Witten register:
iterated-Sugawara ladder ending at E_∞ is the spin-tower gauge invariance
of the boundary at non-critical level. No scope-inflation to falsify.

## Phase 2 — Heal

### H1. Downgrade `cor:wp-dichotomy-healed` status + scope
Add "unconditional on non-logarithmic C₂-cofinite; conditional on F1
for W(p)/M(p) bullets." Status downgraded to scope-qualified. Bullet
tags updated.

### H2. Fix β_N inconsistency in `thm:programme-climax` proof
Update line 367-370 `β_{W_N}` formula from `(N+1)(N+2)/2` to the proved
closed form `12(H_N - 1)` with a single-line cross-reference to
`thm:beta-N-closed-form-proved-all-N`.

### H3. Status qualifier on `rem:evidence-for-tempering-criterion`
Clarify that item (c) W(p) tempering is CONJECTURAL not proved, while
all other items are proved. Preserves the "universal tempering" framing
but honestly scopes.

### H4. No CLAUDE.md atomic updates required
The HOT ZONE HZ-5 label-discipline check: all label prefixes correct,
all statuses correctly downgraded or conjectured. No AP/HZ tokens in
typeset prose (verified by inspection — both files use `%` comments
only for scaffolding).

## Phase 3 — Surgical edits (three)

1. `programme_climax_platonic.tex` line 369-370:
   replace `(N+1)(N+2)/2` with `12(H_N - 1) = \sum_{s=2}^{N} 12/s` with
   cross-reference to `thm:beta-N-closed-form-proved-all-N`.

2. `logarithmic_wp_tempered_analysis_platonic.tex` `cor:wp-dichotomy-
   healed` (lines 802-829): downgrade title to "non-logarithmic
   C₂-cofinite landscape unconditional; full landscape conditional on
   conj:tempered-stratum-contains-wp"; restructure the bullet list;
   status tag split between bullets.

3. `logarithmic_wp_tempered_analysis_platonic.tex`
   `rem:evidence-for-tempering-criterion` (lines 885-903): insert explicit
   status qualifier that item (c) is CONJECTURAL.

## Test verification
Existing tests:
- `compute/tests/test_tempered_stratum.py` — Virasoro tempering.
- `compute/tests/test_wn_tempered_closure.py` — W_N β-independent
  Stirling dominance.
- `compute/tests/test_logarithmic_wp_tempered.py` — W(p) three-channel
  decomposition; Gurarie-Flohr orthogonality.
No new tests needed for this heal (status downgrade only).

## Constitutional hygiene
No AP/HZ tokens in typeset prose. No em-dashes introduced. No em-dash
(---) inserted. No AI-slop tokens.
