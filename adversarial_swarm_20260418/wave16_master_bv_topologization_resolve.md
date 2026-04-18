# Wave-16 Resolution: `conj:master-bv-brst` + `thm:topologization-tower`

**Date**: 2026-04-18
**Scope**: Vol I Tier-1 phantoms re-flagged by Wave-15 chapter-stubs agent (a299abb7).
**Verdict**: Both phantoms already resolved via AP286-legitimate tactical phantomsection aliases. **No new edits required.**

## 1. `conj:master-bv-brst` (47 consumers in Vol I)

### Label-existence grep (pre-verification)
```
grep -rn '\label{conj:master-bv-brst}' /Users/raeez/chiral-bar-cobar
```

Hits (live `.tex` only, excluding audit logs):
- `chapters/connections/editorial_constitution.tex:433` — `\phantomsection\label{conj:master-bv-brst}` (alias)
- `main.tex:1904` — `\phantomsection\label{conj:master-bv-brst}% % editorial_constitution.tex` (main.tex stub)

### Canonical body verification
`chapters/connections/editorial_constitution.tex:434-459` inscribes the full conjecture body under canonical label `\label{conj:v1-master-bv-brst}` (line 435). The conjecture is a genuine `\begin{conjecture}[BV/BRST/bar identification]` with `\ClaimStatusConjectured{}`, four-paragraph scope remark distinguishing D^co resolution (via `thm:bv-bar-coderived`) from chain-level identification (G/L proved, C conditional, M fails — quartic harmonic obstruction), and explicit downstream placement relative to `thm:master-pbw`, `thm:master-theta`, and the other master conjectures. Companion `rem:mc5-vs-bv-brst` at line 461 further scopes the analytic-vs-identification distinction.

### AP286 verdict
This is the **canonical AP286 tactical-alias pattern done correctly**:
1. Body inscribed at canonical label (`conj:v1-master-bv-brst`).
2. Short alias `conj:master-bv-brst` provided at the same file via `\phantomsection\label{}`.
3. Consumer prose is semantically uniform: every consumer references "the BV/BRST/bar identification conjecture" or "the master BV/BRST conjecture", which exactly matches the inscribed body's statement.
4. No prose treats the alias as a distinct conjecture from the canonical.

Confirms Wave-8 agent (a36683fc) verdict. Wave-15 re-flagging was a **detector false positive** — the chapter-stubs detector does not distinguish tactical phantomsection aliases from genuine phantom refs.

**No action required.** Grep-gate delta = 0.

## 2. `thm:topologization-tower` (5 consumers in Vol I)

### Label-existence grep (pre-verification)
```
grep -rn '\label{thm:topologization-tower}' /Users/raeez/chiral-bar-cobar
```

Hits:
- `chapters/frame/preface.tex:5153` — `\phantomsection\label{thm:topologization-tower}% alias: Vol II thm:iterated-sugawara-construction + thm:e-infinity-topologization-ladder (e_infinity_topologization.tex)%`

### Consumers (5 refs across 1 file)
All five Vol I consumers live in `chapters/frame/part_iv_platonic_introduction.tex`:
- `:655` — inside theorem header noting class-$M$ ladder is proved weight-completed here; bounded-direct-sum ambient chain-level is false per cross-volume tower theorem.
- `:682` — clause (iii) of the ladder theorem, citing weight-completed $\Einfty$-topological structure.
- `:716` — inside proof body, class-$M$ direction, weight-completed.
- `:736` — inside HZ-IV decorator's `Derived from:` clause.
- `:939` — table reference.

All five consumers treat `thm:topologization-tower` as the **umbrella class-$M$/class-$L$ topologization result canonically inscribed cross-volume**.

### Canonical Vol II targets (both verified present)
```
grep -n '\label{thm:iterated-sugawara-construction}\|\label{thm:e-infinity-topologization-ladder}' \
  /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/e_infinity_topologization.tex
```
- `:224` — `\ClaimStatusProvedHere]\label{thm:iterated-sugawara-construction}` (class-$L$ cohomological via `[Q,G^{(n)}] = T^{(n)}`).
- `:435` — `\label{thm:e-infinity-topologization-ladder}` (iterated Dunn → $E_{k+2}$-top).

### AP286 verdict
The `preface.tex:5153` alias is an **AP286 umbrella alias** pointing at two distinct but logically paired Vol II theorems. The alias comment explicitly names both targets. The five consumers in `part_iv_platonic_introduction.tex` treat `thm:topologization-tower` as the umbrella — consistent with AP286-legitimate usage per Wave-7 verification pattern (a220890d).

One pedantic concern (AP286 sub-pattern, per CLAUDE.md line): when an alias bundles two theorems, consumer prose should ideally disambiguate which of the two is load-bearing at each site. Audit of the five consumer sites:
- `:655, :682, :716` — cite "the weight-completed class-$M$ topologization", matching `thm:e-infinity-topologization-ladder` at Vol II :435 (the ladder carrying the class-$M$ weight-completed direction).
- `:736` — HZ-IV `Derived from:`, implicitly uses the ladder endpoint.
- `:939` — table entry.

Every consumer's semantic target is `thm:e-infinity-topologization-ladder`. The iterated Sugawara theorem at :224 is logically upstream (input) but not directly cited by Vol I consumers. Alias bundle is **semantically correct but slightly over-named**; semantic purity would be served by either (a) narrowing the alias to just `thm:e-infinity-topologization-ladder`, or (b) leaving bundled with the current comment documenting both inputs. Both are legitimate; (b) preserves the umbrella semantics that Vol I prose already uses.

**No action required.** Confirms Wave-7-style AP286 tactical heal.

## Post-verification grep-gate (AP320 discipline)

```
grep -rn '\label{conj:master-bv-brst}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/main.tex
# 2 hits (unchanged) — phantomsection alias + main.tex stub

grep -rn '\label{thm:topologization-tower}' /Users/raeez/chiral-bar-cobar/chapters /Users/raeez/chiral-bar-cobar/main.tex
# 1 hit (unchanged) — preface.tex phantomsection alias
```

Delta (pre-vs-post) = 0 on both. No edits were required or made.

## Commit plan
None. This note is observational only; neither phantom requires inscription, retargeting, or annotation beyond what Wave-7/Wave-8 already installed. The Wave-15 re-flagging reflects a detector-coverage gap — the chapter-stubs sweep does not compute AP286-alias-legitimacy, so tactical phantomsection aliases are repeatedly re-surfaced as candidates. Recommended detector upgrade (out of scope here): extend the phantom-ref detector to (i) locate the `\phantomsection\label{X}` alias site; (ii) parse the in-line comment for a canonical-target pointer; (iii) verify the canonical target exists (Vol I inline body, or cross-volume `\label{}` at the named file); (iv) suppress the flag when (i)+(ii)+(iii) hold and the consumer prose does not demand umbrella decomposition.

## References
- Wave-8 agent a36683fc: `conj:master-bv-brst` AP286 verification (editorial_constitution.tex:434-459).
- Wave-7 agent a220890d: `conj:topologization-general` AP286 verification (en_koszul_duality.tex:3392).
- Wave-15 chapter-stubs agent a299abb7: re-flagged both as Tier-1 residuals (detector false positive).
- CLAUDE.md AP255/AP286/AP287/AP320.
