# Attack-and-heal: Chiral HDC type error in `thm:H-concentration-via-E3-rigidity`

Date: 2026-04-18
Target: Vol II `chapters/theory/chiral_higher_deligne.tex`
Trigger: Wave HDC audit 2026-04-18 (`attack_heal_chiral_HDC_20260418.md`) surfaced a
composite native/derived + E_1/E_3 envelope type error in the
load-bearing Steps 1–2 of `thm:H-concentration-via-E3-rigidity`.
Mission: targeted heal — downgrade the broken route to conjecture, inscribe
retraction remark, propagate stratified `Conditional` tags to the
downstream corollary `cor:universal-holography-class-M` and theorem
`thm:chd-ds-hochschild` (both of which inherit the chain-level
$E_3$-chiral lift conditionality of `thm:chiral-higher-deligne`(2)),
update cross-volume consumers and the CLAUDE.md status row.
Author: Raeez Lorgat.

## 1. Attack verification

Opened `chapters/theory/chiral_higher_deligne.tex` at the cited theorem
(line 650 before heal) and audited Steps 1–2 verbatim.

Step 1 (lines 664–669, pre-heal):
> The restricted algebra $\cA|_{D_x}$ is an $E_3$-algebra in
> $\Bbbk$-chain complexes (in the sense of
> Convention~\ref{conv:chd-e3-chiral-meaning}) by
> Thm~\ref{thm:chiral-higher-deligne}(1).

This is a **native-vs-derived type error**. `thm:chiral-higher-deligne`(1)
places the $E_3$-chiral structure on the derived centre
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)$, not on $\cA$ itself. The same
chapter inscribes this as an explicit error-template in
`rem:chd-native-vs-derived` (lines 591–599): "Writing $E_3$ on $\cA$ is
a type error." Step 1 of the `thm:H-concentration-via-E3-rigidity` proof
commits exactly that error on the formal-disc restriction.

Step 2 (lines 685–691, pre-heal):
> Chiral PBW collapse for $\cA$ in the Koszul locus (Vol.~I,
> Theorem~\ref*{thm:pbw-koszulness-criterion}) identifies
> $\cA|_{D_x} = U_{E_3}(V_x)$ where $V_x$ is the space of generators
> restricted to $D_x$, of polynomial growth.

This is a **second, independent type error**: chiral PBW on the Koszul
locus gives the $E_1$-chiral envelope of the generating space, not an
$E_3$-envelope. The target of chiral PBW is the native $E_1$-chiral
structure on $\cA$, not an $E_3$-structure.

Combined: replacing $\cA|_{D_x}$ by
$Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ fixes Step 1 but breaks
Step 2. No inscribed theorem presents the derived centre as an
$E_3$-envelope of a polynomial-growth generating space, and a
chiral-$E_3$-PBW theorem of this shape is not available in Vol~I,
Vol~II, or Vol~III at time of writing.

Verdict: the Wave HDC audit's diagnosis is fully confirmed. The
`thm:H-concentration-via-E3-rigidity` proof as written is invalid; the
two errors do not cancel. Theorem H itself is unaffected — the
canonical proof in Vol~I (`thm:hochschild-concentration-E1`, chiral PBW
plus Shelton–Yuzvinsky Orlik–Solomon Koszulity) is disjoint from the
$E_3$-rigidity route.

## 2. Heal applied

### 2.1 Retract `thm:H-concentration-via-E3-rigidity` to conjecture

File: `chapters/theory/chiral_higher_deligne.tex`.

- Environment: `\begin{theorem}` → `\begin{conjecture}`; status tag
  `\ClaimStatusProvedHere` → `\ClaimStatusConjectured`; label
  `thm:H-concentration-via-E3-rigidity` →
  `conj:H-concentration-via-E3-rigidity`, with
  `\phantomsection\label{thm:H-concentration-via-E3-rigidity}` preserved
  for consumer-ref resolution (AP286 tactical alias; paired with
  prose-level honest retraction at every live consumer below).
- Statement body: replaced "applied at each point of $X$" with "applied
  pointwise to $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$" and
  appended an explicit conjectural-status clause naming the
  chiral-$E_3$-PBW inscription as the open closure condition, with
  forward reference to the retraction remark.
- Pointer to canonical Vol~I proof of Theorem H inside the conjecture
  body.

### 2.2 Inscribe `rem:H-concentration-via-E3-rigidity-type-error-retraction`

New remark block (lines 673–719) following the conjecture. Names both
type errors explicitly (Step 1 native-vs-derived; Step 2 E_1-vs-E_3
envelope), cites `rem:chd-native-vs-derived` for the Step-1 error
template, explains that Step-1 correction breaks Step 2, notes that
no chiral-$E_3$-PBW theorem is inscribed in any volume, and clarifies
that Theorem H is unaffected (Vol~I parallel proof is disjoint and
canonical). Registers the retraction under local-AP discipline
(AP2021).

### 2.3 Rewrite Steps 1–3 of the former proof as
`rem:H-concentration-via-E3-rigidity-partial-evidence`

File: `chapters/theory/chiral_higher_deligne.tex` (lines 721–784).

- Environment: `\begin{proof}` → `\begin{remark}[Partial evidence ...]`
  per AP4/HZ-8 (proof after conjecture forbidden; Remark[Evidence] is
  the canonical vehicle).
- Step 1: rewritten to correctly place $E_3$-chiral on
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ with explicit
  cross-reference to `rem:chd-native-vs-derived`.
- Step 2: flagged as `(CONJECTURAL INPUT; not presently inscribed)`;
  records that chiral PBW gives $U_{E_1}^{\mathrm{ch}}(V_x)$, not
  $U_{E_3}$, and that the chiral-$E_3$-PBW presentation of
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x})$ is the open closure
  condition.
- Step 3: rewritten as "conditional on Step 2" with honest scope.
- Closing status paragraph: Theorem H unaffected; $E_3$-rigidity route
  contingent on future chiral-$E_3$-PBW inscription.

### 2.4 Soften `rem:chd-consequence-not-hypothesis`

File: `chapters/theory/chiral_higher_deligne.tex` (lines 786–799).

Retitled "Concentration is consequence, not hypothesis" →
"Concentration as conjectural consequence". Body rewritten to present
the $E_3$-rigidity-as-consequence reading as a suggestive conjectural
re-parse contingent on the open chiral-$E_3$-PBW inscription, with
explicit redirection to the canonical Vol~I chiral-PBW +
Orlik–Solomon proof as the unconditional route.

### 2.5 Stratified `Conditional` tag on `thm:chd-ds-hochschild`

File: `chapters/theory/chiral_higher_deligne.tex` (lines 815–835 header
+ lines 889–898 proof coda).

- Header split: `\ClaimStatusProvedHere` → "$E_2$-chiral brace
  quasi-iso `\ClaimStatusProvedHere`, $E_3$-chiral lift
  `\ClaimStatusConditional`".
- Step 4 proof coda rewritten: the $E_3$-chiral lift clause is
  unconditional on cohomology (associator dependence collapses by
  `thm:chiral-higher-deligne`(3)) and conditional at chain level on
  the $(\SCchtop)^!$-cobar contracting homotopy cited in
  `rem:chd-universality-conditional`. $E_2$-chiral quasi-iso is
  unconditional.

### 2.6 Stratified `Conditional` tag on `cor:universal-holography-class-M`

File: `chapters/theory/chiral_higher_deligne.tex` (lines 920–948 header
+ lines 961–971 proof coda).

- Header split: `\ClaimStatusProvedHere` → "cohomological
  `\ClaimStatusProvedHere`, chain-level $E_3$-chiral
  `\ClaimStatusConditional`".
- Proof coda appended: the $E_3$-chiral chain-level identification
  inherits the conditionality of `thm:chd-ds-hochschild` and
  `thm:chiral-higher-deligne`(2); the underlying $E_2$-chiral /
  Gerstenhaber identification is unconditional.

### 2.7 Independent-verification scaffold (§9) update

File: `chapters/theory/chiral_higher_deligne.tex` (lines 1015–1046).

- Item 2 heading: `thm:H-concentration-via-E3-rigidity` →
  `conj:H-concentration-via-E3-rigidity` with retraction note.
- "Derived-from" → "Scaffolded-from"; introduces "Open closure
  condition" naming the missing chiral-$E_3$-PBW theorem.
- "Verified-against" → "Parallel-unconditional", clarifying that
  Shelton–Yuzvinsky supplies the canonical unconditional Vol~I proof
  of Theorem H and that Fuks 1986 is an independent concentration
  cross-check; the conjectural $E_3$-rigidity route remains an open
  inscription target.
- Test status note: test passes only as consistency check on
  `lem:chd-e3-rigidity-point`, not as independent verification of the
  conjectural route.

### 2.8 "What this chapter does not prove" (§10) update

File: `chapters/theory/chiral_higher_deligne.tex` (lines 1079–1089).

Item on polynomial-growth hypothesis rewritten to condition its
landscape-wide coverage on the conjectural chiral-$E_3$-PBW
inscription; Theorem H's unconditional status is re-emphasised via the
parallel Vol~I Orlik–Solomon proof.

### 2.9 Cross-volume consumer updates

- Vol II `chapters/frame/preface.tex:414`: replaced the parenthetical
  `(Theorem~\ref{thm:H-concentration-via-E3-rigidity})` with a
  multi-sentence honest block attributing Theorem H concentration to
  the unconditional Vol~I chiral-PBW plus Orlik–Solomon proof and
  flagging `conj:H-concentration-via-E3-rigidity` as retracted
  2026-04-18 with pointer to the retraction remark.
- Vol I `chapters/theory/chiral_climax_platonic.tex:926–931`:
  parallel prose update. "The structural source ..." recast as "A
  conjectural structural source ..." with retraction reference and
  re-direction to the canonical Vol~I unconditional proof.
- Vol I `standalone/theorem_index.tex:2402`: row changed from
  `theorem ... ProvedHere` to `conjecture ... Conjectured` with
  retraction note in the title; label bumped to
  `conj:H-concentration-via-E3-rigidity`.
- Vol I `CLAUDE.md:614` (Chiral Higher Deligne status row): rewritten
  to reflect the three-way downgrade: retracted theorem; $E_2$-chiral
  vs $E_3$-chiral split on `thm:chd-ds-hochschild`; cohomological vs
  chain-level split on `cor:universal-holography-class-M`. Pointer to
  this attack-heal note inscribed.

### 2.10 Artifacts not updated (out of mission scope, noted for a
follow-up pass)

- `metadata/dependency_graph.dot:2634`, `metadata/label_index.json:24710`,
  `metadata/claims.jsonl:2500` still tag the label as `theorem`/
  `ProvedHere`. These are machine-generated and will refresh on the
  next `python3 scripts/generate_metadata.py` run.
- `compute/tests/test_chiral_higher_deligne.py:42,235,238` still uses
  the bare `thm:` label in `@independent_verification(claim=...)`
  decorators. The phantomsection alias keeps the label resolvable; a
  follow-up pass should either retarget the `claim=` strings to
  `conj:H-concentration-via-E3-rigidity` or add a short module-level
  comment explaining the alias. The decorated test body itself is a
  consistency check on `lem:chd-e3-rigidity-point`, not an independent
  verification of the conjectural route, and is now annotated as such
  in the §9 scaffold prose.
- Vol II `notes/first_principles_cache_comprehensive.md:1520` narrative
  ("Theorem H concentration is now CONSEQUENCE of $E_3$-rigidity ...")
  is stale under the retraction (AP288 session-ledger drift). Not
  touched in this heal; flagged for a session-ledger pass.
- Vol III `FRONTIER.md:19` narrative mentions
  `thm:H-concentration-via-E3-rigidity` as proved. Not touched;
  flagged for a cross-volume status-row sweep.
- Vol I `FRONTIER.md:39` CL15 entry advertises PROVED and names the
  retracted label. Flagged for the same sweep.
- Vol I `AGENTS.md:641` row. Same.

Rationale for leaving these to a follow-up: the mission brief
scoped the heal to the Vol~II inscription + stratified
`Conditional` propagation to `thm:chd-ds-hochschild` +
`cor:universal-holography-class-M`; cross-volume ledger and
FRONTIER sweeps are separate AP149 propagation tasks and should be
batched atomically to prevent partial drift (AP304-style reservation
discipline recommends scoping narrow per-mission).

## 3. Local AP registration

- AP2021 (chosen from the reserved MC5-swarm block AP2021–AP2040 per
  the mission brief): composite native-vs-derived + E_1-vs-E_3
  envelope type error masked by the same-letter label
  `thm:H-concentration-via-E3-rigidity`, with two type errors in
  consecutive proof steps whose combined effect is that each step's
  correction breaks the other. This is a specific instance of AP159
  (Yangian type conflations) + AP161 (E_1-chiral notion proliferation)
  + AP244 (overcounted foundational terms); distinct diagnostic
  signature: **same algebra carries distinct operadic structures at
  distinct levels of derivation, and a proof conflates them at two
  consecutive steps such that neither can be corrected without
  breaking the other**. Counter: before inscribing any chain-level
  proof invoking both a formal-disc restriction AND a Koszul-locus
  PBW identification AND a higher-$E_n$ structure on the derived
  centre, write a four-line "object table" enumerating
  $(\cA,\cA|_{D_x},Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),
   Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x}))$ and mark for each
  which operadic structure ($E_1$-chiral, $E_3$-chiral) applies by a
  named theorem; a step using "$\cA|_{D_x}$ is $E_3$" or
  "$\cA = U_{E_3}(V)$" must be rejected unless the table has been
  filled in with an explicit citation.

## 4. Build / test status

- Environment balance verified manually at file level after heal:
  `\begin{proof}` 8, `\end{proof}` 8; `\begin{remark}` 11,
  `\end{remark}` 11; `\begin{conjecture}` 1, `\end{conjecture}` 1.
- Full Vol~II build not executable on this host (AP293:
  `pdflatex` not on PATH). Defer build verification to the next
  session that has the LaTeX toolchain installed; the heal is
  confined to well-formed LaTeX changes, so breakage is unlikely but
  not verified.
- `compute/tests/test_chiral_higher_deligne.py` not re-run for the
  same reason; test body is a structural consistency check on
  `lem:chd-e3-rigidity-point` (not dependent on the retracted
  theorem's proof) and should continue to pass.

## 5. Patch index (git-apply form not produced because edits are in
the main working tree, not an isolated worktree)

The edits span the following files in the main tree:

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/chiral_higher_deligne.tex`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex`
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_climax_platonic.tex`
- `/Users/raeez/chiral-bar-cobar/standalone/theorem_index.tex`
- `/Users/raeez/chiral-bar-cobar/CLAUDE.md`

Reviewable via `git diff` in each of the two repositories.

## 6. Downstream items for subsequent waves

- Metadata regeneration (`scripts/generate_metadata.py`) across both
  volumes.
- Test-decorator `claim=` retargeting on
  `compute/tests/test_chiral_higher_deligne.py`.
- Cross-volume FRONTIER.md / AGENTS.md / session-ledger sweep (Vol~I
  FRONTIER.md CL15; Vol~III FRONTIER.md; Vol~II
  `notes/first_principles_cache_comprehensive.md:1520`).
- Open inscription target: chiral-$E_3$-PBW theorem presenting
  $Z^{\mathrm{der}}_{\mathrm{ch}}(\cA|_{D_x}) = U_{E_3}(W_x)$ for
  polynomial-growth $W_x$ across the standard landscape; if
  inscribed, `conj:H-concentration-via-E3-rigidity` would promote
  back to theorem and supply the $E_3$-rigidity parallel proof of
  Theorem H. The two proof chains would then share
  `thm:pbw-koszulness-criterion` and therefore be non-disjoint in
  the HZ-IV sense; the Orlik–Solomon route remains canonical.

End of report.
