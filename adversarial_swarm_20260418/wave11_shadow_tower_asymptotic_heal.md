# Wave 11 — Vol II `thm:shadow-tower-asymptotic-closed-form` targeted heal

**Date**: 2026-04-18
**Scope**: Vol II AP241/HZ-11 genuine phantom (prior Wave-10 Tier-1 classification)
**Agent voice**: Chriss-Ginzburg (targeted, atomic)
**Commits**: NONE (per mission constraints; all edits staged only)

## Mission

Resolve the 5 Vol II `\ref{thm:shadow-tower-asymptotic-closed-form}` consumers in
`chapters/theory/tempered_stratum_characterization_platonic.tex` (lines 199,
238, 262, 987, 1102). Wave-10 triage flagged this as the only GENUINE AP241 of
the Vol II Tier-1 phantoms, requiring semantic heal rather than tactical alias.

## Consumer context read (Phase 1)

All five consumer sites cite the exact same content: the leading Laurent
coefficient closed form

$$A_r \;:=\; \lim_{c \to \infty} c^{r-2} S_r(\mathrm{Vir}_c) \;=\; \frac{8 (-6)^{r-4}}{r}, \qquad r \geq 4,$$

together with the recursion $A_{r+1}/A_r = -6r/(r+1)$.

Representative consumer usages:

- **:170** (section prose): "thm:shadow-tower-asymptotic-closed-form (Vol~I
  \texttt{shadow\_tower\_higher\_coefficients.tex}) supplies the closed form of
  the leading Laurent coefficient $A_r = 8(-6)^{r-4}/r$".
- **:199** (proof of `lem:leading-coefficient-ratio-identity`): "From
  Theorem~\ref{...} (Vol~I shadow\_tower\_higher\_coefficients.tex, lines
  1137–1183), $A_r = 8(-6)^{r-4}/r$".
- **:238** (proof of `prop:virasoro-ratio-test`): "By Theorem~\ref{...},
  $S_r(\mathrm{Vir}_c) = A_r / c^{r-2} + O(c^{-(r-1)})$".
- **:262, :987, :1102** (cross-reference index / HZ-IV `derived_from` / chapter
  cross-links): each attributes the closed form to Vol~I.

**Verdict**: all five consumers already prose-tag the theorem as Vol~I. The
inscription IS canonical; only build-time label resolution was broken.

## Vol I canonical inscription verified

`/Users/raeez/chiral-bar-cobar/chapters/theory/shadow_tower_higher_coefficients.tex:2833-2901`

```
\begin{theorem}[\label{thm:shadow-tower-asymptotic-closed-form}Closed
form for the leading asymptotic]
\ClaimStatusProvedHere
For every r >= 4, ... A_r = 8 (-6)^{r-4} / r.
Equivalently A_r = -6(r-1)/r * A_{r-1}, A_4 = 2.
\end{theorem}
```

Four-step proof body present (master-equation recurrence at $(3, r-1)$ leading
pair, telescoping, numerical check through $r = 11$, sympy cross-check).
Content matches consumer expectations verbatim.

## Heal strategy: **(A) HZ-11 cross-volume retarget via `V1-` phantom**

Options enumerated:

- **(A, selected)** Retarget the 5 Vol II `\ref{}` to the established Vol~II
  `V1-<label>` phantom convention. Reflects true epistemic state: the theorem
  is Vol~I canonical; Vol~II is a consumer. Consistent with ~500 pre-existing
  `V1-*` phantoms in `vol2/main.tex:409+`.
- **(B)** Inscribe locally in Vol~II. REJECTED: duplicates Vol~I proof; creates
  AP124/AP125 label-uniqueness conflict; semantically incorrect (Vol~II
  chapter OPENLY attributes the closed form to Vol~I in its own %% header).
- **(C)** AP286 tactical alias to a Vol~II candidate
  (`rem:shadow-closed-form-structure`, `prop:w3-shadow-leading-asymptotic`,
  `eq:virasoro-r-laurent`). REJECTED: no Vol~II candidate contains the
  explicit $A_r = 8(-6)^{r-4}/r$ content; the Vol~II chapter explicitly
  DERIVES FROM Vol~I, not the other way.

(A) is the canonical HZ-11 pattern: Vol~I inscribes `\ClaimStatusProvedHere`;
Vol~II `\ref`s via `V1-*` phantom; no duplication, no semantic drift.

## Atomic edits applied

**Edit 1** — `vol2/main.tex:652`, insert alphabetically between
`V1-thm:shadow-radius` (651) and `V1-thm:single-line-dichotomy` (652):

```
\phantomsection\label{V1-thm:shadow-tower-asymptotic-closed-form}%
```

**Edit 2** — `vol2/chapters/theory/tempered_stratum_characterization_platonic.tex`,
replace_all `\ref{thm:shadow-tower-asymptotic-closed-form}` →
`\ref{V1-thm:shadow-tower-asymptotic-closed-form}`. Touches 5 consumer sites
(199, 238, 262, 987, 1102). Three non-`\ref` mentions (comment lines 47, 91,
170 — `%%` block + plain-text prose) correctly untouched.

## Verification

- `grep '\\ref\{thm:shadow-tower-asymptotic-closed-form\}'` across all Vol~II
  chapters + standalone: **0 hits** (zero residual unprefixed refs).
- `grep 'V1-thm:shadow-tower-asymptotic-closed-form'` in `vol2/main.tex`:
  1 hit (phantom line 652).
- `grep 'V1-thm:shadow-tower-asymptotic-closed-form'` in
  `tempered_stratum_characterization_platonic.tex`: **5 `\ref{}` hits**
  (matching all 5 consumer sites).
- Build not attempted (mission constraint; local worktree, no commit).

## Discipline audit

- **PE-7 (label uniqueness)**: new `V1-thm:shadow-tower-asymptotic-closed-form`
  unique in `vol2/main.tex` (grep: 1 hit only, inserted).
- **PE-8 (cross-volume)**: Vol~I canonical label preserved; Vol~II refs
  retargeted to phantom; no content duplication.
- **AP241 (advertised-but-not-inscribed)**: resolved — theorem IS inscribed
  (Vol~I), and Vol~II now correctly references it.
- **AP255 (phantom file + phantomsection mask)**: NOT applicable — Vol~I
  inscription is a real theorem with proof body, not a phantom stub; the
  Vol~II `V1-*` phantom is the correct cross-volume convention, not a mask.
- **AP286 (tactical alias vs semantic heal)**: the heal is SEMANTIC — the
  label points to the canonical Vol~I theorem body where the mathematics
  lives. Not a tactical close; the epistemic chain is intact.
- **AP287 (cross-volume citation without HZ-11 attribution)**: all 5 consumer
  sites already prose-attribute to Vol~I ("Vol~I
  \texttt{shadow\_tower\_higher\_coefficients.tex}") and carry explicit line
  citations at `lem:leading-coefficient-ratio-identity` proof body. HZ-11
  attribution discipline satisfied in prose; `V1-` prefix now matches.
- **HZ-11 (cross-volume ProvedHere discipline)**: the consumer lemma
  `lem:leading-coefficient-ratio-identity` is `\ClaimStatusProvedHere` in
  Vol~II citing a Vol~I theorem. Per HZ-11 canonical rule this should either
  (a) inscribe locally in Vol~II, or (b) downgrade to `\ClaimStatusProvedElsewhere`
  with attribution remark. The Vol~II lemma body IS a genuine local argument
  (leading-ratio algebraic computation from the imported Vol~I $A_r$ closed
  form); the import is data, not theorem body. This is a legitimate
  `\ClaimStatusProvedHere` consuming a `\ClaimStatusProvedElsewhere` Vol~I
  input. Flagged for audit awareness; no rectification required by this
  heal's scope.

## Commit plan

Per mission constraint: NONE. Edits staged only. Recommended future commit:

```
Vol II phantom heal: thm:shadow-tower-asymptotic-closed-form → V1-* prefix

- Register V1-thm:shadow-tower-asymptotic-closed-form in main.tex phantom
  block (alphabetical between V1-thm:shadow-radius and
  V1-thm:single-line-dichotomy).
- Retarget 5 \ref{} consumers in tempered_stratum_characterization_platonic.tex
  (199, 238, 262, 987, 1102).
- Resolves Wave-10 Tier-1 AP241 genuine phantom (Vol I inscription exists at
  shadow_tower_higher_coefficients.tex:2833, ClaimStatusProvedHere; Vol II
  was missing the cross-volume phantom mask, causing [?] at build).
```

Authored by: Raeez Lorgat.

## Residual frontier items (OUT OF SCOPE, flagged)

- The `thm:shadow-tower-tier-4-closed-form`, `thm:shadow-tower-subleading-closed-form`,
  `thm:shadow-tower-sub-subleading-closed-form` labels referenced at Vol~II
  `tempered_stratum_characterization_platonic.tex:263-265` were not audited
  in this heal. Separate triage recommended for Wave-12 if any render `[?]`.
- HZ-11 discipline check on `lem:leading-coefficient-ratio-identity` flagged
  above; recommend Wave-12 audit of whether the `\ClaimStatusProvedHere` tag
  should be `\ClaimStatusConditional` on Vol~I input.
