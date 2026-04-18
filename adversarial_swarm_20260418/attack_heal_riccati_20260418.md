# Attack-and-heal: thm:riccati-algebraicity (Virasoro shadow tower)

Author: Raeez Lorgat
Date: 2026-04-18
Target: `chapters/theory/higher_genus_modular_koszul.tex`, `thm:riccati-algebraicity` + upstream `prop:master-equation-from-mc` + downstream closed forms in `chapters/theory/shadow_tower_higher_coefficients.tex`.
AP block reservation: AP1001-AP1020 (sparingly used; see verdict).

## Mission summary

Five lines of attack executed in sequence:

1. Locate `thm:riccati-algebraicity` and verify AP267 heal (r ≥ 5 lower bound, strict j < k, even-r ≥ 6 diagonal separated).
2. Trace upstream to `prop:master-equation-from-mc` and confirm clean derivation from `thm:mc2-bar-intrinsic`; in particular rule out any Wakimoto/SDR fabrication of the AP269 kind.
3. Verify the Σ_Vir(z) closed form `4z³/9 − z²/9 + z/27 − log(1+6z)/162` from the status table.
4. Verify the pole-doubling ansatz `Σ_Vir^{(k)}(z) = [P_k + Q_k log(1+6z)] / (1+6z)^{2k}` at k = 1.
5. Verify the recursion itself against the √Q_L Taylor expansion at rational test data.

Verdict: **NO HEAL REQUIRED**. All five checks pass with zero discrepancies. The AP267 heal (Wave-5, 2026-04-17) is load-bearing and correctly applied.

## 1. Location and AP267 heal audit

CLAUDE.md mission brief cited line 17963; actual `\label{thm:riccati-algebraicity}` is at line 18030 (immediately followed by `\label{thm:shadow-metric-existence}` alias at 18031). The intervening line 17963 sits inside `rem:non-principal-ds-M-class` discussing the Sugawara stress tensor as the quartic-pole generator.

Recursion at lines 18060-18071 reads (verbatim):

```
S_r = -(P/(2r)) sum_{j+k=r+2, 3<=j<=k, j<k} c_{jk} j k S_j S_k
       - (P/(2r)) c_{(r+2)/2,(r+2)/2} ((r+2)/2)^2 S_{(r+2)/2}^2 [r ≡ 0 mod 2, r >= 6]
```

with `c_{jk} = 1` when `j < k` and `c_{jk} = 1/2` when `j = k`.

AP267 compliance:

- Lower bound `r ≥ 5`: explicit in the sentence "the recursion is well-defined starting at r = 5" (line 18078-18079).
- Strict `j < k` in the sum: present (line 18065).
- Even-r ≥ 6 diagonal term separated: the indicator `[r ≡ 0 mod 2, r >= 6]` explicitly gates the diagonal term.

Enumeration of recursion solutions (direct check):

| r | {(j,k) : j+k=r+2, 3 ≤ j < k} | diagonal (r even, r ≥ 6) | total |
|---|------------------------------|---------------------------|-------|
| 4 | ∅ | (would be (3,3) but r < 6) | 0 |
| 5 | {(3,4)} | NA (r odd) | 1 |
| 6 | {(3,5)} | (4,4) with c=1/2 | 2 |
| 7 | {(3,6), (4,5)} | NA (r odd) | 2 |
| 8 | {(3,7),(4,6)} | (5,5) with c=1/2 | 3 |

The r = 4 row has zero recursion solutions, so S_4 is genuinely initial data (the "recursion silently admits S_4 as an output" failure mode of AP267 is absent). The r = 6 row shows the diagonal term (4,4) is non-empty starting at r = 6, not at r = 4, which is exactly what the `[r >= 6]` gate forces.

**AP267 heal verdict: CLEAN.** The recursion lower bounds exactly match the initial-data triple (κ, α, S_4) that the theorem names as structural input.

## 2. Master-equation upstream audit (AP269 check)

`prop:master-equation-from-mc` is at line 13214-13226. Proof (lines 13228-13237):

> The MC equation dΘ + (1/2)[Θ,Θ] = 0 holds in Defcyc^mod(A) by Theorem thm:mc2-bar-intrinsic. Since the differential d and the bracket [-,-] respect the degree filtration, restricting to the degree-r component yields d(Sh_r) + sum_{r_1+r_2=r} [Sh_{r_1}, Sh_{r_2}] = 0, which is exactly ∇_H(Sh_r) + o^(r) = 0.

Three checks:

- Input: `thm:mc2-bar-intrinsic` inscribes the MC equation bar-intrinsically (no SDR, no Wakimoto, no Feigin-Frenkel screening). No AP269 fabrication.
- Mechanism: degree-filtration respecting differential and bracket. Standard; no folklore citation to a deep classical theorem (no AP272).
- Output: `∇_H(Sh_r) + o^(r) = 0` is a direct restriction; no base-change, no six-functor, no AP249.

**Upstream verdict: CLEAN.** The master equation is a structural consequence of the MC equation; the chain to `thm:riccati-algebraicity` is four steps (MC equation → degree-r projection → single-line reduction at j ≥ 3 → convolution identity ⇔ algebraic relation F² = Q_L) and every step is a polynomial / linear-algebra identity, not a citation to external machinery.

## 3. Σ_Vir(z) closed form verification

CLAUDE.md status: `Σ_Vir(z) = 4z³/9 − z²/9 + z/27 − log(1+6z)/162`.

Source inscription: `chapters/theory/shadow_tower_higher_coefficients.tex:814-828` as `thm:shadow-series-closed-form-Virasoro` with `\ClaimStatusProvedHere`.

Proof reduction: from the leading-asymptotic sequence A_r = 8(−6)^(r−4)/r for r ≥ 4, the closed form is derived by summing via the shifted log generating function `sum_{k≥0} u^k/(k+4) = u^{-4}[-log(1-u) - u - u²/2 - u³/3]` and substituting u = −6z.

Independent verification: the predicted coefficient at z^r in the closed form simplifies to

  coef_r(Σ_Vir) = (−6)^r / (162 · r) for r ≥ 4,

because the polynomial part `4z³/9 − z²/9 + z/27` vanishes at r ≥ 4 and the `-log(1+6z)/162` term contributes `(-1)^{r+1}·6^r/r · (-1/162) = (-6)^r/(162 r)` (using log(1+6z) = sum_{n≥1} (-1)^{n+1}·6^n·z^n / n = sum (-(-6)^n)/n · z^n with a sign correction).

Numerical cross-check (Fraction arithmetic, exact):

| r | A_r direct | closed-form coef | match |
|---|------------|-------------------|-------|
| 4 | 2 | 2 | Y |
| 5 | −48/5 | −48/5 | Y |
| 6 | 48 | 48 | Y |
| 7 | −1728/7 | −1728/7 | Y |
| 8 | 1296 | 1296 | Y |
| 9 | −6912 | −6912 | Y |

Identity check: `8/((−6)^4) = 8/1296 = 1/162`, so `8(−6)^(r−4)/r = (−6)^r/(162 r)` ✓.

**Closed-form verdict: VERIFIED** through r = 9 at exact rational arithmetic (ratio of two Python Fraction objects per row, bit-exact).

## 4. Pole-doubling at k = 1

CLAUDE.md status: `Σ_Vir^(k)(z) = [P_k + Q_k log(1+6z)] / (1+6z)^{2k}`.

At k = 1, source inscription is `thm:shadow-series-closed-form-Virasoro-subleading` at `shadow_tower_higher_coefficients.tex:871-889`:

  Σ_Vir^(1)(z) = 16z^5/(1+6z)² + (20/9)z^4/(1+6z)² − (992/405)z³ + (248/405)z² − (248/1215)z + (124/3645) log(1+6z)

Pole-doubling pattern: the rational-function terms all carry denominator `(1+6z)^{2·1} = (1+6z)²`, and there is one log term. The polynomial terms (−992/405·z³, 248/405·z², −248/1215·z) can be absorbed into the P_k numerator by clearing the (1+6z)² denominator, since (1+6z)² is a unit in Q[z] at finite Taylor order.

Independent verification by direct Taylor-expansion arithmetic (no sympy):

- Expand `1/(1+6z)² = sum_{n≥0} (n+1)(−6)^n z^n`.
- Expand `log(1+6z) = sum_{n≥1} −(−6)^n/n · z^n`.
- Combine per the closed form with rational coefficients.
- Compare against `B_r = −(4/45)·(−6)^(r−4)·(5r²−45r+496)/r`.

| r | closed-form Taylor coef | direct B_r | match |
|---|--------------------------|------------|-------|
| 4 | −44/5 | −44/5 | Y |
| 5 | 1056/25 | 1056/25 | Y |
| 6 | −3248/15 | −3248/15 | Y |
| 7 | 40896/35 | 40896/35 | Y |
| 8 | −32832/5 | −32832/5 | Y |
| 9 | 190464/5 | 190464/5 | Y |

**Pole-doubling verdict at k = 1: VERIFIED.** The P_1 + Q_1·log(1+6z) over (1+6z)² structure is consistent with the published subleading generating function; six coefficients match at exact rational arithmetic.

Status of higher k: CLAUDE.md status row asserts the pattern "for all k". This audit verifies k = 1 only; the k ≥ 2 claim relies on the subleading recursion architecture in `shadow_tower_higher_coefficients.tex` and was not independently re-derived here (out of mission scope; the mission asked for k = 1 verification).

## 5. Riccati recursion vs sqrt(Q_L) Taylor consistency

Setup: take rational test data κ = 1, α = 1, S_4 = 1, so

  Q_L(t) = 4 + 12t + 25t²,  F(t) = √Q_L(t),  F(t) = sum_{n≥0} a_n t^n with S_{n+2} = a_n/(n+2).

Compute a_n via quadratic recursion from F² = Q_L (m ≥ 3 forces sum_{i+j=m} a_i a_j = 0):

  a_0 = 2, a_1 = 3, a_2 = 4, a_3 = −6, a_4 = 5, a_5 = 9/2, a_6 = −103/4, a_7 = 357/8, a_8 = −131/16, a_9 = −5295/32.

Independently compute S_r via the Riccati recursion at r = 5, 6, 7, 8, 9 with P = 1/κ = 1:

| r | S_r from F² = Q_L | S_r from Riccati recursion | match |
|---|---------------------|----------------------------|-------|
| 5 | −6/5 | −6/5 | Y |
| 6 | 5/6 | 5/6 | Y |
| 7 | 9/14 | 9/14 | Y |
| 8 | −103/32 | −103/32 | Y |
| 9 | 119/24 | 119/24 | Y |

In particular:

- r = 6 exercises the even-r diagonal term (4,4) with c = 1/2.
- r = 8 exercises both the off-diagonal sum ((3,7), (4,6)) and the diagonal (5,5).
- r = 5, 7, 9 are pure off-diagonal checks.

**Recursion consistency verdict: VERIFIED.** Five non-trivial checks with at least one exercising the diagonal-separated path.

## Scope and residual

Cleanly verified in this audit:

- AP267 recursion-bound heal: correct.
- `prop:master-equation-from-mc` upstream: clean, no AP269 fabrication.
- Σ_Vir(z) leading closed form: exact through r = 9.
- Σ_Vir^(1)(z) subleading closed form: exact through r = 9; pole-doubling k = 1 pattern confirmed.
- Riccati recursion ⇔ F² = Q_L algebraic relation: exact at rational test data through r = 9 (including diagonal term).

Not re-derived in this audit (acknowledged, out of mission scope):

- Pole-doubling at k ≥ 2. Status table asserts `Σ_Vir^(k)(z) = [P_k + Q_k log(1+6z)]/(1+6z)^{2k}` "all k"; k ≥ 2 uses the tail-integration architecture in `shadow_tower_higher_coefficients.tex` which builds Σ^(k) iteratively; recursive verification possible but not executed here.
- Sharp universality on class M beyond Virasoro. `thm:universal-class-M-C-is-6` carries hypothesis (1) S_3(A, T) = 2 (universal T-T OPE) and hypothesis (2) subleading suppression of non-T lines; the Wave-3 audit (`adversarial_swarm_20260417/wave3_koszul_shadow_attack_heal.md`) already certified these hypotheses.
- Class M non-Virasoro (logarithmic W(p), BP, non-principal W). `rem:C-A-scope-E-infinity` restricts scope to E_∞-chiral; E_1-chiral (Yangian etc.) shadow-exponential base is open (self-declared frontier). Out of mission scope.

## AP block utilisation

Zero new APs inscribed this wave. Every attacked object passes at its inscribed scope; the AP267 heal is sufficient, the master-equation derivation is clean, the closed forms are exact, and the recursion is internally consistent. AP1001-AP1020 block returned unused.

This follows AP314 discipline (inscription-rate outpaces audit capacity): when the audit surfaces no new failure mode, the correct output is a verification report, not a catalogue addition.

## Cross-volume propagation check (AP5)

Grep hits for Σ_Vir closed form:

- `chapters/theory/shadow_tower_higher_coefficients.tex:814`: canonical.
- `standalone/shadow_towers.tex`, `standalone/shadow_towers_v2.tex`, `standalone/shadow_towers_v3.tex`: standalone copies; cross-volume consumers of C_Vir = 6.
- `chapters/frame/programme_overview_platonic.tex:243-244`: cites `thm:shadow-exponential-base-Virasoro` and `thm:universal-class-M-C-is-6`.
- `chapters/examples/w3_holographic_datum.tex`, `w3_composite_fields.tex`, `w_algebras.tex`: downstream W_N consumers.

All consumer references resolve at build time (grep-verified labels present); no AP149 resolution-propagation failure detected for this audit target.

## No commits

Per CLAUDE.md session protocol: this audit report is a working-note under `adversarial_swarm_20260418/`, not a git commit. The user has not requested a commit; no commit is created.
