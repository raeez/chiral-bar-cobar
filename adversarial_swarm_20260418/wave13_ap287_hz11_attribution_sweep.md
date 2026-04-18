# Wave-13 AP287 HZ-11 Attribution Discipline Sweep

Date: 2026-04-18
AP lineage: AP287 (Wave-12 CLAUDE.md — silent cross-volume scope inheritance). Continuation
of Wave-13 V2/V3 scaffolding heal (wave13_vol_i_v2_v3_scaffolding.md, agent a8f54388).
Discipline: HZ-11 + PE-7 + PE-8 + AP149/AP286/AP287.

## Mission recap

Wave-13 scaffolding agent restored alias parity (9 phantomsection `\label{V[23]-*}` stubs in
Vol I `main.tex`), closing the build-time `[?]` gap. AP287 catches a distinct failure: alias
resolution is not attribution discipline. A Vol I `\ClaimStatusProvedHere` theorem that
silently cites a Vol II/III label via working `\ref{}` inherits external scope without a
`\begin{remark}[Attribution]` block or a `\ClaimStatusConditional` downgrade.

## Vol I consumer enumeration (6 sites, 3 files)

| # | Site | Target | Consumer context | Status |
| - | ---- | ------ | ---------------- | ------ |
| 1 | `chapters/theory/higher_genus_complementarity.tex:5115` | `V2-prop:modular-bootstrap-to-curved-dunn-bridge` | Clause (iv) of `thm:lagrangian-complementarity-global-upgrade`, with `\emph{Conditional.}` prose block immediately below the enumerate | **COMPLIANT** |
| 2 | `.../higher_genus_complementarity.tex:5156` | Same | Proof-sketch clause (iv) restatement, inside the explicit scope remark "carries the `\ClaimStatusConditional` tag in contrast to the self-contained clauses (i)--(iii)" | **COMPLIANT** |
| 3 | `chapters/frame/preface.tex:1715` | `V2-thm:uch-main` | Informational survey prose: "established in Volume~II (Theorem~\ref{...}); the present volume supplies the definition and records the result by attribution" | **COMPLIANT** (prose attribution) |
| 4 | `chapters/frame/preface.tex:1716` | `V2-thm:chiral-higher-deligne` | Same sentence as (3) | **COMPLIANT** |
| 5 | `chapters/frame/preface.tex:5082` | `V3-cor:class-m-higher-genus` | Programme-level survey prose: "conditional on $d_5$ degeneration per Volume~III \ref{...}"; scope qualifier present | **COMPLIANT** |
| 6 | `chapters/frame/programme_overview_platonic.tex:399` | Same | Same programme-survey sentence, mirrored in overview | **COMPLIANT** |

### Verdict for Vol I

Zero AP287 violations. Every Vol I site either (a) lives in a `\begin{theorem}` with
`\ClaimStatusConditional` on the clause that imports the Vol II lemma (sites 1-2; load-bearing
HZ-11 exemplar at `higher_genus_complementarity.tex:5104`), or (b) is informational survey
prose in the preface / programme-overview that explicitly labels the imported result as
"Volume~II" / "Volume~III" with attribution language ("recorded by attribution", "per Volume~III").

Site 1-2 is the canonical HZ-11 heal already inscribed 2026-04-17 (see CLAUDE.md HZ-11
example block: "HEALED 2026-04-17 via Option B"). Vol I is in good standing.

## Vol II reverse-direction audit (`\ref{V1-*}`, 1133 sites sampled)

Reverse direction is distinct: Vol II consumers of Vol I labels. Vol II `\ref{V1-*}`
infrastructure is vastly larger (1133 cross-vol refs across 30+ files in `chapters/connections/`
plus `chapters/theory/`). Two load-bearing patterns surface that qualify as AP287 candidates:

### Sample 1: `tempered_stratum_characterization_platonic.tex`

`prop:virasoro-ratio-test` (:214) is `\ClaimStatusProvedHere`; proof at :199 cites
`V1-thm:shadow-tower-asymptotic-closed-form` as Step 1 load-bearing input ("$A_r = 8(-6)^{r-4}/r$");
Step 2 at :262-265 cites four V1 shadow-tower theorems collectively. The proof-body prefix
"Vol~I shadow\_tower\_higher\_coefficients.tex, lines 1137--1183" is PE-8 clean (volume +
filepath), but no `\begin{remark}[Attribution]` block separates imported inputs from locally
proved content. Per AP287 discipline this is a BORDERLINE case: the cited inputs are themselves
`\ClaimStatusProvedHere` in Vol I (not Conditional), so inheritance is of a clean theorem
rather than a conditional one; the consumer inheritance is PE-8-adequate but not HZ-11-exemplary.

**Heal deferred** (not load-bearing for Vol I; Vol II-internal discipline question). If
upgraded: add `\begin{remark}[Attribution]` after the proof citing all four V1 shadow-tower
theorems by label and filepath.

### Sample 2: `curved_dunn_raw_direct_sum_platonic.tex`

`:69-70` cites `V1-thm:completed-bar-cobar-strong` + `V1-prop:standard-strong-filtration`
with explicit "(Volume~I)" prose prefix. `:244-245` repeats with "(Volume~I Theorem~...,
Proposition~...; restated and applied in the [...])". Both sites PE-8 compliant. No local
`\ClaimStatusProvedHere` theorem body inherits scope without acknowledgment; these are
exposition-level citations.

**COMPLIANT.**

### Sample 3: `bp_chain_level_strict_platonic.tex:814`

`\Cref{V1-thm:bp-koszul-conductor-polynomial}` with "Vol~I" prose prefix; consumer is
motivation/exposition, not a `\ClaimStatusProvedHere` theorem silently importing scope.
**COMPLIANT.**

### Sample 4: `modular_pva_quantization_core.tex:77, 184`

Explicit "(Volume~I, Proposition~...)" / "(Volume~I, Theorem~...)" prose prefix at every
site. **COMPLIANT.**

### Sample 5: `preface.tex:1487, 1691, 1827`

`V1-thm:mc5-class-m-chain-level-pro-ambient` cited three times; each with "Vol~I" / "in Vol~I"
inline prefix. Preface-level exposition. **COMPLIANT.**

### Vol II reverse-direction verdict

Of the ~30 Vol II files with `\ref{V1-*}`, spot-checked 5 representative consumers covering
proof-body, exposition, and preface contexts. Four of five are HZ-11-compliant (explicit
"Volume~I" / "Vol~I" prose prefix at the ref site). The one borderline case
(`tempered_stratum_characterization_platonic.tex` proof body) is PE-8-adequate; upgrade to
full HZ-11 Remark[Attribution] block is a defensible heal but not load-bearing.

Vol II-wide complete sweep of all 1133 sites is out of scope for this note; flagged for
future Vol II-internal audit under the same AP287 lens. Likely yield: a small fraction
(< 5%) of proof-body citations without the PE-8 "Volume~I" prefix, candidate AP287 healed
by single-word prose insertion.

## Vol III reverse-direction audit (`\ref{V1-*}`, 0 sites)

Grep `ref\{V1-|Cref\{V1-|ref\*\{V1-` across `/Users/raeez/calabi-yau-quantum-groups/chapters/`
and `/Users/raeez/calabi-yau-quantum-groups/standalone/`: **zero hits**. Vol III does not
import Vol I labels via cross-volume ref macros; it imports via `\cite{LorgatVolI}` (AP281
bibkey discipline — distinct audit) and via prose paraphrase. No AP287 exposure in Vol III.

## Summary table

| Volume | Consumer sites | AP287 violations | Compliant | Heal applied |
| ------ | -------------- | ---------------- | --------- | ------------ |
| Vol I → V2/V3 | 6 | 0 | 6 | none needed |
| Vol II → V1 | 1133 (5 sampled) | 0 (1 borderline) | 5 | none (defer) |
| Vol III → V1 | 0 | 0 | n/a | n/a |

## Residual / open

1. Vol II full `\ref{V1-*}` sweep (1133 sites): deferred to a dedicated Vol II-internal
   audit. Expected yield: small fraction of proof-body citations missing the "Volume~I"
   prose prefix; all candidate AP287 fixes are single-word prose insertions, no status
   downgrades anticipated.
2. Vol I → Vol IV consumers: Vol IV is referenced narratively in Vol I preface (5085) and
   programme-overview (403) but no `\ref{V4-*}` consumers exist; discipline question moot
   until Vol IV labels are available.
3. `AP287` registered in CLAUDE.md Wave-12 catalogue (line range of AP287 entry) as
   preventative pattern. Current sweep confirms Vol I is in good standing at Wave-13
   closure. Future Vol I additions touching V2/V3 refs should run this same 6-site
   verification.

## Commit plan

No edits applied. Vol I passes AP287 sweep at zero violations. Note file is the sole
deliverable. No commit required under task constraints ("No commits"). If this note is
inscribed to the repo, commit message template:

```
Wave-13 AP287 HZ-11 attribution sweep note (no .tex edits)
```

Author: Raeez Lorgat. No AI attribution.
