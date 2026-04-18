# Wave-12 Triage: Vol II shadow-tower companion labels + HZ-11 audit of lem:leading-coefficient-ratio-identity

Date: 2026-04-18
Parent: Wave-11 Vol II shadow-tower AP241 heal (commit a76e859e) residual items 1-2.
Scope: `vol2/chapters/theory/tempered_stratum_characterization_platonic.tex` consumers at lines 263-265, 515, 1103; HZ-11 audit of `lem:leading-coefficient-ratio-identity` at lines 176-212.
Discipline gates: PE-7, PE-8, AP4, AP40, AP241, AP255, AP286, AP287.

## 1. Companion-label classification (3 items)

Three-step phantom detector applied per Wave-7 method (grep `\label{...}` across Vol I + Vol II + Vol III `.tex`; multi-line env scan at each hit).

| Label | Vol I hits | Vol II hits | Vol III hits | Class | Canonical home |
|---|---|---|---|---|---|
| `thm:shadow-tower-tier-4-closed-form` | 1 (inscribed) | 0 | 0 | Cross-volume consumer ref (NOT phantom) | `chapters/theory/shadow_tower_higher_coefficients.tex:3408` (theorem body, ClaimStatusProvedHere) |
| `thm:shadow-tower-subleading-closed-form` | 1 (inscribed) | 0 | 0 | Cross-volume consumer ref (NOT phantom) | `chapters/theory/shadow_tower_higher_coefficients.tex:3032` (theorem body, ClaimStatusProvedHere) |
| `thm:shadow-tower-sub-subleading-closed-form` | **2 (AP124 internal Vol I dup; out of scope)** | 0 | 0 | Cross-volume consumer ref (NOT phantom) | Primary: `shadow_tower_higher_coefficients.tex:3215`; secondary: `shadow_tower_sub_subleading_platonic.tex:247` |

All three labels are GENUINELY INSCRIBED in Vol I. The Vol II `tempered_stratum_characterization_platonic.tex` references were bare `\ref{thm:...}` without V1- prefix or phantomsection alias, so they resolved as `[?]` at Vol II build — a consumer-side phantom symptom, not a source-side phantom.

Classification: Class A (self-disabled/inscribed-elsewhere, needs V1- phantom retarget per Wave-11 pattern; AP242-adjacent but not AP242 since labels exist in the programme).

## 2. Canonical target identification

Vol I `shadow_tower_higher_coefficients.tex` inscribes the full subleading-tier ladder under the "wave-13 closed-form" programme:
- Leading (A_r): `V1-thm:shadow-tower-asymptotic-closed-form` (already phantom-aliased in Vol II `main.tex:652`, canonical Vol I hit at lines ~1137-1183).
- Subleading (B_r): `thm:shadow-tower-subleading-closed-form` at `:3032`.
- Sub-subleading (Gamma_r): `thm:shadow-tower-sub-subleading-closed-form` at `:3215`.
- Tier-4 (Delta_r): `thm:shadow-tower-tier-4-closed-form` at `:3408`.

The four theorems form a coherent Laurent stratification of Phi_r(c) = c^{r-2} S_r(Vir_c) = A_r + B_r/c + Gamma_r/c^2 + Delta_r/c^3 + O(c^{-4}). The Vol II tempered-characterisation proof consumes all four simultaneously at Step 2 (subleading tiers, uniformly), line 262-266.

## 3. Atomic heals applied (Wave-11 V1-* phantom pattern)

PE-7/PE-8 templates filled prior to each edit (all `verdict: ACCEPT`; full templates in session reply).

Edits (4 atomic; 0 commits):

1. `vol2/main.tex:652` — inserted three `\phantomsection\label{V1-thm:...}` aliases alphabetically adjacent to the existing `V1-thm:shadow-tower-asymptotic-closed-form` anchor:
   - `V1-thm:shadow-tower-tier-4-closed-form`
   - `V1-thm:shadow-tower-subleading-closed-form`
   - `V1-thm:shadow-tower-sub-subleading-closed-form`

2. `tempered_stratum_characterization_platonic.tex:263-265` — three bare `\ref{thm:...}` retargeted to `\ref{V1-thm:...}` in the Step-2 proof-body list.

3. `tempered_stratum_characterization_platonic.tex:515` — parenthetical `(cf.\ \ref{thm:shadow-tower-tier-4-closed-form})` retargeted to `V1-`.

4. `tempered_stratum_characterization_platonic.tex:1103` — cross-link `\texttt{thm:shadow-tower-tier-4-closed-form}` retargeted to `\texttt{V1-thm:shadow-tower-tier-4-closed-form}`.

Post-heal grep: zero `\ref{thm:shadow-tower-(tier-4|subleading|sub-subleading)-closed-form}` occurrences in Vol II; all four tier references now route through the V1-* phantomsection block.

This is a Wave-11 HZ-11 RETARGET (cross-volume content genuinely inscribed in target volume, phantomsection aliases the name into the consumer volume). Not AP286 tactical alias: the aliased Vol I theorems are first-class inscribed objects with load-bearing proof bodies; the consumer prose treats them as the Vol I theorems they are, not as umbrella names.

## 4. HZ-11 audit: `lem:leading-coefficient-ratio-identity` (lines 176-212)

Read: statement at lines 176-196; proof at lines 198-212.

### Proof anatomy

- **Input datum** (cited): `Theorem~\ref{V1-thm:shadow-tower-asymptotic-closed-form}` (Vol I shadow_tower_higher_coefficients.tex, lines 1137-1183) supplies the closed form `A_r = 8 (-6)^{r-4} / r`.
- **Local computation**: divide `A_{r+1} / A_r`, simplify the base-6 power, collect the `r/(r+1)` factor. One-line algebra, entirely local. Then divide by `(r+1)`, take absolute value, observe limit `6r/(r+1)^2 -> 0`.

### HZ-11 verdict

The lemma's proof is a GENUINELY LOCAL algebraic computation performed on a cited input datum. No Vol I argument (recursion analysis, Stirling, Riccati algebraicity, exponential-base computation) is reproduced; only the closed-form VALUE of A_r is imported, and the lemma's novel content is the ratio identity and its `o(r+1)` consequence.

Two possible readings under HZ-11 discipline:

(i) `\ClaimStatusProvedHere` is LEGITIMATE: the lemma's claim is a local computational identity, the proof body is self-contained modulo a numerical input, and the input is cited via `V1-thm:...` resolving to a Vol I theorem. This is the Wave-11 agent's reading.

(ii) `\ClaimStatusProvedElsewhere` would be more honest: the "ratio identity" is an immediate arithmetic consequence of the Vol I closed form; the lemma is essentially a convenient packaging of `A_{r+1}/A_r = -6r/(r+1)` for downstream citation.

### Recommended verdict: (i) STANDS with minor hardening

Reading (i) is defensible under AP4 (proof body matches local computation) and PE-8 (cross-volume input datum is cited, not re-derived; local derivation is genuinely present). Reading (ii) would be an over-correction: the lemma is NOT `\ref{V1-thm:shadow-tower-asymptotic-closed-form} followed by "QED, see Vol I"`; it performs a small but genuine algebraic reduction (base-power cancellation + `o(r+1)` limit) that the Vol I theorem does not state.

Suggested hardening (optional, for future wave): insert an inline comment

```
% The lemma's local content is the ratio identity + o(r+1) limit;
% the closed form A_r = 8(-6)^{r-4}/r is INPUT from Vol I
% thm:shadow-tower-asymptotic-closed-form, not re-derived here.
```

just above the `\begin{proof}` to make the PE-8 split explicit for future auditors. NOT applied in this wave to keep triage scope minimal.

### AP287 check (cross-volume theorem existence without HZ-11 attribution)

The proof body writes "From Theorem~\ref{V1-thm:shadow-tower-asymptotic-closed-form} (Vol~I shadow_tower_higher_coefficients.tex, lines 1137--1183)" — attribution is EXPLICIT with file + line range. Not an AP287 violation.

## 5. Commit plan (caller-executed; agent has made no commits)

Suggested single commit:

```
Vol II Wave-12: shadow-tower companion V1-* phantom retargets (AP241 residuals from Wave-11)

- vol2/main.tex: add 3 V1-thm:shadow-tower-{tier-4,subleading,sub-subleading}-closed-form phantomsection aliases (canonical homes in Vol I shadow_tower_higher_coefficients.tex).
- vol2/chapters/theory/tempered_stratum_characterization_platonic.tex: retarget 5 bare \ref sites (lines 263-265, 515, 1103) to V1-* phantoms.

HZ-11 discipline for lem:leading-coefficient-ratio-identity: ClaimStatusProvedHere verdict UPHELD — proof is local ratio arithmetic on cited Vol I input datum; AP287 check passes (explicit file+line attribution in proof body).

Companion-label audit complete: 3/3 labels inscribed in Vol I (not phantoms); Vol II consumer side now resolves cleanly via V1-* phantomsection pattern per Wave-11 precedent.

Also noted (out-of-scope for this triage, flagged for future wave):
- AP124 internal Vol I duplicate: thm:shadow-tower-sub-subleading-closed-form
  inscribed in both shadow_tower_higher_coefficients.tex:3215 AND
  shadow_tower_sub_subleading_platonic.tex:247. Canonical choice needed.
```

## 6. Out-of-scope flags for parent caller

- **AP124 internal Vol I duplicate**: `thm:shadow-tower-sub-subleading-closed-form` has TWO `\label{...}` sites in Vol I (`shadow_tower_higher_coefficients.tex:3215` and `shadow_tower_sub_subleading_platonic.tex:247`). Pre-commit grep gate per AP124 would reject this. Needs canonicalisation wave: pick one site, retire the other via phantomsection + rename.
- **Hook lint AP8/AP25/AP34/AP14/AP7/V2-AP26 warnings**: all pre-existing, not touched by this triage; out of mission scope.
- **Build-check hook**: caller handles per session protocol.
