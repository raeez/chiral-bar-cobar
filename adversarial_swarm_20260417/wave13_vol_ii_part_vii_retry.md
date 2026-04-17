# Wave 13 — Vol II Part VII (The Frontier) attack & heal (RETRY, rate-limit-safe)

Target: `~/chiral-bar-cobar-vol2/main.tex` lines 1690–1773 and the ten
frontier chapters it gathers (total 20,327 lines). This wave is the Vol II
mirror of Vol I Wave 10 (`wave10_part_vi_frontier_attack_heal.md`) and
Vol III Wave 10 (`wave10_vol_iii_part_vii_frontier_attack_heal.md`), now
executed after the 2026-04-16/17 closure wave that collapsed OF1/OF3/OF4/
OF8/OF9/OF11/OF12/OF13/OF16/OF17/OF22/OF25 (Vol I FRONTIER §3). The role
of this wave is to synchronise the typeset Vol II frontier register —
the main-abstract "five honest open frontiers" block (`main.tex:1206–1218`)
and the Part VII preamble (`main.tex:1695–1716`) — with the post-closure
status, retire frontier items that have been proved during Wave 1–12, and
surface residual opens in the three-volume canonical form.

Prior retries were aborted at the Edit stage by agent rate-limit cascade
(FM44). This retry document is scoped as a surgical heal register; inline
Edits are enumerated as precise old-string/new-string pairs so the heal
can be applied in a single Edit batch after the rate-limit window clears.

## Attack findings

### A1. "Five honest open frontiers" block is stale (main.tex:1206–1218)

The abstract enumerates F1–F5:

```
(F1) logarithmic W(p) triplet tempering;
(F2) periodic-CDG for non-simply-laced admissible levels
     (sl_2 closed, sl_{N≥3} open);
(F3) original-complex chain-level E_3-topological for class M
     (weight-completed proved);
(F4) super-complementarity canonical pairing (max(m,n) for super-Yangians);
(F5) irregular-singular regularity at M̄_{g,n} boundaries.
```

Post 2026-04-17 closure status (FRONTIER.md §3 + Vol I theorem-status
table):

- **F2 is CLOSED globally.** `thm:periodic-cdg-is-koszul-compatible`
  in `chapters/theory/periodic_cdg_admissible.tex` (Vol I) + its Vol II
  consumer via `thm:admissible-kl-bar-cobar-adjunction` close the
  admissible Kazhdan–Lusztig bar–cobar adjunction for all simply-laced
  types. For non-simply-laced sl_{N} admissible levels the Vol II
  sweep landed chain-level through Arkhipov–Gaitsgory twisted Satake
  + Finkelberg tilting semisimplification (Part "From Frontier to
  Theorem", main.tex:1752–1755). F2 is no longer a frontier item; it
  has been promoted to theorem in the non-degenerate locus.

- **F3 is CLOSED on three equivalent ambients.** The original-complex
  class-M chain-level identification is proved in
  `thm:mc5-class-m-chain-level-pro-ambient`,
  `thm:mc5-class-m-topological-chain-level-j-adic`, and the
  filtered-completed variant `prop:bv-bar-class-m-weight-completed`.
  The direct-sum "genuine falsity" is an ambient-choice artefact
  scoped to bounded Ch(Vect) and is NOT the ambient of the raw bar
  complex with its weight topology. The abstract's phrasing
  "original-complex … (weight-completed proved)" is stale: all three
  equivalent ambients are now proved; the "open" half of the
  sentence has no witness.

- **F1 (W(p) tempering) remains open but is refined.** Per Wave-12
  B91 / AP203 and `rem:wn-frontier-anchor-f1`, the Zhu-bounded-Massey
  proof chain fails at Gurarie 1993 / Flohr 1996 (unbounded Massey
  amplitudes despite finite-dim Zhu). The open direction is
  Adamović–Milas character-amplitude bound on φ_{0,1}. The honest
  statement for the abstract is: tempering on non-logarithmic
  C_2-cofinite landscape is PROVED; W(p) tempering is conjectured
  in H•_reg only.

- **F4 (super-complementarity) remains genuinely open.** Two pairings
  (supertrace vs Berezinian) coexist on the sub-Sugawara line; no
  canonicalisation exists at the programme level. Vol III Wave-1
  inscription of `lem:super-trace-berezinian-bridge` clarifies the
  discrepancy but does not canonicalise. This is the correct frontier
  statement.

- **F5 (irregular-singular M̄_{g,n} regularity) is CLOSED.**
  `thm:irregular-singular-kzb-regularity` in
  `chapters/theory/curved_dunn_higher_genus.tex` closes modular
  operad composition at generic non-integral level via
  Jimbo–Miwa Stokes-replacement. F5 is no longer open.

### A2. Part VII preamble (main.tex:1695–1716) mischaracterises the
class (iii) E_∞-ladder target.

The text says:

> (iii) higher-rung Platonic targets of the E_∞^top-ladder W_N → E_{N+1}^top
> for N ≥ 3, conditional on the higher-spin antighost construction.

This is stale. `thm:iterated-sugawara-construction` + `thm:e-infinity-
topologization-ladder` (Vol II `e_infinity_topologization.tex`) proved
the E_{k+2}-top ladder unconditionally on a depth-k stress tower, and
`cor:e-infinity-topologization-wN` specialised to W_N → E_{N+1}^top for
all N ≥ 3 via the iterated Casimir tower. The higher-spin antighost
construction is the witness of the iterated construction, not a
conditional input. Class (iii) is no longer a frontier class; it has
been absorbed into Part VI (the climax) proper.

### A3. The main-abstract "three volumes meet at one object" block is
correct but lacks the super-Riccati/super-trace caveat the
2026-04-17 audit surfaced.

Lines 1195–1204 read:

> Volume III categorical (the CY-to-chiral functor Φ with E_n-level
> dimension dependence, the six-routes pentagon stratified by
> generator rank ρ^{R_i}, the super-Riccati shadow tower with
> max(m,n) complementarity, …).

Per Vol III Wave-1 B90 healing (`rectification_map_beilinson_audit.md`),
the six-routes pentagon stratifies `ρ^{R_i}` (generator rank), NOT
`κ_ch` (which is Hodge-supertrace invariant = 0 route-independent for
K3×E). The text above is the post-heal phrasing and matches. No edit
required here.

### A4. The "irreducible opens" closing paragraph (main.tex:1765–1769)
overreaches.

> All four irreducible opens remaining at the close of the HEAL+UPGRADE
> sweep (curved-Dunn H², class M chain-level, periodic-CDG admissible,
> chain-level Deligne–Tamarkin) are now closed on the non-degenerate
> locus; the programme's Platonic form is realised.

This statement is correct for the four items named. But it implicitly
erases the five residual opens F1–F5 listed in the abstract. The
architecture needs a one-sentence bridge: "Beyond these four, Part VII
registers five residual directions (F1, F4 above plus three subsidiary
opens) that remain genuinely open; they are scope-boundary items, not
obstructions to the climax." This matches the Vol I `FRONTIER.md` §2
"CLOSED DURING AUDIT" vs §3 "GENUINE OPEN" partition.

## Residual genuine opens after the Wave-1–12 closure pass

Synchronised with Vol I FRONTIER §3 and Vol III CL-registers:

| Item | Statement | Status | Locus |
|------|-----------|--------|-------|
| F1'  | W(p) triplet tempering on H•_reg | Conjectured (Adamović–Milas path) | `conj:f1-wp-tempering`, logarithmic stratum |
| F4'  | Super-complementarity canonical pairing (super-trace vs Berezinian) | Open | sub-Sugawara super-Yangian line |
| F6   | λ_g-conjecture residue at g ≥ 3 (AP225) | Open | Theorem D all-genera clutching-uniqueness |
| F7   | Modular-family Theorem A base-change (Francis–Gaitsgory six-functor) | Conditional | relative Ran prestack |
| F8   | B^{(2)}_TCFT vs B^{(2)}_naive chain-level gap for class M | Open | Vol III AP-CY34 residue |

(F2, F3, F5 retired; class (iii) E_∞-ladder absorbed.)

## Cross-volume bridges

- Vol I `FRONTIER.md` §3 records the canonical OF1–OF25 register; Vol II
  F1'/F4'/F6/F7/F8 correspond to OF5 (W(p)), OF19 (super-pairing),
  OF-AP225 (λ_g residue), CL2 (modular family), OF12 (B^{(2)}).
  A future propagation pass should replace the F1–F5 tags in
  `main.tex:1207–1218` with the cross-volume OF labels so the three
  volumes share one index.

- Vol III `adversarial_swarm_20260417/wave1_*` documents already carry
  the F4' canonical-pairing bridge at the super-Yangian level. Vol II's
  super-Riccati shadow tower in the main abstract is the Hodge-supertrace
  shadow of Vol III's AP-CY46 calculation.

## Surgical heal edits (enumerated; apply in one Edit batch)

The following are the exact old-string / new-string pairs. All labels
continue to exist in the healed tree; no cross-reference breakage.

### HEAL-1. Retire F2 + F3 from the abstract; refine F1; retire F5.

**File:** `~/chiral-bar-cobar-vol2/main.tex`

**Lines 1206–1218.** Replace the five-item block with a three-item
block plus a subsidiary sentence:

```
\textbf{Five honest open frontiers.}
(F1) logarithmic $W(p)$ triplet tempering;
(F2) periodic-CDG for non-simply-laced admissible levels
(sl$_2$ closed, sl$_{N \ge 3}$ open);
(F3) original-complex chain-level $E_3$-topological for class
$\mathbf{M}$ (weight-completed proved,
\texttt{prop:bv-bar-class-m-weight-completed});
(F4) super-complementarity canonical pairing
($\kappa + \kappa^! = \max(m,n)$ for super-Yangians on the
sub-Sugawara line; supertrace versus Berezinian pairings
coexist);
(F5) irregular-singular regularity at $\overline{\cM}_{g,n}$
boundaries.
```

→

```
\textbf{Three residual open frontiers.}
(F1$'$) logarithmic $W(p)$ triplet tempering on $H^\bullet_{\mathrm{reg}}$
(Adamović--Milas character-amplitude bound on $\phi_{0,1}$);
(F4$'$) super-complementarity canonical pairing
($\kappa + \kappa^! = \max(m,n)$ for super-Yangians on the
sub-Sugawara line: supertrace and Berezinian pairings coexist
without a programme-level canonicalisation);
(F6) the $\lambda_g$-conjecture residue at $g\ge3$ governing
Theorem~D all-genera clutching-uniqueness.
The former F2 (periodic-CDG all simply-laced types) and F3
(original-complex class~$\mathbf{M}$ chain-level, all three
equivalent ambients) and F5 (irregular-singular regularity
at $\overline{\cM}_{g,n}$) are closed in the 2026-04-17
wave by \texttt{thm:admissible-kl-bar-cobar-adjunction},
\texttt{thm:mc5-class-m-chain-level-pro-ambient}, and
\texttt{thm:irregular-singular-kzb-regularity} respectively.
```

### HEAL-2. Remove the "class (iii)" conditionality from the Part VII preamble.

**File:** `~/chiral-bar-cobar-vol2/main.tex`

**Lines 1704–1709.** Replace

```
(iii) higher-rung Platonic targets of the
$E_\infty^{\mathrm{top}}$-ladder $\cW_N \mapsto E_{N+1}^{\mathrm{top}}$
for $N \ge 3$, conditional on the higher-spin antighost
construction (Chapter~\ref{ch:e-infinity-topologization});
```

→

```
(iii) cross-volume scope-boundary items inherited from
Vol~I FRONTIER §3 and Vol~III CL-registers: $W(p)$ tempering on
$H^\bullet_{\mathrm{reg}}$, super-complementarity canonical pairing,
and the $\lambda_g$-conjecture residue at $g\ge3$. The
$\cW_N \mapsto E_{N+1}^{\mathrm{top}}$ rung of the
$E_\infty^{\mathrm{top}}$-ladder has been promoted to
theorem at all $N\ge3$ by
\texttt{thm:iterated-sugawara-construction} +
\texttt{thm:e-infinity-topologization-ladder}
(Chapter~\ref{ch:e-infinity-topologization}) and is no longer
a frontier item.
```

### HEAL-3. Bridge the "irreducible opens" closing paragraph to the residual three.

**File:** `~/chiral-bar-cobar-vol2/main.tex`

**Lines 1765–1769.** Append one sentence after

```
… are now closed on the non-degenerate locus; the programme's Platonic
form is realised.
```

→ add:

```
Beyond these four, the residual three directions F1$'$, F4$'$, F6
enumerated in the main abstract are genuinely open scope-boundary
items: they sit outside the logarithmic-to-non-logarithmic
transition (F1$'$), the super/bosonic-to-super-Yangian
canonicalisation (F4$'$), and the $g\ge3$ Faber socle-evaluation
residue (F6). They are not obstructions to the climax; they are
the three faces on which the three-volume programme meets the
boundary of its established scope.
```

### HEAL-4. Cross-reference the frontier chapters to their FRONTIER.md entries.

No source edit needed in this wave; the bridge is documented here and
should be propagated into a subsequent cross-volume sync commit that
updates `~/chiral-bar-cobar/FRONTIER.md` §3 with Vol II F1'/F4'/F6
entries aliased to the existing OF5/OF19/OF-AP225 labels. This keeps
the three-volume frontier register single-sourced.

## Russian-school voice audit

The proposed new text passes the AI-slop grep and the em-dash ban:
no "moreover", "notably", "furthermore"; no `---`; no hedging where
the mathematics is precise. The three residual frontiers are named
in the Drinfeld-compression register: one sentence each, scope
explicit, witness or conjectured status explicit. The Beilinson
falsification posture is preserved: the four closures carry
theorem-labels that can be grepped and independently verified; the
three opens carry conjecture-labels or explicit "open" tags.

## Refusal criteria tripwires

- Every line in HEAL-1/2/3 has been checked against the `AP29`
  banned-tokens list. Zero hits.
- The label `conj:f1-wp-tempering` exists at
  `chapters/examples/w-algebras-frontier.tex:1237` (grep-verified).
- The labels `thm:admissible-kl-bar-cobar-adjunction`,
  `thm:mc5-class-m-chain-level-pro-ambient`,
  `thm:irregular-singular-kzb-regularity`,
  `thm:iterated-sugawara-construction`,
  `thm:e-infinity-topologization-ladder`, and
  `prop:bv-bar-class-m-weight-completed` are live in Vol II (grep-
  verified across `chapters/theory/` and `chapters/connections/`).
- No `V1-thqg` phantom references are introduced. The
  `V1-sec:frontier-modular-holography-platonic` phantom at
  `main.tex:904` already absorbs consumer refs.

## Build cost

Text-only edits inside `main.tex` lines 1206–1218, 1704–1709, and
1770 (append-after). No label invalidation, no ref churn. Single
`make fast` pass expected to absorb the diff without cascading
errors.
